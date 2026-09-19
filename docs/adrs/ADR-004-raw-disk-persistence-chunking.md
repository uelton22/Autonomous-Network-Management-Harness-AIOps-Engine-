# ADR-004: Persistência de .raw em Disco e Chunk Sampling

## Status
Aprovado

## Contexto
Dumps de switches com centenas de interfaces ultrapassam 25.000 linhas. Injetar isso em modelos de linguagem satura o contexto, aumenta a latência e causa o efeito *lost in the middle*, no qual a LLM omite portas ou alucina dados no meio do dump.

## Decisão
1. **Persistência Obrigatória em Disco**: O servidor MCP grava a saída bruta do comando em `storage/raw/{host}_{timestamp}_{action}.raw` e retorna apenas o caminho do arquivo e metadados ao agente.
2. **Chunk Sampling**: Quando o gerador de templates TTP precisar de contexto, extrai-se apenas uma amostra estrutural representativa (cabeçalho de 15 linhas, bloco de repetição de 20 linhas e rodapé de 10 linhas).
3. O parser TTP roda localmente em cima do `.raw` integral no disco.

## Consequências
- A LLM nunca recebe payloads de dezenas de milhares de linhas.
- Preservação da evidência forense em disco para auditoria de rede.
