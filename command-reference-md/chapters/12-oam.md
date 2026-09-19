# Capítulo 12: OAM

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## Continuity Check and Fault Management

### `cfm delay-measurement probe`

> **Página:** 1439 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure CFM delay-measurement probes. Essentially, a probe is the periodic execution of sessions for a specified Maintenance Domain (MD), Maintenance Association (MA), local Maintenance Endpoint (MEP) and, remote MEP. In turn, a session holds all parameters that a user would choose when manually running a troubleshooting command. For each session, consolidated statistics of the last 10 executions are saved and rotated to discard the oldest results.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam cfm delay-measurement probe id md id ma id mep id remote-mep id interval interval oam cfm delay-measurement probe id session id [count value] [pcp value] [interval value] [size value]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `probe id` — Unique probe identifier. — *Valores:* 1 - 512 · *Default:* N/A
- `interval minutes` — The interval between two probe executions, in minutes. — *Valores:* 1 - 1440 · *Default:* 1
- `md id` — Unique Maintenance Domain (MD) identifier that contains the local MEP to issue delay-measurement messages. — *Valores:* String with MD identifier. Only an already created MD is accepted. · *Default:* N/A
- `ma id` — Unique Maintenance Association (MA) identifier that contains the local MEP to issue delay-measurement messages. — *Valores:* String with MA identifier. Only an already created MA is accepted. · *Default:* N/A
- `mep id` — Local MEP ID. Only an existing local MEP is accepted. — *Valores:* 1 - 8191 · *Default:* N/A
- `remote-mep id` — Remote MEP ID. Only an existing remote MEP is accepted. — *Valores:* 1 - 8191 · *Default:* N/A
- `session id` — Unique session identifier. A probe contains up to 8 sessions, where each session has a different PCP (priority code point) value. — *Valores:* 1 - 8 · *Default:* N/A
- `count value` — Number of delay-measurement frames in the session. — *Valores:* 1 - 1024 · *Default:* 10
- `pcp value` — PCP (priority code point) value used in the 802.1Q VLAN tag. — *Valores:* 0 - 7 · *Default:* N/A
- `interval value` — Interval between each delay-measurement frame. — *Valores:* { 1s | 10s | 1min | 10min } · *Default:* 1s
- `size value` — Set delay-measurement frame size; padding is added if necessary. — *Valores:* 64 - 9000 · *Default:* 64

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.10 | This command was introduced. |

**Usage Guidelines:**

Considering the following scenario, with local MEP 11 and remote MEP 12:

```text
# config
(config)# dot1q vlan 10,20,30
(config-vlan-10,20,30)# interface gigabit-ethernet-1/1/2
(config-dot1q-interface-gigabit-ethernet-1/1/2)# top
(config)# oam
(oam)# cfm
(cfm)# md CFM_MD
(cfm-md-CFM_MD)# level 3
(cfm-md-CFM_MD)# ma CFM_MA
(cfm-ma-CFM_MA)# ccm-interval 1s
(cfm-ma-CFM_MA)# remote-meps 12
(cfm-ma-CFM_MA)# vlan-list 10,20,30
(cfm-ma-CFM_MA)# primary-vlan-id 20
(cfm-ma-CFM_MA)# mep 10
(cfm-mep-11)# interface gigabit-ethernet-1/1/2
(cfm-mep-11)# direction up
(cfm-mep-11)# primary-vlan-id 10
(cfm-mep-11)# commit
```

In this example, local MEP 11 will run two delay-measurement sessions to remote MEP 12 every 20 minutes. The first session sends 5 frames with 128 bytes every second to monitor PCP 3, which is tipycally used for voice applications:

```text
(config)# oam cfm delay-measurement probe 1 md CFM_MD ma CFM_MA mep 11
remote-mep 12 interval 20
(cfm-dm-probe-1)# session 1 interval 1s count 5 size 128 pcp 3
```

A second session is used to monitor PCP 1, which usually has the lowest network priority, and will use a different interval and packet size:

```text
(cfm-dm-probe-2)# session 2 interval 10s count 15 size 512 pcp 1
```

To see the consolidated statistics of session 1, run the following command:

```text
# show oam cfm delay-measurement probe 1 session 1
```

LAST LAST LAST ALL ALL ALL AVG AVG LOSS LAST PCP AVG AVG LOSS ALL PCP DELAY JITTER RATIO MISMATCH DELAY JITTER RATIO MISMATCH SESSION PCP (us) (us) % RATIO % (us) (us) % RATIO % ------------------------------------------------------------------------------ 1 3 4493 784 0 0 4493 784 0 0

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `cfm ma`

> **Página:** 1444 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create a Maintenance Association (MA) and configure its parameters.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam cfm md id ma id ccm-interval interval primary-vlan-id vlan-id vlan-list vlan-ids { remote-meps mep-ids }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `md id` — Unique identifier to the MD associated to the MA. — *Valores:* String with a maximum of 43 characters. It only accepts alphanumeric characters and ‘_’, ‘+’ and ‘-’. · *Default:* N/A
- `ma id` — Unique identifier to the MA. — *Valores:* String with a maximum of 43 characters. It only accepts alphanumeric characters and ‘_’, ‘+’ and ‘-’. · *Default:* N/A
- `ccm-interval interval` — Set the interval between CCM transmissions to be used by all MEPs in the MA. — *Valores:* { 1s | 10s | 1min | 10min } · *Default:* N/A
- `primary-vlan-id vlan-id` — Set the MA primary VLAN ID. — *Valores:* 1 - 4094 · *Default:* N/A
- `vlan-list vlan-ids` — Configure VLAN IDs monitored by the MA. Ranges of VLANs or single VLAN are allowed and can be combined to specify the MA VLAN list. Example: vlan-list 1-3,5,7-9 — *Valores:* 1 - 4094 · *Default:* N/A
- `remote-meps mep-ids` — Configure the remote MEPs in the MA. Ranges of MEP IDs or single MEP ID are allowed and can be combined to specify the remote MEP list. Example: remote-meps 1-3,5,7-9 — *Valores:* 1 - 8191 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

To create a CFM Maintenance Association it is necessary to create a valid Maintenance Domain and configure the CCM interval time and a primary VLAN ID. The VLANs of the VLAN list must be created in the equipment. The example below shows the creation of an MA that monitors the VLANs 10, 20 and 30, with VLAN 20 as the primary VLAN ID.

```text
# config
(config)# dot1q vlan 10,20,30
(config-vlan-10,20,30)# top
(config)# oam
(oam)# cfm
(cfm)# md CFM_MD
(cfm-md-CFM_MD)# level 1
(cfm-md-CFM_MD)# ma CFM_MA1
(cfm-ma-CFM_MA1)# ccm-interval 1s
(cfm-ma-CFM_MA1)# vlan-list 10,20,30
(cfm-ma-CFM_MA1)# primary-vlan-id 20
(cfm-ma-CFM_MA1)# remote-meps 10-15
(cfm-ma-CFM_MA1)# commit
```

Commit complete.

```text
(cfm-ma-CFM_MA1)# end
#
```

One-line like command is also supported. The example below shows the creation of another MA.

```text
# config
(config)# dot1q vlan 10
(config-vlan-10)# top
(config)# oam cfm md CFM_MD level 1 ma CFM_MA2 ccm-interval 10s
vlan-list 10 primary-vlan-id 10 remote-meps 2-10
(cfm-ma-CFM_MA2)# commit
```

Commit complete.

```text
(cfm-ma-CFM_MA2)# end
#
```

**Impacts and precautions:**

• The MA is part of an MD and a valid MD configuration is required for the configuration to be committed successfully. • The VLANs in the VLAN list monitored by the MA need to be configured in the equipment for the configuration to be committed successfully.

**Hardware restrictions:**

N/A


### `cfm ma ais`

> **Página:** 1448 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure transmission and reception of Alarm Indication Signal (AIS) frames for a given Maintenance Association (MA). When transmission is enabled, AIS frames are transmitted when a fault is detected, regardless of any alarm configuration and report. When AIS alarm suppression is enabled, alarms are not reported if AIS frames are received.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam cfm md id ma id ais transmission level target-level [interval packets-interval] [vlan-priority priority] [vlan-list vlan-ids] oam cfm md id ma id ais reception alarm-suppression
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `md id` — Unique identifier to the MD associated to the MA. — *Valores:* String with a maximum of 43 characters. It only accepts alphanumeric characters and ‘_’, ‘+’ and ‘-’. · *Default:* N/A
- `ma id` — Unique identifier to the MA. — *Valores:* String with a maximum of 43 characters. It only accepts alphanumeric characters and ‘_’, ‘+’ and ‘-’. · *Default:* N/A
- `ais transmission level target-level` — Destination MD level of the sent AIS packets. The target level must be greater than the MD level where the AIS is configured. — *Valores:* 1 - 7 · *Default:* N/A
- `ais transmission interval packets-interval` — Time interval between AIS packets sending. — *Valores:* {1s | 1min} · *Default:* 1s
- `ais transmission vlan-priority priority` — PCP (802.1p priority) to be used on VLAN Tags for AIS packets. — *Valores:* 0 - 7 · *Default:* 7
- `ais transmission vlan-list vlan-ids` — List of inner VLANs (second VLAN TAGs) which the AIS must be sent with. A copy of the packet is sent with each inner VLAN. The outer VLAN is the MEP’s primary-vlan. Leave it blank when an inner VLAN is unnecessary. VLAN ranges or single VLANs are allowed and can be combined. — *Valores:* 1 - 4094 · *Default:* N/A
- `ais reception alarm-suppression` — Enables the alarm suppression on AIS packet reception. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

To configure AIS transmission it is necessary to create a valid MA and configure all parameters of AIS transmission. AIS reception takes the alarm-suppression parameter only. Transmission and reception can be configured independently.

```text
# config
(config)# dot1q vlan 10,20,30
(config-vlan-10,20,30)# top
(config)# oam
(oam)# cfm
(cfm)# md CFM_MD
(cfm-md-CFM_MD)# level 1
(cfm-md-CFM_MD)# ma CFM_MA1
(cfm-ma-CFM_MA1)# ccm-interval 1s
(cfm-ma-CFM_MA1)# vlan-list 10,20,30
(cfm-ma-CFM_MA1)# primary-vlan-id 20
(cfm-ma-CFM_MA1)#ais transmission
(cfm-ais-tx)# level 3
(cfm-ais-tx)# interval 1min
(cfm-ais-tx)# vlan-list 10
(cfm-ais-tx)# vlan-priority 1
(cfm-ais-rx)# ais reception
(cfm-ais-rx)# alarm-suppression
(cfm-ma-CFM_MA1)# remote-meps 10-15
(cfm-ma-CFM_MA1)# commit
```

Commit complete.

```text
(cfm-ma-CFM_MA1)# end
#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `cfm md`

> **Página:** 1452 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables Connectivity Fault Management (CFM) and create a Maintenance Domain (MD).

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam cfm md id level md-level
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `md id` — Unique identifier to the MD. — *Valores:* String with a maximum of 43 characters. It only accepts alphanumeric characters and ‘_’, ‘+’ and ‘-’. · *Default:* N/A
- `level md-level` — Set the MD level. — *Valores:* 0 - 7 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

To create a CFM Maintenance Domain it is necessary to configure at least the MD level. The example below shows the creation of an MD.

```text
# config
(config)# oam
(oam)# cfm
(cfm)# md CFM_MD1
(cfm-md-CFM_MD1)# level 5
(cfm-md-CFM_MD1)# commit
```

Commit complete.

```text
(cfm-md-CFM_MD1)# end
#
```

One-line like command is also supported. The example below shows the creation of another MD.

```text
# config
(config)# oam cfm md CFM_MD2 level 6
(cfm-md-CFM_MD2)# commit
```

Commit complete.

```text
(cfm-md-CFM_MD2)# end
#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `cfm mep`

