# Capítulo 14: GPON

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## OLT

### `aes-key-exchange`

> **Página:** 1631 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Sets the AES Key Exchange interval.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
aes-key-exchange { interval }
```

**Parameters:**

- `aes-key-exchange interval` — The time interval for the AES Key Exchange procedure. — *Valores:* Number from 30 to 26000. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

To set an aes-key-interval it is necessary to enter in the given gpon card menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# gpon 1/1
(config-gpon-1/1)# aes-key-exchange 30
```

**Impacts and precautions:**

None

**Hardware restrictions:**

N/A


### `clear interface statistics gpon`

> **Página:** 1633 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command clears the statistics for a GPON interface, ONU Ethernet or ONU GEM port.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
clear interface statistics gpon { id | onu onu-id | ethernet ethernet-port | gem gem-id}
```

**Parameters:**

- `id` — GPON interface ID to clear statistics. — *Valores:* Text: chassis/slot/port format · *Default:* None
- `onu-id` — ONU ID to clear statistics. — *Valores:* Number: 0 to 127. · *Default:* None
- `ethernet-port` — ONU Ethernet port to clear statistics. — *Valores:* Number: 1 to 4. · *Default:* None
- `gem-port` — ONU GEM port to clear statistics. — *Valores:* Number: 1 to 16. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. Removed no longer valid ONU ethernet and GEM port statistics parame1.8 ters. |
| 1.8.2 | Added ONU ethernet port statistics parameters. |
| 5.12.0 | Added ONU GEM port statistics parameters. |

**Usage Guidelines:**

Example:

```text
# clear interface statistics gpon 1/1/1
```

**Impacts and precautions:**

All statistics counters for the selected GPON interface, ONU Ethernet or ONU GEM port will be erased.

**Hardware restrictions:**

N/A


### `interface gpon`

> **Página:** 1636 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The interface gpon command is responsible for configuring a gpon interface.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
interface gpon chassis/slot/port interface gpon chassis/slot/port [ upstream-fec | downstream-fec | shutdown | description { string } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `upstream-fec` — Enables forwarding of error correction for upstream flow. Changing the value of this field will prompt the user with a confirmation on the CLI. This confirmation is intended to make the user aware of the data traffic stop that will happen once this config is changed due to ponlink reset. — *Valores:* None. · *Default:* Enable.
- `downstream-fec` — Enables forwarding of error correction for downstream flow. Changing the value of this field will prompt the user with a confirmation on the CLI. This confirmation is intended to make the user aware of the data traffic stop that will happen once this config is changed due to ponlink reset. — *Valores:* None. · *Default:* Disable.
- `reach min-distance min-distance` — Configures the minimum logical distance from OLT to ONU (in km). The difference between maximum and minimum distance must be at least 20 km and cannot exceed 40 km. — *Valores:* 0-40 · *Default:* 0
- `reach max-distance max-distance` — Configures the maximum logical distance from OLT to ONU (in km). The difference between maximum and minimum distance must be at least 20 km and cannot exceed 40 km. — *Valores:* 0-60 · *Default:* 40
- `shutdown` — Disables the GPON interface. — *Valores:* None. · *Default:* Shutdown.
- `description` — Set the interface description or alias. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A

**Default:** N/A.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 2.0 | Port reach configuration option was added. |
| 10.4.0 | Downstream-fec default value was changed to false for GPON ports. |

**Usage Guidelines:**

To set interface gpon parameters is necessary to enter in the interface gpon menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)#
To set description
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# description "test interface name"
Or
(config-gpon-1/1/1)# description test_interface_name
```

Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example:

```text
(config-gpon-1/1/1)# description "test_interface_name|!?;"
```

To change the gpon interface logical reach to the range of 20 to 60 km:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# reach min-distance 20 max-distance 60
```

**Impacts and precautions:**

On shutdown, the GPON interface will be disabled affecting ongoing data traffic. The user must enter ‘interface gpon <id>’ mode to issue other interface commands. IMPORTANT: Upon changing upstream-fec and/or downstream-fec configuration on ponlink the data traffic of all ONUs attached to the ponlink will be temporarily stopped. This happens because the ponlink must be reset for the fec configurations to be applied. When configuring PON link reach max-distance, take special care to give a room of 5km considering the farthest ONU. For example, if the farthest ONU is at 20km, set reach max-distance to 25km.

**Hardware restrictions:**

N/A


### `load default-gpon-profiles`

> **Página:** 1640 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Loads the default GPON profiles, which allow a quick configuration of GPON features.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
load default-gpon-profiles load default-gpon-profiles-bridge load default-gpon-profiles-router
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.8.2 | This command was introduced. Remove ONU-profile from default profiles list. Remove service-profile 4.0.0 from default profiles list. Command load-default-gpon-profiles added. |

**Usage Guidelines:**

The commands create all default GPON profiles that are required to add ONUs to the configuration database. That is, the user have to neither create the profiles nor select them on the ONU. There are different sets of profiles for different applications. There are three different sets of GPON profiles that can be loaded. 1) load default-gpon-profiles-bridge: suitable for bridge ONUs. 2) load default-gpon-profiles-router: suitable for router ONUs. 3) load default-gpon-profiles: suitable for bridge or router ONUs. Contains a line-profile that supports bridge (ethernet-uni) or router (veip). The OLT will skip any of the flow mappings (see line profile) if the ONU does not support it. As the command load factory-config, only the candidate configuration is modified, therefore the user must commit the modifications in order to apply the configuration. Example: Creating profiles for bridge.

```text
# config
Entering configuration mode terminal
(config)# show configuration this
% No configuration changes found.
(config)# load default-gpon-profiles-?
```

Possible completions: default-gpon-profiles-bridge Load the default GPON profiles for bridge ONUs default-gpon-profiles-router Load the default GPON profiles for router ONUs

```text
(config)# load default-gpon-profiles-bridge
```

Loading. Done.

```text
(config)# show configuration this
profile gpon bandwidth-profile DEFAULT-BANDWIDTH
traffic type-4 max-bw 1106944
!
profile gpon line-profile DEFAULT-LINE
upstream-fec
tcont 1 bandwidth-profile DEFAULT-BANDWIDTH
gem 1
tcont 1 priority 1
map any-ethernet
ethernet any vlan any cos any
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
(config)# interface gpon 1/1/3
(config-gpon-1/1/3)# onu 7
(config-gpon-onu-7)# show configuration this
interface gpon 1/1/3
onu 7
line-profile DEFAULT-LINE
!
!
(config-gpon-onu-7)# serial-number DTCM12345678
(config-gpon-onu-7)# show configuration this
interface gpon 1/1/3
onu 7
serial-number DTCM12345678
line-profile DEFAULT-LINE
!
!
(config-gpon-onu-7)# commit
```

Commit complete.

```text
(config-gpon-onu-7)#
```

Example: Editing profiles before the commit, to make them suitable for a different application.

```text
# config
Entering configuration mode terminal
(config)# load default-gpon-profiles-router
```

Loading. Done.

```text
(config)# show configuration this
profile gpon bandwidth-profile DEFAULT-BANDWIDTH
traffic type-4 max-bw 1106944
!
profile gpon line-profile DEFAULT-LINE
upstream-fec
tcont 1 bandwidth-profile DEFAULT-BANDWIDTH
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
(config)# profile gpon bandwidth-profile DEFAULT-BANDWIDTH
(config-bandwidth-profile-DEFAULT-BANDWIDTH)# traffic type-1 fixed-bw 5120
```

Edit the Line Profile with a different mapping, specifying a VLAN:

```text
(config-bandwidth-profile-DEFAULT-BANDWIDTH)# top
(config)# profile gpon line-profile DEFAULT-LINE
(config-line-profile-DEFAULT-LINE)# gem 1
(config-line-prof-gem-1)# no map any-veip
(config-line-prof-gem-1)# map veip-300
(config-line-prof-gem-map-veip-300)# veip 1 vlan 300 cos any
```

Check the edited profiles:

```text
(config-line-prof-gem-map-veip-300)# top
(config)# show configuration this
profile gpon bandwidth-profile DEFAULT-BANDWIDTH
traffic type-1 fixed-bw 5120
!
profile gpon line-profile DEFAULT-LINE
upstream-fec
tcont 1 bandwidth-profile DEFAULT-BANDWIDTH
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

It is advised to use only one of the commands at a time, as running more than one will merge the configurations, potentially creating non-functional configurations.

**Hardware restrictions:**

N/A


### `onu-auto-provisioning`

> **Página:** 1644 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure all parameters to be applied to an ONU when added automatically to database. This configuration is present in the gpon-card prompt.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
onu-auto-provisioning service-port sp-id gem gem port match vlan vlan-id { user-vlan | any } action { vlan { add vlan-id vid | replace vlan-id vid } } [ inner-vlan replace vlan-id vid ] onu-auto-provisioning ipv4 vlan vlan-id vlan-val { cos cos-val } onu-auto-provisioning line-profile line-profile-name onu-auto-provisioning rg-profile rg-profile-name onu-auto-provisioning service-profile svc-profile-name onu-auto-provisioning snmp-profile snmp-profile-name onu-auto-provisioning ethernet ethernet-uni-id { native {vlan vlan-id vlan-val { cos cos-val } | downstream-mode { filter-on-vid-only | inverse-of-upstream } } } onu-auto-provisioning veip veip-id { native vlan vlan-id vlan-val { cos cos-val } }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `enable` — Enable or disable ONU auto provisioning function. — *Valores:* None · *Default:* None
- `ipv4 dhcp` — Configures the ONU IP Host interface to use DHCP. — *Valores:* None · *Default:* None
- `ipv4 vlan vlan-id vlan-val` — Configures the VLAN ID to be configured in the ONU IP Host interface. — *Valores:* 1-4094 · *Default:* None
- `ipv4 vlan vlan-id vlan-val cos cos-val` — Configures the VLAN ID and CoS to be configured in the ONU IP Host interface. — *Valores:* 0-7 · *Default:* None
- `line-profile line-profile-name` — Reference to line-profile that will be applied to the auto provisioned ONU. — *Valores:* Text with up to 48 characters. · *Default:* “DEFAULT-LINE” for GPON platforms and “DEFAULT-LINE-XGSPON”
- `for XGSPON platforms. rg-profile rg-profile-name` — Reference to rg-profile that will be applied to the auto provisioned ONU. — *Valores:* Text with up to 48 characters. · *Default:* None.
- `service-profile service-profile-name` — Reference to a service-profile that will be applied to the auto provisioned ONU. — *Valores:* Text with up to 48 characters. · *Default:* None.
- `snmp-profile snmp-profile-name` — Reference to snmp-profile that will be applied to the auto provisioned ONU. — *Valores:* Text with up to 48 characters. · *Default:* None.
- `sp-id` — Service Port number. — *Valores:* 1-16 · *Default:* None.
- `gem gem port` — The name of the GEM Port where the service-port must apply. — *Valores:* 1-16 · *Default:* None
- `match vlan vlan-id { user-vlan | any }` — The value of the user VLAN where the service-port must apply. — *Valores:* { user-vlan | any } · *Default:* None
- `action vlan { add vlan-id vid | replace vlan-id vid }` — Adds, replaces or allow a transparent flow for the matched VLAN on network side. add vlan-id vid: Adds the vid VLAN to the packets matched by the user-VLAN; replace vlan-id vid: Replaces the vid VLAN in the packets matched by the user-VLAN; — *Valores:* 1-4094 · *Default:* None
- `action inner-vlan replace vlan-id vid` — Replaces the inner-VLAN for the matched VLAN on network side. replace vlan-id vid: Replaces the vid VLAN in the packets matched by the user-VLAN; — *Valores:* 1-4094 · *Default:* None
- `ethernet ethernet-uni-id` — Specify an ethernet UNI that must be created by the ONU auto provisioning function. Required in order to monitor SNMP OIDs for the ethernet UNI. — *Valores:* 1-4 · *Default:* None
- `native vlan vlan-id` — Configures the VLAN ID to be added for the untagged traffic in the ONU ethernet UNI. — *Valores:* 1-4094 · *Default:* None
- `native vlan vlan-id cos cos-val` — Configures the VLAN ID and CoS for the untagged traffic in the ONU ethernet UNI. — *Valores:* 0-7 · *Default:* 0
- `native downstream-mode { filter-on-vid-only | inverse-of-upstream }` — Configures the tagging action to be applied for downstream native VLAN tagged packets. When filter-on-vid-only value is used, the operation performed in the downstream direction is the inverse of that performed in the upstream direction but only VID match is applied, that is, the VLAN tag of downstream packets matching the same VLAN ID, regardless of their CoS, configured in the native vlan settings will be stripped. When inverse-of-upstream value is used, the operation performed in the downstream direction is the inverse of that performed in the upstream direction, that is, the VLAN tag of downstream packets matching the same VLAN ID and CoS configured in the native vlan settings will be stripped. It’s Important to note that the handling of the packets may differ based on the specific ONU implementation. — *Valores:* { filter-on-vid-only | inverse-of-upstream } · *Default:* filter-on-vid-only
- `veip veip-id` — Specify a VEIP that must be created by the ONU auto provisioning function. — *Valores:* 1 · *Default:* None
- `native vlan vlan-id` — Configures the VLAN ID to be added for the untagged traffic in the ONU VEIP. — *Valores:* 1-4094 · *Default:* None
- `native vlan vlan-id cos cos-val` — Configures the VLAN ID and CoS to be added for the untagged traffic in the ONU VEIP. — *Valores:* 0-7 · *Default:* 0

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. Introduced downstream mode configuration for ethernet UNI. Changed |
| 9.4 | the line profile default of XGSPON platforms from “DEFAULT-LINE” to “DEFAULT-LINE-XGSPON”. |

**Usage Guidelines:**

The following configuration will enable auto provisioning feature and make auto provisioned ONUs with one traffic flow. Example:

```text
DM4610# configure terminal
Entering configuration mode terminal
DM4610(config)# gpon 1/1
DM4610(config-gpon-1/1)# onu-auto-provisioning
DM4610(config-onu-auto-provisioning)# line-profile MY_LINE
```

DM4610(config-onu-auto-provisioning)# service-port 1 gem 1 match vlan vlan-id 10 action vlan replace vlan-id 10 DM4610(config-onu-auto-provisioning)# ethernet 1 native vlan vlan-id 10 Auto provisioned ONUs with RG Profile configuration and IP Host. Example:

```text
DM4610# configure terminal
Entering configuration mode terminal
DM4610(config)# gpon 1/1
DM4610(config-gpon-1/1)# onu-auto-provisioning
DM4610(config-onu-auto-provisioning)# line-profile MY_LINE_VEIP_GEM1_IPHOST_GEM2
DM4610(config-onu-auto-provisioning)# rg-profile RG_WAN_PPPoE_VID_10
```

DM4610(config-onu-auto-provisioning)# ipv4 vlan vlan-id 20 DM4610(config-onu-auto-provisioning)# service-port 1 gem 1 match vlan vlan-id 10 action vlan replace vlan-id 10 DM4610(config-onu-auto-provisioning)# service-port 2 gem 2 match vlan vlan-id 20 action vlan replace vlan-id 20 DM4610(config-onu-auto-provisioning)# veip 1 Disable ONU auto provisioning but keep the base configuration. Example:

