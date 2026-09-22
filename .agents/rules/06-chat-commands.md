# Regra de Comandos do Chat (Harness Chat Commands)

Esta regra orienta o Agente a interpretar e responder instantaneamente a comandos rápidos e atalhos iniciados com barra (`/`) enviados pelo operador humano no chat.

---

## Mapeamento de Comandos Rápidos

| Comando | Intenção / Ação | Ferramenta / Fonte | Comportamento Esperado no Chat |
| :--- | :--- | :--- | :--- |
| **`/profiles`** ou **`/profile`** | Listar perfis do cofre | `list_credential_profiles()` ou `registry/credentials.yaml` | Renderiza tabela com Nome, Usuário, Porta, Status e Descrição com senhas mascaradas (`********`). |
| **`/cisco <termo>`** | Pesquisar manual oficial Cisco | `search_command_reference("cisco", termo)` | Busca comandos IOS na pasta `command_reference/cisco/` e exibe sintaxes e modos. |
| **`/datacom <termo>`** | Pesquisar manual oficial Datacom | `search_command_reference("datacom", termo)` | Busca comandos DmOS em `command_reference/datacom/` e exibe sintaxes e modos. |
| **`/huawei <termo>`** | Pesquisar manual oficial Huawei | `search_command_reference("huawei", termo)` | Busca comandos VRP em `command_reference/huawei/` com resolução de versão. |
| **`/actions`** | Catálogo de ações canônicas | `registry/actions.yaml` | Renderiza tabela com todas as ações suportadas, privilégios e plataformas. |
| **`/vault`** | Status de segurança do cofre | `mcp_server.vault` | Exibe quantidade de perfis, tipo de criptografia ativa (Fernet) e variáveis de ambiente. |
| **`/help`** | Ajuda e guia operacional | Diretrizes do Harness | Exibe comandos rápidos e exemplos de perguntas em linguagem natural. |

---

## Diretrizes de Execução no Chat

1. **Resposta Imediata sem Hesitação**:
   Quando a mensagem do operador for exatamente `/profiles` (ou outro comando `/...`), não pergunte o que o operador quer nem peça esclarecimentos. Execute e apresente a resposta de forma direta e visual.

2. **Isolamento e Segurança de Senhas**:
   - Em nenhuma hipótese exiba senhas descriptografadas ou senhas em texto claro no chat.
   - Sempre use `********`.

3. **Contexto de Uso**:
   Sempre informe ao final como o operador pode usar a informação recém-exibida nas perguntas subsequentes (ex: *"Para utilizar qualquer perfil, mencione no chat: `identifique o switch X usando perfil Y`"*).
