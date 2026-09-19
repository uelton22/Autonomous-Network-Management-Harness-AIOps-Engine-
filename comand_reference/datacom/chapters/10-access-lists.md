# Capítulo 10: Access Lists

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## Basic ACLs

### `access-list acl-profile`

> **Página:** 1374 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command is used to create or enter an Access List Profile. The profile can contain multiple ACL entries used to specify match and action criteria. ACL profiles have priorities among them. An ACL profile must have at least one ACL entry configured. For a profile to take effect, it needs to be applied to an interface. L2 profiles always have priority over L3 profiles.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
acl-profile stage type name priority priority
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `stage` — The ACL profile stage. ingress stage ACLs will affect traffic entering the configured interfaces. cpu stage ACLs will affect traffic entering the CPU. — *Valores:* {ingress | cpu} · *Default:* N/A
- `type` — The ACL profile type. — *Valores:* {l2 | l3 | l3-ipv6} · *Default:* N/A
- `name` — The ACL profile name. — *Valores:* Text · *Default:* N/A
- `priority` — The ACL profile priority, being 0 the highest priority. L2 profiles can have priorities from 0 to 255 and L3 profiles can have priorities from 256 to 511. — *Valores:* 0-511 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.1 | This command was introduced. |
| 5.0 | Added new stage cpu. |
| 11.0 | Added support for DM4340 series. |
| 11.6 | Added support for ACL Type l3-ipv6 for DM4340 series only. |

**Usage Guidelines:**

Creating a L2 Access List Profile at ingress stage with name my_acl_profile and priority 0:

```text
(config)# access-list
(config-acl)# acl-profile ingress l2 my_acl_profile
(config-acl-profile-l2-my_acl_profile)# priority 0
```

Adding an entry to the profile:

```text
(config-acl-profile-l2-my_acl_profile)# access-list-entry 0 action deny
(config-access-list-entry-0)# match vlan 10
```

Apply the profile to an interface so the profile can take effect:

```text
(config)# access-list interface gigabit-ethernet-1/1/1 ingress my_acl_profile
```

**Impacts and precautions:**

ACL Rules created with L2 profiles will match only pure Ethernet headers. If the Ethernet header is encapsulated over any protocol, the rule will not apply. ACL Rules created with L3 profiles will match only L3 packets encapsulated over Ethernet header (i.e. if the L3 packet is encapsulated over PPPoE, or other non Ethernet L2 header, the match will not apply).

**Hardware restrictions:**

The DM4340 series does not support CPU profile stage. The DM4340 supports IPv4 and IPv6 matches in two different L3 profile types: l3 and l3-ipv6.


### `access-list interface`

> **Página:** 1377 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command is used to attach a given ACL profile to an interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
interface interface-name stage profile-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — The interface identification. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, two-hundred-g-ethernet, four-hundred-g-ethernet, gpon, xgspon, cpu-port. · *Default:* N/A
- `stage` — The ACL profile stage. ingress stage ACLs will affect traffic entering the configured interfaces. — *Valores:* ingress · *Default:* N/A
- `profile-name` — The ACL profile name. — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.1 | This command was introduced. |
| 3.0 | Added support for 40G interfaces. |
| 4.6 | Added support for 100G interfaces. |
| 5.0 | Added support for 25G interfaces. |
| 12.0 | Added support for 200G and 400G interfaces. |

**Usage Guidelines:**

Given a profile named l2-ingress-acl, the following sequence of commands will apply it on port gigabit-ethernet-1/1/1:

```text
(config)# access-list
(config-acl)# interface gigabit-ethernet-1/1/1 ingress l2-ingress-acl
(config-acl)# commit
```

You can apply the same profile to several interfaces. You can also apply more than one profile to the same interface.

**Impacts and precautions:**

Every device has a different amount of ACL resources to be used. The resources are consumed when the profile is applied to an interface. Please refer to the hardware restriction section for more information about how they operate on each hardware.

**Hardware restrictions:**

The maximum number of ACL rules will depend on the amount of entries applied to all interfaces. DM4610 supports up to 256 entries per profile type (L2 or L3) applied to all interfaces. For instance, when a L2 profile with 128 entries is applied to two interfaces, no new L2 rules will be allowed to be applied.


