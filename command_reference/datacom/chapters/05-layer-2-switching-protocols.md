# Capítulo 5: Layer 2 - Switching Protocols

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## MAC Learning

### `clear mac-address-table`

> **Página:** 372 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** The clear mac-address-table command is used to clear entries learned by the switch.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
clear mac-address-table clear mac-address-table interface interface-name
```

**Parameters:**

- `interface interface-name` — Interface on which to delete L2 entries. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | two-hundred-g-ethernet-chassis/slot/port | four-hundred-g-ethernetchassis/slot/port | lag-id | service-port-id } · *Default:* None

**Default:** N/A. There is no default profile.

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |
| 1.6 | Clear by type blocked and clear by interface were added. |
| 2.2 | Remove clear by type blocked. |
| 3.0 | Added support for 40G interfaces. |
| 4.6 | Added support for 100G interfaces. |
| 5.0 | Added support for 25G interfaces. |
| 12.0 | Added support for 200G and 400G interfaces. |

**Usage Guidelines:**

To clear the entire table:

```text
# clear mac-address-table
```

To clear the entries on a gigabit-ethernet interface:

```text
# clear mac-address-table interface gigabit-ethernet-1/1/9
```

To clear the entries on a service-port:

```text
# clear mac-address-table interface service-port-1
```

**Impacts and precautions:**

Clear confirmation will be asked for the user, once this is a permanent action.

**Hardware restrictions:**

N/A


### `mac-address-table aging-time`

> **Página:** 375 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The mac-address-table aging-time command is used to set the global maximum time that MAC table entries will be stored in the MAC address table without a hit.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
mac-address-table aging-time aging time
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `aging-time` — Maximum time, in seconds, to exclude dynamic MAC table entries. Value of 0 indicates that MAC table entries will never be aged. — *Valores:* 20 to 2000000 0 disables MAC address aging · *Default:* 600

**Default:** N/A. There is no default profile.

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. |

**Usage Guidelines:**

Setting the global MAC address aging time to 500 seconds:

```text
(config)#
(config)# mac-address-table aging time 500
```

To disable MAC address aging time:

```text
(config)#
(config)# mac-address-table aging time 0
```

To go back to the default MAC address aging time:

```text
(config)#
(config)# no mac-address-table aging time
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

Aging time range is from 150 to 1300 for DM4618 platform.


### `mac-address-table interface learning`

> **Página:** 377 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The mac-address-table interface interface-name learning command is used to disable MAC address learning for the specified interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
mac-address-table interface interface-name learning
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Interface on which to configure dynamic MAC table entries learning. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | two-hundred-g-ethernet-chassis/slot/port | four-hundred-g-ethernetchassis/slot/port | lag-id } · *Default:* None
- `learning` — Enable/disable dynamic MAC table entries learning on interface. — *Valores:* enabled | disabled · *Default:* enabled

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 5.0 | Added support for 25G interfaces. |
| 12.0 | Added support for 200G and 400G interfaces. |

**Usage Guidelines:**

Enabling the MAC address learning on interface gigabit-ethernet-1/1/1 :

```text
(config)#
(config)# mac-address-table interface gigabit-ethernet-1/1/1 learning enabled
```

To disable MAC address learning:

```text
(config)#
(config)# mac-address-table interface gigabit-ethernet-1/1/1 learning disabled
```

**Impacts and precautions:**

This command clears all dynamically learned MAC entries on the configured interface. Be careful disabling MAC address learning when storm control unicast is configured on the same interface, it may occur a data loss due to DLF packet flood.

**Hardware restrictions:**

N/A


### `mac-address-table interface limit`

> **Página:** 380 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The mac-address-table interface interface-name limit command is used to set the maximum MAC address table entries that can be learned for the specified interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4270, DM4380, DM4618, DM4770, DM4920.

**Syntax:**

```text
mac-address-table interface interface-name limit maximum entries
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Interface on which to limit MAC table entries. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id } · *Default:* None
- `entries` — Maximum number of dynamic MAC table entries learned on interface. Value of 0 indicates that MAC address table entries will never be learned and traffic will be discarded. — *Valores:* 0 to 16000 0 to disable MAC address learning and data traffic · *Default:* N/|A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 3.0 | Added support for 40G interfaces. |
| 4.0 | Maximum value of parameter limit increased. |
| 4.6 | Added support for 100G interfaces. |
| 5.0 | Added support for 25G interfaces. |

**Usage Guidelines:**

Setting the maximum MAC address to 10 entries on interface gigabit-ethernet-1/1/1 :

```text
(config)#
(config)# mac-address-table interface gigabit-ethernet-1/1/1 limit maximum 10
```

To disable MAC address limit:

```text
(config)#
(config)# (config)# no mac-address-table interface gigabit-ethernet-1/1/1 limit maximum
```

**Impacts and precautions:**

This command clears all dynamically learned MAC entries on the configured interface, so a momentaneous data loss can occur. When used within the vlan mac-limit, the most restrictive rule will be considered.

**Hardware restrictions:**

N/A


### `mac-address-table vlan learning`

> **Página:** 383 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The mac-address-table vlan vlan-id learning command is used to disable MAC address learning for the specified VLAN.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
mac-address-table vlan vlan-id learning
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vlan vlan-id` — VLAN on which to limit MAC table entries. — *Valores:* { 1 to 4094 } · *Default:* None
- `learning` — Enable/disable dynamic MAC table entries learning on VLAN. — *Valores:* enabled | disabled · *Default:* enabled

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.6 | This command was introduced. |

**Usage Guidelines:**

Enabling the MAC address learning on VLAN 15 :

```text
(config)#
(config)# mac-address-table vlan 15 learning enabled
```

To disable MAC address learning:

```text
(config)#
(config)# mac-address-table vlan 15 learning disabled
```

**Impacts and precautions:**

This command clears all dynamically learned MAC entries on the configured VLAN. Be careful disabling MAC address learning when storm control unicast is configured on VLAN’s interfaces, it may occur a data loss due to DLF packet flood.

**Hardware restrictions:**

N/A


### `mac-address-table vlan limit`

> **Página:** 385 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The mac-address-table vlan vlan-id limit command is used to set the maximum MAC address table entries that can be learned for the specified VLAN.

**Supported Platforms:** This command is not supported in the following platforms: DM4270, DM4340, DM4380, DM4618, DM4770, DM4920.

**Syntax:**

```text
mac-address-table vlan vlan-id limit maximum entries
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vlan vlan-id` — VLAN on which to limit MAC table entries. — *Valores:* { 1 to 4094 } · *Default:* None
- `entries` — Maximum number of dynamic MAC table entries learned on VLAN. Value of 0 indicates that MAC address table entries will never be learned and traffic will be discarded. — *Valores:* 0 to 16000 0 to disable MAC address learning and data traffic · *Default:* N/|A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |
| 4.0 | Maximum value of parameter limit increased. |

**Usage Guidelines:**

Setting the maximum MAC address to 10 entries on VLAN 15 :

```text
(config)#
(config)# mac-address-table vlan 15 limit maximum 10
```

To disable MAC address limit:

```text
(config)#
(config)# (config)# no mac-address-table vlan 15 limit maximum
```

**Impacts and precautions:**

This command clears all dynamically learned MAC entries on the configured VLAN, so a momentaneous data loss can occur. When used within the interface mac-limit, the most restrictive rule will be considered.

**Hardware restrictions:**

N/A


### `show mac-address-table`

> **Página:** 388 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** The show mac-address-table command is used to display entries learned by the switch.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
show mac-address-table show mac-address-table [ [interface interface-name] | [mac-address address] | [vlan vlan-id] | [type entry-type] ]
```

**Parameters:**

- `None` — This parameter displays all entries learned by the switch. — *Valores:* N/A · *Default:* N/A
- `interface interface-name` — This parameter displays entries learned by the switch filtered by interface. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | two-hundred-g-ethernet-chassis/slot/port | four-hundred-g-ethernetchassis/slot/port | lag-id | service-port-id } · *Default:* N/A
- `mac-address address` — This parameter displays entries learned by the switch filtered by MAC address. — *Valores:* XX:XX:XX:XX:XX:XX · *Default:* N/A
- `vlan vlan-id` — This parameter displays entries learned by the switch filtered by vlan-id. — *Valores:* 1-4094 · *Default:* N/A
- `type entry-type` — This parameter displays entries learned by the switch filtered by entry type. — *Valores:* dynamic | static · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |
| 2.4 | Column chassis/slot removed from show. |
| 3.0 | Added support for 40G interfaces. |
| 4.6 | Added support for 100G interfaces. |
| 5.0 | Added support for 25G interfaces. |
| 12.0 | Added support for 200G and 400G interfaces. |

**Usage Guidelines:**

To show the entire table:

```text
# show mac-address-table
```

INTERFACE MAC ADDRESS VLAN TYPE ----------------------------------------------------------------------- gigabit-ethernet-1/1/1 a4:88:01:34:c8:a6 100 dynamic gigabit-ethernet-1/1/2 dc:71:48:42:f7:a4 102 dynamic gigabit-ethernet-1/1/3 4c:9b:94:26:08:9c 130 dynamic gigabit-ethernet-1/1/4 2c:77:29:26:fd:e2 100 dynamic gigabit-ethernet-1/1/5 50:8a:9f:15:46:78 104 dynamic ten-gigabit-ethernet-1/1/4 a0:8f:f7:16:8f:02 105 dynamic ten-gigabit-ethernet-1/1/5 e6:30:97:4a:4a:fc 160 dynamic Total MAC Addresses for this criterion: 7

**Output Terms:**

Output Description INTERFACE Interface identifier in the system. MAC ADDRESS MAC Address in hexadecimal presentation. VLAN VLAN identifier in the system. • dynamic: dynamic learn MAC address. TYPE • static: static MAC address entry inserted in MAC address table.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

Maximum number of entries that can be learned depends on hardware used. VLAN This topic describes the commands related to the management of 802.1Q Virtual Bridged LAN and to the management of VLAN extensions such as commands to configure Q-in-Q, dynamic VLANs and VLAN Translations.


## VLAN

### `dot1q vlan`

> **Página:** 392 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables configuration mode for a given VLAN or a range of VLANs

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
dot1q vlan vlan-id [ name vlan-name ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vlan vlan-id` — Single, range or list of VLAN IDs to be configured. — *Valores:* 1 - 4094 · *Default:* N/A
- `name vlan-name` — VLAN name. — *Valores:* 1 - 32 characters · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

When entering the VLAN configuration tree, the VLAN itself is created if it does not exist. VLANs can be created in ranges, or list. The following command will create VLANs from 10 to 20 and VLAN 30 and assing a name to all of them:

```text
(config)#dot1q vlan 10-20,30 name example
```

The following command will destroy the VLAN and its members:

```text
(config)# no dot1q vlan 1
```

**Impacts and precautions:**

VLANs must be created before being used by others features on their configurations.

**Hardware restrictions:**

N/A


### `dot1q vlan interface`

