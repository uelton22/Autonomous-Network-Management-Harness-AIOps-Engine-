# Capítulo 9: Quality of Service

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## QoS Policer

### `qos policer hierarchical`

> **Página:** 1340 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create hierarchical policer instance.

**Supported Platforms:** This command is supported only in the following platforms: DM4050, DM4250, DM4360, DM4370, DM4376, DM4378, DM4610, DM4611, DM4612, DM4615, DM4616.

**Syntax:**

```text
qos policer hierarchical id profile profile-name [ instance instance-id ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `qos policer hierarchical id` — User defined hierarchical policer instance ID. — *Valores:* 1 - 512 · *Default:* N/A
- `profile profile-name` — Profile of the hierarchical policer instance. — *Valores:* String with up to 48 characters: letters, numbers, ’_‘, and’-’. · *Default:* N/A
- `qos policer instance instance-id` — User defined first level policer instance ID. — *Valores:* 1 - 1280 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 6.0 | This command was introduced. |

**Usage Guidelines:**

Hierarchical policer instances can be created to police lower level policer instances which are attached to it. Examples: The following example creates a hierarchical policer instance, that will operate according to profile foo and attach to it two previously created lower level instances.

```text
#config
Entering configuration mode terminal
(config)# qos policer hierarchical 1 profile foo
(policer-hierarchical-1)# instance 1
(policer-hierarchical-1)# instance 2
(policer-hierarchical-1)# top
(config)# commit
```

Commit complete.

```text
(config)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `qos policer instance`

> **Página:** 1343 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create a policer instance and apply it to a network traffic.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
qos policer instance instance-id { interface interface-name } profile profile-name [vlan vlan-id] [pcp pcp] [inner-vlan vlan-id] [name instance-name] [counters { enabled | disabled }]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `qos policer instance instance-id` — User defined policer instance ID. — *Valores:* 1 - 1280 · *Default:* N/A
- `interface interface-name` — Interface the policer instance refers to. Multiple interfaces may be specified, and the policer bandwidth will be shared in this case. — *Valores:* interface-type-chassis/slot/port | lag-id Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, gpon. · *Default:* N/A
- `profile profile-name` — Name of the policer profile created with qos policer profile. — *Valores:* String with a maximum of 48 characters. It only accepts alphanumeric characters and ’_‘,’+‘and’-’. · *Default:* N/A
- `vlan vlan-id` — Apply this policer to a list or to a specific outer VLAN ID. — *Valores:* 1 - 4094 · *Default:* N/A
- `pcp pcp` — Apply this policer to a list or to a specific outer Priority 802.1p. — *Valores:* 0 - 7 · *Default:* N/A
- `inner-vlan vlan-id` — Apply this policer to a list or to a specific inner VLAN ID. The inner VLAN is the second VLAN Tag after ingress VLAN manipulations (QinQ/Vlan Translations). It is applicable only to double tagged packets. — *Valores:* 1 - 4094 · *Default:* N/A
- `inner-pcp pcp` — Apply this policer to a list or to a specific inner Priority 802.1p. The inner Priority 802.1p is the PCP in the second VLAN Tag after ingress VLAN manipulations (QinQ/Vlan Translations). It is applicable only to double tagged packets. — *Valores:* 0 - 7 · *Default:* N/A
- `dscp dscp` — Apply this policer only to a specific IPv4/IPv6 DSCP value. This parameter is only valid for ingress policers. — *Valores:* 0 - 63 | af11 | af12 | af13 | af21 | af22 | af23 | af31 | af32 | af33 | af41 | af42 | af43 | cs1 | cs2 | cs3 | cs4 | cs5 | cs6 | cs7 | ef · *Default:* N/A
- `name instance-name` — Configure a name for the policer instance. — *Valores:* String with a maximum of 48 characters. It only accepts alphanumeric characters and ’_‘,’+‘and’-’. · *Default:* N/A
- `counters` — Configure counters for the policer instance. — *Valores:* { enabled | disabled } · *Default:* disabled

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. Added support for GPON interfaces and added support for filtering the 4.6 traffic by inner-VLAN and inner-pcp. |
| 4.7 | Added support for filtering the traffic by DSCP value. |
| 5.0 | Added support for 25G interfaces. |
| 5.2 | Added support for policer instance counters. |
| 5.4 | Support multiple VLAN ID in the policer instance. |
| 5.6 | Support multiple PCPs in the policer instance. Increase maximum number of policers to 1280. DM4770 supports up to |
| 5.12 | 768 ingress and up to 512 egress policers. DM4270 supports up to 512 or 768 ingress and up to 256 or 512 egress policers according to model. |

