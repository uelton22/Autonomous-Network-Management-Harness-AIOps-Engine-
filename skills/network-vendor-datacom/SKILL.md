---
name: network-vendor-datacom
description: Base de conhecimento especializada do sistema operacional Datacom DmOS (switches DM4000, DM4100, DM4200, DM4300, DM4600).
---

# Vendor Skill: Datacom DmOS

O Datacom DmOS é um sistema operacional com sintaxe proprietária que frequentemente induz modelos de linguagem a alucinar sintaxes do Cisco IOS. Esta skill documenta os comandos reais e comportamentos do DmOS.

## 1. Padrões de Prompt e Conexão
- **Prompt Padrão**: `DM4610#`, `DM4370#`, `DmOS#`, ou `user@hostname#`.
- **Modo de Configuração**: `DM4610(config)#` (exige `commit` para efetivar).
- **Desativação de Pager**: `terminal length 0` (obrigatório em sessões de automação).

## 2. Comandos Canônicos Mapeados

### Versão de Software e Firmware
- **Comando Real**: `show firmware` ou `show platform`
- **Nota Crítica**: `show version` no DmOS exibe apenas resumo de processo; para detalhes de versão de software instalada nos bancos e placas usa-se `show firmware`.

### Modelo de Hardware e Chassis
- **Comando Real**: `show platform | include DM` ou `show platform`
- **Exemplo de Retorno**:
  ```text
  Chassis/Slot Product model Role   Status Firmware version
  ------------ ------------- ------ ------ ----------------------
  1            DM4610        -      -      12.0.2
  1/1          8GPON+8GX+2XS Master Ready  12.0.2-build482
  ```

### Uptime e Recursos do Sistema
- **Comando Real**: `show system uptime` e `show system`
- **Nota**: `show system` exibe uso de CPU, memória e motivo do último reboot.

### Resumo e Detalhes de Interfaces
- **Resumo**: `show interface brief`
- **Detalhes de Interface**: `show interface {interface_name}` (ex: `show interface 1/1/1`)
- **Contadores**: Exibe pacotes, bytes, CRC errors e last link flap.

### Roteamento e BGP
- **Resumo BGP**: `show ip bgp summary` ou `show bgp summary`
- **Tabela de Rotas**: `show ip route` ou `show ip route summary`
