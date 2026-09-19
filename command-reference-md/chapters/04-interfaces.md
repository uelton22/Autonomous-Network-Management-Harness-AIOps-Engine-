# Capítulo 4: Interfaces

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## Ethernet

### `breakout interface`

> **Página:** 255 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the breakout mode of an Ethernet interface.

**Supported Platforms:** This command is supported only in the following platforms: DM4770.

**Syntax:**

```text
breakout interface [ interface-name | split-mode {4x25G}]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Ethernet interface which will have it breakout operation mode configured. — *Valores:* N/A · *Default:* N/A
- `split-mode` — The breakout operation mode that will be applied on the interface. — *Valores:* 4x25G: This configuration allows the interface to work with a breakout cable spliting the interface, in four new interfaces. In order to work this must have the proper cable inserted. Although the breakout configuration only applies as 4x25G, the new 25G interfaces can work in lower speeds such as 10G and 1G. · *Default:* 4x25G

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |

**Usage Guidelines:**

This command should be used to configure breakout on the Ethernet interfaces. Initially this feature is only available to hundred gigabit ethernet ports with the 4x25G configuration. Example: This example is applied to interface-name equal to hundred-gigabit-ethernet-1/1/1. DM4770(config)# breakout interface hundred-gigabit-ethernet-1/1/1 DM4770(breakout-hundred-gigabit-ethernet-1/1/1)# split-mode 4x25G Before the commit is applied, the new splitted interfaces will be available to be configured. Example: DM4770(config)# interface twenty-five-g-ethernet ? Possible completions: <chassis-id:unsignedInt> DM4770(config)# breakout interface hundred-gigabit-ethernet-1/1/1 DM4770(breakout-hundred-gigabit-ethernet-1/1/1)# split-mode 4x25G DM4770(breakout-hundred-gigabit-ethernet-1/1/1)# top DM4770(config)# interface twenty-five-g-ethernet ? Possible completions: <chassis-id:unsignedInt> 1/1/1 1/1/2 1/1/3 1/1/4 When the commit is applied, given it is a new breakout configuration, it will appear a warning with the following message: Example: DM4770(breakout-hundred-gigabit-ethernet-1/1/1)# commit Changing breakout configuration will cause the system to reboot. The following warnings were generated: ’breakout interface’: Proceed? [yes,no] To remove the breakout configuration from a given interface it is only needed to add the “no” form to revert. Example: DM4770(config)# breakout interface hundred-gigabit-ethernet-1/1/1 DM4770(breakout-hundred-gigabit-ethernet-1/1/1)# no split-mode Both the ‘add’ and the ‘remove’ breakout configuration command can be written in one line. Example: DM4770(config)# breakout interface hundred-gigabit-ethernet-1/1/1 split-mode 4x25G DM4770(config)# no breakout interface hundred-gigabit-ethernet-1/1/1 split-mode

**Impacts and precautions:**

The commit of a breakout configuration (either adding or removing the feature on any interface) will cause the equipment to reboot. Given the equipment does have a breakout configuration applied and the load factory-config configuration command is commited, the system will reboot and all the configuration will be reset to factory config, undoing the breakout configuration.

**Hardware restrictions:**

All the breakout interfaces from the same port must have the same speed configured. The DmOS won’t accept the commit of a configuration with different speeds and will output the following error message: Aborted: ’interface twenty-five-g-ethernet’: All split from group twenty-five-g-ethernet-1/1/<initial>-<last> ports must have speed configured to the same value. The breakout configuration cannot be applied on the following interfaces: DM4770 16CX: - hundred-gigabit-ethernet-1/1/1 - hundred-gigabit-ethernet-1/1/2 DM4770 32CX: - hundred-gigabit-ethernet-1/1/31


### `dwdm interface`

> **Página:** 259 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure DWDM QSFP on ethernet ports with support for DWDM.

**Supported Platforms:** This command is supported only in the following platforms: DM4770, DM4780, DM4920.

**Syntax:**

```text
dwdm interface interface-name [ grid-50ghz { frequency { 191.30 .. 196.10} } | grid-100ghz { frequency { 191.3 .. 196.1} } | tx-power { range -20.0 .. 3.0} ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Configures ethernet port that supports DWDM QSFP. — *Valores:* N/A · *Default:* N/A
- `grid` — Configure DWDM grid in GHz. — *Valores:* 50GHz or 100GHz · *Default:* 100GHz
- `frequency` — Configures the DWDM frequency. It’s dependent on the grid choice: 0.05 THz steps for 50GHz grid; 0.1 THz steps for 100GHz grid. — *Valores:* range from 191.3 to 196.1 · *Default:* 193.7
- `tx-power` — Set the DWDM transmission power in dBm with 0.1 steps. — *Valores:* range from -20.0 to 3.0 · *Default:* 0.0

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 6.4 | This command was introduced. |

**Usage Guidelines:**

This command should be used to configure Ethernet interfaces with DWDM QSFP support. Examples: These examples show the DWDM configuration for interface hundred gigabit interface 1/1/16. To configure the grid with 50GHz and its frequency. DM4770(config)# dwdm interface hundred-gigabit-ethernet-1/1/16 DM4770(dwdm-hundred-gigabit-ethernet-1/1/16)# grid-50ghz frequency 191.35 DM4770(dwdm-hundred-gigabit-ethernet-1/1/16)# commit Commit complete. To configure the grid with 100GHz and its frequency. DM4770(config)# dwdm interface hundred-gigabit-ethernet-1/1/16 DM4770(dwdm-hundred-gigabit-ethernet-1/1/16)# grid-100ghz frequency 191.4 DM4770(dwdm-hundred-gigabit-ethernet-1/1/16)# commit Commit complete. To set tx-power DM4770(config)# dwdm interface hundred-gigabit-ethernet-1/1/16 DM4770(dwdm-hundred-gigabit-ethernet-1/1/16)# tx-power -2.0

**Impacts and precautions:**

The tx-power must be set with caution, higher configuration values could damage partner transceiver optical receiver. The tx-power parameter allow the provision of a transmit power lower or equal to the module physical internal laser power capability. This is useful for leveling of several transceivers on a DWDM system, to normalize all channels power to the EDFA without the need of individual external optical attenuators. Since each module have its own maximum power capability and the tx-power command has a range from -20 to 3 dBm, it may occur that the physical output power may not match tx-power definition, specially on higher tx-power configuration.

**Hardware restrictions:**

DM4770 16CX supports QSFP-DD only for hundred gigabit ethernet ports 10, 12, 14 and 16. DM4780 16CX 8DX supports QSFP-DD on all four hundred gigabit ports, and on the two hundred gigabit ports 1/1/3, 1/1/4, 1/1/5 and 1/1/6.


### `interface forty-gigabit-ethernet`

> **Página:** 262 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure forty gigabit Ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
interface forty-gigabit-ethernet id [ shutdown | speed { 40G } | duplex { full } | mdix { normal } | flow-control { rx-pause | tx-pause } | mtu { range* } | description { string }* ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Configures the forty-gigabit-ethernet interface. The ID is composed by chassis/slot/port. — *Valores:* chassis/slot/port Chassis, slot and port indexes depends on the specific platform and/or provisioned linecards(if available in the platform). · *Default:* N/A
- `shutdown` — Turn the interface down administratively (the interfaces startup is no shutdown by default). — *Valores:* N/A · *Default:* N/A
- `speed` — Set interface speed (for forty-gigabit-ethernet it is only available 40G). — *Valores:* 40G. · *Default:* 40G.
- `duplex` — Set a duplex mode (for forty-gigabit-ethernet it is only available full mode). — *Valores:* full. · *Default:* full.
- `mdix` — Set MDIX mode (for forty-gigabit-ethernet it is only available normal mode). — *Valores:* normal. · *Default:* normal.
- `flow-control` — Set a flow control mode. — *Valores:* rx-pause and tx-pause. · *Default:* rx-pause and tx-pause.
- `mtu` — Set MTU (Maximum Transmission Unit) in bytes. Packets that surpass the limit are dropped. — *Valores:* From 64 bytes to the maximum supported on the product. · *Default:* The maximum supported on the product.
- `description` — Set a textual description of the interface, according to the network manager’s choice. Valid characters are A-Z, a-z, 0-9 and A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. Parameter ‘advertising-abilities’ was removed. 4.6 The configuration to set the MTU of interfaces was added. |
| 9.0 | Added support for some special characters on interface description. |

**Usage Guidelines:**

This command should be used to configure the forty gigabit Ethernet interfaces. Example: This example is applied to id equal to 1/1/1. This id correspond to chassis 1, slot 1 and port 1. To set flow control DM4170(config)# interface forty-gigabit-ethernet 1/1/1 DM4170(config-forty-gigabit-ethernet-1/1/1)# flow-control rx-pause tx-pause To set description DM4170(config)# interface forty-gigabit-ethernet 1/1/1 DM4170(config-forty-gigabit-ethernet-1/1/1)# description "test interface name" Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example: DM4170(config)# interface forty-gigabit-ethernet 1/1/1 DM4170(config-forty-gigabit-ethernet-1/1/1)# description "test_interface_name|!?;" To set mtu DM4170(config)# interface forty-gigabit-ethernet 1/1/1 DM4170(config-forty-gigabit-ethernet-1/1/1)# mtu 1500

**Impacts and precautions:**

Changes in interfaces configuration could result in link connection loss. The interface description is set using CLI and the maximum number of characters is 128. This description is available in SNMP through IF-MIB::ifAlias, but it is truncated in 64 characters. The MTU configuration considers an Ethernet frame with the maximum headers size of 26 bytes, which is the case for frames tagged with VLAN (4 bytes) and QinQ (4 bytes). Therefore, untagged frames with a payload that exceeds the MTU configuration by at most 8 bytes will not be dropped.

**Hardware restrictions:**

According to SFP+ inserted, these configurations could be available or not.


### `interface four-hundred-g-ethernet`

> **Página:** 266 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure four hundred gigabit Ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
interface four-hundred-g-ethernet id [ shutdown | negotiation | speed { 40G | 100G } | duplex { full } | mdix { normal } | flow-control { rx-pause | tx-pause } | mtu { range } | description { string } | multirate {1x100G | 2x100G | 3x100G | 4x100G | 2x100G-16QAM } | fec { off | cl91 | auto } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Configures the four-hundred-g-ethernet interface. The ID is composed by chassis/slot/port. — *Valores:* chassis/slot/port Chassis, slot and port indexes depends on the specific platform and/or provisioned linecards(if available in the platform). · *Default:* N/A
- `shutdown` — Turn the interface down administratively (the interfaces startup is no shutdown by default). — *Valores:* N/A · *Default:* N/A
- `negotiation` — Enable autonegotiation. — *Valores:* N/A · *Default:* N/A
- `speed` — Set interface speed to 400G, 200G, 100G or 40G. Available only on DM4780 plataform. — *Valores:* 400G, 200G, 100G, 40G. · *Default:* 400G.
- `duplex` — Set a duplex mode (for four-hundred-g-ethernet it is only available full mode). — *Valores:* full. · *Default:* full.
- `mdix` — Set MDIX mode (for four-hundred-g-ethernet it is only available normal mode). — *Valores:* normal. · *Default:* normal.
- `flow-control` — Set a flow control mode. — *Valores:* rx-pause and tx-pause. · *Default:* rx-pause and tx-pause.
- `mtu` — Set MTU (Maximum Transmission Unit) in bytes. Packets that surpass the limit are dropped. — *Valores:* From 64 bytes to the maximum supported on the product. · *Default:* The maximum supported on the product.
- `description` — Set a textual description of the interface, according to the network manager’s choice. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A
- `multirate` — Set the multirate in four-hundred-g-ethernet interface. Available only on the DM4920 plataform. — *Valores:* 1x100G, 2x100G, 3x100G, 4x100G, 2x100G-16QAM · *Default:* 4x100G
- `fec` — Enable/disable Forward Error Correction. — *Valores:* off, cl91, auto. · *Default:* auto.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.4 | This command was introduced. |
| 9.8 | The multirate command was introduced. |
| 12.0 | Introduced the auto option for the fec parameter. |

**Usage Guidelines:**

This command should be used to configure the four hundred gigabit Ethernet interfaces. Example: This example is applied to id equal to 1/2/1. This id correspond to chassis 1, slot 2 and port 1. To set flow control DM4780(config)# interface four-hundred-g-ethernet 1/1/1 DM4780(config-four-hundred-g-ethernet 1/2/1-1/1/1)# flow-control rx-pause tx-pause To set description DM4920(config)# interface four-hundred-g-ethernet 1/2/1 DM4920(config-four-hundred-g-ethernet-1/2/1)# description "test interface name" Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example: DM4920(config)# interface four-hundred-g-ethernet 1/2/1 DM4920(config-four-hundred-g-ethernet-1/2/1)# description "test_interface_name|!?;" To set mtu DM4780(config)# interface four-hundred-g-ethernet 1/1/1 DM4780(config-four-hundred-g-ethernet-1/1/1)# mtu 1500 To set fec DM4780(config)# interface four-hundred-g-ethernet 1/1/1 DM4780(config-four-hundred-g-ethernet-1/1/1)# fec cl91 To set fec auto DM4780(config)# interface four-hundred-g-ethernet 1/1/1 DM4780(config-four-hundred-g-ethernet-1/1/1)# fec auto

**Impacts and precautions:**

Changes in interfaces configuration could result in link connection loss. The interface description is set using CLI and the maximum number of characters is 128. This description is available in SNMP through IF-MIB::ifAlias, but it is truncated in 64 characters. The fec auto mode will automatically set the Rs544 to 400G and 200G speed, CL91 to 100G and off for 40G speed.

**Hardware restrictions:**

The parameters negotiation, speed, duplex, mdix, flow-control, mtu and fec are not available on the DM4920 platform.


### `interface gigabit-ethernet`

> **Página:** 271 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure gigabit Ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
interface gigabit-ethernet id [ shutdown | negotiation | speed { 10M | 100M | 1G } | duplex { full } | mdix { normal | xover | auto } | flow-control { rx-pause | tx-pause } | advertising-abilities { 10Mfull* | 100Mfull | 1Gfull | rx-pause | tx-pause } | mtu { range* } | description { string }* ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Configures the gigabit-ethernet interface. The ID is composed by chassis/slot/port. — *Valores:* chassis/slot/port Chassis, slot and port indexes depends on the specific platform and/or provisioned linecards(if available in the platform). · *Default:* N/A
- `shutdown` — Turn the interface down administratively (the interfaces startup is no shutdown by default). — *Valores:* N/A · *Default:* N/A
- `negotiation` — Enable autonegotiation. — *Valores:* N/A · *Default:* N/A
- `speed` — Set a speed to be used when negotiation is disabled. — *Valores:* 1G, 10M or 100M. · *Default:* 1G for optical ports and 100M for electrical ports.
- `duplex` — Set a duplex mode to be used when negotiation is disabled. — *Valores:* full. · *Default:* full.
- `mdix` — Set MDIX mode to be used when negotiation is disabled. — *Valores:* normal, xover or auto. · *Default:* normal for ports from 1 to 8.
- `auto for ports from 9 to 12. flow-control` — Set a flow control mode to be used when negotiation is disabled. — *Valores:* rx-pause and tx-pause. · *Default:* N/A
- `advertising-abilities` — Set the speed, duplex and flow control modes that will be advertised on negotiation protocol. — *Valores:* 10Mfull, 100Mfull, 1Gfull, rx-pause and tx-pause. · *Default:* 10Mfull, 100Mfull, 1Gfull.
- `mtu` — Set MTU (Maximum Transmission Unit) in bytes. Packets that surpass the limit are dropped. — *Valores:* From 64 bytes to the maximum supported on the product. · *Default:* The maximum supported on the product.
- `description` — Set a textual description of the interface, according to the network manager’s choice. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. Removed the configurations “duplex half”, “advertising-abilities 10Mhalf” 1.10 and “advertising-abilities 100Mhalf”. |
| 1.12 | The configuration to set the description of interfaces was added. |
| 4.6 | The configuration to set the MTU of interfaces was added. |
| 9.0 | Added support for some special characters on interface description. |

**Usage Guidelines:**

This command should be used to configure the gigabit Ethernet interfaces. Examples: These examples are applied to id equal to 1/1/9. This id correspond to chassis 1, slot 1 and port 9. To shutdown port DM4610(config)# interface gigabit-ethernet 1/1/9 DM4610(config-gigabit-ethernet-1/1/9)# shutdown To enable negotiation DM4610(config)# interface gigabit-ethernet 1/1/9 DM4610(config-gigabit-ethernet-1/1/9)# negotiation To set speed equal to 1 gigagit DM4610(config)# interface gigabit-ethernet 1/1/9 DM4610(config-gigabit-ethernet-1/1/9)# speed 1G To set duplex DM4610(config)# interface gigabit-ethernet 1/1/9 DM4610(config-gigabit-ethernet-1/1/9)# duplex full To set advertising abilities DM4610(config)# interface gigabit-ethernet 1/1/9 DM4610(config-gigabit-ethernet-1/1/9)# advertising-abilities 1Gfull rx-pause To set description DM4610(config)# interface gigabit-ethernet 1/1/9 DM4610(config-gigabit-ethernet-1/1/9)# description "test interface name" Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example: DM4610(config)# interface gigabit-ethernet 1/1/9 DM4610(config-gigabit-ethernet-1/1/9)# description "test_interface_name|!?;" To set mtu DM4610(config)# interface gigabit-ethernet 1/1/9 DM4610(config-gigabit-ethernet-1/1/9)# mtu 1500

**Impacts and precautions:**

Changes in interfaces configuration could result in link connection loss. The interface description is set using CLI and the maximum number of characters is 128. This description is available in SNMP through IF-MIB::ifAlias, but it is truncated in 64 characters. The MTU configuration considers an Ethernet frame with the maximum headers size of 26 bytes, which is the case for frames tagged with VLAN (4 bytes) and QinQ (4 bytes). Therefore, untagged frames with a payload that exceeds the MTU configuration by at most 8 bytes will not be dropped.

**Hardware restrictions:**

According to SFP inserted, these configurations could be available or not.


### `interface hundred-gigabit-ethernet`

> **Página:** 276 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure hundred gigabit Ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
interface hundred-gigabit-ethernet id [ shutdown | negotiation | speed { 40G | 100G } | duplex { full } | mdix { normal } | flow-control { rx-pause | tx-pause } | mtu { range } | description { string } | fec { off | cl91 | auto } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Configures the hundred-gigabit-ethernet interface. The ID is composed by chassis/slot/port. — *Valores:* chassis/slot/port Chassis, slot and port indexes depends on the specific platform and/or provisioned linecards(if available in the platform). · *Default:* N/A
- `shutdown` — Turn the interface down administratively (the interfaces startup is no shutdown by default). — *Valores:* N/A · *Default:* N/A
- `negotiation` — Enable autonegotiation. — *Valores:* N/A · *Default:* N/A
- `speed` — Set interface speed to 100G or to 40G. — *Valores:* 40G, 100G. · *Default:* 100G.
- `duplex` — Set a duplex mode (for hundred-gigabit-ethernet it is only available full mode). — *Valores:* full. · *Default:* full.
- `mdix` — Set MDIX mode (for hundred-gigabit-ethernet it is only available normal mode). — *Valores:* normal. · *Default:* normal.
- `flow-control` — Set a flow control mode. — *Valores:* rx-pause and tx-pause. · *Default:* rx-pause and tx-pause.
- `mtu` — Set MTU (Maximum Transmission Unit) in bytes. Packets that surpass the limit are dropped. — *Valores:* From 64 bytes to the maximum supported on the product. · *Default:* The maximum supported on the product.
- `description` — Set a textual description of the interface, according to the network manager’s choice. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A
- `fec` — Enable/disable Forward Error Correction. — *Valores:* off, cl91, auto. · *Default:* off.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 9.0 | Added support for some special characters on interface description. |
| 12.0 | Introduced the auto option for the fec parameter. |

**Usage Guidelines:**

This command should be used to configure the hundred gigabit Ethernet interfaces. Example: This example is applied to id equal to 1/1/1. This id correspond to chassis 1, slot 1 and port 1. To set flow control DM4270(config)# interface hundred-gigabit-ethernet 1/1/1 DM4270(config-hundred-gigabit-ethernet-1/1/1)# flow-control rx-pause tx-pause To set description DM4270(config)# interface hundred-gigabit-ethernet 1/1/1 DM4270(config-hundred-gigabit-ethernet-1/1/1)# description "test interface name" Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example: DM4270(config)# interface hundred-gigabit-ethernet 1/1/1 DM4270(config-hundred-gigabit-ethernet-1/1/1)# description "test_interface_name|!?;" To set mtu DM4270(config)# interface hundred-gigabit-ethernet 1/1/1 DM4270(config-hundred-gigabit-ethernet-1/1/1)# mtu 1500 To set fec DM4270(config)# interface hundred-gigabit-ethernet 1/1/1 DM4270(config-hundred-gigabit-ethernet-1/1/1)# fec cl91 To set fec auto DM4270(config)# interface hundred-gigabit-ethernet 1/1/1 DM4270(config-hundred-gigabit-ethernet-1/1/1)# fec auto

**Impacts and precautions:**

Changes in interfaces configuration could result in link connection loss. The interface description is set using CLI and the maximum number of characters is 128. This description is available in SNMP through IF-MIB::ifAlias, but it is truncated in 64 characters. The MTU configuration considers an Ethernet frame with the maximum headers size of 26 bytes, which is the case for frames tagged with VLAN (4 bytes) and QinQ (4 bytes). Therefore, untagged frames with a payload that exceeds the MTU configuration by at most 8 bytes will not be dropped. The fec auto mode will automatically set the CL91 to 100G speed and off for 40G speed.

**Hardware restrictions:**

According to SFP+ inserted, these configurations could be available or not. In DM4920 platform, the parameters speed, duplex, negotiation, mdix, mtu and flow-control are not available.


### `interface ten-gigabit-ethernet`

> **Página:** 281 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure ten gigabit Ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
interface ten-gigabit-ethernet id [ shutdown | negotiation | speed { 1G | 10G } | duplex { full } | mdix { normal } | flow-control { rx-pause | tx-pause } | advertising-abilities { 1Gfull* | rx-pause | tx-pause } | mtu { range* } | description { string }* ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Configures the ten-gigabit-ethernet interface. The ID is composed by chassis/slot/port. — *Valores:* chassis/slot/port Chassis, slot and port indexes depends on the specific platform and/or provisioned linecards(if available in the platform). · *Default:* N/A
- `shutdown` — Turn the interface down administratively (the interfaces startup is no shutdown by default). — *Valores:* N/A · *Default:* N/A
- `negotiation` — Enable autonegotiation. — *Valores:* N/A · *Default:* N/A
- `speed` — Set interface speed to 1G or to 10G. — *Valores:* 1G, 10G. · *Default:* 10G.
- `duplex` — Set a duplex mode (for ten-gigabit-ethernet is only available full mode). — *Valores:* full. · *Default:* full.
- `mdix` — Set MDIX mode (for ten-gigabit-ethernet is only available normal mode). — *Valores:* normal. · *Default:* normal.
- `flow-control` — Set a flow control mode. — *Valores:* rx-pause and tx-pause. · *Default:* rx-pause and tx-pause.
- `advertising-abilities` — Set the speed, duplex and flow control modes that will be advertised on negotiation protocol. — *Valores:* 10Mfull, 100Mfull, 1Gfull, rx-pause and tx-pause. · *Default:* 10Mfull, 100Mfull, 1Gfull.
- `mtu` — Set MTU (Maximum Transmission Unit) in bytes. Packets that surpass the limit are dropped. — *Valores:* From 64 bytes to the maximum supported on the product. · *Default:* The maximum supported on the product.
- `description` — Set a textual description of the interface, according to the network manager’s choice. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.12 | The configuration to set the description of interfaces was added. |
| 4.6 | The configuration to set the MTU of interfaces was added. |
| 9.0 | Added support for some special characters on interface description. |

**Usage Guidelines:**

This command should be used to configure the ten gigabit Ethernet interfaces. Example: This example is applied to id equal to 1/1/1. This id correspond to chassis 1, slot 1 and port 1. To set flow control DM4610(config)# interface ten-gigabit-ethernet 1/1/1 DM4610(config-ten-gigabit-ethernet-1/1/1)# flow-control rx-pause tx-pause To set description DM4610(config)# interface ten-gigabit-ethernet 1/1/9 DM4610(config-ten-gigabit-ethernet-1/1/9)# description "test interface name" Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example: DM4610(config)# interface ten-gigabit-ethernet 1/1/9 DM4610(config-ten-gigabit-ethernet-1/1/9)# description "test_interface_name|!?;" To set mtu DM4610(config)# interface ten-gigabit-ethernet 1/1/9 DM4610(config-ten-gigabit-ethernet-1/1/9)# mtu 1500

**Impacts and precautions:**

Changes in interfaces configuration could result in link connection loss. The interface description is set using CLI and the maximum number of characters is 128. This description is available in SNMP through IF-MIB::ifAlias, but it is truncated in 64 characters. The MTU configuration considers an Ethernet frame with the maximum headers size of 26 bytes, which is the case for frames tagged with VLAN (4 bytes) and QinQ (4 bytes). Therefore, untagged frames with a payload that exceeds the MTU configuration by at most 8 bytes will not be dropped.

**Hardware restrictions:**

According to SFP+ inserted, these configurations could be available or not.


### `interface twenty-five-g-ethernet`

> **Página:** 285 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure twenty-five gigabit Ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
interface twenty-five-g-ethernet id [ shutdown | speed { 1G | 10G | 25G } | duplex { full } | mdix { normal } | flow-control { rx-pause | tx-pause } | mtu { range } | description { string } | fec { off | cl74 | cl108 } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Configures the twenty-five-g-ethernet interface. The ID is composed by chassis/slot/port. — *Valores:* chassis/slot/port Chassis, slot and port indexes depends on the specific platform and/or provisioned linecards(if available in the platform). · *Default:* N/A
- `shutdown` — Turn the interface down administratively (the interfaces startup is no shutdown by default). — *Valores:* N/A · *Default:* N/A
- `speed` — Set interface speed to 25G, 10G or to 1G. — *Valores:* 1G, 10G, 25G. · *Default:* 25G.
- `duplex` — Set a duplex mode (for twenty-five-g-ethernet it is only available full mode). — *Valores:* full. · *Default:* full.
- `mdix` — Set MDIX mode (for twenty-five-g-ethernet it is only available normal mode). — *Valores:* normal. · *Default:* normal.
- `flow-control` — Set a flow control mode. — *Valores:* rx-pause and tx-pause. · *Default:* rx-pause and tx-pause.
- `mtu` — Set MTU (Maximum Transmission Unit) in bytes. Packets that surpass the limit are dropped. — *Valores:* From 64 bytes to the maximum supported on the product. · *Default:* The maximum supported on the product.
- `description` — Set a textual description of the interface, according to the network manager’s choice. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A
- `fec` — Enable/disable Forward Error Correction. — *Valores:* off, cl74, cl108. · *Default:* off.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |
| 6.0 | The configuration to set FEC CL74 and CL108 was added. |
| 8.0 | Add restriction to avoid use fec cl108 on DM4618 platform. |
| 9.0 | Added support for some special characters on interface description. |
| 10.6 | Added restriction to use speed 1Gb/s on DM4280 platform. |

**Usage Guidelines:**

This command should be used to configure the twenty-five gigabit Ethernet interfaces. Example: This example is applied to id equal to 1/1/1. This id correspond to chassis 1, slot 1 and port 1. To set flow control DM4770(config)# interface twenty-five-g-ethernet 1/1/1 DM4770(config-twenty-five-g-ethernet-1/1/1)# flow-control rx-pause tx-pause To set description DM4770(config)# interface twenty-five-g-ethernet 1/1/1 DM4770(config-twenty-five-g-ethernet-1/1/1)# description "test interface name" Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example: DM4770(config)# interface twenty-five-g-ethernet 1/1/1 DM4770(config-twenty-five-g-ethernet-1/1/1)# description "test_interface_name|!?;" To set mtu DM4770(config)# interface twenty-five-g-ethernet 1/1/1 DM4770(config-twenty-five-g-ethernet-1/1/1)# mtu 1500 To set fec DM4770(config)# interface twenty-five-g-ethernet 1/1/1 DM4770(config-twenty-five-g-ethernet-1/1/1)# fec cl74

**Impacts and precautions:**

Changes in interfaces configuration could result in link connection loss. The interface description is set using CLI and the maximum number of characters is 128. This description is available in SNMP through IF-MIB::ifAlias, but it is truncated in 64 characters. The MTU configuration considers an Ethernet frame with the maximum headers size of 26 bytes, which is the case for frames tagged with VLAN (4 bytes) and QinQ (4 bytes). Therefore, untagged frames with a payload that exceeds the MTU configuration by at most 8 bytes will not be dropped.

**Hardware restrictions:**

According to SFP+ inserted, these configurations could be available or not. DM4618 platform doesn’t support FEC CL108, instead, use cl74. DM4280 platform doesn’t support speed 1Gb/s.


### `interface two-hundred-g-ethernet`

> **Página:** 289 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure two hundred gigabit Ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
interface two-hundred-g-ethernet id [ shutdown | negotiation | speed { 200G } | duplex { full } | mdix { normal } | flow-control { rx-pause | tx-pause } | mtu { range } | description { string } | fec { off | cl91 | auto } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Configures the two-hundred-g-ethernet interface. The ID is composed by chassis/slot/port. — *Valores:* chassis/slot/port Chassis, slot and port indexes depends on the specific platform and/or provisioned linecards(if available in the platform). · *Default:* N/A
- `shutdown` — Turn the interface down administratively (the interfaces startup is no shutdown by default). — *Valores:* N/A · *Default:* N/A
- `negotiation` — Enable autonegotiation. — *Valores:* N/A · *Default:* N/A
- `speed` — Set interface speed to 200G. — *Valores:* 200G. · *Default:* 200G.
- `duplex` — Set a duplex mode (for two-hundred-g-ethernet it is only available full mode). — *Valores:* full. · *Default:* full.
- `mdix` — Set MDIX mode (for two-hundred-g-ethernet it is only available normal mode). — *Valores:* normal. · *Default:* normal.
- `flow-control` — Set a flow control mode. — *Valores:* rx-pause and tx-pause. · *Default:* rx-pause and tx-pause.
- `mtu` — Set MTU (Maximum Transmission Unit) in bytes. Packets that surpass the limit are dropped. — *Valores:* From 64 bytes to the maximum supported on the product. · *Default:* The maximum supported on the product.
- `description` — Set a textual description of the interface, according to the network manager’s choice. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A
- `fec` — Enable/disable Forward Error Correction. — *Valores:* off, cl91, auto. · *Default:* auto.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.4 | This command was introduced. |
| 12.0 | Introduced the auto option for the fec parameter. |

**Usage Guidelines:**

This command should be used to configure the two hundred gigabit Ethernet interfaces. Example: This example is applied to id equal to 1/1/1. This id correspond to chassis 1, slot 1 and port 1. To set flow control DM4780(config)# interface two-hundred-g-ethernet 1/1/1 DM4780(config-two-hundred-g-ethernet-1/1/1)# flow-control rx-pause tx-pause To set description DM4780(config)# interface two-hundred-g-ethernet 1/1/1 DM4780(config-two-hundred-g-ethernet-1/1/1)# description "test interface name" Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example: DM4780(config)# interface two-hundred-g-ethernet 1/1/1 DM4780(config-two-hundred-g-ethernet-1/1/1)# description "test_interface_name|!?;" To set mtu DM4780(config)# interface two-hundred-g-ethernet 1/1/1 DM4780(config-two-hundred-g-ethernet-1/1/1)# mtu 1500 To set fec auto DM4780(config)# interface two-hundred-g-ethernet 1/1/1 DM4780(config-two-hundred-g-ethernet-1/1/1)# fec auto

**Impacts and precautions:**

This interface is under development. The fec auto mode will automatically set the Rs544 to 200G speed, CL91 to 100G and off for 40G speed.

**Hardware restrictions:**

N/A


### `show dwdm channels`

> **Página:** 293 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows DWDM QSFP tabular information about channels, frequency and wavelength.

**Supported Platforms:** This command is supported only in the following platforms: DM4770, DM4920.

**Syntax:**

```text
show dwdm channels
```

**Parameters:**

- `show dwdm channels` — Show information about the channels, wavelengths and frequencies. — *Valores:* None · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 7.0 | This command was introduced. |

**Usage Guidelines:**

Examples: Show the DWDM table channels

```text
DM4770# show dwdm channels
CHANNEL FREQUENCY WAVELENGTH
(ID) (THz) (nm)
--------------------------------
13 191.3 1567.13
14 191.4 1567.19
...
```

**Output Terms:**

Output Description CHANNEL (ID) Identification of the channel FREQUENCY (THz) Value of the channel frequency measured in THz WAVELENGTH (nm) Value of the channel wavelength measured in nm

**Impacts and precautions:**

N/A

**Hardware restrictions:**

DM4770 16CX supports QSFP-DD only for hundred gigabit ethernet ports 10, 12, 14 and 16. DM4770 32CX does not support this command.


### `show interface description`

> **Página:** 295 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Description of interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface description interface-type
```

**Parameters:**

- `interface-type` — Interface type to filter. — *Valores:* { gigabit-ethernet | ten-gigabit-ethernet | twenty-five-g-ethernet | forty-gigabit-ethernet | hundred-gigabit-ethernet | two-hundred-g-ethernet | four-hundred-g-ethernet } · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |

**Usage Guidelines:**

Use this command to display an overview of all interfaces; Example:

```text
# show interface description
```

Gigabit Ethernet Interfaces: CHASSIS ID/SLOT ID/PORT ID Description -------------------------------------------- 1/1/1 My_pretty_name_for_this_interface 1/1/2 LINK_X 1/1/3 - 1/1/4 - 1/1/5 - 1/1/6 - 1/1/7 - 1/1/8 - 1/1/9 - 1/1/10 - 1/1/11 - 1/1/12 - 1/1/13 - 1/1/14 - 1/1/15 - 1/1/16 - 1/1/17 - 1/1/18 - 1/1/19 - 1/1/20 - 1/1/21 - 1/1/22 - 1/1/23 - 1/1/24 - Ten Gigabit Ethernet Interfaces: ID/SLOT ID/PORT ID Description ------------------------------ 1/1/1 A_short_description 1/1/2 - 1/1/3 - 1/1/4 - Forty Gigabit Ethernet Interfaces: ID/SLOT ID/PORT ID Description ---------------------- 1/1/1 UPLINK 1/1/2 -

**Output Terms:**

Output Description CHASSIS ID/SLOT Interface id referencing chassis/slot/port respectively. ID/ PORT ID The textual description of the interface, according to the network Description manager’s choice.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show interface forty-gigabit-ethernet`

> **Página:** 298 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display status and configuration of forty-gigabit-ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface forty-gigabit-ethernet id
```

**Parameters:**

- `id` — Interface id referencing chassis/slot/port respectively. — *Valores:* chassis/slot/port · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. The fields ‘Last physical up time’ and ‘Last physical down time’ were 10.0 introduced. |
| 10.4 | The field ‘SNMP ifIndex’ was introduced. |

**Usage Guidelines:**

Use this command to display status and configuration of forty-gigabit-ethernet interfaces. Example:

```text
DM4270# show interface forty-gigabit-ethernet 1/1/1
interface forty-gigabit-ethernet 1/1/1
```

Configuration: -------------- Port admin : Enabled Negotiation : Disabled Speed : 40G Duplex : full Flow-Control : Disabled MDIX : normal MTU : 12262 Status: ------- Link Status : Up Speed/Duplex : 40Gfull Flow Control : Disabled MDIX : Normal Last physical up time : 2024-09-10 09:07:09 UTC-3 Last physical down time: 2024-09-10 09:00:15 UTC-3

**Output Terms:**

Output Description Port admin The configured administrative state. Negotiation The configured autonegotiation mode. Speed The configured speed mode. Duplex The configured duplex mode. Flow-Control The configured flow control mode. Output Description MDIX The configuration and status of MDIX mode. MTU The configured MTU (Maximum Transmission Unit) in bytes. Description The configured textual description of the interface. Link status The current interface link state (Up/Down). Speed/Duplex The current speed/duplex state. Flow Control The current flow control state. SNMP ifIndex The ifIndex used for SNMP requests for the interface. Last physical up Timestamp indicating the most recent moment the interface was time confirmed operational. Last physical down Timestamp indicating the most recent moment the interface ceased time operation.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show interface four-hundred-g-ethernet`

> **Página:** 301 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display status and configuration of four-hundred-g-ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface four-hundred-g-ethernet id
```

**Parameters:**

- `id` — Interface id referencing chassis/slot/port respectively. — *Valores:* chassis/slot/port · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.4 | This command was introduced. The fields ‘Last physical up time’ and ‘Last physical down time’ were |
| 10.0 | introduced. The fields ‘Multirate" and ’Channels status’ were introduced. |
| 10.4 | The field ‘SNMP ifIndex’ was introduced. |

**Usage Guidelines:**

Use this command to display status and configuration of four-hundred-g-ethernet interfaces. Example:

```text
DM4920# show interface four-hundred-g-ethernet 1/2/1
interface four-hundred-g-ethernet 1/2/1
```

Configuration: -------------- Port admin : Enabled Negotiation : Disabled Speed : Duplex : Flow-Control : Disabled MDIX : FEC : off MTU : 16361 Multirate : 4x100G Description : Status: ------- Link Status : Up Channels Status : ch1 : Up ch2 : Up ch3 : Up ch4 : Up Speed/Duplex : 400Gfull Flow Control : Disabled MDIX : Normal Last physical up time : 2024-09-10 09:07:09 UTC-3 Last physical down time: 2024-09-10 09:00:15 UTC-3 Example:

```text
DM4780# show interface four-hundred-g-ethernet 1/1/1
interface four-hundred-g-ethernet 1/1/1
```

Configuration: -------------- Port admin : Enabled Negotiation : Disabled Speed : 400G Duplex : full Flow-Control : Disabled MDIX : normal FEC : auto MTU : 9390 Description : Status: ------- Link Status : Up Speed/Duplex : 400Gfull Flow Control : [ RX-Pause TX-Pause ] MDIX : Normal Last physical up time : 2025-12-19 19:26:43 UTC-3 Last physical down time: 2025-12-19 19:26:42 UTC-3

**Output Terms:**

Output Description Port admin The configured administrative state. Negotiation The configured autonegotiation mode. Speed The configured speed mode. Duplex The configured duplex mode. Flow-Control The configured flow control mode. Output Description MDIX The configuration and status of MDIX mode. FEC The configured FEC (Forward Error Correction) mode. MTU The configured MTU (Maximum Transmission Unit) in bytes. Multirate The configured Multirate mode. Description The configured textual description of the interface. Link status The current interface link state (Up/Down). Channels Status The current interface link state per-channel (Up/Down) Speed/Duplex The current speed/duplex state. Flow Control The current flow control state. SNMP ifIndex The ifIndex used for SNMP requests for the interface. Last physical up Timestamp indicating the most recent moment the interface was time confirmed operational. Last physical down Timestamp indicating the most recent moment the interface ceased time operation.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

As some platforms don’t have some parameters on configuration, these parameters can appear as empty here.


### `show interface gigabit-ethernet`

> **Página:** 305 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display status and configuration of gigabit-ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface gigabit-ethernet id
```

**Parameters:**

- `id` — Interface id referencing chassis/slot/port respectively. — *Valores:* chassis/slot/port · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. The fields ‘Last physical up time’ and ‘Last physical down time’ were 10.0 introduced. |
| 10.4 | The field ‘SNMP ifIndex’ was introduced. |

**Usage Guidelines:**

Use this command to display status and configuration of gigabit-ethernet interfaces. Example:

```text
DM4050# show interface gigabit-ethernet 1/1/24
interface gigabit-ethernet 1/1/24
```

Configuration: -------------- Port admin : Enabled Negotiation : Enabled Advertising Abilities : [ 10Mfull 100Mfull 1Gfull ] MDIX : auto MTU : 16338 Status: ------- Link Status : Up Speed/Duplex : 1Gfull Flow Control : Disabled MDIX : Xover Last physical up time : 2024-09-10 09:07:09 UTC-3 Last physical down time: 2024-09-10 09:00:15 UTC-3

**Output Terms:**

Output Description Port admin The configured administrative state. Negotiation The configured autonegotiation mode. Advertising The configured advertising abilities. Abilities MDIX The configuration and status of MDIX mode. MTU The configured MTU (Maximum Transmission Unit) in bytes. Output Description Description The configured textual description of the interface. Link status The current interface link state (Up/Down). Speed/Duplex The current speed/duplex state. Flow Control The current flow control state. SNMP ifIndex The ifIndex used for SNMP requests for the interface. Last physical up Timestamp indicating the most recent moment the interface was time confirmed operational. Last physical down Timestamp indicating the most recent moment the interface ceased time operation.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show interface hundred-gigabit-ethernet`

> **Página:** 308 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display status and configuration of hundred-gigabit-ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface hundred-gigabit-ethernet id
```

**Parameters:**

- `id` — Interface id referencing chassis/slot/port respectively. — *Valores:* chassis/slot/port · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. The fields ‘Last physical up time’ and ‘Last physical down time’ were 10.0 introduced. |
| 10.4 | The field ‘SNMP ifIndex’ was introduced. |

**Usage Guidelines:**

Use this command to display status and configuration of hundred-gigabit-ethernet interfaces. Example:

```text
DM4270# show interface hundred-gigabit-ethernet 1/1/1
interface hundred-gigabit-ethernet 1/1/1
```

Configuration: -------------- Port admin : Enabled Negotiation : Disabled Speed : 100G Duplex : full Flow-Control : Disabled MDIX : normal FEC : off MTU : 12262 Status: ------- Link Status : Up Speed/Duplex : 100Gfull Flow Control : Disabled MDIX : Normal Last physical up time : 2024-09-10 09:07:09 UTC-3 Last physical down time: 2024-09-10 09:00:15 UTC-3

**Output Terms:**

Output Description Port admin The configured administrative state. Negotiation The configured autonegotiation mode. Speed The configured speed mode. Duplex The configured duplex mode. Flow-Control The configured flow control mode. Output Description MDIX The configuration and status of MDIX mode. FEC The configured FEC (Forward Error Correction) mode. MTU The configured MTU (Maximum Transmission Unit) in bytes. Description The configured textual description of the interface. Link status The current interface link state (Up/Down). Speed/Duplex The current speed/duplex state. Flow Control The current flow control state. SNMP ifIndex The ifIndex used for SNMP requests for the interface. Last physical up Timestamp indicating the most recent moment the interface was time confirmed operational. Last physical down Timestamp indicating the most recent moment the interface ceased time operation.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show interface link`

> **Página:** 311 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Overview of interfaces status.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface link interface-type
```

**Parameters:**

- `interface-type` — Interface type to filter. — *Valores:* { gigabit-ethernet | ten-gigabit-ethernet | twenty-five-g-ethernet | forty-gigabit-ethernet | hundred-gigabit-ethernet | two-hundred-g-ethernet | four-hundred-g-ethernet } · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.7 | This command was introduced. Added Speed/Duplex information. Interface type was added as parameters, in order to filters the output. 4.8 Removed Disabled column. |
| 5.0 | Added support to 25G. |
| 5.2 | Added information of which protocols blocked interfaces. |
| 9.4 | Added support to 400G. |
| 10.6 | Added support to 200G. |

**Usage Guidelines:**

Use this command to display an overview of all interfaces; Example:

```text
# show interface link
```

Gigabit Ethernet Interfaces: CHASSIS ID/SLOT ID/PORT Disabled Blocked Parent ID Link Shutdown Speed Duplex by by LAG ------------------------------------------------------------------- 1/1/1 Down false - - [ LAG ] - lag-1 1/1/2 Down false - - - - - 1/1/3 Down false - - - - - 1/1/4 Down false - - - - - 1/1/5 Down false - - - - - 1/1/6 Down false - - - - - 1/1/7 Down false - - - - - 1/1/8 Down false - - - - - 1/1/9 Down false - - - - - 1/1/10 Down false - - - - - 1/1/11 Down false - - - - - 1/1/12 Down false - - - - - 1/1/13 Down false - - - - - 1/1/14 Down false - - [ LAG ] - lag-1 1/1/15 Down false - - [ LAG ] - lag-1 1/1/16 Up false 1G full - [ LBD ] - 1/1/17 Down false - - - - - 1/1/18 Up false 1G full - - - 1/1/19 Down false - - - - - 1/1/20 Up false 1G full - [ CFM ] - 1/1/21 Down false - - - - - 1/1/22 Down false - - - - - 1/1/23 Down false - - - - - 1/1/24 Down false - - - - - Ten Gigabit Ethernet Interfaces: CHASSIS ID/SLOT ID/PORT Disabled Blocked Parent ID Link Shutdown Speed Duplex by by LAG ------------------------------------------------------------------- 1/1/1 Down false - - [ LAG ] - lag-2 1/1/2 Down false - - - - - 1/1/3 Down false - - - - - 1/1/4 Down false - - [ LAG ] - lag-2 Forty Gigabit Ethernet Interfaces: CHASSIS ID/SLOT ID/PORT Disabled Blocked Parent ID Link Shutdown Speed Duplex by by LAG ----------------------------------------------------------------------- 1/1/1 Up false 40G full - [ EFM,CFM ] - 1/1/2 Up false 40G full - - -

**Output Terms:**

Output Description CHASSIS ID/SLOT Interface id referencing chassis/slot/port respectively. ID/ PORT ID Link The current interface link state (Up/Down). Shutdown The configured administrative state. Speed The current speed state. Output Description Duplex The current duplex state. Disabled by Protocol name that is disabling the port. Blocked by Names of protocols blocking the port. Parent LAG LAG ID, if the port belongs to any LAG.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show interface ten-gigabit-ethernet`

> **Página:** 315 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display status and configuration of ten-gigabit-ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface ten-gigabit-ethernet id
```

**Parameters:**

- `id` — Interface id referencing chassis/slot/port respectively. — *Valores:* chassis/slot/port · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. The fields ‘Last physical up time’ and ‘Last physical down time’ were 10.0 introduced. |
| 10.4 | The field ‘SNMP ifIndex’ was introduced. |

**Usage Guidelines:**

Use this command to display status and configuration of ten-gigabit-ethernet interfaces. Example:

```text
DM4270# show interface ten-gigabit-ethernet 1/1/2
interface ten-gigabit-ethernet 1/1/2
```

Configuration: -------------- Port admin : Enabled Negotiation : Disabled Speed : 10G Duplex : full Flow-Control : Disabled MDIX : normal MTU : 12262 Status: ------- Link Status : Up Speed/Duplex : 10Gfull Flow Control : Disabled MDIX : Normal Last physical up time : 2024-09-10 09:07:09 UTC-3 Last physical down time: 2024-09-10 09:00:15 UTC-3

**Output Terms:**

Output Description Port admin The configured administrative state. Negotiation The configured autonegotiation mode. Speed The configured speed mode. Duplex The configured duplex mode. Flow-Control The configured flow control mode. Output Description MDIX The configuration and status of MDIX mode. MTU The configured MTU (Maximum Transmission Unit) in bytes. Description The configured textual description of the interface. Link status The current interface link state (Up/Down). Speed/Duplex The current speed/duplex state. Flow Control The current flow control state. SNMP ifIndex The ifIndex used for SNMP requests for the interface. Last physical up Timestamp indicating the most recent moment the interface was time confirmed operational. Last physical down Timestamp indicating the most recent moment the interface ceased time operation.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show interface twenty-five-g-ethernet`

> **Página:** 318 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display status and configuration of twenty-five-g-ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface twenty-five-g-ethernet id
```

**Parameters:**

- `id` — Interface id referencing chassis/slot/port respectively. — *Valores:* chassis/slot/port · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |
| 6.0 | Added support to FEC CL74 and CL108. The fields ‘Last physical up time’ and ‘Last physical down time’ were 10.0 introduced. |
| 10.4 | The field ‘SNMP ifIndex’ was introduced. |

**Usage Guidelines:**

Use this command to display status and configuration of twenty-five-g-ethernet interfaces. Example:

```text
DM4665# show interface twenty-five-g-ethernet 1/1/1
interface twenty-five-g-ethernet 1/1/1
```

Configuration: -------------- Port admin : Enabled Negotiation : Disabled Speed : 25G Duplex : full Flow-Control : Disabled MDIX : normal FEC : off MTU : 12262 Status: ------- Link Status : Up Speed/Duplex : 25Gfull Flow Control : Disabled MDIX : Normal Last physical up time : 2024-09-10 09:07:09 UTC-3 Last physical down time: 2024-09-10 09:00:15 UTC-3

**Output Terms:**

Output Description Port admin The configured administrative state. Negotiation The configured autonegotiation mode. Speed The configured speed mode. Duplex The configured duplex mode. Flow-Control The configured flow control mode. Output Description MDIX The configuration and status of MDIX mode. FEC The configured FEC (Forward Error Correction) mode. MTU The configured MTU (Maximum Transmission Unit) in bytes. Description The configured textual description of the interface. Link status The current interface link state (Up/Down). Speed/Duplex The current speed/duplex state. Flow Control The current flow control state. SNMP ifIndex The ifIndex used for SNMP requests for the interface. Last physical up Timestamp indicating the most recent moment the interface was time confirmed operational. Last physical down Timestamp indicating the most recent moment the interface ceased time operation.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show interface two-hundred-g-ethernet`

> **Página:** 322 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display status and configuration of two-hundred-g-ethernet interfaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface two-hundred-g-ethernet id
```

**Parameters:**

- `id` — Interface id referencing chassis/slot/port respectively. — *Valores:* chassis/slot/port · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.4 | This command was introduced. |

**Usage Guidelines:**

Use this command to display status and configuration of two-hundred-g-ethernet interfaces. Example:

```text
DM4780# show interface two-hundred-g-ethernet 1/1/1
interface two-hundred-g-ethernet 1/1/1
```

Configuration: -------------- Port admin : Enabled Negotiation : Disabled Speed : 200G Duplex : full Flow-Control : Disabled MDIX : normal FEC : auto MTU : 12262 Status: ------- Link Status : Up Speed/Duplex : 200Gfull Flow Control : Disabled MDIX : Normal Last physical up time : 2024-09-10 09:07:09 UTC-3 Last physical down time: 2024-09-10 09:00:15 UTC-3

**Output Terms:**

Output Description Port admin The configured administrative state. Negotiation The configured autonegotiation mode. Speed The configured speed mode. Duplex The configured duplex mode. Flow-Control The configured flow control mode. Output Description MDIX The configuration and status of MDIX mode. FEC The configured FEC (Forward Error Correction) mode. MTU The configured MTU (Maximum Transmission Unit) in bytes. Description The configured textual description of the interface. Link status The current interface link state (Up/Down). Speed/Duplex The current speed/duplex state. Flow Control The current flow control state. SNMP ifIndex The ifIndex used for SNMP requests for the interface. Last physical up Timestamp indicating the most recent moment the interface was time confirmed operational. Last physical down Timestamp indicating the most recent moment the interface ceased time operation.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A L3 This topic describes the commands related to management of L3 logical interfaces such as commands to configure IP address and bind it to lower layer interface, e.g., VLAN.


## L3

### `interface l3`

> **Página:** 325 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures L3 logical interfaces.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
interface l3 if-name [ description if-description | ipv4 address { a.b.c.d/x | secondary a.b.c.d/x } | ipv6 { enable | address x:x:x:x::x/y [ eui-64 ] | ip-mtu mtu-size | nd ra { lifetime | max-interval | min-interval | mtu suppress | prefix x:x:x:x::x/y [ no-advertise | no-autoconfig | off-link ] | suppress } } | lower-layer-if if-type if-id | vlan-link-detect { enabled | disabled } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `if-name` — Specifies the name of the interface. — *Valores:* Must be a valid string. · *Default:* N/A
- `description if-description` — Specifies the description of the interface. It may point out a more meaningful text about its purpose. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* Must be a valid string. · *Default:* N/A
- `ipv4 address a.b.c.d/x` — Specifies an IPv4 address and prefix length, in CIDR notation, to be assigned to logical interface. — *Valores:* a.b.c.d/x. · *Default:* N/A
- `ipv4 address secondary a.b.c.d/x` — Specifies a secondary IPv4 address and prefix length, in CIDR notation, to be assigned to logical interface. — *Valores:* a.b.c.d/x. · *Default:* N/A
- `ipv6 enable` — Enables/Disables IPv6 on the L3 interface. When enabled, the system automatically configures an IPv6 link-local address to the L3 interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 address x:x:x:x::x/y` — Specifies an IPv6 unicast address and prefix length to be assigned to logical interface. — *Valores:* x:x:x:x::x/y. · *Default:* N/A
- `eui-64` — Sets 64-bit Extended Unique Identifier for specific IPv6 prefix on logical interface. — *Valores:* N/A · *Default:* Disabled.
- `ip-mtu mtu-size` — Specifies the Control Plane IP MTU size of the interface. — *Valores:* 68-9198. · *Default:* 1500
- `lower-layer-if if-type` — Specifies the lower layer interface type to be associated to logical interface. — *Valores:* { vlan } · *Default:* N/A
- `if-id` — Specifies the identifier associated to lower-layer-if if-type selected. — *Valores:* ID of a configured VLAN. · *Default:* N/A
- `vlan-link-detect enabled` — Enables VLAN link detection on the L3 interface. — *Valores:* N/A · *Default:* N/A
- `vlan-link-detect disabled` — Disables VLAN link detection on the L3 interface. — *Valores:* N/A · *Default:* N/A
- `ipv6 nd ra suppress` — Suppresses Router Advertisements on the L3 interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 nd ra prefix x:x:x:x::x/y` — Prefix Address to be advertised on the specified L3 interface. — *Valores:* x:x:x:x::x/y. · *Default:* N/A
- `ipv6 nd ra prefix x:x:x:x::x/y no-advertise` — Disables this prefix on Router Advertisement of this L3 interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 nd ra prefix x:x:x:x::x/y no-autoconfig` — Disables auto configuration of hosts by this L3 interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 nd ra prefix x:x:x:x::x/y off-link` — When disabled, indicates that this prefix can be used for on-link determination on L3 interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 nd ra lifetime lifetime` — Sets Router Advertisement lifetime of this L3 interface. — *Valores:* Must be either zero or between max-interval and 9000 seconds. · *Default:* 1800
- `ipv6 nd ra max-interval max-interval` — The maximum time allowed between sending unsolicited multicast router advertisements from the interface, in seconds. — *Valores:* Must be no less than 4 seconds and no greater than 1800 seconds. · *Default:* 600
- `ipv6 nd ra min-interval min-interval` — The minimum time allowed between sending unsolicited multicast router advertisements from the interface, in seconds. — *Valores:* Must be no less than 3 seconds and no greater than 0.75 * MaxRtrAdvInterval. · *Default:* 198
- `ipv6 nd ra mtu suppress` — Suppresses Router Advertisement’s MTU option. — *Valores:* N/A · *Default:* Enabled.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. |
| 2.2 | VLAN link detect support. |
| 2.4 | IPv6 support. |
| 4.5.0 | Support for secondary IPv4 address. |
| 4.8.0 | Support for IPv6 ND Router Advertisement. Support for MTU configuration. 4.9.0 Support for IPv6 ND RA MTU option suppression. |
| 6.2 | Maximum IP MTU value was increased to 9198. Support for more than one IPv4 secondary address per l3 interface on 9.8 platforms that had this limitation. |

**Usage Guidelines:**

The name of L3 logical interface must be unique across interfaces and it will be used as key to be referenced from other features. It is possible the use of one primary IPv4 address, up to three secondary IPv4 addresses and two IPv6 addresses per L3 logical interface. The products DM4360, DM4370, DM4376, DM4378, DM4611, DM4612 and DM4616 support up to 256 secondary IPv4 addresses across all L3 logical interfaces. Command to configure IPv6 addresses will be available only if ipv6 enable is set for interface. Example below shows that IPv6 address configuration option appears after ipv6 enable is set.

```text
(config-l3-test)# ipv6 ?
```

Possible completions: enable Enable IPv6 on interface

```text
!
(config-l3-test)# ipv6 enable
!
(config-l3-test)# ipv6 ?
```

Possible completions: address IPv6 address enable Enable IPv6 on interface

```text
!
```

Currently it is only possible to associate the logical interface with lower layer of type VLAN. To find which L3 logical interface is configured with a specific IPv4 address or a specific VLAN ID, it is possible to use the commands showed in the example below. Example: This example shows how to find an L3 logical interface using an IPv4 address as parameter:

```text
# show running-config interface l3 | include -b 2 192.168.1.1
5-interface l3 example2
6- lower-layer-if vlan 200
7: ipv4 address 192.168.1.1/24
```

Or in configuration mode:

```text
(config)# show interface l3 | include -b 2 192.168.1.1
5-interface l3 example2
6- lower-layer-if vlan 200
7: ipv4 address 192.168.1.1/24
```

This example shows how to find an L3 logical interface using a VLAN ID as parameter:

```text
# show running-config interface l3 | include -b 1 -a 1 "vlan 300"
9-interface l3 example3
10: lower-layer-if vlan 300
11- ipv4 address 192.168.2.1/24
```

Or in configuration mode:

```text
(config)# show interface l3 | include -b 1 -a 1 "vlan 300"
9-interface l3 example3
10: lower-layer-if vlan 300
11- ipv4 address 192.168.2.1/24
```

**Impacts and precautions:**

The ip-mtu is restricted to control plane. Therefore, it does not have any effect on the data plane.

**Hardware restrictions:**

N/A


### `interface l3 vrf`

> **Página:** 332 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures VRF on L3 logical interfaces.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface l3 if-name vrf vrf-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `if-name` — Specifies the name of the interface. — *Valores:* Must be a valid string. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this interface will be associated with. It is not possible to associate the VRF ‘mgmt’ to an L3 interface. Also, the VRF ‘global’ cannot be directly configured as it is the default VRF when no VRF is associated. — *Valores:* string. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 5.12 | Introduced VRF support on L3 interfaces with IPv6. |

**Usage Guidelines:**

If no VRF is explicitly associated with the L3 interface, it is associated with the global VRF by default. The following example shows how to associate an L3 interface with the ‘test_vrf’ VRF:

```text
(config-l3-vlan100)# ?
```

Possible completions: vrf Assign a VRF instance to the interface

```text
!
(config-l3-vlan100)# vrf ?
```

Possible completions: <WORD> VPN Routing/Forwarding instance name test_vrf

```text
!
(config-l3-vlan100)# vrf test_vrf
(config-l3-vlan100)# commit
```

Commit complete.

**Impacts and precautions:**

Once the VRF associated with an L3 interface is changed, any route in the previous VRF using it as output interface will be uninstalled. In order to keep the connectivity, you will need to configure the routes in the new VRF.

**Hardware restrictions:**

N/A


### `show ip interface`

> **Página:** 335 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows the list of interfaces configured with IPv4 addresses and associated information.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show ip interface [vrf {<vrf-name> | all}] { brief }
```

**Parameters:**

- `vrf vrf-name` — Specifies the name of the VRF to filter displayed information. — *Valores:* Name of VRF to display information · *Default:* N/A
- `brief` — Displays brief information about IPv4 addresses associated with each interface and its status. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 4.5.0 | Added Type column. |

**Usage Guidelines:**

To simply show the global IPv4 interfaces, the following command can be used: Example:

```text
# show ip interface brief
```

Type Codes: P - primary, S - secondary, V - VRRP virtual address VRF-name Interface-name Logical-interface Address Type State --------------------------------------------------------------------------- global mgmt 1/1/1 mgmt-1/1/1 192.168.0.1/24 P active global loopback 0 loopback 0 192.168.1.1/24 P active global intf_l3_1 l3-vlan 10 192.168.10.10/24 P active global intf_l3_1 l3-vlan 10 192.168.10.11/24 S active global intf_l3_5 l3-vlan 50 192.168.50.50/24 PV active global intf_l3_6 l3-vlan 60 192.168.60.60/24 P active global intf_l3_6 l3-vlan 60 192.168.60.61/24 V active To show interfaces configured with IPv4 addresses in all VRFs, the following command can be used: Example:

```text
# show ip interface vrf all brief
```

Type Codes: P - primary, S - secondary, V - VRRP virtual address VRF-name Interface-name Logical-interface Address Type State --------------------------------------------------------------------------- global mgmt 1/1/1 mgmt-1/1/1 192.168.0.1/24 P active global loopback 0 loopback 0 192.168.1.1/24 P active global intf_l3_1 l3-vlan 10 192.168.10.10/24 P active global intf_l3_5 l3-vlan 50 192.168.50.50/24 PV active global intf_l3_6 l3-vlan 60 192.168.60.60/24 P active global intf_l3_6 l3-vlan 60 192.168.60.61/24 V active GREEN intf_l3_2 l3-vlan 20 192.168.20.20/24 P active GREEN intf_l3_3 l3-vlan 30 192.168.30.30/24 P active RED intf_l3_4 l3-vlan 40 192.168.40.40/24 P active To show interfaces configured with IPv4 addresses in a specific VRF, the following command can be used: Example:

```text
# show ip interface vrf GREEN brief
```

Type Codes: P - primary, S - secondary, V - VRRP virtual address VRF-name Interface-name Logical-interface Address Type State --------------------------------------------------------------------------- GREEN intf_l3_2 l3-vlan 20 192.168.20.20/24 P active GREEN intf_l3_3 l3-vlan 30 192.168.30.30/24 P active

**Output Terms:**

Output Description VRF name Displays the VRF name. Interface name Displays the interface name. Output Description Logical interface Displays the logical interface. Address Displays the IPv4 addresses. Type of IPv4 address. Type Codes: P - primary, S - secondary, V - Type VRRP virtual address. State Displays the state of IPv4 addresses.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ipv6 interface`

> **Página:** 339 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows the list of interfaces configured with IPv6 addresses and associated information.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show ipv6 interface [vrf {<vrf-name> | all}] { brief }
```

**Parameters:**

- `vrf vrf-name` — Specifies the name of the VRF to filter displayed information. — *Valores:* Name of VRF to display information · *Default:* N/A
- `brief` — Displays brief information about IPv6 addresses associated with each interface and its status. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 2.4 | IPv6 support. |
| 5.12 | Introduced VRF support. |

**Usage Guidelines:**

To simply show the IPv6 interface brief, the following command can be used: Example:

```text
# show ipv6 interface brief
```

VRF-name Interface-name Logical-interface Address Scope State ---------------------------------------------------------------------------------------------- global intf_l3_1 l3-vlan 300 fe80::204:dfff:feb3:f42a/64 link-local active global intf_l3_1 l3-vlan 300 fd01::1/16 global active To show interfaces configured with IPv6 addresses in all VRFs, the following command can be used: Example:

```text
# show ipv6 interface vrf all brief
```

VRF-name Interface-name Logical-interface Address Scope State ---------------------------------------------------------------------------------------------- global intf_l3_1 l3-vlan 300 fe80::204:dfff:feb3:f42a/64 link-local active global intf_l3_1 l3-vlan 300 fd01::1/16 global active green intf_l3_2 l3-vlan 400 fe80::204:dfff:feb3:f42a/64 link-local active green intf_l3_2 l3-vlan 400 fd02::1/16 global active To show interfaces configured with IPv6 addresses in a specific VRF, the following command can be used: Example:

```text
# show ipv6 interface vrf green brief
```

VRF-name Interface-name Logical-interface Address Scope State ---------------------------------------------------------------------------------------------- green intf_l3_2 l3-vlan 400 fe80::204:dfff:feb3:f42a/64 link-local active green intf_l3_2 l3-vlan 400 fd02::1/16 global active

**Output Terms:**

Output Description VRF name Displays the VRF name. Interface name Displays the interface name. Output Description Logical interface Displays the logical interface. Address Displays the IPv6 addresses. Scope Displays the scope of IPv6 addresses. State Displays the state of IPv6 addresses.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show router vrrp`

> **Página:** 342 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows the list of routers VRRP protecting L3 interfaces address(es).

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show router vrrp { brief }
```

**Parameters:**

- `brief` — Displays brief operational information about router VRRP. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

To simply show router VRRP operational information brief, the following command can be used: Example:

```text
# show router vrrp brief
```

Interface-name Afi VR-ID Priority State --------------------------------------------------- test_backup ipv6 100 100 backup test_init ipv4 1 50 initialize test_master ipv6 200 255 master

**Output Terms:**

Output Description Display the L3 interface name with addresses protected by the router Interface name VRRP. Afi Display the address family of the router VRRP. VR-ID Display virtual router ID of the router VRRP. Priority Display the priority of the router VRRP. State Display state of the router VRRP.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A LOOPBACK This topic describes the commands related to management of Loopback logical interfaces such as commands to configure IP address.


## Loopback

### `interface loopback`

> **Página:** 345 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures Loopback logical interfaces.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
interface loopback id [ description if-description | ipv4 address a.b.c.d/x | ipv6 { enable | address x:x:x:x::x/y [ eui-64 ] } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Specifies the ID of the interface. — *Valores:* 0-7. · *Default:* N/A
- `description if-description` — Specifies the description of the interface. It may point out a more meaningful text about its purpose. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* Must be a valid string. · *Default:* N/A
- `ipv4 address a.b.c.d/x` — Specifies an IPv4 address and prefix length, in CIDR notation, to be assigned to logical interface. — *Valores:* a.b.c.d/x. · *Default:* N/A
- `ipv6 enable` — Enables/Disables IPv6 on interface loopback. When enabled, the system allows configuration of IPv6 unicast addresses. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 address x:x:x:x::x/y` — Specifies an IPv6 unicast address and prefix length to be assigned to interface loopback. — *Valores:* x:x:x:x::x/y. · *Default:* N/A
- `eui-64` — Sets 64-bit Extended Unique Identifier for specific IPv6 prefix on interface loopback. — *Valores:* N/A · *Default:* Disabled.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.8 | This command was introduced. |
| 2.4 | IPv6 support. |

**Usage Guidelines:**

The identifier of Loopback logical interface must be within the valid range of 0 and 7. It is possible the use of only one IPv4 per Loopback logical interface and two IPv6 addresses To find which Loopback logical interface is configured with a specific IPv4 address, it is possible to use the commands showed in the example below. Example: This example shows how to find a Loopback logical interface using address as parameter:

```text
# show running-config interface loopback all | include -b 2 200.200.200.1
3-interface loopback 3
4: ipv4 address 200.200.200.1/32
```

Or in configuration mode:

```text
(config)# show interface loopback all | include -b 2 200.200.200.1
3-interface loopback 3
4: ipv4 address 200.200.200.1/32
(config)# show interface loopback all | include 2001:db8::1/32
ipv6 address 2001:db8::1/32
```

This example shows how to find Loopback logical interface IPv6 addresses:

```text
# show ipv6 interface brief
```

Interface-name Logical-interface Address Scope State ----------------------------------------------------------------- loopback 0 loopback 0 2001:db8::1/32 global active Command to configure IPv6 addresses will be available only if ipv6 enable is set for interface. Example below shows that IPv6 address configuration option appears after ipv6 enable is set.

```text
(config-loopback-4)# ipv6 ?
```

Possible completions: enable Enable IPv6 on interface

```text
!
(config-loopback-4)# ipv6 enable
!
(config-loopback-4)# ipv6 ?
```

Possible completions: address IPv6 address enable Enable IPv6 on interface

```text
!
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `interface loopback vrf`

> **Página:** 349 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures VRF on Loopback logical interfaces.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
interface loopback id vrf vrf-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Specifies the ID of the interface. — *Valores:* 0-7. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this interface will be associated with. It is not possible to associate the VRF ‘mgmt’ to a loopback interface. Also, the VRF ‘global’ cannot be directly configured as it is the default VRF when no VRF is associated. — *Valores:* string. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 5.12 | Introduced VRF support on loopback interfaces with IPv6. |

**Usage Guidelines:**

If no VRF is explicitly associated with the loopback interface, it is associated with the global VRF by default. The following example shows how to associate a loopback interface with the ‘test_vrf’ VRF:

```text
(config-loopback-7)# ?
```

Possible completions: vrf Assign a VRF instance to the interface

```text
!
(config-loopback-7)# vrf ?
```

Possible completions: <WORD> VPN Routing/Forwarding instance name test_vrf

```text
!
(config-loopback-7)# vrf test_vrf
(config-loopback-7)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A EDFA This topic describes the commands related to management of EDFA interfaces such as commands to configure mode or to set the gain of the interface.


## EDFA

### `edfa`

> **Página:** 351 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an EDFA (Erbium Doped Fiber Amplifier).

**Supported Platforms:** This command is supported only in the following platforms: DM4920.

**Syntax:**

```text
edfa edfa-port [description if-description] edfa edfa-port {booster | pre-amp} [mode {gain | power}] [gain-limit limit] [power-limit limit] edfa edfa-port {booster | pre-amp} [mode {gain [gain-value value] | power [power-value value]}] edfa edfa-port {booster | pre-amp} alarm los {threshold value | action {disabled | enabled}}*
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `edfa-port` — EDFA port where configuration will be applied. — *Valores:* chassis/slot/port Chassis, slot and port indexes depends on the provisioned linecards(if available in the platform). · *Default:* None.
- `description if-description` — Specifies the description of the EDFA interface. It may point out a more meaningful text about its purpose. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* Must be a valid string. · *Default:* N/A
- `{booster | pre-amp}` — Sets the amplifier type that defines the basic profiles and limits for EDFA operation according to it’s location in the optical network topology. Booster is associated with TX side and pre-amp is in the RX side. — *Valores:* {booster | pre-amp} · *Default:* None.
- `mode` — Sets the operation mode. In gain mode, EDFA output power will follow the input power plus the configured gain-value. Any power variation in the input will reflect to the output. This is the prefered mode in a WDM system since the inclusion or removal of one channel in the aggregated will not affect the remaining channels. In power mode, the EDFA output power is set to a fixed value configured in power-value. Any power variation in the input will not reflect to the output. The gain will vary to keep the output power static. This mode is suitable for single channel application. — *Valores:* gain | power · *Default:* gain
- `gain-limit limit` — Sets the gain limit in dB to be used in power mode. Maximum gain definition is useful to avoid too low input power to be amplified and cause poor OSNR. If the combined input power and power-value would result in a gain higher than gain-limit configuration, the EDFA will operate in LIM (limiting) mode and deliver physical output power lower than set power-value output. In this case, the gain will be close to gain-limit. — *Valores:* 10.0 - 26.0 · *Default:* Disabled.
- `power-limit limit` — Sets the power limit in dBm to be used in gain mode. Power Limit definition is a safeguard to avoid unintentional too high output power in gain mode configuration. The default value is very restrictive and must be adjusted for proper operation. Good practice is to configure this parameter with tight margin for operation as calculated in the optical network project. If the combined input power and gain-value would result in an output power higher than power-limit configuration, the EDFA will operate in LIM (limiting) mode and deliver physical output power close to power-limit. During steady operation, modifying the argument of this command and committing will smoothly move the EDFA operating condition to the new setting. E.g. This will not cause service disruption. Tuning this value in small steps is highly recommended in a live network to avoid transients. — *Valores:* -5.0 - 20.0 · *Default:* 0.0
- `gain-value value` — Sets the value in dB as the target set point for input to output power gain in gain mode. During steady operation, modifying the argument of this command and committing will smoothly move the EDFA operating condition to the new setting. E.g. This will not cause service disruption. Tuning this value in small steps is highly recommended in a live network to avoid transients. — *Valores:* 10.0 - 26.0 · *Default:* 26.0
- `power-value value` — Sets the value in dBm as the target set point for output power in power mode. During steady operation, modifying the argument of this command and committing will smoothly move the EDFA operating condition to the new setting. E.g. This will not cause service disruption. Tuning this value in small steps is highly recommended in a live network to avoid transients. — *Valores:* -5.0 - 20.0 · *Default:* 5.0
- `alarm` — Alarm type where configuration will be applied: • Los: Indicates if the input power is less than los threshold value; — *Valores:* los · *Default:* None.
- `threshold value` — Sets the threshold point for the LOS alarm. Los alarm will rise when input power gets lower than los threshold. Los alarm will clear when input power rises above los threshold plus an internal fixed hysteresis of 2dB. — *Valores:* • In mode booster: -26.0 - -13.0 • In mode pre-amp: -40.0 - -25.0 · *Default:* • In mode booster: -25.0
- `• In mode pre-amp: -36.0 action` — Sets the behavior of the amplifier on input LOS occurrence: • Disabled: Only LOS alarm will rise; • Enabled: LOS alarm will rise and pump will be disabled, causing output to be muted; — *Valores:* {disabled | enabled} · *Default:* enabled

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.4 | This command was introduced. |
| 10.4 | Added description parameter. |

**Usage Guidelines:**

This command can be executed directly via CLI. All commands must be executed after the LC is provisioned and ready. See usage examples below: To configure EDFA (i.e: edfa 1/4/1) as booster, the following command must be issued:

```text
(config)#
(config)# edfa 1/4/1 booster
(config-edfa-1/4/1-booster)#commit
```

To configure EDFA (i.e: edfa 1/4/2) as pre-amp with a custom power-limit (i.e: 10 dBm), the following command must be issued:

```text
(config)#
(config)#edfa 1/4/2 pre-amp power-limit 10
(config-edfa-1/4/2-pre-amp)#commit
```

Note that same effect is achieved by following commands:

```text
(config)#
(config)#edfa 1/4/2 pre-amp
(config-edfa-1/4/2-pre-amp)#power-limit 10
(config-edfa-1/4/2-pre-amp)#commit
```

To check if the configuration was applied, issue the show running-config edfa command:

```text
#show running-config edfa
edfa 1/4/2
pre-amp
mode gain
gain-value 26.0
power-limit 10.0
alarms
los action enabled
los threshold -36.0
!
!
!
```

To configure EDFA (i.e: edfa 1/5/1) as pre-amp with mode power and a custom power-value (i.e: 10 dBm), the following command must be issued:

```text
(config)#
(config)#edfa 1/5/1 pre-amp mode power power-value 10
(config-edfa-1/5/1-pre-amp)#commit
```

To check if the configuration was applied, issue the show running-config edfa command:

```text
#show running-config edfa
edfa 1/5/1
pre-amp
mode power
power-value 10.0
alarms
los action enabled
los threshold -36.0
!
!
!
```

To configure EDFA (i.e: edfa 1/5/2) as booster with alarm los and a custom threshold (i.e: -20), the following command must be issued:

```text
(config)#
(config)#edfa 1/5/2 booster alarms los threshold -20
(config-edfa-1/5/2-booster-alarms)#commit
```

To check if the configuration was applied, issue the show running-config edfa command:

```text
#show running-config edfa
edfa 1/5/2
booster
mode gain
gain-value 26.0
power-limit 0.0
alarms
los action enabled
los threshold -20.0
!
!
!
```

**Impacts and precautions:**

EDFA linecards have high levels of optical output power. Any dirt in the optical connectors can cause irreparable damage to the product. Before connecting the optic patch cords or fiber jumper cables to the product, inspect them and clean their optical connectors if necessary. Do not operate EDFA with open or unconnected output port. Damage in the optical connectors are not covered by warranty. Follow local safe guidance for the safe use, maintenance, service, and installation of optical communications systems.

**Hardware restrictions:**

Linecard model LC-OAB-S combines EDFA and Line-Protection features. In this specific model, EDFA output is internally connected to an 50/50% splitter to broadcast optical signal over Line OUT-[1:2] ports. The internal optical signal split cause attenuation between EDFA output and Line OUT- [1:2] ports. Theoretical insertion loss in a 50/50% splitter is 3dB from input to each of the outputs. Maximum insertion loss in LC-OAB-S internal splitter product is 4.1dB. All EDFA output power configurations and shows will not accomplish this characteristics, so user must consider insertion loss due to internal splitter and calculate necessary corrections over configurations and shows versus physical ports.


### `show edfa`

> **Página:** 358 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to display EDFA and/or Raman information.

**Supported Platforms:** This command is supported only in the following platforms: DM4920.

**Syntax:**

```text
show edfa [info]
```

**Parameters:**

- `None` — Display EDFA and/or Raman information. — *Valores:* N/A. · *Default:* N/A.
- `info` — Display EDFA and/or Raman information. — *Valores:* N/A. · *Default:* N/A.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.4 | This command was introduced. |
| 9.6 | Remove ‘Pump Current’ field. |
| 10.6 | Add the Raman status info. |

**Usage Guidelines:**

This command can be executed directly via CLI. All commands must be executed after the LC is provisioned and ready. Example: These examples shows how to use the show edfa commands.

```text
# show edfa info
EDFA-1/4/1
Ifindex : 487751681
Description : Configured Description
```

Input Power : -10.93 dBm Output Power : 9.13 dBm Signal Power : 9.02 dBm Gain : 19.95 dB Amplifier : OK LD Current : 106.3 mA LD EOL Current : 937.2 mA TEC Current : -196.4 mA TEC Voltage : -0.384 V Supply Voltage : 3.31 V LD Temperature : 25.1 C Case Temperature : 27.8 C Raman-1/4/1 Input Power : -20.55 dBm Output Power : -11.12 dBm Signal Power : -11.39 dBm ASE Power : -23.90 dBm Reflection Power : -8.85 dBm Gain : 9.90 dB Amplifier : OK Pump Power : 300 mW LD Current : 1572.0 mA LD EOL Current : 2528.0 mA TEC Current : 663.1 mA TEC Voltage : 0.056 V LD Temperature : 24.9 C Case Temperature : 36.2 C

**Output Terms:**

Output Description Ifindex Indicates the interface index. Description The configured textual description of the interface. Input Power Indicates the input power in dBm. Output Description Indicates the total output power in dBm on the EDFA/Raman output Output Power port. Indicates the signal output power in dBm on EDFA/Raman output Signal Power port. Signal power is the total output power minus the Amplified Spontaneous Emission (ASE) on this EDFA/Raman stage. Indicates the Amplified Spontaneous Emission (ASE) power of Raman ASE Power in dBm. Indicates the reflection power of Raman in dBm. This value represents the total amount of pump power reflected back to the Raman Reflection Power input. Lower values indicate better performance. High reflected power may be caused by poor return loss, often due to contamination or damage on the Raman IN port connector. Indicates the current resulting gain in dB from input to output ports. Gain Indicates the amplifier status, only one of the following: • DIS: Amplifier disabled due to amplifier disable input or alarm; • LIM: Amplifier gain or output power limited by gain-limit or Amplifier power-limit configured values; • OK: Amplifier is operating normally; Pump Power Indicates the Raman pump power in mW. LD Current Indicates the PUMP current in mA. LD EOL Current Indicates the PUMP end-of-life current in mA. TEC Current Indicates the TEC current in mA. Output Description TEC Voltage Indicates the TEC Voltage in V. Supply Voltage Indicates the Supply Voltage of EDFA in V. LD Temperature Indicates the PUMP temperature in degrees C. Case Temperature Indicates the case temperature in degrees C.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

Linecard model LC-OAB-S combines EDFA and Line-Protection features. In this specific model, EDFA output is internally connected to an 50/50% splitter to broadcast optical signal over Line OUT-[1:2] ports. The internal optical signal split cause attenuation between EDFA output and Line OUT- [1:2] ports. Theoretical insertion loss in a 50/50% splitter is 3dB from input to each of the outputs. Maximum insertion loss in LC-OAB-S internal splitter product is 4.1dB. All EDFA output power configurations and shows will not accomplish this characteristics, so user must consider insertion loss due to internal splitter and calculate necessary corrections over configurations and shows versus physical ports. The linecard model LC-OAC20-R10-NB integrates Raman and EDFA amplifiers. The Raman output and EDFA input ports are internally connected and are not exposed on the front panel. Values reported by the show edfa command for Raman Output Power and EDFA Input Power on this linecard will consistently be similar, although not necessarily identical. Raman amplification occurs within the transmission fiber, external to the Raman module. A high-power, counter-propagating laser pump is injected into the transmission fiber. The Raman IN port on the front panel is a laser aperture and is classified as a Class 3B laser product. LINE-PROTECTION This topic describes the commands related to management of the Line Protection interfaces such as commands to configure mode or to set the power thresholds.


## Line-Protection

### `line-protection`

> **Página:** 363 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a Line-Protection. Line-Protection is a mechanism used to ensure the reliability and availability of optical communication links in high-capacity networks. It is employed to minimize service disruption in the event of a line breakup or equipment failure along the DWDM transmission path. The available optical signal is broadcast through a primary path (Line-1) and a backup path (protection or Line-2) in a 50% / 50% ratio on the transmit side. On the receiving side, there is an optical power monitor for both the primary and backup paths, along with an optical switch to select which path will be directed to the Line-Protection signal output. In the event of a failure on the primary path resulting in degraded optical power below a defined threshold, the network automatically switches to gather traffic from the backup path to ensure communication is restored in automatic mode. Switching action can also be performed manually using forced mode.

**Supported Platforms:** This command is supported only in the following platforms: DM4920.

**Syntax:**

```text
line-protection line-protection-port [description if-description] line-protection line-protection-port [mode {auto | forced}] line-protection line-protection-port [mode {auto [line-1 {power-threshold value}] [line-2 {power-threshold value}]}] line-protection line-protection-port [mode {forced [selected-line {line-1 | line-2}]}]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `line-protection-port` — Line-Protection port where configuration will be applied. — *Valores:* chassis/slot/port Chassis, slot and port indexes depends on the provisioned linecards (if available in the platform). · *Default:* None.
- `description if-description` — Specifies the description of the line protection interface. It may point out a more meaningful text about its purpose. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* Must be a valid string. · *Default:* N/A
- `mode` — Sets the operation mode. In auto mode, the Line-Protection automatically switches all traffic to the backup path (line-2) in the event of a failure on the primary path (line-1). The configured power thresholds of the lines will be used to determine a signal fail or signal degrade when the readings indicate a signal power below the threshold. This mode is non-revertive, meaning that, in case of a failure in line-1, normal traffic remains on line-2 even after the line-1 recovers or the reason for the failure has been resolved. This is the default operation mode. In forced mode, the Line-Protection forces a manual switch to the selected line. — *Valores:* auto | forced · *Default:* auto
- `line-1 power-threshold value` — Line-1 power threshold configuration. In auto mode, this configuration is used to determine the line-1 signal fail or signal degrade when its signal power is below the threshold. The measurement unit of value is dBm. — *Valores:* -40.0 - 0.0 · *Default:* -30.0
- `line-2 power-threshold value` — Line-2 power threshold configuration. In auto mode, this configuration is used to determine the line-2 signal fail or signal degrade when its signal power is below the threshold. The measurement unit of value is dBm. — *Valores:* -40.0 - 0.0 · *Default:* -30.0
- `selected-line` — In forced mode, selects the line to forces a manual switch: • Line-1: forces a manual switch to line-1; • Line-2: forces a manual switch to line-2; — *Valores:* {line-1 | line-2} · *Default:* line-1

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. All commands must be executed after the LC is provisioned and ready. See usage examples below: To configure Line-Protection (i.e: on slot 4) in auto mode (the default mode), the following command must be issued:

```text
(config)#
(config)# line-protection 1/4/1
(config-line-protection-1/4/1)#commit
```

To configure Line-Protection (i.e: on slot 4) in auto mode with a custom power-threshold (i.e: -20 dBm) in line-1, the following command must be issued:

```text
(config)#
(config)#line-protection 1/4/1 line-1 power-threshold -20
(config-line-protection-1/4/1-line-1)#commit
```

Note that same effect is achieved by following commands:

```text
(config)#
(config)#line-protection 1/4/1
(config-line-protection-1/4/1)#line-1
(config-line-protection-1/4/1-line-1)#power-threshold -20
(config-line-protection-1/4/1-line-1)#commit
```

To check if the configuration was applied, issue the show running-config line-protection command:

```text
#show running-config line-protection
line-protection 1/4/1
mode auto
line-1
power-threshold -20.0
!
line-2
power-threshold -30.0
!
!
```

To configure Line-Protection (i.e: on slot 5) in forced mode and a selected-line (i.e: line-2), the following command must be issued:

```text
(config)#
(config)#line-protection 1/5/1 mode forced selected-line line-2
(config-line-protection-1/5/1)#commit
```

To check if the configuration was applied, issue the show running-config line-protection command:

```text
#show running-config line-protection
line-protection 1/5/1
mode forced
selected-line line-2
!
```

**Impacts and precautions:**

Line-Protection linecards have high levels of signal output power. Any dirt in the connectors can cause irreparable damage to the product. Before connecting the optic patch cords or jumper cables to the product, inspect them and clean their connectors if necessary. Do not operate Line-Protection with open or unconnected output port. Damage in the connectors is not covered by warranty. Follow local safe guidance for the safe use, maintenance, service, and installation of communications systems.

**Hardware restrictions:**

Linecard model LC-OAB-S combines EDFA and Line-Protection features. In this specific model, EDFA output is internally connected to an 50/50% splitter to broadcast optical signal over Line OUT-[1:2] ports. The internal optical signal split cause attenuation between EDFA output and Line OUT- [1:2] ports. Theoretical insertion loss in a 50/50% splitter is 3dB from input to each of the outputs. Maximum insertion loss in LC-OAB-S internal splitter product is 4.1dB. All EDFA output power configurations and shows will not accomplish this characteristics, so user must consider insertion loss due to internal splitter and calculate necessary corrections over configurations and shows versus physical ports.


### `show line-protection`

> **Página:** 368 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to display Line-Protection information.

**Supported Platforms:** This command is supported only in the following platforms: DM4920.

**Syntax:**

```text
show line-protection [line-protection-port]
```

**Parameters:**

- `None` — Display Line-Protection information. — *Valores:* N/A. · *Default:* N/A.
- `line-protection-port` — Display the Line-Protection information of the specified port. — *Valores:* chassis/slot/port Chassis, slot and port indexes of the configured Line-Protection. · *Default:* N/A.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 10.4 | The description was introduced. The ‘Ifindex’ field was introduced. The ‘Selected Line’ was replaced by ‘Active Line’ in Forced mode. 12.0 The ‘Power Threshold Line-1’ was introduced. The ‘Power Threshold Line-2’ was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. All commands must be executed after the LC is provisioned and ready. Example: These examples shows how to use the show line-protection commands.

```text
# show line-protection
line-protection 1/4/1
Ifindex : 521273345
Description : Configured Description
Mode : Automatic
Active Line : LINE-1
```

Power Threshold Line-1 : -30.0 dBm Input Power Line-1 : -8.50 dBm Power Threshold Line-2 : -30.0 dBm Input Power Line-2 : -10.31 dBm

```text
# show line-protection 1/5/1
line-protection 1/5/1
Ifindex : 521306113
```

Description : Mode : Forced Active Line : LINE-2 Power Threshold Line-1 : -30.0 dBm Input Power Line-1 : LOS (-40 dBm) Power Threshold Line-2 : -30.0 dBm Input Power Line-2 : -15.29 dBm

**Output Terms:**

Output Description Ifindex Indicates the Line-Protection interface index. Description The configured textual description of the interface. Output Description Indicates the Line-Protection operation mode: • Automatic: the Line-Protection is operating in automatic switching mode; Mode • Forced: the Line-Protection is operating in forced switching mode; Indicates the active line: • Line-1: the Line-Protection switch is on line-1; Active Line • Line-2: the Line-Protection switch is on line 2; Power Threshold Indicates the value of line-1 configured power threshold in dBm. DeLine-1 fault is -30.0 dBm. Input Power Line-1 Indicates the value of line-1 input power in dBm, or ‘LOS (-40 dBm)’ if less than -40.0 dBm. Power Threshold Indicates the value of line-2 configured power threshold in dBm. DeLine-2 fault is -30.0 dBm. Input Power Line-2 Indicates the value of line-2 input power in dBm, or ‘LOS (-40 dBm)’ if less than -40.0 dBm.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

Linecard model LC-OAB-S combines EDFA and Line-Protection features. In this specific model, EDFA output is internally connected to an 50/50% splitter to broadcast optical signal over Line OUT-[1:2] ports. The internal optical signal split cause attenuation between EDFA output and Line OUT- [1:2] ports. Theoretical insertion loss in a 50/50% splitter is 3dB from input to each of the outputs. Maximum insertion loss in LC-OAB-S internal splitter product is 4.1dB. All EDFA output power configurations and shows will not accomplish this characteristics, so user must consider insertion loss due to internal splitter and calculate necessary corrections over configurations and shows versus physical ports. CHAPTER 5: LAYER 2 - SWITCHING PROTOCOLS This chapter describes the commands related to management of Layer 2 protocols in the DmOS CLI. MAC LEARNING This topic describes the commands related to management of learning conditions such as commands to configure the aging or to inspect the MAC address table.
