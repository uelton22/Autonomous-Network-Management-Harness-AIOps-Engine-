---
name: ttp-self-healing
description: Guia de síntese, validação em sandbox e auto-cura de templates TTP (Template Text Parser) com feedback loop Pydantic.
---

# Procedimento de Auto-Cura de Templates TTP (Self-Healing Loop)

Quando ocorrer um **Cache Miss** ou falha de parsing no Tier 1:

## 1. Amostragem de Dados (Chunk Sampling)
Nunca passe o dump completo para a LLM. Execute o sampling estrutural:
1. Pressione as primeiras 15 linhas (cabeçalhos de tabela e metadados).
2. Localize um bloco repetitivo (ex: 2 interfaces ou 2 peers BGP) e capture 20 a 30 linhas.
3. Capture as últimas 10 linhas (totais e estatísticas finais).

## 2. Síntese do Template TTP
Formule o prompt para a LLM com:
- Vendor e família de SO identificados na fase de Fingerprinting.
- Ação canônica esperada (ex: `get_interface_summary`).
- Recorte estrutural amostrado.
- JSON Schema Pydantic do modelo alvo.
- Erro da tentativa anterior (se houver).

### Regras de Sintaxe TTP
- Use `<group name="...">` compatível com a estrutura de lista ou dicionário do schema.
- Use filtros TTP: `{{ variable | ORPHRASE }}`, `{{ counter | DIGIT }}`, `{{ ip | IP }}`.
- Mantenha os nomes das variáveis idênticos aos campos do Schema Pydantic.

## 3. Teste em Sandbox Local (Sem LLM)
1. Carregue o arquivo `.raw` integral gravado em disco (`storage/raw/...`).
2. Execute o template gerado no parser TTP local.
3. Se o retorno for vazio:
   - Incrementar contador de retentativa.
   - Enviar feedback à LLM com: `"Template retornou lista vazia. Verifique regex e tags de grupo."`
4. Se retornar registros:
   - Validar contra `schema_cls.model_validate(...)`.
   - Se disparar `ValidationError`:
     - Capturar a mensagem e o diff do erro.
     - Enviar de volta à LLM para correção cirúrgica (máximo 3 tentativas).

## 4. Aprovação e Promoção para o Cache
Uma vez aprovado na validação Pydantic:
1. Gravar o template em `storage/templates/{action}/{vendor_os}__{major_version}.ttp`.
2. Registrar no log de auditoria do Agente.
3. A partir deste momento, todas as próximas coletas executarão no **Tier 1 (< 5ms)**.