**Usage Guidelines:**

Policer instances can be created to police shared bandwidth or exclusive bandwidth. Interfaces entered in the same policer instance parameter are treated as shared bandwidth. Examples: The following example creates one policer instance to police shared bandwidth between two interfaces.

```text
#config
Entering configuration mode terminal
(config)# qos policer instance 1
(policer-instance-1)# interface lag-1
(policer-instance-1)# interface ten-gigabit-ethernet-1/5/2
(policer-instance-1)# profile profile1
(policer-instance-1)# vlan 100-102,110
(policer-instance-1)# counters enabled
(policer-instance-1)# top
(config)# commit
```

Commit complete.

```text
(config)#
```

The following example creates two policer instances to police the same interfaces but as exclusive bandwidths instead of shared.

```text
#config
Entering configuration mode terminal
(config)# qos policer instance 1
(policer-instance-1)# interface lag-1
(policer-instance-1)# profile profile1
(policer-instance-1)# pcp 1
(policer-instance-1)# top
(config)# qos policer instance 2
(policer-instance-2)# interface ten-gigabit-ethernet-1/5/2
(policer-instance-2)# profile profile1
(policer-instance-2)# pcp 1-3
(policer-instance-2)# counters enabled
(policer-instance-1)# top
(config)# commit
```

Commit complete.

```text
(config)#
```

**Impacts and precautions:**

The priority of a Policer instance is determined by its matching filters. For example, an instance with matching filter by PCP has higher priority than an instance with matching filter by VLAN. From higher to lower, the priority order is: inner-PCP, PCP, DSCP, inner-VLAN, VLAN. Instances with multiple matching filters will follow the same priority order. E.g.: The instance with matching filters VLAN 100, PCP 5 and inner-VLAN 500 has higher priority than the instance with matching filter VLAN 100 and inner-VLAN 500. A packet with VLAN 100, PCP 5 and inner-VLAN 500 will be accounted by the first Policer instance, while a packet with VLAN 100, PCP 0 and inner-VLAN 500 will be accounted by the second Policer.

**Hardware restrictions:**

On DM4050, the Policer matching filters do not consider the possible packet modifications due to ACLs rules. On DM4270, DM4770 and DM4380 series: it is not possible to classify the packets by VLAN when applying an Egress Policer in an interface which is an untagged member of that VLAN. On DM4770 series: policer instances cannot contain different speed interfaces.


### `qos policer profile`

> **Página:** 1348 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create and configure a policer profile for ingress and egress Ethernet traffic policing and for PON traffic policing (downstream-pon).

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
qos policer profile profile-name mode { flow | srtcm | trtcm | trtcmds } parameters { cir committed-rate cbs committed-burst eir excess-rate ebs excess-burst pir peak-rate pbs peak-burst } { actions { green | yellow | red } { drop | set-dscp dscp | set-pcp pcp } } stage { ingress | egress | downstream-pon }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `qos policer profile profile-name` — User defined policer profile name. — *Valores:* String with a maximum of 48 characters. It only accepts alphanumeric characters and ’_‘,’+‘and’-’. · *Default:* N/A
- `mode` — Policer configuration mode. — *Valores:* • flow: Single-rate two-color marker mode (flow mode) • srtcm: Single-rate three-color marker mode (RFC 2697) • trtcm: Two-rate three-color marker mode (RFC 2698) • trtcmds: Differentiated Service two-rate three-color marker mode (RFC 4115) · *Default:* flow
- `cir committed-rate` — Commited information rate (kbits/s) — *Valores:* 0 - 100,000,000 · *Default:* N/A
- `cbs committed-burst` — Commited burst size (bytes) — *Valores:* 0 - 268,435,456 · *Default:* N/A
- `eir excess-rate` — Excess information rate (kbits/s) Note: this parameter is only available in policer mode trtcmds. — *Valores:* 0 - 100,000,000 · *Default:* N/A
- `ebs excess-burst` — Excess burst size (bytes) Note: this parameter is only available in policer modes trtcmds and srtcm. — *Valores:* 0 - 268,435,456 · *Default:* N/A
- `pir peak-rate` — Peak information rate (kbits/s) Note: this parameter is only available in policer mode trtcm. — *Valores:* 0 - 100,000,000 · *Default:* N/A
- `pbs peak-burst` — Peak burst size (bytes) Note: this parameter is only available in policer mode trtcm. — *Valores:* 0 - 268,435,456 · *Default:* N/A
- `stage` — Interface traffic stage. — *Valores:* • ingress: apply policing to incoming traffic. • egress: apply policing to outgoing traffic. • downstream-pon: apply policing to downstream PON traffic. · *Default:* N/A
- `actions green` — Actions for green-marked packets. — *Valores:* • drop: Drop packet • set-dscp dscp: Set new value for DSCP (RFC 2474) field • set-pcp pcp: Set new value for PCP (802.1p) field · *Default:* N/A
- `actions yellow` — Actions for yellow-marked packets. When the action for green-marked packets is drop, the actions yellow must be drop as well. Note: not configurable in flow mode as there are no yellow-marked packets on this mode. — *Valores:* • drop: Drop packet • set-dscp dscp: Set new value for DSCP (RFC 2474) field • set-pcp pcp: Set new value for PCP (802.1p) field · *Default:* N/A
- `actions red` — Actions for red-marked packets. When the action for green-marked or yellow-marked packets is drop, the actions red must be drop as well. — *Valores:* • drop: Drop packet • set-dscp dscp: Set new value for DSCP (RFC 2474) field • set-pcp pcp: Set new value for PCP (802.1p) field · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |
| 4.7 | Added support for configuring action set-dscp with RFC2474 classes. |
| 9.8 | Added downstream-pon as an option to stage of policer. |