```text
DM4610# configure terminal
Entering configuration mode terminal
DM4610(config)# gpon 1/1
DM4610(config-gpon-1/1)# onu-auto-provisioning
DM4610(config-onu-auto-provisioning)# no enable
```

Disable ONU auto provisioning but remove the base configuration. Example:

```text
DM4610# configure terminal
Entering configuration mode terminal
DM4610(config)# gpon 1/1
DM4610(config-gpon-1/1)# no onu-auto-provisioning
```

**Impacts and precautions:**

When auto provisioning is enabled, ONUs are added automatically to database upon an ONU discovery. It is possible that the database configuration may be rejected due to some database validation, such as maximum number of ONUs in the PON link was reached, PON link bandwidth exceeded etc. In those cases, an alarm per GPON interface is raised. The reject cause will be present in the user logs. Once solved the problem, the alarm will be cleared and new ONUs can be added automatically again. If upstream FEC is enabled on the line profile used for auto provisioning, it must also be enabled on all PON links. When using auto provisioning it is recommended to use T-CONT traffic type 4, which has no assured or fixed bandwidths. Using any other type, and depending on the values configured, the PON link may run out of bandwidth and new ONUs will not be correctly provisioned. IMPORTANT NOTE 1: Avoid entering in configuration prompt by using “config exclusive”. Using this mode may cause undesired behavior once auto provisioning feature does commits into the database. Mode “config exclusive” is recommended when ONU configuration must be changed manually by the operator, preventing auto provisioning feature to add ONUs concurrently. IMPORTANT NOTE 2: Even when using default configuration mode, upon commit, the following message may be displayed: “Aborted: the configuration database is locked by session 59 dummy tcp (system from 127.0.0.1). . . ”. This means that there was a commit concurrency with the auto provisioning feature. Try to run commit again.

**Hardware restrictions:**

N/A


### `profile gpon line-profile`

