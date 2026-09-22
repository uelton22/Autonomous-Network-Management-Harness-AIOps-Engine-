---
name: profiles
description: Exibe os perfis de credenciais SSH do cofre (Vault) cadastrados no projeto quando o usuário digita /profiles ou pergunta sobre perfis e autenticação.
---

# Skill: Perfis de Credenciais SSH (Vault)

Esta habilidade é ativada quando o operador:
- Digita `/profiles` ou `/profile` no chat;
- Pergunta quais perfis de autenticação ou credenciais existem no cofre;
- Solicita listar, verificar ou alternar credenciais de conexão SSH.

---

## Procedimento Operacional

### 1. Obtenção dos Dados
Invoque a ferramenta MCP `list_credential_profiles()`.
Se a ferramenta MCP não estiver disponível na interface atual, obtenha os perfis diretamente instanciando `VaultManager()` de `mcp_server/vault.py` ou lendo `registry/credentials.yaml`.

### 2. Formato Obrigatório de Resposta no Chat
Apresente os perfis em formato de tabela Markdown clara e executiva:

```markdown
### 🔐 Perfis de Credenciais SSH Cadastrados no Cofre (Vault)

| Perfil | Usuário | Porta | Senha | Chave SSH | Status / Padrão | Descrição |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **zabbix** | `zabbix` | 22 | `********` | - | `(default)` | Perfil de telemetria e leitura |
| **admin** | `admin` | 22 | `********` | - | - | Perfil administrativo |
```

### 3. Regras Inegociáveis de Segurança
1. **Zero Clear-text Passwords**: **JAMAIS** exiba senhas ou secrets em texto claro. O campo de senha deve ser sempre mascarado como `********`.
2. **Indicação do Padrão**: Destaque qual perfil é o `default_profile` configurado.

### 4. Instruções de Uso para o Operador
Finalize com um guia rápido de como usar no chat:
- **Conectar com perfil específico**: *"Para usar um perfil em uma consulta, basta solicitar: `Conecte ao switch 100.75.9.252 usando o perfil admin`."*
- **Gerenciar perfis**: *"Para adicionar novos perfis ou alterar credenciais, edite o arquivo `registry/credentials.yaml`."*
- **Criptografar senhas**: *"Para criptografar uma senha com Fernet no terminal: `python3 -m mcp_server.vault --encrypt <senha>`."*