> **Página:** 1454 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create a Maintenance End Point (MEP) and configure its parameters.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam cfm md id ma id mep id interface interface-name direction direction primary-vlan-id vlan-id inner-vlan-id vlan-id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `md id` — Unique identifier to the MD associated to the MA. — *Valores:* String with a maximum of 43 characters. It only accepts alphanumeric characters and ‘_’, ‘+’ and ‘-’. · *Default:* N/A
- `ma id` — Unique identifier to the MA associated to the MEP. — *Valores:* String with a maximum of 43 characters. It only accepts alphanumeric characters and ‘_’, ‘+’ and ‘-’. · *Default:* N/A
- `mep id` — MEP Unique identifier inside the MA. — *Valores:* 1 - 8191 · *Default:* N/A
- `interface interface-name` — Set the interface to which the MEP is attached. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id } · *Default:* N/A
- `direction direction` — Set the direction in which the MEP faces on the interface. — *Valores:* { up | down } · *Default:* N/A
- `primary-vlan-id vlan-id` — Set the MEP primary VLAN ID. — *Valores:* 1 - 4094 · *Default:* N/A
- `inner-vlan-id vlan-id` — Specify the inner VLAN ID (second tag) for this MEP. — *Valores:* 1 - 4094 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |
| 4.9 | Added support for inner tag on MEP. |
| 5.0 | Added support for 25G interfaces. |

**Usage Guidelines:**

To create a CFM Maintenance End Point it is necessary to create a valid Maintenance Association and configure the MEP interface and direction. The interface must be a valid one. The primary VLAN ID specified must be part of the parent MA VLAN list and the MEP interface must be a member of this VLAN. The example below shows the creation of a MEP attached to the VLAN 10.

```text
# config
(config)# dot1q vlan 10,20,30
(config-vlan-10,20,30)# interface gigabit-ethernet-1/1/2
(config-dot1q-interface-gigabit-ethernet-1/1/2)# top
(config)# oam
(oam)# cfm
(cfm)# md CFM_MD
(cfm-md-CFM_MD)# level 3
(cfm-md-CFM_MD)# ma CFM_MA
(cfm-ma-CFM_MA)# ccm-interval 1s
(cfm-ma-CFM_MA)# vlan-list 10,20,30
(cfm-ma-CFM_MA)# primary-vlan-id 20
(cfm-ma-CFM_MA)# mep 1
(cfm-mep-1)# interface gigabit-ethernet-1/1/2
(cfm-mep-1)# direction up
(cfm-mep-1)# primary-vlan-id 10
(cfm-mep-1)# commit
```

Commit complete.

```text
(cfm-mep-1)# end
#
```

One-line like command is also supported. The example below shows the creation of another MEP.

```text
# config
(config)# dot1q vlan 1 interface gigabit-ethernet-1/1/10
(config-dot1q-interface-gigabit-ethernet-1/1/10)# top
(config)# oam cfm md CFM_MD level 3 ma CFM_MA ccm-interval 1s
vlan-list 1 primary-vlan-id 1 mep 2 interface gigabit-ethernet-1/1/10
direction down primary-vlan-id 1
(cfm-mep-2)# commit
```

Commit complete.

```text
(cfm-mep-2)# end
#
```

**Impacts and precautions:**

• The MEP is part of an MA and a valid MA configuration is required for the configuration to be committed successfully. • Only pre-existing interfaces will be accepted when entering an interface name. • Interfaces added as members of a Link Aggregation Group (LAG) cannot be attached in a MEP. The LAG itself should be configured instead. • The primary VLAN ID must be present in the parent MA’s VLAN list. • The MEP interface must be a member of the MEP primary VLAN. • MEPs configured with direction down do not respect VLAN Mapping rules.

**Hardware restrictions:**

N/A


### `cfm mep continuity-check`

> **Página:** 1458 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the Continuity Check Messages (CCM) generation, fault detection and fault notification.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam cfm md id ma id mep id continuity-check { cci-enabled | lowest-faultpriority-defect fault-type | [ fault-action action ] | fault-alarm-time time | faultreset-time time }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `md id` — Unique identifier to the MD associated to the MA. — *Valores:* String with a maximum of 43 characters. It only accepts alphanumeric characters and ‘_’, ‘+’ and ‘-’. · *Default:* N/A
- `ma id` — Unique identifier to the MA associated to the MEP. — *Valores:* String with a maximum of 43 characters. It only accepts alphanumeric characters and ‘_’, ‘+’ and ‘-’. · *Default:* N/A
- `mep id` — MEP Unique identifier inside the MA. — *Valores:* 1 - 8191 · *Default:* N/A
- `cci-enabled` — Enable the MEP’s generation of CCMs. — *Valores:* N/A · *Default:* N/A
- `lowest-fault-priority-defect fault-type` — Set the lowest priority defect that is allowed to generate a Fault Alarm. — *Valores:* { remote-rdi | remote-mac-error | remote-invalid-ccm | invalid-ccm | cross-connect-ccm } · *Default:* N/A
- `fault-alarm-time time` — Set the time (in milliseconds) before a Fault Alarm is issued (100ms step). — *Valores:* { 2500 - 10000 } · *Default:* 2500
- `fault-reset-time time` — Set the time (in milliseconds) before resetting a Fault Alarm (100ms step). — *Valores:* { 2500 - 10000 } · *Default:* 10000
- `fault-action action` — Set the action when this MEP enters in fail state, as controlled by the Continuity Check lowest-fault-priority-defect configuration. — *Valores:* { none | block-port | shutdown-port } · *Default:* none

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |
| 4.6 | Added MEP fault action block-port. |
| 4.8 | Added MEP fault action shutdown-port. |
| 4.9 | Fault action controlled by lowest-fault-priority-defect only. |

**Usage Guidelines:**

To configure the Continuity Check Messages generation it is necessary to create a valid CFM Maintenance End Point. The example below shows the creation of a MEP and CCMs generation configuration.

```text
# config
(config)# dot1q vlan 50
(config-vlan-50)# interface gigabit-ethernet-1/1/1
(config-dot1q-interface-gigabit-ethernet-1/1/1)# top
(config)# oam
(oam)# cfm
(cfm)# md CFM_MD
(cfm-md-CFM_MD)# level 0
(cfm-md-CFM_MD)# ma CFM_MA
(cfm-ma-CFM_MA)# ccm-interval 1s
(cfm-ma-CFM_MA)# vlan-list 50
(cfm-ma-CFM_MA)# primary-vlan-id 50
(cfm-ma-CFM_MA)# mep 1
(cfm-mep-1)# interface gigabit-ethernet-1/1/1
(cfm-mep-1)# direction up
(cfm-mep-1)# primary-vlan-id 50
(cfm-mep-1)# continuity-check
(cfm-mep-1-cci)# cci-enabled
(cfm-mep-1-cci)# lowest-fault-priority-defect invalid-ccm
(cfm-mep-1-cci)# fault-alarm-time 3000
(cfm-mep-1-cci)# fault-reset-time 9000
(cfm-mep-1-cci)# commit
```

Commit complete.

```text
(cfm-mep-1-cci)# end
#
```

One-line like command is also supported. The example below shows the configuration in another MEP.

```text
# config
(config)# dot1q vlan 50 interface gigabit-ethernet-1/1/1
(config-dot1q-interface-gigabit-ethernet-1/1/1)# top
(config)# oam cfm md CFM_MD level 0 ma CFM_MA ccm-interval 1s
vlan-list 50 primary-vlan-id 50 mep 2 interface gigabit-ethernet-1/1/4
direction down primary-vlan-id 50 continuity-check cci-enabled
(cfm-mep-2-cci)# commit
```

Commit complete.

```text
(cfm-mep-2-cci)# end
#
```

Fault Alarm is priority based, so a given value will enable all the values below it: remote-rdi - Enable fault alarm notification for all errors remote-mac-error - Enable fault alarm notification for remote MEPs with Port Status or Interface Status failure and all errors below remove-invalid-ccm - Enable fault alarm notification for remote MEPs without connectivity or remote MEP FSM receiving invalid CCMs and all errors below invalid-ccm - Enable fault alarm notification for reception of invalid CCMs and cross-connection CCMs cross-connect-ccm - Enable fault alarm notification only for reception of cross-connection CCMs

**Impacts and precautions:**

• CCMs generation is part of MEP and a valid MEP configuration is required for the configuration to be committed successfully. • Fault-Action Block-Port can be used only on MEP with direction Down. • Fault-Action Shutdown-Port can be used only on MEP with direction Up.

**Hardware restrictions:**

N/A


### `clear oam cfm statistics`

> **Página:** 1462 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Clear statistics information related to CFM.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
clear oam cfm statistics [md md-id] [ma ma-id] [mep mep-id]
```

**Parameters:**

- `md md-id` — This parameter selects the MD ID to the statistics be cleared. If omitted, all MD IDs will be selected. — *Valores:* N/A · *Default:* N/A
- `ma ma-id` — This parameter selects the MA ID to the statistics be cleared. If omitted, all MA IDs will be selected. — *Valores:* N/A · *Default:* N/A
- `mep mep-id` — This parameter selects the MEP ID to the statistics be cleared. If omitted, all MEP IDs will be selected. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0.0 | This command was introduced. |

**Usage Guidelines:**

```text
# clear oam cfm statistics md my-md ma my-ma mep 1
#
```

**Impacts and precautions:**

None

**Hardware restrictions:**

None


### `delay-measurement`

> **Página:** 1464 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Trigger a delay-measurement session from a local MEP to a remote MEP in order to collect network statistics such as delay and jitter.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam cfm delay-measurement md id ma id mep id remote-mep id [count value] [pcp value] [interval value] [size value]
```

**Parameters:**

- `md id` — Unique Maintenance Domain (MD) identifier. — *Valores:* String with MD identifier. Only an already created MD is accepted. · *Default:* N/A
- `ma id` — Unique Maintenance Association (MA) identifier. — *Valores:* String with MA identifier. Only an already created MA is accepted. · *Default:* N/A
- `mep id` — Local MEP ID. Only an already created local MEP is accepted. — *Valores:* 1 - 8191 · *Default:* N/A
- `remote-mep id` — Remote MEP ID. Only an already created remote MEP is accepted. — *Valores:* 1 - 8191 · *Default:* N/A
- `count value` — Number of delay-measurement frames in the session. — *Valores:* 1 - 1024 · *Default:* 10
- `pcp value` — PCP (priority code point) value used in the 802.1Q VLAN tag. — *Valores:* 0 - 7 · *Default:* 0
- `interval value` — Interval between each delay-measurement frame. — *Valores:* { 1s | 10s | 1min | 10min } · *Default:* 1s
- `size value` — Set delay-measurement frame size; padding is added if necessary. — *Valores:* 64 - 9000 · *Default:* 64

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.10 | This command was introduced. |

**Usage Guidelines:**

In order to start a delay-measurement session, the CFM Maintenance Domain (MD), the Maintenance Association (MA) with at least one remote Maintenance Endpoint (MEP), and the local MEP must be previously configured. The example below shows the creation of the entities, as mentioned earlier in the configuration:

```text
# config
(config)# dot1q vlan 10,20,30
(config-vlan-10,20,30)# top
(config)# oam
(oam)# cfm
(cfm)# md CFM_MD
(cfm-md-CFM_MD)# level 1
(cfm-md-CFM_MD)# ma CFM_MA
(cfm-ma-CFM_MA)# ccm-interval 1s
(cfm-ma-CFM_MA)# vlan-list 10,20,30
(cfm-ma-CFM_MA)# primary-vlan-id 20
(cfm-ma-CFM_MA)# remote-meps 10-15
(cfm-ma-CFM_MA)# mep 1
(cfm-mep-1)# interface gigabit-ethernet-1/1/2
(cfm-mep-1)# direction down
(cfm-mep-1)# primary-vlan-id 10
(cfm-mep-1)# commit
(cfm-ma-CFM_MA1)# commit
```

Commit complete.

```text
(cfm-ma-CFM_MA1)# end
#
```

The remote MEP must also be known. Therefore, at least one valid CCM must be received from the remote MEP before starting a session. According to this example, a possible delay-measurement command would be:

```text
# oam cfm delay-measurement md CFM_MD ma CFM_MA mep 1
remote-mep 10 count 5 interval 1s size 500 pcp 7
```

The delay-measurement replies are shown interactively, and the session summary is provided in the end: Reply from 00:04:df:2f:ad:18 Reply from 00:04:df:2f:ad:18 Reply from 00:04:df:2f:ad:18 Reply from 00:04:df:2f:ad:18 Reply from 00:04:df:2f:ad:18 Session summary: Received 5 of 5 expected replies (0% packet loss, 0% PCP mismatch). Average Minimum Maximum Delay (us): 4303 3559 5226 Jitter (us): 615 483 833

**Impacts and precautions:**

• When a delay-measurement probe or manual session runs on a specific local MEP, parallel requests on the same MEP are not allowed.

**Hardware restrictions:**

N/A


### `linktrace`

