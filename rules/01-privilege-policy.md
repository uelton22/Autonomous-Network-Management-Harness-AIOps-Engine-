# Política de Privilégios de Execução (3 Níveis)

Esta regra define o modelo de segurança e controle de execução do Agente de Rede.

## Princípio do Menor Privilégio
O Agente deve sempre operar no menor nível de privilégio suficiente para atender à solicitação do usuário. O nível padrão é estritamente **`read`**.

---

## Os Três Níveis de Privilégio

### 1. Nível `read` (Auditoria e Inspeção - Padrão)
- **Objetivo**: Coleta de telemetria, verificação de status operacional e auditoria.
- **Comandos Permitidos**:
  - `show *` (Datacom DmOS, Cisco IOS-XE)
  - `display *` (Huawei VRP)
  - `dir *`
  - `ping *`, `traceroute *`, `tracert *`
- **Comandos Proibidos (Bloqueio Imediato)**:
  - Entrada em modo de configuração: `system-view`, `sys`, `config`, `configure terminal`.
  - Mutação de estado: `reboot`, `reset`, `reload`, `shutdown`, `undo *`, `no *`.
  - Escrita em memória ou disco: `save`, `write`, `commit`.
  - Destrutivos: `format`, `erase`, `delete`, `factory-default`.

### 2. Nível `editor` (Operador / Configuração Pontual Controlada)
- **Objetivo**: Manutenção operacional e configurações de baixo impacto previamente autorizadas.
- **Comandos Permitidos**:
  - Todas as ações do nível `read`.
  - Configurações pontuais: alteração de descrição de interfaces, `shutdown`/`undo shutdown` em portas de teste em homologação.
- **Comandos Proibidos**:
  - Reinicialização de sistema: `reboot`, `reload`, `power-off`.
  - Apagamento total: `format`, `erase flash`, `factory-default`.
  - Alteração de segurança: `undo aaa`, alteração de usuários e senhas de administração.

### 3. Nível `full` (Administrador / Superuser)
- **Objetivo**: Alterações estruturais, upgrades de firmware ou rotinas de emergência.
- **Condição Obrigatória**: Exige solicitação explícita do operador humano no chat com justificativa técnica.

---

## Tratamento de Violações
Se um comando for bloqueado pelo Gatekeeper (`PrivilegeViolationError`), o Agente deve:
1. Interromper a execução imediatamente.
2. Informar o operador de forma clara sobre a recusa do Gatekeeper.
3. Não tentar burlar a sintaxe com apelidos ou abreviações.