**Usage Guidelines:**

Example: The following example demonstrates how to create a policer profile. This policer will make red-marked packets be dropped at ingress stage.

```text
#config
Entering configuration mode terminal
(config)# qos policer profile pol1
(policer-profile-pol1)# mode flow
(policer-profile-pol1)# stage ingress
(policer-profile-pol1)# parameters cbs 100000
(policer-profile-pol1)# parameters cir 1000000
(policer-profile-pol1)# actions red drop
(policer-profile-pol1)# top
(config)# commit
```

Commit complete.

```text
(config)#
```

**Impacts and precautions:**

Ingress and Downstream-pon share the same HW resources. When one is in use, the other shall not have available resources. The command ‘show qos policer resources’ will show the available resources.

**Hardware restrictions:**

Only DM4615 and DM4610HW2 support Downstream-pon.


### `show qos policer`

> **Página:** 1353 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays statistics counters for policer instances.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show qos policer [brief] [detail]
```

**Parameters:**

- `brief` — This parameter displays summary information about each policer: instance ID, hierarchical ID, profile name, policer mode, policer stage, CIR, EIR, PIR, interface index, interface name and policer counters (forwarded bytes and dropped bytes). When no parameter is given the show command displays the same content of brief parameter. — *Valores:* N/A · *Default:* N/A
- `detail` — Includes all data presented by brief, and includes extra data about hierarchical policers: CIR, EIR, PIR, and policer counters (forwarded bytes and dropped bytes). — *Valores:* N/A · *Default:* N/A
- `hierarchical` — This parameter displays only the information related to hierarchical policers. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.2 | This command was introduced. |
| 6.0 | Added support for hierarchical policer. Added downstream-pon as an option to stage of policer (only supported 9.8 on DM4615 and DM4610HW2). |

**Usage Guidelines:**

Given the equipment has two policer profiles named foo and bar configured with the flow mode, the command could result in the following output:

```text
# show qos policer
INSTANCE HIERARCHICAL
```

ID ID PROFILE MODE STAGE CIR EIR PIR FORWARDED DROPPED IFINDEX INTERFACE NAME ----------------------------------------------------------------------------------------------------------------------- 1 1 foo flow ingress 10000 - - 1000 100 51412993 gigabit-ethernet-1/1/1 2 1 foo flow ingress 10000 - - 2000 200 51412994 gigabit-ethernet-1/1/2 3 2 foo flow ingress 10000 - - 3000 300 51412995 gigabit-ethernet-1/1/3 Note: When a counter is disabled or unsupported it is displayed as ’-’ HIERARCHICAL INSTANCE ID PROFILE MODE STAGE CIR ID PROFILE ---------------------------------------------------------------- 1 bar flow ingress 20000 1 foo 2 foo 2 bar flow ingress 20000 3 foo Now let’s see the detail information:

```text
# show qos policer detail
INSTANCE HIERARCHICAL
```

ID ID PROFILE MODE STAGE CIR EIR PIR FORWARDED DROPPED IFINDEX INTERFACE NAME ----------------------------------------------------------------------------------------------------------------------- 1 1 foo flow ingress 10000 - - 1000 100 51412993 gigabit-ethernet-1/1/1 2 1 foo flow ingress 10000 - - 2000 200 51412994 gigabit-ethernet-1/1/2 3 2 foo flow ingress 10000 - - 3000 300 51412995 gigabit-ethernet-1/1/3 Note: When a counter is disabled or unsupported it is displayed as ’-’ HIERARCHICAL INSTANCE ID PROFILE MODE STAGE CIR ID PROFILE CIR EIR PIR FORWARDED DROPPED ----------------------------------------------------------------------------------------------------- 1 bar flow ingress 20000 1 foo 10000 - - 1000 100 2 foo 10000 - - 2000 200 2 bar flow ingress 20000 3 foo 10000 - - 3000 300

**Output Terms:**

Output Description INSTANCE ID Policer instance id. HIERARCHICAL ID Hierarchical policer ID. Configured profile for a policer instance, either a regular or hierarPROFILE chical policer. Mode of operation for a policer instance, either a regular or hierarMODE chical policer. STAGE Stage of policer (ingress, egress or downstream-pon). CIR Committed information rate in kbits/s. EIR Excess information rate in kbits/s. PIR Peak information rate in kbits/s. FORWARDED Number of forwarded bytes for a given policer instance. DROPPED Number of dropped bytes for a given policer instance. IF-INDEX Index of the interface configured with a policer instance. IF-NAME Name of the interface configured with a policer instance.

**Impacts and precautions:**

The values presented by this command are accumulated since the last time the operator issued a clear command. Ingress and Downstream-pon share the same HW resources. When one is in use, the other shall not have available resources. The command ‘show qos policer resources’ will show the available resources.

**Hardware restrictions:**

On DM461x, the dropped counters on the egress stage are not supported. Only DM4615 and DM4610HW2 support Downstream-pon.


### `show qos policer resources`

> **Página:** 1357 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays information about the use of policer resources.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show qos policer resources
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |
| 6.0 | Added support for hierarchical policer. Added downstream-pon as an option to stage of policer (only supported 9.8 on DM4615 and DM4610HW2). |

**Usage Guidelines:**

Given the equipment has two policer instances, this command would result in the following output:

```text
# show qos policer resources
STAGE TOTAL USED FREE
-----------------------------------
ingress 0 0 0
egress 128 76 52
downstream-pon 512 1 511
* Ingress and Downstream-pon share the same HW resources, so, when using one of them, the other
will have no available resources
INSTANCE HIERARCHICAL
```

ID ID PROFILE STAGE RESOURCES -------------------------------------------------------- 1 - bar egress 76 5 - foo downstream-pon 1

**Output Terms:**

Output Description qos policer total Total ingress policer resources. ingress resources qos policer used Used ingress policer resources. ingress resources qos policer free Free ingress policer resources. ingress resources qos policer total Total egress policer resources. egress resources qos policer used Used egress policer resources. egress resources Output Description qos policer free Free egress policer resources. egress resources qos policer total downstream-pon Total downstream-pon policer resources. resources qos policer used downstream-pon Used downstream-pon policer resources. resources qos policer free downstream-pon Free downstream-pon policer resources. resources INSTANCE ID Policer instance id. HIERARCHICAL ID Hierarchical policer ID. Configured profile for a policer instance, either a regular or hierarPROFILE chical policer. STAGE Stage of policer (ingress, egress or downstream-pon). Number of resources used by this policer instance, either a regular RESOURCES or hierarchical policer.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A QOS PACKET SCHEDULER AND EGRESS SHAPERS This topic describes the commands related to QoS Packet Scheduler such as commands to configure Strict Priority or Early Discard at individual queues, and commands to set rate limits at egress interfaces.


## QoS Packet Scheduler and Egress Shapers

### `qos interface scheduler-profile`

> **Página:** 1360 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Set a QoS Scheduler Profile into an interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
qos interface interface-identification [scheduler-profile {profile-name}]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-identification` — Identifies the interface to be configured. — *Valores:* interface-type-chassis/slot/port Where interface-type can assume gigabit-ethernet, ten-gigabit-ethernet, forty-gigabit-ethernet or gpon. · *Default:* N/A
- `scheduler-profile profile-name` — The profile name to be set in specified interface. It MUST assume one of the previous created profiles. — *Valores:* String · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. |
| 3.0 | Added support for 40G interfaces. |