> **Página:** 1468 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Trigger a linktrace.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam cfm linktrace md id ma id mep id remote-mep id [ttl value]
```

**Parameters:**

- `md id` — Unique identifier to the MD associated to the MA. — *Valores:* String with MD identifier. Only an already created MD is accepted. · *Default:* N/A
- `ma id` — Unique identifier to the MA. — *Valores:* String with MA identifier. Only an already created MA is accepted. · *Default:* N/A
- `mep id` — Local MEP unique identifier inside the MA. Only an already created Local MEP is accepted. — *Valores:* 1 - 8191 · *Default:* N/A
- `remote-mep id` — Remote MEP unique identifier inside the MA. Only an already created Remote MEP is accepted. — *Valores:* 1 - 8191 · *Default:* N/A
- `ttl value` — Time To Live for the first linktrace packet. — *Valores:* 2 - 255 · *Default:* 64

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.9 | This command was introduced. |

**Usage Guidelines:**

In order to start a linktrace operation, the CFM Maintenance Domain (MD), the Maintenance Association (MA) with at least one remote Maintenance Endpoint (MEP) and the local MEP must be previously configured. The example below shows the creation of the aforementioned elements in the configuration:

```text
# config
(config)# dot1q vlan 10,20,30
(config-vlan-10,20,30)# top
(config)# oam
(oam)# cfm
(cfm)# md CFM_MD
(cfm-md-CFM_MD)# level 1
(cfm-md-CFM_MD)# ma CFM_MA
(cfm-ma-CFM_MA)# ccm-interval 1s
(cfm-ma-CFM_MA)# vlan-list 10,20,30
(cfm-ma-CFM_MA)# primary-vlan-id 20
(cfm-ma-CFM_MA)# remote-meps 10-15
(cfm-ma-CFM_MA)# mep 1
(cfm-mep-1)# interface gigabit-ethernet-1/1/2
(cfm-mep-1)# direction down
(cfm-mep-1)# primary-vlan-id 10
(cfm-mep-1)# commit
(cfm-ma-CFM_MA1)# commit
```

Commit complete.

```text
(cfm-ma-CFM_MA1)# end
#
```

The remote MEP must also be known. Therefore, at least one valid CCM must be received from the remote MEP before starting a linktrace session. According to the example, a possible linktrace command would be:

```text
# oam cfm linktrace md CFM_MD ma CFM_MA mep 1 remote-mep 10 ttl 16
```

The linktrace result will be displayed interactively, but can also be seen with the command:

```text
# show oam cfm linktrace
```

**Impacts and precautions:**

• A linktrace is automatically started by a local MEP to a remote MEP when three consecutive Continuity Check Messages are missed from that remote MEP. • When an automatic or manual linktrace transaction is running on a specific MEP, parallel linktrace requests on the same MEP are not allowed.

**Hardware restrictions:**

N/A


### `loopback`

> **Página:** 1471 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Trigger a loopback session.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam cfm loopback md id ma id mep id remote-mep id [count value] [size value]
```

**Parameters:**

- `md id` — Unique identifier to the MD associated to the MA. — *Valores:* String with MD identifier. Only an already created MD is accepted. · *Default:* N/A
- `ma id` — Unique identifier to the MA. — *Valores:* String with MA identifier. Only an already created MA is accepted. · *Default:* N/A
- `mep id` — Local MEP unique identifier inside the MA. Only an already created Local MEP is accepted. — *Valores:* 1 - 8191 · *Default:* N/A
- `remote-mep id` — Remote MEP unique identifier inside the MA. Only an already created Remote MEP is accepted. — *Valores:* 1 - 8191 · *Default:* N/A
- `count value` — Number of loopback messages to be sent. — *Valores:* 1 - 1024 · *Default:* 10
- `size value` — Size of loopback messages; padding is added if necessary to ensure the requested frame size. — *Valores:* 64 - 16383 · *Default:* 64

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.9 | This command was introduced. |

**Usage Guidelines:**

In order to start a loopback operation, the CFM Maintenance Domain (MD), the Maintenance Association (MA) with at least one remote Maintenance Endpoint (MEP) and the local MEP must be previously configured. The example below shows the creation of the aforementioned elements in the configuration:

```text
# config
(config)# dot1q vlan 10,20,30
(config-vlan-10,20,30)# top
(config)# oam
(oam)# cfm
(cfm)# md CFM_MD
(cfm-md-CFM_MD)# level 1
(cfm-md-CFM_MD)# ma CFM_MA
(cfm-ma-CFM_MA)# ccm-interval 1s
(cfm-ma-CFM_MA)# vlan-list 10,20,30
(cfm-ma-CFM_MA)# primary-vlan-id 20
(cfm-ma-CFM_MA)# remote-meps 10-15
(cfm-ma-CFM_MA)# mep 1
(cfm-mep-1)# interface gigabit-ethernet-1/1/2
(cfm-mep-1)# direction down
(cfm-mep-1)# primary-vlan-id 10
(cfm-mep-1)# commit
(cfm-ma-CFM_MA1)# commit
```

Commit complete.

```text
(cfm-ma-CFM_MA1)# end
#
```

The remote MEP must also be known. Therefore, at least one valid CCM must be received from the remote MEP before starting a loopback session. According to the example, a possible loopback command would be:

```text
# oam cfm loopback md CFM_MD ma CFM_MA mep 1 remote-mep 2 count 10
```

Loopback replies are shown as they are received, and a session summary is presented when it is terminated. Loopback session started to 00:04:df:01:02:03 Reply from 00:04:df:01:02:03, transaction 1 Reply from 00:04:df:01:02:03, transaction 2 Reply from 00:04:df:01:02:03, transaction 3 Reply from 00:04:df:01:02:03, transaction 4 Reply from 00:04:df:01:02:03, transaction 5 Reply from 00:04:df:01:02:03, transaction 6 Reply from 00:04:df:01:02:03, transaction 7 Reply from 00:04:df:01:02:03, transaction 8 Reply from 00:04:df:01:02:03, transaction 9 Reply from 00:04:df:01:02:03, transaction 10 Session summary: Expected 10 replies, received 10 with valid order and 0 out of order. Replies with wrong payload: 0.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show oam cfm delay-measurement`

> **Página:** 1475 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display consolidated delay-measurement statistics for the specified probe and session. If no probe is specified, all probes are shown. If no session is specified for a given probe, all sessions probe sessions are shown. For each session, consolidated statistics of the last 10 executions are saved and rotated to discard the oldest results.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show oam cfm delay-measurement [detail] show oam cfm delay-measurement probe id [detail] show oam cfm delay-measurement probe id session id [detail]
```

**Parameters:**

- `probe id` — Unique probe identifier. — *Valores:* 1 - 512 · *Default:* N/A
- `session id` — Unique session identifier. A probe contains up to 8 sessions, where each session has a different PCP (priority code point) value. — *Valores:* 1 - 8 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.1 | This command was introduced. |

**Usage Guidelines:**

Detailed show:

```text
DM4050# show oam cfm delay-measurement probe 1 session 1 detail
```

LAST LAST LAST LAST LAST LAST LAST ALL ALL ALL ALL ALL ALL ALL AVG MIN MAX AVG MIN MAX LOSS LAST PCP AVG MIN MAX AVG MIN MAX LOSS ALL PCP DELAY DELAY DELAY JITTER JITTER JITTER RATIO MISMATCH DELAY DELAY DELAY JITTER JITTER JITTER RATIO MISMATCH SESSION PCP (us) (us) (us) (us) (us) (us) % RATIO % (us) (us) (us) (us) (us) (us) % RATIO % ------------------------------------------------------------------------------------------------------------------------------------------ 1 1 4892 3176 7063 940 524 1144 0 0 4892 3176 7063 940 524 1144 0 0 Simplified show:

```text
DM4050# show oam cfm delay-measurement probe 1 session 2
```

LAST LAST LAST ALL ALL ALL AVG AVG LOSS LAST PCP AVG AVG LOSS ALL PCP DELAY JITTER RATIO MISMATCH DELAY JITTER RATIO MISMATCH SESSION PCP (us) (us) % RATIO % (us) (us) % RATIO % ------------------------------------------------------------------------------ 2 2 4635 330 0 0 4635 330 0 0

**Output Terms:**

Output Description SESSION Session identitifier, unique for a given probe. PCP Priority code point value configured for the probe. Average delay for all frames of the most recent execution of this LAST AVG DELAY session. Minimum delay for all frames of the most recent execution of this LAST MIN DELAY session. Maximum delay for all frames of the most recent execution of this LAST MAX DELAY session. Average jitter for all frames of the most recent execution of this sesLAST AVG JITTER sion. Minimum jitter for all frames of the most recent execution of this LAST MIN JITTER session. Maximum jitter for all frames of the most recent execution of this LAST MAX JITTER session. Frame loss ratio (missing replies) for the most recent execution of LAST LOSS RATIO this session. LAST PCP MISMATCH Ratio of frames received with PCP value that is not equal to the transRATIO mitted value for the most recent execution of this session.. ALL AVG DELAY Average delay for all frames for all execution of this session. ALL MIN DELAY Minimum delay for all frames for all execution of this session. ALL MAX DELAY Maximum delay for all frames for all execution of this session. Output Description ALL AVG JITTER Average jitter for all frames for all execution of this session. ALL MIN JITTER Minimum jitter for all frames for all execution of this session. ALL MAX JITTER Maximum jitter for all frames for all execution of this session. ALL LOSS RATIO Frame loss ratio (missing replies) for all execution of this session. ALL PCP MISMATCH Ratio of frames received with PCP value that is not equal to the transRATIO mitted value for all execution of this session.

**Impacts and precautions:**

None

**Hardware restrictions:**

None


### `show oam cfm local`

> **Página:** 1479 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display information about CFM Local status and configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show oam cfm local [brief] [detail] [statistics]
```

**Parameters:**

- `brief` — This parameter displays a summary information about the status, including MD name, MA name, MEP ID, MAC Address, TX RDI, Defects, Highest Defect, TX Interface Status, TX Port Status. — *Valores:* N/A · *Default:* N/A
- `detail` — This parameter displays all that the brief parameter displays plus some current configurations. These include Level, Primary VLAN ID, VLAN List, CCM Interval, Remote MEP IDs, Interface, Direction, Fault Alarm Time and Fault Reset Time. When no parameter is given the show command displays the same content of detail parameter. — *Valores:* N/A · *Default:* N/A
- `statistics` — This parameter displays the statistics related to local the MEPs, including the number of received CCMs with sequence errors, the current sequence number of transmitted CCMs and the total number of transmitted CCMs. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |
| 4.6 | Added Block State information. |
| 4.8 | Added Shutdown State information. |

**Usage Guidelines:**

Given the equipment has the following CFM configuration: md Domain level 5 ma Association primary-vlan-id 1 vlan-list 1 ccm-interval 1s remote-meps 2 mep 1 interface gigabit-ethernet-1/1/9 direction down primary-vlan-id 1 continuity-check cci-enabled lowest-faultpriority-defect remote-mac-error fault-action block-port. Let’s see the brief information:

```text
# show oam cfm local brief | notab
oam cfm local
md Domain
ma Association
mep 1
mac-address 00:04:df:40:9c:1b
tx-rdi False
defects -
highest-priority-defect -
tx-interface-status-tlv Up
block-state Forwarding
tx-port-status-tlv "Not Present"
#
```

Now let’s see the detail information:

```text
# show oam cfm local detail | notab
oam cfm local
md Domain
ma Association
mep 1
mac-address 00:04:df:40:9c:1b
tx-rdi False
defects -
highest-priority-defect -
tx-interface-status-tlv Up
block-state Forwarding
tx-port-status-tlv "Not Present"
level 5
primary-vlan-id 1
vlan-list 1
ccm-interval 1s
remote-mep-ids 2
interface gigabit-ethernet-1/1/9
direction Down
fault-alarm-time 2500ms
fault-reset-time 10000ms
#
```

**Output Terms:**

Output Description MD The Maintenance Domain name. MA The Maintenance Association name. MEP The Maintenance End Point ID. MAC Address The MAC Address of local MEP. The Remote Defect Indication in Continuity Check Messages being TX RDI transmitted by this MEP. Defects Show all defects detected by state machines in this local MEP. Highest Priority Show the highest priority defect presented in this configuration. Defect TX Interface The link status of the interface where the local MEP is configured. Status TLV This status can be Up or Down. Blocking state that CFM applies to the interface on which the Down MEP is attached. When fault-action is block-port, this status can be Block State: Blocked or Forwarding. Status N/A is presented if fault-action is not configured. Output Description Shutdown state that CFM applies to the interface on which the UP MEP is attached. When fault-action is shutdown-port, this status can Shutdown State: be Up or Down. Status N/A is presented if fault-action is not configured. The link status of the port where the local MEP is configured. CurTX Port Status TLV rently this status only shows “Not present” and will be implemented in the future. Level Level of the Maintenance Domain on which this MEP is configured. The primary VLAN ID, used in Continuity Check Messages transmitPrimary VLAN ID ted by this local MEP. The inner VLAN ID (second tag) used in Continuity Check Messages Inner VLAN ID transmitted by this local MEP. List of VLANs from the Maintenance Association on which this MEP is VLAN List configured. Transmission interval for Continuity Check Messages, inherited from CCM Interval the configuration of the Maintenance Association on which this MEP is configured. The list of Remote MEPs, inherited from the configuration of the Remote MEP IDs Maintenance Association on which this MEP is configured. Interface The interface on which the MEP is configured. Direction The MEP direction, either Up or Down Fault Alarm Time Configuration of Fault Alarm Time. Fault Reset Time Configuration of Fault Reset Time. Output Description RX Seq Error Count Number of received Continuity Check Messages with sequence number errors. Current sequence number for Continuity Check Messages transmitTX Curr Seq Num ted by this MEP. TX CCM Total Total transmitted Continuity Check Messages.

**Impacts and precautions:**

None

**Hardware restrictions:**

None


### `show oam cfm remote`

> **Página:** 1484 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display information about CFM Remote status and configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show oam cfm remote [brief] [detail] [statistics]
```