### `access-list protection`

> **Página:** 1380 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command is used to apply a given ACL profile to the traffic with CPU destination. It is aimed to allow the user to protect the CPU from malicious traffic data.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920, DM4340.

**Syntax:**

```text
protection stage profile-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `stage` — The ACL profile stage. cpu stage ACLs will affect traffic entering the CPU. — *Valores:* cpu · *Default:* N/A
- `profile-name` — The ACL profile name. — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |
| 12.0 | Added support for DM4780 series. |

**Usage Guidelines:**

To protect the CPU, it is recommended to create an access-list with a White List that blocks all the access to a certain TCP/UDP Destination-Port, and accept connection only from trusted sources: Example:

```text
#config
Entering configuration mode terminal
(config)# access-list
(config-acl)# acl-profile cpu l3 whitelist
(config-acl-profile-l3-whitelist)# priority 0
(config-acl-profile-l3-whitelist)# access-list-entry 0 action permit
(config-access-list-entry-0)# match source-ipv4-address 10.10.0.1
(config-access-list-entry-0)# exit
(config-acl-profile-l3-whitelist)# access-list-entry 1 action permit
(config-access-list-entry-0)# match source-ipv4-address 10.10.1.0/24
(config-access-list-entry-0)# exit
(config-acl-profile-l3-whitelist)# access-list-entry 100 action deny
(config-access-list-entry-0)# match destination-port ssh
(config-access-list-entry-0)# top
(config)# access-list
(config-acl)# protection cpu whitelist
(config-acl)# commit
```

**Impacts and precautions:**

Every device has a different amount of ACL resources to be used. The resources on cpu stage are consumed when the profile is applied as a protection profile.

**Hardware restrictions:**

DM4780 series, on cpu stage, only supports matching by destination IPv4, destination port, ethertype, IP protocol, source IPv4, source IPv6 and source port with actions deny and permit.


### `access-list-entry`

> **Página:** 1383 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Manages Access List Entries at an Access List Profile. Access list entries must contain at least one match and one action.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
access-list-entry entry-id access-list-entry entry-id [match source-mac-address mac-address [match sourcemac-address-mask mac-address-mask]] [match destination-mac-address mac-address [match destination-mac-address-mask mac-address-mask]] [match ethertype ethertype] [match pcp pcp] [match vlan vid] [match inner-pcp pcp] [match inner-vlan vid] [match dscp dscp | match tos tos] [match source-ipv4-address ipv4-address] [match destination-ipv4-address ipv4-address] [match source-ipv6-address ipv6- address] [match destination-ipv6-address ipv6-address] [match ip-protocol ip-protocol] [match destination-port destination-port] [match source-port source-port] [match ttl ttl] access-list-entry entry-id action {deny | permit | redirect | copy pcp | set pcp pcp | set inner-pcp pcp }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `entry-id` — The ACL entry identifier. This value will be used as the relative priority among other ACL entries from the same ACL profile, being 0 the highest priority. — *Valores:* 0-255 · *Default:* N/A
- `match source-mac-address mac-address` — The source MAC address of a match. Available at stages: ingress. Available at types: L2. — *Valores:* xx:xx:xx:xx:xx:xx · *Default:* N/A
- `match source-mac-address-mask mac-address-mask` — A wildcard mask for the source MAC address of a match. This mask is sometimes referred to as an inverse mask because a 1 and 0 mean the opposite of what they mean in a subnet (network) mask. Only bits corresponding to “0” are considered from MAC. Bits with “1” are ignored. This match is only available if a match for a source MAC address has been configured. Available at stages: ingress. Available at types: L2. — *Valores:* xx:xx:xx:xx:xx:xx · *Default:* N/A
- `match destination-mac-address mac-address` — The destination MAC address of a match. Available at stages: ingress. Available at types: L2. — *Valores:* xx:xx:xx:xx:xx:xx | pvst · *Default:* N/A
- `match destination-mac-address-mask mac-address-mask` — A wildcard mask for the destination MAC address of a match. This mask is sometimes referred to as an inverse mask because a 1 and 0 mean the opposite of what they mean in a subnet (network) mask. Only bits corresponding to “0” are considered from MAC. Bits with “1” are ignored. This match is only available if a match for a destination MAC address has been configured. Available at stages: ingress. Available at types: L2. — *Valores:* xx:xx:xx:xx:xx:xx · *Default:* N/A
- `match ethertype ethertype` — The Ethernet type code for a match. Available at stages: ingress, cpu. Available at types: L2 (on ingress stage), L3 (on cpu stage). — *Valores:* 0x0000-0xffff | arp | bpdu | ipv4 | ipv6 | mpls | mpls-mcast | pppoed | pppoes | snmp · *Default:* N/A
- `match pcp pcp` — Outer priority 802.1p for a match. Available at stages: ingress. Available at types: L2, L3. — *Valores:* 0-7 · *Default:* N/A
- `match vlan vid` — Outer VLAN ID for a match. Available at stages: ingress, cpu. Available at types: L2, L3. — *Valores:* 1-4094 · *Default:* N/A
- `match inner-pcp pcp` — Inner priority 802.1p for a match. The inner Priority 802.1p is the PCP in the second VLAN Tag after ingress VLAN manipulations (QinQ/Vlan Translations). It is applicable only to double tagged packets. Available at stages: ingress. Available at types: L2, L3. — *Valores:* 0-7 · *Default:* N/A
- `match inner-vlan vid` — Inner VLAN ID for a match. The inner VLAN is the second VLAN Tag after ingress VLAN manipulations (QinQ/Vlan Translations). It is applicable only to double tagged packets. Available at stages: ingress. Available at types: L2, L3. — *Valores:* 1-4094 · *Default:* N/A
- `match dscp dscp` — The Differentiated Services Code Point code for a match. Remark: DSCP match can not be configured with ToS match in the same entry. Available at stages: ingress. Available at types: L3. — *Valores:* 0-63 | 0 | af11 | af12 | af13 | af21 | af22 | af23 | af31 | af32 | af33 | af41 | af42 | af43 | cs1 | cs2 | cs3 | cs4 | cs5 | cs6 | cs7 | ef · *Default:* N/A
- `match tos tos` — The IPv4 Type of Service or IPv6 Traffic Class for a match. Remark: ToS match can not be configured with DSCP match in the same entry. Available at stages: ingress. Available at types: L3. — *Valores:* 0-255 · *Default:* N/A
- `match source-ipv4-address ipv4-address` — The source IPv4 address and an optional mask of a match. This match must not be configured in the same access-list-entry as the IPv6 matches Available at stages: ingress, cpu. Available at types: L3. — *Valores:* [a.b.c.d | a.b.c.d/x] · *Default:* N/A
- `match destination-ipv4-address ipv4-address` — The destination IPv4 address and an optional mask of a match. This match must not be configured in the same access-list-entry as the IPv6 matches Available at stages: ingress, cpu. Available at types: L3. — *Valores:* [a.b.c.d | a.b.c.d/x] · *Default:* N/A
- `match source-ipv6-address ipv6-address` — The source IPv6 address and an optional mask of a match. This match must not be configured in the same access-list-entry as the IPv4 matches Available at stages: cpu. Available at types: L3. — *Valores:* [X:X:X:X::X | X:X:X:X::X/Y] · *Default:* N/A
- `match destination-ipv6-address ipv6-address` — The destination IPv6 address and an optional mask of a match. This match must not be configured in the same access-list-entry as the IPv4 matches Available at stages: cpu. Available at types: L3. — *Valores:* [X:X:X:X::X | X:X:X:X::X/Y] · *Default:* N/A
- `match ip-protocol ip-protocol` — The IPv4 or IPv6 protocol field of a match. Available at stages: ingress, cpu. Available at types: L3. — *Valores:* 0-255 | icmp | igmp | ipv6-icmp | tcp | udp · *Default:* N/A
- `match destination-port destination-port` — TCP/UDP destination port number of a match. Available at stages: ingress, cpu. Available at types: L3. — *Valores:* 0-65535 | bgp | dns | ftpdata | ftpcontrol | http | https | ntp | smb | snmp | snmptrap | ssh | telnet | whois · *Default:* N/A
- `match source-port source-port` — TCP/UDP source port number of a match. Available at stages: ingress, cpu. Available at types: L3. — *Valores:* 0-65535 | bgp | dns | ftpdata | ftpcontrol | http | https | ntp | smb | snmp | snmptrap | ssh | telnet | whois · *Default:* N/A
- `match ttl ttl` — IPv4 TTL or IPv6 Hop Limit field. Available at stages: cpu. Available at types: L3. — *Valores:* 0-255 · *Default:* N/A
- `action deny` — Action to deny, i.e. drop any packets matching the filter. Available at stages: ingress, cpu. Available at types: L2, L3. — *Valores:* N/A · *Default:* N/A
- `action permit` — Action to permit, i.e. allow any packets that was blocked by a deny rule. Available at stages: ingress, cpu. Available at types: L2, L3. — *Valores:* N/A · *Default:* N/A
- `action redirect` — Action to redirect, i.e. redirect any packets matching the filter to an specific queue. Available at stages: cpu. Available at types: L3. — *Valores:* N/A · *Default:* N/A
- `action copy pcp` — Action to copy the PCP field value from inner VLAN tag of the frame to the outer VLAN tag. Available at stages: ingress. Available at types: L2, L3. This action can not be configured if already exists action set pcp. — *Valores:* N/A · *Default:* N/A
- `action set pcp pcp` — Action to set or replace the PCP field value of the frame with parameter set in action. This action also schedules the packet to a QoS scheduling queue. Please refer to the QoS chapters for more information about the QoS features. Available at stages: ingress. Available at types: L2, L3. This action can not be configured if already exists action copy pcp. — *Valores:* 0-7 · *Default:* N/A
- `action set inner-pcp pcp` — Action to set or replace the PCP field value of the inner VLAN tag in frame with parameter set in action. Available at stages: ingress. Available at types: L2, L3. This action is not available for DM4050 and DM4250 series. — *Valores:* 0-7 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. Removed actions set DSCP and set queue. Added action permit. Re1.1 moved match interface. |
| 3.0 | Added new L3 matches: ip-protocol and destination-port. |
| 4.4 | Added new L3 matches: vlan and pcp. |
| 4.6 | Added new L3 match: tos |
| 4.7 | Added new L2 and L3 matches: inner-vlan and inner-pcp. |
| 4.8 | Added action set inner-pcp on ingress ACLs. |
| 5.0 | Added new stage cpu, and matches source-port and ttl |
| 5.6 | Added action copy pcp on ingress ACLs. |
| 7.0 | Added action redirect on cpu ACLs. |
| 8.2 | Added new L3 ingress match: source-port Added option to L2 ingress match destination-mac-address: pvst |
| 10.6 | Added new L3 cpu matches: source-ipv6-address and destination-ipv6- address |
| 11.0 | Added support for DM4340 series |
| 12.0 | Added support for DM4780 series. |

**Usage Guidelines:**

As ACL entries must be in an ACL profile, it is necessary first to create an Access List Profile. The profile needs a stage, type, priority and name. In this case the stage is ingress, the type is L2, the name is l2-ingress-acl and the priority 0:

```text
(config)# access-list acl-profile ingress l2 l2-ingress-acl
(config-acl-profile-l2-l2-ingress-acl)# priority 0
```

The ACL entry must be created with its id as well:

```text
(config-acl-profile-l2-l2-ingress-acl)# access-list-entry 2
(config-access-list-entry-2)#
```

Then it is possible to add matches and actions, for instance, to deny all ingress traffic with VLAN tag 10:

```text
(config-access-list-entry-2)# match vlan 10
(config-access-list-entry-2)# action deny
```

It is possible to augment this entry with more matches of type L2. For instance, adding a match to the source MAC address with a mask will start blocking only traffic from that VLAN with the specified set of MAC addresses.

```text
(config-access-list-entry-2)#
match source-mac-address 00:00:00:00:00:ad
match source-mac-address-mask ff:ff:ff:ff:ff:00
```

In this case, the match specifies all MAC addresses that ends with the ad octet. In the end, you must apply the profile created to an interface for the entry to take effect.

```text
(config)# access-list
(config-acl)# interface gigabit-ethernet-1/1/1 ingress l2-ingress-acl
(config-acl)# commit
```

After the commit, all packets arriving on interface gigabit-ethernet-1/1/1 with a VLAN tag of 10 and source MAC address ending in ad will be dropped.

**Impacts and precautions:**

None

**Hardware restrictions:**

DM4050 and DM4250 series do not support action set inner-pcp. DM4050, DM4170, DM4250, DM4370, DM4376 and DM46xx series do not support match destination-ipv6-address. DM4340 and DM4780 series only supports L2 ingress matching by vlan, ethertype, destination MAC and source MAC with actions deny, permit and set pcp. DM4780 series requires ip-protocol match (TCP or UDP) when source port or destination port match is configured.


### `show acl-resources`

> **Página:** 1394 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** This command is used to display the ACL resources status.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show acl-resources [ brief | detail | extensive ] show acl-resources [ interface [ interface-name ] ] [ detail | extensive ]
```

