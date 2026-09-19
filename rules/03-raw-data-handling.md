# Diretriz de Tratamento e Isolamento de Arquivos .raw

Esta regra define a política inegociável de persistência e isolamento de saídas brutas de CLI (`.raw`).

---

## 1. A Regra Fundamental: Nunca Enviar .raw Integral à LLM nem Ler Manualmente
Saídas de comandos de rede como `display interface`, `show lldp neighbors` ou `show running-config` frequentemente atingem de centenas a dezenas de milhares de linhas.
- **Proibição de Bypass**: O Agente está terminantemente PROIBIDO de ler diretamente arquivos `.raw` salvos em `storage/raw/` (usando `view_file`, `cat`, `head`, etc.) para tentar interpretar a resposta no olho humano/LLM.
- **Isolamento de Texto**: O conteúdo integral de um arquivo `.raw` jamais deve ser injetado diretamente no prompt da LLM. O servidor MCP não expõe o texto cru de saídas operacionais.
- **Consequências evitadas**: Efeito *lost in the middle*, alucinação de dados críticos de telecom (endereços IP, VLANs, status de enlace) e estouro de contexto/custo desnecessário.

---

## 2. Ciclo Obrigatório de Parsing via Templates TTP
1. **Gravação Imediata**: O servidor MCP grava a saída completa do SSH em `storage/raw/{hostname}_{timestamp}_{action}.raw`.
2. **Proibição de Leitura Direta**: O Agente recebe apenas metadados técnicos (`raw_path`, `line_count`, `bytes_count`).
3. **Parsing Estruturado Obrigatório**:
   - Para comandos catalogados em `actions.yaml`, invoque `run_canonical_action`.
   - Para comandos ad-hoc ou não catalogados, invoque `run_adhoc_action(host, command, action_name)`.
4. **Chunk Sampling para Auto-Cura (Tier 2)**:
   - Caso o template TTP precise ser gerado pela LLM (Tier 2), aplica-se `extract_representative_sample`:
     - Cabeçalho: 15 linhas
     - Corpo estrutural: ~20 a 30 linhas (ex: 2 vizinhos LLDP ou 2 interfaces)
     - Rodapé: 10 linhas
   - O restante do arquivo é omitido no prompt.
5. **Execução no Sandbox e Promoção**: O template TTP gerado é testado pelo motor local contra o `.raw` **integral** salvo em disco, promovido para `storage/templates/{action_name}/` e os dados são entregues à LLM **exclusivamente em JSON estruturado**.
