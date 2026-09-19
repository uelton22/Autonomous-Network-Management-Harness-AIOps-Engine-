# Capítulo 7: MPLS

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## Infra

### `show mpls forwarding-table`

> **Página:** 1002 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Show list of MPLS entries installed on data plane.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls forwarding-table [ prefix-or-tnl-name ipv4-prefix or tunnel-name | action action | in-label label | in-protocol protocol | out-label label | out-protocol protocol | outgoing-interface l3-interface | status status ]
```

**Parameters:**

- `prefix-or-tnl-name ipv4-prefix or tunnel name` — Use IP prefix or tunnel name to filter the output. — *Valores:* a.b.c.d/x | string · *Default:* N/A
- `action action` — Use Action to filter the output. — *Valores:* none | fwd | psh | pop | php | swp · *Default:* N/A
- `in-label label` — Use In Label to filter the output. — *Valores:* label value · *Default:* N/A
- `in-protocol protocol` — Use In Protocol to filter the output. — *Valores:* ldp | rsvp | unk | – · *Default:* N/A
- `out-label label` — Use Out Label to filter the output. — *Valores:* label value · *Default:* N/A
- `out-protocol protocol` — Use Out Protocol to filter the output. — *Valores:* ldp | rsvp | unk | – · *Default:* N/A
- `outgoing-interface l3-interface` — Use Outgoing-Interface to filter the output. — *Valores:* l3-vlan id · *Default:* N/A
- `status status` — Use Status to filter the output. — *Valores:* active | pending | stale | standby | no ecmp resources · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 5.4 | Traffic engineering (TE) info was added. |
| 9.8 | ECMP information was added. |

**Usage Guidelines:**

To simply show the list of MPLS entries installed on data plane the following command can be used: Example:

```text
# show mpls forwarding-table
```

It is possible to filter the results by Prefix or Tunnel-Name, Action, In Label, In Protocol, Out Label, Out Protocol, Out interface and Status. Filter by Prefix: Example:

```text
# show mpls forwarding-table prefix-or-tnl-name 200.200.200.1/32
```

Filter by Tunnel Name: Example:

```text
# show mpls forwarding-table prefix-or-tnl-name tunnel-te-1000
```

Filter by Action: Example:

```text
# show mpls forwarding-table action swp
```

Filter by In Label: Example:

```text
# show mpls forwarding-table in-label 16
```

Filter by In Protocol: Example:

```text
# show mpls forwarding-table in-protocol ldp
```

Filter by Out Label: Example:

```text
# show mpls forwarding-table out-label ImpNull
```

Filter by Out Protocol: Example:

```text
# show mpls forwarding-table out-protocol ldp
```

Filter by Out Interface: Example:

```text
# show mpls forwarding-table outgoing-interface l3-vlan 100
```

Filter by Status: Example:

```text
# show mpls forwarding-table status active
```

**Output Terms:**

Output Description Prefix or Display the LSP prefix or Tunnel-Name associated with MPLS entry. Tunnel-Name Display the MPLS action performed on data plane by the entry. • none: no action associated with entry • fwd: originated MPLS tunnel with Implicit Null Label. • psh: originated MPLS tunnel pushing the outgoing label. Action • pop: remove incoming label to forward the packet. • php: swap the incoming label to Implicit Null label. • swp: swap incoming label to outgoing label. In Label Display the incoming label associated with entry. Display the incoming protocol which distributes the incoming label. • ldp: LDP distributed the label. In Proto • rsvp: RSVP distributed the label. • unk: an unknown protocol has distributed the label. Out Label Display the outgoing label associated with entry. Display the outgoing protocol which distributes the outgoing label. • ldp: LDP distributed the label. Out Proto • rsvp: RSVP distributed the label. • unk: an unknown protocol has distributed the label. Display the outgoing vlan interface for the MPLS traffic associated Out interface with entry. Output Description Display the current status of the entry. • Active: indicates entry is active. • Pending: indicates entry has installation pending due neighbor resolution. Status • Standby: indicates entry was not installed because another rule to the same prefix with a different action is in use. • No Ecmp Resources: indicates entry was not installed because all ECMP resources in the hardware are already in use.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show mpls traffic-eng tunnel-te brief`

> **Página:** 1008 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Show all RSVP-TE tunnel instances information present.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls traffic-eng tunnel-te brief [ backup backup | destination dest | id id | in-label label | in-vlan vlan | instance instance | name name | out-label label | out-vlan vlan | status status ]
```

**Parameters:**

- `backup backup` — Use backup information to filter the output. — *Valores:* available | in-use | none · *Default:* N/A
- `destination dest` — Use tunnel destination IPV4 address to filter the output. — *Valores:* a.b.c.d/x | string · *Default:* N/A
- `id id` — Use tunnel id to filter the output. — *Valores:* tunnel id value · *Default:* N/A
- `in-label label` — Use In Label to filter the output. — *Valores:* label value · *Default:* N/A
- `in-vlan vlan` — Use incoming VLAN to filter the output. — *Valores:* vlan value · *Default:* N/A
- `instance instance` — Use tunnel instance to filter the output. — *Valores:* tunnel instance value · *Default:* N/A
- `name name` — Use tunnel name to filter the output. — *Valores:* tunnel name value · *Default:* N/A
- `out-label label` — Use Out Label to filter the output. — *Valores:* label value · *Default:* N/A
- `out-vlan vlan` — Use outgoing VLAN to filter the output. — *Valores:* vlan value · *Default:* N/A
- `status status` — Use tunnel status to filter the output. — *Valores:* up | down | testing | unknown | dormant | not-present | lower-layer-down · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.8 | This command was updated to receive the brief tag. |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

Use the command to show the list of tunnel instances: Example:

```text
# show mpls traffic-eng tunnel-te brief
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 2 TUNNEL-TE-2 120.120.120.1 2 19 150 ImpNull 151 none up 3 TUNNEL-TE-3 100.100.100.1 2 20 151 ImpNull 150 none up It is possible to filter the results by ID, Name, Destination, Instance, In label, In VLAN, Out label, Out VLAN, Backup, and Status. Filter by ID: Example:

```text
# show mpls traffic-eng tunnel-te brief id 2
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 2 TUNNEL-TE-2 120.120.120.1 2 19 150 ImpNull 151 none up Filter by Name: Example:

```text
# show mpls traffic-eng tunnel-te brief name TUNNEL-TE-2
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 2 TUNNEL-TE-2 120.120.120.1 2 19 150 ImpNull 151 none up Filter by Destination: Example:

```text
# show mpls traffic-eng tunnel-te brief destination 120.120.120.1
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 2 TUNNEL-TE-2 120.120.120.1 2 19 150 ImpNull 151 none up Filter by Instance: Example:

```text
# show mpls traffic-eng tunnel-te brief instance 2
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 2 TUNNEL-TE-2 120.120.120.1 2 19 150 ImpNull 151 none up 3 TUNNEL-TE-3 100.100.100.1 2 20 151 ImpNull 150 none up Filter by In Label: Example:

```text
# show mpls traffic-eng tunnel-te brief in-label 20
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 3 TUNNEL-TE-3 100.100.100.1 2 20 151 ImpNull 150 none up Filter by In VLAN: Example:

```text
# show mpls traffic-eng tunnel-te brief in-vlan 150
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 2 TUNNEL-TE-2 120.120.120.1 2 19 150 ImpNull 151 none up Filter by Out Label: Example:

```text
# show mpls traffic-eng tunnel-te brief out-label ImpNull
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 2 TUNNEL-TE-2 120.120.120.1 2 19 150 ImpNull 151 none up 3 TUNNEL-TE-3 100.100.100.1 2 20 151 ImpNull 150 none up Filter by Out VLAN: Example:

```text
# show mpls traffic-eng tunnel-te brief out-vlan 150
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 3 TUNNEL-TE-3 100.100.100.1 2 20 151 ImpNull 150 none up Filter by Backup: Example:

```text
# show mpls traffic-eng tunnel-te brief backup none
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 2 TUNNEL-TE-2 120.120.120.1 2 19 150 ImpNull 151 none up 3 TUNNEL-TE-3 100.100.100.1 2 20 151 ImpNull 150 none up Filter by Status: Example:

```text
# show mpls traffic-eng tunnel-te brief status up
In In Out Out
```

ID Name Destination Inst label vlan label vlan Backup Status ---------------------------------------------------------------------------------- 2 TUNNEL-TE-2 120.120.120.1 2 19 150 ImpNull 151 none up 3 TUNNEL-TE-3 100.100.100.1 2 20 151 ImpNull 150 none up

**Output Terms:**

Output Description ID Display the Tunnel identifier associated with tunnel interface entry. Name Display the Tunnel-Name associated with tunnel interface entry. Destination Display the IPV4 address associated with tunnel interface entry. Instance Display the tunnel instance associated with tunnel interface entry. In Label Display the incoming label associated with entry. In vlan Display the incoming VLAN associated with entry. Out Label Display the outgoing label associated with entry. Out vlan Display the outgoing VLAN associated with entry. Display status of the backup instance associated with the tunnel interface. • available: Backup is current available. Backup • in-use: Backup is current in use. • none: Backup is not available. Output Description Display the tunnel instance status. • up: The tunnel instance is ready to pass packets. • down: The tunnel instance is not ready to pass packets. • testing: The tunnel instance is in some test mode. • unknown: The tunnel instance status cannot be determined. Status • dormant: The tunnel instance has some missing components. • not-present: The tunnel instance has some missing components. • lower-layer-down: The tunnel instance is down due to the state of lower-layer interfaces.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show mpls traffic-eng tunnel-te id | name`

> **Página:** 1015 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Show detailed RSVP-TE tunnel information for a single instance (by name or id).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls traffic-eng tunnel-te { id id | name name }
```

**Parameters:**

- `id id` — The tunnel id. — *Valores:* tunnel id value · *Default:* N/A
- `name name` — The tunnel name. — *Valores:* tunnel name value · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.8 | This command was introduced. |

**Usage Guidelines:**

Use the command to show the detailed information of a tunnel (by id): Example:

```text
# show mpls traffic-eng tunnel-te id 1
```

Id: 1 Name: R1-R4 [Active instance 2] Src: 192.168.1.1 Dst: 192.168.1.4 Status: Admin: up Oper: up Role: head Dir: out Path option: Path-option attribute: PATH_1 , type: dynamic (holding, instance 1) Affinity (blue): 0x1 [Incl.Any] 0x0 [Incl.All] 0x0 [Excl.Any] Tunnel LSP: Inlabel: -- , Outlabel: -- Path-option attribute: PATH_2 , type: dynamic (active, instance 2) Affinity (red): 0x2 [Incl.Any] 0x0 [Incl.All] 0x0 [Excl.Any] Tunnel LSP: Inlabel: -- , Outlabel: ImpNull Path Info for active instance: 1: 192.168.14.4 Use the command to show the detailed information of a tunnel (by name): Example:

```text
# show mpls traffic-eng tunnel-te name R1-R4
```

Id: 1 Name: R1-R4 [Active instance 2] Src: 192.168.1.1 Dst: 192.168.1.4 Status: Admin: up Oper: up Role: head Dir: out Path option: Path-option attribute: PATH_1 , type: dynamic (holding, instance 1) Affinity (blue): 0x1 [Incl.Any] 0x0 [Incl.All] 0x0 [Excl.Any] Tunnel LSP: Inlabel: -- , Outlabel: -- Path-option attribute: PATH_2 , type: dynamic (active, instance 2) Affinity (red): 0x2 [Incl.Any] 0x0 [Incl.All] 0x0 [Excl.Any] Tunnel LSP: Inlabel: -- , Outlabel: ImpNull Path Info for active instance: 1: 192.168.14.4 In case of all paths being down, no Path Info is shown: Example:

```text
# show mpls traffic-eng tunnel-te name R1-R4
```

Id: 1 Name: R1-R4 [Active instance 2] Src: 192.168.1.1 Dst: 192.168.1.4 Status: Admin: up Oper: up Role: head Dir: out Path option: Path-option attribute: PATH_1 , type: dynamic (holding, instance 1) Affinity (blue): 0x1 [Incl.Any] 0x0 [Incl.All] 0x0 [Excl.Any] Tunnel LSP: Inlabel: -- , Outlabel: -- Path-option attribute: PATH_2 , type: dynamic (active, instance 2) Affinity (red): 0x2 [Incl.Any] 0x0 [Incl.All] 0x0 [Excl.Any] Tunnel LSP: Inlabel: -- , Outlabel: ImpNull Tunnel is down - no path info available For unnamed tunnels (they receive a default name but can’t be queried by name) use the show by id: Example:

```text
# show mpls traffic-eng tunnel-te id 2
```

Id: 2 Name: tunnel-te-2 [Active instance 10] Src: 192.168.1.1 Dst: 1.1.1.1 Status: Admin: up Oper: down Role: head Dir: out Path option: Path-option attribute: PATH_1 , type: dynamic (holding, instance 10) Affinity (green): 0x0 [Incl.Any] 0x0 [Incl.All] 0x3 [Excl.Any] Tunnel LSP: Inlabel: -- , Outlabel: -- Tunnel is down - no path info available

**Output Terms:**

Output Description Id Display the Tunnel identifier associated with tunnel interface entry. Name Display the Tunnel-Name associated with tunnel interface entry. Output Description Active Instance Display the tunnel instance that is currently active. Src Display the IPV4 address associated with tunnel interface entry. Display the IPV4 address associated with tunnel interface destinaDst tion. Display the status of the active tunnel instance. Contains the Admin, Status Oper, Role and Dir information. Admin Admin status of the active instance. Oper Operation status of the active instance. Role The role of this node in the LSP. Dir The direction of the active instance tunnel. Path option Describes all the paths defined for the tunnel. Path-option Display the index of the path. attribute Display the type of the path. type • Currently only dynamic is supported Display the status of the path: • active: The path is active. path status • holding: The path is in hold state. instance Display the instance associated with the path. Output Description Affinity Display the configuration of the path affinity. profile Display the name of the affinity profile associated with the path. Incl.Any Affinity attribute values to be any included. Incl.All Affinity attribute values to be all included. Excl.Any Affinity attribute values to be any excluded. Tunnel LSP: Display the Inlabel of the tunnel path. Inlabel Tunnel LSP: Display the Outlabel of the tunnel path. Outlabel Path Info for active instance Display the path trace of the active instance

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A L2VPN


## L2VPN

### `clear mpls l2vpn counters vpls`

> **Página:** 1020 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Clears the Virtual Private LAN Services (VPLS) counters.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
clear mpls l2vpn counters vpls-group [name | vpn-name name ]
```