> **Página:** 394 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Adds an interface as a member of the configured VLAN.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
dot1q vlan vlan-id interface interface-name [ tag-mode ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vlan vlan-id` — ID of VLAN to be configured. — *Valores:* 1 - 4094 · *Default:* N/A
- `interface interface-name` — Interface name to be configured. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id | service-port-id } · *Default:* N/A
- `tag-mode` — Frames are forwarded with or without VLAN tag. The value tagged configures frames with tag by this VLAN interface. The value untagged configures frames without tag by this VLAN interface. — *Valores:* { tagged | untagged } · *Default:* tagged

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 4.6 | Added support to 40 Gigabit Ethernet and 100 Gigabit Ethernet. |
| 5.0 | Added support to 25 Gigabit Ethernet. |

**Usage Guidelines:**

The following command adds gigabit-ethernet 1/1/1 interface tagged in the VLAN 1:

```text
(config)# dot1q vlan 1 interface gigabit-ethernet-1/1/1
```

When adding an interface as a member of a VLAN, the default behaviour is to add it as tagged. Inside the interface configuration tree, the command untagged will change it.

**Impacts and precautions:**

Only pre-existing interfaces will be accepted when entering an interface name. Interfaces added as a member of a link aggregation group(LAG) cannot be added to VLAN membership. The LAG itself should be configured instead. Service-port interfaces cannot be added untagged to VLAN. All VLAN manipulations for this interface can be done by the service-port command itself.

**Hardware restrictions:**

N/A


### `show dot1q vlan`

> **Página:** 397 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to display VLAN information.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
show dot1q vlan [ [vlan id] [ brief | membership ] ] show vlan [ brief [vlan id] | membership [vlan id] [ brief | detail ] ]
```

**Parameters:**

- `brief` — Display VLAN brief information. — *Valores:* N/A · *Default:* N/A
- `membership` — Display VLAN membership information. — *Valores:* N/A · *Default:* N/A
- `detail` — Display membership detailed information. — *Valores:* N/A · *Default:* N/A
- `vlan id` — Display information of a specific VLAN. — *Valores:* 1-4094 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced Removed parameter detail. Added parameters status and port state. 4.2 Show vlan membership detail is now presented as table by default. show vlan command is deprecated, kept only for compatibility reasons, |
| 8.0 | being show dot1q vlan now the default. Reordered show output columns. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples shows how to use the show dot1q vlan commands.

```text
# show dot1q vlan
VLAN INTERFACE
```

ID NAME TYPE COUNT INTERFACE NAME STATUS PORT STATE --------------------------------------------------------------------------- 100 static 1 gigabit-ethernet-1/1/1 down forwarding 200 static 1 gigabit-ethernet-1/1/2 down forwarding

```text
# show dot1q vlan brief
VLAN INTERFACE
ID NAME TYPE COUNT
-------------------------------
100 static 1
200 static 1
# show dot1q vlan membership
VLAN
```

ID TYPE INTERFACE NAME STATUS PORT STATE ---------------------------------------------------------- 100 static gigabit-ethernet-1/1/1 down forwarding 200 static gigabit-ethernet-1/1/2 down forwarding

**Output Terms:**

Output Description VLAN ID VLAN identifier in the system. NAME Textual name of the VLAN. Type attribute describes how it was created. Static entries means TYPE that users have created it through configuration. INTERFACE COUNT Display the summarized information about VLAN members. INTERFACE NAME Interface identifier in the system. Operational state of the interface. The possible states are Up and STATUS Down. Port state of the interface for this vlan. Can be set by protocolos such PORT STATE as RSTP, EAPS and ERPS. The possible states are Disabled, Learning, Forwarding and Blocked.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `switchport acceptable-frame-types`

> **Página:** 401 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This configuration allows the interface to choose between tagged, untagged and all frames to be accepted. By default all frames either tagged with a IEEE 802.1Q header or not are accepted.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
switchport interface { interface-name } acceptable-frame-types { type-value }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Name of interface to set the acceptable frame type. — *Valores:* interface-type-chassis/slot/port | lag-id Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet. · *Default:* N/A
- `acceptable-frame-types type-value` — Configure acceptable frame types in the interface. — *Valores:* { all | tagged | untagged } · *Default:* all

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.2 | This command was introduced. |

**Usage Guidelines:**

The example below shows the configuration of acceptable-frame-types for a given interface.

```text
# config
Entering configuration mode terminal
(config)# switchport interface gigabit-ethernet-1/1/1
(config-switchport-gigabit-ethernet-1/1/1)# acceptable-frame-types tagged
(config-switchport-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

**Impacts and precautions:**

Only pre-existing interfaces will be accepted when entering an interface name. Interfaces added as a member of a link aggregation group(lag) cannot have acceptableframe-types configured. The lag itself should be configured instead.

**Hardware restrictions:**

N/A


### `switchport native-vlan`

> **Página:** 403 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Defines a native VLAN ID to be added in all untagged packets received in ingress mode in the given interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
switchport interface { interface-name } native-vlan vlan-id { native-vlan-id }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Name of interface to set the native-vlan. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id } · *Default:* N/A
- `vlan-id native-vlan-id` — VLAN ID to be added in incomming untagged packets in the interface. — *Valores:* 1 - 4094 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.8 | This command was introduced. |

**Usage Guidelines:**

To configure a native-vlan the interface must be either valid and untagged member of the VLAN ID being used for native vlan. The VLAN ID which will be added must exists. The example below shows the creation of a native-vlan for the given interface.

```text
# config
Entering configuration mode terminal
(config)# dot1q vlan 100
(config-vlan-100)# interface gigabit-ethernet-1/1/1
(config-dot1q-interface-gigabit-ethernet-1/1/1)# untagged
(config-vlan-100)# top
(config)# switchport interface gigabit-ethernet-1/1/1
(config-switchport-gigabit-ethernet-1/1/1)# native-vlan vlan-id 100
(config-switchport-interface-native-vlan)# commit
```

Commit complete.

**Impacts and precautions:**

Only pre-existing interfaces will be accepted when entering an interface name. Interfaces added as a member of a link aggregation group(lag) cannot have native vlan configured. The lag itself should be configured instead. VLANs to be added on the packets need to pre-exists, so configuration will be commited successfully. When an invalid interface or VLAN ID is used, the user is warned about the error during commit step.

**Hardware restrictions:**

N/A


### `switchport pcp`

> **Página:** 406 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Defines a 802.1p priority (PCP) to be added for untagged packets or for QinQ packets within the native VLAN-ID.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920, DM4780.

**Syntax:**

```text
switchport interface { interface-name } pcp { pcp-value }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Name of interface to set the pcp. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id } · *Default:* N/A
- `pcp pcp-value` — PCP to be added for incoming packets in the interface within the native VLAN-ID — *Valores:* 0 - 7 · *Default:* 0

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.6 | This command was introduced. |

**Usage Guidelines:**

The example below shows the configuration of a pcp for the given interface.

```text
# config
Entering configuration mode terminal
(config)# dot1q vlan 100
(config-vlan-100)# interface gigabit-ethernet-1/1/1
(config-dot1q-interface-gigabit-ethernet-1/1/1)# untagged
(config-vlan-100)# top
(config)# switchport interface gigabit-ethernet-1/1/1
(config-switchport-gigabit-ethernet-1/1/1)# native-vlan vlan-id 100
(config-switchport-interface-native-vlan)# exit
(config-switchport-gigabit-ethernet-1/1/1)# pcp 2
(config-switchport-interface-pcp)# commit
```

Commit complete.

**Impacts and precautions:**

Only pre-existing interfaces will be accepted when entering an interface name. Interfaces added as a member of a link aggregation group(lag) cannot have pcp configured. The lag itself should be configured instead. PCP configuration has no effect without native-vlan configuration.

**Hardware restrictions:**

N/A


### `switchport qinq`

> **Página:** 409 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables VLAN QinQ mode for the packets received on this interface. When enabled, the received packets will get an extra IEEE 802.1Q header, that is created using the native VLAN ID and default values for TPID (0x8100), priority code point(0) and drop eligible information (0). Usually this enclosing VLAN ID is usually refered as S-VLAN.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
switchport interface { interface-name } qinq
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Name of interface to set the QinQ. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id } · *Default:* N/A
- `qinq` — Enable QinQ in the interface. — *Valores:* N/A · *Default:* Disabled

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |

**Usage Guidelines:**

The interface must have a valid configuration for native VLAN. The example below shows the configuration of QinQ for a given interface and its pre-conditions.