**Parameters:**

- `brief` — This parameter displays a summary information about the status, including MD name, MA name, Local MEP ID, Remote MEP ID, MAC Address, RX RDI, State, RX Interface Status, RX Port Status, Last State Change and Sender ID. — *Valores:* N/A · *Default:* N/A
- `detail` — This parameter displays all that the brief parameter displays. When no parameter is given the show command displays the same content of detail parameter. — *Valores:* N/A · *Default:* N/A
- `statistics` — This parameter displays the statistics related to the MEPs, including the sequence number of the Continuity Check Message that was last received from this remote MEP. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0.0 | This command was introduced. |

**Usage Guidelines:**

Given the equipment has the following CFM configuration: md Domain level 5 ma Association primary-vlan-id 1 vlan-list 1 ccm-interval 1s remote-meps 2 mep 1 interface gigabit-ethernet-1/1/9 direction down primary-vlan-id 1 continuity-check cci-enabled lowest-faultpriority-defect remote-mac-error. Let’s see the brief information:

```text
# show oam cfm remote brief | notab
oam cfm remote
md Domain
ma Association
local-mep 1
remote-mep 2
mac-address 00:04:df:61:25:49
rx-rdi False
state Ok
rx-interface-status-tlv Up
rx-port-status-tlv "Not Present"
last-state-change "1min 41s ago"
rx-sender-id ""
#
```

Now let’s see the detail information:

```text
# show oam cfm remote detail | notab
oam cfm remote
md Domain
ma Association
local-mep 1
remote-mep 2
mac-address 00:04:df:61:25:49
rx-rdi False
state Ok
rx-interface-status-tlv Up
rx-port-status-tlv "Not Present"
last-state-change "1min 52s ago"
rx-sender-id ""
#
```

**Output Terms:**

Output Description MD The Maintenance Domain name. MA The Maintenance Association name. Local MEP The Local Maintenance End Point ID. Remote MEP The Remote Maintenance End Point ID. MAC Address The MAC Address of Remote MEP. RX RDI The Remote Defect Indication. The operational state of the Remote MEP. ‘Failed’ means that a local MEP is missing Continuity Check Messages from this remote MEP. State ‘OK’ means that valid Continuity Check Messages from this remote MEP are being received with the expected periodicity. RX Interface The link status of the interface where the remote MEP is configured. Status TLV This status can be Up or Down RX Port Status TLV The link status of the port where the remote MEP is configured. This status can be Up or Blocked. The time past since last state change occurred. If current remote MEP state is ‘OK’, this time since the MEP recovered from a failure. Last State Change If the current remote MEP state is ‘Failed’, this is the time since the failure occurred. Sender ID The sender ID from the last CCM received. RX Last Seq Num Last received Continuity Check Messages sequence number.

**Impacts and precautions:**

None

**Hardware restrictions:**

None ACTIVATION TEST This topic describes the commands related to management of activation test features such as commands to configure RFC2544 generator or traffic loop with MAC swap support.


## Activation Test

### `traffic-loop`

> **Página:** 1488 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create traffic loopback to test and verify the transmit and receive ports.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
traffic-loop id interface interface-name destination-mac-address mac-address sourcemac-address mac-address vlan vlan-id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `traffic-loop id` — Traffic loopback test identifier. — *Valores:* 1 - 8 · *Default:* N/A
- `interface interface-name` — Interface to configure loopback mode on. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet. · *Default:* N/A
- `destination-mac-address mac-address` — Destination MAC address of the generated traffic. — *Valores:* xx:xx:xx:xx:xx:xx · *Default:* N/A
- `source-mac-address mac-address` — Source MAC address from data generator device. — *Valores:* xx:xx:xx:xx:xx:xx · *Default:* N/A
- `vlan vlan-id` — ID of VLAN used on this traffic test session. — *Valores:* 1 - 4094 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.2 | This command was introduced. |
| 5.0 | Added support for 25G interfaces. |
| 5.10 | Added support to DM4270, DM4380 and DM4770 platforms. |

**Usage Guidelines:**

Example: This example show how to create a traffic loopback test.

```text
#config
Entering configuration mode terminal
(config)# traffic-loop 1
(traffic-loop-1)# interface gigabit-ethernet-1/1/1
(traffic-loop-1)# destination-mac-address a3:84:b3:8a:2e:59
(traffic-loop-1)# source-mac-address 21:7d:ed:70:B1:5f
(traffic-loop-1)# vlan 100
(traffic-loop-1)# top
(config)# commit
```

Commit complete.

```text
(config)#
```

**Impacts and precautions:**

• Only pre-existing interfaces will be accepted when entering an interface name. • Link aggregation groups (LAG) cannot be used on for interface parameter. • Interfaces added as a member of a link aggregation group (LAG) can be used. • Traffic Loopback may cause loss of access to inband management! Therefore it is recommended to use commit confirmed for safety.

**Hardware restrictions:**

N/A EFM This topic describes the commands related to the management of transport layer functions between network elements such as commands to monitor the link status or detect remote failures.


## EFM

### `efm`

> **Página:** 1491 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Ethernet in the First Mile configuration according to the specification described in IEEE 802.3ah-2004.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam efm interface interface-name mode working-mode
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Ethernet interface where EFM is being enabled. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet. · *Default:* N/A
- `mode working-mode` — Set the EFM working mode on the interface to be configured. — *Valores:* active | passive · *Default:* active

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |

**Usage Guidelines:**

The EFM can be enabled on Ethernet interfaces to monitor link operation and improve fault isolation on a network.

```text
# config
(config)# oam efm interface gigabit-ethernet-1/1/1
(config-oam-efm-interface-gigabit-ethernet-1/1/1)# mode passive
(config-oam-efm-interface-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(config-oam-efm-interface-gigabit-ethernet-1/1/1)# end
#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show oam efm`

> **Página:** 1493 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display information about EFM status and configuration. This show only presents ports that are configured for EFM.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show oam efm interface [ port ]
```

**Parameters:**

- `port` — The Interface with EFM whose status is desired to show. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |

**Usage Guidelines:**

Given the equipment has the following ports configured for EFM.

```text
# show running-config oam efm
efm
interface ten-gigabit-ethernet-1/1/1
mode active
!
!
#
```

A show will present:

```text
# show oam efm
```

LOCAL LOCAL LOCAL REMOTE REMOTE REMOTE REMOTE DISCOVERY LINK CRITICAL DISCOVERY LINK CRITICAL DYING INTERFACE MODE BLOCKED STATUS FAULT EVENT STATUS FAULT EVENT GASP ---------------------------------------------------------------------------------------------------------- gigabit-ethernet-1/1/1 active no stable no no stable no no -

```text
#
```

**Output Terms:**

Output Description INTERFACE The Interface that is configured for EFM. MODE EFM working mode configured on port. BLOCKED The block status on port. LOCAL DISCOVERY The local status of the EFM discovery process. STATUS Output Description The event indicating if a loss of signal (LoS) error has occurred on LOCAL LINK FAULT local physical link. LOCAL CRITICAL The event indicating if an unspecified critical event has occurred on EVENT local physical link. REMOTE DISCOVERY The remote status of the EFM discovery process. STATUS The event indicating if a loss of signal (LoS) error has occurred on REMOTE LINK FAULT remote physical link. REMOTE CRITICAL The event indicating if an unspecified critical event has occurred on EVENT remote physical link. The timestamp of the last time an unrecoverable remote fault has REMOTE DYING GASP occurred.

**Impacts and precautions:**

None

**Hardware restrictions:**

None LLDP This topic describes the commands related to management of link layer discovery protocol such as commands to configure optional TLVs or to inspect neighbor’s information.


## LLDP

### `lldp`

> **Página:** 1496 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Link Layer Discovery Protocol configuration according to the specification described in IEEE 802.1AB (2009).

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
lldp interface interface-name [ admin-status status | notification | tlvs-tx tlv ] lldp message-fast-tx seconds lldp message-tx-hold-multiplier ttl-multiplier lldp message-tx-interval seconds lldp notification-interval seconds lldp reinit-delay seconds lldp tx-credit-max frames lldp tx-fast-init transmissions
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Selects the interface to be configured. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, two-hundred-g-ethernet, four-hundred-g-ethernet. · *Default:* None
- `admin-status status` — Sets the LLDP administrative status for the interface. — *Valores:* disabled | rx-only | tx-and-rx | tx-only · *Default:* tx-and-rx (transmit and receive LLDP frames)
- `notification` — Enables generation of SNMP notifications for events associated with this interface. — *Valores:* N/A · *Default:* N/A
- `tlvs-tx tlv` — Selects which optional TLVs are transmitted to neighbors. — *Valores:* port-description | system-capabilities | system-description | system-name · *Default:* None
- `message-fast-tx seconds` — Sets the time interval in seconds between transmissions during fast transmission periods. — *Valores:* 1-3600 · *Default:* 1
- `message-tx-hold-multiplier ttl-multiplier` — Sets the TTL value that is carried in transmitted LLDP frames. It is used as a multiplier for message-tx-interval. — *Valores:* 2-10 · *Default:* 4
- `message-tx-interval seconds` — Sets the time interval in seconds between transmissions during normal transmission periods. — *Valores:* 5-32768 · *Default:* 30
- `notification-interval seconds` — Sets the time interval in seconds between transmissions of SNMP notifications during normal transmission periods. — *Valores:* 5-3600 · *Default:* 30
- `reinit-delay seconds` — Sets the amount of delay in seconds from when admin-status of an interface becomes ‘disabled’ until re-initialization is attempted. — *Valores:* 1-10 · *Default:* 2
- `tx-credit-max frames` — Sets the maximum number of consecutive LLDP frames that can be transmitted in a second. — *Valores:* 1-100 · *Default:* 5
- `tx-fast-init transmissions` — Sets the number of LLDP frames that are transmitted during a fast transmission period. — *Valores:* 1-8 · *Default:* 4

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 5.10 | Added support for 25G interfaces. |
| 10.6 | Added support for DM4618 platform. |

**Usage Guidelines:**

Example: This example shows how to configure LLDP with port-description and system-name TLVs transmission disabled.

```text
# config
Entering configuration mode terminal
(config)# lldp
(lldp)# message-fast-tx 100
(lldp)# message-tx-hold-multiplier 5
(lldp)# message-tx-interval 20
(lldp)# notification-interval 10
(lldp)# reinit-delay 5
(lldp)# tx-credit-max 50
(lldp)# tx-fast-init 5
(lldp)# interface gigabit-ethernet-1/1/1
(lldp-gigabit-ethernet-1/1/1)# admin-status tx-only
(lldp-gigabit-ethernet-1/1/1)# notification
(lldp-gigabit-ethernet-1/1/1)# no tlvs-tx port-description
(lldp-gigabit-ethernet-1/1/1)# no tlvs-tx system-name
(lldp-gigabit-ethernet-1/1/1)# top
(config)# commit
```

Commit complete.

```text
(config)#
```

**Impacts and precautions:**

All optional TLVs are transmitted to neighbors by default. To disable the transmission of a specific TLV use the no tlvs-tx command.

**Hardware restrictions:**

This command is not available for the management interface.


### `show lldp local`

> **Página:** 1501 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays information about LLDP Local status and configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
show lldp local [ interface interface-name ] [ detail ] [ statistics ]
```

