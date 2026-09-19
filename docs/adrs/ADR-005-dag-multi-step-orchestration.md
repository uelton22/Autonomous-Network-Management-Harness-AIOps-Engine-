# ADR-005: Orquestração Multietapa em DAG de Comandos Dependentes

## Status
Aprovado

## Contexto
Investigações de incidentes de rede frequentemente dependem do resultado de um comando prévio (ex: identificar quais portas estão com problema antes de puxar contadores detalhados de ótica ou erros de CRC). Executar comandos monolíticos detalhados em todas as portas é proibitivo.

## Decisão
Adotar o modelo de **Grafos Acíclicos Dirigidos (DAG)** composto por Ações Atômicas:
1. **Ação Atômica de Resumo**: Coleta compacta (`display ip interface brief` / `show interface brief`).
2. **Filtro Determinístico em Código**: Filtra portas com anomalia (`status == 'DOWN'`) localmente, sem gastar tokens de IA.
3. **Loop Granular**: Dispara `get_interface_detail` apenas para as portas afetadas.
4. **Reuso de Templates**: O template TTP granular é executado em loop com 100% de cache hit no Tier 1.
5. **Agregador Canônico**: Consolidação de todos os dados sob o schema `OpenConfigInterfacesSchema`.

## Consequências
- Foco absoluto da coleta nos pontos de falha.
- Redução drástica do tráfego SSH no equipamento e da quantidade de dados processados.