**Parameters:**

- `brief` — This parameter displays a summary information split into two big groups: L2 ACL resources and L3 ACL resources. — *Valores:* N/A · *Default:* None
- `detail` — This parameter displays detailed ACL resources information about the profiles and general ACL interfaces resources information. — *Valores:* N/A · *Default:* None
- `extensive` — This parameter displays detailed ACL resources information about the profiles and the interface information discriminating the resources spent by each profile in each interface. — *Valores:* N/A · *Default:* None
- `interface` — This parameter displays only ACL resources information related to interfaces. — *Valores:* N/A · *Default:* None
- `interface-name` — This parameter displays resources information of a specific interface. — *Valores:* N/A · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 5.0 | Added new stage cpu. |

**Usage Guidelines:**

Given the equipment has a total of 256 entries for ingress L2 ACLs, 256 entries for ingress L3 ACLs and 256 entries for CPU L3 ACLs, and the following configuration is applied:

```text
DmOS# show running-config
access-list
interface gigabit-ethernet-1/1/1
ingress testL2
!
interface gigabit-ethernet-1/1/2
ingress testL2 testL3-OneEntry
!
interface gigabit-ethernet-1/1/3
ingress testL2 testL3-OneEntry testL3-ZeroEntries
!
acl-profile ingress l2 testL2
priority 0
access-list-entry 0
action permit
!
access-list-entry 1
action permit
!
!
acl-profile ingress l3 testL3-OneEntry
priority 256
access-list-entry 0
action permit
!
!
acl-profile ingress l3 testL3-ZeroEntries
priority 257
!
acl-profile cpu l3 cpuL3
priority 1
access-list-entry 0
action permit
!
access-list-entry 1
action permit
!
access-list-entry 2
action permit
!
!
```