**Usage Guidelines:**

This command associates a QoS Scheduler Profile to a specific interface. To set a QoS Scheduler Profile to an interface you have to first create the QoS Scheduler Profile: DMOS(config)# qos scheduler-profile testXYZ DMOS(config-qos-scheduler-profile-testXYZ)# mode wfq DMOS(config-qos-scheduler-profile-testXYZ)# queue 0 weight 5 DMOS(config-qos-sch-prof-queue-0)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 1 weight 5 DMOS(config-qos-sch-prof-queue-1)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 2 weight 5 DMOS(config-qos-sch-prof-queue-2)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 3 weight 5 DMOS(config-qos-sch-prof-queue-3)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 4 weight 5 DMOS(config-qos-sch-prof-queue-4)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 5 weight 5 DMOS(config-qos-sch-prof-queue-5)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 6 weight 70 DMOS(config-qos-sch-prof-queue-6)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 7 weight SP DMOS(config-qos-sch-prof-queue-7)# top DMOS(config)# commit Commit complete. DMOS(config)# Now let’s associate the created profile to an interface: DMOS(config)# qos interface gigabit-ethernet 1/1/1 scheduler-profile testXYZ DMOS(config-qos-interface-gigabit-ethernet 1/1/1)# After that let’s check the config and commit it: DMOS(config-qos-interface-gigabit-ethernet 1/1/1)# top DMOS(config)# show full-configuration qos interface gigabit-ethernet 1/1/1 scheduler-profile testXYZ