**Parameters:**

- `vpls-group name` — Use Group name to filter the output. — *Valores:* vpls-group name · *Default:* N/A
- `vpn-name name` — Use VPN name to filter the output. — *Valores:* vpn-name name · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |
| 4.9 | This command was modified. |

**Usage Guidelines:**

To clear the VPLS counters values the following command can be used: Example:

```text
# clear mpls l2vpn counters vpls-group Group1 vpn-name Vpn1
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `clear mpls l2vpn counters vpws`

> **Página:** 1022 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Clears the Virtual Private Wire Services (VPWS) counters.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
clear mpls l2vpn counters vpws-group [name | vpn-name name ]
```

**Parameters:**

- `vpls-group name` — Use Group name to filter the output. — *Valores:* vpls-group name · *Default:* N/A
- `vpn-name name` — Use VPN name to filter the output. — *Valores:* vpn-name name · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 4.9 | This command was modified. |

**Usage Guidelines:**

To clear the VPWS counters values the following command can be used: Example:

```text
# clear mpls l2vpn counters vpws-group Group1 vpn-name Vpn1
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `clear mpls l2vpn mac-address vpls`

> **Página:** 1024 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Clears the L2VPN VPLS macs.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
clear mpls l2vpn mac-address vpls-group [name | vpn-name name ]
```

**Parameters:**

- `vpls-group name` — Use Group name to filter the output. — *Valores:* vpls-group name · *Default:* N/A
- `vpn-name name` — Use VPN name to filter the output. — *Valores:* vpn-name name · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |
| 4.9 | This command was modified. |

**Usage Guidelines:**

To clear the L2VPN VPLS mac-address values the following commands can be used: Example:

```text
# clear mpls l2vpn mac-address vpls-group Group1 vpn-name Vpn1
# clear mpls l2vpn mac-address vpls-group Group1
# clear mpls l2vpn mac-address vpls-group
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn logging pw-status`

> **Página:** 1026 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables logs to monitor the status of the MPLS L2VPN Pseudowires.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn logging pw-status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to enable the MPLS L2VPN Pseudowire status log.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# logging pw-status
(config-l2vpn)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group`

> **Página:** 1028 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The Group ID field is a textual string arbitrary value that is assigned to a group of Virtual Private LAN Services (VPLS).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `text` — A textual string assigned to a group of VPLS. — *Valores:* String - maximum 32 characters. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the l2vpn vpls-group.

```text
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn`

> **Página:** 1030 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** A textual string to uniquely identify a Virtual Private LAN Services (VPLS) that supports Layer 2 VPN technology and provides multi-point Layer 2 connectivity for customers.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn administrative-status`

> **Página:** 1032 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status on a Virtual Private LAN Services (VPLS).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the Virtual Private LAN Services (VPLS). — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn administrative-status.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# administrative-status down
(config-vpn-Seattle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain`

> **Página:** 1035 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies a virtual bridge that connects the multiple access circuits together.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn bridge-domain.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain access-interface`

> **Página:** 1038 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the access interfaces to be attached inside a Virtual Private LAN Services (VPLS) bridge-domain.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain access-interface id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A
- `access-interface id` — Access interface configuration. — *Valores:* gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |
| 4.9 | Support for 100-gigabit Ethernet was added. |
| 5.4 | Support for service-port was added. |
| 5.10 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the bridge-domain access interfaces.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle-bd)# access-interface gigabit-ethernet-1/1/1
(config-vpn-Seattle-bd)# access-interface gigabit-ethernet-1/1/2
(config-vpn-Seattle-bd)# commit
```

To use a service-port as an access interface, the service-port must be configured without any translate rule, bridge domain mtu must be set to 2000 or less and transparent-lanservice must be enabled.

```text
# config
(config)# service-port 1 gpon 1/1/1 onu 1 gem 1
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle-bd)# bridge-mtu 2000
(config-vpn-Seattle-bd)# transparent-lan-service
(config-vpn-Seattle-bd)# access-interface service-port-1
(config-access-port-service-port-1)# commit
```

**Impacts and precautions:**

Vlan-mapping rules do not have effect over vpn access ports because the latter takes precedence over the former.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain access-interface administrative-status`

> **Página:** 1041 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status on a Virtual Private LAN Services (VPLS) access interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain access-interface id administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A
- `access-interface id` — Access interface configuration. — *Valores:* gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id. · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the Virtual Private LAN Services (VPLS) acess interface. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |
| 4.9 | Support for 100-gigabit Ethernet was added. |
| 5.10 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn bridge-domain access-interface administrative-status.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle-bd)# access-interface gigabit-ethernet-1/1/1
(config-access-interface-gigabit-ethernet-1/1/1)# administrative-status down
(config-access-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain access-interface encapsulation dot1q`

> **Página:** 1044 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the encapsulation of customer VLANs (C-VLANs) on a Virtual Private LAN Services (VPLS) access interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain access-interface id encapsulation dot1q values
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A
- `access-interface id` — Access interface configuration. — *Valores:* gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id. · *Default:* N/A
- `encapsulation dot1q values` — dot1q vlan (C-VLAN) or ranges of dot1q vlans (C-VLANs) to be encapsulated. — *Valores:* 1 - 4094 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 8.0 | A new usage guideline for encapsulation dot1q range was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. This command represents encapsulation dot1q ranges as a real range in hardware only when they have more than a fixed number of vlans, where this number is 50 for most platforms and 20 for DM4360, DM4370, DM4376 and DM4378. Otherwise, all vlans in a range are actually considered as individual vlans in the hardware. There are 8 real ranges available in hardware for each access interface. Example: This example shows how to configure the vpn bridge-domain access-interface encapsulation dot1q.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle-bd)# qinq
(config-vpn-Seattle-bd)# access-interface gigabit-ethernet-1/1/1
(config-access-port-gigabit-ethernet-1/1/1)# encapsulation dot1q 5,10-15,20
(config-access-port-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain access-interface encapsulation untagged`

> **Página:** 1047 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable the encapsulation of untagged frames.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain access-interface id encapsulation untagged
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A
- `access-interface id` — Access interface configuration. — *Valores:* gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id. · *Default:* N/A
- `encapsulation untagged` — Enable the untagged mode on the encapsulation of customer VLANs (C-VLANs). — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.12 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn bridge-domain access-interface encapsulation untagged.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle)# qinq
(config-vpn-Seattle-bd)# access-interface gigabit-ethernet-1/1/1
(config-access-port-gigabit-ethernet-1/1/1)# encapsulation untagged
(config-access-port-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain administrative-status`

> **Página:** 1050 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status on a Virtual Private LAN Services (VPLS) bridge-domain.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the Virtual Private LAN Services (VPLS) bridge-domain. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the bridge-domain administrative-status.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle-bd)# administrative-status down
(config-vpn-Seattle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain bridge-mtu`

> **Página:** 1053 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the explicit Maximum Transmission Unit(MTU) of the Virtual Private LAN Services(VPLS) bridge-domain.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain bridge-mtu value
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A
- `bridge-mtu value` — Specifies the VPLS bridge-domain MTU. — *Valores:* 64 - 9390. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the bridge-mtu value that explicitly specifies the MTU value used by the VPLS.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle-bd)# bridge-mtu 64
(config-vpn-Seattle-bd)# commit
```

**Impacts and precautions:**

Make sure to set an appropriate MTU to account for all the encapsulation overhead that will take place on your MPLS backbone to avoid packet drop. When the MTU is not explicitly configured by this command the value set on this VPLS is the lowest MTU value of the attached physical access interfaces.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain dot1q`

> **Página:** 1056 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the Virtual Private LAN Services (VPLS) bridge-domain to match a specific 802.1Q VLAN packets (VLAN-based).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain dot1q id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A
- `dot1q id` — Dot1q VLAN Id to be matched on bridge-domain for this VPN. — *Valores:* 1 - 4094 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: To configure a VLAN-based VPLS bridge-domain, perform this task on the provider edge routers:

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle-bd)# dot1q 23
(config-vpn-Seattle-bd)# commit
```

**Impacts and precautions:**

A VPLS bridge-domain and a Layer 2 bridge-domain that have the same Dot1Q identifier cannot share interfaces.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain mac-limit`

> **Página:** 1059 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the maximum limit of MAC addresses that can be learned on a Virtual Private LAN Services (VPLS) bridge-domain.

**Supported Platforms:** This command is supported only in the following platforms: DM4170, DM4360, DM4370, DM4376, DM4378, DM4610, DM4615.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain mac-limit value
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A
- `mac-limit value` — Specifies the VPLS bridge-domain mac-limit. — *Valores:* 1 - 32767. · *Default:* 1024.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the bridge-domain mac-limit

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle-bd)# mac-limit 4096
(config-vpn-Seattle)# commit
```

**Impacts and precautions:**

Although mac-limit configuration is per VPN, MAC address table is common for all of them in hardware. Therefore, according to the mac-limit value, one or a few VPNs can already consume all the MAC address table entries.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain qinq`

