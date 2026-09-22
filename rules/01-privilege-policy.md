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

## 4. Protocolo de Aprovação Humana e Consentimento Informado (Human-in-the-Loop)

As IDEs (Antigravity, Cursor, Claude Code, VSCode) possuem barreiras de segurança nativas e invariáveis que solicitam autorização do usuário em inglês para execução de scripts de terminal.

Para garantir transparência e evitar que o operador seja surpreendido por diálogos genéricos:

### Regra 1: Proibição Estrita de Contorno via Shell Inline
- É **TERMINANTEMENTE PROIBIDO** disparar scripts Python inline (`python -c "from mcp_server..."`) via terminal (`run_command`) para executar comandos de rede ou forçar `privilege_level='full'`.
- Todas as execuções, testes de sintaxe e coletas em switches devem ocorrer **exclusivamente via Servidor MCP** (`execute_command`, `run_canonical_action`, `run_adhoc_action`). As chamadas de ferramentas MCP não disparam alertas confusos de shell no terminal da IDE.

### Regra 2: Briefing Prévio no Chat em Português
Sempre que for estritamente necessária uma ação de nível `editor` ou `full`, ou antes de executar qualquer comando no terminal que demande aprovação da IDE, o Agente **DEVE** emitir um aviso prévio no chat com a seguinte estrutura:

```markdown
> [!WARNING]
> ### Solicitação de Autorização Operacional
> - **Equipamento**: `<IP_OU_HOSTNAME>`
> - **Nível de Privilégio**: `EDITOR` ou `FULL`
> - **Comandos Solicitados**: `<COMANDO>`
> - **Justificativa Técnica**: `<MOTIVO_CLARO>`
> - **Impacto Estimado**: `<IMPACTO_NA_REDE>`
> 
> *A sua IDE exibirá a janela nativa de confirmação a seguir. Por favor, revise os dados acima e confirme a execução.*
```

---

## 5. Tratamento de Violações
Se um comando for bloqueado pelo Gatekeeper (`PrivilegeViolationError`), o Agente deve:
1. Interromper a execução imediatamente.
2. Informar o operador de forma clara sobre a recusa do Gatekeeper.
3. Não tentar burlar a sintaxe com apelidos, abreviações ou scripts no terminal.

---

## 6. Cofre de Credenciais e Perfis Dinâmicos (Credentials Vault & Profiles)

Para eliminar credenciais estáticas únicas e permitir segregação de acesso enterprise:

1. **Catálogo Declarativo**: As credenciais são cadastradas em `registry/credentials.yaml` (ignorado no git) com template em `registry/credentials.example.yaml`.
2. **Resolução de Segredos**:
   - `env:VAR_NAME`: resolve dinamicamente a partir de variáveis de ambiente.
   - `enc:TOKEN`: segredos criptografados localmente com chave Fernet de 32 bytes (via `python -m mcp_server.vault --encrypt <senha>`).
3. **Isolamento e Mascaramento Estrito**:
   - É **expressamente proibido** retornar, logar ou exibir senhas em texto claro.
   - A ferramenta `list_credential_profiles` e o comando `/profiles` sempre mascaram as senhas como `********`.
4. **Seleção de Perfil**:
   - O operador pode especificar o perfil desejado no prompt (ex: *"usando o perfil zabbix"* ou *"com o usuário admin"*).
   - O Agente repassa o perfil escolhido via argumento `credential_profile="<nome>"`.
   - Na ausência de indicação, o perfil padrão (`default_profile`) é adotado transparentemente.