```text
!
qos scheduler-profile testXYZ
mode wfq
queue 0
weight 5
!
queue 1
weight 5
!
queue 2
weight 5
!
queue 3
weight 5
!
queue 4
weight 5
!
queue 5
weight 5
!
queue 6
weight 70
!
queue 7
weight SP
!
!
DMOS(config)# commit
```

Commit complete. DMOS(config)#

**Impacts and precautions:**

Using SP for a queue’s weight could cause starvation for other queues.

**Hardware restrictions:**

None


### `qos scheduler-profile`

> **Página:** 1363 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure a QoS Scheduler profile to be applied on interfaces.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
qos scheduler-profile profile-name [mode {wfq} | queue queue-index [weight weightvalue]]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `profile-name` — The QoS Scheduler profile identifier. This value is used to distinguish the various profiles. It’s possible to create up to 500 different profiles. — *Valores:* String · *Default:* N/A
- `mode` — Define the QoS Scheduling mode. — *Valores:* wfq (Weighted Fair Queue) · *Default:* N/A
- `queue` — Perform configuration of a specific scheduler queue. — *Valores:* 0-7 · *Default:* N/A
- `weight` — Weight of an specific queue related to the pre-selected scheduling mode. It can assume a numeric percent bandwidth value or the Strict Priority (SP) tag. — *Valores:* 1-100 | SP · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. |

**Usage Guidelines:**

This command is used to define a QoS Scheduler Profile. After it’s done, it’s necessary to associate the profile to an interface in order to the QoS profile take effect over the outgoing traffic of the interface. Each profile can have only one scheduling mode at a time. Once the mode is set it enables the queues’ creation and configuration. Each mode must have all its queues created and configured with a weight. The weight represents the percentage of available bandwidth, and the sum of the weights must be 100. The current supported scheduling mode is WFQ (Weighted Fair Queue), which balances the egress traffic according to the weights set in its queues. The scheduling is based on bytes. To configure a QoS Scheduler Profile the first thing to do is to create the profile: DM4610(config)# qos scheduler-profile testXYZ DM4610(config-profile-testXYZ)# Now let’s configure the scheduling mode: DM4610(config-profile-testXYZ)# mode wfq DM4610(config-profile-testXYZ)# Then it’s necessary to configure all queues: DMOS(config)# qos scheduler-profile testXYZ DMOS(config-qos-scheduler-profile-testXYZ)# mode wfq DMOS(config-qos-scheduler-profile-testXYZ)# queue 0 weight 5 DMOS(config-qos-sch-prof-queue-0)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 1 weight 5 DMOS(config-qos-sch-prof-queue-1)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 2 weight 5 DMOS(config-qos-sch-prof-queue-2)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 3 weight 5 DMOS(config-qos-sch-prof-queue-3)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 4 weight 5 DMOS(config-qos-sch-prof-queue-4)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 5 weight 5 DMOS(config-qos-sch-prof-queue-5)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 6 weight 70 DMOS(config-qos-sch-prof-queue-6)# exit DMOS(config-qos-scheduler-profile-testXYZ)# queue 7 weight SP DMOS(config-qos-sch-prof-queue-7)# exit DMOS(config-qos-scheduler-profile-testXYZ)# Now let’s check the configuration and commit it: DMOS(config-qos-scheduler-profile-testXYZ)# top DMOS(config)# show full-configuration qos scheduler-profile testXYZ mode wfq queue 0 weight 5

