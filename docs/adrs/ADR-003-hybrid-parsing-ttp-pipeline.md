# ADR-003: Pipeline Híbrido de Parsing TTP (Tier 1 < 5ms, Tier 2 Auto-Cura, Tier 3 Pydantic)

## Status
Aprovado

## Contexto
Fazer parsing de saídas CLI utilizando exclusivamente LLMs é lento (segundos a minutos) e consome tokens caros. Por outro lado, parsers puramente manuais (Regex / TextFSM) quebram frequentemente com atualizações de firmware.

## Decisão
Implementar o pipeline híbrido de 3 níveis:
- **Tier 1 (Fast-Path < 5ms)**: TTP determinístico executado localmente a partir de templates cacheados em `storage/templates/`.
- **Tier 2 (Fallback & Auto-Cura)**: Em caso de Cache Miss ou alteração de layout, a LLM sintetiza um novo template TTP com auxílio da Vendor Skill e validação em Sandbox local contra o `.raw` integral, repetindo até 3 vezes com feedback de erro. O template aprovado é promovido ao cache.
- **Tier 3 (Strict Validation)**: Validação em schemas Pydantic OpenConfig para garantir 100% de acurácia matemática.

## Consequências
- 99% das coletas repetitivas rodam em menos de 5ms sem custo de tokens.
- O sistema se auto-cura diante de novas versões de firmware de forma transparente e audita os novos templates.
