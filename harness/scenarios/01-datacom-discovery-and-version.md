# Cenário de Teste 01: Descoberta Zero-Knowledge e Versão Datacom DmOS

## Objetivo
Verificar se o Agente descobre corretamente a plataforma de um switch Datacom (ex: DM4770 / DmOS) no IP fornecido e executa o comando real `show firmware`, sem alucinar sintaxes do Cisco IOS.

## Prompt do Operador no Chat
> "Qual é o firmware e modelo do switch no IP 100.75.9.252?"

## Comportamento Esperado do Agente
1. Chamar `discover_device(host="100.75.9.252")` $\rightarrow$ Retorna `vendor: "datacom"`, `os_family: "dmos"`.
2. Consultar `registry/actions.yaml` $\rightarrow$ Identifica `show firmware` e `show inventory` / `show platform`.
3. Invocar `run_canonical_action(host="100.75.9.252", action="get_system_version", privilege_level="read")`.
4. O servidor MCP grava `storage/raw/100_75_9_252_..._show_firmware.raw`.
5. O parser TTP extrai os dados e valida contra `DeviceInfoSchema`.
6. Responder com tabela clara informando:
   - **Hostname / IP**: `100.75.9.252`
   - **Vendor**: `datacom`
   - **Modelo**: `DM4770`
   - **Versão de Firmware**: `12.0.2`