To display just a summary of resources use show acl-resources brief:

```text
DmOS# show acl-resources brief
```

Total ingress L2 entries: 256 Used ingress L2 entries: 6 Free ingress L2 entries: 250 Total ingress L3 entries: 256 Used ingress L3 entries: 2 Free ingress L3 entries: 254 Total CPU L3 entries: 256 Used CPU L3 entries: 3 Free CPU L3 entries: 253 Note that the testL3-ZeroEntries does not count towards Used L3 entries just because it does not have any entry inside it. To display a detailed information of resources use show acl-resources detail. This command will display the amount of used entries by profile, summing all interfaces that use that profile, and the amount of used entries per interface summing all profiles that the interface uses:

```text
DmOS# show acl-resources detail
```

ACL Ingress L2 Profile Used entries ------------------------------------------------ ------------ testL2 6 -------------------------------------------------------------- TOTAL 6 ACL Ingress L3 Profile Used entries ------------------------------------------------ ------------ testL3-OneEntry 2 testL3-ZeroEntries 0 -------------------------------------------------------------- TOTAL 2 ACL CPU L3 Profile Used entries ------------------------------------------------ ------------ cpuL3 3 -------------------------------------------------------------- TOTAL 3 Interface Used L2 Entries Used L3 Entries ----------------------------- --------------- --------------- gigabit-ethernet-1/1/1 2 gigabit-ethernet-1/1/2 2 1 gigabit-ethernet-1/1/3 2 1 ----------------------------- --------------- --------------- TOTAL 6 2 To display an extensive information use show acl-resources extensive command. The description of the profiles will be the same as in show acl-resources detail, but the description of the interfaces will name all profiles that are consuming entries on that particular interface, instead of just the entry amount:

```text
DmOS# show acl-resources extensive
```

ACL Ingres L2 Profile Used entries ------------------------------------------------ ------------ testL2 6 -------------------------------------------------------------- TOTAL 6 ACL Ingress L3 Profile Used entries ------------------------------------------------ ------------ testL3-OneEntry 2 testL3-ZeroEntries 0 -------------------------------------------------------------- TOTAL 2 ACL CPU L3 Profile Used entries ------------------------------------------------ ------------ cpuL3 3 -------------------------------------------------------------- TOTAL 3 ================================= = gigabit-ethernet-1/1/1 = ================================= ACL Ingress L2 Profile Used entries ------------------------------------------------ ------------ testL2 2 -------------------------------------------------------------- TOTAL 2 ================================= = gigabit-ethernet-1/1/2 = ================================= ACL Ingress L2 Profile Used entries ------------------------------------------------ ------------ testL2 2 -------------------------------------------------------------- TOTAL 2 ACL Ingress L3 Profile Used entries ------------------------------------------------ ------------ testL3-OneEntry 1 -------------------------------------------------------------- TOTAL 1 ================================= = gigabit-ethernet-1/1/3 = ================================= ACL Ingress L2 Profile Used entries ------------------------------------------------ ------------ testL2 2 -------------------------------------------------------------- TOTAL 2 ACL Ingress L3 Profile Used entries ------------------------------------------------ ------------ testL3-OneEntry 1 testL3-ZeroEntries 0 -------------------------------------------------------------- TOTAL 1 When it’s necessary to display only information about the interfaces, or about a specific interface, it’s possible to use show acl-resources interface or show acl-resources interface interface-name. These commands can also be followed by detail and extensive marks:

