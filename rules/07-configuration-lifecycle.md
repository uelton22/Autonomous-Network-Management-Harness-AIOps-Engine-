# Regra 07: Ciclo de Vida de Comandos de Configuração e Mutação (Editor / Full)

Esta política estabelece os padrões e garantias que o **Agente Autônomo de Redes (AIOps Agent)** deve seguir estritamente sempre que for solicitada a execução de qualquer comando ou ação que altere o estado de um equipamento de rede (privilégios `editor` ou `full`).

---

## 1. Princípio "Inspect Before Alter" (Pre-Flight Check Obrigatório)

> [!IMPORTANT]
> **NUNCA ALTERE UM EQUIPAMENTO ÀS CEGAS**: Nenhuma alteração de estado (criação, edição ou exclusão de usuários, interfaces, VLANs, rotas BGP/OSPF, ACLs ou serviços VPWS) pode ser submetida sem uma verificação prévia do estado atual.

### Procedimento de Pre-Check:
1. **Identificação do Alvo**: Antes de enviar o comando de configuração, o agente executa uma coleta de leitura (`read`) correspondente (ex: `get_system_users`, `get_l3_interfaces`, `get_vlans`).
2. **Avaliação de Idempotência**:
   - Se o recurso a ser alterado já possui os parâmetros desejados, o agente avisa o operador que o estado já é o esperado e encerra a ação sem disparar comandos no switch.
3. **Validação de Pré-requisitos**:
   - Se o operador pedir *"Mude o grupo do usuário 'noc_user' para admin"*, mas a inspeção demonstrar que o usuário não existe, o agente **NÃO deve gerar comandos de erro**. Ele interrompe o fluxo e pergunta se o operador deseja criá-lo.
   - Se o operador pedir *"Atribua o IP 10.0.0.1/30 na interface Gi1/0/1"*, a inspeção deve checar se a interface já está ocupada ou se a sub-rede já está alocada em outra interface/VLAN.

---

## 2. Governança de Parâmetros Mandatórios

Se a intenção do operador estiver incompleta ou faltarem parâmetros obrigatórios da sintaxe oficial do fabricante:
1. O agente consulta a documentação oficial via `search_command_reference(vendor, query)`.
2. Ao detectar parâmetros obrigatórios ausentes (ex: senha para novo usuário, máscara de sub-rede para IP, VLAN ID):
   - **O AGENTE DEVE PARAR E PERGUNTAR NO CHAT**:
   - É terminantemente proibido inventar valores padrão críticos (como senhas aleatórias ou máscaras arbitrárias) sem consentimento do operador.
   - Apresente no chat a explicação clara da sintaxe exigida pelo fabricante e solicite os dados faltantes.

---

## 3. Execução em Bloco e Contexto Único de Sessão

1. Comandos de configuração não podem ser disparados fragmentados em múltiplas sessões SSH desconexas.
2. Todo o bloco transacional (ex: entrar na interface, aplicar descrição, atribuir IP, habilitar porta) é enviado em **bloco único** via `send_config_set()` dentro da mesma conexão.
3. Para plataformas com candidate datastore (Datacom DmOS e Huawei VRP V800), o bloco deve prever o comando `commit` de confirmação ou solicitar confirmação explícita do operador antes do commit.

---

## 4. Análise Mandatória de Erros da CLI

1. O switch físico não retorna códigos HTTP. Todo feedback reside na resposta textual da CLI (`%`, `Error:`, `Unrecognized command`, `syntax error`).
2. O retorno da ferramenta conterá `errors_detected` e `is_success`.
3. Se `has_errors: True` ou se o switch rejeitar uma linha:
   - O agente **NUNCA** deve dizer que a configuração foi um sucesso.
   - Ele deve extrair o erro específico retornado pelo switch (ex: `% 10.0.0.0 overlaps with Vlan100`) e explicar didaticamente ao operador o motivo da rejeição e sugerir a ação corretiva.

---

## 5. Trilha de Auditoria Imutável (`storage/audit_log/`)

1. Todas as alterações executadas são salvas automaticamente em `storage/audit_log/` com ID único de auditoria (`audit_id`), timestamp ISO, perfil SSH, linhas executadas e saída da caixa.
2. O agente deve referenciar o `audit_id` ao prestar contas da alteração ao operador humano no chat.