> **Página:** 1652 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Defines the line characteristics of an ONU or of a group of ONUs, such as: • T-CONT and GEM port linkage (GEM port priority included); • T-CONT and Bandwidth Profile linkage; • GEM port Ethernet/iphost/veip mapping (using VLAN and CoS);

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
profile gpon line-profile profile-name [ gem gem-id | tcont tcont-id | upstream-fec ] profile gpon line-profile profile-name gem gem-id [ map map-name { ethernet | iphost | veip } | tcont tcont-id { priority priority-value | gem-traffic-profile profile-name } ] profile gpon line-profile profile-name gem gem-id map map-name [ ethernet {vlan { vlan-id | any} cos { cos-val | any } } profile gpon line-profile profile-name gem gem-id map map-name [ iphost { vlan { vlan-id | any} cos { cos-val | any } } profile gpon line-profile profile-name gem gem-id map map-name [ veip veip-id {vlan { vlan-id | any} cos { cos-val | any } } profile gpon line-profile profile-name tcont tcont-id [ bandwidth-profile bandwidth-profile-name ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `line-profile profile-name` — Indicates the line-profile name. — *Valores:* Text with up to 48 characters. · *Default:* None.
- `tcont tcont-id` — Indicates the ID of the T-CONT. — *Valores:* 1-6. · *Default:* None.
- `bandwidth-profile bandwidth-profile-name` — Indicates the name of a bandwidth-profile to be mapped to the T-CONT. — *Valores:* Text with up to 48 characters. · *Default:* “DEFAULT-BANDWIDTH” for GPON platforms and “DEFAULT-BANDWIDTHXGSPON” for XGSPON platforms.
- `priority priority-value` — Configures a priority for the T-CONT. — *Valores:* 0-7. · *Default:* 0.
- `gem-traffic-profile profile-name` — Indicates the name of a GEM traffic profile to be associated with the GEM port. — *Valores:* Text with up to 48 characters. · *Default:* None.
- `upstream-fec` — Enables forwarding of error correction for upstream flow. — *Valores:* None. · *Default:* None.
- `gem gem-id` — Indicates the ID to identify the GEM port list. — *Valores:* 1-16. · *Default:* None.
- `map map-name` — Indicates the name for the UNI port mapping. — *Valores:* Text with up to 48 characters. · *Default:* None.
- `ethernet { eth-val | any }` — Ethernet ports to be mapped to a GEM port. To use all Ethernet ports, set any. The syntax for a range is 1-3, to use the ports 1 to 3 or 1,2,4 to use the ports 1, 2 and 4. — *Valores:* { 1-4 | any } · *Default:* None.
- `iphost` — Indicates iphost type of mapping to a GEM port. — *Valores:* None. · *Default:* None.
- `veip { veip-id }` — VEIP port to be mapped to a GEM port. — *Valores:* VEIP values: 1. · *Default:* None.
- `vlan { vlan-id | any }` — VLAN ID to be mapped to a GEM port. To use all VLAN IDs, set any. Use value any in conjunction with service-port match any for untagged traffic. — *Valores:* { 1-4094 | any } · *Default:* None.
- `cos { cos-val | any }` — CoS values that will be taken into account by the GEM port. To use all CoS values, set any. The syntax for a range is 0-3, to use the CoS values 0 to 3, or 1,2,4 to use the CoS 1, 2 and 4. — *Valores:* { 0-7 | any } · *Default:* None.

**Default:** N/A.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.4 | The the maximum GEM ID value was changed from 40 to 16. |
| 1.8 | The VEIP configuration command was added. |
| 1.8.2 | Default profiles were added. Changed the bandwidth Profile default of XGSPON platforms from 9.4 “DEFAULT-BANDWIDTH” to “DEFAULT-BANDWIDTH-XGSPON”. |

**Usage Guidelines:**

Create a Bandwidth Profile before binding to a T-CONT by using command profile gpon bandwidth-profile bandwidth-profile-name and configure a traffic type. See bandwidth-profile page. Bind a Bandwidth Profile to a T-CONT before mapping GEM ports. To set interface line profile is necessary to enter in the line profile menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# profile gpon line-profile lineProfName
(config-line-profile-lineProfName)#
```

The mapping of Ethernet ports to a GEM port is done through line profile menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# profile gpon line-profile lineProfName
(config-line-profile-lineProfName)#tcont 1 bandwidth-profile bw1
(config-line-profile-lineProfName)#gem 1
(config-line-prof-gem-1)#gem 1
(config-line-prof-gem-1)# tcont 1 priority 0
(config-line-prof-gem-1)# map map1
(config-line-prof-gem-map-map1)# ethernet 1 vlan 400 cos 0
```

Ethernet ports mapping accepts range. Example:

```text
(config-line-prof-gem-1)# map map1
(config-line-prof-gem-map-map1)# ethernet 1-2,4 vlan 400 cos 0
```

The mapping of IPHOST port to a GEM port is done through line profile menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# profile gpon line-profile lineProfName
(config-line-profile-lineProfName)#tcont 1 bandwidth-profile bw1
(config-line-profile-lineProfName)#gem 1
(config-line-prof-gem-1)#gem 1
(config-line-prof-gem-1)# tcont 1 priority 0
(config-line-prof-gem-1)# map map1
(config-line-prof-gem-map-map1)# iphost vlan 400 cos 0
```

The mapping of VEIP port to a GEM port is done through line profile menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# profile gpon line-profile lineProfName
(config-line-profile-lineProfName)#tcont 1 bandwidth-profile bw1
(config-line-profile-lineProfName)#gem 1
(config-line-prof-gem-1)#gem 1
(config-line-prof-gem-1)# tcont 1 priority 0
(config-line-prof-gem-1)# map map1
(config-line-prof-gem-map-map1)# veip 1 vlan 500 cos 0
```

Some third-party ONUs may not support native VLAN configuration on Ethernet UNI. To use untagged traffic set line-profile match VLAN to any and use service-port match any with action add, this will work as a native VLAN on the service-port.

**Impacts and precautions:**

The sum of the rates of the bandwidth-profiles of the line-profile must not exceed the ponlink capacity (1.25 Gbps). For DM4610 platform, line profile cannot have more than 3 TCONTs with bandwidth traffic type 2 to 5 and 3 TCONTs with bandwidth traffic type 1. For DM4610-HW2/DM4615 platforms, line profile cannot have more than 4 TCONTs with bandwidth traffic type 2 to 5 and 3 TCONTs with bandwidth traffic type 1. Configuring one gem map with vlan any and another gem map, with the same ports, with a specific vlan will result in undefined behavior because it is not guaranteed which mapping will match first. Example of an invalid profile: profile gpon line-profile invalid upstream-fec tcont 1 bandwidth-profile DEFAULT-BANDWIDTH gem 1 tcont 1 priority 0 map service-1 ethernet any vlan 100 cos any gem 2 tcont 1 priority 0 map service-2 ethernet any vlan any cos any It is also not valid to use vlan any on more than one gem map for the same group of ports. Example of an invalid profile: profile gpon line-profile invalid upstream-fec tcont 1 bandwidth-profile DEFAULT-BANDWIDTH gem 1 tcont 1 priority 0 map service-1 ethernet any vlan any cos any gem 2 tcont 1 priority 0 map service-2 ethernet any vlan any cos any When using an ONU with more than one Ethernet interface, the group of ports in a gem map should not have an intersection with another gem map, though it can be the same. Example of an invalid profile: profile gpon line-profile invalid upstream-fec tcont 1 bandwidth-profile DEFAULT-BANDWIDTH gem 1 tcont 1 priority 0 map ethernets1 ethernet 1-2 vlan 100 cos any gem 2 tcont 1 priority 0 map ethetnets2 ethernet 2-4 vlan 200 cos any Example of a valid profile: profile gpon line-profile invalid upstream-fec tcont 1 bandwidth-profile DEFAULT-BANDWIDTH gem 1 tcont 1 priority 0 map ethernets1 ethernet 1-2 vlan 100 cos any gem 2 tcont 1 priority 0 map ethetnets2 ethernet 1-2 vlan 200 cos any It is recommended to use only one gem map for each GEM port because some ONUs may not support configuring more than one mapping for each GEM. With the exception of having a gem map for Ethernet and one for VEIP on the same GEM port, because the ONU will effectively only use one of them.

**Hardware restrictions:**

None


### `rg-one-shot-prov`

> **Página:** 1659 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures RG Profile One-shot Provisioning. When enabled, OLT sends RG profile to ONUs only once, so any further user configuration on ONUs is not overwritten by the OLT. When disabled, RG profile configuration is always sent to the associated ONUs, whenever they go online to the OLT. In this case, local changes in the ONU configuration (i.e. through its WEB interface) can be lost.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
rg-one-shot-prov
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.9 | This command was introduced. |

**Usage Guidelines:**

To enable rg-one-shot-prov it is necessary to enter in the given gpon card menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# gpon 1/1
(config-gpon-1/1)# rg-one-shot-prov
```

To force the reprovisioning of an ONU, see command rg-reprovision.

**Impacts and precautions:**

RG Profile will not be issued automatically in the following situations: 1) Enabling or disabling rg-one-shot-prov flag. 2) RG Profile switch to another RG Profile in an ONU. 3) Any change in rg-profile-override-settings in an ONU. 4) When the user makes a factory-reset locally at the ONU. To re-provision RG Profile to ONU, the command rg-reprovision, available on the onu configuration tree, must be used.

**Hardware restrictions:**

N/A


### `service vlan block`

> **Página:** 1661 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Command used to configure service flood blocking on preexisting VLAN type n:1.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616.

**Syntax:**

```text
service vlan { vlan-id } [ block traffic-type ]*
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vlan vlan-id` — ID of VLAN to be configured. — *Valores:* 1 - 4094 · *Default:* None
- `block traffic-type` — Block downstream flood traffic on configured VLAN. This configuration is only applied on VLAN type n:1. The value broadcast blocks broadcast traffic. The value multicast blocks unknown multicast traffic. The value unicast blocks unknown unicast traffic. — *Valores:* {broadcast | multicast | unicast} · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. |

**Usage Guidelines:**

VLAN must be created and configured to type n:1 to configure a service block for it. The commit of a configuration with a service block on a non existing VLAN will result in an error message and the configuration won’t be applied. Changing service type to other than n:1 will erase any previous service block configuration. Default behaviour of VLANs is not to block any traffic.

**Impacts and precautions:**

This command only applies on VLANs type n:1. Only with pre-existing VLANs the configuration commit will be successful.

**Hardware restrictions:**

N/A


### `service vlan type`

> **Página:** 1663 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Command used to configure service type on preexisting VLAN.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
service vlan { vlan-id } [ type service-type ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vlan vlan-id` — ID of VLAN to be configured. — *Valores:* 1 - 4094 · *Default:* None
- `type service-type` — Service type configured on VLAN. — *Valores:* {n:1 | 1:1 | tls} · *Default:* n:1

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.2 | This command was introduced. |

**Usage Guidelines:**

VLAN must be created to configure a service for it. The commit of a configuration with a service type on a non existing VLAN will result in an error message and the configuration won’t be applied.

**Impacts and precautions:**

Some packets might be lost when this configuration is applied due to changes on VLAN behavior. Only with pre-existing VLANs the configuration commit will be successful.

**Hardware restrictions:**

N/A


### `service-port`

> **Página:** 1665 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Individualizes the data flow for each user, allowing the passthrough of this traffic and even do VLAN translation on it. It is used to connect the network side and the user device side.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
service-port rule-id service-port new { gpon | xgspon } ponlink onu onu-id gem gem port [ match vlan vlan-id { user-vlan | any } action { vlan { add vlan-id vid | replace vlan-id vid } } [ inner-vlan replace vlan-id vid ] ] [ description description-text ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `service-port rule-id` — Enters the service-port configuration. ID of the rule to create. Must be unique for all service-ports. The “rule-id” can be used in a range format to show the active configuration of some service ports. — *Valores:* 1-16777215 · *Default:* None.
- `service-port new` — Enters the service-port configuration. ID is automatically selected (lowest free ID). — *Valores:* None. · *Default:* None.
- `{ gpon | xgspon } ponlink` — Value of the ponlink where the service-port must apply. — *Valores:* chassi/slot/port · *Default:* None.
- `onu onu-id` — The ID of the ONU where the service-port must apply. — *Valores:* 0-127 · *Default:* None
- `gem gem port` — The name of the GEM Port where the service-port must apply. — *Valores:* 1-16 · *Default:* None
- `match vlan vlan-id { user-vlan | any }` — The value of the user VLAN where the service-port must apply. — *Valores:* { user-vlan | any } · *Default:* None
- `action vlan { add vlan-id vid | replace vlan-id vid }` — Adds, replaces or allow a transparent flow for the matched VLAN on network side. add vlan-id vid: Adds the vid VLAN to the packets matched by the user-VLAN, if using match any this will work as a native VLAN; replace vlan-id vid: Replaces the vid VLAN in the packets matched by the user-VLAN; — *Valores:* 1-4094 · *Default:* None
- `action inner-vlan replace vlan-id vid` — Replaces the inner-VLAN for the matched VLAN on network side. replace vlan-id vid: Replaces the vid VLAN in the packets matched by the user-VLAN; — *Valores:* 1-4094 · *Default:* None
- `description description-text` — A textual description of the service-port. — *Valores:* Text up to 128 characters. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. The “rule-name” parameter of the service-port command was changed to “rule-id”. The “line-profile” parameter was removed from the service-1.4 port command. The the maximum GEM ID value was changed from 40 to 16. The “service-port new” command was added to automatically allocate |
| 5.6 | the “rule-id”. The “description” command was added. Line breaks was inserted between gpon, match, action and description commands. The line breaks between commands below service-port when shown run5.8 ning configuration was removed. |
| 9.0 | Added support for some special characters on interface description. |

**Usage Guidelines:**

To set a service-port it is necessary to enter in the config menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# service-port 1 gpon 1/1/1 onu 1 gem 1 match vlan vlan-id 10
action vlan replace vlan-id 100
```

Some third-party ONUs may not support native VLAN on Ethernet UNI, a possible workaround is to use match vlan vlan-id any with action vlan add, thus doing the native VLAN on the service-port. Note that it is also necessary to use vlan any on the line-profile for the ONU used on this service-port for untagged traffic to work. To use a service-port as an access port for a MPLS tunnel, VLAN translate must not be configured. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# service-port 1 gpon 1/1/1 onu 1 gem 1
```

Service-port parameters can be entered in a line after service-port command. Use “new” to select the first free index automatically. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# service-port 1
(config-service-port-1)# gpon 1/1/1 onu 1 gem 1 match vlan vlan-id 10 action vlan replace vlan-id 100 description customer1-internet
(config)# service-port new
(config-service-port-2)# gpon 1/1/1 onu 2 gem 1 match vlan vlan-id 10 action vlan replace vlan-id 100 description customer2-internet
```

Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# service-port 1
(config-service-port-2)# gpon 1/1/1 onu 2 gem 1 match vlan vlan-id 10 action vlan replace vlan-id 100 description "test_interface_name|!?;"
```

**Impacts and precautions:**

No flow is allowed through OLT without a service-port rule. Up to 32768 service-ports can be configured on DM4618 platform. On other platforms, up to 4096 service-ports can be configured. A gem port that is associated to a service-port used for MPLS services should not be used in other service-ports. Service-ports without match and action configuration must be used only for MPLS services.

**Hardware restrictions:**

None


### `show interface gpon`

> **Página:** 1670 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays GPON interface information. Regarding the discovered ONUs show operation, an ONU is only displayed if it discovered in the GPON port but not provisioned. Once an ONU is provisioned, it is no longer displayed.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
show interface gpon [ chassis/slot/port ] [ brief | statistics | detail | discovered-onus ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `chassis/slot/port` — The ponlink to display information. — *Valores:* Text: chassis/slot/port format. · *Default:* N/A
- `brief` — Display brief information of the GPON interface. — *Valores:* brief: Fixed text ‘brief’. · *Default:* N/A
- `statistics` — Display statistics information of the GPON interface. — *Valores:* statistics: Fixed text ‘statistics’. · *Default:* N/A
- `detail` — Display detailed information of the GPON interface. — *Valores:* detail: Fixed text ‘detail’. · *Default:* N/A
- `discovered-onus` — Display discovered ONUs. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 2.4 | Added more information to usage guidelines and output parameters. |
| 4.2.0 | Added support for range of IDs in show options. |
| 10.4.0 | Downstream-fec default value was changed to false for GPON ports. |

**Usage Guidelines:**

Show gpon 1/1/1 information

```text
# show interface gpon 1/1/4
```

Physical interface : gpon 1/1/4, Enabled, Physical link is Up Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : neophotonics-b Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 439449 kbit/s Total BW : 1098624 kbit/s Show all gpon interfaces information

```text
# show interface gpon
```

Physical interface : gpon 1/1/1, Disabled, Physical link is Down Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 1106944 kbit/s Overhead : 33 kbit/s (1 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : gpon 1/1/2, Disabled, Physical link is Down Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : gpon 1/1/3, Disabled, Physical link is Down Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : gpon 1/1/4, Disabled, Physical link is Down Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Show all gpon interfaces information

```text
# show interface gpon *
```

Physical interface : gpon 1/1/1, Disabled, Physical link is Down Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 1106944 kbit/s Overhead : 33 kbit/s (1 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : gpon 1/1/2, Disabled, Physical link is Down Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : gpon 1/1/3, Disabled, Physical link is Down Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : gpon 1/1/4, Disabled, Physical link is Down Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Show a range of gpon interfaces information

```text
# show interface gpon 1/1/3-4
```

Physical interface : gpon 1/1/3, Disabled, Physical link is Down Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Physical interface : gpon 1/1/4, Disabled, Physical link is Down Link-level type : GPON Logical reach : 0-40 km Downstream FEC : Disabled Upstream FEC : Enabled Transceiver type : none Allocated upstream bandwidth Fixed + Assured : 0 kbit/s Fixed : 0 kbit/s Assured : 0 kbit/s Max : 0 kbit/s Overhead : 0 kbit/s (0 ONUs) Available upstream bandwidth CBR BW : 0 kbit/s Total BW : 0 kbit/s Show all gpon interfaces information (brief option)

```text
# show interface gpon brief
```

Interface DS FEC US FEC Admin Link Transceiver type -------------------------------------------------------------------------------- 1/1/1 Disabled Enabled Disabled Down none 1/1/2 Disabled Enabled Disabled Down none 1/1/3 Disabled Enabled Disabled Down none 1/1/4 Disabled Enabled Disabled Down none Show all gpon interfaces information (brief option)

```text
# show interface gpon * brief
```

Interface DS FEC US FEC Admin Link Transceiver type -------------------------------------------------------------------------------- 1/1/1 Disabled Enabled Disabled Down none 1/1/2 Disabled Enabled Disabled Down none 1/1/3 Disabled Enabled Disabled Down none 1/1/4 Disabled Enabled Enabled Up neophotonics-b Show all gpon interfaces in a given chassis/slot information (brief option)

```text
# show interface gpon 1/1/* brief
```

Interface DS FEC US FEC Admin Link Transceiver type -------------------------------------------------------------------------------- 1/1/1 Disabled Enabled Disabled Down none 1/1/2 Disabled Enabled Disabled Down none 1/1/3 Disabled Enabled Disabled Down none 1/1/4 Disabled Enabled Enabled Up neophotonics-b Show a range of gpon interfaces information (brief option)

```text
# show interface gpon 1/1/2-3 brief
```

Interface DS FEC US FEC Admin Link Transceiver type -------------------------------------------------------------------------------- 1/1/2 Disabled Enabled Disabled Down none 1/1/3 Disabled Enabled Disabled Down none Show a list of gpon interfaces information (brief option)

```text
# show interface gpon 1/1/1,3 brief
```

Interface DS FEC US FEC Admin Link Transceiver type -------------------------------------------------------------------------------- 1/1/1 Disabled Enabled Disabled Down none 1/1/3 Disabled Enabled Disabled Down none Show discovered ONUs in all gpon interfaces

```text
# show interface gpon discovered-onus
```

Chassis / Slot / Port Serial Number --------------------- ------------- 1/1/1 DACM00000351 1/1/3 DACM00000352 Show discovered ONUs in all gpon interfaces

```text
# show interface gpon * discovered-onus
```

Chassis / Slot / Port Serial Number --------------------- ------------- 1/1/1 DACM00000351 1/1/3 DACM00000352 Show discovered ONUs in all gpon interfaces in a given chassis/slot

```text
# show interface gpon 1/1/* discovered-onus
```

Chassis / Slot / Port Serial Number --------------------- ------------- 1/1/1 DACM00000351 1/1/3 DACM00000352 Show discovered ONUs in a range of gpon interfaces

```text
# show interface gpon 1/1/1-3 discovered-onus
```

Chassis / Slot / Port Serial Number --------------------- ------------- 1/1/1 DACM00000351 1/1/3 DACM00000352 Show statistics of all gpon interfaces using table mode

```text
# show interface gpon * | tab | select statistics
CHASSIS
```

ID/SLOT IN IN IN IN OUT OUT OUT ID/PORT IN UNICAST BROADCAST MULTICAST IN IN UNKNOWN OUT UNICAST BROADCAST MULTICAST OUT OUT I-D--------O-C-T-E-T-S---P-K-T-S------P-K-T-S--------P-K-T-S--------D-I-S-C-A-R-D-S---E-R-R-O-R-S---P-R-O-T-O-S----O-C-T-E-T-S---P-K-T-S------P-K-T-S--------P-K-T-S--------D-I-S-C-A-R-D-S---E-R-R-O-R-S--- 1/1/1 0 0 0 0 0 0 0 0 0 0 0 0 0 1/1/2 0 0 0 0 0 0 0 0 0 0 0 0 0 1/1/3 0 0 0 0 0 0 0 0 0 0 0 0 0 1/1/4 0 0 0 0 0 0 0 0 0 0 0 0 0

**Output Terms:**

Output Description Physical interface Name and status of the GPON interface. Link-level type Type of the Link-level. Logical reach Show the interface differential logical reach (in kilometers). Downstream FEC Downstream FEC status. Upstream FEC Upstream FEC status. Transceiver type Type of the transceiver. Allocated upstream Header for the types of bandwidth allocated. bandwidth Fixed + Assured Allocated bandwidth of both Fixed and Assured types added. Fixed Allocated bandwidth of Fixed type. Assured Allocated bandwidth of Assured type. Output Description Max Allocated bandwidth of Maximum type. Allocated bandwidth for inband management of all ONUs on the Overhead GPON interface. ONUs Number of ONUs configured on the GPON interface. Available upstream Header for the types of available upstream bandwidth. bandwidth CBR BW Available fixed bandwidth (traffic type-1 and type-5) in the ponlink. Available total bandwidth (assured+fixed; traffic type-1, type-2, Total BW type-3 and type-5) in the ponlink.

**Impacts and precautions:**

It is not supported to use commas in the key wildcard in gpon interface discovered-onus show option ( show interface gpon 1/1/2,3,4 discovered-onus ).

**Hardware restrictions:**

N/A ONU PROFILES This topic describes the ONU profiles commands related to ONU traffic configuration, such as line and service profiles.


## ONU Profiles

### `profile gpon bandwidth-profile`

> **Página:** 1678 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The bandwidth-profile is used to enter in bandwidth-profile mode and manage the dynamic allocation of bandwidth for upstream flow. In this mode is possible to choose the traffic type between type-1 to type-5. The no profile gpon bandwidth-profile command is used to delete a specific bandwidth profile.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
profile gpon bandwidth-profile profile-name traffic { type-1 fixed-bw fixed-bandwidth | type-2 assured-bw assured-bandwidth | type-3 assured-bw assured-bandwidth max-bw max-bandwidth | type-4 max-bw max-bandwidth | type-5 fixed-bw fixed-bandwidth assured-bw assured-bandwidth max-bw max-bandwidth }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `bandwidth-profile profile-name` — Name of the profile to create. Must be unique for all bandwidth-profiles. Can have up to 48 characters. — *Valores:* Text: up to 48 characters. · *Default:* None
- `traffic type-1` — Fixed bandwidth. Type-1 defines a fix bandwidth that will be fully allocated to a T-CONT. Although the user is not using the bandwidth it will not be shared with another user. Used for constant traffic with high relevance for jitter and delay parameters. VoIP for instance. — *Valores:* See fixed-bw parameter values. · *Default:* None
- `traffic type-2` — Assured bandwidth. Type-2 defines an assured bandwidth that will be allocated at the moment an ONU requires the bandwidth. The bandwidth that is not in use by the user will be shared with another ONU. — *Valores:* See assured-bw parameter values. · *Default:* None
- `traffic type-3` — Assured + maximum bandwidth. Type-3 bandwidth defines an assured bandwidth (can be shared when not in use) and an additional maximum limit (not assured) that the bandwidth can reach. Used for variable rates services for guaranteing an average rate. This type is mainly used for VoIP services. — *Valores:* See assured-bw and max-bw parameters values. · *Default:* None
- `traffic type-4` — Max bandwidth. Type-4 defines a maximum bandwidth (not assured) that can be reached in the T-CONT. Used for variable traffic services that does not take in count jitter or delay like Internet and low priority services. — *Valores:* See max-bw parameter values. · *Default:* None
- `traffic type-5` — Fixed + assured + max bandwidth. Type-5 defines the user will have a guaranteed bandwidth, an assured bandwidth that can be occupied when necessary and a maximum bandwidth that the user can reach. — *Valores:* See fixed-bw, assured-bw and max-bw paremeters values. · *Default:* None
- `fixed-bw fixed-bandwidth` — Fixed bandwidth defines a bandwidth that cannot be shared when allocated. — *Valores:* type-1: (GPON Platform) Number from 512 to 442752 kbit/s in steps of 64. (XGSPON Platform) Number from 512 to 9953280 kbit/s in steps of 128. type-5: (GPON Platform) Number from 128 to 442752 kbit/s in steps of 64. (XGSPON Platform) Number from 128 to 9953280 kbit/s in steps of 128. type-5 for DM4610HW2: (GPON Platform) Number from 256 to 442752 kbit/s in steps of 64. (XGSPON Platform) Number from 256 to 9953280 kbit/s in steps of 128. · *Default:* None
- `assured-bw assured-bandwidth` — Assured bandwidth defines a bandwidth that can be shared between users. — *Valores:* (GPON Platform) Number from 256 to 1106816 kbit/s in steps of 64. (XGSPON Platform) Number from 256 to 9953280 kbit/s in steps of 128. · *Default:* None
- `max-bw max-bandwidth` — Max bandwidth defines the bandwith the user can reach. — *Valores:* type-3: (GPON Platform) Number from 384 to 1106944 kbit/s in steps of 64. (XGSPON Platform) Number from 384 to 9953280 kbit/s in steps of 128. type-4: (GPON Platform) Number from 128 to 1106944 kbit/s in steps of 64. (XGSPON Platform) Number from 128 to 9953280 kbit/s in steps of 128. type-4 for DM4610HW2: (GPON Platform) Number from 128 to 1106944 kbit/s in steps of 64. (XGSPON Platform) Number from 256 to 9953280 kbit/s in steps of 128. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. The maximum allowed bandwidth value for type bandwidths 1,2,3,4 and 9.0 |
| 5 | increased to 10Gbps for XGSPON plataforms. |

**Usage Guidelines:**

When using traffic type-3, maximum bandwidth must be greater than or equal to assured bandwidth + 128 kbit/s. When using traffic type-5, assured bandwidth must be greater than or equal to fixed bandwidth + 128 kbit/s and max bandwidth must be greater or equal to fixed + assured + 128 kbit/s. When using DM4610HW2 and traffic type-3, maximum bandwidth must be greater than or equal to assured bandwidth + 256 kbit/s. When using DM4610HW2 and traffic type-5, assured bandwidth must be greater than or equal to fixed bandwidth + 256 kbit/s and max bandwidth must be greater or equal to fixed + assured + 256 kbit/s. When using DM4616, configurable bandwidth values for traffic types 1, 2, 3, 4 and 5 need to be divisible by 128 for port operating in GPON or XGSPON mode. To set a bandwith profile it is necessary to enter in bandwith profile menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# profile gpon bandwidth-profile bwProfName
(config-bandwidth-profile-bwProfName)# traffic type-1 fixed-bw 512
```

**Impacts and precautions:**

The profile cannot be modified after it is committed.

**Hardware restrictions:**

N/A


### `profile gpon gem-traffic-profile`

> **Página:** 1684 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Defines rate-limiting parameters to be associated with a GEM port, such as commited information rate (CIR), excess information rate (EIR) and upstream GEM priority.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
profile gpon gem-traffic-profile profile-name { cir rate | eir rate | upstream-gempriority priority-value }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `gem-traffic-profile profile-name` — Name of the GEM traffic profile. — *Valores:* String (1-48 characters). · *Default:* None
- `cir rate` — Committed information rate (CIR) in steps of 64 kbit/s. — *Valores:* 64-2499968 · *Default:* None
- `eir rate` — Excess information rate (EIR) in steps of 64 kbit/s. — *Valores:* 0-2499904 · *Default:* None
- `upstream-gem-priority priority-value` — Upstream GEM port priority. — *Valores:* 0-7 · *Default:* 0

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. |

**Usage Guidelines:**

In order to configure a GEM traffic profile, it is necessary to enter the gem-traffic-profile menu. Both CIR and EIR parameters must be specified, and their sum cannot exceed 2499968 kbit/s. The total rate, also known as PIR (Peak Information Rate), is the sum of CIR and EIR. The profile cannot be modified after it is committed. The profile cannot be deleted if it is referenced by a line profile. In order for the profile to be effective, it must be referenced by a line profile. The rate-limiting configuration specified by the profile is applied in both upstream and downstream directions. Example:

```text
# config terminal
Entering configuration mode terminal
(config)# profile gpon gem-traffic-profile gemTrProfName
(config-gem-traffic-profile-gemTrProfName)# cir 10240
(config-gem-traffic-profile-gemTrProfName)# eir 5120
(config-gem-traffic-profile-gemTrProfName)# upstream-gem-priority 2
```

**Impacts and precautions:**

Some ONU models may not support GEM traffic profile. Check the ONU datasheet for reference.

**Hardware restrictions:**

N/A


### `profile gpon media-profile`

> **Página:** 1687 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The media-profile command is used to configure media parameters for VoIP services, allowing the user to set a priority ordered codec list, where is set the codec type, packet-period and silence-suppression for each entry on the list. Media-profile command is also used to enable/disable out-of-band DTMF, configure the target of the jitter buffer, and the maximum depth of the jitter buffer.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
profile gpon media-profile { media-profile-name [ codec-order order-index { type codec-type | packet-period packet-period-value | silence-suppression } | jitter { target { dynamic-buffer | buffer target-buffer-value } | maximum { onu-internalbuffer | buffer maximum-buffer-value } } | oob-dtmf | pstn-protocol-variant countrycode-value] }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `media-profile media-profile-name` — Indicates the media profile name. — *Valores:* String: up to 48 characters. · *Default:* None.
- `codec-order order-index` — Indicates the codec selection order which will be configured. The list can be filled in any order. — *Valores:* 1-4 · *Default:* None.
- `type codec-type` — Select the codec type defined by IETF RFC 3551. — *Valores:* cn | dvi4-8000 | dvi4-11025 | dvi4-16000 | dvi4-22050 | gsm | g722 | g723 | g728 | g729 | lpc | l16-2-channel | l16-1-channel | mpa | pcma | pcmu | qcelp. · *Default:* pcma.
- `packet-period packet-period-value` — Select the packet period interval in milliseconds. — *Valores:* 10-30 milliseconds. · *Default:* 10 milliseconds.
- `silence-suppression` — Enable or disable silence suppression for the codec entry. — *Valores:* None. · *Default:* Disable.
- `jitter target dynamic-buffer` — Set the target value of the jitter buffer as dynamic. — *Valores:* N/A · *Default:* None.
- `jitter target buffer target-buffer-value` — Select the target value of the jitter buffer in milliseconds. — *Valores:* 1-65535 milliseconds. · *Default:* 135 milliseconds.
- `jitter maximum onu-internal-buffer` — Configure the ONU to use its internal default value for the maximum jitter buffer. — *Valores:* N/A · *Default:* None.
- `jitter maximum buffer maximum-buffer-value` — Select the maximum depth of the jitter buffer in milliseconds. — *Valores:* 1-65535 milliseconds. · *Default:* 135 milliseconds.
- `oob-dtmf` — Enable or disable out-of-band DTMF. When enabled, DTMF signals are carried out-of-band. When disabled, DTMF signals are carried in the PCM stream. — *Valores:* None. · *Default:* Disable.
- `pstn-protocol-variant country-code-value` — Configure PSTN protocol variant (Country Codes). This parameter controls which variant of POTS signalling is used. — *Valores:* AGO | ARE | ARG | AUS | AUT | BEL | BOL | BRA | CHE | CHL | CHN | COL | CYP | CZH | DEU | DNK | ECU | EGY | ESP | FIN | FRA | GBR | GHA | HKG | HUN | IND | IRL | ITA | JPN | KOR | MAR | MEX | NLD | NOR | NZL | PER | POL | PRY | ROU | SVK | SVN | SWE | TUN | TWN | URY | USA | VEN | ZAF. · *Default:* None.

**Default:** None.

**History:**

| Release | Modification |
| --- | --- |
| 1.12 | This command was introduced. |

**Usage Guidelines:**

To set the media profile it is necessary to enter in the media-profile menu. Example:

```text
# config
Entering configuration mode terminal
(config)# profile gpon media-profile mediaName
(config-media-profile-mediaName)# pstn-protocol-variant BRA
(config-media-profile-mediaName)# jitter target dynamic-buffer
(config-media-profile-mediaName)# jitter maximum buffer 30000
(config-media-profile-mediaName)# codec-order 1
(config-codec-order-1)# type pcma
(config-codec-order-1)# codec-order 2
(config-codec-order-2)# type g723
(config-codec-order-2)# codec-order 3
(config-codec-order-3)# type g729
(config-codec-order-3)# codec-order 4
(config-codec-order-4)# type pcmu
(config-codec-order-4)# packet-period 20
```

**Impacts and precautions:**

First check the ONU capabilities before configuring the codec list, because some ONU models do not support all the codecs listed. There must be 4 codecs configured in a Media Profile. When there is no pstn-protocol-variant configured, the ONU must use its internal default.

**Hardware restrictions:**

None.


### `profile gpon onu-profile`

> **Página:** 1691 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Defines the amount of each type of port of an ONU or a group of ONUs.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

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
| 1.0 | This command was introduced. |
| 1.8 | Configuration of number of VEIPs was added. |

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

N/A


### `profile gpon rg-profile`

> **Página:** 1694 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The rg-profile (residential gateway) is used to enter in rg-profile mode and manage the ONU DM984-42x WAN, LAN and WLAN configuration through the OLT. DM985-100 ONU also supports the rg-profile configuration, but some parameters may not be fully supported. Check DM985-100 release notes for reference. The no profile gpon rg-profile command is used to delete a specific RG profile.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
profile gpon rg-profile profile-name wan-pppoe-connection connection-name [ auth-type { auto | chap | mschap | pap } | firewall | fullcone-nat | multicast-proxy { igmp } | multicast-source { igmp } | nat | username username | password password | vlan-mux vlan vlan-id cos cos tpid tpid ] wan-ip-connection connection-name [ firewall | fullcone-nat | multicast-proxy { igmp } | multicast-source { igmp } | nat | vlan-mux vlan vlan-id cos cos tpid tpid | ipv4 { dhcp | static default-gateway def-gw-addr } ] wan-bridge-connection connection-name [ multicast-source { igmp } | vlan-mux vlan vlan-id cos cos tpid tpid ] wlan wlan-name [ network-auth { open | wpa2-psk | wpa2/wpa-psk } | ssid { auto { onu-serial-number { prefix prefix | suffix sufix } } | custom ssid } | wpa-encryption { aes | tkip+aes } | wpa-passphrase wpa-passphrase ] wan-pppoe-connection connection-name [ itf-grouping [ dhcp-server | dhcp-server-address-pool start-address starting-ip-address end-address ending-ip-address | igmp-snooping | ipv4 address ip-addr netmask addr-netmask | ports { eth1 | eth2 | eth3 | eth4 | wl0 | wl0-vap1 } [ vlan vlan-id cos cos ] ] ] wan-ip-connection connection-name [ itf-grouping [ dhcp-server | dhcp-server-address-pool start-address starting-ip-address end-address ending-ip-address | igmp-snooping | ipv4 address ip-addr netmask addr-netmask | ports { eth1 | eth2 | eth3 | eth4 | wl0 | wl0-vap1 } [ vlan vlan-id cos cos ] ] ] wan-bridge-connection connection-name [ itf-grouping [ igmp-snooping | ipv4 address ip-addr netmask addr-netmask | ports { eth1 | eth2 | eth3 | eth4 | wl0 | wl0-vap1 } [ vlan vlan-id cos cos ] ] ] wan-pppoe-connection connection-name [ ip-filtering priority filtering-type action act match [ destination-ip-address dest-addr | source-ip-address src-addr | protocol proto | source-port { port | port-proto | range start start-port stop stop-port } | destination-port { port | port-proto | range start start-port stop stop-port } ] ] wan-ip-connection connection-name [ ip-filtering priority filtering-type action act match [ destination-ip-address dest-addr | source-ip-address src-addr | protocol proto | source-port { port | port-proto | range start start-port stop stop-port } | destination-port { port | port-proto | range start start-port stop stop-port } ] ] user-mgmt [ priv-lvl-support | priv-lvl-user ] password { auto { onu-serial-number { prefix prefix | suffix sufix } } | custom password }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `rg-profile profile-name` — Name of the profile to create. Must be unique within all RG profiles. Can have up to 48 characters. — *Valores:* Text: up to 48 characters. · *Default:* None
- `wan-pppoe-connection connection-name` — WAN PPPoE connection configuration. Each connection represents a WAN connection in the ONU. — *Valores:* Text: up to 48 characters. · *Default:* None
- `auth-type { auto | chap | mschap | pap }` — PPPoE authentication type. — *Valores:* auto, chap, mschap or pap. · *Default:* auto
- `firewall` — Enables firewall for the PPPoE WAN interface. — *Valores:* None. · *Default:* no firewall
- `fullcone-nat` — Enables fullcone NAT for the PPPoE WAN interface. — *Valores:* None. · *Default:* no fullcone-nat
- `multicast-proxy { igmp }` — Enables IGMP multicast proxy for the PPPoE WAN interface. IGMP multicast source must be enabled too. — *Valores:* None. · *Default:* no multicast-proxy igmp
- `multicast-source { igmp }` — Enables IGMP multicast source for the PPPoE WAN interface. — *Valores:* None. · *Default:* no multicast-source igmp
- `nat` — Enables NAT for the PPPoE WAN interface. — *Valores:* None. · *Default:* nat
- `password password` — PPPoE connection password. — *Valores:* Text: up to 32 characters. · *Default:* None.
- `username username` — PPPoE connection username. — *Valores:* Text: up to 64 characters. · *Default:* None.
- `service-name service-name` — PPPoE connection service name. — *Valores:* Text with up to 32 characters. · *Default:* None.
- `vlan-mux vlan vlan-id` — VLAN ID to be used for the WAN PPPoE interface. — *Valores:* 1-4094. · *Default:* None.
- `vlan-mux cos cos` — CoS to be used for the WAN PPPoE interface. — *Valores:* 0-7. · *Default:* 0.
- `vlan-mux tpid tpid` — TPID to be used for the WAN PPPoE interface. — *Valores:* 0x88a8, 0x8100 or 0x9100. · *Default:* 0x8100.
- `wlan wlan-name` — WLAN interface. It can be a physical interface (wl0) or virtual access points (wl0-vpax). — *Valores:* wl0 (refers to the physical wlan interface), wl0-vap1 (Virtual access point 1), wl0-vap2 (Virtual access point 2), wl0-vap3 (Virtual access point 3). · *Default:* None
- `network-auth { open | wpa2-psk | wpa2/wpa-psk }` — Wireless LAN network authentication method. — *Valores:* open, wpa2-psk or wpa2/wpa-psk. · *Default:* wpa2/wpa-psk
- `ssid auto onu-serial-number` — Enables automatic fill of WLAN interface SSID, which in this case will be equal to the associated ONU serial number. — *Valores:* None. · *Default:* None.
- `ssid auto onu-serial-number prefix* prefix` — A textual prefix to be added (prepended) to the auto-generated SSID. — *Valores:* Text: up to 20 characters. · *Default:* None.
- `ssid auto onu-serial-number suffix* suffix` — A textual suffix to be added (appended) to the auto-generated SSID. — *Valores:* Text: up to 20 characters. · *Default:* None.
- `ssid custom ssid` — Set WLAN interface SSID. — *Valores:* Text: up to 32 characters. · *Default:* None.
- `wpa-passphrase wpa-passphrase` — WPA passphrase. — *Valores:* Text: up to 63 characters. · *Default:* None.
- `wpa-encryption aes tkip+aes` — WPA encryption mode. — *Valores:* aes or tkip+aes. · *Default:* tkip+aes.
- `ipv4 dhcp` — Configures DHCP mode for the IP connection. — *Valores:* a.b.c.d · *Default:* None
- `ipv4 static default-gateway def-gw-addr` — Configures a default gateway address for related IP connection (static address mode). — *Valores:* a.b.c.d · *Default:* None
- `itf-grouping dhcp-server` — Enables the DHCP server on LAN side. — *Valores:* None. · *Default:* dhcp-server
- `dhcp-server-address-pool start-address starting-ip-address` — Starting IP address for the DHCP pool on LAN side. If no value is specified and the DHCP server is enabled, the default generated by the ONU will be used. — *Valores:* a.b.c.d · *Default:* None.
- `dhcp-server-address-pool end-address ending-ip-address` — Ending IP address for the DHCP pool on LAN side. If no value is specified and the DHCP server is enabled, the default generated by the ONU will be used. — *Valores:* a.b.c.d · *Default:* None.
- `itf-grouping igmp-snooping` — Enables IGMP snooping on the LAN side. — *Valores:* None. · *Default:* igmp-snooping
- `ipv4 address ip-addr` — IP address set for this interface grouping. If no value is configured, the default generated by the ONU will be used. — *Valores:* a.b.c.d · *Default:* None.
- `ipv4 netmask addr-netmask` — Netmask set for this interface grouping. If no value is configured, the default generated by the ONU will be used. — *Valores:* a.b.c.d · *Default:* None.
- `ports { eth1 | eth2 | eth3 | eth4 | wl0 | wl0-vap1}` — Sets the ports that will be members of this interface grouping. — *Valores:* eth1, eth2, eth3, eth4, wl0, wl0-vap1 · *Default:* None.
- `vlan vlan-id` — Add a VLAN to this port. — *Valores:* 1-4094. · *Default:* None.
- `cos cos` — Add cos to port. — *Valores:* 0-7. · *Default:* 0.
- `ip-filtering priority` — Create an IP filtering rule with the given priority. The highest priority is 0. — *Valores:* 0-7. · *Default:* None
- `filtering-type` — IP filtering type. — *Valores:* incoming. · *Default:* None
- `action act` — IP filtering action. — *Valores:* permit. · *Default:* None
- `match destination-ip-address dest-addr` — Filter by destination IP address and prefix length. — *Valores:* IPv4 address and prefix length. · *Default:* None
- `match source-ip-address src-addr` — Filter by source IP address and prefix length. — *Valores:* IPv4 address and prefix length. · *Default:* None
- `match protocol proto` — Filter by IP protocol. — *Valores:* icmp, tcp, udp, tcp/udp. · *Default:* None
- `match source-port port` — Filter TCP/UDP source port. It is necessary to also select protocol TCP or UDP. — *Valores:* 1-65535. · *Default:* None
- `match source-port port-proto` — Filter TCP/UDP source port of given protocol. — *Valores:* dns, http, https, snmp, snmptrap, ssh, telnet, whois. · *Default:* None
- `match source-port range start start-port` — Starting TCP/UDP port for range filter. — *Valores:* 1-65535. · *Default:* None
- `match source-port range stop stop-port` — Stopping TCP/UDP port for range filter. — *Valores:* 1-65535. · *Default:* None
- `match destination-port port` — Filter TCP/UDP destination port. It is necessary to also select protocol TCP or UDP. — *Valores:* 1-65535. · *Default:* None
- `match destination-port port-proto` — Filter TCP/UDP destination port of given protocol. — *Valores:* dns, http, https, snmp, snmptrap, ssh, telnet, whois. · *Default:* None
- `match destination-port range start start-port` — Starting TCP/UDP port for range filter. — *Valores:* 1-65535. · *Default:* None
- `match destination-port range stop stop-port` — Stopping TCP/UDP port for range filter. — *Valores:* 1-65535. · *Default:* None
- `user-mgmt [ priv-lvl-support | priv-lvl-user ] password auto onu-serial-number` — Enables automatic fill of the ONU user (level support or user) WEB login credential, which in this case will be equal to the associated ONU serial number. — *Valores:* None. · *Default:* None.
- `user-mgmt [ priv-lvl-support | priv-lvl-user ] password auto onu-serial-number prefix* prefix` — A textual prefix to be added (prepended) to the auto-generated ONU user (level support or user) WEB login credential. — *Valores:* Text: up to 4 characters. · *Default:* None.
- `user-mgmt [ priv-lvl-support | priv-lvl-user ] password auto onu-serial-number suffix* suffix` — A textual suffix to be added (appended) to the auto-generated ONU user (level support or user) WEB login credential. — *Valores:* Text: up to 4 characters. · *Default:* None.
- `user-mgmt [ priv-lvl-support | priv-lvl-user ] password custom password` — Set ONU user (level support or user) WEB login credential. — *Valores:* Text: up to 16 characters. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |
| 5.2 | Command user-mgmt added. |

**Usage Guidelines:**

When associated with an ONU, the OLT will apply all configuration present in the RG profile to specified DM984-42x/DM985-100 ONU, erasing any other WAN configuration, and their dependencies, made through its WEB interface. Some parameters can be specified per ONU basis, overriding the values in the RG profile. See the ‘onu’ command for reference. To use an IP filtering rule it is necessary to enable the firewall on the WAN. To set RG profile it is necessary to enter in rg-profile menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# profile gpon rg-profile MY_PLAN
(config-rg-profile-MY_PLAN)# wan-pppoe-connection pppoe_1
(config-wan-pppoe-connection-pppoe_1)# vlan-mux vlan 100
(config-wan-pppoe-connection-pppoe_1)# nat
(config-wan-pppoe-connection-pppoe_1)# ip-filtering 0 incoming action permit
(config-ip-filtering-0)# match protocol tcp/udp destination-port range start 2000 stop 3000
(config-ip-filtering-0)# itf-grouping
(config-itf-grouping)# ipv4-address 192.168.0.1 netmask 255.255.255.0
(config-itf-grouping)# dhcp-server-address-pool start-address 192.168.0.2 end-address 192.168.0.254
(config-itf-grouping)# ports eth1
(config-itf-grouping)# ports eth2
(config-itf-grouping)# ports eth3
(config-itf-grouping)# ports eth4
(config-itf-grouping)# ports wl0
(config-itf-grouping)# ports wl0-vap1
(config-itf-grouping)# exit
(config-wan-pppoe-connection-pppoe_1)# exit
(config-rg-profile-MY_PLAN)# wlan wl0-vap1
(config-wlan-wl0-vap1)# ssid custom test
(config-wlan-wl0-vap1)# wpa-encryption tkip+aes
(config-wlan-wl0-vap1)# wpa-passphrase teste123
```

**Impacts and precautions:**

Editing this profile will cause all associated ONUs to be reconfigured causing traffic loss. If the IP connection is configured for static IP address mode, the static IP address must be configured in the related ONU override settings. The ONU has a default interface grouping which will always aggregate all ports and WANs that are not included in other groupings. IP address for this default grouping is 192.168.0.1 and DHCP server is enabled. As new interface groupings are created, the ONU will automatically assign IPs 192.168.2.1, 192.168.3.1 and so on, if no custom value is configured. When configuring the custom IP address of an interface grouping to an IP 192.168.X.X, it is necessary to be aware of possible conflicts with the default grouping, or with other groupings which don’t have a custom IP configured. The names of WLAN ports on interface grouping are a little bit different from the ONU DM984-42X web interface. The WLAN port wl0 is referred to wlan0 and the wl0-vap1 port is referred to wl0_Guest1. The port wl0-vap1 only can be present on a interface grouping if the WLAN interface wl0-vap1 is configured on rg-profile.

**Hardware restrictions:**

N/A


### `profile gpon service-profile`

> **Página:** 1706 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The service-profile command is used to create an ONU service profile. This profile configures ONU capability and the parameters related to services. These parameters include the user’s ONU and VLAN.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
profile gpon service-profile profile-name { onu-profile profile-name }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `service-profile profile-name` — Indicates the service-profile name. — *Valores:* Text. · *Default:* None
- `onu-profile profile-name` — Indicates the onu-profile name tied to service-profile. — *Valores:* Text. · *Default:* None.

**Default:** N/A. There is no default profile.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.8.2 | Default profiles were added. |
| 4.0.0 | Binding an ONU-profile is not mandatory. |

**Usage Guidelines:**

The onu-profile to be tied to service-profile must be configured. To set a service profile is necessary to enter in the service-profile menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# profile gpon service-profile servProfName
(config-service-profile-servProfName)#
```

**Impacts and precautions:**

The profile cannot be modified if it is already committed to configuration.

**Hardware restrictions:**

N/A


### `profile gpon sip-agent-profile`

> **Página:** 1708 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The sip-agent-profile command is used to enter in SIP Agent profile mode and set the SIP server configuration, such as registrar address, proxy server address and outbound proxy server address.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
profile gpon sip-agent-profile { sip-agent-profile-name [ registrar registrar-address | proxy-server proxy-server-address | outbound-proxy outbound-proxy-address ] }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `sip-agent-profile expires-timeout` — This attribute specifies the SIP registration expiration time in seconds. The ONU will resend registration messages before the expiration time. — *Valores:* 20-604800 · *Default:* 3600
- `sip-agent-profile sip-agent-profile-name` — Indicates the SIP Agent profile name. — *Valores:* String: up to 48 characters. · *Default:* None.
- `registrar registrar-address` — Indicates the SIP registrar IPv4 address. — *Valores:* String: IPv4 address. · *Default:* None.
- `proxy-server proxy-server-address` — Indicates the SIP proxy server IPv4 address. — *Valores:* String: IPv4 address. · *Default:* None.
- `outbound-proxy outbound-proxy-address` — Indicates the SIP outbound proxy IPv4 address. — *Valores:* String: IPv4 address. · *Default:* None.

**Default:** None.

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. |

**Usage Guidelines:**

To set the sip-agent profile it is necessary to enter in the sip-agent-profile menu. Example:

```text
# config
Entering configuration mode terminal
(config)# profile gpon sip-agent-profile sipAgentName
(config-sip-agent-profile-sipAgentName)#
```

**Impacts and precautions:**

No field validation is performed at registrar, proxy-server and outbound-proxy parameters. The user must inform a valid IPv4 address format for each of these fields.

**Hardware restrictions:**

None.


### `profile gpon snmp-profile`

> **Página:** 1711 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Defines which OIDs will be available for SNMP monitoring of GPON objects.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
profile gpon snmp-profile profile-name [ if-alias | if-name | if-type | if-descr | ifadmin-status | if-oper-status | if-onu-power-tx | if-onu-power-rx | if-onu-sysuptime | statistics-in-octets | statistics-in-ucast-pkts | statistics-in-multicast-pkts | statisticsin-broadcast-pkts | statistics-in-discards | statistics-in-errors | statistics-in-unknownprotos | statistics-out-octets | statistics-out-ucast-pkts | statistics-out-multicastpkts | statistics-out-broadcast-pkts | statistics-out-discards | statistics-out-errors | statistics-in-bw-usage | statistics-out-bw-usage ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `snmp-profile profile-name` — Name of the SNMP profile. — *Valores:* String (1-48 characters; accepts alphanumeric characters, ‘+’, ‘-’ and ’_’). · *Default:* None
- `if-alias` — Enable monitoring of interface textual description. — *Valores:* None · *Default:* Disabled
- `if-name` — Enable monitoring of interface name. — *Valores:* None · *Default:* Disabled
- `if-type` — Enable monitoring of global IANA interface type. — *Valores:* None · *Default:* Enabled
- `if-descr` — Enable monitoring of interface description. — *Valores:* None · *Default:* Enabled
- `if-admin-status` — Enable monitoring of interface administrative state. — *Valores:* None · *Default:* Disabled
- `if-oper-status` — Enable monitoring of interface operational state. — *Valores:* None · *Default:* Enabled
- `if-onu-power-tx` — Enable monitoring of ONU Tx optical power. — *Valores:* None · *Default:* Disabled
- `if-onu-power-rx` — Enable monitoring of ONU Rx optical power. — *Valores:* None · *Default:* Enabled
- `if-onu-sysuptime` — Enable monitoring of ONU system uptime. — *Valores:* None · *Default:* Disabled
- `statistics-in-octets` — Enable monitoring of ethernet UNI input octets. — *Valores:* None · *Default:* Disabled
- `statistics-in-ucast-pkts` — Enable monitoring of ethernet UNI input unicast packets. — *Valores:* None · *Default:* Disabled
- `statistics-in-multicast-pkts` — Enable monitoring of ethernet UNI input multicast packets. — *Valores:* None · *Default:* Disabled
- `statistics-in-broadcast-pkts` — Enable monitoring of ethernet UNI input broadcast packets. — *Valores:* None · *Default:* Disabled
- `statistics-in-discards` — Enable monitoring of ethernet UNI input discarded packets. — *Valores:* None · *Default:* Disabled
- `statistics-in-errors` — Enable monitoring of ethernet UNI input packets with errors. — *Valores:* None · *Default:* Disabled
- `statistics-in-unknown-protos` — Enable monitoring of ethernet UNI input packets with unknown protocol. — *Valores:* None · *Default:* Disabled
- `statistics-out-octets` — Enable monitoring of ethernet UNI output octets. — *Valores:* None · *Default:* Disabled
- `statistics-out-ucast-pkts` — Enable monitoring of ethernet UNI output unicast packets. — *Valores:* None · *Default:* Disabled
- `statistics-out-multicast-pkts` — Enable monitoring of ethernet UNI output multicast packets. — *Valores:* None · *Default:* Disabled
- `statistics-out-broadcast-pkts` — Enable monitoring of ethernet UNI output broadcast packets. — *Valores:* None · *Default:* Disabled
- `statistics-out-discards` — Enable monitoring of ethernet UNI output discarded packets. — *Valores:* None · *Default:* Disabled
- `statistics-out-errors` — Enable monitoring of ethernet UNI output packets with errors. — *Valores:* None · *Default:* Disabled
- `statistics-in-bw-usage` — Enable monitoring of ethernet UNI input bandwidth usage. — *Valores:* None · *Default:* Enabled
- `statistics-out-bw-usage` — Enable monitoring of ethernet UNI output bandwidth usage. — *Valores:* None · *Default:* Enabled

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

To configure a GPON SNMP profile, it is necessary to enter the snmp-profile menu. The profile cannot be deleted if it is referenced by an ONU. Example (configuring an SNMP profile to monitor the administrative status of GPON interfaces):

```text
# config
Entering configuration mode terminal
(config)# profile gpon snmp-profile snmpProfName
(config-snmp-profile-snmpProfName)# if-admin-status
```

Example (configuring an SNMP profile to monitor the bandwidth usage of GPON interfaces):

```text
# config
Entering configuration mode terminal
(config)# profile gpon snmp-profile snmpProfName
(config-snmp-profile-snmpProfName)# statistics-in-bw-usage
(config-snmp-profile-snmpProfName)# statistics-out-bw-usage
```

**Impacts and precautions:**

Some OIDs (such as if-type/if-descr) are enabled by default and cannot be removed from the profile.

**Hardware restrictions:**

N/A


### `profile gpon tr069-acs-profile`

> **Página:** 1717 · **Modo:** Configuration mode · **Privilégios:** N/A · **Leitura (show/display):** não

**Description:** The tr069-acs-profile command is used to configure parameters for access to TR069 ACS (Auto Configuration Server). This allows the ONU to be managed and upgraded by a TR069 ACS. The no profile gpon tr069-acs-profile command is used to delete a specific TR069 ACS profile.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
profile gpon tr069-acs-profile profile-name url url username username password password
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `tr069-acs-profile profile-name` — Name of the profile to create. Must be unique within all TR069 profiles. Can have up to 48 characters. — *Valores:* Text: up to 48 characters. · *Default:* None
- `url url` — ACS network address URL. — *Valores:* Text: up to 128 characters. URL cannot contain white spaces or the following characters: " < > ˆ ‘ { | }. · *Default:* None
- `username username` — ACS username credential. — *Valores:* Text: up to 25 characters. · *Default:* None
- `password password` — ACS password credential — *Valores:* Text: up to 25 characters. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |

**Usage Guidelines:**

When associated with an ONU, the OLT will apply all configuration present in the TR069 ACS profile to specified ONU. To set TR069 ACS profile it is necessary to enter in tr069-acs-profile menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# profile gpon tr069-acs-profile MY_PROF
(config-rg-profile-MY_PROF)# url http://myacs.com:7547
(config-rg-profile-MY_PROF)# username admin
(config-rg-profile-MY_PROF)# password admin
```

**Impacts and precautions:**

Editing this profile will cause all associated ONUs to be reconfigured causing traffic loss. Configuring an url is mandatory.

**Hardware restrictions:**

N/A


### `vlan-mapping`

> **Página:** 1720 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The VLAN-mapping command is part of the service-profile structure and is used to add VLAN IDs and CoS values to packets.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
profile gpon service-profile service-profile-id vlan-mapping name symmetric { ethernet ethernet-ports | veip veip-idx } match vlan vlan-id { vlan-val | any } cos { cos-val | any } action vlan { add | replace } vlan-id { vlan-val | copy-vlan } cos { cos-val | copy-vlan }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `name` — Name of the VLAN-mapping. — *Valores:* Text: up to 48 characters. · *Default:* None
- `symmetric` — Symmetric VLAN-mapping specifies that the operation performed in the downstream direction is the inverse of the VLAN tagging operation that is performed in the upstream direction. — *Valores:* None · *Default:* None
- `ethernet ethernet-ports` — Ethernet ports to be affected. — *Valores:* Number: from 1 to 4. Range: two values from 1 to 4 separated by hifen. List of ranges/values: a combination of the above separated by commas. Examples: ethernet 1 ethernet 1,3 ethernet 1-4 ethernet 1-2,4 ethernet 1-2,3-4 · *Default:* None
- `veip veip-idx` — VEIP to be affected. — *Valores:* Number: 1. · *Default:* None
- `match` — Parameters after match and before action describe the type of flow that the rule applies to. — *Valores:* None · *Default:* None
- `vlan vlan-id { vlan-val | any }` — VLAN ID to be matched, or any in case all VLAN IDs apply. — *Valores:* None in case of ‘any’. vlan-val: Number from 0 to 4094. · *Default:* None.
- `cos { cos-val | any }` — CoS value to be matched, or any in case all CoS values apply. — *Valores:* None in case of ‘any’. cos-val: Number from 0 to 7. · *Default:* None.
- `action` — Parameters after action describe the action to be taken upon the flow that the rule applies to. — *Valores:* None. · *Default:* None.
- `vlan { add | replace }` — Add a new VLAN tag or replace an existing one. — *Valores:* None. · *Default:* None.
- `vlan-id { vlan-val | copy-vlan }` — New VLAN ID for the VLAN tag, or copy-vlan in case the original VLAN ID should be kept. — *Valores:* None in case of ‘copy-vlan’. vlan-val: Number from 0 to 4094. · *Default:* None.
- `cos { cos-val | copy-vlan }` — New CoS value for the VLAN tag, or copy-vlan in case the original CoS value should be kept. — *Valores:* None in case of ‘copy-vlan’. cos-val: Number from 0 to 7. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 5.8 | This command supports creating VLAN mapping rules for VEIP. |

**Usage Guidelines:**

For the ethernet field, valid configuration could be: A single port:

```text
(config-service-profile-servProfName)# vlan-mapping vlanMapName
symmetric ethernet 2 ...
```

Multiple ports separated by commas:

```text
(config-service-profile-servProfName)# vlan-mapping vlanMapName
symmetric ethernet 1,3,4 ...
```

A range of ports:

```text
(config-service-profile-servProfName)# vlan-mapping vlanMapName
symmetric ethernet 1-3 ...
```

A mix of the above:

```text
(config-service-profile-servProfName)# vlan-mapping vlanMapName
symmetric ethernet 1-3,4 ...
```

The command requires all fields configured to be applied. To set a VLAN-mapping is necessary to enter in the interface service-profile menu.

```text
(config)# profile gpon service-profile servProfName
(config-service-profile-servProfName)# vlan-mapping vlanMapName
symmetric ethernet 1 match vlan vlan-id 10 cos any action vlan replace vlan-id 100 cos copy-vlan
```

To actually apply the VLAN mapping rules, the service-profile must be selected on the ONU and the interface must be created.

```text
(config)# interface gpon 1/1/1 onu 0
(config-gpon-onu-0)# service-profile servProfName
(config-gpon-onu-0)# ethernet 1
```

**Impacts and precautions:**

• VLAN mapping rules will only be applied to ONUs that configured the service-profile containing the rules. • A VLAN mapping rule will only be applied if the target interface (Ethernet UNI, VEIP) is present in the ONU configuration.

**Hardware restrictions:**

N/A ONU This topic describes the commands related to ONU such as commands to authenticate an ONU and configure its UNIs.


## ONU

### `interface {gpon | xgspon} onu`

> **Página:** 1725 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Adds, modifies, removes, activates or deactivates an ONU as well as assigns profiles and configures Ethernet/POTS/VEIP UNI.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
interface {gpon | xgspon} <chassis/slot/port> onu onu-id interface {gpon | xgspon} <chassis/slot/port> onu onu-id [ name onu-name | serial-number serial-number [ password password ] | password password [ serial-number serial-number ] | service-profile service-profile-name [ line-profile line-profile-name ] | line-profile line-profile-name [ service-profile service-profile-name ] | ethernet ethernet-port | ipv4 { dhcp vlan { cos cos-val | vlan-id vlan-val } | static { address ip-addr | default-gateway def-gw-addr } | vlan { vlan-id vlan-val | cos cos-val } } | rg-profile rg-profile-name | rg-profile-override-settings | tr069-acs-profile tr069- acs-profile-name | auto-provisioned { true | false } ] interface {gpon | xgspon} <chassis/slot/port> onu onu-id ethernet ethernet-port [ speed { 10 | 100 | 1000 } [ duplex { full | half } ] | duplex { full | half } [ speed { 10 | 100 | 1000 } ] | native vlan { cos cos-val | vlan-id vlan-val }* | native downstream-mode { filter-on-vid-only | inverse-of-upstream } | negotiation | shutdown | mac-limit mac-limit-value | description { string }* ] interface {gpon | xgspon} <chassis/slot/port> onu onu-id pots pots-port [ sip-useragent display-name display-name username user-name password password userpart-aor user-part-aor [ sip-agent-profile sip-agent-profile-name ] | media-profile media-profile-name sip-agent-profile sip-agent-profile-name [ sip-user-agent display-name display-name username user-name password password user-part-aor userpart-aor ]] interface {gpon | xgspon} <chassis/slot/port> onu onu-id veip veip-port [ native vlan { vlan-id vlan-val | cos cos-val } ] interface {gpon | xgspon} <chassis/slot/port> onu onu-id rg-profile-override-settings wan-pppoe-connection pppoe-connection-name [ username username | password password ]* interface {gpon | xgspon} <chassis/slot/port> onu onu-id rg-profile-override-settings wan-ip-connection ip-connection-name static { address ip-addr | default-gateway def-gw-addr } interface {gpon | xgspon} <chassis/slot/port> onu onu-id rg-profile-override-settings wan-wlan wlan-name [ wpa-passphrase wpa-passphrase | ssid ssid ] interface {gpon | xgspon} <chassis/slot/port> onu onu-id rg-profile-override-settings user-mgmt [ priv-lvl-support | priv-lvl-user ] password password
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `onu onu-id` — Configures the ONU ID — *Valores:* 0-127 · *Default:* None
- `name onu-name` — Configures the ONU name. The name is optional. — *Valores:* Text with up to 48 characters. · *Default:* None
- `serial-number onu-name` — Text beginning with 4 ASCII characters, case sensitive, followed by 8 HEX characters, case insensitive. — *Valores:* ONU’s serial number. · *Default:* None
- `password password` — ONU’s password. The ONU’s password must be unique inside the ponlink it is located. However, this condition must only be met if the GPON Card ONU Authentication Method is set to password only. The password is case sensitive. — *Valores:* Text beginning with 0x followed by up to 20 HEX characters, or up to 10 alphanumerical characters. · *Default:* None
- `service-profile service-profile-name` — Reference to service-profile to be bound. — *Valores:* Text with up to 48 characters. · *Default:* None.
- `line-profile line-profile-name` — Reference to line-profile to be bound. — *Valores:* Text with up to 48 characters. · *Default:* “DEFAULT-LINE” for GPON platforms and “DEFAULT-LINE-XGSPON”
- `for XGSPON platforms. rg-profile rg-profile-name` — Reference to rg-profile to be bound. — *Valores:* Text with up to 48 characters. · *Default:* None.
- `rg-profile-override-settings` — Enter in RG profile override settings mode. — *Valores:* N/A. · *Default:* N/A.
- `wan-pppoe-connection pppoe-connection-name` — Reference to WAN PPPoE connection inside the related rg-profile. — *Valores:* Text with up to 48 characters. · *Default:* None.
- `username username` — Override PPPoE username of the WAN PPPoE connection inside the related rg-profile. — *Valores:* Text with up to 64 characters. · *Default:* None.
- `password password` — Override PPPoE password of the WAN PPPoE connection inside the related rg-profile. — *Valores:* Text with up to 32 characters. · *Default:* None.
- `wan-ip-connection ip-connection-name` — Reference to WAN IPoE connection inside the related rg-profile. — *Valores:* Text with up to 48 characters. · *Default:* None.
- `wan-ip-connection ip-connection-name ipv4 static address ip-addr` — Configures an IP address for related IP connection in RG Profile. The subnet mask prefix must be passed. — *Valores:* a.b.c.d/x · *Default:* None
- `wan-ip-connection ip-connection-name ipv4 static default-gateway def-gw-addr` — Configures a default gateway address for related IP connection in RG Profile. — *Valores:* a.b.c.d · *Default:* None
- `wlan wlan-name` — Reference to WLAN interface inside the related rg-profile. — *Valores:* One of the WLAN interface name from the rg-profile. · *Default:* None.
- `wpa-passphrase wpa-passphrase` — Override WPA passphrase of the WLAN interface inside the related rg-profile. — *Valores:* Text with up to 64 characters. · *Default:* None.
- `ssid ssid` — Override SSID name of the WLAN interface inside the related rg-profile. — *Valores:* Text with up to 32 characters. · *Default:* None.
- `auto-provisioned { true | false }` — Indicates that ONU was configured by auto provisioned (true) or not (false). If ONU configuration is changed after ONU was auto provisioned, it is recommended to set auto-provisioned to false. — *Valores:* True (auto provisioned) or false (not auto provisioned). · *Default:* False.
- `user-mgmt [ priv-lvl-support | priv-lvl-user ] password password` — RG profile override of ONU user (level support or user) WEB login credential configuration. — *Valores:* Text: up to 16 characters. · *Default:* None.
- `ethernet ethernet-port` — Configures the user network interface. An entry of the ethernet port must be created in order to monitor SNMP OIDs for the Ethernet UNI. — *Valores:* 1-4 · *Default:* None
- `speed { 10 | 100 | 1000 }` — Configures the user network interface speed to 10 Mbit/s, 100 Mbit/s or 1 Gbit/s. — *Valores:* { 10 | 100 | 1000 } · *Default:* None
- `duplex { full | half }` — Configures the user network interface flow to half-duplex or full-duplex. — *Valores:* { full | half } · *Default:* None
- `native vlan vlan-id` — Configures a VLAN ID to be added to incoming Ethernet untagged traffic. — *Valores:* 1-4094 · *Default:* None
- `native vlan cos cos-val` — Configures a class-of-service value for the VLAN configured. — *Valores:* 0-7 · *Default:* 0
- `native downstream-mode` — Configures the tagging action to be applied for downstream native VLAN tagged packets. When filter-on-vid-only value is used, the operation performed in the downstream direction is the inverse of that performed in the upstream direction but only VID match is applied, that is, the VLAN tag of downstream packets matching the same VLAN ID, regardless of their CoS, configured in the native vlan settings will be stripped. When inverse-of-upstream value is used, the operation performed in the downstream direction is the inverse of that performed in the upstream direction, that is, the VLAN tag of downstream packets matching the same VLAN ID and CoS configured in the native vlan settings will be stripped. It’s Important to note that the handling of the packets may differ based on the specific ONU implementation. — *Valores:* { filter-on-vid-only | inverse-of-upstream } · *Default:* filter-on-vid-only
- `negotiation` — Configures the user network interface to auto-negotiation mode. — *Valores:* None · *Default:* Negotiation
- `shutdown` — Disables the user network interface. — *Valores:* None · *Default:* no shutdown
- `snmp all` — Enables SNMP monitoring for the ONU. This command enables the ONU to report all available OIDs, including Ethernet UNI counters. — *Valores:* None · *Default:* Disabled (no snmp all)
- `snmp profile snmp-profile-name` — Reference to snmp-profile to be bound. Enables SNMP monitoring for the ONU. This command enables the ONU to report the OIDs selected in the specified SNMP profile, including Ethernet UNI counters. — *Valores:* Text with up to 48 characters. · *Default:* Disabled (no snmp profile)
- `snmp real-time` — Enables real-time SNMP monitoring for the ONU Ethernet UNI counters. When this parameter is disabled, Ethernet UNI counters are collected and updated in a 15-minute window. When enabled, these counters are collected continuously, being updated with a higher frequency. This frequency is inversely proportional to the number of ONUs configured and the number of ONUs with real-time update enabled. — *Valores:* None · *Default:* Disabled (no snmp real-time)
- `mac-limit mac-limit-value` — Configure MAC address learning limit. When this parameter is disabled (no mac-limit), there is no limitation on how many MAC addresses could be learned. In this case, the limitation will be given by the ONU MAC address table size. — *Valores:* 1-255 · *Default:* None (unlimited MAC address learning).
- `description` — Set the interface description or alias. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* The interface description. · *Default:* N/A
- `ipv4 dhcp vlan vlan-id vlan-val` — Configures a VLAN ID for ONUs IP address. — *Valores:* 1-4094 · *Default:* None
- `ipv4 dhcp vlan cos cos-val` — Configures a class-of-service value for the VLAN configured in ipv4 VLAN parameter. — *Valores:* 0-7 · *Default:* None
- `ipv4 static address ip-addr` — Configures an IP address for the ONU. The subnet mask prefix must be passed. — *Valores:* a.b.c.d/x · *Default:* None
- `ipv4 static default-gateway def-gw-addr` — Configures a default gateway address for the ONU. — *Valores:* a.b.c.d · *Default:* None
- `ipv4 vlan vlan-id vlan-val` — Configures an outer VLAN for the ONU. — *Valores:* 1-4094 · *Default:* None
- `ipv4 vlan cos cos-val` — Configure an outer CoS for the ONU. — *Valores:* 0-7 · *Default:* None
- `pots pots-port` — Configures the POTS interface. — *Valores:* 1-4 · *Default:* None
- `display-name display-name` — Indicates the display-name of the SIP user. — *Valores:* Text with up to 48 characters. · *Default:* None
- `username user-name` — Indicates the user name for the SIP user authentication. — *Valores:* Text with up to 32 characters. · *Default:* None
- `password password` — Indicates the password for the SIP user authentication. — *Valores:* Text with up to 32 characters. · *Default:* None
- `user-part-aor user-part-aor` — Defines the user identity by unique AOR (address of record). — *Valores:* Text with up to 256 characters. · *Default:* None
- `media-profile media-profile-name` — Reference to the media profile. — *Valores:* Text with up to 48 characters. · *Default:* None
- `sip-agent-profile sip-agent-profile-name` — Reference to the SIP agent profile. — *Valores:* Text with up to 48 characters. · *Default:* None
- `veip veip-port` — Configures the ONU Virtual Ethernet Interface Point (VEIP). — *Valores:* 1. · *Default:* None
- `native vlan vlan-id` — Configures a VLAN ID to be added to incoming VEIP untagged traffic. — *Valores:* 1-4094 · *Default:* None
- `native vlan cos cos-val` — Configures a class-of-service value for the VLAN configured. — *Valores:* 0-7 · *Default:* 0
- `tr069-acs-profile tr069-acs-profile-name` — Reference to tr069-acs-profile to be bound. — *Valores:* Text with up to 48 characters. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.6 | The POTS configuration command was added. Ethernet UNI Mac address learning limit command was added. 1.8 The VEIP configuration command was added. |
| 1.8.2 | Default profiles were added. |
| 1.12 | Media profile was added. |
| 2.0 | Command ‘snmp all’ option was added. |
| 2.4 | Command ‘snmp profile’ and ‘snmp real-time’ options were added. |
| 3.0 | Commands ‘rg-profile’ and ‘rg-profile-override-settings’ were added. Binding a service-profile is not mandatory. Added auto-provisioned com4.0.0 mand. |
| 5.0 | Command ‘tr069-acs-profile’ was added. |
| 5.2 | Command user-mgmt added. |
| 9.0 | Added support for some special characters on interface description. Changed the line profile default of XGSPON platforms from “DEFAULT9.4 LINE” to “DEFAULT-LINE-XGSPON”. |

**Usage Guidelines:**

To set interface gpon or xgspon onu parameters is necessary to enter in the interface gpon or xgspon onu menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu 1
(config-gpon-onu-1)# ethernet 1
(config-ethernet-1)# description test_interface_name
```

Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example:

```text
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu 1
(config-gpon-onu-1)# ethernet 1
(config-gpon-1/1/1)# description "test_interface_name|!?;"
```

To configure service profile:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu 1
(config-gpon-onu-1)# service-profile serviceName
```

To configure media profile:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu 1
(config-gpon-onu-1)# pots 1
(config-pots-1)# media-profile mediaName
```

To enable SNMP monitoring for the ONU:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu 1
(config-gpon-onu-1)# snmp all
```

To configure a RG profile and override only the PPPoE password:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu 1
(config-gpon-onu-1)# rg-profile MY_RG_PROFILE
(config-gpon-onu-1)# rg-profile-override-settings
(config-gpon-onu-1-rg-...)# wan-pppoe-connection pppoe_1 password MY_PASSWORD
```

To configure a RG profile and static IP address for the WAN interface:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu 1
(config-gpon-onu-1)# rg-profile MY_RG_PROFILE
(config-gpon-onu-1)# rg-profile-override-settings
(config-...-rg-...)# wan-ip-connection ipoe_1 ipv4 static address 10.2.3.4/24
```

To configure a RG profile and override SSID and wpa-passphrase for the WLAN interface:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu 1
(config-gpon-onu-1)# rg-profile MY_RG_PROFILE
(config-gpon-onu-1)# rg-profile-override-settings
(config-gpon-onu-1-rg-...)# wlan wl0 wpa-passphrase MY_PASSWORD ssid MY_SSID
```

To configure a TR069 ACS profile:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu 1
(config-gpon-onu-1)# tr069-acs-profile MY_TR069_PROFILE
```

Some third-party ONUs may not support the use of a native VLAN on the Ethernet UNI. As a workaround the service-port may be configured to work as a native VLAN (match “any” plus action “add” operation).

**Impacts and precautions:**

Configuring a serial-number and/or password must match with gpon authentication method command defined configuration. Binding a line-profile is mandatory. An outer-VLAN must be set when configuring ipv4. Binding a valid SIP agent profile is mandatory when configuring ONU POTS interfaces. Even if SNMP (all or profile) configured, Ethernet UNI SNMP counters are published each 15 minutes. If Ethernet UNI SNMP counters needs to be updated more frequently, turn on real-time update. When real-time SNMP update is enabled, Ethernet UNI SNMP counters are published continuously, being updated with a higher frequency. This frequency is inversely proportional to the number of ONUs configured and the number of ONUs with real-time update enabled. Up to 32 ONUs can have real-time SNMP monitoring turned on globally. It is recommended that the polling interval by the external monitoring tool should be 5 minutes or higher. In order to monitor SNMP OIDs for a given Ethernet UNI, an entry must be created with the ethernet ethernet-port command. RG profile will only work for DM984-42x and DM985-100 ONU models. When overriding RG profile settings, only the selected parameters will be overridden while others will come from the associated RG profile. If the RG profile contains IP connections with static IP address mode, the static IP address for each connection must be configured in the override settings. When using a TR069 ACS profile, ensure that the ONU has an IP path already configured for this service.

**Hardware restrictions:**

None


### `onu-auth-method`

> **Página:** 1739 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Defines the method that will be used to authenticate an ONU. This configuration is applied to the gpon-card as a whole, affecting all its ONUs.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
onu-auth-method { serial-number | pasword | serial-number-and-password }
```

**Parameters:**

- `serial-number` — Sets the authentication method to serial number only. — *Valores:* None · *Default:* None
- `password` — Sets the authentication method to password only. — *Valores:* None · *Default:* None
- `serial-number-and-password` — Sets the authentication method to serial number and password. — *Valores:* None · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

To set an onu-auth-method it is necessary to enter in the given gpon card menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# gpon 1/1
(config-gpon-1/1)# onu-auth-method password
```

**Impacts and precautions:**

None

**Hardware restrictions:**

N/A


### `onu-enable`

> **Página:** 1741 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command re-enables an inactive ONU.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
onu-enable { all | serial-number }
```

**Parameters:**

- `onu-enable all` — Enable all ONUs. — *Valores:* None · *Default:* None
- `onu-enable serial-number` — Only the ONU with the given serial number will be enabled. — *Valores:* Four letters followed by eight hexadecimal values (0-f). · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

To apply an onu-enable it is necessary to enter in the given gpon or xgspon interface menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu-enable all
```

**Impacts and precautions:**

Depending on the reason why the ONU was disabled, it may not become enabled when this command is issued. This command merely attempts to enable an ONU.

**Hardware restrictions:**

N/A


### `onu-force-status-update`

> **Página:** 1743 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command forces an ONU to update its status.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
onu-force-status-update { onu onu-id }
```

**Parameters:**

- `onu onu-id` — Selects an ONU. — *Valores:* A registered ONU ID. See command ‘onu’ for range information. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

In scenarios with hundreds of ONUs, status polling can take a long time to update a given ONU status. This command can be used to force a particular ONU to update its status. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu-force-status-update onu 1
```

In the example above, execute “show interface gpon 1/1/1 onu 1” to check the updated status.

**Impacts and precautions:**

It is expected that the ONU status might be updated a few seconds after the command is executed. Even with the command executed, the uptime only will be updated when interval time is reached (interval of 5 minutes). The TX/RX optical power is only updated if the difference is greater than 0.2dBm.

**Hardware restrictions:**

N/A


### `onu-reset`

> **Página:** 1745 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command resets an ONU.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
onu-reset { onu onu-id }
```

**Parameters:**

- `onu onu-id` — Resets a specific ONU. — *Valores:* A registered ONU ID. See command ‘onu’ for range information. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

To apply an onu-reset it is necessary to enter in the given gpon or xgspon interface menu. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu-reset onu 1
```

**Impacts and precautions:**

The refered ONU will be reset, affecting ongoing data traffic. Only works on configured and connected ONUs.

**Hardware restrictions:**

N/A


### `request firmware onu cancel`

> **Página:** 1747 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Cancels ONU firmware upgrade.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
request onu cancel interface gpon { chassis/slot/port } { onu onu-id | all }
```

**Parameters:**

- `interface gpon chassis/slot/port` — Specifies the gpon interface in chassis/slot/port. — *Valores:* chassis/slot/port · *Default:* None
- `onu onu-id` — Defines the ONU to be used in the operation. — *Valores:* 0-127 · *Default:* None

**Default:** None

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |
| 2.0 | Removed ‘remote’ from the command syntax. |

**Usage Guidelines:**

Use the cancel command to cancel the firmware installation in one or in all ONUs in a given gpon interface. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# request firmware onu cancel interface gpon 1/1/1 onu 1
```

**Impacts and precautions:**

None

**Hardware restrictions:**

None


### `request firmware onu install`

> **Página:** 1749 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Installs the firmware image to an ONU. For in-band-upgrade option, only DM984-42x ONU model is currently supported.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
request firmware onu install { filename } interface gpon { chassis/slot/port } { onu onu-id | all } request firmware onu install { filename } in-band-upgrade { model onu-model } { ip-address ipv4-address } [ { username onu-username } ] [ { password onu-password } ]
```

**Parameters:**

- `filename` — Defines the name of the firmware image file to be used in a remote ONU update. — *Valores:* Text with no character limit · *Default:* None
- `interface gpon chassis/slot/port` — Specifies the gpon interface in chassis/slot/port. — *Valores:* chassis/slot/port · *Default:* None
- `onu onu-id` — Defines the ONU to be used in the operation. — *Valores:* 0-127 · *Default:* None
- `in-band-upgrade` — Selects the in-band mode for upgrade of ONU firmware. — *Valores:* None · *Default:* N/A
- `model onu-model` — Identifies the model of the ONU that will be upgraded. — *Valores:* dm984-42x · *Default:* None
- `ip-address ipv4-address` — ONU’s IP Host address. — *Valores:* a.b.c.d · *Default:* None
- `username onu-username` — ONU’s management user. The username is case sensitive. — *Valores:* Word with up to 32 characters · *Default:* None
- `password onu-password` — ONU’s management password. The password is case sensitive. — *Valores:* Word with up to 32 characters · *Default:* None

**Default:** None

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |
| 2.0 | Removed remote from the command syntax. |
| 2.4 | Added text in Impacts and precautions. The in-band-upgrade operation mode was introduced. Also moved some |
| 4.9 | text from Impacts and precautions to request firmware onu add section. |

**Usage Guidelines:**

Use install filename interface command to install the firmware at some ONU connected to a GPON interface. For this option, use the cancel command to stop the operation. Example:

```text
# request firmware onu install fwName interface gpon 1/1/1 onu 1
```

Use install filename in-band-upgrade command to install the firmware at some ONU known by its IPv4 address. The cancel command does not apply here because the operation blocks until finished, when the result of operation is printed. If the upgrade fails, the message informs about the reason. Examples: Succeeded operation:

```text
# request firmware onu install fwName in-band-upgrade model dm984-42x
ip-address 192.168.10.10 username anon password rightpass
in-band-upgrade succeeded for 192.168.10.10
```

Failed operation:

```text
# request firmware onu install fwName in-band-upgrade model dm984-42x
ip-address 192.168.10.10 username anon password wrongpass
in-band-upgrade FAILED for 192.168.10.10 (not authorized)
```

**Impacts and precautions:**

The ONU will reboot to activate the new firmware image. When upgrading using the interface operation mode, it is the operator responsibility to check if the selected ONU (or ONUs) is (are) compatible with the selected ONU firmware file. The OLT will not check this compatibility, even though most of ONU models have the capability of performing this function. In these cases, ONU firmware transfer will fail and the ONU will remain in the previous state. When upgrading using the in-band-upgrade operation mode, the addressed ONU’s model will be read and compared with the selected model in the command. In case of mismatch, the command will be refused. Only one firmware file can be used at a time globally in the equipment. That is, if the operator is upgrading a given ONU model, another upgrade with a different firmware file cannot happen while the all other transfers finish. In other words, once started one or more ONU firmware file transfers, the operator needs to wait for all of them to complete in order to start a new one with a different ONU firmware file.

**Hardware restrictions:**

None


### `rg-reprovision`

> **Página:** 1753 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command re-provision an ONU associated with an rg-profile.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
rg-reprovision
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.9.0 | This command was introduced. |

**Usage Guidelines:**

To apply an rg-reprovision it is necessary to enter in the given onu config. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu 1
(config-gpon-onu-1)# rg-reprovision
```

To use the command on multiple ONUs, ranges can be used. Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1
(config-gpon-1/1/1)# onu *
(config-gpon-onu-*)# rg-reprovision
```

Example:

```text
# configure terminal
Entering configuration mode terminal
(config)# interface gpon 1/1/1-8
(config-gpon-1/1/1-8)# onu *
(config-gpon-onu-*)# rg-reprovision
```

**Impacts and precautions:**

This command will reprovision the ONU and configurations made via the ONU web interface might be erased.

**Hardware restrictions:**

N/A


### `show firmware`

> **Página:** 1755 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** General information about ONU firmware.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
show firmware onu
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `onu` — General information on ONU firmware. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. Removed the “show firmware gpon onu interface” command. Modified 1.4 “show firmware info” command. |

**Usage Guidelines:**

```text
# show firmware onu
A-v-a-i-l-a-b-l-e--F-i-r-m-w-a-r-e-s--f-o-r--O-N-UName : 0906-02.R4.2.30.027.man
MD5 : 9e42ded778438cb1b1d4ad9f56846c70
Size : 7098372
----
```

**Output Terms:**

Output Description Name Field to show the firmware name. MD5 Field to show the Message-Digest algorithm 5 (MD5). Size Field to show the firmware size in bytes.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show interface gpon onu`

> **Página:** 1757 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays ONU information.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
show interface gpon chassis/slot/port onu onu-id [ version | optical-info | brief | rssi ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `chassis/slot/port` — The GPON port on which the ONU is located. — *Valores:* Text: chassis/slot/port format. · *Default:* N/A
- `onu onu-id` — The ONU referred. — *Valores:* onu-id: Number from 0 to 127. · *Default:* N/A
- `version` — Display firmware version of the ONU. — *Valores:* N/A · *Default:* N/A
- `optical-info` — Display informations of the ONU’s optical interface. — *Valores:* N/A · *Default:* N/A
- `brief` — Display brief information of the ONU. — *Valores:* N/A · *Default:* N/A
- `rssi` — Display the RSSI (received signal strength indication) for a specific ONU. The value represents the power level received at the OLT for the selected ONU. Only one ONU can be selected each time. The value read from the CLI may be different from the actual value read by a power meter. The value can also be affected by the amount of traffic transmitted by ONU. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.10 | Added configured password. |
| 2.4 | Added more information to usage guidelines and output parameters. |
| 4.2.0 | Added support for range of IDs in show options. Added support to RSSI (Received signal strength indication) measure6.2.0 ment for ONUs. Uptime and last_seen_online: updated only when the difference of the time info is greater than 5 minutes. Last_Update: updated only when 8.0.0 others status are updated. TX/RX optical power: updated only when the difference is greater than 0.2dBm. |

**Usage Guidelines:**

```text
# show interface gpon 1/1/8 onu 1
```

Last updated : 2017-11-22 15:00:27 UTC+0 ID : 1 Serial Number : DACM00000353 Password : Uptime : 22:34 Last Seen Online : N/A Vendor ID : DACM Equipment ID : DM984-100B Name : Operational state : Up Primary status : Active Distance : 0 [km] IPv4 mode : Not configured IPv4 address : IPv4 default gateway : IPv4 VLAN : IPv4 CoS : Line Profile : DEFAULT-LINE Service Profile : RG Profile : RG One Shot Provision : Not provisioned TR069 ACS Profile : SNMP : Disabled Allocated bandwidth : 0 fixed, 0 assured+fixed [kbit/s] Upstream-FEC : Enabled Anti Rogue ONU isolate : Disabled Version : Active FW : v1.3.2 valid, committed Standby FW : v1.3.1 valid, not committed Software Download State : None Rx Optical Power [dBm] : -8.16 Tx Optical Power [dBm] : -0.08 Show all ONUs in all gpon interfaces

```text
# show interface gpon onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 2 CIGG12345672 Up Complete ONU2 1/1/3 1 CIGG12345673 Up Complete ONU3 1/1/4 1 CIGG12345674 Up Complete ONU4 1/1/4 5 CIGG12345675 Up Complete ONU5 Show all ONUs in all gpon interfaces

```text
# show interface gpon * onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 2 CIGG12345672 Up Complete ONU2 1/1/3 1 CIGG12345673 Up Complete ONU3 1/1/4 1 CIGG12345674 Up Complete ONU4 1/1/4 5 CIGG12345675 Up Complete ONU5 Show all ONUs in all gpon interfaces in a given chassis/slot

```text
# show interface gpon 1/1/* onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 2 CIGG12345672 Up Complete ONU2 1/1/3 1 CIGG12345673 Up Complete ONU3 1/1/4 1 CIGG12345674 Up Complete ONU4 1/1/4 5 CIGG12345675 Up Complete ONU5 Show all ONUs in range of gpon interfaces/slot

```text
# show interface gpon 1/1/1-4 onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 2 CIGG12345672 Up Complete ONU2 1/1/3 1 CIGG12345673 Up Complete ONU3 Show all ONUs in a list of gpon interfaces/slot

```text
# show interface gpon 1/1/2,4 onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/2 1 CIGG12345671 Up Complete ONU1 1/1/2 2 CIGG12345672 Up Complete ONU2 1/1/4 1 CIGG12345673 Up Complete ONU3 Show all ONUs in a given gpon interface/slot

```text
# show interface gpon 1/1/1 onu
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 9 CIGG12345672 Up Complete ONU9 1/1/1 22 CIGG12345673 Up Complete ONU22 Show a range of ONUs in a given gpon interface/slot

```text
# show interface gpon 1/1/1-10 onu *
```

Itf ONU ID Serial Number Oper State Software Download State Name -------- ------ ------------- ---------- -------------------------- ------------------------------------------------ 1/1/1 1 CIGG12345671 Up Complete ONU1 1/1/1 9 CIGG12345672 Up Complete ONU9

**Output Terms:**

Output Description Shows the timestamp of the last time the selected ONU has its status Last updated published to the database. Updated only when others status are updated. ID ID of the ONU. Serial Number Serial number of the ONU. Password ONU password. The uptime reported by the ONU. Updated only when the difference Uptime of the time info is greater than 5 minutes. Output Description The time since ONU was online. Updated only when the difference Last Seen Online of the time info is greater than 5 minutes. Vendor ID Vendor ID part of the ONU. Equipment ID Equipment ID of the ONU. Name User defined name of the ONU. Operational state State of operation of the ONU. Primary status Primary status of the ONU. Distance Approximate ONU logical distance (in kilometers) from the OLT. IPv4 mode ONU IP-Host mode: static or DHCP. IPv4 Address ONU IP-Host IPv4 Address. IPv4 default ONU IP-Host IPv4 default gateway. gateway IPv4 VLAN ONU IP-Host VLAN. IPv4 CoS ONU IP-Host CoS. Line Profile Line Profile assigned to the ONU. Service Profile Service Profile assigned to the ONU. RG Profile RG Profile assigned to the ONU. Output Description RG One Shot Indicates the time that RG Profile was provisioned at ONU. Provision TR069 ACS Profile TR069 ACS Profile assigned to the ONU. Shows if the ONU has snmp enabled and the SNMP profile when apSNMP plicable. Allocated Type and amount of bandwidth allocated for the ONU. bandwidth Upstream-FEC Upstream-FEC state. Anti Rogue ONU Anti Rogue ONU isolate state. isolate Version ONU firmware version. Active FW Firmware version of the ONU active image. Standby FW Firmware version of the ONU standby image. Software Download ONU firmware upgrade state. State Rx Optical Power Rx power level in dBms. Updated only when the difference is greater -dBm- than 0.2dBm. Tx Optical Power Tx power level in dBms. Updated only when the difference is greater -dBm- than 0.2dBm. RSSI -dBm- Power level received at the OLT for a specific ONU.

**Impacts and precautions:**

It is not supported to use a key pattern in both ONU and gpon interface IDs ( show interface gpon * onu * ). It is not supported to use ONU ID key pattern together with brief/optical-info/version options ( show interface gpon 1/1/1 onu * brief ). In some scenarios, the ONU logical distance cannot be retrieved correctly and it will be shown as N/A. This behavior can happen specially when the configured PON link maximum distance is close to the ONU logical distance, for example, when the ONU is at 20km distant and PON link maximum distance is configured to 21km.

**Hardware restrictions:**

N/A


### `show interface gpon onu Ethernet`

> **Página:** 1764 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays information about the user’s Ethernet ports of the ONU.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
show interface gpon chassis/slot/port onu [ onu-id ] ethernet [ ethernet-port [ brief | detail | statistics ] ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `chassis/slot/port` — The GPON port on which the ONU is located. — *Valores:* Text: chassis/slot/port format. · *Default:* N/A
- `onu-id` — The ONU to which the Ethernet port belongs to. — *Valores:* onu-id: Number from 0 to 127. · *Default:* N/A
- `ethernet-port` — Number of the ONU’s Ethernet port. — *Valores:* Number from 1 to 4 depending on the ONU profile of the ONU. · *Default:* N/A
- `brief` — Display brief information of the ONU’s Ethernet interfaces. — *Valores:* brief: Fixed text ‘brief’. · *Default:* N/A
- `statistics` — Display statistics information of the ONU’s Ethernet interfaces. — *Valores:* statistics: Fixed text ‘statistics’. · *Default:* N/A
- `detail` — Display detailed information of the ONU’s Ethernet interfaces. — *Valores:* detail: Fixed text ‘detail’. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.8 | Removed no longer valid ‘detail’ and ‘statistics’ parameters. |
| 1.8.2 | Added ‘detail’ and ‘statistics’ parameters. |
| 4.2.0 | Added support for range of IDs in show options. |

**Usage Guidelines:**

```text
# show interface gpon 1/1/8 onu 1 ethernet 1
```

Physical interface : ethernet 1, Enabled, Physical link is up GPON Information : gpon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Show all ethernet UNIs in a given ONU

```text
# show interface gpon 1/1/1 onu 1 ethernet *
```

Physical interface : ethernet 1, Enabled, Physical link is up GPON Information : gpon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Physical interface : ethernet 2, Enabled, Physical link is up GPON Information : gpon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Show all ethernet UNIs in a given ONU

```text
# show interface gpon 1/1/1 onu 1 ethernet
```

Physical interface : ethernet 1, Enabled, Physical link is up GPON Information : gpon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Physical interface : ethernet 2, Enabled, Physical link is up GPON Information : gpon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Show a range ethernet UNIs in a given ONU

```text
# show interface gpon 1/1/1 onu 1 ethernet 1-2
```

Physical interface : ethernet 1, Enabled, Physical link is up GPON Information : gpon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Physical interface : ethernet 2, Enabled, Physical link is up GPON Information : gpon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Show all ethernet UNIs in all ONUs in a given gpon interface

```text
# show interface gpon 1/1/1 onu * ethernet *
```

Physical interface : ethernet 1, Enabled, Physical link is up GPON Information : gpon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Physical interface : ethernet 2, Enabled, Physical link is up GPON Information : gpon-1/1/1, ONU 1 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: 1 Gbit/s Full-Duplex Native VLAN/CoS : - MAC limit : Unlimited Physical interface : ethernet 1, Enabled, Physical link is down GPON Information : gpon-1/1/1, ONU 10 Link-level type : Ethernet Speed/Duplex : Auto Status Negotiation: Native VLAN/CoS : - MAC limit : Unlimited When using detail option, it will override other show options passed. For example, if the operator runs “show interface gpon 1/1/1 onu 1 ethernet 1 brief detail”, “show interface gpon 1/1/1 onu 1 ethernet 1 statistics detail” or “show interface gpon 1/1/1 onu 1 ethernet 1 brief detail statistics” only detail option will be shown. The same way, statistics option will override the default “show interface gpon 1/1/1 onu 1 ethernet 1” or it will have precedence over brief option in “show interface gpon 1/1/1 onu 1 ethernet 1 brief statistics” outputs as well.

**Output Terms:**

Output Description Physical interface Name and status of the GPON interface. Link-level type Type of the Link-level. Speed Speed of the Ethernet UNI. Duplex Duplex configuration. Negotiation Negotiation status (enabled/disabled). Status Negotiation Negotiated Speed and Duplex. Native-vlan Native VLAN of the Ethernet UNI.

**Impacts and precautions:**

It is not supported to use a key pattern in gpon interface IDs ( show interface gpon * onu * ethernet ).

**Hardware restrictions:**

N/A


### `show interface gpon onu gem`

> **Página:** 1769 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays ONU GPON Encapsulation Method information.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
show interface gpon chassis/slot/port onu [ onu-id ] gem [ gem-id ] [ brief | statistics ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `chassis/slot/port` — The GPON port on which the ONU is located. — *Valores:* Text: chassis/slot/port format. · *Default:* N/A
- `onu-id` — The ONU where the GEM is located. — *Valores:* onu-id: Number from 0 to 127 (maximum of 64 elements). · *Default:* N/A
- `gem-id` — The ID of the GEM for information display. — *Valores:* gem-id: Number from 1 to 16. · *Default:* N/A
- `brief` — Display brief information of the GEM. — *Valores:* brief: Fixed text ‘brief’. · *Default:* N/A
- `statistics` — Display statistics information of the ONU’s GEM port. — *Valores:* statistics: Fixed text ‘statistics’. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.4 | The the maximum GEM ID value was changed from 40 to 16. |
| 1.8 | Removed no longer valid ‘statistics’ parameter. |
| 4.2.0 | Added support for range of IDs in show options. |
| 5.12.0 | Added ‘statistics’ parameter. |

**Usage Guidelines:**

Show a GEM in an ONUs

```text
# show interface gpon 1/1/1 onu 13 gem 1
GEM ID : 1
```

GPON Information : gpon-1/1/1, ONU 10 Operational status is : up GEM Port-ID : 352 Alloc-ID : 256 T-CONT : 1 Encryption : disabled Show all GEMs in all ONUs in a given gpon interface

```text
# show interface gpon 1/1/1 onu * gem *
GEM ID : 1
```

GPON Information : gpon-1/1/1, ONU 1 Operational status is : up GEM Port-ID : 305 Alloc-ID : 256 T-CONT : 1 Encryption : disabled GEM ID : 1 GPON Information : gpon-1/1/1, ONU 10 Operational status is : up GEM Port-ID : 450 Alloc-ID : 257 T-CONT : 1 Encryption : disabled Show all GEMs in a given ONU

```text
# show interface gpon 1/1/1 onu 10 gem *
GEM ID : 1
```

GPON Information : gpon-1/1/1, ONU 10 Operational status : down GEM Port-ID : 449 Alloc-ID : 0 T-CONT : 1 Encryption : disabled GEM ID : 2 GPON Information : gpon-1/1/1, ONU 10 Operational status : down GEM Port-ID : 450 Alloc-ID : 0 T-CONT : 1 Encryption : disabled Show all GEMs in a given ONU

```text
# show interface gpon 1/1/1 onu 10 gem
GEM ID : 1
```

GPON Information : gpon-1/1/1, ONU 10 Operational status : down GEM Port-ID : 449 Alloc-ID : 256 T-CONT : 1 Encryption : unknown GEM ID : 2 GPON Information : gpon-1/1/1, ONU 10 Operational status : down GEM Port-ID : 450 Alloc-ID : 256 T-CONT : 1 Encryption : disabled Show GEM statistics

```text
# show interface gpon 1/1/1 onu 10 gem
GEM ID : 1
```

GPON Information : gpon-1/1/1, ONU 10 Operational status : down GEM Port-ID : 449 Alloc-ID : 256 T-CONT : 1 Encryption : unknown Traffic statistics : Input packets : 750 Output packets : 1100 Input octets : 150000 Output octets : 220000

**Output Terms:**

Output Description GEM ID ID of the GEM. Operation status Operational status. is GEM Port-ID ID of the GEM Port. Alloc-ID Alloc ID of the GEM. T-CONT T-CONT ID related to the GEM. Encryption Encryption state (enabled/disabled).

**Impacts and precautions:**

It is not supported to use a key pattern in gpon interface IDs. For example: show interface gpon * onu * gem

**Hardware restrictions:**

N/A


### `show onu-global-count`

> **Página:** 1774 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays global (total of all PON links) ONUs counting.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
show onu-global-count
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.4 | This command was introduced. |

**Usage Guidelines:**

To view the global ONU counting data, just enter the command below. Example:

```text
# show onu-global-count
--ONU Counting of all PONs--
T-O-T-A-L-----N-O-N--P-R-O-V-I-S-I-O-N-E-D-----U-P-----D-O-W-N5 4 1 0
```

**Output Terms:**

Output Description Displays the total number of ONUs on OLT, including Up, Down and TOTAL ONUS non provisioned ONUs. NON PROVISIONED Displays the total number of non provisioned ONUs on OLT. ONUS UP ONUS Displays the total number of ONUs with status UP on OLT. DOWN ONUS Displays the total number of ONUs with status Down on OLT.

**Impacts and precautions:**

Not apply.

**Hardware restrictions:**

N/A


### `show onu-interface-count`

> **Página:** 1776 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays ONUs counting by PON link.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
show onu-interface-count
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.4 | This command was introduced. |

**Usage Guidelines:**

To view the ONU counting data per PON link, just enter the command below. Example:

```text
# show onu-interface-count
NON
```

INTERFACE TOTAL PROVISIONED UP DOWN I-F--I-N-D-E-X----N-A-M-E----------O-N-U-S----O-N-U-S----------O-N-U-S---O-N-U-S--- 101744641 gpon-1/1/1 1 0 1 0 101744672 gpon-1/1/32 4 4 0 0

**Output Terms:**

Output Description IF INDEX Displays the interface index of PON link. INTERFACE NAME Displays the name of the PON link with type and id. Displays the total number of ONUs on PON link, including Up, Down TOTAL ONUS and non provisioned ONUs. NON PROVISIONED Displays the number of non provisioned ONUs on PON link. ONUS UP ONUS Displays the number of ONUs with status Up on PON link DOWN ONUS Displays the number of ONUs with status Down on PON link

**Impacts and precautions:**

Not apply.

**Hardware restrictions:**

N/A CHAPTER 15: XGSPON This chapter describes the commands related to management of XGSPON interfaces and remote ONUs. OLT This topic describes the global commands related to XGSPON OLT, service-port and service-vlan.
