# ADR-002: Gatekeeper de Privilégios em 3 Níveis (read, editor, full)

## Status
Aprovado

## Contexto
Permitir que uma LLM envie comandos diretamente a switches de produção via SSH sem controle rigoroso cria risco de apagão (ex: a LLM inferir um comando de reboot, commit ou shutdown de interface crítica durante um diagnóstico).

## Decisão
Implementar um **Gatekeeper Determinístico em 3 Níveis** diretamente no servidor MCP SSH:
1. **`read` (Padrão)**: Apenas inspeção (`show *`, `display *`, `dir`, `ping`, `traceroute`). Bloqueia categoricamente modo de configuração, gravação e comandos destrutivos.
2. **`editor`**: Permite comandos operacionais e alterações pontuais previamente autorizadas (ex: descrição de interface), mas bloqueia reboots, wipe de flash ou modificações em usuários AAA.
3. **`full`**: Permite execução irrestrita, exigindo confirmação explícita do operador.

## Consequências
- A validação ocorre em Python antes de qualquer pacote SSH ser transmitido ao equipamento.
- Tentativas de evasão de privilégio geram `PrivilegeViolationError` imediato com auditoria.
