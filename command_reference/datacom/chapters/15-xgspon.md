# Capítulo 15: XGSPON

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## OLT

### `clear interface statistics xgspon`

> **Página:** 1778 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command clears the statistics for a xgspon interface or ONU Ethernet.

**Supported Platforms:** This command is supported only in the following platforms: DM4616.

**Syntax:**

```text
clear interface statistics xgspon { id | onu onu-id | ethernet ethernet-port}
```

**Parameters:**

- `id` — xgspon interface ID to clear statistics. — *Valores:* Text: chassis/slot/port format · *Default:* None
- `onu-id` — ONU ID to clear statistics. — *Valores:* Number: 0 to 127. · *Default:* None
- `ethernet-port` — ONU Ethernet port to clear statistics. — *Valores:* Number: 1 to 4. · *Default:* None
- `gem-port` — ONU GEM port to clear statistics. — *Valores:* Number: 1 to 16. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.0 | This command was introduced. |

**Usage Guidelines:**

To clear interface statistics xgspon it is necessary to enter in config menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# clear interface statistics xgspon 1/1/1
```

**Impacts and precautions:**

All statistics counters for the selected xgspon interface, ONU Ethernet or ONU GEM port will be erased.

**Hardware restrictions:**

N/A


### `interface xgspon`

> **Página:** 1781 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The interface xgspon command is responsible for configuring a xgspon interface.

**Supported Platforms:** This command is supported only in the following platforms: DM4616.

**Syntax:**

```text
interface xgspon chassis/slot/port interface xgspon chassis/slot/port [ upstream-fec | downstream-fec | shutdown | description { string } | mode { gpon | xgspon } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `upstream-fec` — Enables forwarding of error correction for upstream flow. Changing the value of this field will prompt the user with a confirmation on the CLI. This confirmation is intended to make the user aware of the data traffic stop that will happen once this config is changed due to ponlink reset. — *Valores:* None. · *Default:* Enable.
- `downstream-fec` — Enables forwarding of error correction for downstream flow. Changing the value of this field will prompt the user with a confirmation on the CLI. This confirmation is intended to make the user aware of the data traffic stop that will happen once this config is changed due to ponlink reset. — *Valores:* None. · *Default:* Enable.
- `reach min-distance min-distance` — Configures the minimum logical distance from OLT to ONU (in km). The difference between maximum and minimum distance must be at least 20 km and cannot exceed 40 km. — *Valores:* 0-40 · *Default:* 0
- `reach max-distance max-distance` — Configures the maximum logical distance from OLT to ONU (in km). The difference between maximum and minimum distance must be at least 20 km and cannot exceed 40 km. — *Valores:* 0-60 · *Default:* 40
- `shutdown` — Disables the XGSPON interface. — *Valores:* None. · *Default:* Shutdown.
- `description` — Set the interface description or alias. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A
- `mode` — Set the PON link operating mode (Only available for XGSPON platforms). — *Valores:* gpon or xgspon. · *Default:* xgspon.

**Default:** N/A.

**History:**

| Release | Modification |
| --- | --- |
| 9.0 | This command was introduced. |

**Usage Guidelines:**

To set interface xgspon parameters is necessary to enter in the interface xgspon menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface xgspon 1/1/1
(config-xgspon-1/1/1)#
To set description
(config)# interface xgspon 1/1/1
(config-xgspon-1/1/1)# description "test interface name"
Or
(config-xgspon-1/1/1)# description test_interface_name
```

Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example:

```text
(config-xgspon-1/1/1)# description "test_interface_name|!?;"
```

To change the xgspon interface logical reach to the range of 20 to 60 km:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface xgspon 1/1/1
(config-xgspon-1/1/1)# reach min-distance 20 max-distance 60
```

To set PON Link operation mode

```text
(config)# interface xgspon 1/1/1
(config-xgspon-1/1/1)# mode gpon
Or
(config)# interface xgspon 1/1/1 mode gpon
```

**Impacts and precautions:**

On shutdown, the XGSPON interface will be disabled affecting ongoing data traffic. The user must enter ‘interface xgspon <id>’ mode to issue other interface commands. IMPORTANT: Upon changing upstream-fec and/or downstream-fec configuration on ponlink the data traffic of all ONUs attached to the ponlink will be temporarily stopped. This happens because the ponlink must be reset for the fec configurations to be applied. When configuring PON link reach max-distance, take special care to give a room of 5km considering the farthest ONU. For example, if the farthest ONU is at 20km, set reach max-distance to 25km.

**Hardware restrictions:**

N/A


### `load default-xgspon-profiles`

> **Página:** 1785 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Loads the default XGSPON profiles, which allow a quick configuration of XGSPON features.

**Supported Platforms:** This command is supported only in the following platforms: DM4616.

**Syntax:**

```text
load default-xgspon-profiles load default-xgspon-profiles-bridge load default-xgspon-profiles-router
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.4.0 | This command was introduced. |

**Usage Guidelines:**

The commands create all default XGSPON profiles that are required to add ONUs to the configuration database. That is, the user have to neither create the profiles nor select them on the ONU. There are different sets of profiles for different applications. There are three different sets of XGSPON profiles that can be loaded. 1) load default-xgspon-profiles-bridge: suitable for bridge ONUs. 2) load default-xgspon-profiles-router: suitable for router ONUs. 3) load default-xgspon-profiles: suitable for bridge or router ONUs. Contains a line-profile that supports bridge (ethernet-uni) or router (veip). The OLT will skip any of the flow mappings (see line profile) if the ONU does not support it. As the command load factory-config, only the candidate configuration is modified, therefore the user must commit the modifications in order to apply the configuration. Example: Creating profiles for bridge.

```text
# config
Entering configuration mode terminal
(config)# show configuration this
% No configuration changes found.
(config)# load default-xgspon-profiles-?
```

Possible completions: default-xgspon-profiles-bridge Load the default XGSPON profiles for bridge ONUs default-xgspon-profiles-router Load the default XGSPON profiles for router ONUs

```text
(config)# load default-xgspon-profiles-bridge
```

Loading. Done.

```text
(config)# show configuration this
profile gpon bandwidth-profile DEFAULT-BANDWIDTH-XGSPON
traffic type-4 max-bw 9953280
!
profile gpon line-profile DEFAULT-LINE-XGSPON
upstream-fec
tcont 1 bandwidth-profile DEFAULT-BANDWIDTH-XGSPON
gem 1
tcont 1 priority 1
map any-ethernet
ethernet any vlan any cos any
!
map any-veip
veip 1 vlan any cos any
!
!
gem 2
tcont 1 priority 0
map any-iphost
iphost vlan any cos any
!
!
!
(config)# commit
```

Commit complete.

```text
(config)#
```

Example: Creating an ONU without explicitly selecting its profiles.

```text
# config
Entering configuration mode terminal
(config)# interface xgspon 1/1/3
(config-xgspon-1/1/3)# onu 7
(config-xgspon-onu-7)# show configuration this
interface xgspon 1/1/3
onu 7
line-profile DEFAULT-LINE-XGSPON
!
!
(config-xgspon-onu-7)# serial-number DTCM12345678
(config-xgspon-onu-7)# show configuration this
interface gpon 1/1/3
onu 7
serial-number DTCM12345678
line-profile DEFAULT-LINE-XGSPON
!
!
(config-xgspon-onu-7)# commit
```

Commit complete.

```text
(config-xgspon-onu-7)#
```

Example: Editing profiles before the commit, to make them suitable for a different application.

```text
# config
Entering configuration mode terminal
(config)# load default-xgspon-profiles-router
```

Loading. Done.

```text
(config)# show configuration this
profile gpon bandwidth-profile DEFAULT-BANDWIDTH-XGSPON
traffic type-4 max-bw 9953280
!
profile gpon line-profile DEFAULT-LINE-XGSPON
upstream-fec
tcont 1 bandwidth-profile DEFAULT-BANDWIDTH-XGSPON
gem 1
tcont 1 priority 1
map any-veip
veip 1 vlan any cos any
!
!
gem 2
tcont 1 priority 0
map any-iphost
iphost vlan any cos any
!
!
!
```

Edit the Bandwidth Profiles with a different traffic type and bandwidth:

```text
(config)# profile gpon bandwidth-profile DEFAULT-BANDWIDTH-XGSPON
(config-bandwidth-profile-DEFAULT-BANDWIDTH-XGSPON)# traffic type-1 fixed-bw 5120
```

Edit the Line Profile with a different mapping, specifying a VLAN:

```text
(config-bandwidth-profile-DEFAULT-BANDWIDTH-XGSPON)# top
(config)# profile gpon line-profile DEFAULT-LINE-XGSPON
(config-line-profile-DEFAULT-LINE-XGSPON)# gem 1
(config-line-prof-gem-1)# no map any-veip
(config-line-prof-gem-1)# map veip-300
(config-line-prof-gem-map-veip-300)# veip 1 vlan 300 cos any
```

Check the edited profiles:

```text
(config-line-prof-gem-map-veip-300)# top
(config)# show configuration this
profile gpon bandwidth-profile DEFAULT-BANDWIDTH-XGSPON
traffic type-1 fixed-bw 5120
!
profile gpon line-profile DEFAULT-LINE-XGSPON
upstream-fec
tcont 1 bandwidth-profile DEFAULT-BANDWIDTH-XGSPON
gem 1
tcont 1 priority 1
map veip-300
veip 1 vlan 300 cos any
!
!
gem 2
tcont 1 priority 0
map any-iphost
iphost vlan any cos any
!
!
!
(config)# commit
```

Commit complete.

```text
(config)#
```

**Impacts and precautions:**

It is advised to use only one of the commands at a time, as running more than one will merge the configurations, potentially creating non-functional configurations. The default xgspon profiles will always be required when an interface xgspon has been used, even though its mode has been set as gpon. In this case, one needs to adjust the bandwidth traffic limits to be supported in that mode.

**Hardware restrictions:**

N/A


### `show interface xgspon`

> **Página:** 1789 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays XGSPON interface information. Regarding the discovered ONUs show operation, an ONU is only displayed if it discovered in the XGSPON port but not provisioned. Once an ONU is provisioned, it is no longer displayed.

**Supported Platforms:** This command is supported only in the following platforms: DM4616.

**Syntax:**

```text
show interface xgspon [ chassis/slot/port ] [ brief | statistics | detail | discovered-onus ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `chassis/slot/port` — The ponlink to display information. — *Valores:* Text: chassis/slot/port format. · *Default:* N/A
- `brief` — Display brief information of the XGSPON interface. — *Valores:* brief: Fixed text ‘brief’. · *Default:* N/A
- `statistics` — Display statistics information of the XGSPON interface. — *Valores:* statistics: Fixed text ‘statistics’. · *Default:* N/A
- `detail` — Display detailed information of the XGSPON interface. — *Valores:* detail: Fixed text ‘detail’. · *Default:* N/A
- `discovered-onus` — Display discovered ONUs. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.0 | This command was introduced. |

**Usage Guidelines:**

Show xgspon 1/1/1 information

```text
# show interface xgspon 1/1/4
```

Physical interface : xgspon 1/1/4, Enabled, Physical link is Up Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : neophotonics-b Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 439449 kbit/s Total BW : 1098624 kbit/s Show all xgspon interfaces information

```text
# show interface xgspon
```

Physical interface : xgspon 1/1/1, Disabled, Physical link is Down Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 1106944 kbit/s Overhead : 33 kbit/s (1 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : xgspon 1/1/2, Disabled, Physical link is Down Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : xgspon 1/1/3, Disabled, Physical link is Down Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : xgspon 1/1/4, Disabled, Physical link is Down Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Show all xgspon interfaces information

```text
# show interface xgspon *
```

Physical interface : xgspon 1/1/1, Disabled, Physical link is Down Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 1106944 kbit/s Overhead : 33 kbit/s (1 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : xgspon 1/1/2, Disabled, Physical link is Down Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : xgspon 1/1/3, Disabled, Physical link is Down Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : xgspon 1/1/4, Disabled, Physical link is Down Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Show a range of xgspon interfaces information

```text
# show interface xgspon 1/1/3-4
```

Physical interface : xgspon 1/1/3, Disabled, Physical link is Down Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : xgspon 1/1/4, Disabled, Physical link is Down Link-level type : XGSPON Logical reach : 0-40 km Downstream FEC : Enabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Show all xgspon interfaces information (brief option)

```text
# show interface xgspon brief
```

Interface DS FEC US FEC Admin Link Transceiver type -------------------------------------------------------------------------------- 1/1/1 Enabled Enabled Disabled Down none 1/1/2 Enabled Enabled Disabled Down none 1/1/3 Enabled Enabled Disabled Down none 1/1/4 Enabled Enabled Disabled Down none Show all xgspon interfaces information (brief option)

```text
# show interface xgspon * brief
```

Interface DS FEC US FEC Admin Link Transceiver type -------------------------------------------------------------------------------- 1/1/1 Enabled Enabled Disabled Down none 1/1/2 Enabled Enabled Disabled Down none 1/1/3 Enabled Enabled Disabled Down none 1/1/4 Enabled Enabled Enabled Up neophotonics-b Show all xgspon interfaces in a given chassis/slot information (brief option)

```text
# show interface xgspon 1/1/* brief
```

Interface DS FEC US FEC Admin Link Transceiver type -------------------------------------------------------------------------------- 1/1/1 Enabled Enabled Disabled Down none 1/1/2 Enabled Enabled Disabled Down none 1/1/3 Enabled Enabled Disabled Down none 1/1/4 Enabled Enabled Enabled Up neophotonics-b Show a range of xgspon interfaces information (brief option)

```text
# show interface xgspon 1/1/2-3 brief
```

Interface DS FEC US FEC Admin Link Transceiver type -------------------------------------------------------------------------------- 1/1/2 Enabled Enabled Disabled Down none 1/1/3 Enabled Enabled Disabled Down none Show a list of xgspon interfaces information (brief option)

```text
# show interface xgspon 1/1/1,3 brief
```

Interface DS FEC US FEC Admin Link Transceiver type -------------------------------------------------------------------------------- 1/1/1 Enabled Enabled Disabled Down none 1/1/3 Enabled Enabled Disabled Down none Show discovered ONUs in all xgspon interfaces

```text
# show interface xgspon discovered-onus
```

Chassis / Slot / Port Serial Number --------------------- ------------- 1/1/1 DACM00000351 1/1/3 DACM00000352 Show discovered ONUs in all xgspon interfaces

```text
# show interface xgspon * discovered-onus
```

Chassis / Slot / Port Serial Number --------------------- ------------- 1/1/1 DACM00000351 1/1/3 DACM00000352 Show discovered ONUs in all xgspon interfaces in a given chassis/slot

```text
# show interface xgspon 1/1/* discovered-onus
```

Chassis / Slot / Port Serial Number --------------------- ------------- 1/1/1 DACM00000351 1/1/3 DACM00000352 Show discovered ONUs in a range of xgspon interfaces

```text
# show interface xgspon 1/1/1-3 discovered-onus
```

Chassis / Slot / Port Serial Number --------------------- ------------- 1/1/1 DACM00000351 1/1/3 DACM00000352 Show statistics of all xgspon interfaces using table mode

```text
# show interface xgspon * | tab | select statistics
CHASSIS
```

ID/SLOT IN IN IN IN OUT OUT OUT ID/PORT IN UNICAST BROADCAST MULTICAST IN IN UNKNOWN OUT UNICAST BROADCAST MULTICAST OUT OUT I-D--------O-C-T-E-T-S---P-K-T-S------P-K-T-S--------P-K-T-S--------D-I-S-C-A-R-D-S---E-R-R-O-R-S---P-R-O-T-O-S----O-C-T-E-T-S---P-K-T-S------P-K-T-S--------P-K-T-S--------D-I-S-C-A-R-D-S---E-R-R-O-R-S--- 1/1/1 0 0 0 0 0 0 0 0 0 0 0 0 0 1/1/2 0 0 0 0 0 0 0 0 0 0 0 0 0 1/1/3 0 0 0 0 0 0 0 0 0 0 0 0 0 1/1/4 0 0 0 0 0 0 0 0 0 0 0 0 0

**Output Terms:**

Output Description Physical interface Name and status of the XGSPON interface. The Link-level type can be either GPON or XGSPON, depending on Link-level type the pon port mode. Logical reach Show the interface differential logical reach (in kilometers). Downstream FEC Downstream FEC status. Upstream FEC Upstream FEC status. Transceiver type Type of the transceiver. Allocated upstream Header for the types of bandwidth allocated. bandwidth Fixed + Assured Allocated bandwidth of both Fixed and Assured types added. Fixed Allocated bandwidth of Fixed type. Assured Allocated bandwidth of Assured type. Output Description Max Allocated bandwidth of Maximum type. Allocated bandwidth for inband management of all ONUs on the Overhead XGSPON interface. ONUs Number of ONUs configured on the XGSPON interface. Available upstream Header for the types of available upstream bandwidth. bandwidth CBR BW Available fixed bandwidth (traffic type-1 and type-5) in the ponlink. Available total bandwidth (assured+fixed; traffic type-1, type-2, Total BW type-3 and type-5) in the ponlink.

**Impacts and precautions:**

It is not supported to use commas in the key wildcard in xgspon interface discovered-onus show option ( show interface xgspon 1/1/2,3,4 discovered-onus ).

**Hardware restrictions:**

N/A ONU PROFILES This topic describes the ONU profiles commands related to ONU traffic configuration, such as line and service profiles.


## ONU Profiles

### `profile gpon onu-profile`

> **Página:** 1797 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Defines the amount of each type of port of an ONU or a group of ONUs.

**Supported Platforms:** This command is supported only in the following platforms: DM4616.

**Syntax:**

```text
profile gpon onu-profile profile-name { ethernet { eth-ports | adaptive } | pots { pots-ports | adaptive } | veip veip-ports }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `onu-profile profile-name` — Name of the ONU profile. — *Valores:* String (1-48 characters; accepts alphanumeric characters, ‘+’, ‘-’ and ’_’). · *Default:* None
- `ethernet { eth-ports | adaptive }` — Number of Ethernet ports or adaptive mode (auto discovery). — *Valores:* 1-4 or adaptive · *Default:* None
- `pots { pots-ports | adaptive }` — Number of POTS (Voice) ports or adaptive mode (auto discovery). — *Valores:* 1-4 or adaptive · *Default:* None
- `veip veip-ports` — Number of Virtual Ethernet Interface Points (for router/residential gateway ONUs). — *Valores:* 1 · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.0 | This command was introduced. |

**Usage Guidelines:**

To configure an ONU profile, it is necessary to enter the onu-profile menu. It is not possible to create an ONU profile with no Ethernet, POTS or VEIP value. The profile cannot be modified after it is committed. The profile cannot be deleted if it is referenced by a service-profile. Example (configuring an ONU profile with 4 Ethernet ports and 2 POTS ports):

```text
# config
Entering configuration mode terminal
(config)# profile gpon onu-profile onuProfName
(config-onu-profile-onuProfName)# ethernet 4
(config-onu-profile-onuProfName)# pots 2
```

Example (configuring an ONU profile with a VEIP interface):

```text
# config
Entering configuration mode terminal
(config)# profile gpon onu-profile onuProfName2
(config-onu-profile-onuProfName2)# veip 1
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A ONU This topic describes the commands related to ONU such as commands to authenticate an ONU and configure its UNIs.


## ONU

### `show interface xgspon onu`

> **Página:** 1800 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays ONU information.

**Supported Platforms:** This command is supported only in the following platforms: DM4616.

**Syntax:**

```text
show interface xgspon chassis/slot/port onu onu-id [ version | optical-info | brief | rssi ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `chassis/slot/port` — The XGSPON port on which the ONU is located. — *Valores:* Text: chassis/slot/port format. · *Default:* N/A
- `onu onu-id` — The ONU referred. — *Valores:* onu-id: Number from 0 to 127. · *Default:* N/A
- `version` — Display firmware version of the ONU. — *Valores:* N/A · *Default:* N/A
- `optical-info` — Display informations of the ONU’s optical interface. — *Valores:* N/A · *Default:* N/A
- `brief` — Display brief information of the ONU. — *Valores:* N/A · *Default:* N/A
- `rssi` — Display the RSSI (received signal strength indication) for a specific ONU. The value represents the power level received at the OLT for the selected ONU. Only one ONU can be selected each time. The value read from the CLI may be different from the actual value read by a power meter. The value can also be affected by the amount of traffic transmitted by ONU. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.0 | This command was introduced. |

**Usage Guidelines:**

```text
# show interface xgspon 1/1/8 onu 1
```

Last updated : 2017-11-22 15:00:27 UTC+0 ID : 1 Serial Number : DACM00000353 Password : Uptime : 22:34 Last Seen Online : N/A Vendor ID : DACM Equipment ID : DM984-100B Name : Operational state : Up Primary status : Active Distance : 0 [km] IPv4 mode : Not configured IPv4 address : IPv4 default gateway : IPv4 VLAN : IPv4 CoS : Line Profile : DEFAULT-LINE Service Profile : RG Profile : RG One Shot Provision : Not provisioned TR069 ACS Profile : SNMP : Disabled Allocated bandwidth : 0 fixed, 0 assured+fixed [kbit/s] Upstream-FEC : Enabled Anti Rogue ONU isolate : Disabled Version : Active FW : v1.3.2 valid, committed Standby FW : v1.3.1 valid, not committed Software Download State : None Rx Optical Power [dBm] : -8.16 Tx Optical Power [dBm] : -0.08 Show all ONUs in all xgspon interfaces

```text
# show interface xgspon onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 2 CIGG12345672 Up Complete ONU2 1/1/3 1 CIGG12345673 Up Complete ONU3 1/1/4 1 CIGG12345674 Up Complete ONU4 1/1/4 5 CIGG12345675 Up Complete ONU5 Show all ONUs in all xgspon interfaces

```text
# show interface xgspon * onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 2 CIGG12345672 Up Complete ONU2 1/1/3 1 CIGG12345673 Up Complete ONU3 1/1/4 1 CIGG12345674 Up Complete ONU4 1/1/4 5 CIGG12345675 Up Complete ONU5 Show all ONUs in all xgspon interfaces in a given chassis/slot

```text
# show interface xgspon 1/1/* onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 2 CIGG12345672 Up Complete ONU2 1/1/3 1 CIGG12345673 Up Complete ONU3 1/1/4 1 CIGG12345674 Up Complete ONU4 1/1/4 5 CIGG12345675 Up Complete ONU5 Show all ONUs in range of xgspon interfaces/slot

```text
# show interface xgspon 1/1/1-4 onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 2 CIGG12345672 Up Complete ONU2 1/1/3 1 CIGG12345673 Up Complete ONU3 Show all ONUs in a list of xgspon interfaces/slot

```text
# show interface xgspon 1/1/2,4 onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/2 1 CIGG12345671 Up Complete ONU1 1/1/2 2 CIGG12345672 Up Complete ONU2 1/1/4 1 CIGG12345673 Up Complete ONU3 Show all ONUs in a given xgspon interface/slot

```text
# show interface xgspon 1/1/1 onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 9 CIGG12345672 Up Complete ONU9 1/1/1 22 CIGG12345673 Up Complete ONU22 Show a range of ONUs in a given xgspon interface/slot

```text
# show interface xgspon 1/1/1-10 onu *
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 9 CIGG12345672 Up Complete ONU9

**Output Terms:**

Output Description Shows the timestamp of the last time the selected ONU has its status Last updated published to the database. Updated only when others status are updated. ID ID of the ONU. Serial Number Serial number of the ONU. Output Description Password ONU password. The uptime reported by the ONU. Updated only when the difference Uptime of the time info is greater than 5 minutes. The time since ONU was online. Updated only when the difference Last Seen Online of the time info is greater than 5 minutes. Vendor ID Vendor ID part of the ONU. Equipment ID Equipment ID of the ONU. Name User defined name of the ONU. Operational state State of operation of the ONU. Primary status Primary status of the ONU. Distance Approximate ONU logical distance (in kilometers) from the OLT. IPv4 mode ONU IP-Host mode: static or DHCP. IPv4 Address ONU IP-Host IPv4 Address. IPv4 default ONU IP-Host IPv4 default gateway. gateway IPv4 VLAN ONU IP-Host VLAN. IPv4 CoS ONU IP-Host CoS. Line Profile Line Profile assigned to the ONU. Output Description Service Profile Service Profile assigned to the ONU. RG Profile RG Profile assigned to the ONU. RG One Shot Indicates the time that RG Profile was provisioned at ONU. Provision TR069 ACS Profile TR069 ACS Profile assigned to the ONU. Shows if the ONU has snmp enabled and the SNMP profile when apSNMP plicable. Allocated Type and amount of bandwidth allocated for the ONU. bandwidth Upstream-FEC Upstream-FEC state. Anti Rogue ONU Anti Rogue ONU isolate state. isolate Version ONU firmware version. Active FW Firmware version of the ONU active image. Standby FW Firmware version of the ONU standby image. Software Download ONU firmware upgrade state. State Rx Optical Power Rx power level in dBms. Updated only when the difference is greater -dBm- than 0.2dBm. Tx Optical Power Tx power level in dBms. Updated only when the difference is greater -dBm- than 0.2dBm. Output Description RSSI -dBm- Power level received at the OLT for a specific ONU.

**Impacts and precautions:**

It is not supported to use a key pattern in both ONU and xgspon interface IDs ( show interface xgspon * onu * ). It is not supported to use ONU ID key pattern together with brief/optical-info/version options ( show interface xgspon 1/1/1 onu * brief ). In some scenarios, the ONU logical distance cannot be retrieved correctly and it will be shown as N/A. This behavior can happen specially when the configured PON link maximum distance is close to the ONU logical distance, for example, when the ONU is at 20km distant and PON link maximum distance is configured to 21km.

**Hardware restrictions:**

N/A


### `show interface xgspon onu Ethernet`

> **Página:** 1807 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays information about the user’s Ethernet ports of the ONU.

**Supported Platforms:** This command is supported only in the following platforms: DM4616.

**Syntax:**

```text
show interface xgspon chassis/slot/port onu [ onu-id ] ethernet [ ethernet-port [ brief | detail | statistics ] ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `chassis/slot/port` — The XGSPON port on which the ONU is located. — *Valores:* Text: chassis/slot/port format. · *Default:* N/A
- `onu-id` — The ONU to which the Ethernet port belongs to. — *Valores:* onu-id: Number from 0 to 127. · *Default:* N/A
- `ethernet-port` — Number of the ONU’s Ethernet port. — *Valores:* Number from 1 to 4 depending on the ONU profile of the ONU. · *Default:* N/A
- `brief` — Display brief information of the ONU’s Ethernet interfaces. — *Valores:* brief: Fixed text ‘brief’. · *Default:* N/A
- `statistics` — Display statistics information of the ONU’s Ethernet interfaces. — *Valores:* statistics: Fixed text ‘statistics’. · *Default:* N/A
- `detail` — Display detailed information of the ONU’s Ethernet interfaces. — *Valores:* detail: Fixed text ‘detail’. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.0 | This command was introduced. |

**Usage Guidelines:**

```text
# show interface xgspon 1/1/8 onu 1 ethernet 1
```

Physical interface : ethernet 1, Enabled, Physical link is up XGSPON Information: xgspon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Show all ethernet UNIs in a given ONU

```text
# show interface xgspon 1/1/1 onu 1 ethernet *
```

Physical interface : ethernet 1, Enabled, Physical link is up XGSPON Information: xgspon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Physical interface : ethernet 2, Enabled, Physical link is up XGSPON Information: xgspon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Show all ethernet UNIs in a given ONU

```text
# show interface xgspon 1/1/1 onu 1 ethernet
```

Physical interface : ethernet 1, Enabled, Physical link is up XGSPON Information: xgspon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Physical interface : ethernet 2, Enabled, Physical link is up XGSPON Information: xgspon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Show a range ethernet UNIs in a given ONU

```text
# show interface xgspon 1/1/1 onu 1 ethernet 1-2
```

Physical interface : ethernet 1, Enabled, Physical link is up XGSPON Information: xgspon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Physical interface : ethernet 2, Enabled, Physical link is up XGSPON Information: xgspon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Show all ethernet UNIs in all ONUs in a given xgspon interface

```text
# show interface xgspon 1/1/1 onu * ethernet *
```

Physical interface : ethernet 1, Enabled, Physical link is up XGSPON Information: xgspon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Physical interface : ethernet 2, Enabled, Physical link is up XGSPON Information: xgspon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Physical interface : ethernet 1, Enabled, Physical link is down XGSPON Information: xgspon-1/1/1, ONU 10 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: Native VLAN/CoS : - MAC limit : Unlimited When using detail option, it will override other show options passed. For example, if the operator runs “show interface xgspon 1/1/1 onu 1 ethernet 1 brief detail”, “show interface xgspon 1/1/1 onu 1 ethernet 1 statistics detail” or “show interface xgspon 1/1/1 onu 1 ethernet 1 brief detail statistics” only detail option will be shown. The same way, statistics option will override the default “show interface xgspon 1/1/1 onu 1 ethernet 1” or it will have precedence over brief option in “show interface xgspon 1/1/1 onu 1 ethernet 1 brief statistics” outputs as well.

**Output Terms:**

Output Description Physical interface Name and status of the XGSPON interface. Link-level type Type of the Link-level. Speed Speed of the Ethernet UNI. Duplex Duplex configuration. Negotiation Negotiation status (enabled/disabled). Status Negotiation Negotiated Speed and Duplex. Native-vlan Native VLAN of the Ethernet UNI.

**Impacts and precautions:**

It is not supported to use a key pattern in xgspon interface IDs ( show interface xgspon * onu * ethernet ).

**Hardware restrictions:**

N/A


### `show interface xgspon onu gem`

> **Página:** 1812 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays ONU XGSPON Encapsulation Method information.

**Supported Platforms:** This command is supported only in the following platforms: DM4616.

**Syntax:**

```text
show interface xgspon chassis/slot/port onu [ onu-id ] gem [ gem-id ] [ brief ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `chassis/slot/port` — The XGSPON port on which the ONU is located. — *Valores:* Text: chassis/slot/port format. · *Default:* N/A
- `onu-id` — The ONU where the GEM is located. — *Valores:* onu-id: Number from 0 to 127 (maximum of 64 elements). · *Default:* N/A
- `gem-id` — The ID of the GEM for information display. — *Valores:* gem-id: Number from 1 to 16. · *Default:* N/A
- `brief` — Display brief information of the GEM. — *Valores:* brief: Fixed text ‘brief’. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.0 | This command was introduced. |

**Usage Guidelines:**

Show a GEM in an ONUs

```text
# show interface xgspon 1/1/1 onu 13 gem 1
GEM ID : 1
```

XGSPON Information : xgspon-1/1/1, ONU 10 Operational status is : up GEM Port-ID : 352 Alloc-ID : 256 T-CONT : 1 Encryption : disabled Show all GEMs in all ONUs in a given xgspon interface

```text
# show interface xgspon 1/1/1 onu * gem *
GEM ID : 1
```

XGSPON Information : xgspon-1/1/1, ONU 1 Operational status is : up GEM Port-ID : 305 Alloc-ID : 256 T-CONT : 1 Encryption : disabled GEM ID : 1 XGSPON Information : xgspon-1/1/1, ONU 10 Operational status is : up GEM Port-ID : 450 Alloc-ID : 257 T-CONT : 1 Encryption : disabled Show all GEMs in a given ONU

```text
# show interface xgspon 1/1/1 onu 10 gem *
GEM ID : 1
```

XGSPON Information : xgspon-1/1/1, ONU 10 Operational status : down GEM Port-ID : 449 Alloc-ID : 0 T-CONT : 1 Encryption : disabled GEM ID : 2 XGSPON Information : xgspon-1/1/1, ONU 10 Operational status : down GEM Port-ID : 450 Alloc-ID : 0 T-CONT : 1 Encryption : disabled Show all GEMs in a given ONU

```text
# show interface xgspon 1/1/1 onu 10 gem
GEM ID : 1
```

XGSPON Information : xgspon-1/1/1, ONU 10 Operational status : down GEM Port-ID : 449 Alloc-ID : 256 T-CONT : 1 Encryption : unknown GEM ID : 2 XGSPON Information : xgspon-1/1/1, ONU 10 Operational status : down GEM Port-ID : 450 Alloc-ID : 256 T-CONT : 1 Encryption : disabled

**Output Terms:**

Output Description GEM ID ID of the GEM. Operation status Operational status. is GEM Port-ID ID of the GEM Port. Alloc-ID Alloc ID of the GEM. T-CONT T-CONT ID related to the GEM. Encryption Encryption state (enabled/disabled).

**Impacts and precautions:**

It is not supported to use a key pattern in xgspon interface IDs. For example: show interface xgspon * onu * gem

**Hardware restrictions:**

N/A CHAPTER 16: SERVICES This chapter describes the CLI commands related to DmOS available services. MANAGEMENT This topic describes the commands related to use of management clients such as commands to open a telnet or SSH connection to a remote device.