```text
!
queue 1
weight 5
!
queue 2
weight 5
!
queue 3
weight 5
!
queue 4
weight 5
!
queue 5
weight 5
!
queue 6
weight 70
!
queue 7
weight SP
!
!
DMOS(config)# commit
```

Commit complete. DMOS(config)#

**Impacts and precautions:**

Using SP for a queue’s weight could cause starvation for other queues. To remove a profile it’s necessary to remove all interfaces assignments to the referred profile. So in the following scenario to remove myProfile1 we have to: DMOS(config)# show full-configuration qos interface gigabit-ethernet 1/1/1 scheduler-profile myProfile1

```text
!
qos interface gigabit-ethernet 1/1/2
scheduler-profile myProfile2
!
qos scheduler-profile myProfile1
mode wfq
(...)
!
qos scheduler-profile myProfile2
mode wfq
(...)
!
```

DMOS(config)# qos interface gigabit-ethernet 1/1/1 DMOS(config-qos-interface-gigabit-ethernet 1/1/1)# no scheduler-profile DMOS(config-qos-interface-gigabit-ethernet 1/1/1)# top DMOS(config)# no qos scheduler-profile myProfile1 DMOS(config)# commit Commit complete. DMOS(config)#

**Hardware restrictions:**

N/A


### `rate-limit`

> **Página:** 1367 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Limits the traffic of an interface according to a configurable bandwidth and burst.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
rate-limit { egress | ingress } bandwidth value burst value
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `egress` — Configure rate-limit parameters to egress traffic. — *Valores:* N/A · *Default:* N/A
- `ingress` — Configure rate-limit parameters to ingress traffic. — *Valores:* N/A · *Default:* N/A
- `bandwidth value` — Bandwidth, in kbps, to limit the traffic. — *Valores:* 100-400000000 · *Default:* N/A
- `burst value` — Accepted burst rate in kbytes. — *Valores:* 2-2000 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.12 | This command was introduced. |
| 2.0 | Added rate-limit mode ingress. |
| 3.0 | Added support for 40G interfaces. |
| 4.6 | Added support for 100G interfaces. |
| 5.1 | Added support for 25G interfaces. |
| 7.0 | Removed support for 25G, 40G and 100G interfaces. |
| 9.0 | Re-added support for 25G, 40G and 100G interfaces. |
| 10.8 | Added support for 200G and 400G interfaces. |
| 10.8 | Change the maximum bandwidth to support 200G and 400G interfaces. |

**Usage Guidelines:**

This command is located inside qos node. So, to configure a rate limit into an interface follow these steps: Access the interface in qos node. DmOS(config)# qos interface gigabit-ethernet-1/1/1 DmOS(config-qos-interface-gigabit-ethernet-1/1/1)# Now access the rate limit configuration informing the traffic flow to be limited. Suppose egress traffic: DmOS(config-qos-interface-gigabit-ethernet-1/1/1)# rate-limit egress DmOS(config-rate-limit-egress)# Now configure the bandwidth and burst to limit the interface. Both parameters are required. At the end of configuration, commit it: DmOS(config-rate-limit-egress)# bandwidth 64000 DmOS(config-rate-limit-egress)# burst 1024 DmOS(config-rate-limit-egress)# commit Commit complete. DmOS(config-rate-limit-egress)#

**Impacts and precautions:**

N/A

