---
name: device-fingerprinting
description: Procedimento operacional padrão para identificação progressiva (Zero-Knowledge) de equipamentos de rede multi-vendor sem credenciais pré-configuradas.
---

# Procedimento de Descoberta Progressiva (Zero-Knowledge Fingerprinting)

Quando o operador fornecer apenas um endereço IP ou nome de host:

## Etapas de Execução

### Nível 1: Banner Grab Pré-Autenticação (TCP Socket Porta 22)
1. Conectar ao socket TCP na porta 22 antes de enviar credenciais SSH.
2. Capturar os primeiros 256 bytes enviados pelo daemon SSH.
3. Avaliar padrões:
   - `SSH-2.0-Huawei-*` $\rightarrow$ Vendor: `huawei`, OS: `vrp`, Version: extraída do sufixo.
   - `SSH-2.0-Datacom-*` ou `DmOS` $\rightarrow$ Vendor: `datacom`, OS: `dmos`, Version: extraída do sufixo.
   - `SSH-2.0-Cisco-*` $\rightarrow$ Vendor: `cisco`, OS: `ios-xe`.

### Nível 2: Análise de Prompt no Handshake SSH
Se o banner for genérico (ex: `SSH-2.0-OpenSSH`):
1. Iniciar autenticação SSH básica com credenciais de monitoramento.
2. Avaliar caracteres de prompt recebidos:
   - `<...>` ou `[...]` $\rightarrow$ **Huawei VRP**
   - `DM...#` ou `DmOS#` ou `user@host#` $\rightarrow$ **Datacom DmOS**
   - `hostname#` ou `hostname>` $\rightarrow$ **Cisco IOS / IOS-XE**

### Nível 3: Probing CLI Determinístico
Se o prompt for ambíguo:
1. Enviar comando neutro de leitura:
   - Teste 1: `display version | include VRP`
     - Se retornar dados de versão $\rightarrow$ Confirma **Huawei VRP**.
   - Teste 2: `show firmware` ou `show platform`
     - Se retornar informações de cards $\rightarrow$ Confirma **Datacom DmOS**.
   - Teste 3: `show version`
     - Se retornar IOS Software $\rightarrow$ Confirma **Cisco**.

### Cache de Metadados
Armazenar o resultado em cache com chave `host` e TTL de 24 horas:
`{ "vendor": "datacom", "os_family": "dmos", "major_version": "12_0_2" }`