```text
# config
Entering configuration mode terminal
(config)# dot1q vlan 50
(config-vlan-50)# interface gigabit-ethernet-1/1/1 untagged
(config-dot1q-interface-gigabit-ethernet-1/1/1)# top
(config)# switchport interface gigabit-ethernet-1/1/1
(config-switchport-gigabit-ethernet-1/1/1)# native-vlan vlan-id 50
(config-switchport-interface-native-vlan)# exit
(config-switchport-gigabit-ethernet-1/1/1)# qinq
(config-switchport-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

**Impacts and precautions:**

Only pre-existing interfaces will be accepted when entering an interface name. Interfaces added as a member of a link aggregation group(lag) cannot have qinq configured. The lag itself should be configured instead. VLANs to be added on the packets need to pre-exists, so configuration will be commited successfully. When an invalid interface or VLAN ID is used, the user is warned about the error during commit step.

**Hardware restrictions:**

N/A


### `switchport tpid`

> **Página:** 412 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures tag protocol identifier(TPID) accepted for VLAN tagged frames. Only frames received with the configured TPID are considered as tagged frames. Also, tagged frames sent by the configured interface will have the configured TPID.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
switchport interface { interface-name } tpid { tpid-value }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Name of interface to set the TPID. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | lag-id } · *Default:* N/A
- `tpid tpid-value` — Configure TPID in the interface. — *Valores:* { 0x8100 | 0x88a8 | 0x9100 } · *Default:* 0x8100

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |

**Usage Guidelines:**

The example below shows the configuration of TPID for a given interface.

```text
# config
Entering configuration mode terminal
(config)# switchport interface gigabit-ethernet-1/1/1
(config-switchport-gigabit-ethernet-1/1/1)# tpid 0x88a8
(config-switchport-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

**Impacts and precautions:**

Only pre-existing interfaces will be accepted when entering an interface name. Interfaces added as a member of a link aggregation group(lag) cannot have TPID configured. The lag itself should be configured instead. When an invalid interface is used, the user is warned about the error during commit step.

**Hardware restrictions:**

N/A


### `vlan-mapping`

> **Página:** 414 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create or update VLAN mapping rules to add or replace a VLAN tags when match criteria is met.

**Supported Platforms:** This command is not supported in the following platforms: DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
vlan-mapping interface { interface-name } { stage } rule { rule-name } match vlan vlan-id { vlan-id-match } action { add | replace } vlan vlan-id { vlan-id-action } [pcp { pcp } ] [ inner-action replace inner-vlan vlan-id { vlan-id-action } [pcp { pcp } ] ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Name of interface to install the rule. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | two-hundred-g-ethernet-chassis/slot/port | four-hundred-g-ethernetchassis/slot/port | lag-id } · *Default:* N/A
- `stage` — Specify the stage the VLAN-mapping rule refers to (ingress or egress data). — *Valores:* ingress | egress · *Default:* N/A
- `rule rule-name` — Name of the rule being created/updated. Only accepts alphanumeric characters and ‘_’, ‘+’ and ‘-’. — *Valores:* String with maximum 48 characters · *Default:* N/A
- `match` — Parameters after match and before action describe the type of flow selected to be modified. — *Valores:* N/A · *Default:* N/A
- `vlan vlan-id vlan-id-match` — Single, range or list of VLAN ID that will be matched. — *Valores:* 1 - 4094 · *Default:* N/A
- `action { add | replace }` — Selects the action to be applied to the outer VLAN. replace will replace the outer VLAN tag of packets that meet match criteria. add will add a new outer VLAN tag to packets that meet match criteria. The action is only available after the match is configured. — *Valores:* add | replace · *Default:* N/A
- `inner-action replace` — Selects the action to be applied to the inner VLAN. replace will replace the inner VLAN tag of packets that meet match criteria. When the action is add (for the outer VLAN), then the new added VLAN is considered the outer VLAN, and the inner-action will act over the previous outer VLAN tag. The inner-action is only available after the action is configured. The combination of action add and inner-action replace is only valid when switchport qinq is enabled for the interface. The combination of action replace and inner-action replace is only valid when switchport qinq is disabled for the interface. — *Valores:* replace · *Default:* N/A
- `vlan vlan-id vlan-id-action` — VLAN ID that will be added or replaced into the outer VLAN tag of the packet. — *Valores:* 1 - 4094 · *Default:* N/A
- `inner-vlan vlan-id vlan-id-action` — VLAN ID that will be replaced into the inner VLAN tag of the packet. The value copy may be configured, and it will keep the current VLAN ID in the inner VLAN tag. — *Valores:* 1 - 4094 | copy · *Default:* N/A
- `pcp pcp` — VLAN PCP (802.1p) field value that will be added into packet for outer or inner VLAN tag. It can be the numeric priority value or the copy from the PCP value from the existing VLAN tag. — *Valores:* 0-7 | copy · *Default:* 0

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |
| 4.6 | Added pcp action. Added support for 100G interfaces. |
| 4.8 | Added inner-action. |
| 5.0 | Added support for 25G interfaces. Remove restriction of using action add without QinQ enabled for DM4270, 5.10 DM4770 and DM4380 series. |

**Usage Guidelines:**

To configure a VLAN mapping rule the interface must be a valid one. Also, the VLAN that will replace the original one in the VLAN tag must exist. The example below shows the creation of a rule with replace action.

```text
# config
(config)# dot1q vlan 100
(config-vlan-100)# interface gigabit-ethernet-1/1/1
(config-interface-gigabit-ethernet-1/1/1)# top
(config)# vlan-mapping interface gigabit-ethernet-1/1/1 ingress rule RULE1
(config-rule-RULE1)# match vlan vlan-id 1 action replace vlan vlan-id 100
(config-rule-RULE1)# commit
```

Commit complete.

```text
(config-rule-RULE1)# end
#
```

**Impacts and precautions:**

Only pre-existing interfaces will be accepted when entering an interface name. Interfaces added as members of a link aggregation group (LAG) cannot be added to vlan-mapping rules. The LAG itself should be configured instead. VLANs to be added on the packets need to pre-exist, so configuration will be commited successfully.

**Hardware restrictions:**

DM4611, DM4612 and DM4616 series do not support VLAN Mapping. DM4050 and DM4250 series do not support PCP copy on ingress rules. DM4050 and DM4250 series do not support inner-action. On DM4270, DM4770 and DM4380 series, VLAN mapping rules do not act over packets modified by ACL. On DM4270, DM4770 and DM4380 series, VLANs associated with L3 interfaces cannot be used for ingress VLAN Mapping rules when there is no QinQ enabled, except when both the match and action VLANs are the same. On DM4270, DM4770 and DM4380 series, VLAN mapping rules with action add do not act over double-tagged packets when the ingress interface has QinQ disabled. On DM4340 series, only ingress rule needs to be created as ingress and egress rules are symmetric, so, the egress rule is not shown in the CLI. On DM4340 series, the PCP value of the new tag is copied from existing VLAN tag. Therefore, the PCP parameter isn’t available in the CLI. On DM4780 series, PCP replace options in VLAN translate ingress rules and PCP copy configurations in VLAN translate egress rules are not available. LINK AGGREGATION This topic describes the commands related to management of interface aggregations such as commands to configure static and dynamic aggregations.


## Link Aggregation

### `clear lacp`

> **Página:** 419 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** The clear lacp command is used to reset statistics about Link Aggregation Control Protocol (LACP).

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
clear lacp statistics {all | lag id id }
```

**Parameters:**

- `all` — Reset statistics for all link-aggregations. — *Valores:* N/A · *Default:* N/A
- `lag id id` — Reset statistics for a specific link-aggregation. The actual maximum number of link-aggregations depends on the product model. — *Valores:* 1-32 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.12 | This command was introduced |
| 2.4 | Number of LAG-IDs increased to eight |

**Usage Guidelines:**

To clear all LAGs statistics:

```text
# clear lacp statistics all
```

To clear a single LAG statistics:

```text
# clear lacp statistics lag id 1
```

**Impacts and precautions:**

It is only possible to clear statistics for link-aggregations controlled by LACP, i.e., link-aggregations configured in active or passive modes.

**Hardware restrictions:**

N/A


### `link-aggregation`

> **Página:** 421 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Link aggregation bundles individual ethernet links into a single logical link. It may be used for redundancy or to expand bandwidth capacity. It is controlled by Link Aggregation Control Protocol (LACP).

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
link-aggregation [system-priority priority] link-aggregation [load-balance hash-function hash] link-aggregation interface lag lag-id [administrative-status status] [load-balance type] [maximum-active links] [minimum-active links] [mode lacp-mode] [period period-interval] interface interface-name [port-priority priority] link-aggregation interface lag lag-id mc-lag [rg-id redundancy-group-id] [lag-priority priority] [min-links links]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `system-priority priority` — Sets the priority of the LACP system. — *Valores:* 0-65535 · *Default:* 32768
- `load-balance hash-function hash` — Sets the global load balance hash function for enhanced and dynamic mode. — *Valores:* { crc16xor8 | crc16xor4 | crc16xor2 | crc16xor1 | crc16 | xor16 | crc16ccitt | crc32lo | crc32hi | crc32ethlo | crc32ethhi | crc32koopmanlo | crc32koopmanhi } · *Default:* crc16xor8
- `interface lag lag-id` — Creates a Link Aggregation Group with a specific identifier. The actual maximum number of link-aggregations depends on the product model. — *Valores:* 1-32 · *Default:* N/A
- `administrative-status status` — Sets the administrative status of the LAG interface. — *Valores:* { down | up } · *Default:* up
- `load-balance type` — Sets the load balancing algorithm to apply to traffic forwarded on this LAG interface. The dynamic balance type provides an evenly load distribution across the LAG members. By taking into account the instant values for the load of the LAG members, flows are dynamically moved from links with lower loads. Other types are hash-based, where the packet order is always maintained. However, as the output interface is selected according to the traffic (using an XOR of packet fields), bandwidth usage might not be uniform among the LAG members. Eventually, some LAG members present heavy loading while others are underused. — *Valores:* { dst-ip | dst-mac | dynamic | enhanced | src-dst-ip | src-dst-mac | src-ip | src-mac } · *Default:* enhanced
- `maximum-active links` — Sets the maximum number of links allowed to be simultaneously active on this LAG interface. If more interfaces are configured than the maximum-active links, the exceeding interfaces with higher port-priority will remain inactive. The maximum value for this parameter may be lower depending on the product model. The default value for this parameter is equal to the maximum value, which may be lower depending on the product model. — *Valores:* 1-16 · *Default:* 16
- `minimum-active links` — Sets the minimum number of links required to bring up this LAG interface. If less interfaces are active than the minimum-active links, the LAG interface itself will be considered inactive. The maximum value for this parameter may be lower depending on the product model. — *Valores:* 1-16 · *Default:* 1
- `mode lacp-mode` — Sets the mode of LACP operation for this LAG. If set to Static, LACP is disabled. If set to Passive, the remote node must be set to Active. — *Valores:* { static | active | passive } · *Default:* static
- `period period-interval` — Sets the interval period of LACP for this LAG, short ( 1s ) or long ( 30s ). Short option allows a faster link detection/recovery. Preferably both nodes must be set with the same value. — *Valores:* { short | long } · *Default:* long
- `description` — Sets a textual description of the interface, according to the network manager’s choice. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A
- `interface interface-name` — Interface to be added to LAG. Each interface may appear in only one LAG at time. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | two-hundred-g-ethernet-chassis/slot/port | four-hundred-g-ethernetchassis/slot/port } · *Default:* N/A
- `port-priority priority` — Sets a port priority for a LAG member. — *Valores:* 0-65535 · *Default:* 32768
- `mc-lag rg-id redundancy-group-id` — Sets the MC-LAG redundancy group (if any) to associate with the LAG interface. The actual maximum number of redundancy group IDs depends on the product model. — *Valores:* 1-8 · *Default:* N/A
- `lag-priority priority` — Sets the priority of this LAG interface when associated to a Redundancy Group. — *Valores:* 5-32000 · *Default:* 1000
- `min-links links` — Sets the minimum number of links required to consider a LAG interface as active. — *Valores:* 1-8 · *Default:* 1

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced |
| 1.12 | Implemented support to LACP |
| 2.4 | Added description parameter and number of LAG-IDs increased to eight |
| 3.0 | Added support for 40G interfaces |
| 4.5 | Added maximum-active and minimum-active parameters |
| 4.6 | Added support for 100G interfaces |
| 4.9 | Added support for load-balance command |
| 5.0 | Added support for 25G interfaces |
| 5.10 | Added support for load-balance hash-function command |
| 9.0 | Added support for some special characters on LAG description. |
| 9.2 | Added support for MC-LAG feature |

**Usage Guidelines:**

Commands for configuring the link-aggregation. Example: This example shows how to configure a simple static link-aggregation.

```text
# config terminal
Entering configuration mode terminal
(config)# link-aggregation interface lag 1
(config-la-if-lag-1)# interface gigabit-ethernet-1/1/1
(config-la-if-gigabit-ethernet-1/1/1)#
```

Regarding to LAG description, special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example: DM4270(config)# link-aggregation interface lag 1 DM4270(config-la-if-lag-1)# description "test_interface_name|!?;" Commands for configuring MC-LAG for a single LAG interface. Example: This example shows how to assign a previously created redundancy group to a LAG interface.

```text
(config)# link-aggregation interface lag 1
(config-la-if-lag-1)# mc-lag rg-id 1
(config-la-if-lag-1)# mc-lag lag-priority 2500
(config-la-if-lag-1)# mc-lag min-links 1
(config-la-if-lag-1)#
```

**Impacts and precautions:**

Each interface may appear in only one LAG at time. Only interfaces with the same nominal speed can be aggregated together. Interfaces with half-duplex configuration cannot be members of a LAG. Each LAG must contain at least one and no more than eight aggregatable interfaces. If the LAG interface has more physical interfaces than the configured maximum-active parameter, in static mode the interfaces with higher value at port-priority parameter will be maintained inactive as standby. In active or passive modes the interface selection criteria follows the following path of comparisons: System Priority -> System MAC -> Port Priority -> Port ID. In priority comparisons, numerically lower values have higher priority. This means that the interfaces of the equipment with lower System Priority will be used for standby selection, according to its Port Priority and Port ID. If System Priority is the same on both equipment, the equipment with lower System MAC will use its interfaces to decide standby selection, according to its Port Priority and Port ID. Maximum-links and minimum-links are independent configuration options. They can be used in any mode of operation (static, active or passive). A valid redundancy group must be created first, before associating LAG interfaces to it. The active device on the MC-LAG bundle will be the one with higher LAG priority (numerically lower).

**Hardware restrictions:**

When load-balance enhanced is used, the platform DM4050 only supports non-unicast (broadcast, multicast and unknown unicast) load-balance based on source and destination MAC addresses. Other load-balance criterias like source and destination IP and TCP/UDP ports are not available. Load-balance is not supported in the following platform: DM4618 Load-balance dynamic is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4050, DM4250, DM4360, DM4370, DM4376 and DM4378. Load-balance hash-function parameter is not supported in the DM4050 and DM4618 platforms.


### `link-aggregation mc-lag redundancy-group`

> **Página:** 429 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** A redundancy group is the collection of devices that provide protection for a bundle, forming the MC-LAG. A redundancy group is identified by an unique redundancy-groupid.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
link-aggregation mc-lag redundancy-group rg-id [system-mac-address address] [system-priority priority] [wait-time time] link-aggregation mc-lag redundancy-group rg-id local-member local-id id [local-port port] link-aggregation mc-lag redundancy-group rg-id remote-member remote-id id ip ipv4-address [remote-port port]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mc-lag redundancy-group redundancy-group-id` — ID of the redundancy group to be configured. The actual maximum number of redundancy group IDs depends on the product model. — *Valores:* 1 - 32 · *Default:* N/A
- `system-mac-address system-mac-address-value` — Sets an unicast system MAC address for this device in the redundancy group. — *Valores:* xx:xx:xx:xx:xx:xx · *Default:* 00:04:df:00:00:00
- `system-priority priority` — Sets the system priority for this device in the redundancy group. — *Valores:* 0 - 65535 · *Default:* 32768
- `wait-time time` — Sets the time to wait after activation before assuming that another redundancy group member is down. — *Valores:* 0 - 65535 (seconds) · *Default:* 30 (seconds)
- `local-member local-id id` — Sets the ID for this device in the redundancy group. — *Valores:* 1 - 8 · *Default:* N/A
- `local-member local-port port` — Sets the local member TCP port. — *Valores:* 1024 - 32767 · *Default:* 30012
- `remote-member remote-id id` — Sets the ID for the remote (partner) device in the redundancy group. — *Valores:* 1-8 · *Default:* N/A
- `remote-member ip ipv4-address` — Sets the remote member IPv4 address. — *Valores:* a.b.c.d · *Default:* N/A
- `remote-member remote-port port` — Sets the remote member TCP port. — *Valores:* 1024 - 32767 · *Default:* 30012

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.2 | This command was introduced |

**Usage Guidelines:**

Commands to configure the link-aggregation. Example: This example shows how to configure a redundancy-group for a MC-LAG bundle.

```text
# config terminal
Entering configuration mode terminal
(config)# link-aggregation mc-lag redundancy-group 1
(config-redundancy-group-1)# local-member local-id 1 local-port 1500
(config-redundancy-group-1)# remote-member ip 192.0.2.0
(config-redundancy-group-1)# remote-member remote-port 1500
(config-redundancy-group-1)# remote-member remote-id 2
(config-redundancy-group-1)# system-mac-address d8:fe:d9:29:34:c1
(config-redundancy-group-1)# system-priority 10000
(config-redundancy-group-1)# wait-time 15
```

**Impacts and precautions:**

The local member ID must match the remote member ID configured on the other equipment in the redundancy group. For the same equipment, it is advised that both IDs be different. In addition, do not configure the same ports for already existing services. It is recommended to set a different system priority value for each member PE in the RG in order to avoid a “split-brain” scenario, i.e., when the communication link between them is down. The downside of using this approach is that the switchover may take longer whenever the active PE goes down. This is due to the system ID used by the redundancy group may change, in this case.

**Hardware restrictions:**

N/A


### `show link-aggregation`

> **Página:** 433 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to display link-aggregation information.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
show link-aggregation [ brief | interfaces | mc-lag | lacp [ brief | statistics | extensive ] ]
```

**Parameters:**

- `brief` — Display brief information about link-aggregations. — *Valores:* N/A · *Default:* N/A
- `interfaces` — Display information about members of link-aggregations. — *Valores:* N/A · *Default:* N/A
- `mc-lag` — Display MC-LAG-related status information on LAG interfaces and redundancy groups. — *Valores:* N/A · *Default:* N/A
- `lacp` — Display information about dynamic aggregations controlled by Link Aggregation Control Protocol (LACP). — *Valores:* N/A · *Default:* N/A
- `extensive` — Display detailed information about link-aggregations. — *Valores:* N/A · *Default:* N/A
- `statistics` — Display information about PDU exchange in dynamic aggregations controlled by Link Aggregation Control Protocol (LACP). — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced |
| 1.12 | The LACP parameter was introduced |
| 4.6 | New aggregation states added |
| 9.2 | Added support for MC-LAG feature |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples shows how to use the show link-aggregation commands.

```text
# show link-aggregation brief
```

State codes: down - no link up; up - at least 1 member up; MC-LAG standby - inactive due to MC-LAG standby role; LAG SNMP ID State Mode ifIndex Description ----------------------------------------- 1 up static 83886081 - 3 down static 83886083 -

```text
# show link-aggregation interfaces
```

Aggregation Status: active - member is aggregated; inactive - member is not aggregated; LACP Status: active - the link is selected in a bundle. inactive - the link is not selected in a bundle. bundle failed - LACP failed to add the link to the bundle. standby - the link is selected as standby. incompatible - the link properties are not compatible with other links in the bundle. too few links - the number of active links is less than minimum active links. disabled - the LACP signalling is disabled for the link. no partner info - the link has not received information from its LACP protocol partner. partner indiv - the LACP protocol partner has indicated that the link is individual. max lt min - the maximum number of links allowed is less than the minimum number of links. different lag id - the Link Aggregation Group ID is different to that of the highest priority link. connected - this interface is connected to another interface that is also configured in the bundle. LAG Oper Aggregation LACP ID Interface Name Status Status Status ---------------------------------------------------------------- 1 ten-gigabit-ethernet-1/1/5 up active active ten-gigabit-ethernet-1/1/6 up active active 3 ten-gigabit-ethernet-1/1/8 down inactive inactive

```text
# show link-aggregation mc-lag
```

MC-LAG Role: not selected - the bundle is not MC-LAG enabled, or is not operational; active - this device is the primary switch for the MC-LAG bundle; standby - this device is a standby switch for the MC-LAG bundle; MC-LAG Role Reason: not selected - the bundle is not MC-LAG enabled or has not yet selected its MC-LAG role for the bundle; local best - this device has the best priority for the bundle of all RG members; remote best - a remote device has a better priority than the local device for the bundle; startup - this device has been selected as standby for the bundle because it has not synced yet; deact - this device has been selected as standby for the bundle because the bundle is deactivating; MC-LAG LAG RG MC-LAG Role ID ID Role Reason ----------------------------- 1 1 active local best Redundancy Group Sync Status: down - the connection to the member is down; connected - the connection is up, but synchronization is not yet complete; synchronized - the connection is up and synchronization of system information is complete; sync failed - synchronization has failed due to inconsistent system configuration; Local Remote RG System MAC Member Member Sync ID Address ID ID Status ----------------------------------------------- 1 00:04:df:00:00:00 1 2 synchronized

**Output Terms:**

Output Description LAG ID Identifier of link-aggregation instance in the system. LAG operational state. ‘Up’ means that at least 1 interface member has link status up. ‘Down’ means no member has active link. ‘MCState LAG standby’ means that the LAG is in a ‘standby’ mode since the device assumed the MC-LAG ‘standby’ role for this LAG. Indicates the operation mode for a LAG, three options are available: • static - LAG is configured statically by user; Mode • active - LAG is controlled by LACP in active mode; • passive - LAG is controlled by LACP in passive mode. SNMP ifIndex Indicates the ifIndex used for SNMP requests for the LAG interface. Description Indicates the textual description set for the LAG interface. Output Description Indicates the MC-LAG Redundancy Group ID (if any) associated with RG ID the LAG interface. Indicates the MC-LAG Role. The possibles values are: • not selected - the bundle is not MC-LAG enabled, or is not operational; MC-LAG Role • active - this device is the primary switch for the MC-LAG bundle; • standby - this device is a standby switch for the MC-LAG bundle. Indicates the MC-LAG Role Reason. The possibles values are: • not selected - the bundle is not MC-LAG enabled or has not yet selected its MC-LAG role for the bundle; • local best - this device has the best priority for the bundle of all RG members; MC-LAG Role Reason • remote best - a remote device has a better priority than the local device for the bundle; • startup - this device has been selected as standby for the bundle because it has not synced yet; • deact - this device has been selected as standby for the bundle because the bundle is deactivating. Interface Name Indicates the name of the LAG member interface Oper Status Indicates the operational status of the LAG member interface Indicates whether this LAG member is active in the LAG. The possibles values are: Aggregation Status • active - the member is selected for aggregation. • inactive - the member is not aggregated in the LAG. Output Description Indicates the LACP status for the LAG member. The possibles values are: • active - the link is selected in a bundle. • inactive - the link is not selected in a bundle, and none of the more specific aggregation status values apply. • bundle failed - LACP failed to add the link to the bundle. • standby - the link is selected as standby. • incompatible - the link cannot be aggregated because the link properties are not compatible with other links in the bundle. • too few links - the number of active links in the bundle is less than minimum active links. • disabled - the link cannot be aggregated because LACP signalling is disabled for the link, and another link in the bundle has LACP signalling enabled. LACP Status • no partner info - the link cannot be aggregated because it has not received information from its LACP protocol partner. • partner indiv - the link cannot be aggregated because its LACP protocol partner has indicated that the link is individual. • max lt min - the link cannot be aggregated because the maximum number of links allowed in the bundle is less than the minimum number of links. • different lag id - the link cannot be aggregated because its Link Aggregation Group ID is different to that of the highest priority link in the bundle. • connected - the link cannot be aggregated because this interface is connected to another interface that is also configured in the bundle. Output Description Indicates the PDUs rate requested by protocol: • slow - PDUs sent at long intervals of 30 seconds; Rate • fast - PDUs sent at short intervals of 1 second. Port Prio Indicates the configured priority for this interface. Port ID Indicates the port identifier in the system. Key Indicates the link-aggregation key used by LACP to establish LAGs. System Prio Indicates the system priority used by LACP. LACPDUs Indicates the number of sent or received PDUs in an interface. Sent/Received Pkt Errors Indicates the number of invalid PDUs received in an interface. Indicates the elapse time (in seconds) since the statistics of this inCleared terface were cleared. System MAC Address Indicates the system MAC address for the device in the Redundancy Group. Indicates the local member ID for the device in the Redundancy Local Member ID Group. Indicates the ID for the remote (partner) device in the Redundancy Remote Member ID Group. Indicates the synchronization status of the remote PE about the ReSync Status dundancy Group.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A SPANNING-TREE This topic describes the commands related to management of Spanning-Tree topologies such as commands to configure the spanning-tree mode, to change the path cost or to inspect the interface roles.


## Spanning-Tree

### `show spanning-tree`

> **Página:** 441 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to display spanning-tree information.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show spanning-tree [ brief | detail | extensive ]
```

**Parameters:**

- `brief` — Display spanning tree brief information. — *Valores:* N/A · *Default:* N/A
- `detail` — Display spanning tree detailed information. — *Valores:* N/A · *Default:* N/A
- `extensive` — Display spanning tree extensive information. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples shows how to use the show spanning-tree command.

```text
# show spanning-tree
```

Spanning tree enabled protocol rstp Root ID Priority: 32768; Address: 00:00:00:00:00:00; Cost: 0; Port: global; Hello Time: 2sec; Max Age: 20sec; Forward Delay: 15sec; Bridge ID Priority: 32768; Address: n/a; Hello Time: 2sec; Max Age: 20sec; Forward Delay: 15sec; Designated Interface Port Prio Cost Sts Cost Bridge ID Port --------- ---- ---- ---- --- ---- ----------------------- ---- gigabit-ethernet-1/1/1 0 128 100 DIS 0 0 00:00:00:00:00:00 0

```text
# show spanning-tree brief
```

Spanning tree enabled protocol rstp Root ID Priority: 32768; Address: 00:00:00:00:00:00; Cost: 0; Port: global; Hello Time: 2sec; Max Age: 20sec; Forward Delay: 15sec; Bridge ID Priority: 32768; Address: n/a; Hello Time: 2sec; Max Age: 20sec; Forward Delay: 15sec; Designated Interface Port Prio Cost Sts Cost Bridge ID Port --------- ---- ---- ---- --- ---- ----------------------- ---- gigabit-ethernet-1/1/1 0 128 100 DIS 0 0 00:00:00:00:00:00 0

```text
# show spanning-tree detail
```

Spanning tree enabled protocol: rstp Bridge Identifier has priority: 32768; address: n/a; Configured: hello time: 2sec; max age: 20sec; forward delay: 15sec; Topology flag not set; Number of topology changes 0,last change occurred 0 seconds ago; Times: hold: 6; hello: 2; max age: 20; forward delay: 15; Port 0 (gigabit-ethernet-1/1/1) is discarding Path cost: 100; Priority: 128; Designated root: priority: 0; address: 00:00:00:00:00:00; Designated bridge: priority: 0; address: 00:00:00:00:00:00; Designated port: 0; designated path cost: 0; Number of transitions to forwarding state: 0;

```text
# show spanning-tree extensive
```

Spanning tree enabled protocol: rstp Administrative state: up; Operational state: failed; Bridge Identifier has priority: 32768; address: n/a; Configured: hello time: 2sec; max age: 20sec; forward delay: 15sec; Topology flag not set; Number of topology changes 0,last change occurred 0 seconds ago; Times: hold: 6; hello: 2; max age: 20; forward delay: 15; Port 0 (gigabit-ethernet-1/1/1) is discarding Operational state: down; Forwarding state: discarding; Role: disabled; Path cost: 100; Priority: 128; P2p: no; Edge: no; Up-time: 0; Disputed: false; Designated root: priority: 0; address: 00:00:00:00:00:00; Designated bridge: priority: 0; address: 00:00:00:00:00:00; Designated port: 0; designated path cost: 0; Number of transitions to forwarding state: 0;

**Output Terms:**

Output Description Priority Spanning tree priority of the STP instance. Address Mac address of STP instance. Cost (Root ID) The cost configured for a port from Root. Port (Root ID) Display the port id from Root. Hello Time Time interval that the root bridge will generate BPDUs. The maximum length of time that passes before a bridge port saves Max Age its configuration BPDU information. Time interval that interfaces of all bridges should wait to change Forward Delay from its listening and learning states to forwarding state. Interface Spanning tree interface name. Port Display port number. Prio Display the port priority. Cost The path cost configured for a port. Sts Port state from STP instance. Cost Designated path cost configured for a port. Bridge ID Designated Bridge ID used for sending and receiving STP BPDUs. Port Designated Port from STP instance.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `spanning-tree`

> **Página:** 445 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The Spanning Tree Protocol (STP) is a network protocol that prevents loops from occurring in the network topology. Spanning tree also allows a network design to include redundant links to provide automatic backup paths.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
spanning-tree [bridge-priority priority] [forward-delay seconds] [hello-time seconds] [maximum age seconds] [mode version] [name identifier] [revision number] [transmit hold-count number] [maximum {[age number] [hops number] } ] interface name { [cost number] [port-priority number] [link-type type] [restricted-role] [restricted-tcn] [{edge-port | auto-edge}] [bpdu-guard] }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `bridge-priority priority` — The bridge priority for this instance. When using the MSTP mode, this parameter is used as the CIST bridge priority. — *Valores:* 0-61440 · *Default:* 32768
- `forward-delay seconds` — Used by root to set the number in seconds, that interfaces of all bridges should wait to change from its listening and learning states to forwarding state. — *Valores:* 4-30 · *Default:* 15
- `hello-time seconds` — Value that all bridges will use for the hello time if this bridge is acting as root. — *Valores:* 1-10 · *Default:* 2
- `maximum age seconds` — Value that all bridges will use for the max age of BPDUs if this bridge is acting as root. — *Valores:* 6-40 · *Default:* 20
- `mode version` — Spanning Tree Protocol version selection. — *Valores:* rstp, mstp · *Default:* rstp
- `name identifier` — The Configuration Name part of the STP Configuration Identifier. — *Valores:* Name - maximum 32 characters · *Default:* N/A
- `revision number` — The Configuration Revision level part of the MSTP Configuration Identifier. Only available when mode is MSTP. — *Valores:* 0-65535 · *Default:* 0
- `transmit hold-count number` — The value used by port to limit the maximum BPDU transmission rate. — *Valores:* 1-10 · *Default:* 6
- `maximum age number` — Value that all bridges will use for the max age of BPDUs if this bridge is acting as root. — *Valores:* 6-40 · *Default:* 20
- `maximum hops number` — The maximum number of hops across an MST region. Only available when mode is MSTP. — *Valores:* 6-40 · *Default:* 20
- `interface name` — Interface name to be configured. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | two-hundred-g-ethernet-chassis/slot/port | four-hundred-g-ethernetchassis/slot/port | lag-id } · *Default:* N/A
- `cost number` — Path cost configuration for the port. — *Valores:* 1-200000000 · *Default:* 20000
- `port-priority number` — Priority configuration for the port. — *Valores:* 0-240 · *Default:* 128
- `link-type type` — Link type configuration for the port. — *Valores:* auto, not-point-to-point, point-to-point · *Default:* auto
- `restricted-role` — Restricted role configuration for the port. Also known as root guard. When enable for an interface that would be choosen as root port, this interface will be blocked instead. — *Valores:* N/A · *Default:* N/A
- `restricted-tcn` — Restricts the propagation of topology changes for the port. Topology change notifications received on the interface are not propagated to other interfaces. — *Valores:* N/A · *Default:* N/A
- `edge-port` — Administrative edge port configuration for the port. When configured, auto-edge configuration is ignored. — *Valores:* N/A · *Default:* N/A
- `auto-edge` — Automatic edge port detection on this port. — *Valores:* N/A · *Default:* N/A
- `bpdu-guard` — Enables bpdu-guard for the port. When enable, if an edge port receives a BPDU, the port role is set to disable and port state is set to discarding. Bpdu-guard parameter only can be set if edge-port is also set. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced |
| 1.12 | Spanning-tree supports configuration in link-aggregations. |
| 3.0 | Added support for 40G interfaces. |
| 4.6 | Added support for 100G interfaces. Added support for MSTP mode. Added parameters restricted-role, 4.8 restricted-tcn and bpdu-guard. |
| 5.0 | Added support for 25G interfaces. The cist-bridge-priority parameter was deprecated and unified with the 5.2 bridge-priority parameter. |

