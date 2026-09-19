# Orquestração Multietapa (DAGs de Comandos Dependentes e Agregação)

Esta regra orienta a decomposição de investigações complexas de rede em Grafos Acíclicos Dirigidos (DAGs) de ações atômicas.

---

## 1. Princípio da Decomposição Atômica
Nunca execute coletas monolíticas e pesadas para tentar responder a uma pergunta ampla.
- **Abordagem Incorreta**: Executar `display interface` ou `show interface` geral para 500 portas e tentar processar tudo de uma vez.
- **Abordagem Correta (DAG)**:
  1. Executar ação atômica de resumo (`get_interface_summary` via `display ip interface brief` ou `show interface brief`).
  2. Filtrar localmente em código determinístico as entidades com problema (ex: `oper_status == 'DOWN'`).
  3. Executar ações atômicas granulares (`get_interface_detail` com `{interface_name}`) apenas para as entidades selecionadas.
  4. Agregar os resultados em um único schema canônico OpenConfig.

---

## 2. Reuso de Templates TTP Granulares
- O template TTP para `get_interface_detail` é universal para qualquer interface daquela família de SO.
- Ao executar o detalhe em lote para 3 interfaces caídas, o mesmo template é reaproveitado 3 vezes, usufruindo de **100% de cache hit no Tier 1 (< 5ms)**.

---

## 3. Papel da LLM no Fluxo DAG
- A LLM **não** deve ser utilizada para filtrar listas (ex: selecionar portas DOWN). Isso é trabalho de código local rápido e determinístico.
- A LLM entra em dois momentos específicos:
  1. Sintetizar um template TTP caso ocorra Cache Miss em Tier 2.
  2. Redigir a conclusão diagnóstica final em linguagem natural ao operador com base no payload JSON OpenConfig agregado.
