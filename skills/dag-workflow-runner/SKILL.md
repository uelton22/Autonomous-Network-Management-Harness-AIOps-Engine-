---
name: dag-workflow-runner
description: Procedimento operacional para encadeamento e orquestração de workflows DAG de comandos dependentes com agregação OpenConfig.
---

# Procedimento de Execução de Workflows DAG

Este procedimento estabelece como o Agente executa investigações multietapa sem sobrecarregar a rede ou a LLM.

## Exemplo Canônico: `diagnose_down_interfaces`

### Etapa 1: Coleta Geral Resumida
1. Chamar a ação atômica `get_interface_summary`.
2. O servidor MCP executa o comando leve (`display ip interface brief` ou `show interface brief`).
3. O TTP extrai a lista intermediária com `name`, `admin_status` e `oper_status`.

### Etapa 2: Filtro Determinístico em Código (Zero Tokens)
1. Aplicar a condição de filtro:
   `down_interfaces = [i for i in interfaces if i['oper_status'] == 'DOWN']`
2. Se `down_interfaces` for vazio:
   - Encerrar o workflow com status de integridade OK.
   - Retornar ao operador: *"Todas as interfaces estão operacionais UP."*

### Etapa 3: Loop Batch de Coleta Detalhada
1. Para cada interface identificada como DOWN:
   - Chamar `get_interface_detail(interface_name=down_iface['name'])`.
   - O servidor MCP executa `display interface <nome>` ou `show interface <nome>`.
   - O parser reutiliza o mesmo template granular `get_interface_detail.ttp`.
2. Coletar estatísticas detalhadas: CRC errors, discards, last flapped.

### Etapa 4: Agregação Canônica OpenConfig
1. Mesclar os dados do resumo com os detalhes coletados em um único payload estruturado conforme `registry/schemas/interfaces.json`.
2. Entregar o JSON consolidado para a LLM final responder em linguagem natural com a causa-raiz precisa.