**Parameters:**

- `interface interface-name` — Selects the interface to display local LLDP information. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, two-hundred-g-ethernet, four-hundred-g-ethernet. · *Default:* N/A
- `detail` — This parameter displays detailed local LLDP information. — *Valores:* N/A · *Default:* N/A
- `statistics` — Displays the statistics related to LLDP agent, including current number of frames transmitted, received or dropped by interface, current number of inserts and deletions in the LLDP table as well as number of neighbors aged out and more. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 10.6 | Added support for DM4618 platform. |

**Usage Guidelines:**

Given the equipment has 2 interfaces the command could result in the following output:

```text
# show lldp local
lldp local chassis-id-subtype mac-address
lldp local chassis-id 00:04:DF:60:D0:18
lldp local system-name ""
lldp local system-description "Local System Description"
lldp local system-capabilities-supported bridge,router
lldp local system-capabilities-enabled bridge
PORT ID
```

INTERFACE NAME SUBTYPE ... --------------------------------------- ... gigabit-ethernet-1/1/1 interface-name ... gigabit-ethernet-1/1/2 interface-name ... PORT ID PORT DESCRIPTION ------------------------------------------------ gigabit-ethernet-1/1/1 Gigabit Ethernet Port 1 gigabit-ethernet-1/1/2 Gigabit Ethernet Port 2 The output of statistics command could look like this:

```text
# show lldp statistics
lldp remote-table-inserts 50
lldp remote-table-deletes 12
lldp remote-table-drops 40
lldp remote-table-ageouts 12
```

TX RX FRAME ... INTERFACE NAME FRAMES FRAMES DROPS ... ---------------------------------------------- ... gigabit-ethernet-1/1/1 140 500 0 ... gigabit-ethernet-1/1/2 150 1240 40 ... FRAMES PDU UNKNOWN DISCARDED WITH LENGTH TLVS TLVS NEIGHBOR ERROR ERRORS COUNT COUNT AGEOUTS --------------------------------------------- 10 0 20 3 2 15 0 32 5 10

**Output Terms:**

Output Description The value that indicates the basis for the chassis ID entity that is CHASSIS ID SUBTYPE listed in the chassis ID field. For the local system this value is mac-address. The specific identifier for the chassis in this system. For the local CHASSIS ID system it is represented by the system MAC. SYSTEM NAME The local system’s assigned name. The description of this network entity. Includes the full name and SYSTEM DESCRIPTION version identification of the local system’s hardware type, software operating system and networking software. SYSTEM CAPABILITIES The primary functions supported by the local system. SUPPORTED SYSTEM CAPABILITIES The primary functions enabled on the local system. ENABLED INTERFACE NAME The local interface. The value that indicates the basis for the identifier that is listed in PORT ID SUBTYPE the port ID field. For the local system this value is interface-name. PORT ID The specific identifier for the local interface. PORT DESCRIPTION The description of the local interface. REMOTE TABLE Total number of neighbors inserted in the LLDP remote table. INSERTS Output Description REMOTE TABLE Total number of neighbors deleted in the LLDP remote table. DELETES REMOTE TABLE DROPS Total number of neighbors dropped in the LLDP remote table. REMOTE TABLE Total number of neighbors aged out in the LLDP remote table. AGEOUTS TX FRAMES Current number of LLDP frames transmitted on a given interface. RX FRAMES Current number of LLDP frames received on a given interface. FRAME DROPS Current number of LLDP frames dropped on a given interface. Current number of LLDP frames with error received on a given interFRAMES WITH ERROR face. PDU LENGTH ERRORS The number of LLDPDU length errors recorded on a given interface. UNKNOWN TLVS COUNT Current number of unknown/unrecognized TLVs received on a given interface. DISCARDED TLVS Current number of discarded TLVs on a given interface. COUNT NEIGHBORS AGEOUTS Current number of neighbors aged out on a given interface.

**Impacts and precautions:**

None

**Hardware restrictions:**

None


### `show lldp neighbors`

> **Página:** 1506 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays information about LLDP neighbors status.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
show lldp neighbors [ interface-name ] [ brief ] [ detail ] [ management ] [unknown-tlvs ]
```

**Parameters:**

- `interface-name` — Selects the local interface to display neighbor LLDP information. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, two-hundred-g-ethernet, four-hundred-g-ethernet. · *Default:* N/A
- `brief` — This parameter displays a summary information from neighbors, including ID, chassis ID subtype, chassis ID, system name and port Description. — *Valores:* N/A · *Default:* N/A
- `detail` — This parameter displays all that the brief parameter displays plus system capabilities supported, system capabilities enabled, port ID subtype and port ID from neighbors. When no parameter is given the show command displays the same content of brief parameter. — *Valores:* N/A · *Default:* N/A
- `management` — This parameter displays the management information from neighbors, including neighbor ID, management address subtype, management address, interface ID subtype and interface ID. — *Valores:* N/A · *Default:* N/A
- `unknown-tlvs` — This parameter displays the unknown TLVs received from neighbors. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 10.6 | Added support for DM4618 platform. |

**Usage Guidelines:**

Given the equipment has 2 interfaces with a neighbor attached at each one of them, the command could result in the following output:

```text
# show lldp neighbors
```

NEIGHBOR CHASSIS ID CHASSIS ... LOCAL INTERFACE ID SUBTYPE ID ... ------------------------------------------------------------- ... gigabit-ethernet-1/1/1 1 chassis-component 4 ... gigabit-ethernet-1/1/2 2 chassis-component 4 ... SYSTEM NAME PORT DESCRIPTION ------------------------------ DmSwitch Ethernet Port 12 DmSwitch Ethernet Port 15 The output of management command could look like this:

```text
# show lldp neighbors management
```

NEIGHBOR ADDRESS ... LOCAL INTERFACE ID SUBTYPE ADDRESS ... ---------------------------------------------------- ... gigabit-ethernet-1/1/1 1 ipv4 40.0.0.4 ... gigabit-ethernet-1/1/2 2 ipv4 30.0.0.4 ... INTERFACE INTERFACE ID SUBTYPE SUBTYPE --------------------------------- system-port-number 12 system-port-number 15 The output of detail command could look like this:

```text
# show lldp neighbors detail
```

NEIGHBOR CHASSIS ID CHASSIS ... LOCAL INTERFACE ID SUBTYPE ID ... ------------------------------------------------------------- ... gigabit-ethernet-1/1/1 1 chassis-component 4 ... gigabit-ethernet-1/1/2 2 chassis-component 4 ... SYSTEM SYSTEM CAPABILITIES CAPABILITIES ... SYSTEM NAME SYSTEM DESCRIPTION SUPPORTED ENABLED ... ------------------------------------------------------------- ... DmSwitch Switch Description bridge bridge ... DmSwitch Switch Description bridge bridge ... PORT ID SUBTYPE PORT ID PORT DESCRIPTION ---------------------------------------------------------- interface-name gigabit-ethernet-1/1/12 Ethernet Port 12 interface-name gigabit-ethernet-1/1/15 Ethernet Port 15

**Output Terms:**

Output Description LOCAL INTERFACE The local interface associated with this neighbor. NEIGHBOR ID The neighbor’s identification for the system. The value that indicates the basis for the chassis ID entity that CHASSIS ID SUBTYPE is listed in the chassis ID field. Possible values are chassis-component, interface-alias, port-component, mac-address, network-address, interface-name and local. CHASSIS ID The specific identifier for the neighbor’s chassis. SYSTEM NAME The neighbor’s system name. Output Description The neighbor’s description. Includes the full name and version idenSYSTEM DESCRIPTION tification of the system’s hardware type, software operating system and networking software. SYSTEM CAPABILITIES The primary functions supported by the neighbor. SUPPORTED SYSTEM CAPABILITIES The functions enabled on the neighbor. ENABLED The value that indicates the basis for the identifier that is listed in the port ID field. Possible values are interface-alias, port-component, PORT ID SUBTYPE mac-address, network-address, interface-name, agent-circuit-id and local. PORT ID The specific identifier for the neighbor’s interface. PORT DESCRIPTION The description of the neighbor’s interface. ADDRESS SUBTYPE The type of the management address listed in the address field. ADDRESS The management address of the neighbor. The value that indicates the numbering method used for defining the INTERFACE ID interface ID field. Possible values are unknown, if-index and systemSUBTYPE port-number. The assigned number that identifies the interface associated with INTERFACE ID the management address. TLV TYPE The type of the unknown TLV received. Output Description TLV INFO The value of the unknown TLV received.

**Impacts and precautions:**

None

**Hardware restrictions:**

None TWAMP This topic describes the commands related to management of Active Measurement Protocol such as commands to configure and inspect OWAMP, TWAMP Generator or TWAMP Reflector.


## TWAMP

### `show oam twamp reflector connection`

> **Página:** 1511 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows the list of current and deactivated TWAMP-control connections.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp reflector connection [ brief | detail ]
```

**Parameters:**

- `brief` — This parameter displays a summary information about all current and previous TWAMP-Control connections. — *Valores:* N/A · *Default:* N/A
- `detail` — This parameter displays a detailed information about all current and previous TWAMP-Test connections. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This example below demonstrates two TWAMP-Control sessions. The first session is deactivated, and the second is running at the moment of the show. Example:

```text
# show oam twamp reflector connection brief
```

Client-address Client-port Server-address Server-port State ------------------------------------------------------------------ 192.168.0.30 58500 192.168.0.25 862 finished 192.168.0.26 58548 192.168.0.25 862 active The description for each TWAMP-Control session state is shown below: • connecting: the TWAMP-Control session parameters are being negotiated by the Server and Control-Client. • established: TWAMP-Control session established but no tests are running. • active: TWAMP-Control session is active and a related TWAMP-Test session is running. • finished: TWAMP-Control session is closed. • unknown: unknown state. Either an error occured or it was not possible to determine the current TWAMP-Control session state

**Output Terms:**

Output Description Client address Display the TWAMP Control-Client IP address for this connection. Display the TCP port used by the TWAMP Control-Client to initiate Client port this connection. Display the IP address from the current device used by the TWAMP Server address Server on this connection. Display the TCP port used by the TWAMP Server to initiate this conServer port nection. State | Connection Display state of the TWAMP-Control connection. States may be: unstate known, connecting, established, active or finished. Connection Display the TWAMP-Control connection identifier. identifier VRF name Display the name of VRF instance assigned to TWAMP reflector. Display the operational mode of TWAMP reflector (not configurable). Mode Inactive connection timeout Display the timeout to close the connection if no packet is received. Test Session Display the timeout to close the connection if no packet is received. Number

**Impacts and precautions:**

• Former TWAMP-Control sessions will appear in this show with state closed.

**Hardware restrictions:**

N/A


### `show oam twamp reflector test-session`