**Usage Guidelines:**

Commands for configure the spanning-tree. Example: This example shows how to configure the spanning-tree protocol.

```text
# config terminal
Entering configuration mode terminal
(config)# spanning-tree forward-delay 20
(config)# spanning-tree hello-time 5
(config)# spanning-tree transmit hold-count 10
(config-spanning-tree)# spanning-tree interface gigabit-ethernet 1/1/1
(config-stp-interface-gigabit-ethernet-1/1/1)# cost 2000
(config-stp-interface-gigabit-ethernet-1/1/1)# port-priority 100
(config-stp-interface-gigabit-ethernet-1/1/1)# link-type auto
(config-stp-interface-gigabit-ethernet-1/1/1)# edge-port
```

**Impacts and precautions:**

The maximum age timer controls the maximum length of time that passes before a bridge port saves its configuration BPDU information. The switch that is at the periphery of the network does not time out the root information under stable conditions. So, the maximum age requires the coherence (2x(hello-time) <= age <= 2x(forward-delay - 1)).

**Hardware restrictions:**

N/A


### `spanning-tree mst`

> **Página:** 451 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Spanning-tree mst allows multiples instances of spanning-tree, according to IEEE 802.1Q, 2011. This command is only available when spanning-tree mode is set to mstp.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
spanning-tree mst id [priority priority] [vlan vlans] [interface name [cost number] [port-priority number]]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mst id` — The id of this MST instance. — *Valores:* 1-64 · *Default:* N/A
- `priority priority` — The bridge priority for this MST instance. — *Valores:* 0-61440 · *Default:* 32768
- `vlan vlans` — Sets the list of protected VLANs of this MST instance. Ranges of VLANs or single VLAN are allowed and can be combined to specify the set of protected VLANs — *Valores:* 1-4094 Example: protected-vlans 1-3,5,7-9 · *Default:* None
- `interface name` — Interface name to be configured in this MST instance. The interface must also be configured in the CIST instance. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | two-hundred-g-ethernet-chassis/slot/port | four-hundred-g-ethernetchassis/slot/port | lag-id } · *Default:* N/A
- `cost number` — Path cost configuration for the port in this MST instance. — *Valores:* 1-200000000 · *Default:* 20000
- `port-priority number` — Priority configuration for the port in this MST instance. — *Valores:* 0-240 · *Default:* 128

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced |
| 5.0 | Add support for 25G interfaces |

**Usage Guidelines:**

Commands for configure the spanning-tree. Example: This example shows how to configure a spanning-tree instance.

```text
# config terminal
Entering configuration mode terminal
(config)# spanning-tree mode mstp
(config-spanning-tree)# interface gigabit-ethernet-1/1/1
(config-stp-gigabit-ethernet-1/1/1)# port-priority 240
(config-stp-gigabit-ethernet-1/1/1)# cost 2000
(config-stp-gigabit-ethernet-1/1/1)# exit
(config-spanning-tree)# interface gigabit-ethernet-1/1/2
(config-stp-gigabit-ethernet-1/1/2)# cost 2000
(config-stp-gigabit-ethernet-1/1/2)# port-priority 240
(config-stp-gigabit-ethernet-1/1/2)# exit
(config-spanning-tree)# spanning-tree mst 1
(config-stp-mst1)# priority 1
(config-stp-mst1)# interface gigabit-ethernet-1/1/1
(config-stp-mst-gigabit-ethernet-1/1/1)# port-priority 16
(config-stp-mst-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A ERPS This topic describes the commands related to management of G.8032 ERPS topologies such as commands to configure the RPL or to inspect the protection status.


## ERPS

### `erps ring`

> **Página:** 454 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The current implementation follows ERPS version 2 specification, as described in ITU-T G.8032.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
erps ring ring-name erps ring ring-name ring-id id erps ring ring-name control-vlan vlan-id erps ring ring-name protected-vlans vlans erps ring ring-name r-aps-level level erps ring ring-name { port0 | port1 } { interface interface-name | virtual-channel control-vlan vlan-id } erps ring ring-name { port0 | port1 } interface interface-name rpl-role role erps ring ring-name timers [ guard milliseconds | hold-off milliseconds | wtr minutes ]* erps ring ring-name type ring-type erps ring ring-name node ring-node erps ring ring-name parent-ring ring-name erps ring ring-name propagate-tc
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `erps ring ring-name` — Sets a textual name for this ERPS ring instance, according to the network manager’s choice. Valid characters are A-Z, a-z, 0-9 and + _ - “. — *Valores:* An identifier with up to 48 characters. · *Default:* None
- `erps ring ring-name ring-id id` — Sets the ring identifier used for control traffic (ERPS PDUs). — *Valores:* 1-239 · *Default:* None
- `erps ring ring-name control-vlan vlan-id` — Sets the VLAN used for control traffic (ERPS PDUs). — *Valores:* 1-4094 · *Default:* None
- `erps ring ring-name protected-vlans vlans` — Sets the list of VLANs protected by this ERPS ring instance. VLAN ranges or single VLANs are allowed and can be combined to specify the set of protected VLANs. — *Valores:* 1-4094 Example: protected-vlans 1-3,5,7-9 · *Default:* None
- `erps ring ring-name r-aps-level level` — Sets the R-APS level of PDUs exchanged by this ring instance. — *Valores:* 0-7 · *Default:* 0
- `erps ring ring-name port0 interface interface-name` — Sets the first ring instance’s port. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, two-hundred-g-ethernet, four-hundred-g-ethernet, lag. · *Default:* None
- `erps ring ring-name port1 interface interface-name` — Sets the second ring instance’s port. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, two-hundred-g-ethernet, four-hundred-g-ethernet, lag. · *Default:* None
- `erps ring ring-name port1 virtual-channel control-vlan vlan-id` — Sets the ring instance’s virtual-channel. Only port1 can be set as virtual-channel. This configuration is available only when ring-type parameter is set to sub-ring and node parameter is set to interconnection. — *Valores:* 1-4094 · *Default:* None
- `erps ring ring-name port0 interface interface-name rpl-role role` — Sets the RPL role of the first ring instance’s port. — *Valores:* owner | neighbor | none · *Default:* none (the interface is not an end of the RPL).
- `erps ring ring-name port1 interface interface-name rpl-role role` — Sets the RPL role of the second ring instance’s port. — *Valores:* owner | neighbor | none · *Default:* none (the interface is not an end of the RPL).
- `erps ring ring-name timers guard milliseconds` — Sets the guard timer value. — *Valores:* 10-2000 in steps of 10 · *Default:* 500
- `erps ring ring-name timers hold-off milliseconds` — Sets the hold-off timer value. — *Valores:* 0-10000 in steps of 100 · *Default:* 0
- `erps ring ring-name timers wtr minutes` — Sets the wait-to-restore timer value. — *Valores:* 1-12 · *Default:* 5
- `erps ring ring-name type ring-type` — Sets the ring-type for this ring instance. — *Valores:* major-ring | sub-ring · *Default:* major-ring
- `erps ring ring-name node node-type` — Sets the node-type for this ring instance. This configuration is available only when ring-type parameter is set to sub-ring. — *Valores:* interconnection | non-interconnection · *Default:* non-interconnection
- `erps ring ring-name parent-ring ring-name` — Sets the parent-ring for this ring instance. This configuration is available only when ring-type parameter is set to sub-ring. — *Valores:* An already created ring-name. · *Default:* None
- `erps ring ring-name propagate-tc` — Allows the sub-ring instance to propagate topology changes to the parent-ring instance. This configuration is available only when ring-type parameter is set to sub-ring. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |
| 4.6 | Added support for 100G interfaces. |
| 5.6 | Added sub-ring support. |
| 5.1 | Added support for 25G interfaces. |

**Usage Guidelines:**

Example: This example shows how to create an ERPS ring instance.

```text
#config
Entering configuration mode terminal
(config)#dot1q vlan 100
(config-vlan-100)# interface lag-1
(config-dot1q-interface-lag-1)# exit
(config-vlan-100)# interface ten-gigabit-ethernet-1/1/1
(config-vlan-100)#top
(config)#erps ring Foo
(erps-ring-Foo)#ring-id 10
(erps-ring-Foo)#control-vlan 100
(erps-ring-Foo)#protected-vlans 1-4,100-400,1024
(erps-ring-Foo)#r-aps-level 5
(erps-ring-Foo)#timers
(erps-ring-timers)#wtr 7
(erps-ring-timers)#guard 600
(erps-ring-timers)#hold-off 2000
(erps-ring-timers)#exit
(erps-ring-Foo)#port0 interface ten-gigabit-ethernet-1/1/1
(erps-ring-port0)#exit
(erps-ring-Foo)#port1 interface lag-1
(erps-ring-port1)#top
(config)#commit
```

Commit complete.

```text
(config)#
```

**Impacts and precautions:**

• Changes on specific configurations will cause a protocol reset for the affected rings, namely: ring ID and control VLAN. Traffic on the protected VLANs will be affected. Considerations to prevent network loops during maintenance procedures: • Before mounting a physical ring, please consider disabling, in the node that is going to be designated as the RPL owner node, the port that represents the RPL end point. • To add a new protected VLAN, you must add it to the protected VLANs list of the ERPS ring before adding the ring ports to the VLAN domain (dot1q vlan id interface name). • Before removing a VLAN from the ERPS list of protected VLANs, you must first remove the ring ports from that VLAN domain (no dot1q vlan id interface name). • To physically add a new node in the ERPS ring, it is recommended to disable (shutdown) the adjacent port of the neighbors’ nodes of the ring node that is being added. After making all the connections and configurations of the new ring node, enable (no shutdown) the adjacent ports to finish the procedure. • To physically remove a node from the ERPS ring, it is recommended to disable (shutdown) the adjacent port of the neighbors’ nodes of the ring node that is being removed. After the ring node removal, enable (no shutdown) the adjacent ports to finish the procedure. Considerations to create a valid ERPS configuration: • ERPS cannot be configured in a port that is member of an EAPS domain or is protected by STP. • The minimum configuration of an ERPS ring must contain a ring-id, a control-vlan, at least one protected-vlan and two different ports (port0 and port1) as members of the ring. • At least one of the ring member ports’ rpl-role must be ‘none’. • The ports of an ERPS ring must be members, and the only members, of its control-vlan. • A control-vlan of an ERPS ring cannot exist in the protected-vlan list of any ERPS ring or EAPS domain. • The protected-vlan list of an ERPS ring cannot overlap the protected-vlan list of another ERPS ring or EAPS domain. • The same protected-vlan list can be used in different ERPS rings or EAPS domains as long as the protected ports are different.

**Hardware restrictions:**

N/A


### `show erps`

> **Página:** 461 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display ERPS status information.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show erps [brief] [detail]
```

**Parameters:**

- `brief` — This parameter displays a summary information about ring instances, including name, ring ID, control VLAN, and state. — *Valores:* N/A · *Default:* N/A
- `detail` — This parameter displays all that the brief parameter displays plus a table listing the the number of protected VLANs, the ring ports, and their RPL roles. When no parameter is given the show command displays the same content of detail parameter. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |
| 8.4.0 | Changed the column’s order for the ring table. |

**Usage Guidelines:**

Given the equipment has 5 ring instances, the brief status command could result in the following output:

```text
# show erps brief
RING CONTROL PARENT
```

ID VLAN NAME RING TYPE RING STATE PORT0 STATE PORT1 STATE ------------------------------------------------------------------------------------- 1 11 MyRing1 major-ring - Protection Forward Blocked 2 20 MyRing2 major-ring - Idle Forward Blocked 3 31 MyRing3 major-ring - Pending Forward Blocked 15 151 MyRing4 major-ring - Protection Forward Forward 15 152 MyRing5 sub-ring MyRing1 Protection Data Blocked -

```text
#
```

The output of a detail status command would look like this:

```text
# show erps detail
```

RING CONTROL PARENT PROTECTED ... ID VLAN NAME RING TYPE RING STATE VLANS PORT0 ... ------------------------------------------------------------------------------- ... 1 11 MyRing1 major-ring - Protection 10 1ge-1/1/1 ... 2 20 MyRing2 major-ring - Idle 5 1ge-1/1/3 ... 3 31 MyRing3 major-ring - Pending 5 1ge-1/1/9 ... 15 151 MyRing4 major-ring - Protection 8 lag-1 ... 15 152 MyRing5 sub-ring MyRing1 Protection 20 1ge-1/1/5 ... PORT0 PORT0 PORT1 PORT1 RPL LOCAL RPL LOCAL ROLE FAILURE PORT0 STATE PORT1 ROLE FAILURE PORT1 STATE ------------------------------------------------------------------------------------ owner Yes Forward 1ge-1/1/2 none No Data Blocked none No Forward 1ge-1/1/4 owner No Blocked owner Yes Forward 1ge-1/1/10 none No Blocked none No Forward lag-2 neighbor Yes Forward none No Forward virtual-channel 15 - - -

```text
#
```

**Output Terms:**

Output Description NAME The name of the ring. Output Description RING ID The ring identifier. CONTROL VLAN The VLAN used for ERPS control packets, in this ring instance. The current state of the ring instance. The possible states are Init, STATE Idle, Protection, ManualSwitch, ForcedSwitch, and Pending. PROTECTED VLANS The number of VLANs protected by this ring instance. PORT0 The first ring instance’s port. The RPL role of the first ring instance’s port. Possible values are PORT0 RPL ROLE owner, neighbor, and none. The state of the port. Possible values are Forward, Blocked, Data PORT0 STATE Blocked, Control Channel Blocked and Unknown. PORT0 LOCAL Inform if the port has a local failure. Possible values are Yes and No. FAILURE PORT1 The second ring instance’s port. The RPL role of the second ring instance’s port. Possible values are PORT1 RPL ROLE owner, neighbor, and none. The state of the port. Possible values are Forward, Blocked, Data PORT1 STATE Blocked, Control Channel Blocked and Unknown. PORT1 LOCAL Inform if the port has a local failure. Possible values are Yes and No. FAILURE

**Impacts and precautions:**

None

**Hardware restrictions:**

None EAPS This topic describes the commands related to management of EAPS topologies such as commands to configure the protected VLANs or to inspect the protection status.


## EAPS

### `eaps`

> **Página:** 465 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The current implementation follows the EAPS version 1.3 described as a Internet-Draft, which includes some enhancements over the EAPS version 1 described by RFC 3619.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
eaps domain { control-vlan vlan-id | port { primary interface-name | secondary interface-name }* | protected-vlans vlans }* eaps domain [name identifier] eaps domain {mode {transit | master}} eaps domain [ failtime seconds | failtime-action action-type | hellotime seconds ]*
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `eaps domain` — Domain identification — *Valores:* 0-63 · *Default:* None
- `control-vlan vlan-id` — Sets the VLAN used for control traffic (EAPS PDUs). This VLAN cannot be used for data traffic. — *Valores:* 1-4094 · *Default:* None
- `failtime seconds` — Only relevant for the Master node. After received health check PDUs, a timer with this value is started and upon its expiration the ring will take the failtime-action. The timer is restarted on receipt of any health check PDU. — *Valores:* 1-60 · *Default:* 3
- `failtime-action action-type` — Only relevant for the Master node. Use action send-alert to log the failure and query the link status of all Transit nodes and then force a network converge through the secondary port if some failure is reported. — *Valores:* { send-alert } · *Default:* send-alert
- `hellotime seconds` — Only relevant for the Master node. Sets the interval for transmission of health check PDUs. — *Valores:* 1-60 · *Default:* 1
- `mode { master | transit }` — Sets the EAPS mode of this ring node. A ring is allowed to have a single Master node and multiple Transit nodes. — *Valores:* { master | transit } · *Default:* transit
- `name identifier` — Set a textual name for this EAPS domain, according to the network manager’s choice. Valid characters are A-Z, a-z, 0-9 and + _ - " — *Valores:* An identifier with at most 48 characters. · *Default:* None
- `port { primary interface-name | secondary interface-name}*` — Defines both primary and secondary ports of EAPS ring. — *Valores:* NA · *Default:* NA
- `primary interface-name` — Sets a specific port as primary. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet,two-hundred-g-ethernet, four-hundred-g-ethernet, lag. · *Default:* None
- `secondary interface-name` — Sets a specific port as secondary — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, lag. · *Default:* None
- `protected-vlans vlans` — Sets the list of protected VLANs of this EAPS domain. Ranges of VLANs or single VLAN are allowed and can be combined to specify the set of protected VLANs — *Valores:* 1-4094 Example: protected-vlans 1-3,5,7-9 · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |
| 3.0 | Added support on 40G interfaces |
| 4.6 | Added support on 100G interfaces |
| 5.0 | Added support on 25G interfaces |
| 11.0 | Added support for DM4340 series |

**Usage Guidelines:**

Example: This example shows how to create an EAPS master domain.

```text
#config
Entering configuration mode terminal
(config)#dot1q vlan 100
(config-vlan-100)# interface lag-1
(config-dot1q-interface-lag-1)# exit
(config-vlan-100)# interface ten-gigabit-ethernet-1/1/1
(config-vlan-100)#top
(config)#eaps 0
(config-eaps-1)#control-vlan 100
(config-eaps-1)#mode master
(config-eaps-1)#protected-vlans 1-4,100-400,1024
(config-eaps-1)#port
(config-eaps-1-port)#primary ten-gigabit-ethernet-1/1/1
(config-eaps-1-port)#secondary lag-1
(config-eaps-1)#top
(config)#commit
```

Commit complete.

```text
(config)#
```

**Impacts and precautions:**

• Changes on specific configurations will cause a protocol reset for the affected domains, namely: primary or secondary port, control-vlan and mode. Traffic on the protected VLANs will be affected. Considerations to prevent network loops during maintenance procedures: • Before mounting a physical ring, please consider disabling the secondary port of the Master node. • To add a new protected VLAN, you must add it to the protected VLAN list of the EAPS domain before adding the ring ports to the VLAN domain (dot1q vlan id interface name). • Before removing a VLAN from the EAPS list of protected VLANs, you must first remove the ring ports from that VLAN domain (no dot1q vlan id interface name). • To physically add a new node in the EAPS ring, it is recommended to disable (shutdown) the adjacent port of the neighbors nodes of the ring node that is being added. After making all the connections and configurations of the new ring node, enable (no shutdown) the adjacent ports to finish the procedure. • To physically remove a node from the EAPS ring, it is recommended to disable (shutdown) the adjacent port of the neighbors nodes of the ring node that is being removed. After the ring node removal, enable (no shutdown) the adjacent ports to finish the procedure.

**Hardware restrictions:**

The DM4340 series supports up to four simultaneous EAPS domains. As a result, the valid configuration range is from 0 to 3.


### `show eaps`

> **Página:** 470 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display information about EAPS status and statistics.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show eaps [brief] [detail]
```

**Parameters:**

- `brief` — This parameter displays a summary information about the domains, including domain’s ID, name, state, mode and status of both primary and secondary ports. — *Valores:* N/A · *Default:* N/A
- `detail` — This parameter displays all that the brief parameter displays plus a table listing the protected VLANs and both the primary and secondary ports. When no parameter is given the show command displays the same content of detail parameter. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

Given the equipment has the domains 0, 1, 2, 3, 4, 5 and 63 created, let’s see the brief information:

```text
# show eaps brief
PRIMARY PORT SECONDARY
```

ID NAME STATE MODE STATE PORT STATE ---------------------------------------------------------------------------- 0 My-Eaps-Domain-0 Idle transit Down Blocked Down Blocked 1 My-Eaps-Domain-1 Init master Up Enabled Up Blocked 2 My-Eaps-Domain-2 Complete master Up Enabled Up Blocked 3 My-Eaps-Domain-3 Failed master Down Enabled Up Blocked 4 My-Eaps-Domain-4 Pre Forwarding transit Up Enabled Up Blocked 5 My-Eaps-Domain-5 Links Down transit Up Enabled Down Blocked 63 My-Eaps-Domain-63 Links Up transit Up Enabled Up Enabled

```text
#
```

Now let’s see the detailed information:

```text
# show eaps detail
PRIMARY PORT SECONDARY
```

ID NAME STATE MODE STATE PORT STATE ---------------------------------------------------------------------------- 0 My-Eaps-Domain-0 Idle transit Down Blocked Down Blocked 1 My-Eaps-Domain-1 Init master Up Enabled Up Blocked 2 My-Eaps-Domain-2 Complete master Up Enabled Up Blocked 3 My-Eaps-Domain-3 Failed master Down Enabled Up Blocked 4 My-Eaps-Domain-4 Pre Forwarding transit Up Enabled Up Blocked 5 My-Eaps-Domain-5 Links Down transit Up Enabled Down Blocked 63 My-Eaps-Domain-63 Links Up transit Up Enabled Up Enabled PROTECTED ID PRIMARY PORT SECONDARY PORT VLANS --------------------------------------------------------------------- 0 ten-gigabit-ethernet-1/1/1 gigabit-ethernet-1/1/1 10,20,30 1 ten-gigabit-ethernet-1/1/2 gigabit-ethernet-1/1/2 31-35,39 2 ten-gigabit-ethernet-1/1/3 gigabit-ethernet-1/1/3 40 3 ten-gigabit-ethernet-1/1/4 gigabit-ethernet-1/1/4 45-50 4 ten-gigabit-ethernet-1/1/5 gigabit-ethernet-1/1/5 51-55,60-65 5 ten-gigabit-ethernet-1/1/6 gigabit-ethernet-1/1/6 70,75 63 ten-gigabit-ethernet-1/1/7 gigabit-ethernet-1/1/7 100,105-110

```text
#
```

**Output Terms:**

Output Description ID The ID number of the domain. Name The name of the domain. The current state of the domain. The possible states are Idle, Init, State Complete, Failed, Pre Forwarding, Links Down and Links Up. The state of the domain’s primary port, where Up and Down refer Primary port state to port link status and Enable and Blocked refer to the port traffic block state. The state of the domain’s secondary port, where Up and Down refer Secondary port to port link status and Enable and Blocked refer to the port traffic state block state. Primary port The primary port configured in the domain. Secondary port The secondary port configured in the domain. Protected VLANs The list of protected VLANs configured in the domain.

**Impacts and precautions:**

None

**Hardware restrictions:**

None CONTROL PROTOCOLS This topic describes the commands related to management of control protocol such as commands to enable PDU tunnel, drop, peer and forward of some specific protocol.


## Control Protocols

### `layer2-control-protocol interface protocols action action-type`

> **Página:** 474 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Allows actions for L2 control protocols (PDUs) received by an interface. The action tunnel is based on destination MAC address modification for protocol packets. PDUs received on a port that has tunneling enabled will have their destination address changed to another address. With that destination address the packets will be transparently forwarded (flooded) through the network until some other port with tunneling enabled is reached. You must use this command on access ports that will convert protocol packets into tunneled packets and/or convert tunneled packets into protocol packets. The intermediate ports on the tunneling path must not have this command enabled so that they will only forward tunneled packets without modifications. If no action is specified for an interface, the PDUs will be dropped, forwarded or treated according with the protocol standards.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
layer2-control-protocol { interface interface-name [ protocols { action action-type } ] }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Interface to be configured. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | hundred-gigabit-ethernet-chassis/slot/port | two-hundred-g-ethernet-chassis/slot/port | four-hundred-g-ethernetchassis/slot/port |lag-id } · *Default:* None
- `protocols` — Protocol or group of protocols. The value extended configures the following group of protocols: IEEE, Cisco, EAPS and RRPP. Other protocols can be configured with its respective name and they take precedence over the extended tunneling. — *Valores:* { extended | lacp | marker | oam | stp | pvst | lldp | pagp | udld | cdp | vtp | eaps | erps | gvrp | dot1x } · *Default:* None
- `action action-type` — PDU packet action. The value tunnel configures Layer 2 protocols tunneling for Ethernet interfaces. The value forward is only available for extended protocols and configures Layer 2 protocols to be switched transparently for Ethernet interfaces. — *Valores:* { tunnel | forward } · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 3.0 | Added support for 40G interfaces. |
| 4.6 | Added support for 100G interfaces. |
| 4.7 | Added support for new protocols tunneling. Added support for LLDP tunneling and action Forward for extended tun4.9 neling. |
| 5.0 | Added support for 25G interfaces. |
| 5.2 | Added support for tunneling protocols PAGP, UDLD, CDP and VTP. |
| 5.4 | Added support for tunneling protocols EAPS, ERPS, GVRP and Dot1x. |