**Hardware restrictions:**

• ingress rate-limit is not supported on DM4270, DM4770 and DM4380 series. • On DM4340 the egress rate limit minimum burst value is 8 kbytes. STORM CONTROL This topic describes the commands related to Storm Control such as commands to configure multicast, broadcast and unknown unicast(DLF) rate limits.


## Storm Control

### `switchport interface storm-control`

> **Página:** 1370 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure Storm Control protection to an interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
switchport interface interface-identification [storm-control { broadcast percent | multicast percent | unicast percent }* ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-identification` — Identifies the ingress interface to be configured. — *Valores:* interface-type-chassis/slot/port Where interface-type can assume gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, two-hundred-g-ethernet, four-hundred-g-ethernet or lag. · *Default:* N/A
- `broadcast percent` — Specifies a rate-limit on an ingress interface for broadcast packets as a percentage of the interface’s nominal speed in steps of 0.01. — *Valores:* 0.01-100.00 · *Default:* N/A
- `multicast percent` — Specifies a rate-limit on an ingress interface for unknown multicast packets as a percentage of the interface’s nominal speed in steps of 0.01. — *Valores:* 0.01-100.00 · *Default:* N/A
- `unicast percent` — Specifies a rate-limit on an ingress interface for unknown unicast (DLF) packets as a percentage of the interface’s nominal speed in steps of 0.01. — *Valores:* 0.01-100.00 · *Default:* N/A

**Default:** Disabled

**History:**

| Release | Modification |
| --- | --- |
| 1.1 | This command was introduced. |
| 3.0 | Added support for 40G and LAG interfaces. |
| 4.6 | Added support for 100G interfaces. |
| 5.1 | Added support for 25G interfaces. |

**Usage Guidelines:**

The following commands enable storm-control for ingress traffic on interface gigabit-ethernet-1/1/1, with rate-limit of 0.5% of interface’s nominal speed for broadcast packets, 10% for unknown multicast packets and 1% for unknown unicast (DLF) packets: DMOS(config)# switchport interface gigabit-ethernet-1/1/1 DMOS(config-switchport-gigabit-ethernet-1/1/1)# storm-control DMOS(config-switchport-gigabit-ethernet-1/1/1-storm-ctrl)# broadcast 0.5 DMOS(config-switchport-gigabit-ethernet-1/1/1-storm-ctrl)# multicast 10 DMOS(config-switchport-gigabit-ethernet-1/1/1-storm-ctrl)# unicast 1 Check the configuration and commit it so it is applied: DMOS(config-switchport-gigabit-ethernet-1/1/1-storm-ctrl)# top DMOS(config)# show configuration this switchport interface gigabit-ethernet-1/1/1 storm-control switchport interface gigabit-ethernet-1/1/1 storm-control broadcast 0.5 multicast 10.0 unicast 1.0

```text
!
!
!
DMOS(config)# commit
```

Commit complete. DMOS(config)# Precede the command with no to disable Storm Control. The following commands disable Storm Control multicast for interface gigabit-ethernet-1/1/1, and then disable all types of Storm Control for the same interface: DMOS(config)# switchport interface gigabit-ethernet-1/1/1 DMOS(config-switchport-gigabit-ethernet-1/1/1)# storm-control DMOS(config-switchport-gigabit-ethernet-1/1/1-storm-ctrl)# no multicast DMOS(config-switchport-gigabit-ethernet-1/1/1-storm-ctrl)# exit DMOS(config-switchport-gigabit-ethernet-1/1/1)# commit Commit complete. DMOS(config-switchport-gigabit-ethernet-1/1/1)# no storm-control DMOS(config-switchport-gigabit-ethernet-1/1/1)# commit Commit complete.

**Impacts and precautions:**

Enabling Storm Control may result in unexpected lost of packets. You can use the command: show interface interface-identification statistics to verify possible dropped packets.

**Hardware restrictions:**

On DM4340, Storm Control for multicast traffic is not enabled. For these devices, it is possible to use Storm Control for unicast traffic, as this setting applies to both unicast and multicast traffic. On DM4780, the maximum value that percent can take is 60% for 200G interfaces and 30% for 400G interfaces. CHAPTER 10: ACCESS LISTS This chapter describes the commands related to management of ACLs in the DmOS CLI. BASIC ACLS This topic describes the commands related to management of ACLs such as commands to configure match criteria or actions.