```text
DmOS# show acl-resources interface detail
```

Interface Used L2 Entries Used L3 Entries ----------------------------- --------------- --------------- gigabit-ethernet-1/1/1 2 gigabit-ethernet-1/1/2 2 1 gigabit-ethernet-1/1/3 2 1 ----------------------------- --------------- --------------- TOTAL 6 2

```text
DmOS# show acl-resources interface extensive
=================================
= gigabit-ethernet-1/1/1 =
=================================
```

ACL Ingress L2 Profile Used entries ------------------------------------------------ ------------ testL2 2 -------------------------------------------------------------- TOTAL 2 ================================= = gigabit-ethernet-1/1/2 = ================================= ACL Ingress L2 Profile Used entries ------------------------------------------------ ------------ testL2 2 -------------------------------------------------------------- TOTAL 2 ACL Ingress L3 Profile Used entries ------------------------------------------------ ------------ testL3-OneEntry 1 -------------------------------------------------------------- TOTAL 1 ================================= = gigabit-ethernet-1/1/3 = ================================= ACL Ingress L2 Profile Used entries ------------------------------------------------ ------------ testL2 2 -------------------------------------------------------------- TOTAL 2 ACL Ingress L3 Profile Used entries ------------------------------------------------ ------------ testL3-OneEntry 1 testL3-ZeroEntries 0 -------------------------------------------------------------- TOTAL 1

```text
DmOS# show acl-resources interface gigabit-ethernet-1/1/1 detail
```

Interface Used L2 Entries Used L3 Entries ----------------------------- --------------- --------------- gigabit-ethernet-1/1/1 2

```text
DmOS# show acl-resources interface gigabit-ethernet-1/1/1 extensive
=================================
= gigabit-ethernet-1/1/1 =
=================================
```

ACL Ingress L2 Profile Used entries ------------------------------------------------ ------------ testL2 2 -------------------------------------------------------------- TOTAL 2

**Output Terms:**

Output Description Total entries Total number of entries available on hardware. Used entries Number of hardware resources spent. Free entries Number of unused resources.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

The Total Entries value could vary according to the product. CHAPTER 11: SECURITY This chapter describes the commands related to management of security features in the DmOS CLI. AAA This topic describes the commands related to management of authentication, authorization and accounting such as commands to configure Radius or Tacacs+ external servers or to manage the local user database.
