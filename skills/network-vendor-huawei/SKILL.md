---
name: network-vendor-huawei
description: Base de conhecimento especializada do sistema operacional Huawei VRP (roteadores NE40E, NetEngine, switches CloudEngine e S-Series).
---

# Vendor Skill: Huawei VRP

O Huawei Versatile Routing Platform (VRP) utiliza primordialmente a palavra-chave `display` para comandos de leitura e inspeção.

## 1. Padrões de Prompt e Conexão
- **Modo Usuário**: `<HUAWEI>`, `<BORDER-01-NE40E>`
- **Modo Sistema**: `[HUAWEI]`, `[~HUAWEI]`
- **Desativação de Pager**: `screen-length 0 temporary` (não usar `screen-length 0` definitivo).

## 2. Comandos Canônicos Mapeados

### Versão de Software e Uptime
- **Comando Real**: `display version`
- **Campos Típicos**: `VRP (R) software, Version 8.180`, `uptime is 120 days...`, `Patch Version: ...`

### Hardware e Placas
- **Comando Real**: `display device` ou `display elabel`
- **Exemplo de Retorno**:
  ```text
  Slot #    Type       Online    Register      Status      Primary
  ----------------------------------------------------------------------
  1         LPU        Present   Registered    Normal      NA
  9         MPU        Present   Registered    Normal      Master
  ```

### Interfaces
- **Resumo**: `display ip interface brief`
- **Detalhes de Interface**: `display interface {interface_name}` (ex: `display interface GigabitEthernet1/0/2`)
- **Status Operacional**: `Physical: up/down`, `Protocol: up/down`, `*down` (administrativamente desativada).

### BGP
- **Resumo de Peers**: `display bgp peer`
- **Contadores de Prefixos**: Campo `PrefRcv` e estado `Established`.