**Usage Guidelines:**

To configure protocols to tunnel:

```text
(config)# layer2-control-protocol
(l2cp)# interface gigabit-ethernet-1/1/1
(l2cp-interface-gigabit-ethernet-1/1/1)# extended action tunnel
(l2cp-interface-gigabit-ethernet-1/1/1)# lacp action tunnel
(l2cp-interface-gigabit-ethernet-1/1/1)# stp action tunnel
```

To remove protocol configuration:

```text
(config)# layer2-control-protocol
(l2cp)# interface gigabit-ethernet-1/1/1
(l2cp-interface-gigabit-ethernet-1/1/1)# no extended
(l2cp-interface-gigabit-ethernet-1/1/1)# no stp
```

**Impacts and precautions:**

When action parameter is configured as tunnel, the equipment will not be in accordance with the “Frame Filtering” section from IEEE 802.1Q standard. Features such as STP, EAPS and others that have their controls protocols packets impacted will not work together with action tunnel. ACL action “deny” does not affect tunneled packets. When enabling Protocol tunnelings for an access interface, it is recommended to configure the same tunneling modes for all access interfaces within the same VLAN.

**Hardware restrictions:**

N/A


### `layer2-control-protocol tunnel-mac`

> **Página:** 478 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Allows to set the destination MAC address for tunneled packets on modes LACP, Marker, OAM and STP.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
layer2-control-protocol tunnel-mac mac
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `tunnel-mac mac` — Set destination MAC Address for per-protocol tunneled packets. — *Valores:* { datacom | interop } · *Default:* datacom

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.7 | This command was introduced. |

