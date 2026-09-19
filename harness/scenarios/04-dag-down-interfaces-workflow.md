# Cenário de Teste 04: Orquestração Multietapa DAG (Diagnóstico de Interfaces DOWN)

## Objetivo
Validar a execução de um DAG de comandos dependentes: coleta resumida $\rightarrow$ filtro determinístico sem LLM $\rightarrow$ coleta detalhada apenas nas portas afetadas $\rightarrow$ agregação OpenConfig e diagnóstico preciso.

## Prompt do Operador no Chat
> "Audite as interfaces no switch no IP 100.75.9.252 e me dê um diagnóstico das portas com problema."

## Comportamento Esperado do Agente
1. Invocar `run_workflow_dag(host="100.75.9.252", workflow_name="diagnose_down_interfaces")`.
2. **Passo 1**: O MCP executa `show interface status` / `show interface brief` $\rightarrow$ TTP extrai as interfaces e seus status operacionais.
3. **Passo 2**: Filtro determinístico em código local identifica as interfaces com `oper_status == 'DOWN'`.
4. **Passo 3**: O MCP dispara a coleta granular detalhada (`show interface <nome>`) apenas nas portas com problema.
5. **Passo 4**: Agregador consolida os dados no modelo `OpenConfigInterfacesSchema`.
6. O Agente apresenta a conclusão ao operador com tabela resumida das portas caídas e causa provável.