> **Página:** 1515 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows the list of current and deactivated TWAMP-Test sessions.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp reflector test-session [ brief | detail ]
```

**Parameters:**

- `brief` — This parameter displays a summary information about all current and previous TWAMP-Test sessions. — *Valores:* N/A · *Default:* N/A
- `detail` — This parameter displays a detailed information about all current and previous TWAMP-Test sessions. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | Brief command was introduced. |
| 4.6 | Detail command was introduced. |

**Usage Guidelines:**

This example below demonstrates two TWAMP-Test sessions. The first TWAMP-Test session is deactivated, and the second is running at the moment of the show. Example:

```text
# show oam twamp reflector test-session brief
```

Sender-address Sender-port Reflector-address Reflector-port State -------------------------------------------------------------------------- 192.168.0.30 9785 192.168.0.25 9785 finished 192.168.0.26 9328 192.168.0.25 9328 active

```text
# show oam twamp reflector test-session detail
Test-session-state : finished
Connection-ID : 1
Session-ID : 0x1e1e1e02e18809228f6e503f9c958a74
Sender-address : 192.168.0.30
Sender-port : 9785
Reflector-address : 192.168.0.25
Reflector-port : 9785
VRF name : global
Mode : unauthenticated
DSCP : 0 (CS0)
Payload-length : 50
Created-time : 2019-11-26 20:27:14
Last-start-time : 2019-11-26 20:27:16
Last-stop-time : 2019-11-26 20:27:29
Test-RX-packets : 50
Test-RX-packets-error: 0
Test-TX-packets : 50
Test-session-state : active
Connection-ID : 2
Session-ID : 0x1e1e1e02e18809374bb7b6bbfd86610
Sender-address : 192.168.0.26
Sender-port : 9328
Reflector-address : 192.168.0.25
Reflector-port : 9328
VRF name : global
Mode : unauthenticated
DSCP : 0 (CS0)
Payload-length : 50
Created-time : 2019-11-26 20:28:33
Last-start-time : 2019-11-26 20:28:35
Last-stop-time : never
Test-RX-packets : 18
Test-RX-packets-error: 0
Test-TX-packets : 18
```

**Output Terms:**

Output Description Sender address Display the TWAMP Control-Client IP address for this session. Output Description Display the UDP port used by the TWAMP Control-Client to send Sender port TWAMP test packets. Display the IP address from the current device used by the TWAMP Reflector address Session-Reflector on this TWAMP-Test session. Display the UDP port used by the TWAMP Session-Reflector to reflect Reflector port TWAMP test packets. State | Test Display state of the TWAMP-Test session. States may be: unknown, session state inactive, active. Connection ID Display the TWAMP connection identifier. Session ID Display the TWAMP Session identifier in hexadecimal format. VRF name Display the name of VRF instance assigned to TWAMP reflector. Display the operational mode of TWAMP reflector (not configurable). Mode Display the Differentiated Services Code Point (DSCP) transmitted in DSCP this TWAMP-Test session. Payload length Payload length of received test packets. Created time Display the TWAMP-Test session creation time. Last start time Display the TWAMP-Test session start time. Last stop time Display the TWAMP-Test session stop time. Test RX packets Display the total of received packets. Output Description Test RX packets Display the total of received packets with error. error Test TX packets Display the total of transmitted packets.

**Impacts and precautions:**

• Closed TWAMP-Test sessions will appear in these shows with state finished.

**Hardware restrictions:**

N/A


### `show oam twamp sender connection`

> **Página:** 1519 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows the list of current and deactivated TWAMP-Control connections.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp reflector connection connection-id [brief | test-session | test-sessionstatistics]
```

**Parameters:**

- `connection-id` — Specify Configure the TWAMP Control-Client connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `brief` — This parameter displays information about TWAMP-Control client configuration. — *Valores:* N/A · *Default:* N/A
- `test-session` — This parameter displays information about every TWAMP-Test session configuration. — *Valores:* N/A · *Default:* N/A
- `test-session-statistics` — This parameter displays information about every TWAMP-Test session statistics. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | These commands were introduced. |
| 6.4 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This example below demonstrates the show oam twamp sender connection brief. Example:

```text
# show oam twamp sender connection 1 brief
Connection ID : 1
Administrative Status : enabled
Client IP : 192.168.0.26
Client Port : 53073
Server IP : 192.168.0.25
Server Port : 862
VRF name : global
Mode : unauthenticated
```

Number of packets : 50 Packets interval : 200 ms Test Interval : 30 s Number of Test-Sessions : 1 ----------------------------------------------------

```text
#
```

This example below demonstrates the show oam twamp sender connection test-session. Example:

```text
# show oam twamp sender connection 1 test-session
Connection ID : 1
```

Connection State : last run successful Last-connection-start-time : 2019-12-3 20:07:52 Last-connection-stop-time : 2019-12-3 20:08:06 Test-session-ID : 1 Session-ID : 0xc0a80019e1913f1821d323fdb76f7c6 State : last run successful Sender IP : 192.168.0.26 Sender Port : 30119 Reflector IP : 192.168.0.25 Reflector Port : 30119 VRF name : global DSCP : 0 (CS0) Packet Size : 64 Min Port : 1024 Max Port : 655351 ----------------------------------------------------

```text
#
```

This example below demonstrates the show oam twamp sender connection test-sessionstatistics. Example:

```text
# show oam twamp sender connection 1 test-session
Connection ID : 1
Last-connection-start-time : 2019-12-3 20:07:52
Last-connection-stop-time : 2019-12-3 20:08:06
Test-session-ID : 1
Session-ID : 0xc0a80019e1913f1821d323fdb76f7c6
```

State : last run successful Minimum Delay : 1.70 ms Maximum Delay : 4.36 ms Average Delay : 2.07 ms Minimum Jitter : 0.03 ms Maximum Jitter : 0.19 ms Average Jitter : 0.05 ms Loss Ratio : 0.000% Packets Sent : 50 Packets Received : 50 Packets Error : 0 Packets Reordered : 0 ----------------------------------------------------

```text
#
```

**Output Terms:**

