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

### Link Aggregation (Eth-Trunk)
- **Resumo**: `display eth-trunk`
- **Detalhes**: `display eth-trunk {id}`
- **Membros**: Interfaces físicas agrupadas com status `Selected` ou `Unselect`.

### Usuários e Sessões
- **Contas Locais**: `display local-user`
- **Sessões Conectadas**: `display users`

### LLDP (Vizinhança)
- **Vizinhos**: `display lldp neighbor brief`

---

## 3. Documentação Oficial e Referência Multi-Versão

Os manuais oficiais de comandos da Huawei estão indexados em `command_reference/huawei/` particionados por versão de SO (ex: `command_reference/huawei/V200R011C10/`).

Sempre que precisar consultar sintaxes ou parâmetros específicos de VRP, consulte a tool MCP:
```python
search_command_reference(vendor="huawei", query="display eth-trunk", version="v200", read_only=True)
```
- **Versões Suportadas no Repositório**:
  - `V200R011C10` (Switches S1720, S2700, S5700, S6720)
  - `V600` / `V800` (Roteadores NE40E, NetEngine, switches CloudEngine - em expansão)