> **Página:** 1062 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable Selective Encapsulation QinQ mode for VPLS. This mode allows the configuration of multiple VLANs in the access-interface encapsulation command in order to set up a Selective Encapsulation VPN. This mode requires the vfi pw-type to be vlan and contain the service-delimiting VLAN which will be stacked up top into the frame along with the ingressed access VLANs.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain qinq
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A
- `qinq` — Enable Selective Encapsulation QinQ mode for VPLS. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.10 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure a Selective Encapsulation VPN QinQ mode.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle-bd)# qinq
(config-vpn-Seattle-bd)# access-interface gigabit-ethernet-1/1/1
(config-access-port-gigabit-ethernet-1/1/1)# encapsulation dot1q 5,10-15,20
(config-access-port-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn bridge-domain transparent-lanservice`

> **Página:** 1065 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable the Transparent LAN Service (TLS) mode on a Virtual Private LAN Services (VPLS) bridge-domain.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text bridge-domain transparent-lan-service
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `bridge-domain` — A virtual bridge representation. — *Valores:* N/A · *Default:* N/A
- `transparent-lan-service` — Enable the Transparent LAN Service (TLS) mode on a VPLS bridge-domain. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to enable the bridge-domain transparent-lan-service:

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# bridge-domain
(config-vpn-Seattle-bd)# transparent-lan-service
(config-vpn-Seattle-bd)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn description`

> **Página:** 1068 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies a textual string containing information about the Virtual Private LAN Services (VPLS) entity.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text description text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `description text` — A textual string containing information about the VPLS entity. — *Valores:* String - maximum 32 characters · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn description.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# description Text
(config-vpn-Seattle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi`

> **Página:** 1071 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies a Virtual Forwarding Instance (VFI) that connects multiples neighbors together.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn vfi.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# vfi
(config-vfi)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi administrative-status`

> **Página:** 1074 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status on a Virtual Forwarding Instance (VFI).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the Virtual Forwarding Instance. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn vfi administrative-status.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# vfi
(config-vfi)# administrative-status down
(config-vfi)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi neighbor`

> **Página:** 1077 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the IPv4 address to uniquely identify a Virtual Private LAN Services (VPLS) neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi neighbor id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A
- `neighbor id` — Specifies the VPLS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn vfi neighbor.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# vfi
(config-vfi)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi neighbor administrative-status`

> **Página:** 1080 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status on a Virtual Private LAN Services (VPLS) neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi neighbor id administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A
- `neighbor id` — Specifies the VPLS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the Virtual Private LAN Services (VPLS) neighbor. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn vfi neighbor administrative-status.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# vfi
(config-vfi)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# administrative-status down
(config-neighbor-30.30.30.30)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi neighbor pw-id`

> **Página:** 1083 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the pseudo-wire (PW) ID, a non-zero identifier that distinguishes between two MPLS peers from the others. To connect two attachment circuits through a PW, you need to associate each one with the same PW ID. This configuration is mandatory for neighbor enabling.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi neighbor id pw-id id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A
- `neighbor id` — Specifies the VPLS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `pw-id id` — Specifies the VPLS pseudo-wire numerical identifier. — *Valores:* 1-4294967294. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn vfi neighbor pw-id.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# vfi
(config-vfi)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-id 222
(config-neighbor-30.30.30.30)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi neighbor pw-load-balance`

> **Página:** 1086 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies mechanisms to load-balance the traffic over the Virtual Private LAN Services(VPLS).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi neighbor id pw-load-balance
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A
- `neighbor id` — Specifies the VPLS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `pw-load-balance` — Specifies the VPLS load-balance mechanisms. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure a load-balance mechanism over VPLS traffic.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# vfi
(config-vfi)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-load-balance
(config-pw-load-balance)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi neighbor pw-load-balance flow-label`

> **Página:** 1089 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the Flow-Aware Transport(FAT) that provides the capability to identify individual flows within a VPLS. This provides the routers the ability to use these flows to load-balance traffic.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi neighbor id pw-load-balance flow-label value
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A
- `neighbor id` — Specifies the VPLS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `pw-load-balance` — Specifies the VPLS load-balance mechanisms. — *Valores:* N/A · *Default:* N/A
- `flow-label value` — Specifies the VPLS Flow-Aware Transport. — *Valores:* both | receive | transmit. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the VPLS Flow-Aware Transport.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# vfi
(config-vfi)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-load-balance
(config-pw-load-balance)# flow-label both
(config-pw-load-balance)# commit
```

**Impacts and precautions:**

Make sure that both edges on the VPN have a consistently FAT configuration.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi neighbor pw-mtu`

> **Página:** 1092 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the explicitly signalization of the Maximum Transmission Unit(MTU) on the Virtual Private LAN Services(VPLS) neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi neighbor id pw-mtu value
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A
- `neighbor id` — Specifies the VPLS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `pw-mtu value` — Specifies the VPLS neighbor signalization MTU. — *Valores:* 64 - 9198. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn vfi neighbor pw-mtu value that explicitly specifies the MTU value used on the VPLS neighbor signalization.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# vfi
(config-vfi)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-mtu 64
(config-neighbor-30.30.30.30)# commit
```

**Impacts and precautions:**

The pw-mtu configuration is used by the signalization process, signaling purpose only. For packet dropping, check the access interface MTU. When the pw-mtu is not explicitly configured by this command the MTU value signaled by this VPLS is the same as the access interface MTU value.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi neighbor split-horizon`

> **Página:** 1095 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Control the pseudowire (PW) split-horizon group to prevents/allows packets received from a PW from being forwarded into another PW. This technique is important for creating loop-free paths in a full-meshed network.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi neighbor id split-horizon command
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A
- `neighbor id` — Specifies the VPLS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `split-horizon command` — Control the VPLS pseudowire split-horizon group. — *Valores:* enable | disable. · *Default:* enable.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn vfi neighbor split-horizon.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# vfi
(config-vfi)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# split-horizon disable
(config-neighbor-30.30.30.30)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi neighbor tunnel-interface`

> **Página:** 1098 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the MPLS Traffic Engineering (TE) Tunnel interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi neighbor id tunnel-interface interface
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A
- `neighbor id` — Specifies the VPLS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `tunnel-interface interface-name` — Specifies the (TE) Traffic Engineering tunnel interface. — *Valores:* tunnel-te-<tunnel ID>. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure vpn tunnel interface.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# vfi
(config-vpn-Seattle)# neighbor 40.40.40.40
(config-neighbor-40.40.40.40)# tunnel-interface tunnel-te-1000
(config-neighbor-40.40.40.40)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpls-group vpn vfi pw-type`

> **Página:** 1101 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the Virtual Forwarding Instance (VFI) encapsulation mode.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpls-group text vpn text vfi pw-type type
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpls-group text` — A textual string to represent a VPLS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPLS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vfi` — A Virtual Forwarding Instance representation. — *Valores:* N/A · *Default:* N/A
- `pw-type type` — Specifies the VPLS VFI pseudo-wire encapsulation type. — *Valores:* ethernet | vlan | vlan id. · *Default:* ethernet.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn vfi pw-type ethernet. In this mode, all Ethernet frames received on the attachment circuit will be transmitted on a single PW. This service corresponds to PW type 0x0005 “Ethernet”.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# pw-type ethernet
(config-vpn-Seattle)# commit
```

This example shows how to configure the vpn vfi pw-type vlan. This mode uses access dot1q id as a service-delimiting tag to map input Ethernet frames to respective PWs and corresponds to PW type 0x0004 “Ethernet Tagged Mode”.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# pw-type vlan
(config-vpn-Seattle)# commit
```

This example shows how to configure the vpn neighbor pw-type vlan with a explicit VLAN Id. This mode uses a explicit service-delimiting tag to map input Ethernet frames to respective PWs and corresponds to PW type 0x0004 “Ethernet Tagged Mode”.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpls-group Washington
(config-vpls-group-Washington)# vpn Seattle
(config-vpn-Seattle)# pw-type vlan 22
(config-vpn-Seattle)# commit
```

**Impacts and precautions:**

The pw-type must be selected in such a way that it matches both ends of the VPLS neighbors.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group`

> **Página:** 1104 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The Group ID field is a textual string arbitrary value that is assigned to a group of pseudo-wire (PW).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `text` — A textual string assigned to a group of pseudo-wire (PW). — *Valores:* String - maximum 32 characters. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the l2vpn vpws-group.

```text
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn`

> **Página:** 1106 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** A textual string to uniquely identify a Virtual Private Wire Services (VPWS). A VPWS connection deploys a Layer 2 service over MPLS to build a point-to-point topology connection attaching end customer sites in a VPN.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# commit
```

**Impacts and precautions:**

Service-port cannot be used as VPN uplink.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn access-interface`

> **Página:** 1108 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the access interface for a Virtual Private Wire Services (VPWS).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text access-interface id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `access-interface id` — Access interface configuration. — *Valores:* gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 3.0 | Support for 40-gigabit Ethernet and LAG was added. |
| 4.8 | Support for service-port was added. |
| 4.9 | Support for 100-gigabit Ethernet was added. |
| 5.10 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn access interface.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# access-interface gigabit-ethernet-1/1/1
(config-access-port-gigabit-ethernet-1/1/1)# commit
```

To use a service-port as an access interface, the service-port must be configured without any translate rule and mtu must be set to 2000 or less.

```text
# config
(config)#service-port 1 gpon 1/1/1 onu 1 gem 1
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# access-interface service-port-1
(config-access-port-service-port-1)# mtu 2000
(config-access-port-service-port-1)# commit
```

**Impacts and precautions:**

Vlan-mapping rules do not have effect over vpn access ports because the latter takes precedence over the former.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn access-interface administrative-status`

> **Página:** 1111 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status on an access interface for a Virtual Private Wire Services (VPWS).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text access-interface id administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `access-interface id` — Access interface configuration. — *Valores:* gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the Access Interface. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 3.0 | Support for 40-gigabit Ethernet and LAG was added. |
| 4.8 | Support for service-port was added. |
| 4.9 | Support for 100-gigabit Ethernet was added. |
| 5.10 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn access-interface administrative-status.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# access-interface gigabit-ethernet-1/1/1
(config-access-port-gigabit-ethernet-1/1/1)# administrative-status down
(config-access-port-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn access-interface dot1q`

> **Página:** 1114 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables the Virtual Private Wire Services(VPWS) access interface to match specific 802.1Q VLAN packets (VLAN-based).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text access-interface intf-id dot1q id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `access-interface intf-id` — Access interface configuration. — *Valores:* gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `dot1q id` — Dot1q VLAN Id to be matched on access interface for this VPN. — *Valores:* 1 - 4094 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 3.0 | Support for 40-gigabit Ethernet and LAG was added. |
| 4.8 | Support for service-port was added. |
| 4.9 | Support for 100-gigabit Ethernet was added. |
| 5.10 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: To configure a VLAN-based VPWS, perform this task on the provider edge routers:

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# access-interface gigabit-ethernet-1/1/1
(config-access-port-gigabit-ethernet-1/1/1)# dot1q 23
(config-access-port-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn access-interface encapsulation dot1q`

> **Página:** 1117 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the encapsulation of multiple customer VLANs (C-VLANs) on a Virtual Private Wire Services (VPWS) access interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text access-interface intf-id encapsulation dot1q values
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `access-interface intf-id` — Access interface configuration. — *Valores:* gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `encapsulation dot1q values` — dot1q vlan (C-VLAN) or ranges of dot1q vlans (C-VLANs) to be encapsulated. — *Valores:* 1 - 4094 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.12 | This command was introduced. |
| 8.0 | A new usage guideline for encapsulation dot1q range was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. This command represents encapsulation dot1q ranges as a real range in hardware only when they have more than a fixed number of vlans, where this number is 50 for most platforms and 20 for DM4360, DM4370, DM4376 and DM4378. Otherwise, all vlans in a range are actually considered as individual vlans in the hardware. There are 8 real ranges available in hardware for each access interface. Example: This example shows how to configure the vpn access-interface encapsulation dot1q.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# qinq
(config-vpn-Seattle)# access-interface gigabit-ethernet-1/1/1
(config-access-port-gigabit-ethernet-1/1/1)# encapsulation dot1q 5,10-15,20
(config-access-port-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn access-interface encapsulation untagged`

> **Página:** 1120 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable the encapsulation of untagged frames.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text access-interface intf-id encapsulation untagged
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `access-interface intf-id` — Access interface configuration. — *Valores:* gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id. · *Default:* N/A
- `encapsulation untagged` — Enable the untagged mode on the encapsulation of customer VLANs (C-VLANs). — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 6.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn access-interface encapsulation untagged.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# qinq
(config-vpn-Seattle-bd)# access-interface gigabit-ethernet-1/1/1
(config-access-port-gigabit-ethernet-1/1/1)# encapsulation untagged
(config-access-port-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn access-interface mtu`

> **Página:** 1123 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the explicit Maximum Transmission Unit(MTU) of the Virtual Private Wire Services(VPWS) access interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text access-interface intf-id mtu value
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `access-interface intf-id` — Access interface configuration. — *Valores:* gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `mtu value` — Specifies the explicit MTU used by the VPWS access interface. — *Valores:* 64 - 9390. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |
| 4.8 | Support for service-port was added. |
| 4.9 | Support for 100-gigabit Ethernet was added. |
| 5.10 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: To configure an explicit access interface MTU on a VPWS, perform this task on the provider edge routers:

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# access-interface gigabit-ethernet-1/1/1
(config-access-port-gigabit-ethernet-1/1/1)# mtu 64
(config-access-port-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

Make sure to set an appropriate MTU to account for all the encapsulation overhead that will take place on your MPLS backbone to avoid packet drop. When the mtu is not explicitly configured by this command the mtu value set on this VPWS is the same one set on the access interface. For a service-port access interface, mtu must be set to 2000 or less.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn administrative-status`

> **Página:** 1126 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status on a Virtual Private Wire Services (VPWS).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the Virtual Private Wire Services (VPWS). — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn administrative-status.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# administrative-status down
(config-vpn-Seattle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn backup-neighbor`

> **Página:** 1129 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Virtual Private Wire Services (VPWS) backup neighbor configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text backup-neighbor id [ pw-load-balance flow-label value | pw-id id | administrative-status status ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `backup-neighbor id` — Specifies the VPWS backup neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d · *Default:* N/A
- `pw-load-balance` — Specifies mechanisms to load-balance the traffic over the Virtual Private Wire Services (VPWS). — *Valores:* N/A · *Default:* N/A
- `flow-label value` — Specifies the Flow-Aware Transport (FAT) that provides the capability to identify individual flows within a VPWS. This provides the routers the ability to use these flows to load-balance traffic. — *Valores:* both | receive | transmit · *Default:* None
- `pw-id id` — Specifies the VPWS pseudo-wire numerical identifier. This configuration is mandatory for neighbor enabling. — *Valores:* 1-4294967294 · *Default:* N/A
- `administrative-status status` — Specifies the desired administrative status on a Virtual Private Wire Services (VPWS) backup neighbor. — *Valores:* up | down · *Default:* up

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 6.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the VPN backup neighbor.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# backup-neighbor 30.30.30.30
(config-backup-neighbor-30.30.30.30)# pw-id 100
(config-backup-neighbor-30.30.30.30)# administrative-status up
(config-backup-neighbor-30.30.30.30)# pw-load-balance flow-label both
(config-pw-load-balance)# commit
```

**Impacts and precautions:**

Both pw-type and pw-mtu configuration from the main neighbor are shared with the backup neighbor. Make sure that both edges on the VPN have a consistent FAT configuration. If the main neighbor is up, it will be the active PW for this VPN. If a failure is detected in the main PW, it will switchover to the backup PW. When failure from the main PW is recovered, there will be a 30 seconds guard-time before restoring the main as the active PW. If a new failure is detected in the main PW within the guard time, it will remain in the backup PW. If a failure is detected in the backup PW while the main PW is up, it will immediately switch back to the main PW.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn description`

> **Página:** 1132 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies a textual string containing information about the VPWS entity.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text description text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `description text` — A textual string containing information about the VPWS entity. — *Valores:* String - maximum 32 characters · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn description.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# description Text
(config-vpn-Seattle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn neighbor`

> **Página:** 1135 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the IPv4 address to uniquely identify a Virtual Private Wire Services (VPWS) neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text neighbor id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `neighbor id` — Specifies the VPWS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn neighbor.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn neighbor administrative-status`

> **Página:** 1138 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status on a Virtual Private Wire Services (VPWS) neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text neighbor id administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `neighbor id` — Specifies the VPWS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the Virtual Private Wire Services (VPWS) neighbor. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn neighbor administrative-status.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Name
(config-vpws-group-Washington)# vpn Name
(config-vpn-Seattle)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# administrative-status down
(config-neighbor-30.30.30.30)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn neighbor pw-id`

> **Página:** 1141 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the pseudo-wire (PW) ID, a non-zero identifier that distinguishes between two MPLS peers from the others. To connect two attachment circuits through a PW, you need to associate each one with the same PW ID. This configuration is mandatory for neighbor enabling.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text neighbor id pw-id id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `neighbor id` — Specifies the VPWS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `pw-id id` — Specifies the VPWS pseudo-wire numerical identifier. — *Valores:* 1-4294967294. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn neighbor pw-id.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-id 222
(config-neighbor-30.30.30.30)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn neighbor pw-load-balance`

> **Página:** 1144 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies mechanisms to load-balance the traffic over the Virtual Private Wire Services(VPWS).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text neighbor id pw-load-balance
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `neighbor id` — Specifies the VPWS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `pw-load-balance` — Specifies the VPWS load-balance mechanisms. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure a load-balance mechanism over VPWS traffic.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-load-balance
(config-pw-load-balance)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn neighbor pw-load-balance flow-label`

> **Página:** 1147 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the Flow-Aware Transport(FAT) that provides the capability to identify individual flows within a VPWS. This provides the routers the ability to use these flows to load-balance traffic.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text neighbor id pw-load-balance flow-label value
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `neighbor id` — Specifies the VPWS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `pw-load-balance` — Specifies the VPWS load-balance mechanisms. — *Valores:* N/A · *Default:* N/A
- `flow-label value` — Specifies the VPWS Flow-Aware Transport. — *Valores:* both | receive | transmit. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the VPWS Flow-Aware Transport.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-load-balance
(config-pw-load-balance)# flow-label both
(config-pw-load-balance)# commit
```

**Impacts and precautions:**

Make sure that both edges on the VPN have a consistently FAT configuration.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn neighbor pw-mtu`

> **Página:** 1150 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the explicitly signalization of the Maximum Transmission Unit(MTU) on the Virtual Private Wire Services(VPWS).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text neighbor id pw-mtu value
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `neighbor id` — Specifies the VPWS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `pw-mtu value` — Specifies the VPWS signalization MTU. — *Valores:* 64 - 9198. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn neighbor pw-mtu value that explicitly specifies the MTU value used on the VPWS signalization.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-mtu 64
(config-neighbor-30.30.30.30)# commit
```

**Impacts and precautions:**

Make sure to set an appropriate MTU to account for all the encapsulation overhead that will take place on your MPLS backbone to avoid packet drop. When the pw mtu is not explicitly configured by this command the mtu value signaled by this VPWS is the same as the access interface mtu value.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn neighbor pw-type`

> **Página:** 1153 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the Virtual Private Wire Services(VPWS) encapsulation mode.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text neighbor id pw-type type
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `neighbor id` — Specifies the VPWS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `pw-type type` — Specifies the VPWS neighbor pseudo-wire encapsulation type. — *Valores:* ethernet | vlan | vlan id. · *Default:* ethernet.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the vpn neighbor pw-type ethernet. In this mode, all Ethernet frames received on the attachment circuit will be transmitted on a single PW. This service corresponds to PW type 0x0005 “Ethernet”.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-type ethernet
(config-neighbor-30.30.30.30)# commit
```

This example shows how to configure the vpn neighbor pw-type vlan. This mode uses access dot1q id as a service-delimiting tag to map input Ethernet frames to respective PWs and corresponds to PW type 0x0004 “Ethernet Tagged Mode”.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-type vlan
(config-neighbor-30.30.30.30)# commit
```

This example shows how to configure the vpn neighbor pw-type vlan with a explicit VLAN Id. This mode uses a explicit service-delimiting tag to map input Ethernet frames to respective PWs and corresponds to PW type 0x0004 “Ethernet Tagged Mode”.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# neighbor 30.30.30.30
(config-neighbor-30.30.30.30)# pw-type vlan 22
(config-neighbor-30.30.30.30)# commit
```

**Impacts and precautions:**

The pw-type must be selected in such a way that it matches both ends of the VPWS.

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn neighbor tunnel-interface`

> **Página:** 1156 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the MPLS Traffic Engineering (TE) Tunnel interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text neighbor id tunnel-interface interface
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `neighbor id` — Specifies the VPWS neighbor identifier expressed in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `tunnel-interface interface-name` — Specifies the (TE) Traffic Engineering tunnel interface. — *Valores:* tunnel-te-<tunnel ID>. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure vpn tunnel interface.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# neighbor 40.40.40.40
(config-neighbor-40.40.40.40)# tunnel-interface tunnel-te-1000
(config-neighbor-40.40.40.40)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls l2vpn vpws-group vpn qinq`

> **Página:** 1159 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable Selective Encapsulation QinQ mode for VPWS. This mode allows the configuration of multiple VLANs in the access-interface encapsulation command in order to set up a Selective Encapsulation VPN. This mode requires the neighbor pw-type to be vlan and contain the service-delimiting VLAN which will be stacked up top into the frame along with the ingressed access VLANs.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls l2vpn vpws-group text vpn text qinq
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls l2vpn vpws-group text` — A textual string to represent a VPWS group. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `vpn text` — A textual string to represent a VPWS entity. — *Valores:* String - maximum 32 characters. · *Default:* N/A
- `qinq` — Enable Selective Encapsulation QinQ mode for VPWS. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.12 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure a Selective Encapsulation VPN QinQ mode.

```text
# config
(config)# mpls l2vpn
(config-l2vpn)# vpws-group Washington
(config-vpws-group-Washington)# vpn Seattle
(config-vpn-Seattle)# qinq
(config-vpn-Seattle)# access-interface gigabit-ethernet-1/1/1
(config-access-port-gigabit-ethernet-1/1/1)# encapsulation dot1q 5,10-15,20
(config-access-port-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show mpls l2vpn counters`

> **Página:** 1162 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays the L2VPN counters values since the last clear mpls l2vpn counters command.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls l2vpn counters [ vpws-group name | vpls-group name] [ vpn-name name ] [ access-interface name ]
```

**Parameters:**

- `vpws-group name` — Use Group name to filter the Virtual Private Wire Services (VPWS) groups. — *Valores:* group name · *Default:* N/A
- `vpls-group name` — Use Group name to filter the Virtual Private LAN Services (VPLS) groups. — *Valores:* group name · *Default:* N/A
- `vpn-name name` — Use VPN name to filter the output. — *Valores:* vpn name · *Default:* N/A
- `access-interface name` — Use access interface name to filter the output. — *Valores:* access interface name · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | The VPWS filter was introduced. |
| 5.6 | The access-interface filter was introduced for vpls. |

**Usage Guidelines:**

To displays the L2VPN counters values since the last clear mpls l2vpn counters command the following command can be used: Example: It is possible to filter the results by VPWS Group and VPN Name.

```text
# show mpls l2vpn counters vpws-group California vpn-name LA
```

VPLS-Group: California, VPN-Name: LA, State: created Segment-1: gigabit-ethernet-1/1/3, State: created Statistics: Packets: Received: 42, Sent: 42 Segment-2: 20.20.20.20, Pw-ID: 3, State: created Statistics: Packets: Received: 42, Sent: 42 Also, for VPLS vpns it is possible to filter the results by access interface.

```text
# show mpls l2vpn counters vpls-group Texas vpn-name Houston access-interface service-port-1
```

VPLS-Group: Texas, VPN-Name: Houston, State: created Segment-1: bridge-domain, Status: up service-port-1, State: created Statistics: Packets: Received: 42, Sent: 42 Segment-2: Virtual Forwarding Instance, Status: up 200.200.200.2, Pw-ID: 101, State: created Statistics: Packets: Received: 42, Sent: 42

```text
# show mpls l2vpn counters vpls-group Texas vpn-name Houston access-interface gigabit-ethernet-1/1/5
```

VPLS-Group: Texas, VPN-Name: Houston, State: created Segment-1: bridge-domain, Status: up gigabit-ethernet-1/1/5, State: created Statistics: Packets: Received: 42, Sent: 42 Segment-2: Virtual Forwarding Instance, Status: up 200.200.200.2, Pw-ID: 101, State: created Statistics: Packets: Received: 42, Sent: 42

**Output Terms:**

Output Description VPWS-Group Display the VPWS group name associated with entry. VPLS-Group Display the VPLS group name associated with entry. VPN-Name Display the VPN name associated with entry. Display the MPLS VPN status associated with entry. • created: indicates entry is created in hardware. State • pending: indicates entry has installation pending. • failed: indicates a failed installation in hardware. Segment-1 Display the access interface id associated with entry. Display the MPLS access status associated with entry. • created: indicates entry is created in hardware. State • pending: indicates entry has installation pending. • failed: indicates a failed installation in hardware. Display the number of packets received in the L2VPN access interReceived face. Sent Display the number of packets sent by the L2VPN access interface. Segment-2 Display the neighbor id associated with entry. Pw-ID Display the PW id associated with entry. Output Description Display the number of packets received in the L2VPN uplink interReceived face. Sent Display the number of packets sent by the L2VPN uplink interface. Display the MPLS uplink status associated with entry. • created: indicates entry is created in hardware. • pending: indicates entry has installation pending due neighbor State resolution. • failed: indicates a failed installation in hardware.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show mpls l2vpn hardware`

> **Página:** 1166 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Show list of L2VPN entries installed on data plane.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls l2vpn hardware [ vpws-group name | vpn-name name | vpn-state state | seg1-id gigabit/ten-gigabit-ethernet | seg1-state state | seg2-id ipv4-prefix | local-label label | remote-label label | seg2-state state | pw-id id | pw-type type ]
```

**Parameters:**

- `vpws-group name` — Use Group name to filter the output. — *Valores:* group name · *Default:* N/A
- `vpn-name name` — Use VPN name to filter the output. — *Valores:* vpn name · *Default:* N/A
- `vpn-state state` — Use VPN state to filter the output. — *Valores:* created | pending | failed · *Default:* N/A
- `seg1-id gigabit-ethernet` — Use Segment 1 ID to filter the output. — *Valores:* gigabit/ten-gigabit-ethernet · *Default:* N/A
- `seg1-state state` — Use Segment 1 State to filter the output. — *Valores:* created | pending | failed · *Default:* N/A
- `seg2-id ipv4-prefix` — Use Segment 2 ID to filter the output. — *Valores:* a.b.c.d · *Default:* N/A
- `local-label label` — Use Segment 2 Local Label to filter the output. — *Valores:* local label · *Default:* N/A
- `remote-label label` — Use Segment 2 Remote Label to filter the output. — *Valores:* remote label · *Default:* N/A
- `seg2-state state` — Use Segment 2 State to filter the output. — *Valores:* created | pending | failed · *Default:* N/A
- `pw-id id` — Use PW ID to filter the output. — *Valores:* pw id · *Default:* N/A
- `pw-type type` — Use PW type to filter the output. — *Valores:* ethernet | vlan | vlan XXX · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 2.4 | Added new pw-type parameter. |

**Usage Guidelines:**

To simply show the list of MPLS L2VPN installed on data plane the following command can be used: Example:

```text
# show mpls l2vpn hardware
```

It is possible to filter the results by VPWS Group, VPN Name, VPN State, Segment-1 Id, Access State, Segment-2 Id, Pw-ID, Local Label, Remote Label and Neighbor State. Filter by VPWS Group: Example:

```text
# show mpls l2vpn hardware vpws-group NAME
```

Filter by VPN Name: Example:

```text
# show mpls l2vpn hardware vpn-name NAME
```

Filter by VPN State: Example:

```text
# show mpls l2vpn hardware vpn-state created
```

Filter by Segment-1 Id: Example:

```text
# show mpls l2vpn hardware seg1-id gigabit-ethernet-1/1.1/1
```

Filter by Access State: Example:

```text
# show mpls l2vpn hardware seg1-state created
```

Filter by Segment-2 Id: Example:

```text
# show mpls l2vpn hardware seg2-id 2.2.2.2
```

Filter by Pw-ID: Example:

```text
# show mpls l2vpn hardware pw-id 55
```

Filter by Pw-Type: Example:

```text
# show mpls l2vpn hardware pw-type vlan 100
```

Filter by Local Label: Example:

```text
# show mpls l2vpn hardware local-label 11
```

Filter by Remote Label: Example:

```text
# show mpls l2vpn hardware remote-label 12
```

Filter by Neighbor State: Example:

```text
# show mpls l2vpn hardware seg2-state created
```

**Output Terms:**

Output Description VPWS-Group Display the VPWS group name associated with entry. VPN-Name Display the VPN name associated with entry. Display the MPLS VPN status associated with entry. • created: indicates entry is created in hardware. State • pending: indicates entry has installation pending. • failed: indicates a failed installation in hardware. Segment-1 Display the access interface id associated with entry. Display the MPLS access status associated with entry. • created: indicates entry is created in hardware. State • pending: indicates entry has installation pending. • failed: indicates a failed installation in hardware. Segment-2 Display the neighbor id associated with entry. Pw-ID Display the PW id associated with entry. Pw-Type Display the PW type associated with entry. Local Label Display the local label associated with entry. Remote Label Display the remote label associated with entry. Output Description Display the MPLS uplink status associated with entry. • created: indicates entry is created in hardware. • pending: indicates entry has installation pending due neighbor State resolution. • failed: indicates a failed installation in hardware.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show mpls l2vpn vpls-group`

> **Página:** 1172 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows list of L2VPN (VPLS) entries present on control plane.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls l2vpn vpls-group [ brief | detail ] [ vpls-group name | vpn-name name ]
```

**Parameters:**

- `brief` — Shows resumed information about the L2VPN (VPLS) control plane. — *Valores:* N/A · *Default:* N/A
- `detail` — Shows detailed information about the L2VPN (VPLS) control plane. — *Valores:* N/A · *Default:* N/A
- `vpls-group name` — Uses Group name to filter the output. — *Valores:* group name · *Default:* N/A
- `vpn-name name` — Uses VPN name to filter the output. — *Valores:* vpn name · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

To simply show the list of MPLS L2VPN present on control plane the following command can be used: Example:

```text
# show mpls l2vpn vpls-group brief
```

VPLS-Group VPN-Name Status Segment-1 State Segment-2 Pw-ID State ----------------------------------------------------------------------------------------------------------------------- California LA up gigabit-ethernet-1/1/19.1000 up - - - ten-gigabit-ethernet-1/1/1.1000 up - - - ten-gigabit-ethernet-1/1/2.1000 up - - - - - 200.200.2.2 147852 up - - 200.200.2.3 1478524 up - - 200.200.2.45 14785256 dormant ---------- ------ ------------------------------- ----- --------------- ---------- ---------------- SD down gigabit-ethernet-1/1/12 down - - - - - 200.200.200.2 1234 down - - 200.200.200.3 1234567989 failed ---------- ------ ------------------------------- ----- --------------- ---------- ---------------- SF up ten-gigabit-ethernet-1/1/1.1519 up - - - ten-gigabit-ethernet-1/1/2.1519 up - - - ten-gigabit-ethernet-1/1/3.1519 up - - - ten-gigabit-ethernet-1/1/4.1519 up - - - - - 200.200.200.2 19664 dormant ---------- ------ ------------------------------- ----- --------------- ---------- ---------------- SJ up - - 200.200.200.2 987652412 up - - 200.200.200.22 987652412 up - - 200.200.200.221 987652412 lower-layer-down ---------- ---------- ------ ------------------------------- ----- --------------- ---------- ---------------- Ilinois Chicago up gigabit-ethernet-1/1/20 down - - - gigabit-ethernet-1/1/22 up - - - gigabit-ethernet-1/1/23 up - - - gigabit-ethernet-1/1/24 up - - - - - 200.200.20.20 20 up - - 200.200.200.123 123 up ---------- ---------- ------ ------------------------------- ----- --------------- ---------- ---------------- It is possible to filter the results by VPLS Group or VPN Name. Filter by VPLS Group: Example:

```text
# show mpls l2vpn vpls-group brief vpls-group Ilinois
```

VPLS-Group VPN-Name Status Segment-1 State Segment-2 Pw-ID State ------------------------------------------------------------------------------------------------------------ Ilinois Chicago up gigabit-ethernet-1/1/20 up - - - gigabit-ethernet-1/1/22 up - - - gigabit-ethernet-1/1/23 up - - - gigabit-ethernet-1/1/24 up - - - - - 200.200.20.20 20 down - - 200.200.200.123 123 down ---------- ---------- ------ ------------------------------- ----- --------------- ---------- ----- To simply show the detailed list of MPLS L2VPN present on control plane the following command can be used: It is possible to filter the results by VPLS Group or VPN Name. Example:

```text
# show mpls l2vpn vpls-group detail
```

VPLS-Group: Texas; VPN-Name: Dallas; Admin status: up; Bridge-Domain: Admin status: up; Oper state: up; MAC learning: enabled MAC aging time: 339 s, Type: inactivity MAC limit: 1024, Action: drop Transparent-LAN-Service: enabled Bridge-MTU: 4000 Dot1q: 72 AC: forty-gigabit-ethernet-1/1/1.72; Admin status: up; Oper state: up; MTU: 4000; Encapsulation Dot1q: 150-300,untagged; AC: forty-gigabit-ethernet-1/1/2.72; Admin status: up; Oper state: up; MTU: 4000; Encapsulation Dot1q: 10,50-100,120; AC: forty-gigabit-ethernet-1/1/3.72; Admin status: up; Oper state: up; MTU: 4000; Encapsulation Dot1q: untagged; AC: lag-1.72; Admin status: up; Oper state: up; Encapsulation Dot1q: 15,20,30; MTU: 4000; VFI: Admin status: up; Oper state: up; Pw-type: vlan 71; Signalling protocol: ldp; PW: Neighbor address: 200.200.200.3; Admin status: up; Oper state: up; Up time: 0 days 0 hours 0 minutes 24 seconds; Last state change time: Wed Sep 12 13:13:44 2018; Pw-ID: 72; Pw-MTU: 4000; Tunnel interface: tunnel-te-100; FAT: Flow-label receive: true; Flow-label transmit: false; Split-horizon: enabled; Remote access interface state: up; MPLS VC labels: Local: 27; Remote: 17; MTU: Local: 4000; Remote: 4000; PW: Neighbor address: 200.200.200.4; Admin status: up; Oper state: up; Up time: 0 days 0 hours 0 minutes 24 seconds; Last state change time: Wed Sep 12 13:13:44 2018; Pw-ID: 71; Pw-MTU: 4000; Tunnel interface: tunnel-te-200; FAT: Flow-label receive: true; Flow-label transmit: false; Split-horizon: enabled; Remote access interface state: up; MPLS VC labels: Local: 34; Remote: 17; MTU: Local: 4000; Remote: 4000; VPLS-Group: Texas; VPN-Name: Houston; Admin status: up; Bridge-Domain: Admin status: up; Oper state: down; MAC learning: enabled MAC aging time: 339 s, Type: inactivity MAC limit: 1024, Action: drop Bridge-MTU: 1555 Dot1q: 92 AC: forty-gigabit-ethernet-1/1/1.92; Admin status: down; Oper state: down; MTU: 1555; AC: forty-gigabit-ethernet-1/1/2.92; Admin status: up; Oper state: up; MTU: 1555; AC: lag-1.92; Admin status: up; Oper state: up; MTU: 1555; VFI: Admin status: up; Oper state: up; Pw-type: vlan 4000; Signalling protocol: ldp; PW: Neighbor address: 200.200.200.2; Admin status: up; Oper state: up; Up time: 0 days 0 hours 0 minutes 24 seconds; Last state change time: Wed Sep 12 13:13:44 2018; Pw-ID: 92; Pw-MTU: 1555; Tunnel interface: ldp; FAT: Flow-label receive: true; Flow-label transmit: false; Split-horizon: enabled; Remote access interface state: up; MPLS VC labels: Local: 18; Remote: 18; MTU: Local: 1555; Remote: 1555; PW: Neighbor address: 200.200.200.4; Admin status: up; Oper state: up; Up time: 0 days 0 hours 0 minutes 24 seconds; Last state change time: Wed Sep 12 13:13:44 2018; Pw-ID: 91; Pw-MTU: 1999; Tunnel interface: ldp; FAT: Flow-label receive: false; Flow-label transmit: true; Split-horizon: enabled; Remote access interface state: up; MPLS VC labels: Local: 33; Remote: 16; MTU: Local: 1999; Remote: 1999;

**Output Terms:**

Output Description Pw-ID Displays the PW id associated with that entry. Segment-1 Displays the access interface id associated with that entry. Segment-2 Displays the neighbor id associated with that entry. Displays the MPLS access interface status associated with that entry. • up: The interface is ready to pass packets. Segment-1 State • down: The interface is admin down and deprogrammed. Displays the MPLS pseudowire status associated with that entry. • up: The PW is ready to pass packets. • down: The PW is admin down and deprogrammed. • dormant: The PW is not in a condition to pass packets. It is waiting for signaling to complete. Segment-2 State • lowerLayerDown: One or more of the lower-layer interfaces is not in OperStatus ‘up’ state. • failed: The PW is admin up but has failed to go operationally Up. It is not ready to pass packets because of a local or remote failure. Status Displays the MPLS VPN status associated with that entry. Transparent-LAN-ServiDciesplays the VPLS bridge-domain TLS mode i.e. disabled or enabled. Output Description Bridge-MTU Displays the VPLS bridge-domain MTU. Displays the VPLS bridge-domain Dot1q VLAN Id that is set for the Dot1q VPN’s bridge-domain. Encapsulation Displays the set of C-VLANs that are encapsulated on the VPLS acDot1q cess interface. Last state change Displays the last time that PW operational state has changed. time MAC Learning Displays the MAC Learning status. It is always enabled. Displays the MAC aging time. This parameter is configured globaly, MAC aging time see mac-address-table aging-time command configuration for more details. MAC Limit Displays the VPN MAC limit. It can be configured. MPLS VC labels Displays the exchanged labels information for VPLS service. Pw-type Displays the VFI pseudowire encapsulation type. Remote access interface state Displays the neighbor access interface operational state. Split-horizon Displays the split-horizon forwarding mode. Tunnel interface Displays the tunnel interface name. Up Time Displays the total time that the PW has been Up and running. Output Description VPLS-Group Displays the VPLS group name associated with that entry. VPN-Name Displays the VPN name associated with that entry. Displays the Flow-Aware Transport(FAT) status for received flows. • true: The local configuration has flow label reception capability enabled and the remote configuration has the flow label transmission capability enabled. Flow-label receive • false: The local configuration doesn’t have flow label reception capability enabled or the remote configuration doesn’t have the flow label transmission capability enabled. Displays the Flow-Aware Transport(FAT) status for transmitted flows. • true: The local configuration has flow label transmission capability enabled and the remote configuration has the flow label reception capability enabled. Flow-label transmit • false: The local configuration doesn’t have flow label transmission capability enabled or the remote configuration doesn’t have the flow label reception capability enabled.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show mpls l2vpn vpws-group`

> **Página:** 1179 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows list of L2VPN entries present on control plane.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls l2vpn vpws-group [ group-name | vpn-name name | group-name vpn-name name ] [ brief | detail ]
```

**Parameters:**

- `brief` — Shows resumed information about the L2VPN control plane. — *Valores:* N/A · *Default:* N/A
- `group-name` — Uses Group name to filter the output. — *Valores:* group name · *Default:* N/A
- `vpn-name name` — Uses VPN name to filter the output. — *Valores:* vpn name · *Default:* N/A
- `detail` — Shows detailed information about the L2VPN control plane. — *Valores:* N/A · *Default:* N/A
- `group-name` — Uses Group name to filter the output. — *Valores:* group name · *Default:* N/A
- `vpn-name name` — Uses VPN name to filter the output. — *Valores:* vpn name · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. Backup PW state was introduced. Update show brief to display the VPN 6.0 operational state instead of administrative status. |

**Usage Guidelines:**

To simply show the list of MPLS L2VPN present on control plane the following command can be used: Example:

```text
# show mpls l2vpn vpws-group brief
```

Oper Oper Oper Redundancy Redundancy VPWS-Group VPN-Name State Segment-1 State Segment-2 Pw-ID State Role State ---------------------------------------------------------------------------------------------------------------- California Eureka up gigabit-ethernet-1/1/1 up 172.0.10.120 12503 up main active 172.0.10.150 22500 up backup standby Illinois Fresno up gigabit-ethernet-1/1/2 up 172.0.10.160 99222 up - - Chicago up gigabit-ethernet-1/1/3 up 172.0.10.177 12123 up - - It is possible to filter the results by VPWS Group and VPN Name. Filter by VPWS Group: Example:

```text
# show mpls l2vpn vpws-group Illinois brief
VPWS-Group: Illinois;
```

Oper Oper Oper Redundancy Redundancy VPN-Name State Segment-1 State Segment-2 Pw-ID State Role State ---------------------------------------------------------------------------------------------------- Fresno up gigabit-ethernet-1/1/2 up 172.0.10.160 99222 up - - Chicago up gigabit-ethernet-1/1/3 up 172.0.10.177 12123 up - - Filter by VPWS Group and VPN Name: Example:

```text
# show mpls l2vpn vpws-group Illinois vpn-name Chicago brief
```

VPN-Name: Chicago; Oper state: up; AC: gigabit-ethernet-1/1/3; Oper state: up; PW: Neighbor address: 172.0.10.177; Oper state: up; Pw-ID: 12123; Redundancy: Role: n/a; Local state: n/a To simply show the detailed list of MPLS L2VPN present on control plane the following command can be used: Example:

```text
# show mpls l2vpn vpws-group detail
VPWS-Group: California;
```

VPN-Name: Eureka; Admin Status: up; Oper state: up; AC: gigabit-ethernet-1/1/1; Admin Status: up; Oper state: up; Encapsulation Dot1q: 10,20,30-50 PW: Neighbor address: 172.0.10.120; Admin Status: up; Oper state: up; Up time: 0 day(s) 0 hour(s) 1 minute(s) 30 second(s); Last state change time: Thu Sep 21 15:24:17 2017; Pw-ID: 12503; Pw-type: vlan 2017; Tunnel interface: ldp; FAT: Flow-label receive: true; Flow-label transmit: false; Remote access interface state: up; MPLS VC labels: Local: 37; Remote: 57; MTU: Local: 1500; Remote: 1500; Signaling protocol: ldp; Redundancy: Role: main; Local active: none; Remote state: active; PW: Neighbor address: 172.0.10.150; Admin Status: up; Oper state: dormant; Up time: 0 day(s) 0 hour(s) 0 minute(s) 0 second(s); Last state change time: Thu Sep 21 15:24:17 2017; Pw-ID: 22500; Pw-type: vlan 2017; Tunnel interface: ldp; FAT: Flow-label receive: true; Flow-label transmit: false; Remote access interface state: up; MPLS VC labels: Local: 14: Remote: 18; MTU: Local: 1500; Remote: 1500; Signaling protocol: ldp; Redundancy: Role: backup; Local state: standby; Remote state: active; VPN-Name: Fresno; Admin Status: up; Oper state: up; AC: gigabit-ethernet-1/1/2; Admin Status: up; Oper state: up; Encapsulation Dot1q: 10,20,30-50,untagged PW: Neighbor address: 172.0.10.160; Admin Status: up; Oper state: up; Up time: 0 day(s) 0 hour(s) 1 minute(s) 28 second(s); Last state change time: Thu Sep 21 15:24:20 2017; Pw-ID: 99222; Pw-type: vlan 2017; Tunnel interface: tunnel-te-200; FAT: Flow-label receive: true; Flow-label transmit: false; Remote access interface state: up; MPLS VC labels: Local: 40; Remote: 60; MTU: Local: 1500; Remote: 1500; Signaling protocol: ldp; Redundancy: Role: n/a; Local state: n/a; Remote state: n/a; VPN-Name: Sacramento; Admin Status: up; Oper state: up; AC: gigabit-ethernet-1/1/2; Admin Status: up; Oper state: up; Encapsulation Dot1q: none PW: Neighbor address: 172.0.10.160; Admin Status: up; Oper state: up; Up time: 0 day(s) 0 hour(s) 2 minute(s) 38 second(s); Last state change time: Thu Sep 21 15:24:20 2017; Pw-ID: 3314; Pw-type: vlan 2017; Tunnel interface: tunnel-te-300; FAT: Flow-label receive: true; Flow-label transmit: false; Remote access interface state: up; MPLS VC labels: Local: 40; Remote: 60; MTU: Local: 1500; Remote: 1500; Signaling protocol: ldp; Redundancy: Role: n/a; Local state: n/a; Remote state: n/a; VPWS-Group: Illinois; VPN-Name: Chicago; Admin Status: up; Oper state: up; AC: gigabit-ethernet-1/1/3; Admin Status: up; Oper state: up; Encapsulation Dot1q: untagged PW: Neighbor address: 172.0.10.177; Admin Status: up; Oper state: up; Up time: 0 day(s) 0 hour(s) 1 minute(s) 15 second(s); Last state change time: Thu Sep 21 15:24:18 2017; Pw-ID: 12123; Pw-type: vlan 2017; Tunnel interface: ldp; FAT: Flow-label receive: true; Flow-label transmit: false; Remote access interface state: up; MPLS VC labels: Local: 22; Remote: 21; MTU: Local: 1500; Remote: 1500; Signaling protocol: ldp; Redundancy: Role: n/a; Local state: n/a; Remote state: n/a; It is possible to filter the results by VPWS Group and VPN Name. Filter by VPWS Group: Example:

```text
# show mpls l2vpn vpws-group Illinois detail
VPWS-Group: Illinois;
```

VPN-Name: Chicago; Admin Status: up; Oper state: up; AC: gigabit-ethernet-1/1/3; Admin Status: up; Oper state: up; Encapsulation Dot1q: untagged PW: Neighbor address: 172.0.10.177; Admin Status: up; Oper state: up; Up time: 0 day(s) 0 hour(s) 1 minute(s) 15 second(s); Last state change time: Thu Sep 21 15:24:18 2017; Pw-ID: 3; Pw-type: vlan 2017; Tunnel interface: ldp; FAT: Flow-label receive: true; Flow-label transmit: false; Remote access interface state: up; MPLS VC labels: Local: 22; Remote: 21; MTU: Local: 1500; Remote: 1500; Signaling protocol: ldp; Redundancy: Role: n/a; Local state: n/a; Remote state: n/a; Filter by VPWS Group and VPN Name: Example:

```text
# show mpls l2vpn vpws-group Illinois vpn-name Chicago
```

VPN-Name: Chicago; Admin Status: up; Oper state: up; AC: gigabit-ethernet-1/1/3; Admin Status: up; Oper state: up; Encapsulation Dot1q: untagged PW: Neighbor address: 172.0.10.177; Admin Status: up; Oper state: up; Up time: 0 day(s) 0 hour(s) 1 minute(s) 15 second(s); Last state change time: Thu Sep 21 15:24:18 2017; Pw-ID: 3; Pw-type: vlan 2017; Tunnel interface: ldp; FAT: Flow-label receive: true; Flow-label transmit: false; Remote access interface state: up; MPLS VC labels: Local: 22; Remote: 21; MTU: Local: 1500; Remote: 1500; Signaling protocol: ldp; Redundancy: Role: n/a; Local state: n/a; Remote state: n/a;

**Output Terms:**

Output Description VPWS-Group Display the VPWS group name associated with entry. VPN-Name Display the VPN name associated with entry. Oper State Display the MPLS VPN status associated with entry. Segment-1 Display the access interface id associated with entry. Display the MPLS access status associated with entry. • up: The interface is ready to pass packets. Oper State • down: The interface is admin down and deprogrammed. Segment-2 Display the neighbor id associated with entry. Pw-ID Display the PW id associated with entry. Output Description Display the MPLS uplink status associated with entry. • up: The PW is ready to pass packets. • down: The PW is admin down and deprogrammed. • dormant: The PW is not in a condition to pass packets. It is waiting for signaling to complete. Oper State • lowerLayerDown: One or more of the lower-layer interfaces is not in OperStatus ‘up’ state. • failed: The PW is admin up but has failed to go operationally Up. It is not ready to pass packets because of a local or remote failure. Display the Role associated with entry. Empty if the PW does not have backup neighbor configured. Redundancy Role • main: The PW is the main neighbor associated with entry. • backup: The PW is the backup neighbor associated with entry. Display the status associated with entry. Empty if the PW does not have backup neighbor configured. • active: The PW is active and ready to pass packets. Redundancy State • standby: The PW is standby and could be ready to pass packets if the other neighbor is down.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A L3VPN


## L3VPN

### `show mpls l3vpn`

> **Página:** 1186 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information regarding L3VPN prefixes.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls l3vpn { vpnv4 | vpnv6 } vrf vrf-name brief
```

**Parameters:**

- `vrf vrf-name` — VRF used to filter the output. — *Valores:* Name of VRF or all VRFs. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.0 | The vpnv6 parameter was added. |

**Usage Guidelines:**

To simply show MPLS L3VPN information, the following command can be used: Example:

```text
# show mpls l3vpn vpnv4 vrf all brief
In Out Out
```

VRF-name Prefix Next-hop Action Label Label Interface Status --------------------------------------------------------------------------------- VRF_GREEN -- -- pop 16 -- VRF_GREEN active VRF_GREEN 1.1.1.0/24 200.200.200.2/32 psh -- 17 tunnel-ldp active VRF_GREEN 2.1.1.0/24 200.200.200.2/32 psh -- 17 tunnel-ldp active VRF_RED -- -- pop 17 -- VRF_RED active VRF_RED 1.1.1.0/24 200.200.200.2/32 psh -- 16 tunnel-ldp active VRF_RED 2.1.1.0/24 200.200.200.2/32 psh -- 16 tunnel-ldp active

```text
DM4270# show mpls l3vpn vpnv6 vrf all brief
In Out Out
```

VRF-name Prefix Next-hop Action Label Label Interface Status ----------------------------------------------------------------------------------- VRF_GREEN 2001:1::/64 ::ffff:4.4.4.1 psh -- 16 tunnel-ldp active VRF_GREEN 2001:2::/64 ::ffff:4.4.4.1 psh -- 16 tunnel-ldp active It is possible to filter the output by VRF. Filter by VRF: Example:

```text
# show mpls l3vpn vpnv4 vrf VRF_RED brief
```

**Output Terms:**

Output Description VRF-name Display the VRF in which the L3VPN entry exists. Prefix Display the prefix associated with the L3VPN entry. Next-hop Display the next-hop associated with the L3VPN entry. Output Description Display the MPLS action performed on data plane by the L3VPN entry. • none: no action associated with entry. • psh: tunnel incoming traffic by pushing the outgoing label to Action the packets. • pop: remove incoming label to forward the packet. In Label Display the incoming label associated with the L3VPN entry. Out Label Display the outgoing label associated with the L3VPN entry. Display the outgoing interface for the MPLS traffic associated with Out Interface the L3VPN entry. The outgoing interface could be an access VRF or the uplink tunnel. Display the status of this rule entry. • Active: indicates entry is active. • Pending: indicates entry has installation pending due to neighStatus bor resolution. • Unused: indicates entry is not in used to forward traffic.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A RSVP


## RSVP

### `interface tunnel-te`

> **Página:** 1190 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure MPLS Traffic Engineering Tunnel interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface tunnel-te id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface tunnel-te id` — Specifies the identifier of the tunnel interface. — *Valores:* 1-65535. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure an MPLS Traffic Engineering Tunnel interface.

```text
# config
(config)# interface tunnel-te 1
```

**Impacts and precautions:**

The tunnel interface destination parameter is mandatory.

**Hardware restrictions:**

N/A


### `interface tunnel-te administrative-status`

> **Página:** 1192 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure MPLS Traffic Engineering Tunnel interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface tunnel-te id administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface tunnel-te id` — Specifies the identifier of the tunnel interface. — *Valores:* 1-65535. · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the tunnel interface. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to set the tunnel interface administrative-status.

```text
# config
(config)# interface tunnel-te 1
(config-tunnel-te-1)# administrative-status up
(config-tunnel-te-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `interface tunnel-te description`

> **Página:** 1194 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies a textual string containing information about the tunnel interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface tunnel-te id description text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface tunnel-te id` — Specifies the identifier of the tunnel interface. — *Valores:* 1-65535. · *Default:* N/A
- `description text` — A textual description of the tunnel interface. — *Valores:* String - maximum 64 characters. Any character is supported. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to add a tunnel interface description.

```text
# config
(config)# interface tunnel-te 1
(config-tunnel-te-1)# description Text
(config-tunnel-te-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `interface tunnel-te destination`

> **Página:** 1196 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies the IPv4 address destination of the tunnel interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface tunnel-te id destination addr
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface tunnel-te id` — Specifies the identifier of the tunnel interface. — *Valores:* 1-65535. · *Default:* N/A
- `destination addr` — Tunnel destination IPv4 address. — *Valores:* a.b.c.d. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure a tunnel interface destination.

```text
# config
(config)# interface tunnel-te 2
(config-tunnel-te-1)# destination 1.1.1.1
(config-tunnel-te-1)# commit
```

**Impacts and precautions:**

The tunnel interface destination address is mandatory.

**Hardware restrictions:**

N/A


### `interface tunnel-te name`

> **Página:** 1198 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Specifies a textual string to identify the tunnel interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface tunnel-te id name text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface tunnel-te id` — Specifies the identifier of the tunnel interface. — *Valores:* 1-65535. · *Default:* N/A
- `name text` — A textual string to represent a tunnel interface. — *Valores:* String - maximum 32 characters. Characters supported are ‘a-z’, ‘A-Z’, ‘0-9’, ’_‘and’-’. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to add a tunnel interface name.

```text
# config
(config)# interface tunnel-te 1
(config-tunnel-te-1)# name tunnel1
(config-tunnel-te-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `interface tunnel-te path-option`

> **Página:** 1200 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** A tunnel interface can have six path options associated with different priorities. The path option with a lower priority value is tried first. If this path is unavailable in the CSPF database, the next path option with lower priority value is tried.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface tunnel-te id path-option prio
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface tunnel-te id` — Specifies the identifier of the tunnel interface. — *Valores:* 1-65535. · *Default:* N/A
- `path-option prio` — Priority for the path option. — *Valores:* 1-255. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure a tunnel interface path-option priority.

```text
# config
(config)# interface tunnel-te 1
(config-tunnel-te-1)# path-option 1
(config-tunnel-te-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `interface tunnel-te path-option`

> **Página:** 1202 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable or disable a specific path option.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface tunnel-te id path-option prio [enable | disable]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface tunnel-te id` — Specifies the identifier of the tunnel interface. — *Valores:* 1-65535. · *Default:* N/A
- `path-option prio` — Priority for the path option. — *Valores:* 1-255. · *Default:* N/A
- `status` — Enables or disables the path option. — *Valores:* enable | disable. · *Default:* enable.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to disable and enable a specific tunnel interface path-option.

```text
# config
(config)# interface tunnel-te 1
(config-tunnel-te-1)# path-option 1 disable
(config-tunnel-te-1)# commit
(config-tunnel-te-1)# path-option 1 enable
(config-tunnel-te-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `interface tunnel-te path-option dynamic attribute-set`

> **Página:** 1205 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Set of attributes that are associated with the dynamic path-option. The CSPF uses these attributes information on the tunnel ingress to determine whether the path can be established for a specific destination or not.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface tunnel-te id path-option prio dynamic attribute-set attribute
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface tunnel-te id` — Specifies the identifier of the tunnel interface. — *Valores:* 1-65535. · *Default:* N/A
- `path-option prio` — Priority for the path option. — *Valores:* 1-255. · *Default:* N/A
- `dynamic attribute-set attribute` — Specifies the attributes that are associated with a dynamic path-option. The attribute-set must be created in the mpls traffic-eng configuration. — *Valores:* Any attribute-set created in the mpls traffic-eng configuration. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to associated an attribute-set in a dynamic path-option.

```text
# config
(config)# interface tunnel-te 1
(config-tunnel-te-1)# path-option 1 dynamic attribute-set Set1
(config-tunnel-te-1)# commit
```

It is not possible to configure both dynamic and explicit path within the same path-option, nor the same tunnel interface.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `interface tunnel-te path-option explicit name`

> **Página:** 1208 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Set of nodes that are associated with the explicit path-option.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface tunnel-te id path-option prio explicit name explicit-path
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface tunnel-te id` — Specifies the identifier of the tunnel interface. — *Valores:* 1-65535. · *Default:* N/A
- `path-option prio` — Priority for the path option. — *Valores:* 1-255. · *Default:* N/A
- `explicit name explicit-path` — Specifies the path that is associated with an explicit path-option. The explicit-path must be created in the mpls traffic-eng configuration. — *Valores:* Any explicit-path created in the mpls traffic-eng configuration. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 7.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to associated an explicit-path in a path-option.

```text
# config
(config)# interface tunnel-te 1
(config-tunnel-te-1)# path-option 1 explicit name Seattle
(config-tunnel-te-1)# commit
```

It is not possible to configure both dynamic and explicit path within the same path-option, nor the same tunnel interface.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls rsvp`

> **Página:** 1211 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable Resource Reservation Protocol (RSVP) that provides traffic management capabilities.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls rsvp
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls rsvp` — Enable Resource Reservation Protocol. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the RSVP.

```text
# config
(config)# mpls rsvp
(config-rsvp)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls rsvp hello`

> **Página:** 1213 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure MPLS RSVP Hello settings.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls rsvp hello { [enabled|disabled] [interval time in milliseconds] [retry number of retries] }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `enabled | disabled` — Enables/Disables the hello. — *Valores:* n/a · *Default:* enabled
- `interval time in milliseconds` — Average interval between hello messages. — *Valores:* 500-60000 · *Default:* 3000
- `retry number of retries` — The number of sequential hello acks that can be missed before considering the partner is down. — *Valores:* 2-10 · *Default:* 3

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to change the rsvp hello configuration values.

```text
# config
(config)# mpls rsvp hello interval 10000 retry 5
(config-rsvp)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls rsvp interface`

> **Página:** 1215 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable Resource Reservation Protocol (RSVP) capabilities in a specific interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls rsvp interface interface-name [max-reservable-bandwidth value]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls rsvp` — Enable Resource Reservation Protocol. — *Valores:* N/A · *Default:* N/A
- `interface interface-name` — Enable RSVP capabilities in an L3 interface. The L3 interface must be created. — *Valores:* any L3 interface. · *Default:* N/A
- `max-reservable-bandwidth value` — Configure the maximum reservable bandwidth (in Mbps) for RSVP Bandwidth Reservation of the interface. If no value is configured, the interface will not deny any tunnel establishment. — *Valores:* 0-1000000 - Value in Mbps, where 0 only allows connection of tunnels with 0 Mbps of reservation request or without reservation request configured. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |
| 10.0 | Support for max-reservable-bandwidth configuration. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to enable RSVP capabilities in an L3 interface.

```text
# config
(config)# mpls rsvp
(config-rsvp)# interface l3-vlan1
(config-rsvp)# max-reservable-bandwidth 1000
(config-interface-l3-vlan1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls rsvp refresh`

> **Página:** 1218 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure MPLS RSVP refresh settings.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls rsvp refresh
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interval time in milliseconds` — Average interval between refresh messages. — *Valores:* 1000-86400000 · *Default:* 30000
- `retry number of retries` — Number of consecutive attempts to send a refresh without receiving a response. — *Valores:* 2-10 · *Default:* 3

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 8.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to change the rsvp refresh configuration values.

```text
# config
(config)# mpls rsvp refresh interval 15000 retry 5
(config-rsvp)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls traffic-eng`

> **Página:** 1220 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable MPLS traffic engineering that ensures Quality of Service (QoS) for data transmission.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls traffic-eng
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls traffic-eng` — Enable MPLS traffic engineering. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to enable MPLS traffic engineering.

```text
# config
(config)# mpls traffic-eng
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls traffic-eng attribute-set`

> **Página:** 1222 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Set of attributes to be used by MPLS traffic engineering.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls traffic-eng attribute-set
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls traffic-eng` — Enable MPLS traffic engineering. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng attribute-set` — Enable MPLS traffic engineering attributes. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure MPLS traffic engineering attributes.

```text
# config
(config)# mpls traffic-eng
(config-traffic-eng)# attribute-set
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls traffic-eng attribute-set path-option`

> **Página:** 1224 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure an MPLS traffic engineering (MPLS-TE) dynamic path to be associated with a tunnel interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls traffic-eng attribute-set path-option text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls traffic-eng` — Enable MPLS traffic engineering. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng attribute-set` — Enable MPLS traffic engineering attributes. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng attribute-set path-option text` — A textual string to represent a path-option. — *Valores:* String - maximum 32 characters. Characters supported are ‘a-z’, ‘A-Z’, ‘0-9’, ’_‘and’-’. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the path option attribute-set.

```text
# config
(config)# mpls traffic-eng
(config-traffic-eng)# attribute-set
(config-attribute-set)# path-option Seattle
(config-path-option-Seattle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls traffic-eng attribute-set path-option affinity-flags exclude-any`

> **Página:** 1227 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Affinity flags attribute configured to define a path option. The path will be valid if any link to a destination does not have any affinity-flag bits in the CSPF calculation base.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls traffic-eng attribute-set path-option text affinity-flags exclude-any flag
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls traffic-eng` — Enable MPLS traffic engineering. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng attribute-set` — Enable MPLS traffic engineering attributes. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng attribute-set path-option text` — A textual string to represent a path-option. — *Valores:* String - maximum 64 characters. · *Default:* N/A
- `mpls traffic-eng attribute-set path-option text affinity-flags exclude-any flag` — Affinity attribute values to be any excluded. — *Valores:* Hexadecimal in lower-case - 0x0-0xffffffff · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the path option attribute-set to exclude any affinity-flag bits.

```text
# config
(config)# mpls traffic-eng
(config-traffic-eng)# attribute-set
(config-attribute-set)# path-option Seattle
(config-path-option-Seattle)# affinity-flags exclude-any 0xa
(config-path-option-Seattle)# commit
```

**Impacts and precautions:**

A path can have different affinity statements associated at the same time.

**Hardware restrictions:**

N/A


### `mpls traffic-eng attribute-set path-option affinity-flags include-all`

> **Página:** 1230 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Affinity flags attribute configured to define a path option. The path will be valid if each link to a destination has the same affinity-flag bits in the CSPF calculation base.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls traffic-eng attribute-set path-option text affinity-flags include-all flag
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls traffic-eng` — Enable MPLS traffic engineering. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng attribute-set` — Enable MPLS traffic engineering attributes. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng attribute-set path-option text` — A textual string to represent a path-option. — *Valores:* String - maximum 64 characters. · *Default:* N/A
- `mpls traffic-eng attribute-set path-option text affinity-flags include-all flag` — Affinity attribute values to be all included. — *Valores:* Hexadecimal in lower-case - 0x0-0xffffffff · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the path option attribute-set to include all affinity-flag bits.

```text
# config
(config)# mpls traffic-eng
(config-traffic-eng)# attribute-set
(config-attribute-set)# path-option Seattle
(config-path-option-Seattle)# affinity-flags include-all 0xa
(config-path-option-Seattle)# commit
```

**Impacts and precautions:**

A path can have different affinity statements associated at the same time.

**Hardware restrictions:**

N/A


### `mpls traffic-eng attribute-set path-option affinity-flags include-any`

> **Página:** 1233 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Affinity flags attribute configured to define a path option. The path will be valid if all links to a destination have at least one affinity-flag bit in the CSPF calculation base.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls traffic-eng attribute-set path-option text affinity-flags include-any flag
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls traffic-eng` — Enable MPLS traffic engineering. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng attribute-set` — Enable MPLS traffic engineering attributes. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng attribute-set path-option text` — A textual string to represent a path-option. — *Valores:* String - maximum 64 characters. · *Default:* N/A
- `mpls traffic-eng attribute-set path-option text affinity-flags include-any flag` — Affinity attribute values to be any included. — *Valores:* Hexadecimal in lower-case - 0x0-0xffffffff · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the path option attribute-set to include any affinity-flag bits.

```text
# config
(config)# mpls traffic-eng
(config-traffic-eng)# attribute-set
(config-attribute-set)# path-option Seattle
(config-path-option-Seattle)# affinity-flags include-any 0xa
(config-path-option-Seattle)# commit
```

**Impacts and precautions:**

A path can have different affinity statements associated at the same time.

**Hardware restrictions:**

N/A


### `mpls traffic-eng explicit-path`

> **Página:** 1236 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure an MPLS traffic engineering (MPLS-TE) explicit path to be associated with a tunnel interface. It consists of a series of nodes through which the MPLS-TE tunnel will be established.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls traffic-eng explicit-path text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls traffic-eng` — Enable MPLS traffic engineering. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng explicit-path text` — A textual string to represent a explicit-path. — *Valores:* String - maximum 48 characters. Characters supported are ‘a-z’, ‘A-Z’, ‘0-9’, ’_‘and’-’. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 7.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the path option explicit-path.

```text
# config
(config)# mpls traffic-eng
(config-traffic-eng)# explicit-path Seattle
(config-explicit-path-Seattle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls traffic-eng explicit-path hop`

> **Página:** 1238 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure a node in an explicit path with its attributes, including the IP address and hop type.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls traffic-eng explicit-path text hop id ipv4 next-address addr hop-type
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls traffic-eng` — Enable MPLS traffic engineering. — *Valores:* N/A · *Default:* N/A
- `mpls traffic-eng explicit-path text` — A textual string to represent a explicit-path. — *Valores:* String - maximum 48 characters. Characters supported are ‘a-z’, ‘A-Z’, ‘0-9’, ’_‘and’-’. · *Default:* N/A
- `mpls traffic-eng explicit-path text hop id` — Index of a node on the explicit-path. — *Valores:* 1-65535. · *Default:* N/A
- `mpls traffic-eng explicit-path text hop id ipv4 next-address addr` — The IPv4 address of a node on the explicit-path. It must be unique in current explicit-path. — *Valores:* a.b.c.d. · *Default:* N/A
- `mpls traffic-eng explicit-path text hop id ipv4 next-address addr hop-type` — The connection to a node on the explicit-path. A strict hop is directly connected to its next hop, while for loose hop, other nodes may exist between them. — *Valores:* loose | strict. · *Default:* strict.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 7.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the path option explicit-path to include a series of hops.

```text
# config
(config)# mpls traffic-eng
(config-traffic-eng)# explicit-path Seattle
(config-explicit-path-Seattle)# hop 42 ipv4 next-address 1.2.3.4 strict
(config-explicit-path-Seattle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls traffic-eng interface`

> **Página:** 1241 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable MPLS traffic engineering capabilities in a specific interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls traffic-eng interface interface-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls traffic-eng` — Enable MPLS traffic engineering. — *Valores:* N/A · *Default:* N/A
- `interface interface-name` — Enable MPLS traffic engineering capabilities in a specific L3 interface. The L3 interface must be created. — *Valores:* any L3 interface. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to enable MPLS traffic engineering capabilities in an L3 interface.

```text
# config
(config)# mpls traffic-eng
(config-traffic-eng)# attribute-set
(config-attribute-set)# interface l3-vlan1
(config-interface-l3-vlan1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls traffic-eng interface affinity-flags`

> **Página:** 1243 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable affinity-flag bits in a specific L3 interface. The IGP advertises the affinity-flag to devices in the same IGP area. Then the CSPF on the ingress uses this information to determine whether a link can be used to establish an RSVP-TE path or not.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4615, DM4610, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls traffic-eng interface interface-name affinity-flags flag
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls traffic-eng` — Enable MPLS traffic engineering. — *Valores:* N/A · *Default:* N/A
- `interface interface-name` — Enable MPLS traffic engineering capabilities in a specific L3 interface. The L3 interface must be created. — *Valores:* any L3 interface. · *Default:* N/A
- `affinity-flags flag` — Affinity-flag value to be used by a specific L3 interface. — *Valores:* Hexadecimal in lower-case - 0x0-0xffffffff · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to enable MPLS traffic engineering capabilities in an L3 interface.

```text
# config
(config)# mpls traffic-eng
(config-traffic-eng)# attribute-set
(config-attribute-set)# interface l3-vlan1
(config-interface-l3-vlan1)# affinity-flags 0xa
(config-interface-l3-vlan1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A LDP This topic describes the commands related to management of Label Distribution Protocol such as commands to configure LDP parameters or to inspect the protocol status.


## LDP

### `mpls ldp lsr-id`

> **Página:** 1246 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a LSR-ID that uniquely identifies the label switch router (LSR) within the network and enables MPLS LDP in the device. This configuration is mandatory to enable LDP in the device.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls ldp lsr-id loopback-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `loopback-name` — Specifies a loopback interface for the label switching router. — *Valores:* Any loopback interface. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the LDP lsr id.

```text
# config
(config)# mpls ldp lsr-id loopback-1
(config-lsr-id-loopback-1)# commit
```

**Impacts and precautions:**

The loopback interface to be used as an LDP LSR identifier must be previously created. In addition, it must be configured with an IPv4 address and a /32 netmask.

**Hardware restrictions:**

N/A


### `mpls ldp lsr-id interface`

> **Página:** 1248 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables LDP basic discovery on the specified interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls ldp lsr-id loopback-name interface interface-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `loopback-name` — Specifies a loopback interface for the label switching router. The loopback interface must be created. — *Valores:* Any loopback interface. · *Default:* N/A
- `interface-name` — Specifies the L3 interfaces for LDP basic discovery. The L3 interfaces must be created. — *Valores:* any L3 interface. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to enable LDP basic discovery on the interface.

```text
# config
(config)# mpls ldp lsr-id loopback-1 interface l3-vlan1
(config-interface-l3-vlan1)# commit
```

**Impacts and precautions:**

The l3 interface to be used for LDP basic discovery must be previously created. In addition, it must be configured with an IPv4 address.

**Hardware restrictions:**

N/A


### `mpls ldp lsr-id interface hello-holdtime`

> **Página:** 1250 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the Hello hold timer for this LDP Basic Discovery.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls ldp lsr-id loopback-name interface interface-name hello-holdtime seconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `loopback-name` — Specifies a loopback interface for the label switching router. The loopback interface must be created. — *Valores:* Any loopback interface. · *Default:* N/A
- `interface-name` — Specifies the L3 interfaces for LDP basic discovery. The L3 interfaces must be created. — *Valores:* any L3 interface. · *Default:* N/A
- `hello-holdtime` — Hello hold timer for the LDP Basic Discovery. — *Valores:* 1-65535. · *Default:* 15.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the LDP interface Hello holdtime.

```text
# config
(config)# mpls ldp lsr-id loopback-1
(config-lsr-id-loopback-1)# interface l3-vlan1
(config-interface-l3-vlan1)# hello-holdtime 20
(config-interface-l3-vlan1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls ldp lsr-id interface keep-alive-holdtime`

> **Página:** 1253 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the Keep alive hold timer for this LDP Basic Discovery.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls ldp lsr-id loopback-name interface interface-name keep-alive-holdtime seconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `loopback-name` — Specifies a loopback interface for the label switching router. The loopback interface must be created. — *Valores:* Any loopback interface. · *Default:* N/A
- `interface-name` — Specifies the L3 interfaces for LDP basic discovery. The L3 interfaces must be created. — *Valores:* any L3 interface. · *Default:* N/A
- `keep-alive-holdtime` — Keep alive hold timer for the LDP Basic Discovery. — *Valores:* 1-65535. · *Default:* 40.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the LDP interface Keep alive holdtime.

```text
# config
(config)# mpls ldp lsr-id loopback-1
(config-lsr-id-loopback-1)# interface l3-vlan1
(config-interface-l3-vlan1)# keep-alive-holdtime 50
(config-interface-l3-vlan1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls ldp lsr-id neighbor targeted`

> **Página:** 1256 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables LDP extended discovery with the specified internetwork layer address.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls ldp lsr-id loopback-name neighbor targeted address
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `loopback-name` — Specifies a loopback interface for the label switching router. The loopback interface must be created. — *Valores:* Any loopback interface. · *Default:* N/A
- `address` — The internetwork layer address used for the extended discovery. — *Valores:* any IPv4 address. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to enable LDP extended discovery with the specified internetwork layer address.

```text
# config
(config)# mpls ldp lsr-id loopback-1 neighbor targeted 9.9.9.9
(config-neighbor-9.9.9.9)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls ldp lsr-id neighbor targeted hello-holdtime`

> **Página:** 1258 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the Hello hold timer for this LDP Extended Discovery.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls ldp lsr-id loopback-name neighbor targeted address hello-holdtime seconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `loopback-name` — Specifies a loopback interface for the label switching router. The loopback interface must be created. — *Valores:* Any loopback interface. · *Default:* N/A
- `address` — The value of the internetwork layer address used for the Extended Discovery. — *Valores:* any IPv4 address. · *Default:* N/A
- `hello-holdtime` — Hello hold timer for the LDP Extended Discovery. — *Valores:* 1-65535. · *Default:* 45.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the Hello holdtime.

```text
# config
(config)# mpls ldp lsr-id loopback-1
(config-lsr-id-loopback-1)# neighbor targeted 9.9.9.9
(config-neighbor-9.9.9.9)# hello-holdtime 20
(config-neighbor-9.9.9.9)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls ldp lsr-id neighbor targeted keep-alive-holdtime`

> **Página:** 1261 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the Keep alive hold timer for this LDP Extended Discovery.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls ldp lsr-id loopback-name neighbor targeted address keep-alive-holdtime seconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `loopback-name` — Specifies a loopback interface for the label switching router. The loopback interface must be created. — *Valores:* Any loopback interface. · *Default:* N/A
- `address` — The value of the internetwork layer address used for the Extended Discovery. — *Valores:* any IPv4 address. · *Default:* N/A
- `keep-alive-holdtime` — Keep alive hold timer for the LDP Extended Discovery. — *Valores:* 1-65535. · *Default:* 40.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the Keep alive holdtime.

```text
# config
(config)# mpls ldp lsr-id loopback-1
(config-lsr-id-loopback-1)# neighbor targeted 9.9.9.9
(config-neighbor-9.9.9.9)# keep-alive-holdtime 50
(config-neighbor-9.9.9.9)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `mpls ldp lsr-id neighbor targeted password`

> **Página:** 1264 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the neighbor to use Message-Digest algorithm 5 (MD5) authentication on the TCP connection between LDP peers.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
mpls ldp lsr-id loopback-name neighbor targeted address password pwd
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `loopback-name` — Specifies a loopback interface for the label switching router. The loopback interface must be created. — *Valores:* Any loopback interface. · *Default:* N/A
- `address` — The value of the internetwork layer address used for the Extended Discovery. — *Valores:* any IPv4 address. · *Default:* N/A
- `password pwd` — Specifies the LDP neighbor case-sensitive password to be used between the TCP peer connection. — *Valores:* string (length 2 - 80). · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure the LDP password.

```text
# config
(config)# mpls ldp lsr-id loopback-1
(config-lsr-id-loopback-1)# neighbor targeted 9.9.9.9
(config-neighbor-9.9.9.9)# password pwdTest
(config-neighbor-9.9.9.9)# commit
```

This example shows the configuration of a neighbor password using an already encrypted password.

```text
# config
(config)# mpls ldp lsr-id loopback-1
(config-lsr-id-loopback-1)# neighbor targeted 9.9.9.9
(config-neighbor-50.50.50.1)# password "hls:2922743918:337ZpL=Z"
(config-neighbor-50.50.50.1)# commit
```

This example shows the configuration of a neighbor password using special characters (i.e: " " , “?” , “!” , “;”). Please note that it is necessary to use double quotation marks in this case.

```text
# config
(config)# mpls ldp lsr-id loopback-1
(config-lsr-id-loopback-1)# neighbor targeted 9.9.9.9
(config-neighbor-50.50.50.1)# password "pwd?test:2"
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

Password must be enclosed in double quotation marks if special characters were used (i.e: " " , “?” , “!” , “;”). Note that in an established LDP session if password is configured or changed the session will be restarted.

**Hardware restrictions:**

N/A


### `show mpls ldp database`

> **Página:** 1267 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** This command shows a list of all labels present in LDP database, including non-selected labels, marked with NS, which are not installed. (not used to forward packets).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls ldp database [ ** prefix ** ]
```

**Parameters:**

- `prefix ipv4-prefix` — Use Network Prefix to filter the output. — *Valores:* a.b.c.d/x · *Default:* N/A.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 2.4 | This command was updated. |

**Usage Guidelines:**

Every label mapping received from a peer LSR is retained regardless of whether the LSR is the active next hop for the advertised mapping or not. Only the label received from the current next hop will be installed. This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to use this command.

```text
# show mpls ldp database
```

State codes: A - active, NS - not selected DownStream Network Prefix UpStream LSR-ID Label LSR-ID Label State -------------------------------------------------------------------------------- 1.1.1.1/32 4.4.4.4 19 -- -- A 1.1.1.1/32 5.5.5.5 19 -- -- A 1.1.1.1/32 8.8.8.8 19 -- -- A 2.2.2.2/32 4.4.4.4 17 -- -- A 2.2.2.2/32 5.5.5.5 17 -- -- A 2.2.2.2/32 8.8.8.8 17 -- -- A 1.1.1.1/32 -- -- 2.2.2.2 179 A 1.1.1.1/32 -- -- 4.4.4.4 133 NS 1.1.1.1/32 -- -- 5.5.5.5 26 NS 2.2.2.2/32 -- -- 2.2.2.2 3 A 2.2.2.2/32 -- -- 4.4.4.4 38 NS 2.2.2.2/32 -- -- 5.5.5.5 85 NS

```text
# show mpls ldp database 1.1.1.1/32
```

State codes: A - active, NS - not selected DownStream Network Prefix UpStream LSR-ID Label LSR-ID Label State -------------------------------------------------------------------------------- 1.1.1.1/32 4.4.4.4 19 -- -- A 1.1.1.1/32 5.5.5.5 19 -- -- A 1.1.1.1/32 8.8.8.8 19 -- -- A 1.1.1.1/32 -- -- 2.2.2.2 179 A 1.1.1.1/32 -- -- 4.4.4.4 133 NS 1.1.1.1/32 -- -- 5.5.5.5 26 NS

**Output Terms:**

Output Description Network Prefix Indicates a specific FEC present on MPLS LDP database. ID of an upstream LSR to which a label for this FEC was distributed Upstream LSR-ID via a MPLS LDP label mapping message. Label Indicates the label distributed to the upstream LSR. ID of a downstream LSR from which a label was received for this FEC DownStream LSR-ID via a MPLS LDP label mapping message. Output Description Label Indicates the downstream label distributed by the downstream LSR. Indicates the state of a specific FEC. Entries marked with NS are not State installed (not used to forward packets).

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show mpls ldp neighbor`

> **Página:** 1270 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows either summarized or detailed information about LDP sessions.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls ldp neighbor [ brief | detail ]
```

**Parameters:**

- `brief` — Shows summarized information about the MPLS LDP sessions. — *Valores:* N/A · *Default:* N/A
- `detail` — The full output of this command displays general status information about the established LDP sessions (status, role, up-time, remaining keepalive hold time, etc.), negotiated session timer values, and the addresses advertised by the neighbors through LDP Address Messages. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to use this command.

```text
# show mpls ldp neighbor
```

Neighbor LDP-ID State Nbr type ----------------- ------------- --------------- 20.20.20.20:0 Operational linked/targeted 30.30.30.30:0 Operational targeted Local LDP-ID: 222.222.222.222:0; Peer LDP-ID: 20.20.20.20:0; Last change: 00:00:00; State: operational; Role: active; Max ldp pdu: 1440; Protocol version: 1; Local configured KeepAlive (KA) hold time: 40s; Peer’s advertised KA hold time: 40s; Negotiated KeepAlive (KA) hold time: 40s; Negotiated time between KA messages: 7s; KA hold time remaining for this session: 00:00:39s; Remote addresses: 1.1.1.2 4.4.4.2 20.20.20.20 Adjacency: 20.20.20.20:0; - Basic Discovery Mechanism Adjacency discovery hello hold time: 15s; Local discovery hello hold time: 15s; Negotiated discovery hello hold time: 15s; Remaining hello hold time: 14s; Adjacency: 20.20.20.20:0; - Extended Discovery Mechanism Adjacency discovery hello hold time: 45s; Local discovery hello hold time: 45s; Negotiated discovery hello hold time: 45s; Remaining hello hold time: 39s; Local LDP-ID: 222.222.222.222:0; Peer LDP-ID: 30.30.30.30:0; Last change: 00:00:00; State: operational; Role: active; Max ldp pdu: 1440; Protocol version: 1; Local configured KeepAlive (KA) hold time: 40s; Peer’s advertised KA hold time: 40s; Negotiated KeepAlive (KA) hold time: 40s; Negotiated time between KA messages: 7s; KA hold time remaining for this session: 00:00:39s; Remote addresses: 30.30.30.30 4.4.4.1 Adjacency: 30.30.30.30:0; - Extended Discovery Mechanism Adjacency discovery hello hold time: 45s; Local discovery hello hold time: 45s; Negotiated discovery hello hold time: 45s; Remaining hello hold time: 44s;

```text
# show mpls ldp neighbor brief
```

Neighbor LDP-ID State Nbr type ----------------- ------------- --------------- 20.20.20.20:0 Operational linked/targeted 30.30.30.30:0 Operational targeted

```text
# show mpls ldp neighbor detail
```

Local LDP-ID: 222.222.222.222:0; Peer LDP-ID: 20.20.20.20:0; Last change: 00:00:00; State: operational; Role: active; Max ldp pdu: 1440; Protocol version: 1; Local configured KeepAlive (KA) hold time: 40s; Peer’s advertised KA hold time: 40s; Negotiated KeepAlive (KA) hold time: 40s; Negotiated time between KA messages: 7s; KA hold time remaining for this session: 00:00:39s; Remote addresses: 1.1.1.2 4.4.4.2 20.20.20.20 Adjacency: 20.20.20.20:0; - Basic Discovery Mechanism Adjacency discovery hello hold time: 15s; Local discovery hello hold time: 15s; Negotiated discovery hello hold time: 15s; Remaining hello hold time: 14s; Adjacency: 20.20.20.20:0; - Extended Discovery Mechanism Adjacency discovery hello hold time: 45s; Local discovery hello hold time: 45s; Negotiated discovery hello hold time: 45s; Remaining hello hold time: 39s; Local LDP-ID: 222.222.222.222:0; Peer LDP-ID: 30.30.30.30:0; Last change: 00:00:00; State: operational; Role: active; Max ldp pdu: 1440; Protocol version: 1; Local configured KeepAlive (KA) hold time: 40s; Peer’s advertised KA hold time: 40s; Negotiated KeepAlive (KA) hold time: 40s; Negotiated time between KA messages: 7s; KA hold time remaining for this session: 00:00:39s; Remote addresses: 30.30.30.30 4.4.4.1 Adjacency: 30.30.30.30:0; - Extended Discovery Mechanism Adjacency discovery hello hold time: 45s; Local discovery hello hold time: 45s; Negotiated discovery hello hold time: 45s; Remaining hello hold time: 44s;

**Output Terms:**

Output Description Neighbor Indicates the Peer-ID value of the MPLS LDP neighbor. LDP-ID Indicates the label space value of the MPLS LDP neighbor. State Indicates the adjacency state with the MPLS LDP neighbor. Indicates the operation type <targeted/linked> of the MPLS LDP sesNbr type sion.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show mpls ldp parameters`

> **Página:** 1274 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about the current control-plane configuration state of several LDP parameters.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show mpls ldp parameters [ brief ]
```

**Parameters:**

- `brief` — Shows resumed information about the current LDP control-plane configuration. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to use this command.

```text
# show mpls ldp parameters
LSR_ID: 222.222.222.222;
Protocol version: 1;
Allocation mode: Ordered;
Encapsulation mode: PHP implicit-null;
Distribution mode: Unsolicited;
Retention mode: Liberal;
```

Local addresses: 222.222.222.222 1.1.1.1

**Output Terms:**

Output Description LSR_ID Indicates the local Label Switch Router ID. Protocol version Indicates the version of the MPLS LDP protocol. Allocation mode Indicates the advertising FEC-label bindings mode. Encapsulation mode Indicates the MPLS LDP encapsulation mode. Output Description Distribution mode Indicates the label distribution mode. Retention mode Indicates the label retention mode. Indicates the local LDP-enabled interfaces (the IP addresses that are Local addresses advertised by this router to its neighbors through LDP Address Message).

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A CHAPTER 8: MULTICAST This chapter describes the commands related to management of Multicast protocols in the DmOS CLI. IGMP SNOOPING This topic describes the CLI commands related to the IGMP snooping functionality. The IGMP snooping feature allows a network switch to listen to the IGMP protocol messages exchanged between routers and hosts, with the purpose of identifying which host ports are interested on a specific multicast traffic, and sending that traffic only to those ports.