Output Description Connection ID Display the TWAMP connection identifier. Administrative Display the TWAMP connection administrative status configured. Status Client IP Display the TWAMP Control-Client IP address for this connection. Display the TCP port used by the TWAMP Control-Client to initiate Client port this connection. Display the IP address from the current device used by the TWAMP Server IP Server on this connection. Display the TCP port used by the TWAMP Server to initiate this conServer port nection. VRF name Display the name of VRF instance assigned to TWAMP connection. Display the operational mode of TWAMP connection (not configMode urable). Number of packets Display the number of packets sent on TWAMP-Test sessions. Packets interval Display the packet interval on TWAMP-Test sessions. Test Interval Display the test interval on TWAMP-Test sessions. Output Description Number of Display the number of TWAMP-Test sessions configured on TWAMP-Test-Sessions Control connection. Connection State Display state of the TWAMP-Control connection. Last-connection-start-time Display date and time of last TWAMP-Control connection started. Last-connection-stop-time Display date and time of last TWAMP-Control connection finished. Test-session-ID Display the TWAMP-Test session identifier configured. Session-ID Display the TWAMP-Test session identifier generated the server. State Display state of the TWAMP-Test session. Sender IP Display the TWAMP Control-Client address. Display the UDP port negotiated by the TWAMP Control-Client to run Sender Port this TWAMP-Test session. Reflector IP Display the TWAMP Session-Reflector address. Display the UDP port negotiated by the TWAMP Session-Reflector to Reflector Port run this TWAMP-Test session. DSCP Display the DSCP configured for this TWAMP-Test session. Packet Size Display the packet size configured for this TWAMP-Test session. Display the UDP minimum port configured for this TWAMP-Test sesMin Port sion. Output Description Display the UDP maximum port configured for this TWAMP-Test sesMax Port sion. Minimum Delay Display the minimum delay value identified during the test. Maximum Delay Display the maximum delay value identified during the test. Average Delay Display the average delay value identified during the test. Minimum Jitter Display the minimum jitter value identified during the test. Maximum Jitter Display the maximum jitter value identified during the test. Average Jitter Display the average jitter value identified during the test. Loss Ratio Display the percentage of packets lost during the test. Packets Sent Display the number of packets sent during the test. Packets Received Display the number of packets received during the test. Packets Error Display the number of packets with errors received during test. Packets Reordered Display the number of packets reordered during test.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp reflector`

> **Página:** 1525 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable TWAMP Session-Reflector on the device.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp reflector
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to enable the TWAMP Session-Reflector on this device.

```text
(config)# oam twamp reflector
(twamp-reflector)# commit
```

**Impacts and precautions:**

The TWAMP Session-Reflector will respond to any reachable IP address configured in the device. This includes the management interface, any L3 logical interface or loopback interface given they are reachable by the TWAMP controller. To restrict which IP addresses should be allowed to start a test session, use the command twamp reflector client-address.

**Hardware restrictions:**

N/A


### `twamp reflector administrative-status`

> **Página:** 1527 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status of the TWAMP Session-Reflector.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp reflector administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `administrative-status status` — Set to up to (re)activate or down to deactivate the TWAMP Session-Reflector. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a TWAMP Session-Reflector.

```text
(config)# oam twamp reflector
(twamp-reflector)# administrative-status down
(twamp-reflector)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp reflector client-address`

> **Página:** 1529 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a list of IP addresses allowed to start a TWAMP-Test session with this reflector. This list works as a whitelist ACL. If there is no IP address configured, any IP address will be allowed to start a TWAMP-Test session with this reflector with no restriction.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp reflector { ipv4 | ipv6 } client-address { a.b.c.d | x:x:x:x::x }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `client-address { a.b.c.d | x:x:x:x::x }` — IP address allowed to start a TWAMP-Test session. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to allow an IP address to start a TWAMP-Test session with this reflector.

```text
(config)# oam twamp reflector
(twamp-reflector)# ipv4 client-address 192.168.1.1
(config-client-address-192.168.1.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp reflector client-network`

> **Página:** 1531 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a list of IP networks allowed to start a TWAMP-Test session with this reflector. This command is similar to twamp reflector client-address but allows any IP inside the configured network to start a test session. This list works as a whitelist ACL. If there is no IP address or IP network configured, any IP address will be allowed to start a TWAMP-Test session with this reflector with no restriction.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp reflector { ipv4 | ipv6 } client-network { a.b.c.d/x | x:x:x:x::x/x }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `client-network { a.b.c.d/x | x:x:x:x::x/x }` — Network which IPs are allowed to start a TWAMP-Test session. — *Valores:* a.b.c.d/x or x:x:x:x::x/x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to allow any IP on a network to start a TWAMP-Test session with this Session-Reflector.

```text
(config)# oam twamp reflector
(twamp-reflector)# ipv4 client-network 192.168.1.0/24
(config-client-network-192.168.1.0/24)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp reflector port`

> **Página:** 1533 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures which TCP port will listen for connections on this TWAMP Session-Reflector. Note that the TWAMP Session-Reflector must be disabled to allow the change of the port number.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp reflector port port-number
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `port port-number` — Set the TCP port number that will be listening for new TWAMP-Control connections. — *Valores:* 862 | 1024-65535 · *Default:* 862

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to change the TWAMP Session-Reflector listening TCP port.

```text
(config)# oam twamp reflector
(twamp-reflector)# port 50000
(twamp-reflector)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp reflector vrf`

> **Página:** 1535 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Assign a VRF instance to TWAMP reflector.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp reflector vrf vrf-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vrf vrf-name` — Assign a VRF instance to TWAMP reflector. — *Valores:* Name of an existent VRF. · *Default:* global

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example shows how to assign the VRF to TWAMP reflector on this device.

```text
(config)# oam twamp reflector
(twamp-reflector)# vrf red
(twamp-reflector)# commit
```

Commit complete.

```text
(twamp-reflector)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp sender administrative-status`

> **Página:** 1537 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the TWAMP Control-Client global administrative-status on the device.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `administrative-status status` — Activate (up) or deactivate (down) the TWAMP Control-Client global administrative status. — *Valores:* up | down. · *Default:* up

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the global administrative status of TWAMP Control-Client on this device.

```text
(config)# oam twamp sender administrative-status down
(config-connection-1)# commit
```

Commit complete.

```text
(config-connection-1)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp sender connection`

> **Página:** 1539 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the TWAMP Control-Client connection administrative-status on the device.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP Control-Client connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `administrative-status status` — Activate (up) or deactivate (down) the TWAMP Control-Client connection. — *Valores:* up | down. · *Default:* up

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 6.2 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the administrative status of TWAMP Control-Client connection on this device.

```text
(config)# oam twamp sender connection 1
(config-connection-1)# administrative-status down
(config-connection-1)# commit
```

Commit complete.

```text
(config-connection-1)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp sender connection`

> **Página:** 1541 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the TWAMP Control-Client connection on the device.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id [ipv4 | ipv6] [source-address | target-address] ipv4 address | ipv6 address
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP Control-Client connection ID. — *Valores:* 1 - 255 · *Default:* N/A
- `[ipv4 | ipv6] source-address ipv4 address | ipv6 address` — Configure the TWAMP Control-Client source address. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `[ipv4 | ipv6] target-address ipv4 address | ipv6 address` — Configure the TWAMP Control-Client target address. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 5.0 | The connection range was modified from [0..255] to [1..255]. |
| 6.4 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the TWAMP Control-Client connection on this device.

```text
(config)# oam twamp sender connection 1
(config-connection-1)#
(config-connection-1)# ipv4 source-address 192.168.0.26
(config-source-address-192.168.0.26)# exit
(config-connection-1)# ipv4 target-address 192.168.0.25
(config-target-address-192.168.0.25)# exit
(config-connection-1)# commit
```

Commit complete.

```text
(config-connection-1)#
```

**Impacts and precautions:**

The number of TWAMP Control-Client connection is limited to 10 connections. The number of TWAMP-Test sessions is limited to 8 per connection or 10 TWAMP-Test sessions globally in the device.

**Hardware restrictions:**

N/A


### `twamp sender connection interval`

> **Página:** 1544 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the test interval in seconds.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id test-interval interval
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP Control-Client connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `test-interval interval` — Configure the test interval in seconds. — *Valores:* 0 - 65535 · *Default:* 300

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 6.2 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the TWAMP Control-Client connection on this device.

```text
(config)# oam twamp sender connection 1
(config-connection-1)# test-interval 60
(config-connection-1)# commit
```

Commit complete.

```text
(config-connection-1)#
```

**Impacts and precautions:**

All TWAMP-Test sessions of a connection will start after test-interval counting. Before the first round of tests the state of all TWAMP-Test sessions will show – indicating that tests don’t run yet.

**Hardware restrictions:**

N/A


### `twamp sender connection number-of-packets`

> **Página:** 1546 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the number of packets sent on every TWAMP-Test session.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id number-of-packets number
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP Control-Client connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `number-of-packets number` — Configure the number of packets sent on every test-session. — *Valores:* 1 - 65535 · *Default:* 50

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 6.4 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the number of packets used on every TWAMP-Test session on this device.

```text
(config)# oam twamp sender connection 1
(config-connection-1)# number-of-packets 100
(config-connection-1)# commit
```

Commit complete.

```text
(config-connection-1)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp sender connection server-port`

> **Página:** 1548 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the server port number for TCP connection.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id server-port TCP port
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP Control-Client connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `server-port` — Configure the server port number for TCP connection. — *Valores:* 1024 - 65535 · *Default:* 862

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 6.4 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the server port of the TWAMP Control-Client connection on this device.

```text
(config)# oam twamp sender connection 1
(config-connection-1)# server-port 1024
(config-connection-1)# commit
```

Commit complete.

```text
(config-connection-1)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp sender connection test-session`

> **Página:** 1550 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the TWAMP-Test sessions in the device.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id test-session test-session ID [ipv4 | ipv6] [source-address | target-address] ipv4 address | ipv6 address
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP sender connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `test-session` — Configure the TWAMP-Test session. — *Valores:* 1 - 255 · *Default:* N/A
- `[ipv4 | ipv6] source-address ipv4 address | ipv6 address` — Configure the TWAMP-Test session source address. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `[ipv4 | ipv6] target-address ipv4 address | ipv6 address` — Configure the TWAMP-Test session target address. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 5.0 | The test-session range was modified from [0..255] to [1..255]. |
| 6.4 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the TWAMP-Test sessions on this device.

```text
(config)# oam twamp sender connection 1
(config-connection-1)# test-session 1
(config-test-session-1)# ipv4 source-address 192.168.0.26
(config-source-address-192.168.0.26)# exit
(config-test-session-1)# ipv4 target-address 192.168.0.25
(config-target-address-192.168.0.25)# exit
(config-test-session-1)# commit
```

Commit complete.

```text
(config-test-session-1)#
```

**Impacts and precautions:**

The number of TWAMP sender connection is limited to 10 connections. The number of TWAMP-Test sessions is limited to 8 per connection or 10 TWAMP-Test sessions globally in the device.

**Hardware restrictions:**

N/A


### `twamp sender connection test-session dscp`

> **Página:** 1553 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the DSCP used in TWAMP-Test sessions.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id test-session test-session ID dscp dscp value
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP sender connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `test-session test-session ID` — Configure the TWAMP-Test session. — *Valores:* 1 - 255 · *Default:* N/A
- `dscp dscp value` — Configure the DSCP used in TWAMP-Test sessions. — *Valores:* 0 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 | 30 | 32 | 34 | 36 | 38 | 40 | 46 | 48 | 56 · *Default:* 0

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 6.4 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the DSCP used in TWAMP-Test session on this device.

```text
(config)# oam twamp sender connection 1
(config-connection-1)# test-session 1
(config-test-session-1)# dscp 56
(config-test-session-1)# commit
```

Commit complete.

```text
(config-test-session-1)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp sender connection test-session max-port`

> **Página:** 1556 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the UDP maximum port number used in TWAMP-Test sessions.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id test-session test-session ID max-port UDP port
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP sender connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `test-session test-session ID` — Configure the TWAMP-Test session. — *Valores:* 1 - 255 · *Default:* N/A
- `max-port UDP port` — Configure the UDP maximum port number. — *Valores:* 1024 - 65535 · *Default:* 65535

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 6.2 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the UDP maximum port of a TWAMP-Test session on this device.

```text
(config)# oam twamp sender connection 1
(config-connection-1)# test-session 1
(config-test-session-1)# max-port 6500
(config-test-session-1)# commit
```

Commit complete.

```text
(config-test-session-1)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp sender connection test-session min-port`

> **Página:** 1559 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the UDP minimum port number used in TWAMP-Test sessions.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id test-session test-session ID min-port UDP port
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP sender connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `test-session test-session ID` — Configure the TWAMP-Test session. — *Valores:* 1 - 255 · *Default:* N/A
- `min-port UDP port` — Configure the UDP minimum port number. — *Valores:* 1024 - 65535 · *Default:* 1024

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 6.2 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the UDP minimum port of a TWAMP-Test session on this device.

```text
(config)# oam twamp sender connection 1
(config-connection-1)# test-session 1
(config-test-session-1)# min-port 2048
(config-test-session-1)# commit
```

Commit complete.

```text
(config-test-session-1)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp sender connection test-session packet-size`

> **Página:** 1562 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the size of packets sent in TWAMP-Test sessions.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id test-session test-session ID packet-size size
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP sender connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `test-session test-session ID` — Configure the TWAMP-Test session. — *Valores:* 1 - 255 · *Default:* N/A
- `packet-size size` — Configure the size of packets sent in TWAMP-Test sessions. — *Valores:* 64 - 65535 · *Default:* 64

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 6.2 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the packet size used in a TWAMP-Test session on this device.

```text
(config)# oam twamp sender connection 1
(config-connection-1)# test-session 1
(config-test-session-1)# packet-size 128
(config-test-session-1)# commit
```

Commit complete.

```text
(config-test-session-1)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `twamp sender connection vrf`

> **Página:** 1565 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Assign a VRF instance to TWAMP Control-Client connection.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
oam twamp sender connection connection-id vrf vrf-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `connection-id` — Configure the TWAMP Control-Client connection ID. — *Valores:* 1 - 65535 · *Default:* N/A
- `vrf vrf-name` — Assign a VRF instance to TWAMP Control-Client connection. — *Valores:* Name of an existent VRF. · *Default:* global

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |
| 6.2 | The connection ID range was modified from [1..255] to [1..65535]. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example shows how to assign the VRF to TWAMP Control-Client connection.

```text
(config)# oam twamp sender connection 1
(config-connection-1)# vrf red
(config-connection-1)# commit
```

Commit complete.

```text
(config-connection-1)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A SFLOW This topic describes the commands related to the configuration of sFlow Protocol.


## sFlow

### `sflow agent ipv4`

> **Página:** 1567 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the IP address of sFlow agent

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam sflow agent ipv4 ip
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `agent ipv4 ip` — Specifies the agent IPv4 identifier. — *Valores:* a.b.c.d · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. The IP address of sFlow agent is not mandatory and if it is not configured, the IP from management interface will be used. In case outband management IP is not available, the address 0.0.0.0 is used. Example: This example shows how to configure the IP address (identifier) of sFlow agent.

```text
(config)# oam
(oam)# sflow agent ipv4 192.168.0.26
(sflow)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `sflow collector`

> **Página:** 1569 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a sFlow collector

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam sflow collector name ipv4 address [ enabled | disabled ] [ max-datagram-size size ] [ port value ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `name` — Specifies a name for the collector. — *Valores:* String (1-32 characters) · *Default:* N/A
- `ipv4 address` — Specifies collector IPv4 address. — *Valores:* a.b.c.d · *Default:* N/A
- `enabled` — Enables the collector (this is set by default) — *Valores:* n/a · *Default:* N/A
- `disabled` — Disables the collector. — *Valores:* n/a · *Default:* N/A
- `max-datagram-size size` — Specifies the maximum datagram size of sFlow packets — *Valores:* 200-9116 · *Default:* 1400
- `port value` — Specifies the sFlow collector listening UDP port number. — *Valores:* 1-65535 · *Default:* 6343

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a sFlow collector.

```text
(config)# oam
(oam)# sflow collector collector_1
(config-sflow-collector-collector_1)# ipv4 10.1.1.1
(config-sflow-collector-collector_1)# commit
```

Commit complete.

```text
(config-sflow-collector-collector_1)#
```

Example: This example shows how to configure a sFlow collector UDP port and maximum datagram size.

```text
(config)# oam
(oam)# sflow collector collector_1
(config-sflow-collector-collector_1)# port 32768
(config-sflow-collector-collector_1)# max-datagram-size 4500
(config-sflow-collector-collector_1)# commit
```

Commit complete.

```text
(config-sflow-collector-collector_1)#
```

**Impacts and precautions:**

The collector IP address must be reachable through mgmt or L3 interface. The maximum datagram size must take into account the maximum header size configured at the interfaces, otherwise samples may be dropped. Also, if those values are close enough to each other, it may happen to have sFlow datagrams with 0 (zero) samples sent to collector.

**Hardware restrictions:**

N/A


### `sflow interface`

> **Página:** 1572 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the interface to be monitored by sFlow.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
oam sflow interface interface [ counter-sampling-collector collector-name | countersampling-interval interval | flow-sampling-collector collector-name | flow-samplingrate rate | max-header-size size ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface` — Specifies the interface to be monitored. — *Valores:* String · *Default:* N/A
- `flow-sampling-rate rate` — Specifies the interface sampling rate in the format 1/rate. Flow sampling average of 1 out of N packets transmitted or received on the port. — *Valores:* 4096-16777215 for gigabit-ethernet 4096-16777215 for ten-gigabit-ethernet 4096-16777215 for twenty-five-g-ethernet 20480-16777215 for forty-gigabit-ethernet 51200-16777215 for hundred-gigabit-ethernet · *Default:* 8192 for gigabit-ethernet
- `20480 for ten-gigabit-ethernet 51200 for twenty-five-g-ethernet 81920 for forty-gigabit-ethernet 204800 for hundred-gigabit-ethernet max-header-size size` — Specifies the sFlow maximum header size in bytes. — *Valores:* 64-512 · *Default:* 128
- `flow-sampling-collector collector-name` — Specifies the collector to send flow samples. — *Valores:* String · *Default:* N/A
- `counter-sampling-collector collector-name` — Specifies the collector to send counter samples. — *Valores:* String · *Default:* N/A
- `counter-sampling-interval interval` — Specifies the time interval in seconds to send a new counter sampling to counter collector. — *Valores:* 2-3600 · *Default:* 20

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |
| 5.10 | Added support for 25G interfaces. |

**Usage Guidelines:**

This command can be executed directly via CLI. Only Ethernet interfaces are supported. Link Aggregation and L3 interfaces are not supported. Example: This example shows how to configure an interface to be monitored by sFlow.

```text
(config)# oam
(oam)# sflow
(sflow)# collector collector_1 ipv4 10.1.1.1
(sflow-collector-collector_1)# interface gigabit-ethernet-1/1/1
(sflow-gigabit-ethernet-1/1/1)# flow-sampling-collector collector_1
(sflow-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(sflow-gigabit-ethernet-1/1/1)#
```

Example: This example shows how to configure a sampling rate in a monitored interface.

```text
(config)# oam
(oam)# sflow
(sflow-collector-collector_1)# interface gigabit-ethernet-1/1/1
(sflow-gigabit-ethernet-1/1/1)# flow-sampling-rate 8192
(sflow-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(sflow-gigabit-ethernet-1/1/1)#
```

Example: This example shows how to configure the maximum header size in a monitored interface.

```text
(config)# oam
(oam)# sflow
(sflow-collector-collector_1)# interface gigabit-ethernet-1/1/1
(sflow-gigabit-ethernet-1/1/1)# max-header-size 256
(sflow-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(sflow-gigabit-ethernet-1/1/1)#
```

You can use ranges and wildcards to edit more than one interface at once. Note that range operations do not add new interfaces, they only act on already added interfaces.

```text
(config)# oam
(oam)# sflow
(sflow)# collector collector_1 ipv4 10.1.1.1
(sflow-collector-collector_1)# interface gigabit-ethernet-1/1/1
(sflow-gigabit-ethernet-1/1/1)# interface gigabit-ethernet-1/1/3
(sflow-gigabit-ethernet-1/1/3)# interface ten-gigabit-ethernet-1/1/1
(sflow-ten-gigabit-ethernet-1/1/1)# exit
(sflow)# interface gigabit-ethernet-1/1/1-3
(sflow-gigabit-ethernet-1/1/1-3)# flow-sampling-rate 5000
(sflow-gigabit-ethernet-1/1/1-3)# interface ten-gigabit-ethernet-1/1/*
(sflow-ten-gigabit-ethernet-1/1/*)# flow-sampling-rate 40000
(sflow-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(sflow-gigabit-ethernet-1/1/1)# top
(config)# show oam sflow
oam
sflow
interface gigabit-ethernet-1/1/1
flow-sampling-rate 5000
!
interface gigabit-ethernet-1/1/2
flow-sampling-rate 5000
!
interface gigabit-ethernet-1/1/3
flow-sampling-rate 5000
!
interface ten-gigabit-ethernet-1/1/1
flow-sampling-rate 40000
!
!
!
```

Example: This example shows how to configure an interface to send counter samples to a counter collector.

```text
(config)# oam
(oam)# sflow
(sflow)# collector collector_1 ipv4 10.1.1.1
(sflow-collector-collector_1)# interface gigabit-ethernet-1/1/1
(sflow-gigabit-ethernet-1/1/1)# counter-sampling-collector collector_1
(sflow-gigabit-ethernet-1/1/1)# counter-sampling-interval 10
(sflow-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(sflow-gigabit-ethernet-1/1/1)#
```

**Impacts and precautions:**

Once an interface and collector are configured in sFlow, it starts sampling on that interface with default sampling rate. In order to disable the sampling, the user must remove the interface or collector from sFlow. Some sample packets can be dropped if the maximum datagram size does not take into account the maximum header size. For egress flow sampling, only unicast packets are sent to sflow collector. Multicast, broadcast and unknown unicast packets are not supported in the egress direction.

**Hardware restrictions:**

N/A REMOTE DEVICES MANAGEMENT This topic describes the commands related to Remote Devices Management (RDM) such as commands to allow remote control by a master device.


## Remote Devices Management

### `remote-devices`

> **Página:** 1577 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Remote Devices Management (RDM) configuration.

**Supported Platforms:** This command is supported only in the following platforms: DM4340, DM4360, DM4370.

**Syntax:**

```text
remote-devices mode operational-mode interface interface-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mode operational-mode` — Set the RDM operational mode on the equipment. — *Valores:* slave · *Default:* slave
- `interface interface-name` — Ethernet interface where RDM is being enabled. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.2 | This command was introduced. |

**Usage Guidelines:**

RDM can be enabled on Ethernet interfaces to allow the remote control by a master device. EFM protocol must be enabled on the interface to allow the configuration.

```text
# config
(config)# oam efm interface gigabit-ethernet-1/1/1
(config-oam-efm-interface-gigabit-ethernet-1/1/1)# mode passive
(config-oam-efm-interface-gigabit-ethernet-1/1/1)# top
(config)# remote-devices interface gigabit-ethernet-1/1/1
(rdm-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(rdm-gigabit-ethernet-1/1/1)# end
#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show remote-devices`

> **Página:** 1579 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display information about RDM status and configuration. This show only presents ports that are configured for RDM.

**Supported Platforms:** This command is supported only in the following platforms: DM4340, DM4360, DM4370.

**Syntax:**

```text
show remote-interface interface [ port ]
```

**Parameters:**

- `port` — The Interface with RDM whose status is desired to show. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.2 | This command was introduced. |

**Usage Guidelines:**

Given the equipment has established the communication with another equipment through RDM protocol and the following port configured for RDM.

```text
# show running-config remote-devices
remote-devices
interface gigabit-ethernet-1/1/1
!
!
#
```

A show will present:

```text
# show remote-devices
remote-devices
mode slave
received vlan-id 100
received ip-address 63.161.169.137/16
received default-gateway 63.161.169.1
```

INTERFACE NAME STATE OUI OID ... --------------------------------------------------------------------... gigabit-ethernet-1/1/1 ready 00:04:df 1.3.6.1.4.1.3709.1.2.91 ... gigabit-ethernet-1/1/2 detected 00:04:df 1.3.6.1.4.1.3709.1.2.91 ... VENDOR SERIAL REMOTE NUMBER MAC ADDRESS NUMBER INTERFACE ------------------------------------------------ 1 00:04:df:10:11:12 1731295 eth 1/20 1 00:04:df:10:11:12 8721983 eth 1/23

```text
#
```

**Output Terms:**

Output Description MODE RDM operational mode configured on equipment. RECEIVED VLAN ID VLAN ID configuration received from remote equipment. RECEIVED IP IP address configuration received from remote equipment. ADDRESS RECEIVED DEFAULT Default Gateway address configuration received from remote equipGATEWAY ment. Output Description INTERFACE NAME The Interface that is configured for RDM. STATE The current state of the RDM protocol on port. OUI Organization Unique Identifier received from remote equipment. OID The SNMP Object Identifier from remote equipment. VENDOR NUMBER Vendor specific information from remote equipment. MAC ADDRESS MAC Address in hexadecimal presentation from remote equipment. SERIAL NUMBER Serial Number from remote equipment. REMOTE INTERFACE The remote interface with the communication established.

**Impacts and precautions:**

None

**Hardware restrictions:**

None ICMP-PROBE This topic describes the commands related to management of ICMP ping tests.


## ICMP-Probe

### `icmp-probe`

> **Página:** 1582 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a ICMP-probe ping test. This feature enables the use of ICMP ECHO packets (according to RFC-792) to measure network metrics such as Round-Trip Time (RTT) between devices. As described in RFC-4560, this mechanism allows for remote ping operations, where a device sends ICMP ECHO_REQUEST packets to a target and waits for the corresponding ECHO_REPLY. The time between sending and receiving these packets is calculated to determine RTT statistics. The results are stored on DATACOM-PING-MIB, that implements the DISMAN-PING-MIB, and can be queried by the SNMP manager for connectivity monitoring, fault diagnosis, and network performance analysis.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
icmp-probe ping-test test-name [description text] [source-address source-address] [target-address target-address] [target-address-type {ipv4}] [data-size value] [timeout value] [probe-count value] [admin-status status] [frequency value] [history-table-max-rows value]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `ping-test test-name` — Configures a remote ping test. Up to 10 ping test configuration entries are supported. — *Valores:* The name of the ping test. · *Default:* N/A
- `description text` — Specifies a textual description of the ping test. It may point out a more meaningful text about its purpose. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* Must be a valid string. · *Default:* N/A
- `target-address-type` — Specifies the type of host address to be used at a remote host for performing a ping operation. For now, only ipv4 is supported. — *Valores:* ipv4 · *Default:* ipv4
- `source-address source-address` — Specifies the source host address to be used for performing a ping operation. The source address type is determined by the value of the corresponding target-address-type. — *Valores:* The network address of the source host. · *Default:* N/A
- `target-address target-address` — Specifies the host address to be used at a remote host for performing a ping operation. The host address type is determined by the value of the corresponding target-address-type. — *Valores:* The network address of the target host. · *Default:* N/A
- `data-size value` — Specifies the size of the data portion to be transmitted in a ping operation, in octets. — *Valores:* 0 - 65507 · *Default:* 0
- `timeout value` — Specifies the time-out value, in seconds, for a remote ping operation. — *Valores:* 1 - 60 · *Default:* 3
- `probe-count value` — Specifies the number of times to perform a ping operation at a remote host as part of a single ping test. — *Valores:* 1 - 15 · *Default:* 1
- `admin-status status` — Reflects the desired state that the ping test should be in: • enabled: test should be started. • disabled: test should be stopped. — *Valores:* {enabled | disabled} · *Default:* enabled
- `frequency value` — The number of seconds to wait before repeating a ping test. A single ping test consists of a series of ping probes. The number of probes is determined by the value of the corresponding probe-count. After a single test is completed, the number of seconds as defined by the value of frequency must elapse before the next ping test is started. A value of 0 for this object implies that the test will not be repeated. — *Valores:* The desired frequency in seconds. · *Default:* 0
- `history-table-max-rows value` — The maximum number of rows allowed in the pingProbeHistoryTable for a configured ping test. The pingProbeHistoryTable stores results of the ping test probes. This field is responsible for limiting the numbers of rows for its respective ping test. Once the number of rows in the pingProbeHistoryTable reaches the value specified by history-table-maxrows for the corresponding ping test, the oldest entry is removed to allow the addition of a new entry. A value of 0 for this parameter means that no history of the ping test will be saved, therefore setting this parameter to 0 from a non 0 value will discard all existing probe history entries saved. In DmOS, the probe results stored in the pingProbeHistoryTable can be queried through the DATACOM-PING-MIB. — *Valores:* 0 - 500 · *Default:* 50

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.6 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. See usage examples below: To configure a ping test with target address 10.10.10.1, the following command must be issued:

```text
(config)#
(config)# icmp-probe ping-test "my-ping-test"
(config-ping-test-my-ping-test)# target-address 10.10.10.1
(config-ping-test-my-ping-test)# commit
```

To configure a ping test with probe-count 15, timeout of 5 seconds and frequency of 60 seconds, the following command must be issued:

```text
(config)#
(config)# icmp-probe ping-test "my-ping-test" target-address 10.10.10.1
(config-ping-test-my-ping-test)# probe-count 15
(config-ping-test-my-ping-test)# timeout 5
(config-ping-test-my-ping-test)# frequency 60
(config-ping-test-my-ping-test)# commit
```

To check if the configuration was applied, issue the show running-config icmp-probe command:

```text
#show running-config icmp-probe
icmp-probe ping-test my-ping-test
target-address 10.10.10.1
probe-count 15
timeout 5
frequency 60
!
```

To configure a ping test with admin status disabled, the following command must be issued:

```text
(config)#
(config)# icmp-probe ping-test "my-ping-test" target-address 10.10.10.1
(config-ping-test-my-ping-test)# admin-status disabled
(config-ping-test-my-ping-test)# commit
```

To configure a ping test with at max 25 of probe history entries, the following command must be issued:

```text
(config)#
(config)# icmp-probe ping-test "my-ping-test" target-address 10.10.10.1
(config-ping-test-my-ping-test)# history-table-max-rows 25
(config-ping-test-my-ping-test)# commit
```

To check if the configuration was applied, issue the show running-config icmp-probe command: icmp-probe ping-test my-ping-test target-address 10.10.10.1 history-table-max-rows 25

```text
!
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show icmp-probe`

> **Página:** 1588 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays ICMP-Probe information.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
show icmp-probe [ping-test test-name]
```

**Parameters:**

- `None` — Displays all ICMP-Probe information. — *Valores:* N/A · *Default:* N/A
- `ping-test test-name` — Displays ICMP-Probe information of the specified ping test. — *Valores:* Name of the configured ping test. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.6 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples shows how to use the show icmp-probe commands.

```text
# show icmp-probe
icmp-probe ping-test my-ping-test
Description : -
Operation status : enabled
```

Target address type : ipv4 Target address : 10.10.10.1 Min-rtt(ms) : 5 Max-rtt(ms) : 20 Average-rtt(ms) : 10 Probe responses : 15 Sent probes : 15 Rtt-sum-of-squares : 400 Last good probe : 2024-06-03T00:00:00-03:00

```text
# show icmp-probe ping-test my-ping-test
icmp-probe ping-test my-ping-test
Description : datacom
Operation status : disabled
```

Target address type : ipv4 Target address : 10.10.10.1 Min-rtt(ms) : 0 Max-rtt(ms) : 0 Average-rtt(ms) : 0 Probe responses : 0 Sent probes : 0 Rtt-sum-of-squares : 0 Last good probe : -

**Output Terms:**

Output Description Description A textual description of the ping test. Output Description The operational state of the ping test: • enabled: test is active; Operation status • disabled: test has stopped; • completed: test is completed. Target address Indicates the type of the target address. type Target address The network address of the target host. Min-rtt The minimum ping round-trip-time (RTT) received in milliseconds. Max-rtt The maximum ping round-trip-time (RTT) received in milliseconds. Average-rtt The current average ping round-trip-time (RTT) in milliseconds. Probe responses Number of responses received. Sent probes Number of probes sent. Rtt-sum-of-squares Sum of the squares for all ping responses received. Last good probe Date and time when the last response was received for a probe.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A CHAPTER 13: SYNCHRONIZATION This chapter describes the CLI commands related to time synchronization signals at DmOS. NTP This topic describes the commands related to management of Network Time Protocol such as commands to configure an external NTP Server or to inspect the system clock.