**Usage Guidelines:**

To configure the destination MAC address for tunneled packets:

```text
(config)# layer2-control-protocol
(l2cp)# tunnel-mac interop
```

To reset the configuration to default:

```text
(config)# layer2-control-protocol
(l2cp)# no tunnel-mac
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `layer2-control-protocol tunnel-priority`

> **Página:** 480 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Allows to set the PCP (802.1p) and QoS Scheduler Queue for tunneled packets.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
layer2-control-protocol tunnel-priority priority
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `tunnel-priority priority` — Set PCP (802.1p) and QoS Scheduler Queue for tunneled packets. — *Valores:* { 0-7 } · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |

**Usage Guidelines:**

To configure priority for tunneled packets:

```text
(config)# layer2-control-protocol
(l2cp)# tunnel-priority 7
```

To remove configuration:

```text
(config)# layer2-control-protocol
(l2cp)# no tunnel-priority
```

**Impacts and precautions:**

The tunnel-priority takes precedence over the priority from ACL action “set pcp”.

**Hardware restrictions:**

N/A


### `layer2-control-protocol vlan protocols action action-type`

> **Página:** 482 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Command used to configure PDU on preexisting VLAN configured with service/VLAN TLS.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616.

**Syntax:**

```text
layer2-control-protocol { vlan vlan-id [ protocols { action action-type } ] }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vlan vlan-id` — VLAN ID to be configured. — *Valores:* 1 - 4094 · *Default:* None
- `protocols` — Protocol or group of protocols. The value extended configures the following group of protocols: IEEE, Cisco, EAPS and RRPP. — *Valores:* extended · *Default:* None
- `action action-type` — PDU packet action. The value drop discards the packet. The value forward sends the packet without any change. — *Valores:* {drop | forward} · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. This command was deprecated. From this version on, all service VLAN 4.2 TLS have forward action by default. |

**Usage Guidelines:**

VLAN must be created and configured as service/VLAN TLS to use this functionality. The commit of a configuration with a PDU action (drop or forward) with a non existing VLAN or with a VLAN not configured properly (without service/VLAN TLS configuration) will result in an error message and the configuration will not be applied. This command supports up to 186 actions, however it depends on platform and services configured. To configure extended protocols to forward:

```text
(config)# layer2-control-protocol
(l2cp)# vlan 100
(l2cp-vlan-100)# extended action forward
```

To configure extented protocols to drop:

```text
(config)# layer2-control-protocol
(l2cp)# vlan 100
(l2cp-vlan-100)# extended action drop
```

To remove configuration:

```text
(config)# layer2-control-protocol
(l2cp)# no vlan 100
```

**Impacts and precautions:**

When action parameter is configured as forward (transparent), the equipment will not be in accordance with the “Frame Filtering” section from IEEE 802.1Q standard.

**Hardware restrictions:**

N/A LOOPBACK DETECTION This topic describes the commands related to loopback detection.


## Loopback Detection

### `loopback-detection`

> **Página:** 485 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enable Loopback Detection

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
loopback-detection destination-address address interface interface-name timer time
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `destination-address address` — Destination MAC address to be used on Loopback Detection frames. — *Valores:* alternative is the only value currently supported. It means that the alternative MAC address of slow protocols (01:04:DF:10:00:02) will be used. · *Default:* alternative
- `interface interface-name` — Ethernet interface where Loopback Detection is being enabled. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet. · *Default:* N/A
- `timer time` — Set the time interval to be waited before unblock the interface. — *Valores:* 2-86400 seconds · *Default:* 30 seconds

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.7 | This command was introduced. |
| 5.10 | Added support for 25G interfaces. |

**Usage Guidelines:**

The Loopback Detection can be enabled on Ethernet interfaces to detect loop failures caused by RX/TX fiber loop or loops in neighbor networks.

```text
# config
(config)# loopback-detection interface gigabit-ethernet-1/1/1
(config-lbd-interface-gigabit-ethernet-1/1/1)# timer 30
(config-lbd-interface-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(config-lbd-interface-gigabit-ethernet-1/1/1)# end
#
```

One-line like command is also supported.

```text
# config
(config)# loopback-detection interface ten-gigabit-ethernet-1/1/1 timer 45
(config-lbd-interface-ten-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(config-lbd-interface-ten-gigabit-ethernet-1/1/1)# end
#
```

**Impacts and precautions:**

• Loopback Detection is not supported on interfaces added as members of a Link Aggregation Group (LAG) or LAG interfaces themselves. In this case LACP can be used to prevent loops.

**Hardware restrictions:**

N/A


### `show loopback detection`

> **Página:** 488 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display information about Loopback Detection status and configuration. This show only present ports that are configured for Loopback Detection.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show loopback-detection [ { port | all } ] [ loopback ] [ timeout ] [ unblock-time ]
```

**Parameters:**

- `port` — The Interface with Loopback Detection whose status is desired to show. — *Valores:* N/A · *Default:* N/A
- `all` — Shows the Loopback Detection status for all enabled interfaces. — *Valores:* N/A · *Default:* N/A
- `loopback` — Shows only the Loopback Detection status for the desired port. — *Valores:* N/A · *Default:* N/A
- `timeout` — Shows only the time that the port still needs to wait in non-loop status to unblock. — *Valores:* N/A · *Default:* N/A
- `unblock-time` — Shows only the configured time to unblock a port after the loop state clearance. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.7 | This command was introduced. |
| 5.10 | Added support for 25G interfaces. |

**Usage Guidelines:**

Given the equipment has the following ports configured for Loopback detection.

```text
# show running-config loopback-detection
loopback-detection
destination-address alternative
interface ten-gigabit-ethernet-1/1/1
timer 10
!
!
#
```

A show will present:

```text
# show loopback-detection
UNBLOCK
INTERFACE TIME TIMEOUT LOOPBACK
-------------------------------------------------------
ten-gigabit-ethernet-1/1/1 10 3 yes
#
```

**Output Terms:**

Output Description INTERFACE The Interface that is configured for Loopback Detection. The configured time to unblock a port after the loop state clearance. UNBLOCK TIME The time that the port still needs to wait in non-loop status to unTIMEOUT block. The status of loopback detection for the port. Can be YES for looped, LOOPBACK or NO for non-loop.

**Impacts and precautions:**

None

**Hardware restrictions:**

None LINK FLAP DETECTION This topic describes the commands related to link flap detection.


## Link Flap Detection

### `link-flap`

> **Página:** 491 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure Link Flap Detection

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
link-flap interface interface-name detection transitions value interval time restore-timeout time
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Ethernet interface where Link Flap Detection is being enabled. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet. · *Default:* N/A
- `detection transitions value` — Set the transitions to be detected during the interval before blocking the interface. — *Valores:* 2-100 transitions · *Default:* 10 transitions.
- `detection interval time` — Set the time interval to monitor the transitions of interface link state after the first one. — *Valores:* 1-3600 seconds · *Default:* 40 seconds.
- `detection restore-timeout time` — Set the time interval without new transitions to wait before restoring the interface to the previous state. — *Valores:* 1-86400 seconds · *Default:* 30 seconds.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.7 | This command was introduced. |
| 5.10 | Added support for 25G interfaces. |

**Usage Guidelines:**

The Link Flap Detection can be enabled on Ethernet interfaces to avoid link status propagation on unstable links.

```text
# config
(config)# link-flap interface gigabit-ethernet-1/1/1
(config-lfd-interface-gigabit-ethernet-1/1/1)# detection transitions 4
(config-lfd-interface-gigabit-ethernet-1/1/1)# detection interval 20
(config-lfd-interface-gigabit-ethernet-1/1/1)# detection restore-timeout 60
(config-lfd-interface-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(config-lfd-interface-gigabit-ethernet-1/1/1)# end
#
```

One-line like command is also supported .

```text
# config
(config)# link-flap interface gigabit-ethernet-1/1/1 detection transitions 4 detection
interval 20 detection restore-timeout 60
(config-lfd-interface-ten-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(config-lfd-interface-ten-gigabit-ethernet-1/1/1)# end
#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show link-flap`

> **Página:** 494 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays information about Link Flap Detection status and configuration. This command only shows interfaces that are configured for Link Flap Detection.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show link-flap [ { interface | all } ] [ config-interval ] [ config-restore-timeout ] [ config-transitions ] [ detected-transitions ] [ detection-timeout ] [ link-flap ] [ restore-timeout ]
```

**Parameters:**

- `interface` — The interface whose Link Flap Detection status should be shown. — *Valores:* N/A · *Default:* N/A
- `all` — Shows the Link Flap Detection status for all enabled interfaces. — *Valores:* N/A · *Default:* N/A
- `config-interval` — Shows the configured detection time interval for the specified interface. — *Valores:* N/A · *Default:* N/A
- `config-restore-timeout` — Shows the configured restore time interval for the specified interface. — *Valores:* N/A · *Default:* N/A
- `config-transitions` — Shows the configured number of transitions to be detected before blocking the specified interface. — *Valores:* N/A · *Default:* N/A
- `detected-transitions` — Shows the number of transitions detected for the specified interface. — *Valores:* N/A · *Default:* N/A
- `detection-timeout` — Show the remaining time before resetting the transitions counter if the specified interface does not enter link flap state. — *Valores:* N/A · *Default:* N/A
- `link-flap` — Shows the Link Flap Detection state for the specified interface. — *Valores:* N/A · *Default:* N/A
- `restore-timeout` — Shows the remaining time without transitions before unblocking the specified interface. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

Given the equipment has the following interface configured for Link Flap Detection.

```text
# show running-config link-flap
link-flap
interface ten-gigabit-ethernet-1/1/1
detection transitions 5
detection interval 25
detection restore-timeout 65
!
!
#
```

A show command will display the following information:

```text
# show link-flap
...
```

Configured ... Configured Configured Restore ... Interface Transitions Interval Timeout ... ----------------------------------------------------------------- ... ten-gigabit-ethernet-1/1/1 5 25 65 ... Detected Detection Restore Link Transitions Timeout Timeout Flap --------------------------------------- 0 0 0 no

```text
#
```

**Output Terms:**

Output Description Interface The interface that is configured for Link Flap Detection. Configured The configured number of transitions to be detected before blocking Transitions the interface. Configured The configured detection time interval. Interval Configured restore The configured restore timeout. timeout Detected The number of transitions detected. Transitions Remaining time before resetting the transitions counter if the interDetection Timeout face does not enter link flap state. Restore Timeout Remaining time without transitions before unblocking the interface. Link Flap The Link Flap Detection state.

**Impacts and precautions:**

None

**Hardware restrictions:**

None HOLD TIME This topic describes the commands related to hold time feature.


## Hold Time

### `hold-time`

> **Página:** 498 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure a delay for processing a link event on a interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
hold-time interface interface-name down time
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Ethernet interface where hold-time is being enabled. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet. · *Default:* N/A
- `down time` — Delay for processing a link down event on an interface. When a link down happens, a timer will be started. If the timer expires, the link down will be notified. If a link up happens before it expires, the timer is reset. The administrative shutdown of a interface may be affected by this configuration, therefore a “no shutdown” may prevent a link down notification if executed before the timer expiring. — *Valores:* 50-5000 milliseconds in steps of 50 milliseconds. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.10 | This command was introduced. |

**Usage Guidelines:**

The hold-time configuration can be enabled on Ethernet interfaces to delay the link down processing.

```text
# config
(config)# hold-time interface gigabit-ethernet-1/1/1
(config-interface-gigabit-ethernet-1/1/1)# down 500
(config-interface-gigabit-ethernet-1/1/1)# commit
```

Commit complete.

```text
(config-interface-gigabit-ethernet-1/1/1)# end
#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A BACKUP LINK This topic describes the commands related to backup link protection.


## Backup Link

### `backup-link`

> **Página:** 500 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create an alternative interface to the main interface (Backup-Link pair). That is, in case of link problems (link down, blocked due to link-flap detection, EFM, loopback detection, etc.) in the main interface, the backup interface takes its place, preventing packet loss. The main interface assumes again when a link problem occurs with the backup interface (and the state of the main interface link is up) or when the revertive mode is configured. The Backup-Link can be configured on ethernet and LAG interfaces.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
backup-link id {main interface-name} {backup interface-name} [action {block | shutdown}] [reversion [mode {revertive | non-revertive}] [delay time]] [description text]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Unique identification number of the Backup-Link pair. — *Valores:* 0 - 65535 · *Default:* N/A
- `main interface-name` — Main ethernet or LAG interface where Backup-Link is being enabled. — *Valores:* Name of the interface. · *Default:* N/A
- `backup interface-name` — Backup ethernet or LAG interface where Backup-Link is being enabled. — *Valores:* Name of the interface. · *Default:* N/A
- `action {block | shutdown}` — Configuration of the link state of the Backup-Link pair interfaces. On block mode operation, when one or both interfaces have the link up, the other must be blocked, and, when both are down, both must be blocked. On shutdown mode operation, when one or both interfaces have the link up, the other must be administratively down, and, when both are down, both must be administratively down. With shutdown action, it’s not possible to configure the revertive mode. — *Valores:* List of supported actions: block and shutdown. · *Default:* block.
- `reversion mode {revertive | non-revertive}` — With the link status in block, it’s possible to configure the automatic reversion to the main interface. That is, when setting the mode to revertive, if a link problem occurs to the main interface and the backup interface takes its place, the main, when fully recovered, will assumes again automatically after the configured delay. In non-revertive mode, the main interface will only assumes again if the backup interface links goes down. Reversion is not supported with shutdown action. — *Valores:* List of supported reversion modes: revertive and non-revertive. · *Default:* non-revertive.
- `reversion delay time` — When in revertive mode, set the delay interval before reactivating the main interface. After the delay ends and the main interface link is up, the Backup-Link interfaces are switched back. — *Valores:* 1 - 300 seconds. · *Default:* 35 seconds.
- `description text` — Optional description of the Backup-Link pair. — *Valores:* String with a maximum of 128 characters. It only accepts alphanumeric characters and ‘*’, ‘@’, ‘/’, ‘_’, ‘.’, ‘+’ and ‘-’. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 6.2 | This command was introduced. |

**Usage Guidelines:**

The following example shows how to create a Backup-Link pair with non-revertive block configuration.

```text
# config
(config)# backup-link 1
(config-backup-link-1)# main gigabit-ethernet-1/1/1
(config-backup-link-1)# backup gigabit-ethernet-1/1/2
(config-backup-link-1)# commit
```

Commit complete.

```text
(config-backup-link-1)#
```

The following example shows how to create a Backup-Link pair with revertive block configuration and delay of 30 seconds.

```text
# config
(config)# backup-link 2
(config-backup-link-2)# main ten-gigabit-ethernet-1/1/1
(config-backup-link-2)# backup ten-gigabit-ethernet-1/1/2
(config-backup-link-2)# action block
(config-backup-link-2)# reversion mode revertive
(config-backup-link-2)# reversion delay 30
(config-backup-link-2)# commit
```

Commit complete.

```text
(config-backup-link-2)#
```

The following example shows how to create a Backup-Link pair with shutdown configuration.

```text
# config
(config)# backup-link 3
(config-backup-link-3)# main lag-1
(config-backup-link-3)# backup lag-2
(config-backup-link-3)# action shutdown
(config-backup-link-3)# commit
```

Commit complete.

```text
(config-backup-link-3)#
```

**Impacts and precautions:**

None.

**Hardware restrictions:**

LAG interfaces are not supported as main or backup interface in the following platform: DM4340. CHAPTER 6: LAYER 3 - ROUTING This chapter describes the commands related to management of Layer 3 protocols in the DmOS CLI. BASIC This topic describes the commands related to management of basic routing such as commands to configure the ARP behavior or Static Routes.
