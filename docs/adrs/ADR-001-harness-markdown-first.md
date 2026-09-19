# ADR-001: Harness Orientado a Arquivos (Markdown/YAML First)

## Status
Aprovado

## Contexto
Sistemas de automação de rede tradicionais implementam toda a lógica de negócio em código Python procedural/orientado a objetos rígido. Quando novos comandos de fabricantes ou alterações de políticas surgem, engenheiros de rede precisam alterar código-fonte, lidar com dependências e arriscar quebras de regressão.

## Decisão
Adotar uma arquitetura **Harness Orientada a Arquivos (Agent-First)**:
1. Toda a inteligência, políticas de segurança, catálogo de comandos e fluxos de diagnóstico são expressos em arquivos Markdown (`.md`), YAML (`registry/actions.yaml`) e JSON Schemas.
2. A sessão de IA (Cursor, Claude Code, Antigravity, Codex) consome diretamente esses arquivos como contexto vivo.
3. O único código da plataforma é o servidor MCP SSH em Python e o motor local de execução/validação TTP.

## Consequências
- **Positivas**:
  - Engenheiros de rede podem adicionar suporte a novos comandos ou fabricantes apenas editando `registry/actions.yaml` e as Vendor Skills, sem tocar em código Python.
  - Portabilidade total entre diferentes ambientes de IA e IDEs.
  - Auditoria simplificada por versionamento Git de arquivos declarativos.
- **Mitigações**:
  - Exige schemas JSON rígidos para garantir que o resultado final seja determinístico.
