# Capítulo 6: Layer 3 - Routing

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## Basic

### `clear ip host-table`

> **Página:** 504 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Clears the neighbor cache table of the system.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
clear ip host-table [ intf l3-if ] clear ip host-table [ vrf {vrf-name | all} | ip-address a.b.c.d | port port-if ]*
```

**Parameters:**

- `ip-address a.b.c.d` — Clear host with specified IPv4 address from system ARP cache. — *Valores:* a.b.c.d. · *Default:* N/A
- `intf l3-if` — Clear all hosts with specified L3 interface from system ARP cache. — *Valores:* Name of L3 interface. · *Default:* N/A
- `port port-if` — Clear all hosts with specified physical port interface from system ARP cache. — *Valores:* Name of physical port. · *Default:* N/A
- `vrf vrf-name` — Clear all hosts with specified VRF name from system ARP cache. When no VRF is specified, the clear will be performed on the global VRF. — *Valores:* Name of the VRF. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10.0 | This command was introduced. |
| 4.4 | VRF parameter support. |

**Usage Guidelines:**

Clearing the neighbor cache table of the system forces the deletion of all dynamically learned entries, except those that are next-hop. Next-hop entries will be probed and refreshed. After executing this command it is possible to ensure the correct mapping between learned IP addresses with their corresponding MAC addresses. This command clears IPv4 and IPv6 hosts, but the ip-address parameter only accepts IPv4 addresses at the moment.

**Impacts and precautions:**

Clearing hosts may cause temporary traffic disruption.

**Hardware restrictions:**

N/A


### `ip arp aging-time`

> **Página:** 507 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures aging-time for ARP entries

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
ip arp aging-time value
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `value` — Specifies the time in seconds that an ARP entry stays in cache. — *Valores:* 200-1000000. · *Default:* 3600.

**Default:** Aging-time of 3600 seconds.

**History:**

| Release | Modification |
| --- | --- |
| 1.10.0 | This command was introduced. |

**Usage Guidelines:**

The aging-time ensures that the ARP cache does not retain learned entries that are no longer used. To configure ARP aging-time the following command can be used: Example: DM4610(config)# ip arp aging-time 500 If ‘no’ command is used, the default value is applied: DM4610(config)# no ip arp aging-time

**Impacts and precautions:**

For longer aging-time periods, the ARP cache can retain entries that are no longer used. And as you reduce the ARP timeout, your network resolution traffic can increase. The general recommended value for aging-time is the configured default value, which is 1 hour (3600 seconds).

**Hardware restrictions:**

N/A


### `prefix-list`

> **Página:** 509 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Prefix list configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
prefix-list name seq seq-number action { permit | deny } [ address prefix ] [ le prefix-len ] [ ge prefix-len]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `prefix-list name` — Creates a prefix list with the given name. — *Valores:* N/A · *Default:* N/A
- `seq seq-number` — Apply the sequence number to the prefix list entry. — *Valores:* 1-4294967295. · *Default:* N/A
- `action` — The action permit allows a matched prefix. The action deny denies a matched prefix. — *Valores:* permit - deny. · *Default:* permit.
- `address prefix` — A unicast IP/IPv6 prefix/mask format. — *Valores:* <a.b.c.d/x> or <x:x:x:x::x/x>. · *Default:* N/A
- `le prefix-len` — The maximum prefix length to match. — *Valores:* 1-128. · *Default:* N/A
- `ge prefix-len` — The minimum prefix length to match. — *Valores:* 1-128. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 4.8 | Added support to IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a prefix list that only permits the network address 50.50.50.0/24.

```text
(config)# prefix-list TEST
(config-prefix-list-TEST)# seq 10
(config-seq-10)# address 50.50.50.0/24
(config-seq-10)# commit
```

Commit complete. This example shows how to configure a prefix list which allows both prefixes 60.60.60.0/24 and 60.60.60.0/25.

```text
(config)# prefix-list TEST_RANGE
(config-prefix-list-TEST_RANGE)# seq 20
(config-seq-20)# address 60.60.60.0/24 ge 24 le 25
(config-seq-20)# commit
```

Commit complete. This example shows how to configure a prefix list that denies the network address 60.60.60.0/24 but allows the others.

```text
(config)# prefix-list TEST_DENY
(config-prefix-list-TEST_DENY)# seq 20
(config-seq-20)# action deny
(config-seq-20)# address 60.60.60.0/24
(config-seq-20)# exit
(config-prefix-list-TEST_DENY)# seq 30
(config-seq-30)# address 0.0.0.0/0 le 32
(config-seq-30)# commit
```

Commit complete. This example shows how to configure a prefix list that denies the network address 2001::/64 but allows the others.

```text
(config)# prefix-list TEST_DENY
(config-prefix-list-TEST_DENY)# seq 20
(config-seq-20)# action deny
(config-seq-20)# address 2001::/64
(config-seq-20)# exit
(config-prefix-list-TEST_DENY)# seq 30
(config-seq-30)# address ::/0 le 128
(config-seq-30)# commit
```

Commit complete.

**Impacts and precautions:**

When the prefix list is associated with a route map the permit or deny action configuration of the prefix list entry is ignored. In case of prefix list directly associated with a BGP neighbor and no permit action matches are found, all routes will be denied. Therefore, it is necessary to add an additional sequence with a clause to permit the other routes by setting a matching all address (0.0.0.0/0 le 32). Notice that a route policy associated with a neighbor have precedence over a prefix list directly associated with it. If there is no route refresh capability support any update on the prefix list configuration that is associated with a BGP neighbor will cause its BGP session to be restarted. Updates on prefix-lists associated with a neighbor or with a route map will trigger either route-refresh or update messages. Route-refresh messages request to the neighbor the sending of all its prefixes. Differently from a route-refresh message the sending of update messages is an optimization because only the prefixes not included on the previous BGP update will be advertised.

**Hardware restrictions:**

N/A


### `router static address-family ipv4`

> **Página:** 513 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an IPv4 static route.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
router static [ vrf vrf-name ] address-family ipv4 a.b.c.d/x { { next-hop a.b.c.d [administrative-distance distance] [administrative-status status] [interface interface-name] [metric metric-value] } | { black-hole } }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vrf-name` — Specifies the name of the VRF this IPv4 route will be associated with. — *Valores:* N/A · *Default:* N/A
- `a.b.c.d/x` — Specifies the IPv4 network address for the destination. — *Valores:* Must be a valid IPv4 network address and prefix length. · *Default:* N/A
- `next-hop a.b.c.d` — Specifies the IPv4 address of the next hop for this static route. — *Valores:* Must be a valid IPv4 address. · *Default:* N/A
- `administrative-distance distance` — Specifies the administrative distance for the static route. — *Valores:* 1-255. · *Default:* 1.
- `administrative-status status` — Activates (up) or deactivates (down) the static route. — *Valores:* {up | down}. · *Default:* up.
- `interface interface-name` — Specifies the L3 interface to be used as output interface for the static route. — *Valores:* Must be a valid L3 interface name. · *Default:* N/A
- `metric metric-value` — Specifies the metric for the static route. — *Valores:* 0 - 65535. · *Default:* 0.
- `black-hole` — Specifies that all traffic to IPv4 network address must be discarded. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced supporting only IPv4 routes |
| 2.4 | This command was changed to support IPv6, VRF and output interface. |
| 3.0 | This command was changed to support administrative distance. |
| 5.4 | Added support for black-hole. |
| 9.0 | This command was changed to support the metric parameter. |

**Usage Guidelines:**

Currently are supported up to 1000 IPv4 static routes. If IPv6 static routes are configured, the following constraint must be considered: (number of IPv6 static routes x 2) + number of IPv4 routes <= 1000 Example: This example shows how to configure an IPv4 static route.

```text
(config)# router static address-family ipv4
(config-static-ipv4)# 203.0.113.0/24 next-hop 198.51.100.254
(config-static-ipv4-203.0.113.0/24-198.51.100.254)# commit
```

Commit complete. Example: This example shows how to configure an IPv4 static route in VRF green.

```text
(config)# router static vrf green address-family ipv4
(config-static-vrf-ipv4)# 203.0.113.0/24 next-hop 198.51.100.254
(config-static-vrf-ipv4-203.0.113.0/24-198.51.100.254)# commit
```

Commit complete. Example: This example shows how to configure an IPv4 static route with administrative distance.

```text
(config)# router static address-family ipv4
(config-static-ipv4)# 203.0.113.0/24 next-hop 198.51.100.254
(config-static-ipv4-203.0.113.0/24-198.51.100.254)# administrative-distance 2
(config-static-ipv4-203.0.113.0/24-198.51.100.254)# commit
```

Commit complete. Example: This example shows how to configure an IPv4 static route with metric.

```text
(config)# router static address-family ipv4
(config-static-ipv4)# 203.0.113.0/24 next-hop 198.51.100.254
(config-static-ipv4-203.0.113.0/24-198.51.100.254)# metric 3
(config-static-ipv4-203.0.113.0/24-198.51.100.254)# commit
```

Commit complete. Example: This example shows how to configure an IPv4 static route with black-hole.

```text
(config)# router static address-family ipv4
(config-static-ipv4)# 203.0.113.0/24 black-hole
(config-static-ipv4-203.0.113.0/24-black-hole)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

Some platforms may have VRF restrictions, only supporting ‘global’ and ‘mgmt’ VRFs.


### `router static address-family ipv6`

> **Página:** 517 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an IPv6 static route.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
router static [ vrf vrf-name ] address-family ipv6 x:x:x:x::x/y { { next-hop x:x:x:x::x [administrative-distance distance] [administrative-status status] [interface interface-name] [metric metric-value] } | { black-hole } }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vrf-name` — Specifies the name of the VRF this IPv6 route will be associated with. — *Valores:* N/A · *Default:* N/A
- `x:x:x:x::x/y` — Specifies the IPv6 network address for the destination. — *Valores:* Must be a valid IPv6 network address and prefix length. · *Default:* N/A
- `next-hop x:x:x:x::x` — Specifies the IPv6 address of the next hop for this static route. — *Valores:* Must be a valid IPv6 address. · *Default:* N/A
- `administrative-distance distance` — Specifies the administrative distance for the static route. — *Valores:* 1-255. · *Default:* 1.
- `administrative-status status` — Activates (up) or deactivates (down) the static route. — *Valores:* {up | down}. · *Default:* up.
- `interface interface-name` — Specifies the L3 interface to be used as output interface for the static route. — *Valores:* Must be a valid L3 interface name. · *Default:* N/A
- `metric metric-value` — Specifies the metric for the static route. — *Valores:* 0 - 65535. · *Default:* 0.
- `black-hole` — Specifies that all traffic to IPv6 network address must be discarded. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 3.0 | This command was changed to support administrative distance. |
| 5.4 | Added support for black-hole. |
| 6.0 | Introduced VRF support. |
| 9.0 | This command was changed to support the metric parameter. |

**Usage Guidelines:**

Currently are supported up to 500 IPv6 static routes. If IPv4 static routes are configured, the following constraint must be considered: (number of IPv6 static routes x 2) + number of IPv4 routes <= 1000 Example: This example shows how to configure an IPv6 static route.

```text
(config)# router static address-family ipv6
(config-static-ipv6)# 2001:db8::/64 next-hop 2001:db8:1::1
(config-static-ipv6-2001:db8::/64-2001:db8:1::1)# commit
```

Commit complete. Example: This example shows how to configure an IPv6 static route in VRF green.

```text
(config)# router static vrf green address-family ipv6
(config-static-vrf-ipv6)# 2001:db8::/64 next-hop 2001:db8:1::1
(config-static-vrf-ipv6-2001:db8::/64-2001:db8:1::1)# commit
```

Commit complete. Example: This example shows how to configure an IPv6 static route with administrative distance.

```text
(config)# router static address-family ipv6
(config-static-ipv6)# 2001:db8::/64 next-hop 2001:db8:1::1
(config-static-ipv6-2001:db8::/64-2001:db8:1::1)# administrative-distance 2
(config-static-ipv6-2001:db8::/64-2001:db8:1::1)# commit
```

Commit complete. Example: This example shows how to configure an IPv6 static route with metric.

```text
(config)# router static address-family ipv6
(config-static-ipv6)# 2001:db8::/64 next-hop 2001:db8:1::1
(config-static-ipv6-2001:db8::/64-2001:db8:1::1)# metric 3
(config-static-ipv6-2001:db8::/64-2001:db8:1::1)# commit
```

Commit complete. Example: This example shows how to configure an IPv6 static route with black-hole.

```text
(config)# router static address-family ipv6
(config-static-ipv6)# 2001:db8::/64 black-hole
(config-static-ipv6-2001:db8::/64-black-hole)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

Some platforms may have VRF restrictions, only supporting ‘global’ and ‘mgmt’ VRFs.


### `show ip fib`

> **Página:** 521 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays IPv4 route information from Forwarding Information Base (FIB).

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
show ip fib [ vrf { vrf-name | all } ] { brief } [ network ip-address | state route-state ]
```

**Parameters:**

- `vrf vrf-name` — Specifies the name of the VRF to filter displayed information. — *Valores:* Name of VRF to display information. · *Default:* N/A
- `brief` — Displays brief information about IPv4 route from FIB. — *Valores:* N/A · *Default:* N/A
- `network ip-address` — IPv4 address and mask network used to filter the output. — *Valores:* a.b.c.d/x · *Default:* N/A
- `state route-state` — Route state used to filter the output. — *Valores:* active | inactive | installing | no ecmp resources | pending · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |
| 4.0 | Route state ‘inactive’ created. |
| 4.6 | Filter by VRF changed. |
| 5.4 | Black-hole route support was added. |
| 9.0 | Route state ‘installing’ created. |
| 9.8 | Route state ‘no ecmp resources’ created. |

**Usage Guidelines:**

To simply show IPv4 FIB information, the following command can be used: Example:

```text
# show ip fib brief
```

VRF-name Network Next-hop Logical-interface State ------------------------------------------------------------------ global 10.1.30.0/24 10.1.30.10 l3-vlan 30 active global 10.1.30.0/24 10.1.31.10 l3-vlan 31 active global 10.1.40.0/24 10.1.40.10 l3-vlan 40 inactive global 10.1.100.0/24 10.1.100.10 l3-vlan 100 pending global 10.1.200.0/24 10.1.200.10 l3-vlan 200 active global 10.1.201.0/24 0.0.0.0 black-hole-0 active It is possible to filter the output by Network, State and VRF. Filter by Network: Example:

```text
# show ip fib brief network 10.1.100.0/24
```

VRF-name Network Next-hop Logical-interface State ------------------------------------------------------------------ global 10.1.100.0/24 10.1.100.10 l3-vlan 100 pending Filter by State: Example:

```text
# show ip fib brief state pending
```

VRF-name Network Next-hop Logical-interface State ------------------------------------------------------------------ global 10.1.100.0/24 10.1.100.10 l3-vlan 100 pending Filter by VRF: Example:

```text
# show ip fib vrf all brief
```

VRF-name Network Next-hop Logical-interface State ------------------------------------------------------------------ global 10.1.30.0/24 10.1.30.10 l3-vlan 30 active global 10.1.40.0/24 10.1.40.10 l3-vlan 40 inactive global 10.1.100.0/24 10.1.100.10 l3-vlan 100 pending global 10.1.200.0/24 10.1.200.10 l3-vlan 200 active black 10.1.200.0/24 10.1.200.10 l3-vlan 201 active red 10.1.200.0/24 10.1.200.10 l3-vlan 202 active

**Output Terms:**

Output Description VRF-name Display the VRF name associated with the IPv4 route. Display the destination IPv4 address and mask of the remote netNetwork work. Next-hop Display the IPv4 address of the next router to the remote network. Display the output logical interface to reach the remote network, or Logical-interface display black-hole-0 for routes that discard traffic. Display the route state. The active state represents installed routes; the inactive state represents unsupported routes that will not be installed; the installing state means that the route is waiting for nextState hop resolution; the no ecmp resources state points to the exhaustion of ECMP groups in hardware; and the pending state represents valid routes currently not installed due to a hardware limitation.

**Impacts and precautions:**

Depending on the number of routes installed, the execution of the command may take a while.

**Hardware restrictions:**

N/A


### `show ip host-table`

> **Página:** 525 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows the list of hosts present in the system.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show ip host-table [ vrf { vrf-name | all } ] { brief } [ address ip-address | mac { mac-address | incomplete } | type host-type ]
```

**Parameters:**

- `vrf vrf-name` — Specifies the name of the VRF to filter displayed information. — *Valores:* Name of VRF to display information. · *Default:* N/A
- `brief` — Displays brief information about IP hosts. — *Valores:* N/A · *Default:* N/A
- `address ip-address` — IP address used to filter the output. — *Valores:* a.b.c.d · *Default:* N/A
- `mac mac-address` — MAC address used to filter the output. — *Valores:* XX:XX:XX:XX:XX:XX | incomplete · *Default:* N/A
- `type host-type` — Type of host to filter the output. — *Valores:* dynamic | local | static | unknown · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.8 | This command was introduced. |
| 4.4 | Added VRF-name column and filter by VRF. |

**Usage Guidelines:**

To simply show the list of hosts the following command can be used: Example:

```text
# show ip host-table brief
```

To show the the list of hosts of all VRFs the following command can be used: Example:

```text
# show ip host-table vrf all brief
```

To show the the list of hosts of an specific VRF the following command can be used: Example:

```text
# show ip host-table vrf vrf-test brief
```

It is possible to filter the results by IP address, MAC address and Type. Filter by IP: Example:

```text
# show ip host-table brief address 1.1.10.1
```

Filter by MAC: Example:

```text
# show ip host-table brief mac 00:11:22:33:44:55
```

Filter by Type: Example:

```text
# show ip host-table brief type local
```

**Output Terms:**

Output Description VRF-name Display the VRF name associated with the host. Address Display the IP addresses associated with host. MAC Display the MAC addresses associated with host IP addresses. Display the logical interface on which the respective host is associLogical interface ated. Physical interface Display the physical interface on which the respective host is associated. Type Display the type of the host entry.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip rib`

> **Página:** 529 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays route information from Routing Information Base (RIB).

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
show ip rib [bgp | connected | destination ip-address | ospf | static | vrf name ]
```

**Parameters:**

- `bgp` — Displays route information filtering by BGP routes. — *Valores:* N/A · *Default:* N/A
- `connected` — Displays route information filtering by connected routes and local IP addresses. — *Valores:* N/A · *Default:* N/A
- `destination ip-address` — Displays route information filtering by exact match of destination IP address and mask. — *Valores:* a.b.c.d/x · *Default:* N/A
- `ospf` — Displays route information filtering by OSPF routes. — *Valores:* N/A · *Default:* N/A
- `static` — Displays route information filtering by static routes. — *Valores:* N/A · *Default:* N/A
- `vrf name` — Displays route information for VRF name. — *Valores:* Name of VRF. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.8 | This command was introduced. |
| 2.0 | The command was modified to have OSPF input/output. |
| 2.4 | The command was modified to have VRF. |
| 4.0 | The command was modified to have BGP filter. |
| 5.4 | Black-hole route support was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples show how to use the show ip rib command.

```text
# show ip rib
```

Type Codes: C - connected, S - static, L - local, O - OSPF, B - BGP E1 - OSPF external type 1, E2 - OSPF external type 2, IA - OSPF inter area, Output Interface Codes: DC - directly connected Type Dest Address/Mask Next-hop Age AD Metric Output Interface ------ ------------------- --------------- -------- --- ------ ---------------- S 192.0.2.0/25 0.0.0.0 00:46:42 1 0 black-hole-0 S 192.0.2.128/25 0.0.0.0 00:46:42 1 0 black-hole-0 S 198.51.100.0/26 198.51.100.66 00:46:42 1 0 loose-next-hop C 198.51.100.64/26 198.51.100.65 01:15:48 0 0 mgmt-1/1/1 L 198.51.100.65/32 0.0.0.0 01:15:48 0 0 DC C 198.51.100.128/26 198.51.100.129 00:05:48 0 0 l3-vlan 100 L 198.51.100.129/32 0.0.0.0 00:05:48 0 0 DC

```text
# show ip rib vrf red
```

Type Codes: C - connected, S - static, L - local, O - OSPF, B - BGP E1 - OSPF external type 1, E2 - OSPF external type 2, IA - OSPF inter area, Output Interface Codes: DC - directly connected Type Dest Address/Mask Next-hop Age AD Metric Output Interface ------ ------------------- --------------- -------- --- ------ ---------------- C 198.51.100.64/26 198.51.100.65 00:02:26 0 0 l3-vlan 101 L 198.51.100.65/32 0.0.0.0 00:02:26 0 0 DC S 198.51.100.99/32 0.0.0.0 00:00:48 1 0 black-hole-0 S 203.0.113.0/25 198.51.100.66 00:00:48 1 0 loose-next-hop

```text
# show ip rib destination 192.0.2.0/25
```

Routing entry for 192.0.2.0 (mask 255.255.255.128) Known via ’static’, distance 1, metric 0 Redistributing via static Last update from 0.0.0.0 00:00:02 ago Routing Descriptor Blocks: 0.0.0.0 directly connected, via black-hole-0 00:00:02 ago Route metric is 0

```text
#
```

**Output Terms:**

Output Description Indicates the type and the protocol that derived the route. The legType end codes are displayed at the beginning of each report. Indicates the destination IP address and mask of the remote network. Dest Address/Mask Next-hop Indicates the address of the next router to the remote network. Age Indicates the time period since this route was last updated. AD Indicates the administrative distance value of the route. Metric Indicates the routing metric value of the route. Indicates the output interface through which the specified network Output Interface can be reached. It may display black-hole-0 for routes that discard traffic.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip route`

> **Página:** 533 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display route information based on Forwarding Information Base (FIB).

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show ip route [bgp | connected | destination ip-address | ospf | static | summary | vrf name ]
```

**Parameters:**

- `bgp` — Displays route information filtering by BGP routes. — *Valores:* N/A · *Default:* N/A
- `connected` — Displays route information filtering by connected routes and local IP addresses. — *Valores:* N/A · *Default:* N/A
- `destination ip-address` — Displays route information filtering by exact match of destination IP address and mask. — *Valores:* a.b.c.d/x · *Default:* N/A
- `ospf` — Displays route information filtering by OSPF routes. — *Valores:* N/A · *Default:* N/A
- `static` — Displays route information filtering by static routes. — *Valores:* N/A · *Default:* N/A
- `summary` — Displays summary route information. — *Valores:* N/A · *Default:* N/A
- `vrf name` — Displays route information for VRF name. — *Valores:* Name of VRF. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.8 | The command output was improved. |
| 2.0 | The command was modified to have OSPF input/output. |
| 2.4 | The command was modified to have VRF. |
| 4.0 | The command was modified to have BGP filter. |
| 5.4 | Black-hole route support was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples show how to use the show ip route command.

```text
# show ip route
```

Type Codes: C - connected, S - static, L - local, O - OSPF, B - BGP E1 - OSPF external type 1, E2 - OSPF external type 2, IA - OSPF inter area, Output Interface Codes: DC - directly connected Type Dest Address/Mask Next-hop Age AD Metric Output Interface ------ ------------------- --------------- -------- --- ------ ---------------- S 192.0.2.0/25 0.0.0.0 00:46:42 1 0 black-hole-0 S 192.0.2.128/25 0.0.0.0 00:46:42 1 0 black-hole-0 S 198.51.100.0/26 198.51.100.66 00:46:42 1 0 mgmt-1/1/1 C 198.51.100.64/26 198.51.100.65 01:15:48 0 0 mgmt-1/1/1 L 198.51.100.65/32 0.0.0.0 01:15:48 0 0 DC C 198.51.100.128/26 198.51.100.129 00:05:48 0 0 l3-vlan 100 L 198.51.100.129/32 0.0.0.0 00:05:48 0 0 DC

```text
# show ip route vrf red
```

Type Codes: C - connected, S - static, L - local, O - OSPF, B - BGP E1 - OSPF external type 1, E2 - OSPF external type 2, IA - OSPF inter area, Output Interface Codes: DC - directly connected Type Dest Address/Mask Next-hop Age AD Metric Output Interface ------ ------------------- --------------- -------- --- ------ ---------------- C 198.51.100.64/26 198.51.100.65 00:02:26 0 0 l3-vlan 101 L 198.51.100.65/32 0.0.0.0 00:02:26 0 0 DC S 198.51.100.99/32 0.0.0.0 00:00:48 1 0 black-hole-0 S 203.0.113.0/25 203.0.113.200 00:00:48 1 0 l3-vlan 101

```text
# show ip route destination 192.0.2.0/25
```

Routing entry for 192.0.2.0 (mask 255.255.255.128) Known via ’static’, distance 1, metric 0 Redistributing via static Last update from 0.0.0.0 00:00:02 ago Routing Descriptor Blocks: 0.0.0.0 directly connected, via black-hole-0 00:00:02 ago Route metric is 0

```text
#
```

**Output Terms:**

Output Description Indicates the type and the protocol that derived the route. The legType end codes are displayed at the beginning of each report. Indicates the destination IP address and mask of the remote network. Dest Address/Mask Next-hop Indicates the address of the next router to the remote network. Age Indicates the time period since this route was last updated. AD Indicates the Administrative Distance value of the route. Metric Indicates the routing metric value of the route. Output Description Indicates the output interface through which the specified network Output Interface can be reached. It may display black-hole-0 for routes that discard traffic.

**Impacts and precautions:**

Right after switch initialization the route table will be empty, because it takes a while to be populated.

**Hardware restrictions:**

N/A


### `show ipv6 fib`

> **Página:** 537 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays IPv6 route information from Forwarding Information Base (FIB).

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
show ipv6 fib [ vrf { vrf-name | all } ] { brief } [ network ipv6-address | state route-state ]
```

**Parameters:**

- `vrf vrf-name` — Specifies the name of the VRF to filter displayed information. — *Valores:* Name of VRF to display information. · *Default:* N/A
- `brief` — Displays brief information about IPv6 routes from FIB. — *Valores:* N/A · *Default:* N/A
- `network ipv6-address` — IPv6 address and mask network used to filter the output. — *Valores:* x:x:x:x::x/y · *Default:* N/A
- `state route-state` — Route state used to filter the output. — *Valores:* active | inactive | installing | no ecmp resources | pending · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |
| 4.0 | Route state ‘inactive’ created. |
| 4.6 | Filter by VRF changed. |
| 5.4 | Black-hole route support was added. |
| 9.0 | Route state ‘installing’ created. |
| 9.8 | Route state ‘no ecmp resources’ created. |

**Usage Guidelines:**

To simply show IPv6 FIB information, the following command can be used: Example:

```text
# show ipv6 fib brief
```

VRF-name Network Next-hop Logical-interface State ------------------------------------------------------------------------------ global 2001:db8:aaaa::/48 2001:db8:c3af::1 l3-vlan 100 pending global 2001:db8:aaaa::/48 2001:db8:caaa::1 l3-vlan 101 pending global 2001:db8:bbbb::/48 2001:db8:bbbb::1 l3-vlan 200 active global 2001:db8:cccc::/48 2001:db8:a1f::1 l3-vlan 300 active global 2001:db8:dddd::/48 2001:db8:a1f3::1 l3-vlan 400 inactive global 2001:db8:eeee::/48 :: black-hole-0 active It is possible to filter the output by Network, State and VRF. Filter by Network: Example:

```text
# show ipv6 fib brief network 2001:db8:cccc::/48
```

VRF-name Network Next-hop Logical-interface State ------------------------------------------------------------------------------ global 2001:db8:cccc::/48 2001:db8:a1f::1 l3-vlan 300 active Filter by State: Example:

```text
# show ipv6 fib brief state active
```

VRF-name Network Next-hop Logical-interface State ------------------------------------------------------------------------------ global 2001:db8:bbbb::/48 2001:db8:bbbb::1 l3-vlan 200 active global 2001:db8:cccc::/48 2001:db8:a1f::1 l3-vlan 300 active Filter by VRF: Example:

```text
# show ipv6 fib vrf all brief
```

VRF-name Network Next-hop Logical-interface State ------------------------------------------------------------------------------ global 2001:db8:aaaa::/48 2001:db8:c3af::1 l3-vlan 100 pending global 2001:db8:bbbb::/48 2001:db8:bbbb::1 l3-vlan 200 active global 2001:db8:cccc::/48 2001:db8:a1f::1 l3-vlan 300 active global 2001:db8:dddd::/48 2001:db8:a1f3::1 l3-vlan 400 inactive

**Output Terms:**

Output Description VRF-name Display the VRF name associated with the IPv6 route. Display the destination IPv6 address and mask of the remote netNetwork work. Next-hop Display the IPv6 address of the next router to the remote network. Display the output logical interface to reach the remote network, or Logical-interface display black-hole-0 for routes that discard traffic. Display the route state. The active state represents installed routes; the inactive state represents unsupported routes that will not be installed; the installing state means that the route is waiting for nextState hop resolution; the no ecmp resources state points to the exhaustion of ECMP groups in hardware; and the pending state represents valid routes currently not installed due to a hardware limitation.

**Impacts and precautions:**

Depending on the number of routes installed, the execution of the command may take a while.

**Hardware restrictions:**

N/A


### `show ipv6 host-table`

> **Página:** 541 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows the list of IPv6 hosts present in the system.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show ipv6 host-table [ vrf { vrf-name | all } ] { brief } [ address ipv6-address | mac { mac-address | incomplete } | type host-type ]
```

**Parameters:**

- `vrf vrf-name` — Specifies the name of the VRF to filter displayed information. — *Valores:* Name of VRF to display information. · *Default:* N/A
- `brief` — Displays brief information about IPv6 hosts. — *Valores:* N/A · *Default:* N/A
- `address ipv6-address` — IPv6 address used to filter the output. — *Valores:* x:x:x:x::x/y · *Default:* N/A
- `mac mac-address` — MAC address used to filter the output. — *Valores:* XX:XX:XX:XX:XX:XX | incomplete · *Default:* N/A
- `type host-type` — Type of host to filter the output. — *Valores:* dynamic | local | static | unknown · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 4.4 | Added VRF-name column and filter by VRF. |

**Usage Guidelines:**

To simply show the list of hosts the following command can be used: Example:

```text
# show ipv6 host-table brief
```

To show the the list of hosts of all VRFs the following command can be used: Example:

```text
# show ipv6 host-table vrf all brief
```

To show the the list of hosts of an specific VRF the following command can be used: Example:

```text
# show ipv6 host-table vrf vrf-test brief
```

It is possible to filter the results by IPv6 address, MAC address, and Type. Filter by IPv6 address: Example:

```text
# show ipv6 host-table brief address 2001:db8::1
```

Filter by MAC: Example:

```text
# show ipv6 host-table brief mac 00:11:22:33:44:55
```

Filter by Type: Example:

```text
# show ipv6 host-table brief type local
```

**Output Terms:**

Output Description VRF-name Display the VRF name associated with the host. Address Display the IPv6 addresses associated with host. MAC Display the MAC addresses associated with host IPv6 addresses. Display the logical interface on which the respective host is associLogical interface ated. Physical interface Display the physical interface on which the respective host is associated. Type Display the type of the host entry.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ipv6 rib`

> **Página:** 545 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays IPv6 route information based on Routing Information Base (RIB).

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
show ipv6 rib [bgp | connected | destination ip-address | ospf | static | vrf vrf-name ]
```

**Parameters:**

- `bgp` — Displays route information filtering by BGP routes. — *Valores:* N/A · *Default:* N/A
- `connected` — Displays IPv6 route information filtering by connected routes and local IP addresses. — *Valores:* N/A · *Default:* N/A
- `destination ip-address` — Displays IPv6 route information filtering by exact match of destination IPv6 address and mask. — *Valores:* x:x:x:x::x/x · *Default:* N/A
- `ospf` — Displays route information filtering by OSPFv3 routes. — *Valores:* N/A · *Default:* N/A
- `static` — Displays IPv6 route information filtering by static routes — *Valores:* N/A · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF to filter displayed information. — *Valores:* Name of VRF to display information · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 4.0 | OSPF and BGP parameters were added. |
| 5.4 | Black-hole route support was added. |
| 5.12 | Introduced VRF support. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples show how to use the show ipv6 rib command.

```text
# show ipv6 rib
```

Type Codes: C - connected, S - static, L - local, O - OSPF, B - BGP E1 - OSPF external type 1, E2 - OSPF external type 2, IA - OSPF inter area, Output Interface Codes: DC - directly connected Type Dest Address/Mask Next-hop Age AD Metric Output Interface ------ --------------------- ----------------- -------- --- ------ ---------------- C 2001:db8:100::/64 2001:db8:100::1 00:11:45 0 0 l3-vlan 100 L 2001:db8:100::1/128 :: 00:11:45 0 0 DC S 2001:db8:2010::/64 :: 00:00:20 1 0 black-hole-0 C 2001:db8:2020::/64 2001:db8:2020::1 00:00:20 0 0 mgmt-1/1/1 L 2001:db8:2020::1/128 :: 00:00:20 0 0 DC S 2001:db8:2030::/64 2001:db8:2020::2 00:00:20 1 0 loose-next-hop

```text
# show ipv6 rib destination 2001:db8:2010::/64
```

Routing entry for 2001:db8:2010:: (mask 64) Known via ’static’, distance 1, metric 0 Redistributing via static Last update from :: 00:00:03 ago Routing Descriptor Blocks: :: directly connected, via black-hole-0 00:00:03 ago Route metric is 0

```text
# show ipv6 rib vrf green
```

Type Codes: C - connected, S - static, L - local, O - OSPF, B - BGP E1 - OSPF external type 1, E2 - OSPF external type 2, IA - OSPF inter area, Output Interface Codes: DC - directly connected Type Dest Address/Mask Next-hop Age AD Metric Output Interface ------ ------------------ --------- -------- --- ------ ---------------- C fd01::/16 fd01::1 00:04:16 0 0 l3-vlan 101 L fd01::1/128 :: 00:04:16 0 0 DC

```text
#
```

**Output Terms:**

Output Description Indicates the type and the protocol that derived the route. The legType end codes are displayed at the beginning of each report. Indicates the destination IPv6 address and mask of the remote netDest Address/Mask work. Next-hop Indicates the address of the next router to the remote network. Age Indicates the time period since this route was last updated. AD Indicates the Administrative Distance value of the route. Metric Indicates the routing metric value of the route. Indicates the output interface through which the specified network Output Interface can be reached. It may display black-hole-0 for routes that discard traffic.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ipv6 route`

> **Página:** 549 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays IPv6 route information based on Forwarding Information Base (FIB).

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show ipv6 route [bgp | connected | destination ip-address | ospf | static | summary | vrf vrf-name ]
```

**Parameters:**

- `bgp` — Displays route information filtering by BGP routes. — *Valores:* N/A · *Default:* N/A
- `connected` — Displays IPv6 route information filtering by connected routes and local IP addresses. — *Valores:* N/A · *Default:* N/A
- `destination ip-address` — Displays route information filtering by exact match of destination IPv6 address and mask. — *Valores:* x:x:x:x::x/x · *Default:* N/A
- `ospf` — Displays route information filtering by OSPFv3 routes. — *Valores:* N/A · *Default:* N/A
- `static` — Displays IPv6 route information filtering by static routes — *Valores:* N/A · *Default:* N/A
- `summary` — Displays summary IPv6 route information — *Valores:* N/A · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF to filter displayed information. — *Valores:* Name of VRF to display information · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 4.0 | OSPF and BGP parameters were added. |
| 5.4 | Black-hole route support was added. |
| 5.12 | Introduced VRF support. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples show how to use the show ipv6 route command.

```text
# show ipv6 route
```

Type Codes: C - connected, S - static, L - local, O - OSPF, B - BGP E1 - OSPF external type 1, E2 - OSPF external type 2, IA - OSPF inter area, Output Interface Codes: DC - directly connected Type Dest Address/Mask Next-hop Age AD Metric Output Interface ------ --------------------- ----------------- -------- --- ------ ---------------- C 2001:db8:100::/64 2001:db8:100::1 00:11:29 0 0 l3-vlan 100 L 2001:db8:100::1/128 :: 00:11:29 0 0 DC S 2001:db8:2010::/64 :: 00:00:03 1 0 black-hole-0 C 2001:db8:2020::/64 2001:db8:2020::1 00:00:03 0 0 mgmt-1/1/1 L 2001:db8:2020::1/128 :: 00:00:03 0 0 DC S 2001:db8:2030::/64 2001:db8:2020::2 00:00:04 1 0 mgmt-1/1/1

```text
# show ipv6 route summary
```

IPv6 routing table name is Default-IPv6-Routing-Table Family Total routes ipv6 6

```text
# show ipv6 route destination 2001:db8:2010::/64
```

Routing entry for 2001:db8:2010:: (mask 64) Known via ’static’, distance 1, metric 0 Redistributing via static Last update from :: 00:00:03 ago Routing Descriptor Blocks: :: directly connected, via black-hole-0 00:00:03 ago Route metric is 0

```text
# show ipv6 route vrf green
```

Type Codes: C - connected, S - static, L - local, O - OSPF, B - BGP E1 - OSPF external type 1, E2 - OSPF external type 2, IA - OSPF inter area, Output Interface Codes: DC - directly connected Type Dest Address/Mask Next-hop Age AD Metric Output Interface ------ ------------------ --------- -------- --- ------ ---------------- C fd01::/16 fd01::1 00:03:03 0 0 l3-vlan 101 L fd01::1/128 :: 00:03:04 0 0 DC

```text
#
```

**Output Terms:**

Output Description Indicates the type and the protocol that derived the route. The legType end codes are displayed at the beginning of each report. Indicates the destination IPv6 address and mask of the remote netDest Address/Mask work. Next-hop Indicates the address of the next router to the remote network. Age Indicates the time period since this route was last updated. AD Indicates the Administrative Distance value of the route. Metric Indicates the routing metric value of the route. Output Description Indicates the output interface through which the specified network Output Interface can be reached. It may display black-hole-0 for routes that discard traffic.

**Impacts and precautions:**

Right after switch initialization the route table will be empty, because it takes a while to be populated.

**Hardware restrictions:**

N/A BFD This topic describes the commands related to management of BFD such as commands to configure the BFD parameters or to inspect the sessions status.


## BFD

### `show bfd session`

> **Página:** 553 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about the BFD sessions.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show bfd session brief
```

**Parameters:**

- `brief` — Shows summarized information about BFD sessions. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show bfd session brief
```

Protocol Codes: O - OSPF Proto Local-address Remote-address Output interface State ----- ----------------- -------------- ---------------- -------- O 172.16.100.1 172.16.100.2 l3-vlan 100 up O 172.16.101.1 172.16.101.2 l3-vlan 101 down 2 BFD sessions found.

```text
#
```

**Output Terms:**

Output Description Proto Indicates the client protocol which is protected by this BFD session. Local-address Indicates the local address used in the monitored link. Output Description Remote-address Indicates the address of remote endpoint in the monitored link. Indicates the L3 interface used to communicate to the other endOutput interface point. State Indicates the state of monitored link (up or down).

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A BGP This topic describes the commands related to management of BGP topologies such as commands to configure the BGP parameters or to inspect the protocol status.


## BGP

### `clear bgp neighbor`

> **Página:** 556 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Restart BGP neighbors via Notification Cease message.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
clear bgp [vrf name] neighbor [ip IP address]
```

**Parameters:**

- `vrf name` — Specifies a VRF name (only in supported platforms). — *Valores:* Name of an existent VRF, global or all. · *Default:* N/A
- `ip IP address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 4.0 | Added support for IPv6. |
| 4.6 | Added VRF support. |
| 7.0 | Added support for IPv6 on VRF. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to restart a BGP neighbor from a BGP router specifying a neighbor ip address.

```text
# clear bgp neighbor ip 50.50.50.1
# clear bgp neighbor ip 2001:db8::1
```

This example shows how to restart all BGP neighbors from a BGP router.

```text
# clear bgp neighbor
```

If no VRF parameter is included, the action will be executed only for the BGP on the global VRF. The VRF parameter accepts a VRF name, the global VRF or all VRFs. This example shows how to restart all BGP neighbors on a specific VRF.

```text
# clear bgp vrf GREEN neighbor
```

It is also possible to specify a neighbor IP address on that VRF.

```text
# clear bgp vrf GREEN neighbor ip 50.50.50.1
# clear bgp vrf GREEN neighbor ip 2001:db8::1
```

To restart all BGP neighbors for all VRFs, the following command can be used.

```text
# clear bgp vrf all neighbor
```

**Impacts and precautions:**

This command will restart the connections to the neighbors.

**Hardware restrictions:**

N/A


### `clear bgp soft`

> **Página:** 559 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Performs soft reset in BGP sessions.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
clear bgp [vrf name] soft [ip IP address]
```

**Parameters:**

- `vrf name` — Specifies a VRF name (only in supported platforms). — *Valores:* Name of an existent VRF, global or all. · *Default:* N/A
- `ip IP address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 4.0 | Added support for IPv6. |
| 4.6 | Added VRF support. |
| 7.0 | Added support for IPv6 on VRF. |

**Usage Guidelines:**

This command can be executed directly via CLI. It requires route refresh capability in router BGP. Example: This example shows how to perform soft reset in a specific BGP neighbor.

```text
# clear bgp soft ip 50.50.50.1
# clear bgp soft ip 2001:db8::1
```

This example shows how to perform a soft reset in all BGP sessions.

```text
# clear bgp soft
```

If no VRF parameter is included, the action will be executed only for the BGP on the global VRF. The VRF parameter accepts a VRF name, the global VRF or all VRFs. This example shows how to soft restart all BGP sessions on a specific VRF.

```text
# clear bgp vrf GREEN soft
```

It is also possible to specify a neighbor IP address on that VRF.

```text
# clear bgp vrf GREEN soft ip 50.50.50.1
# clear bgp vrf GREEN soft ip 2001:db8::1
```

To soft restart all BGP sessions for all VRFs, the following command can be used.

```text
# clear bgp vrf all soft
```

**Impacts and precautions:**

For neighbors that do not support the route refresh capability a Cease Notification message will be sent instead causing BGP session to restart.

**Hardware restrictions:**

N/A


### `router bgp`

> **Página:** 562 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a BGP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a BGP router.

```text
(config)# router bgp 65000
(config-bgp-65000)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp address-family`

> **Página:** 564 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables the router BGP address family support.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number address-family { ipv4 | ipv6 } unicast
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `address-family { ipv4 | ipv6 }` — Selects the address family (AFI). — *Valores:* ipv4 or ipv6. IPv4 or IPv6 address family. · *Default:* N/A
- `unicast` — Selects the subsequent address family (SAFI). — *Valores:* unicast. IPv4 or IPv6 unicast routes. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. The disabling of a router BGP address family support is only possible if it is not configured in any BGP neighbor. Thus, the removal of all BGP neighbors address family configuration is required before disabling the address family on the router BGP. Example: This example shows how to enable the router BGP IPv4 unicast address family support.

```text
(config)# router bgp 65000
(config-bgp-65000)# address-family ipv4 unicast
(config-address-family-ipv4/unicast)# commit
```

Commit complete. This example shows how to enable the router BGP IPv6 unicast address family support.

```text
(config)# router bgp 65000
(config-bgp-65000)# address-family ipv6 unicast
(config-address-family-ipv6/unicast)# commit
```

Commit complete.

**Impacts and precautions:**

Changes on the address family will impact the router BGP capabilities. It also causes a flap in the established BGP sessions.

**Hardware restrictions:**

N/A


### `router bgp address-family`

> **Página:** 567 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables the router BGP VPNv4/VPNv6 address family support.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number address-family { vpnv4 | vpnv6 } unicast
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `address-family { vpnv4 | vpnv6 }` — Selects the address family (AFI). — *Valores:* vpnv4. VPNv4 address family. vpnv6. VPNv6 address family. · *Default:* N/A
- `unicast` — Selects the subsequent address family (SAFI). — *Valores:* unicast. VPNv4/VPNv6 unicast routes. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.0 | Added VPNv6 Address Family |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. The disabling of a router BGP address family support is only possible if it is not configured in any BGP neighbor. Thus, the removal of all BGP neighbors address family configuration is required before disabling the address family on the router BGP. Dual-stack can be enabled. Example: This example shows how to enable the router BGP VPNv4 unicast address family support.

```text
(config)# router bgp 65000
(config-bgp-65000)# address-family vpnv4 unicast
(config-address-family-vpnv4/unicast)# commit
```

Commit complete. Example: This example shows how to enable the router BGP VPNv6 unicast address family support.

```text
(config)# router bgp 65000
(config-bgp-65000)# address-family vpnv6 unicast
(config-address-family-vpnv6/unicast)# commit
```

Commit complete.

**Impacts and precautions:**

Changes on the address family will impact the router BGP capabilities. It also causes a flap in the established BGP sessions.

**Hardware restrictions:**

N/A


### `router bgp administrative-status`

> **Página:** 570 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status of a BGP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `administrative-status status` — Activate (up) or deactivate (down) the BGP router. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the administrative status.

```text
(config)# router bgp 65000 administrative-status down
(config-bgp-65000)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp as-size`

> **Página:** 572 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the Router BGP Autonomous system(AS) size.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number as-size length
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `as-size length` — Specifies the Router BGP Autonomous System(AS) size. — *Valores:* two-octets | four-octets. · *Default:* four-octets.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the Router BGP Autonomous system(AS) size.

```text
(config)# router bgp 65000 as-size two-octets
(config-bgp-65000)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp bgp cluster-id`

> **Página:** 574 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the Router Cluster-ID.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number bgp cluster-id id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `bgp cluster-id id` — Specifies the BGP Cluster-ID for this Router in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* 0.0.0.0.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the BGP Cluster-ID.

```text
(config)# router bgp 65000 bgp cluster-id 1.1.1.1
(config-bgp-65000)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp bgp default-local-preference`

> **Página:** 576 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the Router BGP Default Local Preference.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number bgp default-local-preference local-preference
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `bgp default-local-preference local-preference` — Specifies the default local preference for this Router. — *Valores:* 0-4294967295. · *Default:* 100.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the BGP default local preference.

```text
(config)# router bgp 65000 bgp default-local-preference 150
(config-bgp-65000)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor`

> **Página:** 578 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a neighbor for a BGP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a neighbor for a BGP router.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor address-family`

> **Página:** 580 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables the BGP neighbor address family support and enters in mode configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address address-family { ipv4 | ipv6 } unicast
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `address-family { ipv4 | ipv6 } unicast` — Enables the BGP neighbor address family mode support and enters in mode configuration. — *Valores:* ipv4 or ipv6 unicast. IPv4 or IPv6 address family. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. The enabling of a BGP neighbor address family support is only possible if it is already configured in router BGP. Example: This example shows how to enable the BGP neighbor IPv4 unicast address family support.

```text
(config)# router bgp 65000
(config-bgp-65000)# neighbor 1.1.10.2
(config-neighbor-1.1.10.2)# address-family ipv4 unicast
(config-address-family-ipv4/unicast)# commit
```

Commit complete. This example shows how to enable the BGP neighbor IPv6 unicast address family support.

```text
(config)# router bgp 65000
(config-bgp-65000)# neighbor 2222::2
(config-neighbor-2222::2)# address-family ipv6 unicast
(config-address-family-ipv6/unicast)# commit
```

Commit complete.

**Impacts and precautions:**

Changes on the address family will impact the BGP neighbor capabilities. It also causes a flap in the established BGP neighbor session.

**Hardware restrictions:**

N/A


### `router bgp neighbor address-family prefix-list`

> **Página:** 583 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Associates a prefix list with a BGP neighbor for export or import based on the address family.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address address-family ipv4 unicast [export-prefix-list prfx-name] [import-prefix-list prfx-name]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `address-family ipv4 unicast` — Enters in the BGP neighbor address family mode configuration. — *Valores:* ipv4 unicast. IPv4 unicast address family. · *Default:* N/A
- `export-prefix-list prfx-name` — Specifies the prefix list for export to be directly associated with the BGP neighbor. Use the no form to remove this parameter. — *Valores:* Name of a prefix list. · *Default:* N/A
- `import-prefix-list prfx-name` — Specifies the prefix list for import to be directly associated with the BGP neighbor. Use the no form to remove this parameter. — *Valores:* Name of a prefix list. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. Changes on the behavior when a prefix list and a route policy are associ3.0 ated with a neighbor. |

**Usage Guidelines:**

This command can be executed directly via CLI. Notice that a route policy associated with a neighbor have precedence over a prefix list directly associated with it. This command is only supported in IPv4 address family mode configuration. Example: This example shows how to associate the prefix list for export named PRX_LIST_EXPORT with a BGP neighbor. This prefix list must be previously created.

```text
(config)# router bgp 65000
(config-bgp-65000)# neighbor 1.1.10.2
(config-neighbor-1.1.10.2)# address-family ipv4 unicast
(config-address-family-ipv4/unicast)# export-prefix-list PRX_LIST_EXPORT
(config-address-family-ipv4/unicast)# commit
```

This example shows how to associate the prefix list for import named PRX_LIST_IMPORT with a BGP neighbor. This prefix list must be previously created.

```text
(config)# router bgp 65000
(config-bgp-65000)# neighbor 1.1.10.2
(config-neighbor-1.1.10.2)# address-family ipv4 unicast
(config-address-family-ipv4/unicast)# import-prefix-list PRX_LIST_IMPORT
(config-address-family-ipv4/unicast)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor address-family vpn`

> **Página:** 586 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables the BGP neighbor VPNv4/VPNv6 address family support and enters in mode configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address address-family { vpnv4 | vpnv6 } unicast
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 address format. — *Valores:* a.b.c.d · *Default:* N/A
- `address-family { vpnv4 | vpnv6 } unicast` — Enables the BGP neighbor address family mode support and enters in mode configuration. — *Valores:* vpnv4 unicast. VPNv4 unicast address family. vpnv6 unicast. VPNv6 unicast address family. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.0 | Added VPNv6 Address Family |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. The enabling of a BGP neighbor address family support is only possible if it is already configured in router BGP. IPv4 neighbors support both VPNv4 (L3VPN) and VPNv6 (6VPE) address families. IPv6 neighbors don’t support VPN address families. Dual-stack can be enabled. Example: This example shows how to enable the BGP neighbor VPNv4 unicast address family support.

```text
(config)# router bgp 65000
(config-bgp-65000)# neighbor 1.1.10.2
(config-neighbor-1.1.10.2)# address-family vpnv4 unicast
(config-address-family-vpnv4/unicast)# commit
```

Commit complete. This example shows how to enable the BGP neighbor VPNv6 unicast address family support.

```text
(config)# router bgp 65000
(config-bgp-65000)# neighbor 1.1.10.2
(config-neighbor-1.1.10.2)# address-family vpnv6 unicast
(config-address-family-vpnv6/unicast)# commit
```

Commit complete. This example shows how to enable dual-stack on BGP neighbor.

```text
(config)# router bgp 65000
(config-bgp-65000)# neighbor 1.1.10.2
(config-neighbor-1.1.10.2)# address-family vpnv4 unicast
(config-address-family-vpnv4/unicast)# address-family vpnv6 unicast
(config-address-family-vpnv6/unicast)# commit
```

Commit complete.

**Impacts and precautions:**

Changes on the address family will impact the BGP neighbor capabilities. It also causes a flap in the established BGP neighbor session.

**Hardware restrictions:**

N/A


### `router bgp neighbor administrative-status`

> **Página:** 589 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status of a BGP neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `administrative-status status` — Activate (up) or deactivate (down) the BGP neighbor. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the BGP neighbor administrative status in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# administrative-status down
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor description`

> **Página:** 592 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BGP neighbor description.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address description text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `description text` — A textual string containing information about the BGP neighbor. — *Valores:* string. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a BGP neighbor description in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# description "Remote bgp peer"
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor ebgp-multihop`

> **Página:** 595 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the maximum hop count to reach a BGP neighbor not directly connected.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address ebgp-multihop hop-count
```

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `ebgp-multihop hop-count` — Specifies the maximum hop count to reach the neighbor. — *Valores:* 1-255. · *Default:* 1 for eBGP sessions. 255 for iBGP sessions.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the BGP neighbor ebgp-multihop in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1 remote-as 66000
(config-neighbor-50.50.50.1)# ebgp-multihop 2
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

For security reasons, please note that this parameter is automatically configured to 1 for eBGP and 255 for iBGP sessions, unless it was manually configured. But if neighbor mode changes (to iBGP or eBGP) and ebgp-multihop has not been changed, it will be automatically updated according to the new mode.

**Hardware restrictions:**

N/A


### `router bgp neighbor enforce-first-as`

> **Página:** 598 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures whether the BGP neighbor should check the first AS number in the AS_PATH attribute in an UPDATE received from this peer to make sure it is the same as the AS number of the peer.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address enforce-first-as {enable | disable}
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `enforce-first-as` — Specifies the BGP neighbor should check the first AS number in the AS_PATH attribute. — *Valores:* enable | disable. · *Default:* enable

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to disable the check the first AS number in the AS_PATH attribute after entering in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# enforce-first-as disable
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

This configuration only applies to eBGP peers and only takes effect for a particular neighbor when the neighbor session is restarted. If modified with a neighbor session already stablished, it is necessary to set admin down followed by admin up for this neighbor.

**Hardware restrictions:**

N/A


### `router bgp neighbor maximum-prefix`

> **Página:** 601 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the limit number of prefixes that can be accepted from this BGP neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address maximum-prefix limit-number
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `limit-number` — Specifies the prefix limit number (totalled across all supported address families) accepted from this neighbor. Zero (0) represents no prefix limit. — *Valores:* 0-2147483647. · *Default:* 0 (no limit)

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 11.2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a BGP neighbor description in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# maximum-prefix 1024
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

Up to introduction of this command (DmOS version 11.2.0), each product model had a fixed non-configurable maximum-prefix limit. When upgrading DmOS from a version before the support of this command, the fixed limit will drop, and all configured BGP neighbors will be set to default (0 - no limit).

**Hardware restrictions:**

N/A


### `router bgp neighbor maximum-prefix-action`

> **Página:** 604 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the action to take when BGP neighbor prefixes reaches the configured limit number.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address maximum-prefix-action { drop | warn }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `action` — Specifies the BGP action when limit reaches. Setting drop will cause the BGP neighbor session to be dropped when the prefix limit is reached. If warn is set, a warning is generated when the maximum-prefix number is exceeded. — *Valores:* drop | warn · *Default:* warn

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 11.2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a BGP neighbor description in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# maximum-prefix-action drop
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

Up to the introduction of this command (11.2.0), each product model had a fixed, non-configurable maximum-prefix limit. When upgrading DmOS from a version before the support of this command, the fixed maximum-prefix will be overwritten to default (0).

**Hardware restrictions:**

N/A


### `router bgp neighbor next-hop-self`

> **Página:** 607 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BGP neighbor to use its own address as next hop in the advertised routes.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address next-hop-self
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `next-hop-self` — Enables the neighbor option to use itself as next-hop. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the BGP neighbor next hop self in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# next-hop-self
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor password`

> **Página:** 610 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the neighbor to use Message-Digest algorithm 5 (MD5) authentication on the TCP connection between BGP peers.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address password pwd
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `password pwd` — Specifies the BGP neighbor case-sensitive password to be used between the TCP peer connection. — *Valores:* string (length 2 - 80). · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. The same password must be applied for both BGP peers. Example: This example shows how to configure the BGP neighbor password in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# password pwdTest
(config-neighbor-50.50.50.1)# commit
```

This example shows the configuration of a neighbor password using an already encrypted password.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# password "hls:2922743918:337ZpL=Z"
(config-neighbor-50.50.50.1)# commit
```

This example shows the configuration of a neighbor password using special characters (i.e: " " , “?” , “!” , “;”). Please note that it is necessary to use double quotation marks in this case.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# password "pwd?test:2"
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

Password must be enclosed in double quotation marks if special characters were used (i.e: " " , “?” , “!” , “;”). Note that in an established BGP session if password is configured or changed the session will be restarted.

**Hardware restrictions:**

N/A


### `router bgp neighbor remote-as`

> **Página:** 613 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BGP neighbor remote Autonomous System(AS) number.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address remote-as as-number
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `remote-as as-number` — Specifies the BGP neighbor remote Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a neighbor remote Autonomous System(AS) number after entering in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# remote-as 65001
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor remove-private-as`

> **Página:** 616 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BGP neighbor private Autonomous System(AS) removal.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address remove-private-as action
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `remove-private-as action` — Specifies the BGP neighbor should remove private Autonomous System(AS) from the AS path. — *Valores:* remove | none | remove-all | replace | replace-all. · *Default:* remove

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the removal of private Autonomous System(AS) from the AS path after entering in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# remove-private-as remove
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor route-policy`

> **Página:** 618 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Associates a route policy with the BGP neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address route-policy rp-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `route-policy rp-name` — Specifies the route policy to be associated with the BGP neighbor. — *Valores:* Route policy name. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. It is only supported by IPv4 BGP neighbors. The route refresh capability in router BGP is required to avoid BGP sessions to be restarted. Example: This example shows how to associate the route policy named RP_INTERNET with a BGP neighbor. This route policy must be previously created.

```text
(config)# router bgp 101
(config-bgp-101)# neighbor 1.1.10.2
(config-neighbor-1.1.10.2)# route-policy RP_INTERNET
(config-neighbor-1.1.10.2)# commit
```

**Impacts and precautions:**

If there is no route refresh capability support any update on the route policy configuration that is associated with a BGP neighbor will cause its BGP session to be restarted.

**Hardware restrictions:**

N/A


### `router bgp neighbor route-reflector`

> **Página:** 621 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BGP route-reflector option.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address route-reflector option
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `route-reflector option` — Configure the route reflector options — *Valores:* client | non-client. · *Default:* non-client.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure route-reflector after entering in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# route-reflector client
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor timers hold-time`

> **Página:** 624 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the hold time interval for the session with the neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address timers hold-time time
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `timers hold-time time` — Specifies the hold time interval to use when negotiating a connection with the neighbor. — *Valores:* 3-65535. (0 for infinite hold time) · *Default:* 180.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. The hold time interval must be greater than or equal to the keepalive interval. Indeed, it is recommended that the hold time is 3 times the interval at which keepalive messages are sent. A zeroed value means an infinite time. If the hold time interval is set to zero, the keepalive interval must be set to zero as well. Example: This example shows how to configure the BGP neighbor hold time interval in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1 remote-as 66000
(config-neighbor-50.50.50.1)# timers hold-time 90
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor timers keepalive`

> **Página:** 627 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the keepalive interval for the session with the neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address timers keepalive time
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `timers keepalive time` — Specifies the keepalive interval to use when negotiating a connection with the neighbor. — *Valores:* 0-21845. · *Default:* 60.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. The keepalive interval must be lower than or equal to the hold-time interval. Indeed, it is recommended that the hold time is 3 times the interval at which keepalive messages are sent. A zeroed value for keepalive timer disables the sending of keepalive messages. In this case, the hold-time interval must be set to zero as well. The router automatically adjusts the effective keepalive timer based on the configured values, according to the following formula: keepalive = negotiated hold-time / truncate ( configured hold-time / configured keepalive ) As example, if the configured and negotiated hold-time are both 150 and keepalive is configured to 60: keepalive = 150 / truncate ( 150 / 60 ) keepalive = 150 / 2 keepalive = 75 Example: This example shows how to configure the BGP neighbor keepalive interval in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1 remote-as 66000
(config-neighbor-50.50.50.1)# timers keepalive 30
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp neighbor update-source-address`

> **Página:** 630 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BGP neighbor source address to be used during the session establishment.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number neighbor address update-source-address address
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `update-source-address address` — Specifies the BGP neighbor source address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the BGP neighbor IPv4 source address in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 50.50.50.1
(config-neighbor-50.50.50.1)# update-source-address 100.100.100.1
(config-neighbor-50.50.50.1)# commit
```

Commit complete. This example shows how to configure the BGP neighbor IPv6 source address in the neighbor command tree.

```text
(config)# router bgp 65000 neighbor 2222::2
(config-neighbor-2222::2)# update-source-address 2002::1
(config-neighbor-2222::2)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp network address-family ipv4`

> **Página:** 633 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Inserts a network present locally in the routing table into BGP domain and advertises it to the neighbor, when that network exactly matches a given prefix.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number network address-family ipv4 address a.b.c.d/x
```

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `network address-family ipv4` — Specifies that the network prefix entry is from IPv4 address family. — *Valores:* N/A · *Default:* N/A
- `address a.b.c.d/x` — Defines the network that must be matched in order to be inserted into BGP domain. — *Valores:* Must be a valid IPv4 prefix/mask. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to create a list of 2 network prefixes to be redistributed into BGP domain.

```text
(config)# router bgp 65000
(config-bgp-65000)# network address-family ipv4 address 40.40.40.240/28
(config-network/ipv4)# exit
(config-bgp-65000)# network address-family ipv4 address 80.80.128.0/17
(config-network/ipv4)# commit
```

**Impacts and precautions:**

The network inserted into BGP domain will have its path attribute origin set as IGP. The network will be advertised to the neighbors only if it is already present in the routing table. That means, there must be a route learned using local or connected networks, static routes, or a dynamic IGP such as OSPF.

**Hardware restrictions:**

N/A


### `router bgp network address-family ipv6`

> **Página:** 636 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Inserts a network present locally in the routing table into BGP domain and advertises it to the neighbor, when that network exactly matches a given prefix.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number network address-family ipv6 address x:x:x:x::x/y
```

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `network address-family ipv6` — Specifies that the network prefix entry is from IPv6 address family. — *Valores:* N/A · *Default:* N/A
- `address x:x:x:x::x/y` — Defines the network that must be matched in order to be inserted into BGP domain. — *Valores:* Must be a valid IPv6 prefix/mask. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to create a list of 2 network prefixes to be redistributed into BGP domain.

```text
(config)# router bgp 65000
(config-bgp-65000)# network address-family ipv6 address 1111::1/128
(config-network/ipv6)# exit
(config-bgp-65000)# network address-family ipv6 address 2222::2/128
(config-network/ipv6)# commit
```

**Impacts and precautions:**

The network inserted into BGP domain will have its path attribute origin set as IGP. The network will be advertised to the neighbors only if it is already present in the routing table. That means, there must be a route learned using local or connected networks, static routes, or a dynamic IGP such as OSPF.

**Hardware restrictions:**

N/A


### `router bgp prefix-list`

> **Página:** 639 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Prefix list configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number prefix-list name seq seq-number [ permit | deny ] address-family ipv4 unicast [ address prefix ] [ le prefix-len ] [ ge prefix-len]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `prefix-list name` — Creates a prefix list with the given name. — *Valores:* N/A · *Default:* N/A
- `seq seq-number` — Apply the sequence number to the prefix list entry. — *Valores:* 1-4294967295. · *Default:* N/A
- `permit` — In case of match the route is allowed to be redistributed. The permit keyword is the default option. — *Valores:* N/A · *Default:* permit.
- `deny` — In case of match the route is rejected and no further processing is performed. — *Valores:* N/A · *Default:* permit.
- `address-family ipv4 unicast` — Unicast IPv4 address family configuration. — *Valores:* N/A · *Default:* N/A
- `address prefix` — A unicast IPv4 prefix in A.B.C.D/length format. — *Valores:* a.b.c.d/x. · *Default:* 0.0.0.0/0.
- `le prefix-len` — The maximum prefix length to match. — *Valores:* 1-32. · *Default:* N/A
- `ge prefix-len` — The minimum prefix length to match. — *Valores:* 1-32. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 2.2 | Added the optional parameters deny and permit. Changes on the behavior when a prefix list and a route policy are associ3.0 ated with a neighbor. This Command was deprecated. From this version on, the prefix list is |
| 4.6 | configured in the config level. For further information please see Prefix List command. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a prefix list that permits the network address 50.50.50.0/24.

```text
(config)# router bgp 101
(config-bgp-101)# prefix-list TEST
(config-prefix-list-TEST)# seq 10
(config-seq-10)# address-family ipv4 unicast
(config-unicast)# address 50.50.50.0/24
(config-unicast)# commit
```

Commit complete. This example shows how to configure a prefix list with a permitted prefix range from subnetwork 60.60.60.0/25 to network 60.60.60.0/24.

```text
(config)# router bgp 101
(config-bgp-101)# prefix-list TEST_RANGE
(config-prefix-list-TEST_RANGE)# seq 20
(config-seq-20)# address-family ipv4 unicast
(config-unicast)# address 60.60.60.0/24 ge 24 le 25
(config-unicast)# commit
```

Commit complete. This example shows how to configure a prefix list that denies the network address 60.60.60.0/24 but allows the others.

```text
(config)# router bgp 101
(config-bgp-101)# prefix-list TEST_DENY
(config-prefix-list-TEST_DENY)# seq 20
(config-seq-20)# deny
(config-seq-20)# address-family ipv4 unicast
(config-unicast)# address 60.60.60.0/24
(config-unicast)# exit
(config-seq-20)# exit
(config-prefix-list-TEST_DENY)# seq 30
(config-seq-30)# address-family ipv4 unicast
(config-unicast)# address 0.0.0.0/0 ge 1 le 32
(config-unicast)# commit
```

Commit complete.

**Impacts and precautions:**

When the prefix list is associated with a route map the permit or deny configuration of the prefix list entry is ignored. In case of prefix list directly associated with a BGP neighbor and no permit matches are found, all routes will be denied. Therefore, it is necessary to add an additional sequence with a clause to permit the other routes by setting a matching all address (0.0.0.0/0 ge 1 le 32). Notice that when there is a route policy importing a route map associated with a neighbor the prefix list for import directly associated with it will be ignored. The same precedence applies to the case when both are set for export. If there is no route refresh capability support any update on the prefix list configuration that is associated with a BGP neighbor will cause its BGP session to be restarted. Updates on prefix-lists associated with a neighbor or with a route map will trigger either route-refresh or update messages. Route-refresh messages request to the neighbor the sending of all its prefixes. Differently from a route-refresh message the sending of update messages is an optimization because only the prefixes not included on the previous BGP update will be advertised.

**Hardware restrictions:**

N/A


### `router bgp redistribute`

> **Página:** 644 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Redistributes routes into the domain of this BGP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number redistribute {connected | static | ospf} address-family { ipv4 | ipv6 }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `redistribute connected` — Redistributes connected routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `redistribute static` — Redistributes static routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `redistribute ospf` — Redistributes ospf routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `address-family ipv4` — Redistributes only routes from IPv4 address family. — *Valores:* N/A · *Default:* N/A
- `address-family ipv6` — Redistributes only routes from IPv6 address family. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a redistribution of all IPv4 static routes.

```text
# router bgp 65000 redistribute static address-family ipv4
(config-redistribute-static/ipv4)# commit
```

This example shows how to configure a redistribution of all IPv4 connected routes.

```text
# router bgp 65000 redistribute connected address-family ipv4
(config-redistribute-connected/ipv4)# commit
```

This example shows how to configure a redistribution of all IPv4 ospf routes.

```text
# router bgp 65000 redistribute ospf address-family ipv4
(config-redistribute-ospf/ipv4)# commit
```

This example shows how to configure a redistribution of all IPv6 static routes.

```text
# router bgp 65000 redistribute static address-family ipv6
(config-redistribute-static/ipv6)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp redistribute administrative-status`

> **Página:** 647 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status of a redistribution rule.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number redistribute {connected | static | ospf} address-family {ipv4 | ipv6} administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `redistribute connected` — Redistributes connected routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `redistribute static` — Redistributes static routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `redistribute ospf` — Redistributes ospf routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `address-family ipv4` — Redistributes only routes from IPv4 address family. — *Valores:* N/A · *Default:* N/A
- `address-family ipv6` — Redistributes only routes from IPv6 address family. — *Valores:* N/A · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the BGP router redistribution. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to disable IPv4 static routes redistribution.

```text
# router bgp 65000 redistribute static address-family ipv4
(config-redistribute-static/ipv4)# administrative-status down
(config-redistribute-static/ipv4)# commit
```

This example shows how to disable IPv6 static routes redistribution.

```text
# router bgp 65000 redistribute static address-family ipv6
(config-redistribute-static/ipv6)# administrative-status down
(config-redistribute-static/ipv6)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp redistribute match-address address-family ipv4`

> **Página:** 650 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Redistributes only the routes that match the specified address into the domain of this BGP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number redistribute {connected | static} address-family ipv4 match-address a.b.c.d/x
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `redistribute connected` — Redistributes connected routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `redistribute static` — Redistributes static routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `address-family ipv4` — Redistributes only routes from IPv4 address family. — *Valores:* N/A · *Default:* N/A
- `match-address a.b.c.d/x` — Redistributes specific routes that match the supplied prefix/mask filter into the domain of this BGP router. — *Valores:* Must be a valid IPv4 prefix/mask. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a route redistribution which matches a single IPv4 address prefix.

```text
# router bgp 65000 redistribute static address-family ipv4
(config-redistribute-static/ipv4)# match-address 10.1.0.0/24
(config-redistribute-static/ipv4)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp redistribute match-address address-family ipv6`

> **Página:** 653 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Redistributes only the routes that match the specified address into the domain of this BGP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number redistribute {connected | static} address-family ipv6 match-address x:x:x:x::x/y
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `redistribute connected` — Redistributes connected routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `redistribute static` — Redistributes static routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `address-family ipv6` — Redistributes only routes from IPv6 address family. — *Valores:* N/A · *Default:* N/A
- `match-address x:x:x:x::x/y` — Redistributes specific routes that match the supplied prefix/mask filter into the domain of this BGP router. — *Valores:* Must be a valid IPv6 prefix/mask. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a route redistribution which matches a single IPv6 address prefix.

```text
# router bgp 65000 redistribute static address-family ipv6
(config-redistribute-static/ipv6)# match-address 2001::1/128
(config-redistribute-static/ipv6)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp route-map`

> **Página:** 656 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Route map configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number route-map rmap-name { seq-number | * } action { permit | deny } { match-ip nlri prefix-list prfx-name | match-as-path as-path | match-med med | match-origin origin | set-local-preference value | set-med med | set-origin origin | set-prepend-local-as num-times | continue seq-number}
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `route-map rmap-name` — Creates a route map with the given rmap-name. — *Valores:* N/A · *Default:* N/A
- `seq-number` — Applies the sequence number to the route map entry. — *Valores:* 1-4294967295. · *Default:* N/A
- `∗` — A reference for all route map sequences. This option allows edition or deletion of all route map sequences simultaneously. — *Valores:* N/A · *Default:* N/A
- `action` — When action permit is used in case of match of any criteria the route is allowed to be redistributed and the set of actions is performed. When action deny is used in case of match of any criteria the route is rejected and no further processing is performed. — *Valores:* permit - deny. · *Default:* permit.
- `match-ip nlri prefix-list prfx-name` — Matches IP addresses present on BGP NLRI based on an existent prefix list named as prfx-name. — *Valores:* Name of a prefix list. · *Default:* N/A
- `match-as-path as-path` — Regular expression to match BGP AS paths (write regex using POSIX extended standard ensuring the use of double quote in order to avoid problems with special characters) — *Valores:* string (length 1 - 127). · *Default:* N/A
- `match-med med` — Matches BGP Multi Exit Discriminator (MED). — *Valores:* 0-4294967295. · *Default:* N/A
- `match-origin origin` — Matches BGP origin. — *Valores:* egp, igp or incomplete. · *Default:* N/A
- `set-local-preference value` — Sets the BGP local preference path attribute. — *Valores:* 0-2147483647. · *Default:* N/A
- `set-med med` — Sets the BGP Multi Exit Discriminator (MED). — *Valores:* 0-4294967295. · *Default:* 0.
- `set-origin origin` — Sets the BGP origin. — *Valores:* egp, igp or incomplete. · *Default:* N/A
- `set-prepend-local-as num-times` — Prepends the AS number to the AS path the number of times specified by num-times. — *Valores:* 1-254. · *Default:* N/A
- `continue seq-number` — Continues the route map on a different sequence number. The sequence number must exist and be higher than the current one. The continue parameter can only be used with permit sequences of route map. — *Valores:* 1-4294967295. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. Added match-as-path option. Added range mode to edit or delete all 2.2 route map sequences. |
| 4.6 | Added action parameter to configure permit or deny actions. |

**Usage Guidelines:**

This command can be executed directly via CLI. The route map must be associated with a route policy in order to be applied to a neighbor. The route refresh capability in router BGP is required to avoid BGP sessions to be restarted. Example: This example shows how to configure a route map with matching for a prefix list and setting of local preference.

```text
(config)# router bgp 101
(config-bgp-101)# route-map RMAP 10
(config-route-map-RMAP/10)# match-ip nlri prefix-list PRX_LIST
(config-route-map-RMAP/10)# set-local-preference 200
(config-route-map-RMAP/10)# commit
```

This example shows how to configure all sequences of a route map simultaneously to perform a deny action.

```text
(config)# router bgp 101
(config-bgp-101)# route-map RMAP 10
(config-route-map-RMAP/10)# exit
(config-bgp-101)# route-map RMAP 20
(config-route-map-RMAP/20)# exit
(config-bgp-101)# route-map RMAP *
(config-route-map-RMAP/*)# action deny
(config-route-map-RMAP/*)# commit
```

This example shows how to delete the entire route map.

```text
(config)# router bgp 101
(config-bgp-101)# route-map RMAP 10
(config-route-map-RMAP/10)# exit
(config-bgp-101)# route-map RMAP 20
(config-route-map-RMAP/20)# exit
(config-bgp-101)# no route-map RMAP *
(config-bgp-101)# commit
```

Some examples of regular expressions to be used in match-as-path parameter: Second AS number should be 300 or 400

```text
(config-route-map-RMAP/10)# match-as-path ".(300|400)" or "(.300)|(.400)"
```

Specific sequence (all three values should appear in this exact order)

```text
(config-route-map-RMAP/10)# match-as-path "333.100.444"
```

Path must contain AS 400 or AS 200

```text
(config-route-map-RMAP/10)# match-as-path "400|200"
```

Path must start with 333 and finish with 300

```text
(config-route-map-RMAP/10)# match-as-path "^333.300$"
```

Path must not end with 333

```text
(config-route-map-RMAP/10)# match-as-path "[^3]33$"
```

Path must not start with 333

```text
(config-route-map-RMAP/10)# match-as-path "^[^3]33"
```

Path does not contain 333 (see impacts and precautions for more details about deny rules)

```text
(config-route-map-RMAP/10)# match-as-path "(333)"
(config-route-map-RMAP/10)# action deny
(config-route-map-RMAP/10)# exit
(config-bgp-101)# route-map RMAP 20
(config-route-map-RMAP/20)# commit
```

**Impacts and precautions:**

When a route map is not specified, routes are automatically permitted by default. However, if a route map is created but no matching clauses are found, all routes will be denied. In this case it is necessary to add an additional sequence without any clause in order to permit all other routes. If there is no route refresh capability support any update on the route map configuration that is associated with a BGP neighbor will cause its BGP session to be restarted. Updates on route map associated with a neighbor through a route policy will trigger either route-refresh or update messages. Route-refresh messages request to the neighbor the sending of all its prefixes. Differently from a route-refresh message the sending of update messages is an optimization because only the prefixes not included on the previous BGP update will be advertised.

**Hardware restrictions:**

N/A


### `router bgp route-map match-community`

> **Página:** 662 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Match community configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number route-map rmap-name { seq-number | * } match-community communities
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System (AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `route-map rmap-name` — Creates a route map with the given rmap-name. — *Valores:* N/A · *Default:* N/A
- `seq-number` — Applies the sequence number to the route map entry. — *Valores:* 1-4294967295. · *Default:* N/A
- `∗` — A reference for all route map sequences. This option allows edition or deletion of all route map sequences simultaneously. — *Valores:* N/A · *Default:* N/A
- `match-community communities` — Sets the regular expression for matching communities. — *Valores:* String (length 1 - 127). · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a match for communities.

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# match-community 200:123
(config-route-map-RMAP/10)# route-map RMAP 11
(config-route-map-RMAP/11)# match-community "[65535:65281|65535:65282]"
(config-route-map-RMAP/11)# route-map RMAP 12
(config-route-map-RMAP/12)# match-community "65535:6528.*"
(config-route-map-RMAP/12)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp route-map match-extended-community`

> **Página:** 665 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Match extended community configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number route-map rmap-name { seq-number | * } match-extendedcommunity communities
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System (AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `route-map rmap-name` — Creates a route map with the given rmap-name. — *Valores:* N/A · *Default:* N/A
- `seq-number` — Applies the sequence number to the route map entry. — *Valores:* 1-4294967295. · *Default:* N/A
- `∗` — A reference for all route map sequences. This option allows edition or deletion of all route map sequences simultaneously. — *Valores:* N/A · *Default:* N/A
- `match-extended-community communities` — Sets the regular expression for matching extended communities. — *Valores:* String (length 1 - 127). · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 12.0.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: When a route is received through BGP, it can carry multiple extended communities. The list of received extended communities will be converted into a string list separated by comma, and match-extended-community regex will try to match this string list. An example of this string list of communities: “target:200:10,target:192.168.101.20:6553,origin:2200:11”. The examples below shows how to configure a regex match. Matches any community that contains the string “200:1”, this regex can match any other community that contains this substring, such as “1200:14”:

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# match-extended-community "200:1"
(config-route-map-RMAP/10)# commit
```

Matches a community thats has the exactly “200:1”:

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# match-extended-community "\\b200:1\\b"
(config-route-map-RMAP/10)# commit
```

Matches a community thats has the exactly “200:1” and subtype origin:

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# match-extended-community "origin:200:1\\b"
(config-route-map-RMAP/10)# commit
```

Matches a community thats has the exactly AS IP “192.168.101.20”:

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# match-extended-community "192.168.101.20\\b"
(config-route-map-RMAP/10)# commit
```

Matches a community list that contains a list of two communities:

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# match-extended-community "target:200:123,origin:4369:272\\b"
(config-route-map-RMAP/10)# commit
```

Matches a community list that contains regex for community number ‘200:1’ or ‘200:2’:

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# match-extended-community "\\b200:[1|2]\\b"
(config-route-map-RMAP/10)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp route-map set-community`

> **Página:** 668 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Set community configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number route-map rmap-name { seq-number | * } set-community { community | internet | local-AS | no-advertise | no-export }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System (AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `route-map rmap-name` — Creates a route map with the given rmap-name. — *Valores:* N/A · *Default:* N/A
- `seq-number` — Applies the sequence number to the route map entry. — *Valores:* 1-4294967295. · *Default:* N/A
- `∗` — A reference for all route map sequences. This option allows edition or deletion of all route map sequences simultaneously. — *Valores:* N/A · *Default:* N/A
- `set-community { community | internet | local-AS | no-advertise | no-export }` — Sets the community attribute. The DmOS user can enter either a single community or a list of communities, separated by spaces. A single route map can include up to 32 communities. — *Valores:* Well-known community or specific community in AS:nn format. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. Previous versions only allowed users to enter one community per route |
| 11.2.0 | map. With version 11.2.0 , DmOS users were given the option to enter a list of communities. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a community for prefixes.

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# set-community 100:123
(config-route-map-RMAP/10)# commit
```

Example: This example shows how to configure multiple communities to a route map.

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# set-community 100:124 100:344 100:556 100:834
(config-route-map-RMAP/10)# commit
```

Example: This example shows how to remove multiple communities from a route map.

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# no set-community 100:123 100:344
(config-route-map-RMAP/10)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp route-map set-community-action`

> **Página:** 671 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Set action to be applied to route communities

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number route-map rmap-name { seq-number | * } set-communityaction { none | remove-all | remove-all-and-set | remove-specific | set-specific }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System (AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `route-map rmap-name` — Creates a route map with the given rmap-name. — *Valores:* N/A · *Default:* N/A
- `seq-number` — Applies the sequence number to the route map entry. — *Valores:* 1-4294967295. · *Default:* N/A
- `∗` — A reference for all route map sequences. This option allows edition or deletion of all route map sequences simultaneously. — *Valores:* N/A · *Default:* N/A
- `set-community-action { none | remove-all | remove-all-and-set | remove-specific | set-specific}` — Possible actions to be applied to route communities. Actions remove-all-and-set, remove-specific and set-specific must have set-community attribute configured. Action none has the same effect as no set-communityaction. — *Valores:* none | remove-all | remove-all-and-set | remove-specific | set-specific · *Default:* none.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a community action for prefixes.

```text
(config)# router bgp 100
(config-bgp-100)# route-map RMAP 10
(config-route-map-RMAP/10)# set-community 100:123
(config-route-map-RMAP/10)# set-community-action remove-all-and-set
(config-route-map-RMAP/10)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp route-policy`

> **Página:** 674 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Route policy configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number route-policy rp-name [ import-route-map rmap-name ] [ export-route-map rmap-name ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `route-policy rp-name` — Creates a route-policy named rp-name. — *Valores:* String · *Default:* N/A
- `import-route-map rmap-name` — Specifies the route map that will be used for route imports. — *Valores:* String · *Default:* N/A
- `export-route-map rmap-name` — Specifies the route map that will be used for route exports. — *Valores:* String · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. Added action parameter to configure permit or deny actions in the com4.6 mand route-map. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how create a policy to export a Route Map.

```text
(config-bgp-101)# route-map rm-route50 10
(config-route-map-rm-route50/10)# action permit
(config-bgp-101)# route-policy rp-route50
(config-route-policy-rp-route50)# export-route-map rm-route50
(config-route-policy-rp-route50)# commit
```

Commit complete.

```text
(config-route-policy-rp-route50)#
```

**Impacts and precautions:**

If there is no route refresh capability support any update on the route policy configuration that is associated with a BGP neighbor will cause its BGP session to be restarted. Updates on route policy associated with a neighbor will trigger either route-refresh or update messages. Route-refresh messages request to the neighbor the sending of all its prefixes. Differently from a route-refresh message the sending of update messages is an optimization because only the prefixes not included on the previous BGP update will be advertised.

**Hardware restrictions:**

N/A


### `router bgp router-id`

> **Página:** 677 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the router identifier of a BGP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number router-id id
```

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `router-id id` — Specifies the Router BGP identifier expressed in IPv4 address format. The value 0.0.0.0 and addresses in range 224.0.0.0 - 247.255.255.255 cannot be used as id. — *Valores:* a.b.c.d. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the router-id of a BGP router.

```text
(config)# router bgp 65000 router-id 1.1.1.1
(config-bgp-65000)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf`

> **Página:** 679 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Associates a VRF with router BGP.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. The VRF must be previously created. Example: This example shows how to associate a VRF with the router BGP.

```text
(config)# router bgp 65000 vrf example
(config-vrf-example)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf address-family`

> **Página:** 681 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables the router BGP address family support per VRF.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name address-family { ipv4 | ipv6 } unicast
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `address-family { ipv4 | ipv6 }` — Selects the address family (AFI). — *Valores:* ipv4 or ipv6. IPv4 or IPv6 address family. · *Default:* N/A
- `unicast` — Selects the subsequent address family (SAFI). — *Valores:* unicast. IPv4 or IPv6 unicast routes. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. The disabling of a router BGP address family support is only possible if it is not configured in any BGP neighbor. Thus, the removal of all BGP neighbors address family configuration is required before disabling the address family on the router BGP. Example: This example shows how to enable the router BGP IPv4 unicast address family support.

```text
(config)# router bgp 65000 vrf red
(config-bgp-vrf)# address-family ipv4 unicast
(config-bgp-vrf-address-family-ipv4/unicast)# commit
```

Commit complete.

**Impacts and precautions:**

Changes on the address family will impact the router BGP capabilities. It also causes a flap in the established BGP sessions.

**Hardware restrictions:**

N/A


### `router bgp vrf address-family network`

> **Página:** 684 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Inserts a network present locally in the routing table into BGP VRF domain and advertises it to the neighbor, when that network exactly matches a given prefix.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name address-family { ipv4 | ipv6 } unicast network ip-prefix
```

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `address-family { ipv4 | ipv6 }` — Selects the address family (AFI). — *Valores:* ipv4 or ipv6. IPv4 or IPv6 address family. · *Default:* N/A
- `unicast` — Selects the subsequent address family (SAFI). — *Valores:* unicast. IPv4 or IPv6 unicast routes. · *Default:* N/A
- `network ip-prefix` — Defines the network that must be matched in order to be inserted into BGP domain. — *Valores:* Must be a valid IPv4 or IPv6 prefix/mask. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example shows how to create a list of 2 network prefixes to be redistributed into BGP domain in a VRF.

```text
(config)# router bgp 65000
(config-bgp-65000)# vrf red
(config-bgp-vrf-red)# address-family ipv4 unicast
(config-bgp-vrf-address-family-ipv4/unicast)# network 40.40.40.240/28
(config-network-40.40.40.240/28)# top
(config)# router bgp 65000 vrf red address-family ipv4 unicast network 80.80.128.0/17
(config-network-80.80.128.0/17)# commit
```

**Impacts and precautions:**

The network inserted into BGP domain will have its path attribute origin set as IGP. The network will be advertised to the neighbors only if it is already present in the VRF routing table. That means, there must be a route learned using local or connected networks or static routes.

**Hardware restrictions:**

N/A


### `router bgp vrf address-family redistribute match-address`

> **Página:** 687 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Redistributes only the routes from VRF that match the specified address into the domain of this BGP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name address-family { ipv4 | ipv6 } unicast redistribute {connected | static} match-address ip-prefix
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `address-family { ipv4 | ipv6 }` — Selects the address family (AFI). — *Valores:* ipv4 or ipv6. IPv4 or IPv6 address family. · *Default:* N/A
- `unicast` — Selects the subsequent address family (SAFI). — *Valores:* unicast. IPv4 or IPv6 unicast routes. · *Default:* N/A
- `redistribute connected` — Redistributes VRF connected routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `redistribute static` — Redistributes VRF static routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `match-address ip-prefix` — Redistributes specific routes that match the supplied prefix/mask filter into the domain of this BGP router. — *Valores:* Must be a valid IPv4 or IPv6 prefix/mask. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example shows how to configure redistribution of IPv4 connected routes from VRF example which matches a single IPv4 address prefix.

```text
# router bgp 65000 vrf example address-family ipv4 unicast redistribute connected
(config-bgp-vrf-address-family-redist-connected)# match-address 10.1.0.0/24
(config-bgp-vrf-address-family-redist-connected)# commit
```

This example shows how to configure redistribution of IPv4 static routes from VRF example which matches a single IPv4 address prefix.

```text
# router bgp 65000 vrf example address-family ipv4 unicast redistribute static
(config-bgp-vrf-address-family-redist-static)# match-address 10.1.0.0/24
(config-bgp-vrf-address-family-redist-static)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf address-family { ipv4 | ipv6 } unicast redistribute`

> **Página:** 690 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Redistributes routes from the VRF into the domain of this BGP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name address-family { ipv4 | ipv6 } unicast redistribute {connected | ospf | static}
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `address-family { ipv4 | ipv6 } unicast` — Redistributes unicast routes from IPv4 and/or IPv6 address family. Dual stack can be enabled. — *Valores:* N/A · *Default:* N/A
- `redistribute connected` — Redistributes VRF connected routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `redistribute ospf` — Redistributes VRF OSPF routes into the domain of this BGP router. OSPF is onnly valid for IPv4 address-families. — *Valores:* N/A · *Default:* N/A
- `redistribute static` — Redistributes VRF static routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |
| 5.0 | Support for redistribute OSPF. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example shows how to configure a redistribution of all IPv4 connected routes from VRF example.

```text
# router bgp 65000 vrf example address-family ipv4 unicast redistribute connected
(config-bgp-vrf-address-family-redist-connected)# commit
```

This example shows how to configure a redistribution of all IPv6 connected routes from VRF example.

```text
# router bgp 65000 vrf example address-family ipv6 unicast redistribute connected
(config-bgp-vrf-address-family-redist-connected)# commit
```

This example shows how to configure a redistribution of all OSPF routes from VRF example.

```text
# router bgp 65000 vrf example address-family ipv4 unicast redistribute ospf
(config-bgp-vrf-address-family-redist-ospf)# commit
```

This example shows how to configure a redistribution of all IPv4 static routes from VRF example.

```text
# router bgp 65000 vrf example address-family ipv4 unicast redistribute static
(config-bgp-vrf-address-family-redist-static)# commit
```

This example shows how to configure a redistribution of dual stack connected routes from VRF example.

```text
# router bgp 65000 vrf example address-family ipv4 unicast redistribute connected
# router bgp 65000 vrf example address-family ipv6 unicast redistribute connected
(config-bgp-vrf-address-family-redist-connected)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf address-family { ipv4 | ipv6 } unicast redistribute administrative-status`

> **Página:** 694 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the administrative status of a redistribution rule.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name address-family { ipv4|ipv6 } unicast redistribute {connected | static } administrative-status { up | down }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `address-family { ipv4 | ipv6 } unicast` — Redistributes only unicast routes from IPv4/IPv6 address family. — *Valores:* N/A · *Default:* N/A
- `redistribute connected` — Redistributes VRF connected routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `redistribute static` — Redistributes VRF static routes into the domain of this BGP router. — *Valores:* N/A · *Default:* N/A
- `administrative-status { up | down }` — Activates (up) or deactivates (down) the BGP router redistribution. — *Valores:* up or down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example shows how to deactivate the redistribution of IPv4 connected routes from VRF example.

```text
# router bgp 65000 vrf example address-family ipv4 unicast redistribute connected
(config-bgp-vrf-address-family-redist-static)# administrative-status down
(config-bgp-vrf-address-family-redist-static)# commit
```

This example shows how to deactivate the redistribution of IPv4 static routes from VRF example.

```text
# router bgp 65000 vrf example address-family ipv4 unicast redistribute static
(config-bgp-vrf-address-family-redist-static)# administrative-status down
(config-bgp-vrf-address-family-redist-static)# commit
```

This example shows how to deactivate the redistribution of IPv6 connected routes from VRF example.

```text
# router bgp 65000 vrf example address-family ipv6 unicast redistribute connected
(config-bgp-vrf-address-family-redist-static)# administrative-status down
(config-bgp-vrf-address-family-redist-static)# commit
```

This example shows how to deactivate the redistribution of IPv6 static routes from VRF example.

```text
# router bgp 65000 vrf example address-family ipv6 unicast redistribute static
(config-bgp-vrf-address-family-redist-static)# administrative-status down
(config-bgp-vrf-address-family-redist-static)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor`

> **Página:** 697 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a neighbor for a BGP VRF router.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example shows how to configure a neighbor for a BGP VRF router.

```text
(config)# router bgp 65000
(config-bgp-65000)# vrf red
(config-bgp-vrf-red)# neighbor 50.50.50.1
(config-bgp-vrf-neighbor-50.50.50.1)# remote-as 65000
(config-bgp-vrf-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor address-family`

> **Página:** 700 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables the BGP VRF neighbor address family support and enters in mode configuration.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address address-family { ipv4 | ipv6 } unicast
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `neighbor address` — Specifies the BGP VRF neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `address-family { ipv4 | ipv6 }` — Selects the address family (AFI). — *Valores:* ipv4 or ipv6. IPv4 or IPv6 address family. · *Default:* N/A
- `unicast` — Selects the subsequent address family (SAFI). — *Valores:* unicast. IPv4 or IPv6 unicast routes. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. The enabling of a BGP VRF neighbor address family support is only possible if it is already configured in router BGP VRF. Example: This example shows how to enable the IPv4 unicast address family support for a BGP VRF neighbor.

```text
(config)# router bgp 65000 vrf red
(config-bgp-vrf-red)# neighbor 1.1.10.2
(config-bgp-vrf-neighbor-1.1.10.2)# remote-as 65000
(config-bgp-vrf-neighbor-1.1.10.2)# address-family ipv4 unicast
(config-bgp-vrf-neighbor-address-family-ipv4/unicast)# commit
```

**Impacts and precautions:**

Changes on the address family will impact the BGP neighbor capabilities. It also causes a flap in the established BGP neighbor session.

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor address-family allow-as-in`

> **Página:** 703 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** When receiving routes from the respective neighbor, this option allows the installation of routes with local Autonomous System(AS) number present in AS path.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address address-family { ipv4 | ipv6 } unicast allow-as-in number-of-occurrences
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `neighbor address` — Specifies the BGP VRF neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `address-family { ipv4 | ipv6 }` — Selects the address family (AFI). — *Valores:* ipv4 or ipv6. IPv4 or IPv6 address family. · *Default:* N/A
- `unicast` — Selects the subsequent address family (SAFI). — *Valores:* unicast. IPv4 or IPv6 unicast routes. · *Default:* N/A
- `allow-as-in number-of-occurrences` — Specifies the maximum number of local AS number occurrences in AS path. — *Valores:* 0-10. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. The enabling of a BGP VRF neighbor address family support is only possible if it is already configured in router BGP VRF. Example: This example shows how to configure allow-as-in to accept routes with up to five local AS occurrences in AS path.

```text
(config)# router bgp 65000 vrf red
(config-bgp-vrf-red)# neighbor 1.1.10.2
(config-bgp-vrf-neighbor-1.1.10.2)# remote-as 65001
(config-bgp-vrf-neighbor-1.1.10.2)# address-family ipv4 unicast
(config-bgp-vrf-neighbor-address-family-ipv4/unicast)# allow-as-in 5
(config-bgp-vrf-neighbor-address-family-ipv4/unicast)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor address-family as-override`

> **Página:** 706 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** When advertising routes to the respective neighbor, this option replaces the remote Autonomous System(AS) number occurrences in AS path by the local AS number.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address address-family { ipv4 | ipv6 } unicast as-override
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `neighbor address` — Specifies the BGP VRF neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `address-family { ipv4 | ipv6 }` — Selects the address family (AFI). — *Valores:* ipv4 or ipv6. IPv4 or IPv6 address family. · *Default:* N/A
- `unicast` — Selects the subsequent address family (SAFI). — *Valores:* unicast. IPv4 or IPv6 unicast routes. · *Default:* N/A
- `as-override` — Option to replace the remote AS number by the local AS number in AS path. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. The enabling of a BGP VRF neighbor address family support is only possible if it is already configured in router BGP VRF. Example: This example shows how to configure as-override for a BGP VRF neighbor.

```text
(config)# router bgp 65000 vrf red
(config-bgp-vrf-red)# neighbor 1.1.10.2
(config-bgp-vrf-neighbor-1.1.10.2)# remote-as 65001
(config-bgp-vrf-neighbor-1.1.10.2)# address-family ipv4 unicast
(config-bgp-vrf-neighbor-address-family-ipv4/unicast)# as-override
(config-bgp-vrf-neighbor-address-family-ipv4/unicast)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor address-family prefix-list`

> **Página:** 709 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Associates a prefix list with a BGP neighbor in a VRF for export or import based on the address family.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address address-family ipv4 unicast [export-prefix-list prfx-name] [import-prefix-list prfx-name]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 address format. — *Valores:* a.b.c.d. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `address-family ipv4 unicast` — Enters in the BGP neighbor address family mode configuration. — *Valores:* ipv4 unicast. IPv4 unicast address family. · *Default:* N/A
- `export-prefix-list prfx-name` — Specifies the prefix list for export to be directly associated with the BGP neighbor. Use the no form to remove this parameter. — *Valores:* Name of a prefix list. · *Default:* N/A
- `import-prefix-list prfx-name` — Specifies the prefix list for import to be directly associated with the BGP neighbor. Use the no form to remove this parameter. — *Valores:* Name of a prefix list. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |

**Usage Guidelines:**

The VRF must be previously created. The prefix-list must exist. This command is only supported in IPv4 address family mode configuration. Example: This example shows how to associate the prefix list for export named PRXE with a BGP neighbor. This prefix list must be previously created.

```text
(config)# router bgp 65000
(config-bgp-65000)# vrf red
(config-bgp-vrf-red)# neighbor 50.50.50.1
(config-bgp-vrf-neighbor-50.50.50.1)# remote-as 65000
(config-bgp-vrf-neighbor-50.50.50.1)# address-family ipv4 unicast
(config-bgp-vrf-neighbor-address-family-ipv4/unicast)# export-prefix-list PRXE
```

This example shows how to associate the prefix list for import named PRXI with a BGP neighbor. This prefix list must be previously created.

```text
(config)# router bgp 65000
(config-bgp-65000)# vrf red
(config-bgp-vrf-red)# neighbor 50.50.50.1
(config-bgp-vrf-neighbor-50.50.50.1)# remote-as 65000
(config-bgp-vrf-neighbor-50.50.50.1)# address-family ipv4 unicast
(config-bgp-vrf-neighbor-address-family-ipv4/unicast)# import-prefix-list PRXI
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor administrative-status`

> **Página:** 712 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status of a BGP VRF neighbor.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `neighbor address` — Specifies the BGP VRF neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `administrative-status status` — Activate (up) or deactivate (down) the BGP VRF neighbor. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example shows how to configure the administrative status for a BGP VRF neighbor.

```text
(config)# router bgp 65000 vrf red neighbor 50.50.50.1
(config-bgp-vrf-neighbor-50.50.50.1)# remote-as 65001
(config-bgp-vrf-neighbor-50.50.50.1)# administrative-status down
(config-bgp-vrf-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor ebgp-multihop`

> **Página:** 715 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the maximum hop count to reach a BGP neighbor not directly connected.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address ebgp-multihop hop-count
```

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `neighbor address` — Specifies the BGP neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `ebgp-multihop hop-count` — Specifies the maximum hop count to reach the neighbor. — *Valores:* 1-255. · *Default:* 1

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.6 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the BGP neighbor ebgp-multihop in the neighbor command tree.

```text
(config)# router bgp 65000 vrf red neighbor 50.50.50.1 remote-as 66000
(config-neighbor-50.50.50.1)# ebgp-multihop 2
(config-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

This parameter is only available for eBGP sessions, when remote-as parameter is different from the as-number. For security reasons, this parameter is automatically configured to 1 and can manually configured to any value between 1 to 255. But if neighbor mode changes to iBGP setting remote-as parameter to same value as the as-number, the multihop value is automatically set to 255 and is no longer available on cli.

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor next-hop-self`

> **Página:** 718 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BGP VRF neighbor to use its own address as next hop in the advertised routes.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address next-hop-self
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `neighbor address` — Specifies the BGP VRF neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `next-hop-self` — Enables the neighbor option to use itself as next-hop. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example shows how to configure the BGP VRF neighbor to use its own address as next hop in the advertised routes.

```text
(config)# router bgp 65000 vrf red neighbor 50.50.50.1
(config-bgp-vrf-neighbor-50.50.50.1)# next-hop-self
(config-bgp-vrf-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor password`

> **Página:** 721 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BGP VRF neighbor password to be used in the Message Digest 5 (MD5) algorithm for TCP authentication.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address password pwd
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `neighbor address` — Specifies the BGP VRF neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `password pwd` — Specifies the BGP neighbor case-sensitive password to be use in the TCP connection authentication. — *Valores:* string (length 2 - 80). · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. The same password must be applied for both BGP peers. Example: This example shows how to configure the BGP VRF neighbor password using a plain text. This password is shown encrypted after the commit.

```text
(config)# router bgp 65000 vrf green neighbor 50.50.50.1 remote-as 65000
(config-bgp-vrf-neighbor-50.50.50.1)# password pwdTest
(config-bgp-vrf-neighbor-50.50.50.1)# commit
```

This example shows how to configure the BGP VRF neighbor password using an encrypted password.

```text
(config)# router bgp 65000 vrf green neighbor 50.50.50.1 remote-as 65000
(config-bgp-vrf-neighbor-50.50.50.1)# password "hls:2922743918:337ZpL=Z"
(config-bgp-vrf-neighbor-50.50.50.1)# commit
```

This example shows how to configure the BGP VRF neighbor password using special characters (i.e: " " , “?” , “!” , “;”). Please note that it is necessary to use double quotation marks in this case.

```text
(config)# router bgp 65000 vrf green neighbor 50.50.50.1 remote-as 65000
(config-bgp-vrf-neighbor-50.50.50.1)# password "pwd?test:2"
(config-bgp-vrf-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

Password must be enclosed in double quotation marks if special characters were used (i.e: " " , “?” , “!” , “;”). Note that in an established BGP session if password is configured or changed the session will be restarted.

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor remote-as`

> **Página:** 724 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BGP VRF neighbor remote Autonomous System(AS) number.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address remote-as as-number
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `neighbor address` — Specifies the BGP VRF neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `remote-as as-number` — Specifies the BGP VRF neighbor remote Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example shows how to configure a remote Autonomous System (AS) number for a VRF neighbor.

```text
(config)# router bgp 65000 vrf red neighbor 50.50.50.1
(config-bgp-vrf-neighbor-50.50.50.1)# remote-as 65000
(config-bgp-vrf-neighbor-50.50.50.1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf neighbor update-source-address`

> **Página:** 727 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BGP VRF neighbor source address to be used during the session establishment.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name neighbor address update-source-address address
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `neighbor address` — Specifies the BGP VRF neighbor address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `update-source-address address` — Specifies the BGP neighbor source address in IPv4 or IPv6 address format. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |
| 6.2 | Added support for IPv6. |

**Usage Guidelines:**

The VRF must be previously created. Example: This example show how to configure the source address for a BGP VRF neighbor in the neighbor command tree.

```text
(config)# router bgp 65000 vrf red neighbor 50.50.50.1
(config-bgp-vrf-neighbor-50.50.50.1)# update-source-address 100.100.100.1
(config-bgp-vrf-neighbor-50.50.50.1)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf route-map set-community`

> **Página:** 730 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Set community configuration on VRF.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name route-map rmap-name { seq-number | * } set-community { community | internet | local-AS | no-advertise | no-export }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System (AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `route-map rmap-name` — Creates a route map with the given rmap-name. — *Valores:* N/A · *Default:* N/A
- `seq-number` — Applies the sequence number to the route map entry. — *Valores:* 1-4294967295. · *Default:* N/A
- `∗` — A reference for all route map sequences. This option allows edition or deletion of all route map sequences simultaneously. — *Valores:* N/A · *Default:* N/A
- `set-community { community | internet | local-AS | no-advertise | no-export }` — Sets the community attribute. The DmOS user can enter either a single community or a list of communities, separated by spaces. A single route map can include up to 32 communities. — *Valores:* Well-known community or specific community in AS:nn format. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. Previous versions only allowed users to enter one community per route map. With version 11.2.0 , DmOS users were given the option to enter a 11.4.0 list of communities on VRF global. In version 11.4.0 the functionality has been enhanced to include support for other VRFs. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a community for prefixes.

```text
(config)# router bgp 100 vrf red
(config-bgp-vrf-red)# route-map RMAP 10
(config-route-map-RMAP/10)# set-community 100:123
(config-route-map-RMAP/10)# commit
```

Example: This example shows how to configure multiple communities to a route map.

```text
(config)# router bgp 100 vrf red
(config-bgp-vrf-red)# route-map RMAP 10
(config-route-map-RMAP/10)# set-community 100:124 100:344 100:556 100:834
(config-route-map-RMAP/10)# commit
```

Example: This example shows how to remove multiple communities from a route map.

```text
(config)# router bgp 100 vrf red
(config-bgp-vrf-red)# route-map RMAP 10
(config-route-map-RMAP/10)# no set-community 100:123 100:344
(config-route-map-RMAP/10)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router bgp vrf router-id`

> **Página:** 733 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the router identifier of a BGP router per VRF.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router bgp as-number vrf vrf-name router-id id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `as-number` — Specifies the Router BGP Autonomous System(AS) number. — *Valores:* 1-4294967295. · *Default:* N/A
- `vrf vrf-name` — Specifies a VRF name. — *Valores:* Name of an existent VRF. · *Default:* N/A
- `router-id id` — Specifies the Router BGP identifier expressed in IPv4 address format. The value 0.0.0.0 and addresses in range 224.0.0.0 - 247.255.255.255 cannot be used as id. — *Valores:* a.b.c.d. · *Default:* global bgp router-id

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |

**Usage Guidelines:**

The VRF must be previously created. When the router-id for the BGP router in the VRF is not configured, the global BGP router-id is used. Example: This example shows how to configure the router-id for the BGP router in the VRF red.

```text
(config)# router bgp 65000 vrf red router-id 1.1.1.1
(config-bgp-65000)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip bgp`

> **Página:** 736 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows summarized information about the BGP routing processes.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show ip bgp [vrf name] summary
```

**Parameters:**

- `vrf name` — Specifies a VRF name (only in supported platforms). — *Valores:* Name of an existent VRF. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |
| 4.6 | Added VRF support. |

**Usage Guidelines:**

The time counter format is showed using only three units progressively: • hh:mm:ss - example: 23:59:59 • XXdaysYYhoursZZmin - example: 06d23h59m • XXweeksYYdaysZZhours - example: 04w01d23h • XXmonthsYYweeksZZdays - example: 11m04w01d • XXyearsYYmonthsZZweeks - example: 99y11m04w Example: This example shows summarized information about BGP routers on global VRF.

```text
# show ip bgp
```

BGP router identifier 1.1.10.1, local AS number 101, Admin Status: up ipv4 unicast statistics: iBGP routes in : 1 eBGP routes in : 0 Eligible routes : 0 Ineligible routes : 1 Active routes : 0 Advertised routes : 0 ipv6 unicast statistics: iBGP routes in : 5 eBGP routes in : 0 Eligible routes : 3 Ineligible routes : 2 Active routes : 3 Advertised routes : 0 Neighbor V AS MsgRcvd MsgSent Up/Down State/PfxRcd -------------------------------------------------------------------------- 1.1.1.1 4 101 165 157 00:24:41 1 1111::1 4 101 169 157 00:24:18 5 This example shows summarized information about all BGP routers on VRFs.

```text
# show ip bgp vrf all summary
VRF: global
=======
```

BGP router identifier 1.1.10.1, local AS number 101, Admin Status: up ipv4 unicast statistics: iBGP routes in : 1 eBGP routes in : 0 Eligible routes : 0 Ineligible routes : 1 Active routes : 0 Advertised routes : 0 vpnv4 unicast statistics: iBGP routes in : 0 eBGP routes in : 0 Eligible routes : 0 Ineligible routes : 0 Active routes : 0 Advertised routes : 0 ipv6 unicast statistics: iBGP routes in : 5 eBGP routes in : 0 Eligible routes : 3 Ineligible routes : 2 Active routes : 3 Advertised routes : 0 Neighbor V AS MsgRcvd MsgSent Up/Down State/PfxRcd -------------------------------------------------------------------------- 1.1.1.1 4 101 165 157 00:24:41 1 1111::1 4 101 169 157 00:24:18 5 VRF: GREEN ======= BGP router identifier 1.1.10.1, local AS number 101, Admin Status: up ipv4 unicast statistics: iBGP routes in : 1 eBGP routes in : 0 Eligible routes : 0 Ineligible routes : 1 Active routes : 0 Advertised routes : 0 Neighbor V AS MsgRcvd MsgSent Up/Down State/PfxRcd -------------------------------------------------------------------------- 2.2.2.2 4 101 165 157 00:00:00 idle This example shows summarized information about a specific VRF.

```text
# show ip bgp vrf GREEN summary
VRF: GREEN
=======
```

BGP router identifier 1.1.10.1, local AS number 101, Admin Status: up ipv4 unicast statistics: iBGP routes in : 1 eBGP routes in : 0 Eligible routes : 0 Ineligible routes : 1 Active routes : 0 Advertised routes : 0 vpnv4 unicast statistics: iBGP routes in : 0 eBGP routes in : 0 Eligible routes : 0 Ineligible routes : 0 Active routes : 0 Advertised routes : 0 ipv6 unicast statistics: iBGP routes in : 0 eBGP routes in : 0 Eligible routes : 0 Ineligible routes : 0 Active routes : 0 Advertised routes : 0 Neighbor V AS MsgRcvd MsgSent Up/Down State/PfxRcd -------------------------------------------------------------------------- 2.2.2.2 4 101 165 157 00:00:00 idle

**Output Terms:**

Output Description VRF Name Indicates the VRF name for the current BGP instance. BGP router Indicates the router identifier of BGP. identifier local AS number Local Autonomous System(AS) number. Admin Status Indicates the administrative status of BGP. iBGP routes in The total number of IBGP routes received. Output Description eBGP routes in The total number of EBGP routes received. Eligible routes The number of prefixes received that are eligible to become active. The number of prefixes received that are not eligible to become Ineligible routes active. Active routes The number of active routes. The number of advertised prefixes currently associated with any Advertised routes neighbor. Neighbor The IP address of the neighbor. V BGP version. AS The remote Autonomous System(AS) number. MsgRcvd The total number of messages received from the neighbor. MsgSent The total number of messages transmitted to the neighbor. How long the neighbor is in the established state or since the last time it was established. When zeroed, the session were never esUp/Down tablished. See the usage guidelines of this command for information about time counter format. The BGP neighbor state while the session is not established or the State/PfxRcd number of prefixes received from the neighbor if the session is already established.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip bgp community`

> **Página:** 741 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about communities received from neighbors and included in the BGP routing table.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show ip bgp community [ attribute { community | internet | local-AS | no-advertise | no-export } | network ip-address ]*
```

**Parameters:**

- `community` — Shows information about all received communities. — *Valores:* N/A · *Default:* N/A
- `attribute community | internet | local-AS | no-advertise | no-export` — Specifies the community attribute to be searched for. — *Valores:* Well-known community or specific community in AS:nn format. · *Default:* N/A
- `network ip-address` — Specifies the network to filter displayed information. — *Valores:* Must be a valid IPv4 or IPv6 network. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command to list all communities.

```text
# show ip bgp community
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; Network Next Hop Metric LocPrf Community ------------------------------------------------------------------------------ *>i 40.40.40.0/24 200.200.200.4 0 100 no-export *>i 30.30.30.0/24 200.200.200.3 0 100 no-advertise *>i 20.20.20.0/24 200.200.200.2 0 100 local-AS *>i 10.10.10.0/24 200.200.200.1 0 100 internet 200:200 *> 21.21.21.0/24 0.0.0.0 0 100 100:100 200:200 300:300 *> 22.22.22.0/24 0.0.0.0 0 100 100:100 200:200 300:30000 This example shows how to use this command to filter a specific community.

```text
# show ip bgp community attribute 100:100
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; Network Next Hop Metric LocPrf Community ------------------------------------------------------------------------------ *> 21.21.21.0/24 0.0.0.0 0 100 100:100 200:200 300:300 *> 22.22.22.0/24 0.0.0.0 0 100 100:100 200:200 300:30000 This example shows how to use this command to filter a specific network.

```text
# show ip bgp community network 10.10.10.0/24
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; Network Next Hop Metric LocPrf Community --------------------------------------------------------------------- *>i 10.10.10.0/24 200.200.200.1 0 100 internet 200:200

**Output Terms:**

Output Description The status of the prefix entry. This information is displayed prior to Status Code the Network column. The legend of status codes is displayed at the beginning of each report. Network The network address. Indicates the IP address for forwarding traffic to destination network. Next Hop Metric Indicates the route metric. LocPrf Indicates the route local preference value. The default value is 100. Community Indicates the route communities attribute.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip bgp neighbor`

> **Página:** 744 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about the BGP neighbors.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show ip bgp [ vrf name ] neighbor [ ip-address [ [ address-family ipv4 | ipv6 | vpnv4 | vpnv6 ] advertised-routes | received-routes ] | summary | brief | detail | extensive ]
```

**Parameters:**

- `vrf name` — Specifies a VRF name (only in supported platforms) — *Valores:* Name of an existent VRF. · *Default:* N/A
- `ip-address` — Filters the command output by the remote IP address. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `address-family` — Filters the command output by address-family — *Valores:* ipv4 | ipv6 | vpnv4 | vpnv6 · *Default:* N/A
- `advertised-routes` — Shows the routes that are being advertised to the given neighbor. — *Valores:* N/A · *Default:* N/A
- `received-routes` — Shows the routes that are being received from a given neighbor. — *Valores:* N/A · *Default:* N/A
- `summary` — Shows summarized information about BGP neighbors. — *Valores:* N/A · *Default:* N/A
- `brief` — Shows brief information about BGP neighbors. — *Valores:* N/A · *Default:* N/A
- `detail` — Shows detailed information about the BGP neighbors. — *Valores:* N/A · *Default:* N/A
- `extensive` — Shows extensive information about the BGP neighbors. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. |
| 4.6 | Added VRF support. |
| 9.4 | Added advertised-routes show. |
| 9.6 | Added received-routes show. |
| 9.8 | Added address-family filter. |

**Usage Guidelines:**

The time counter format is showed using only three units progressively: • hh:mm:ss - example: 23:59:59 • XXdaysYYhoursZZmin - example: 06d23h59m • XXweeksYYdaysZZhours - example: 04w01d23h • XXmonthsYYweeksZZdays - example: 11m04w01d • XXyearsYYmonthsZZweeks - example: 99y11m04w When the command does not provide any VRF filter, only the information about the BGP in the global VRF will be displayed. Example: This example shows how to use the show ip bgp neighbor brief command. Please note that for sessions not established the Port value is zero.

```text
# show ip bgp neighbor brief
```

Remote address Port Local address Port Admin BGP state -------------- ---- ------------- ---- ----- --------- 150.150.150.2 0 199.199.199.1 0 up active 100.100.100.1 48078 200.200.200.1 179 up established 200.200.200.3 0 200.200.200.2 0 up active 1111::1 179 2222::2 39015 up established To show just the entry with Remote IP address 100.100.100.1, the following command must be used:

```text
# show ip bgp neighbor 100.100.100.1 brief
```

Remote address Port Local address Port Admin BGP state -------------- ---- ------------- ---- ----- --------- 100.100.100.1 48078 200.200.200.1 179 up established To order neighbor entries by the Remote address column, the following command must be used:

```text
# show ip bgp neighbor brief | sort-by remote-addr-type
```

Remote address Port Local address Port Admin BGP state -------------- ---- ------------- ---- ----- --------- 100.100.100.1 48078 200.200.200.1 179 up established 150.150.150.2 0 199.199.199.1 0 down idle 200.200.200.3 0 200.200.200.2 0 up active This example shows how to use the show ip bgp neighbor detail command.

```text
# show ip bgp neighbor detail
Local AS: 300;
```

Local address: 8.8.8.2; Admin: enable; BGP state: established; BGP Version: 4; Remote address: 8.8.8.1; Remote AS: 200; Last received Update message 00:00:12 Last received message: 00:00:10 Up/Down time: 00:04:01; Neighbor ID: 200.200.200.1; Hold time: 180 secs; Keepalive: 60 secs; Neighbor capabilities: Address family IPv4 Unicast: advertised and received Address family IPv6 Unicast: advertised Four Bytes AS Number: advertised and received Route Refresh: advertised and received Route Refresh Cisco: advertised and received Message counters: Type Sent Received ---- ---- -------- Open 1 1 Notification 0 0 Update 1 1 Keepalive 1 1 Route refresh 0 0 Total 3 3 Connect retries: 2; BGP transitions established: 1; Last BGP state: Established; Last BGP event: received-keepalive; Selected local address: 8.8.8.2; Selected local port: 179; Selected remote port: 51304; Local AS: 300; Local address: 2222::2; Admin: enable; BGP state: established; BGP Version: 4; Remote address: 1111::1; Remote AS: 200; Last received update message: 00:55:01; Last received message: 00:00:41; Up/Down time: 01:01:16; Neighbor ID: 1.1.1.1; Hold time: 180 secs; Keepalive: 60 secs; Neighbor capabilities: Address family IPv4 Unicast: advertised Address family IPv6 Unicast: advertised and received Four Bytes AS Number: advertised and received Route Refresh: advertised and received Route Refresh Cisco: advertised and received Message counters: Type Sent Received ---- ---- -------- Open 2 2 Notification 0 1 Update 0 11 Keepalive 197 197 Route refresh 0 0 Total 199 211 Connect retries: 2; BGP transitions established: 2; Last BGP state: Established; Last BGP event: received-keepalive; Selected local address: 2222::2; Selected local port: 39015; Selected remote port: 179; This example shows how to use the show ip bgp neighbor extensive command.

```text
# show ip bgp neighbor extensive
Local AS: 300;
```

Local address: 8.8.8.2; Admin: enable; BGP state: established; BGP Version: 4; Remote address: 8.8.8.1; Remote AS: 200; Last received Update message 01d02h03m Last received message: 00:00:25 Up/Down time: 04w01d03h; Neighbor ID: 200.200.200.1; Hold time: 180 secs; Keepalive: 60 secs; Neighbor capabilities: Address family IPv4 Unicast: advertised and received Address family IPv6 Unicast: advertised Four Bytes AS Number: advertised and received Route Refresh: advertised and received Route Refresh Cisco: advertised and received Message counters: Type Sent Received ---- ---- -------- Open 1 1 Notification 0 0 Update 1 1 Keepalive 3154 3154 Route refresh 0 0 Total 3156 3156 Connect retries: 2; BGP transitions established: 1; Last BGP state: Established; Last BGP event: received-keepalive; Selected local address: 8.8.8.2; Selected local port: 179; Selected remote port: 51304; Peer prefix counters: ipv4 unicast: Received: 1 Sent: 1 Accepted: 1 Advertised: 1 Rejected: 0 Active: 0 Local AS: 300; Local address: 2222::2; Admin: enable; BGP state: established; BGP Version: 4; Remote address: 1111::1; Remote AS: 200; Last received update message: 01:00:18; Last received message: 00:00:53; Up/Down time: 01:06:33; Neighbor ID: 1.1.1.1; Hold time: 180 secs; Keepalive: 60 secs; Neighbor capabilities: Address family IPv4 Unicast: advertised Address family IPv6 Unicast: advertised and received Four Bytes AS Number: advertised and received Route Refresh: advertised and received Route Refresh Cisco: advertised and received Message counters: Type Sent Received ---- ---- -------- Open 2 2 Notification 0 1 Update 0 11 Keepalive 203 203 Route refresh 0 0 Total 205 217 Connect retries: 2; BGP transitions established: 2; Last BGP state: Established; Last BGP event: received-keepalive; Selected local address: 2222::2; Selected local port: 39015; Selected remote port: 179; Peer prefix counters: ipv4 unicast: Received: 0 Sent: 0 Accepted: 0 Advertised: 0 Rejected: 0 Active: 0 Peer prefix counters: ipv6 unicast: Received: 5 Sent: 0 Accepted: 3 Advertised: 0 Rejected: 2 Active: 3 This command shows brief information about neighbors from the given VRF (red, in the example).

```text
# show ip bgp vrf red neighbor brief
```

Remote address Port Local address Port Admin BGP State ------------------------------------------------------------------ 172.30.20.2 179 172.30.20.1 43647 up established This command shows just summary information about neighbors from all VRFs.

```text
# show ip bgp vrf all neighbor summary
VRF: global
=======
```

Neighbor V AS MsgRcvd MsgSent Up/Down State/PfxRcd --------------------------------------------------------------------------- 10.10.10.1 4 300 2109 4918 00:00:15 0 a:f0ca:bebe:cafe::1 4 400 1760 2019 14:38:07 4 cafe:c0ca:caca::1 4 300 0 0 00:00:00 idle VRF: black ======= Neighbor V AS MsgRcvd MsgSent Up/Down State/PfxRcd --------------------------------------------------------------------------- 40.40.40.1 4 900 1777 2042 14:46:50 0 VRF: red, route-distinguisher 255.255.255.255:99 ============================= Neighbor V AS MsgRcvd MsgSent Up/Down State/PfxRcd --------------------------------------------------------------------------- 172.30.20.2 4 200 671 1013 14:39:14 11

```text
# show ip bgp vrf red neighbor summary
```

Neighbor V AS MsgRcvd MsgSent Up/Down State/PfxRcd --------------------------------------------------------------------------- 172.30.20.2 4 200 34 36 00:14:59 10 To filter a specific VRF, the following command must be used:

```text
# show ip bgp vrf red prefixes
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; Origin codes: i - IGP; e - EGP; ? - incomplete; Network Next Hop Metric LocPrf Weight Learned from Path ------------------------------------------------------------------------------- *> 2.2.1.0/20 7.6.8.2 0 100 0 7.6.8.2 200 ? This example shows how to use this command to list advertised routes to a neighbor on global VRF.

```text
# show ip bgp neighbor 200.200.200.3 advertised-routes
```

Neighbor Network Next Hop LocPrf Path --------------------------------------------------------------------------------- 200.200.200.3 8.8.8.0/24 200.200.200.1 100 0 200.200.200.3 9.9.9.0/24 200.200.200.1 100 0 200.200.200.3 10.10.10.0/24 200.200.200.1 100 0 200.200.200.3 20.20.20.0/24 200.200.200.1 100 0 200.200.200.3 200.200.200.1/32 200.200.200.1 100 0 200.200.200.3 200.200.200.2/32 200.200.200.1 100 0 200.200.200.3 200.200.200.3/32 20.20.20.2 100 0 To filter a specific VRF when listing advertised routes, the following command must be used:

```text
# show ip bgp vrf green neighbor 8.8.8.2 advertised-routes
```

Neighbor Network Next Hop LocPrf Path ------------------------------------------------------------------------------- 8.8.8.2 2.2.2.0/24 8.8.8.1 0 200 This example shows how to use this command to list routes received from a neighbor in the global VRF.

```text
# show ip bgp neighbor c0ca:c01a:21::1 received-routes
```

Network Next Hop Metric LocPrf Weight Path ---------------------------------------------------------------------------------- *> c0ca:c01a:10::/64 c0ca:c01a:21::1 0 100 0 1000 ? *> c0ca:c01a:11::/64 c0ca:c01a:21::1 0 100 0 1000 ? * c0ca:c01a:21::/64 c0ca:c01a:21::1 0 100 0 1000 ? This example shows how to use this command to filter a specific VRF when listing received routes.

```text
# show ip bgp vrf blue neighbor c0ca:c01a:41::1 received-routes
```

Network Next Hop Metric LocPrf Weight Path ---------------------------------------------------------------------------------- *> c0ca:c01a:30::/64 c0ca:c01a:41::1 0 100 0 1000 ? *> c0ca:c01a:31::/64 c0ca:c01a:41::1 0 100 0 1000 ? * c0ca:c01a:41::/64 c0ca:c01a:41::1 0 100 0 1000 ?

**Output Terms:**

Output Description Remote address The neighbor IP address. Port Indicates the remote and local TCP ports used in this connection. Output Description Local address The local IP address of BGP session. Admin Administrative status of the neighbor. BGP state The negotiation stage of BGP session. Local AS Local Autonomous System(AS) number. BGP Version BGP Protocol Version. Remote AS Autonomous System(AS) number of the neighbor. Elapsed time since the last BGP Update message was received from Last received the neighbor. If no Update messages were received, this value reUpdate message mains zeroed. See the usage guidelines of this command for information about time counter format. Elapsed time since the last BGP message was received from the Last received neighbor. If no BGP messages were received, this value remains message zeroed. See the usage guidelines of this command for information about time counter format. How long the neighbor is in the established state or since the last time it was established. When zeroed, the session was never estabUp/Down time lished. See the usage guidelines of this command for information about time counter format. Neighbor ID BGP neighbor router identifier. Time interval in seconds for the hold timer established with the Hold time neighbor. Time interval in seconds for the keepalive timer established with the Keepalive neighbor. Output Description Neighbor Capabilities exchanged with the neighbor. Capabilities neither adcapabilities vertised nor received are omitted from the list. Address family Address family IPv4 Unicast capability was advertised and/or reIPv4 Unicast ceived. Address family Address family IPv6 Unicast capability was advertised and/or reIPv6 Unicast ceived. Four Bytes AS Four Bytes AS Number capability was advertised and/or received. Number Graceful Restart Graceful Restart capability was advertised and/or received. ORF Outbound Route Filters capability was advertised and/or received. Outbound Route Filters Cisco capability was advertised and/or reORF Cisco ceived. Route Refresh Route Refresh capability was advertised and/or received. Route Refresh Route Refresh Cisco capability was advertised and/or received. Cisco Number of BGP messages sent or received for each type of message. Message counters Output Description Type of BGP message: • Open: used to establish a BGP session; • Notification: used to notify an error condition and close a BGP session; • Update: exchange network reachability information; • Keepalive: exchange between peers to keep a BGP session esType tablished; • Route refresh: used to request BGP route updates from BGP neighbor or to send outbound route updates to a BGP neighbor; • Total: the number of all BGP message types exchanged with the neighbor. Sent The number of sent messages of each BGP message type. Received The number of received messages of each BGP message type. Connect retries The number of connection retry attempts of this peer. BGP transitions The total number of times the state transitioned into established established state for this neighbor. Last BGP state The BGP neighbor previous state. Last BGP event The last BGP event which was used to transition the BGP state. Selected local The local address used by the transport connection for the peering address session. Selected local The local port used by the transport connection for the peering sesport sion. Output Description Selected remote The remote port used by the transport connection for the peering port session. Peer prefix The number of prefixes exchanged with the peer classified according counters to the performed action. Received The total number of prefixes received from this peer. Sent The number of prefixes ready to be sent. Accepted The number of accepted prefixes. Advertised The number of advertised prefixes. Rejected The number of rejected prefixes. Active The number of active prefixes.

**Impacts and precautions:**

For sessions not established the Local/Remote Port value will display zero and Local Address will display “0.0.0.0”.

**Hardware restrictions:**

N/A


### `show ip bgp prefixes`

> **Página:** 756 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about prefixes received from neighbors and included in the BGP routing table.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show ip bgp [vrf name] prefixes [destination prefix]
```

**Parameters:**

- `vrf name` — Specifies a VRF name (only in supported platforms) — *Valores:* Name of an existent VRF. · *Default:* N/A
- `destination prefix` — Specifies a destination prefix to be searched for. The search result will include prefixes that matches networks with the same prefix length or longer. — *Valores:* Must be a valid IPv4 or IPv6 prefix. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | Added support for IPv6. • Added VRF support. 4.6 • Added destination filter. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command to list prefixes learned on VRF Global. Please note the different status code for entries “221.10.0.19/19” since one was selected as best path due to higher local preference.

```text
# show ip bgp prefixes
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; Origin codes: i - IGP; e - EGP; ? - incomplete; Network Next Hop Metric LocPrf Weight Learned from Path ------------------------------------------------------------------------------- *> 221.10.0.0/19 172.16.78.1 0 200 0 172.16.78.1 65001 ? *> 221.10.0.0/20 172.16.78.1 0 100 0 172.16.78.1 65001 ? * 221.10.0.0/19 172.16.78.3 0 100 0 172.16.78.3 65001 ? *> 221.10.16.0/20 172.16.78.3 0 100 0 172.16.78.3 65001 ? *>i 2001::/64 2002::3 0 100 0 1111::1 i *>i 2002::/64 1111::1 0 100 0 1111::1 i * i 5050::/64 8009::2 0 100 0 1111::1 i *>i 8009::/64 1111::1 0 100 0 1111::1 i To show just the network 221.10.16.0/20 entry, use the following destination filter:

```text
# show ip bgp prefixes destination 221.10.16.0/20
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; Origin codes: i - IGP; e - EGP; ? - incomplete; Network Next Hop Metric LocPrf Weight Learned from Path ------------------------------------------------------------------------------- *> 221.10.16.0/20 172.16.78.3 0 100 0 172.16.78.3 65001 ? Similarly, to search for all networks that start with 221.10.X.X, this filter could be used:

```text
# show ip bgp prefixes destination 221.10.0.0/16
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; Origin codes: i - IGP; e - EGP; ? - incomplete; Network Next Hop Metric LocPrf Weight Learned from Path ------------------------------------------------------------------------------- *> 221.10.0.0/19 172.16.78.1 0 200 0 172.16.78.1 65001 ? *> 221.10.0.0/20 172.16.78.1 0 100 0 172.16.78.1 65001 ? * 221.10.0.0/19 172.16.78.3 0 100 0 172.16.78.3 65001 ? *> 221.10.16.0/20 172.16.78.3 0 100 0 172.16.78.3 65001 ? This example shows how to use this command to list prefixes learned on all VRFs including VRF global.

```text
# show ip bgp vrf all prefixes
VRF: global
=======
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; Origin codes: i - IGP; e - EGP; ? - incomplete; Network Next Hop Metric LocPrf Weight Learned from Path ------------------------------------------------------------------------------- *> 2.1.0.0/19 7.6.8.1 0 200 0 7.6.8.1 500 ? *> 2.1.0.0/20 7.6.8.1 0 100 0 7.6.8.1 500 ? * 2.1.0.0/19 7.6.8.3 0 100 0 7.6.8.3 500 ? *> 2.1.6.0/20 7.6.8.3 0 100 0 7.6.8.3 500 ? *>i 2001::/64 2002::3 0 100 0 1111::1 i *>i 2002::/64 1111::1 0 100 0 1111::1 i * i 5050::/64 8009::2 0 100 0 1111::1 i *>i 8009::/64 1111::1 0 100 0 1111::1 i VRF: red ======= Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; Origin codes: i - IGP; e - EGP; ? - incomplete; Network Next Hop Metric LocPrf Weight Learned from Path ------------------------------------------------------------------------------- *> 2.2.1.0/20 7.6.8.2 0 100 0 7.6.8.2 200 ? To filter a specific VRF, the following command must be used:

```text
# show ip bgp vrf red prefixes
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; Origin codes: i - IGP; e - EGP; ? - incomplete; Network Next Hop Metric LocPrf Weight Learned from Path ------------------------------------------------------------------------------- *> 2.2.1.0/20 7.6.8.2 0 100 0 7.6.8.2 200 ?

**Output Terms:**

Output Description VRF Name Indicates the VRF name for the current BGP instance. Output Description The status of the prefix entry. This information is displayed prior to Status Code the Network column. The legend of status codes is displayed at the beginning of each report. The origin of the prefix entry. This information is displayed right Origin codes after the Path column. The legend of origin codes is displayed at the beginning of each report. Network The network address. Indicates the IP address for forwarding traffic to destination network. Next Hop Metric Indicates the route metric. LocPrf Indicates the route local preference value. The default value is 100. Indicates the route local degree of preference. A lower weight value Weight is preferred. Learned from Indicates the IP address from where this entry was learned from. Indicates the AS path through which the destination network was Path learned.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip bgp vpnv4 labels`

> **Página:** 761 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about incoming and outgoing BGP labels for each prefix on a Virtual Private Network IPv4 (VPNv4).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show ip bgp [vrf name] vpnv4 labels
```

**Parameters:**

- `vrf name` — Specifies a VRF name (only in supported platforms) — *Valores:* Name of an existent VRF. · *Default:* N/A
- `vpnv4 labels` — Shows the incoming and outgoing labels for each prefix on a VPNv4. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |

**Usage Guidelines:**

This command can be used to show information about the prefixes and respective incoming and outgoing labels on a VPNv4. Example: This example shows how to use this command to display all prefixes and the respective labels related to VRF global.

```text
# show ip bgp vpnv4 labels
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; In Out RD Network Next Hop Label Label --------------------------------------------------------------- *> 100:1 50.50.50.0/24 200.200.200.1 17 -- *> 100:1 50.50.51.0/28 200.200.200.1 17 -- *> 100:1 50.50.52.0/31 200.200.200.1 17 -- *>i 100:1 150.150.150.0/24 200.200.200.2 -- 17 *>i 100:1 150.150.151.0/28 200.200.200.2 -- 17 *>i 100:1 150.150.152.0/31 200.200.200.2 -- 17 *> 100:2 90.90.90.0/24 200.200.200.1 16 -- *>i 100:2 190.190.190.0/24 200.200.200.2 -- 16 *>i 101:1 6.6.6.0/24 200.200.200.3 -- 16 *>i 101:1 160.160.160.0/24 200.200.200.3 -- 16 *>i 1.2.3.4:1 9.9.9.0/24 200.200.200.3 -- 17 *>i 1.2.3.4:1 195.195.195.0/24 200.200.200.3 -- 17 *>i 90000:5 2.2.2.0/24 200.200.200.3 -- 18 To show the VPNv4 information for all VRFs the following command can be used:

```text
# show ip bgp vrf all vpnv4 labels
VRF: green, route-distinguisher 100:1
=============================
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; In Out RD Network Next Hop Label Label ----------------------------------------------------------- *> 100:1 50.50.50.0/24 200.200.200.1 17 -- *> 100:1 50.50.51.0/28 200.200.200.1 17 -- *> 100:1 50.50.52.0/31 200.200.200.1 17 -- *>i 100:1 150.150.150.0/24 200.200.200.2 -- 17 *>i 100:1 150.150.151.0/28 200.200.200.2 -- 17 *>i 100:1 150.150.152.0/31 200.200.200.2 -- 17 *>i 101:1 6.6.6.0/24 200.200.200.3 -- 16 *>i 101:1 160.160.160.0/24 200.200.200.3 -- 16 VRF: red, route-distinguisher 100:2 ============================= Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; In Out RD Network Next Hop Label Label ----------------------------------------------------------- *> 100:2 90.90.90.0/24 200.200.200.1 16 -- *>i 100:2 190.190.190.0/24 200.200.200.2 -- 16 To show the VPNv4 information for a specific VRF the following command can be used:

```text
# show ip bgp vrf red vpnv4 labels
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; In Out RD Network Next Hop Label Label ----------------------------------------------------------- *> 100:2 90.90.90.0/24 200.200.200.1 16 -- *>i 100:2 190.190.190.0/24 200.200.200.2 -- 16

**Output Terms:**

Output Description VRF Name Indicates the VRF name for the current BGP instance. Output Description The status of the prefix entry. This information is displayed prior to Status codes the Network column. The legend of status codes is displayed at the beginning of each report. RD Route Distinguisher of the VPNv4 prefix. Network The network address. Indicates the IP address for forwarding traffic to destination network. Next Hop In Label Indicates the incoming label. Out Label Indicates the outgoing label.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip bgp vpnv6 labels`

> **Página:** 765 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about incoming and outgoing BGP labels for each prefix on a Virtual Private Network IPv6 (VPNv6).

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show ip bgp [vrf name] vpnv6 labels
```

**Parameters:**

- `vrf name` — Specifies a VRF name (only in supported platforms) — *Valores:* Name of an existent VRF. · *Default:* N/A
- `vpnv6 labels` — Shows the incoming and outgoing labels for each prefix on a VPNv6. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 6.0 | This command was introduced. |

**Usage Guidelines:**

This command can be used to show information about the prefixes and respective incoming and outgoing labels on a VPNv6. Example: This example shows how to use this command to display all prefixes and the respective labels related to VRF global.

```text
# show ip bgp vpnv6 labels
```

Status codes: s suppressed; d damped; h history; * valid; > best; i - internal; S Stale; RD Network Next Hop In Label Out Label ------------------------------------------------------------------------- *> 60000:740 2001:db8:101::/64 ::ffff:1.1.1.1 16 -- *> 60000:740 2001:db8:201::/64 ::ffff:1.1.1.1 16 -- *>i 60000:750 2001:db8:102::/64 ::ffff:4.4.4.1 -- 16 *>i 60000:750 2001:db8:202::/64 ::ffff:4.4.4.1 -- 16 To show the VPNv6 information for all VRFs the following command can be used:

```text
# show ip bgp vrf all vpnv6 labels
```

To show the VPNv6 information for a specific VRF the following command can be used:

```text
# show ip bgp vrf red vpnv6 labels
```

**Output Terms:**

Output Description VRF Name Indicates the VRF name for the current BGP instance. Output Description The status of the prefix entry. This information is displayed prior to Status codes the Network column. The legend of status codes is displayed at the beginning of each report. RD Route Distinguisher of the VPNv6 prefix. Network The network address. Indicates the IP address for forwarding traffic to destination network. Next Hop In Label Indicates the incoming label. Out Label Indicates the outgoing label.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A OSPF This topic describes the commands related to management of OSPF topologies such as commands to configure the OSPF parameters or to inspect the protocol status.


## OSPF

### `clear ospf`

> **Página:** 768 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Clears OSPF information about neighbors, processes or statistics.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
clear ospf neighbor [ip neighbor-ip][process-id process-id] clear ospf process process-id clear ospf statistics interface
```

**Parameters:**

- `neighbor` — Clears OSPF neighbor information. — *Valores:* N/A · *Default:* N/A
- `neighbor ip neighbor-ip` — Clears only neighbor information for the specified OSPF neighbor. — *Valores:* 0.0.0.0-255.255.255.255. · *Default:* N/A
- `neighbor process-id process-id` — Clears only neighbor information for the specified OSPF process ID. — *Valores:* 1-65535. · *Default:* N/A
- `process process-id` — Clears OSPF information for the specified OSPF process ID. — *Valores:* 1-65535. · *Default:* N/A
- `statistics interface` — Clears OSPF interface statistics. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples show how to clear OSPF information.

```text
# clear ospf process 1
# clear ospf neighbor
# clear ospf neighbor ip 10.10.10.0
# clear ospf neighbor ip 10.10.10.0 process-id 1
# clear ospf statistics interface
```

**Impacts and precautions:**

The command “clear ospf process” will restart all OSPF adjacencies from the specified router instance. The command “clear ospf neighbor” will restart all OSPF adjacencies if neighbor address was not specified.

**Hardware restrictions:**

N/A


### `router ospf`

> **Página:** 771 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an OSPF router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. For platforms with VRF restrictions, only the VRF ‘global’ is available. — *Valores:* string. · *Default:* global

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 5.0 | The command was modified to support OSPF routers in VRFs. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure an OSPF router.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# commit
```

This example shows how to configure an OSPF router in VRF green.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 10 vrf green
(config-ospf-10-vrf-green)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf administrative-status`

> **Página:** 774 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the administrative status of an OSPF router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `administrative-status status` — Activates (up) or deactivates (down) the OSPF router. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the administrative status.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# administrative-status down
(config-ospf-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area`

> **Página:** 776 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the area of a router OSPF.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 1-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a router ospf area.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 5
(config-area-5)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area administrative-status`

> **Página:** 778 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the administrative status of an OSPF area.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `administrative-status status` — Activates (up) or deactivates (down) the OSPF area. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the administrative status.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 5 administrative-status down
(config-area-5)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area interface`

> **Página:** 781 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables the OSPF protocol on an specified L3 or loopback interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface interface-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface-name` — Specifies L3 and loopback interfaces for the OSPF router. The L3 and loopback interfaces must be created before the commit. — *Valores:* Any L3 and loopback interfaces. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a router ospf interface.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 5 interface l3-vlan1
(config-interface-l3-vlan1)# exit
(config-area-0)# interface loopback-1
(config-interface-loopback-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area interface administrative-status`

> **Página:** 784 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the administrative status of an OSPF area interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface interface-name administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* L3 interface. · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the L3 interface. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the administrative status.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 administrative-status down
(config-ospf-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area interface authentication`

> **Página:** 787 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the authentication type for an OSPF interface. Only one type of authentication may be configured.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface interface-name authentication { md5 | none | simple-password } [authentication-key-id key-id]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* N/A
- `interface interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* L3 interface. · *Default:* N/A
- `authentication { md5 | none | simple-password }` — Specifies the type of authentication to be used. — *Valores:* md5, none or simple-password. · *Default:* none.
- `authentication md5 authentication-key-id key-id` — Specifies a key ID for MD5 authentication. This parameter is only available for the MD5 authentication type. — *Valores:* 0-255. · *Default:* 0.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the available authentication types.

```text
# config terminal
Entering configuration mode terminal
(config-ospf-area-intf-l3-if1)# authentication md5 authentication-key-id 1
(config)# commit
(config-ospf-area-intf-l3-if1)# authentication none
(config)# commit
(config-ospf-area-intf-l3-if1)# authentication simple-password
(config)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area interface authentication-key`

> **Página:** 790 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the authentication key for an OSPF interface. This command is only available after an authentication type of MD5 or simple password has been configured.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface interface-name authentication-key key
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* N/A
- `interface interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* L3 interface. · *Default:* N/A
- `authentication-key key` — Specifies the authentication key to be used. — *Valores:* String containing from 2 to 8 characters for simple password authentication, or from 2 to 16 characters for MD5 authentication. · *Default:* Empty string.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure MD5 authentication.

```text
# config terminal
Entering configuration mode terminal
(config-ospf-area-intf-l3-if1)# authentication md5 authentication-key-id 1
(config-ospf-area-intf-l3-if1)# authentication-key abcde
(config)# commit
```

This example shows how to configure simple password authentication.

```text
(config-ospf-area-intf-l3-if1)# authentication simple-password
(config-ospf-area-intf-l3-if1)# authentication-key abcde
(config)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area interface bfd session-type`

> **Página:** 793 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the BFD session type for an L3 interface in OSPF router.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface interface-name bfd session-type type
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* any L3 interface. · *Default:* N/A
- `bfd session-type type` — Configures BFD session-type for this OSPF interface. The none type means BFD is disabled for this OSPF interface. The desired type means BFD is enabled right after the OSPF session establishment and will be used to monitor the session. In case of session type mismatch between the two endpoints, the OSPF may be run on this interface ignoring BFD state. — *Valores:* desired | none · *Default:* none

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.2 | This command was introduced |

**Usage Guidelines:**

Commands to configure the BFD session type. When the BFD session type is configured as desired, the timers min-tx-interval and minrx-interval have both the value of 100ms and the multiplier has a fixed value of 3. Example: This example shows how to configure BFD session type.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100
(config-ospf-area-intf-l3-vlan100-bfd)# session-type desired
(config-ospf-area-intf-l3-vlan100-bfd)# commit
(config-ospf-area-intf-l3-vlan100-bfd)# session-type none
(config-ospf-area-intf-l3-vlan100-bfd)# commit
```

**Impacts and precautions:**

When the session type is changed from desired to none, the OSPF session may flap.

**Hardware restrictions:**

N/A


### `router ospf area interface cost`

> **Página:** 796 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Explicitly sets the OSPF routing cost of a L3 interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface interface-name cost cost
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* any L3 interface. · *Default:* N/A
- `cost cost` — Explicitly sets the OSPF routing cost of a L3 interface. — *Valores:* 1-65535 · *Default:* 1.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the cost. Example: This example shows how to configure the cost.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 cost 2
(config-ospf-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area interface dead-interval`

> **Página:** 799 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures how long the OSPF process will wait before declaring a neighbor down if it stops receiving Hello packets.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface interface-name dead-interval {seconds | minimal fast-hello-multiplier multiplier}
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `dead-interval seconds` — Interval after which a neighbor is declared down. If configured to 1 second, the configured Hello interval will be ignored and the Fast Hello multiplier will be used instead. — *Valores:* 1-65535. · *Default:* 40.
- `dead-interval minimal fast-hello-multiplier multiplier` — Number of Hello packets to be sent per second when dead-interval is configured to 1 second (Fast Hellos). — *Valores:* 3-20. · *Default:* 5.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the dead-interval. Example: This example shows how to configure the dead interval.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 0 interface l3-vlan100
(config-ospf-area-intf-l3-vlan100)# dead-interval 50
(config-ospf-area-intf-l3-vlan100)# commit
(config-ospf-area-intf-l3-vlan100)# dead-interval 1
(config-ospf-area-intf-l3-vlan100)# dead-interval minimal fast-hellomultiplier 3
(config-ospf-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

A mismatch in the OSPF dead-intervals between neighbors will not permit the adjacency to be established or cause it to goes down.

**Hardware restrictions:**

N/A


### `router ospf area interface hello-interval`

> **Página:** 802 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the interval in which Hello packets will be sent.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface interface-name hello-interval seconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `hello-interval seconds` — Sets the interval in which a Hello packet will be sent. — *Valores:* 1-65535. · *Default:* 10.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the hello-interval. Example: This example shows how to configure the Hello interval.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 hello-interval 20
(config-ospf-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

A mismatch in the OSPF hello-intervals between neighbors will not permit the adjacency to be established or cause it to goes down.

**Hardware restrictions:**

N/A


### `router ospf area interface mtu-ignore`

> **Página:** 805 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Disables OSPF Maximum Transmission Unit (MTU) mismatch detection on received Database Description (DBD) packets.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface interface-name mtu-ignore
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* any L3 interface. · *Default:* N/A
- `mtu-ignore` — Sets the interface to ignore the MTU mismatch detection on received DBD packets. — *Valores:* N/A · *Default:* N/A

**Default:** Disabled.

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the mtu-ignore. Example: This example shows how to configure the mtu-ignore.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 mtu-ignore
(config-ospf-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area interface network-type`

> **Página:** 808 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the network type of an OSPF L3 interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface l3-interface-name network-type type
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* N/A
- `interface l3-interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* any L3 interface. · *Default:* N/A
- `network-type type` — Defines the network type to be used for this interface. For broadcast, the interface must be connected to a broadcast network. For point-to-point, the connection is between a single source and a single destination. — *Valores:* broadcast | point-to-point. · *Default:* broadcast.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the network-type. Example: This example shows how to configure the network-type.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 network-type point-to-point
(config-ospf-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area interface passive`

> **Página:** 811 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an OSPF interface as passive. Passive interfaces neither establish adjacencies nor send OSPF updates, but is still advertised as part of the OSPF routing domain.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface interface-name passive
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* any L3 interface. · *Default:* N/A
- `passive` — Defines the interface as passive. — *Valores:* N/A · *Default:* N/A

**Default:** Disabled.

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the passive interface. Example: This example shows how to configure the interface as passive.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 passive
(config-ospf-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area interface router-priority`

> **Página:** 814 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the router priority of an OSPF L3 interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id interface l3-interface-name router-priority priority
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* N/A
- `interface l3-interface-name` — Specifies L3 interface for the OSPF router. The L3 interface must be created before the commit. — *Valores:* any L3 interface. · *Default:* N/A
- `router-priority priority` — Defines the router priority value, which determines the designated router for the specific network. — *Valores:* 0-255. · *Default:* 1.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the router-priority. Example: This example shows how to configure the router-priority.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 router-priority 120
(config-ospf-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area nssa`

> **Página:** 817 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an OSPF area as NSSA (Not-So-Stubby Area).

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id nssa [no-summary | suppress-external | default-information originate]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* N/A
- `nssa` — Defines the OSPF area as NSSA. It is not possible to define the backbone area (area-id 0 or 0.0.0.0) or a stub area as NSSA. — *Valores:* N/A · *Default:* N/A
- `no-summary` — Defines the OSPF area as a totally NSSA. It prevents an Area Border Router (ABR) from sending summary LSAs into the NSSA. — *Valores:* N/A · *Default:* N/A
- `suppress-external` — When the NSSA ABR is also an ASBR, prevents it from originating Type-7 LSAs into the NSSA for redistributed external routes. — *Valores:* N/A · *Default:* N/A
- `default-information originate` — When the NSSA router is an ABR, this parameter will make the router to always originate a Type 7 LSA for the default route into the NSSA area. According to RFC 1587, default routes are necessary because NSSAs do not receive full routing information and must have one to access AS-external destinations. In some cases, the router receives a default route from an external source, and the user wants to advertise this route in NSSA instead of the default route from OSPF. This can be accomplished by disabling this configuration. — *Valores:* N/A · *Default:* Enabled.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure an area as NSSA. Example: This example shows how to configure an area as NSSA.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 1 nssa
(config-nssa)# no-summary
(config-nssa)# suppress-external
(config-nssa)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area range`

> **Página:** 820 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Summarizes routes matching IP address/mask at an area border.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id range ip mask [advertise | not-advertise]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* N/A
- `range ip mask` — Specifies the IP address and mask portion of the range. All inter-area network addresses that match the specified area range are summarized. — *Valores:* N/A · *Default:* N/A
- `ip` — IP address to match. — *Valores:* 0.0.0.0-255.255.255.255. · *Default:* N/A
- `mask` — Netmask to match. — *Valores:* 0.0.0.0-255.255.255.255. · *Default:* N/A
- `advertise` — Advertises the address range. — *Valores:* N/A · *Default:* N/A
- `not-advertise` — Does not advertise the range. — *Valores:* N/A · *Default:* N/A

**Default:** advertise.

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to summarize a route matching address/mask.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 0 range 172.16.0.1 255.255.255.0
(config-area-0)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf area stub`

> **Página:** 823 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an OSPF area as a stub area.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] area area-id stub [no-summary]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `area area-id` — Specifies the OSPF router area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* N/A
- `stub` — Defines the OSPF router area as stub area. It is not possible to define the backbone area (area-id 0 or 0.0.0.0) as a stub area. — *Valores:* N/A · *Default:* N/A
- `no-summary` — Defines the OSPF area as a totally stub area. It prevents an Area Border Router (ABR) from sending summary LSAs into the stub area. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure an area as stub area. Example: This example shows how to configure an area as stub area.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# area 1 stub
(config-stub)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf auto-cost reference-bandwidth`

> **Página:** 826 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This feature enables the OSPF router to automatically determine the cost of a link based on the nominal speed of its L3 interface. This is calculated by dividing the reference bandwidth value by the interface speed. Consequently, links with higher speeds (approaching the reference bandwidth) are assigned lower costs, while slower links are assigned higher costs. It prioritises the fastest paths in the OSPF topology. If the user configures the cost of an L3 interface directly, the user’s value takes priority over the auto-cost feature and will not be overwritten. However, if the user-set cost is subsequently removed while the auto-cost feature is active, the router OSPF will assign the auto-cost value to the interface in its place. The speed of an L3 interface is equal to the speed of the physical interface to which its VLAN is connected. However, if the VLAN is linked to multiple physical interfaces, the speed will be equal to the speed of the slowest physical port. If the L3 interface’s VLAN is linked to a LAG, the speed will be the sum of the speeds of all the LAG’s members. If a VLAN on an L3 interface does not have a configured physical port, the auto-cost calculation will not be applied and the OSPF cost will be set to 1.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] auto-cost reference-bandwidth reference-bandwidth
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `auto-cost reference-bandwidth reference-bandwidth` — The value of the reference bandwidth in Mbit/s that will be used to calculate the auto-cost of the L3 interfaces used in the router OSPF. — *Valores:* 1-4294967 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the auto-cost for a router ospf.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# auto-cost reference-bandwidth 1000000
(config-area-5)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf export-prefix-list`

> **Página:** 829 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the prefix-list to filter prefixes advertisement from route table into OSPF domain.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] export-prefix-list prefix-list-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `export-prefix-list prefix-list-name` — Specifies the prefix-list to be exported. — *Valores:* Name of a prefix list. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to associate the prefix-list named PRX_LIST_EXPORT for export with an OSPF router. This prefix-list must be previously created.

```text
(config)# router ospf 1
(config-ospf-1-vrf-global)# export-prefix-list PRX_LIST_EXPORT
(config-ospf-1-vrf-global)# commit
```

**Impacts and precautions:**

This command only works on the prefixes redistributed by the ASBR into OSPF.

**Hardware restrictions:**

N/A


### `router ospf import-prefix-list`

> **Página:** 831 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the prefix-list to filter the installation of incoming OSPF prefixes on route table.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] import-prefix-list prefix-list-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `import-prefix-list prefix-list-name` — Specifies the prefix-list to be imported. — *Valores:* Name of a prefix-list. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to associate the prefix-list for import named PRX_LIST_IMPORT with an OSPF router. This prefix-list must be previously created.

```text
(config)# router ospf 1
(config-ospf-1-vrf-global)# import-prefix-list PRX_LIST_IMPORT
(config-ospf-1-vrf-global)# commit
```

**Impacts and precautions:**

Note that once a prefix-list is associated to the OSPF router all other prefixes are denied, i.e., they are not installed on HW. But, even if not installed to HW, it does not affect network topology: prefixes are added to OSPF database and are still forwarded to other neighbors.

**Hardware restrictions:**

N/A


### `router ospf max-metric`

> **Página:** 834 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the max-metric advertisement of an OSPF router to overload the configured metric with the maximum possible value(65536) during a pre-determined time after the OSPF process start.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] max-metric advertise router ospf process-id [vrf vrf-name] max-metric include-stub router ospf process-id [vrf vrf-name] max-metric time-to-advertise seconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `advertise` — Enable OSPF to advertise all the non-stub links in its router LSA with the maximum valid value during a specified period or time after the OSPF process start. — *Valores:* N/A · *Default:* N/A
- `include-stub` — Enable OSPF to advertise all the stub links in addition to non-stub links in its router LSA with the maximum valid value during a specified period or time after the OSPF process start. — *Valores:* N/A · *Default:* N/A
- `time-to-advertise seconds` — The amount of time OSPF advertises all the non-stub links in its router LSA with the maximum valid value after OSPF activates. Once this time has passed, the non-stub links will be advertised with their normal metrics. — *Valores:* 1-86400. · *Default:* 600.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.8 | These commands were introduced. |

**Usage Guidelines:**

These commands can be executed directly via CLI. Example: This example shows how to configure the advertise max-metric to 5 minutes.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# advertise-max-metric
(config-ospf-1-vrf-global)# time-to-advertise 300
(config-ospf-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf maximum paths`

> **Página:** 837 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the maximum number of equal-cost multi-paths (ECMP) for each OSPF router process.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] maximum paths number-of-paths
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `maximum paths number-of-paths` — Specifies the maximum number of paths with equal cost. — *Valores:* 1-16. · *Default:* 1.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the maximum number of paths of a router ospf.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# maximum paths 4
(config-ospf-1-vrf-global)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf mpls-te router-id`

> **Página:** 839 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure the MPLS Traffic Engineering (TE) routing protocol parameters.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
router ospf mpls-te router-id interface
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mpls-te router-id interface` — Specifies a loopback interface whose IP address will be used as MPLS TE router identifier. — *Valores:* Any loopback interface redistributed by the OSPF router. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command requires a license to be used. Please contact the support for further information. Example: This example shows how to configure a router ospf mpls-te router-id.

```text
# config terminal
Entering configuration mode terminal
(config)# interface loopback 0
(config-loopback-0)# ipv4 address 200.200.200.1/32
(config-loopback-0)# top
(config)# router ospf 1
(config-ospf-1-vrf-global)# mpls-te router-id loopback-0
(config-ospf-1-vrf-global)# area 0 interface loopback-0
(config-area-0)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf redistribute`

> **Página:** 841 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Redistributes external routes into the domain of this OSPF router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] redistribute {bgp [metric metric-value] | connected | static} [match-address a.b.c.d/x]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `redistribute bgp` — Redistributes BGP routes into the domain of this OSPF router. — *Valores:* N/A · *Default:* N/A
- `redistribute connected` — Redistributes connected routes into the domain of this OSPF router. — *Valores:* N/A · *Default:* N/A
- `redistribute static` — Redistributes static routes, including black-holes, into the domain of this OSPF router. — *Valores:* N/A · *Default:* N/A
- `match-address a.b.c.d/x` — Redistributes specific routes, that match the supplied prefix/mask filter, into the domain of this OSPF router. — *Valores:* Must be a valid IPv4 prefix/mask. · *Default:* N/A
- `metric` — Allows to set the metric that will be carried from BGP process to OSPF process. The default metric value is 1. — *Valores:* 1-16777214. · *Default:* 1.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. Introduced black-hole redistribution with the redistribute static com9.2 mand. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the route redistribution.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# redistribute connected
(config-redistribute-connected)# exit
(config-ospf-1-vrf-global)# redistribute static
(config-redistribute-static)# exit
(config-ospf-1-vrf-global)# redistribute connected match-address 192.168.0.0/24
(config-redistribute-connected)# exit
(config-ospf-1-vrf-global)# redistribute static match-address 10.1.0.0/24
(config-redistribute-static)# commit
```

Example: This example shows how to configure a metric for the redistributed routes from BGP. It allows managing the metric selection criteria in the OSPF database.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# redistribute bgp
(config-redistribute-connected)# metric 1000
(config-redistribute-connected)# exit
(config-ospf-1-vrf-global)# commit
```

**Impacts and precautions:**

Redistributed routes always use metric-type 2 and the metric value is the original value of the external route.

**Hardware restrictions:**

N/A


### `router ospf rfc1583-compatible`

> **Página:** 845 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the router identifier of an OSPF router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] rfc1583-compatible
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `rfc1583-compatible` — The RFC 2328, successor to RFC 1583, suggests a change to the path preference algorithm that prevents routing loops that were possible in the previous recommendation for OSPFv2. More specifically, the intra-area route in a non-backbone area is preferred. The inter-area route and intra-area route in the backbone area have equal preference. RFC 1583 specifies a different method than RFC 2328 for selecting the optimal route to a destination in another AS. When multiple routes are available to the ASBR, all these routes have equal preference, OSPF selects the optimal route by selecting the route with the lower cost. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the rfc1583-compatible of a router ospf.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# rfc1583-compatible
(config-ospf-1-vrf-global)# commit
```

**Impacts and precautions:**

Changing the OSPF rfc1583-compatible will restart the OSPF router process.

**Hardware restrictions:**

N/A


### `router ospf router-id`

> **Página:** 848 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the router identifier of an OSPF router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] router-id id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `router-id id` — Specifies the OSPF router identifier expressed in IPv4 address. — *Valores:* a.b.c.d. · *Default:* 0.0.0.0.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the router-id of a router ospf.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# router-id 1.1.1.1
(config-ospf-1-vrf-global)# commit
```

**Impacts and precautions:**

Changing the OSPF router-id will restart the OSPF router process.

**Hardware restrictions:**

N/A


### `router ospf timers lsa-arrival`

> **Página:** 850 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the minimum interval in which the same link-state advertisement (LSA) from OSPF neighbors is accepted by a router OSPF.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] timers lsa-arrival delay
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `lsa-arrival delay` — Specifies the minimum delay between accepting the same LSA in milliseconds. — *Valores:* 0-600000. · *Default:* 100.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. The default value of parameter lsa-arrival has been changed to 100ms. 4.9 |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a router ospf timers lsa-arrival.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# timers lsa-arrival 5000
(config-timers)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf timers throttle lsa-originate`

> **Página:** 853 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the rate-limiting for link-state advertisement (LSA) generation of a OSPF router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] timers throttle lsa-originate hold-interval interval | max-interval interval | start-interval interval
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `hold-interval interval` — Specifies the minimum delay between originating the same LSA in milliseconds. — *Valores:* 0-600000. · *Default:* 500.
- `max-interval interval` — Specifies the maximum delay between originating the same LSA in milliseconds. — *Valores:* 0-600000. · *Default:* 5000.
- `start-interval interval` — Specifies the start delay to generate the first LSA occurrence in milliseconds. — *Valores:* 0-600000. · *Default:* 100.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. The default values of parameters hold-interval, max-interval and 4.9 start-interval have been changed. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a router ospf timers throttle lsa-originate.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# timers throttle
(config-throttle)# lsa-originate hold-interval 1000
(config-throttle)# lsa-originate max-interval 10000
(config-throttle)# lsa-originate start-interval 500
(config-throttle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospf timers throttle spf`

> **Página:** 856 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the scheduling for Shortest Path First (SPF) calculations of a OSPF router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospf process-id [vrf vrf-name] timers throttle spf hold-interval interval | max-interval interval | start-interval interval
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPF router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPF router. — *Valores:* string. · *Default:* global
- `hold-interval interval` — Specifies the minimum wait time between SPF calculations in milliseconds. — *Valores:* 0-600000. · *Default:* 500.
- `max-interval interval` — Specifies the maximum wait time for SPF calculation in milliseconds. — *Valores:* 0-600000. · *Default:* 5000.
- `start-interval interval` — Specifies the delay between receiving a change to start SPF calculation in milliseconds. — *Valores:* 0-600000. · *Default:* 100.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a router ospf timers throttle spf.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospf 1
(config-ospf-1-vrf-global)# timers throttle
(config-throttle)# spf hold-interval 1000
(config-throttle)# spf max-interval 10000
(config-throttle)# spf start-interval 500
(config-throttle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip ospf`

> **Página:** 859 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about the OSPF routing processes.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
show ip ospf [{brief | detail | extensive} [process-id]]
```

**Parameters:**

- `brief` — Shows summarized information about the routing OSPF processes. — *Valores:* N/A · *Default:* N/A
- `detail` — Shows detailed information about the routing OSPF processes. — *Valores:* N/A · *Default:* N/A
- `extensive` — Shows extensive information about the routing OSPF processes. — *Valores:* N/A · *Default:* N/A
- `process-id` — Shows only information about the specified OSPF process. — *Valores:* 1-65535. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show ip ospf
```

Router-ID Version Admin Op-status Routing-process --------------- ------- ----- --------- --------------- 1.1.1.1 2 up up 1

```text
# show ip ospf brief
```

Router-ID Version Admin Op-status Routing-process --------------- ------- ----- --------- --------------- 1.1.1.1 2 up up 1

```text
# show ip ospf detail
Routing-process: 1;
```

Version: 2; Router-ID: 1.1.1.1; Current router-ID: 1.1.1.1; Area border router: no; Autonomous system border router: enable; Support type-of-service routing: no; Support opaque LSA: yes; Type-5, external LSA: 0; Checksum sum: 0x00000000 Type-11, AS opaque LSA: 0; Checksum sum: 0x00000000 New originated LSA: 231; New instances LSA: 230; LSA with checksum pending: 0; Number pending updates: 0; Number merged updates: 0; Hitless restart status: none; Remaining hitless restart interval: none; Last hitless restart result: none; Advertise-max-metric: disabled; Remaining time(seconds): n/a;

```text
# show ip ospf extensive
Routing-process: 1;
```

Version: 2; Router-ID: 1.1.1.1; Current router-ID: 1.1.1.1; Area border router: no; Autonomous system border router: enable; Support type-of-service routing: no; Support opaque LSA: yes; Type-5, external LSA: 0; Checksum sum: 0x00000000 Type-11, AS opaque LSA: 0; Checksum sum: 0x00000000 New originated LSA: 231; New instances LSA: 230; LSA with checksum pending: 0; Number pending updates: 0; Number merged updates: 0; Hitless restart status: none; Remaining hitless restart interval: none; Last hitless restart result: none; Advertise-max-metric: disabled; Remaining time(seconds): n/a; Number of areas in this router: 1; Normal areas: 1; Stub areas: 0; NSSA areas: 0; Number transit capable areas: 0; Area 0; Op-state: up; Number of interfaces: 1; Authentication: no; Transit capable: no Number of reachable area border routers: 0; Number of reachable autonomous system border routers: 2; Number of times SPF algorithm executed: 3; NSAA translation state: disabled; NSSA state changes: n/a; LSA Type Count Checksum sum -------- ----- ------------ Total LSA 2 0x0000F02A Type-1, router 2 0x0000F02A Type-2, network 0 0x00000000 Type-3, summary 0 0x00000000 Type-4, ASBR 0 0x00000000 Type-7, NSSA 0 0x00000000 Type-10, area opaque 0 0x00000000

**Output Terms:**

Output Description Router-ID Indicates the router identifier of the OSPF routing process. Version Indicates the OSPF protocol version. Admin Indicates the administrative status of the OSPF routing process. Op-status Indicates the operational status of the OSPF routing process. Routing-process Indicates the process identifier of the OSPF routing process.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip ospf database`

> **Página:** 863 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows a set of information related to the OSPF database.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
show ip ospf [process-id [area-id]] database [opaque-area | asbr | network | router | summary] [adv-router adv-router-id | self-originate] [link-state-id] [brief | detail] show ip ospf database external [{brief | detail} [process-id {type-5 | type-11} [link-state-id [adv-router-id]]]]
```

**Parameters:**

- `process-id` — Specifies the Router OSPF process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area-id` — Specifies the Router OSPF area identifier. May be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295 | 0.0.0.0-255.255.255.255. · *Default:* N/A
- `link-state-id` — Shows only information identified by the specified Link State ID. — *Valores:* 0.0.0.0-255.255.255.255. · *Default:* N/A
- `brief` — Shows resumed information about the OSPF database. — *Valores:* N/A · *Default:* N/A
- `detail` — Shows detailed information about the OSPF database. — *Valores:* N/A · *Default:* N/A
- `adv-router adv-router-id` — Shows only information about LSAs advertized by the specified router. — *Valores:* 0.0.0.0-255.255.255.255. · *Default:* N/A
- `opaque-area` — Shows information about opaque area link states. — *Valores:* N/A · *Default:* N/A
- `asbr` — Shows only information about Autonomous System Boundary Router(ASBR) LSAs. — *Valores:* N/A · *Default:* N/A
- `external` — Shows only information about external LSAs. — *Valores:* N/A · *Default:* N/A
- `network` — Shows only information about network LSAs. — *Valores:* N/A · *Default:* N/A
- `router` — Shows only information about router LSAs. — *Valores:* N/A · *Default:* N/A
- `self-originate` — Shows only information about self-originated LSAs (from the local router). — *Valores:* N/A · *Default:* N/A
- `summary` — Shows only information about summary LSAs. — *Valores:* N/A · *Default:* N/A
- `type-5` — Shows only information about Type-5 external LSAs. — *Valores:* N/A · *Default:* N/A
- `type-11` — Shows only information about Type-11 external LSAs. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.0 | The extensive parameter was removed. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples show how to use this command.

```text
# show ip ospf database brief
```

OSPF Router with ID (121.121.121.1) Process ID (1) Area 0.0.0.0; Link type Link ID ADV router Age (secs) Sequence Checksum --------- ------- ---------- ---------- -------- -------- 1 - router 120.120.120.1 120.120.120.1 1000 0x80000002 0x000051F1 1 - router 121.121.121.1 121.121.121.1 999 0x80000002 0x00004FEE

```text
# show ip ospf database detail
```

OSPF Router with ID (121.121.121.1) Process ID (1) Area 0.0.0.0; Link type: router; Link state ID: 120.120.120.1; Advertising router: 120.120.120.1; Age: 1595 secs; Sequence number: 0x80000002; Checksum: 0x000051F1 Advertisement length: 60 (first 58 chars displayed) Advertisement: 0x0001020178787801787878018000000251f1003c0200000379797901ac Options: E Bits: E Links: 3 Router links: 1. Link ID: 121.121.121.1; Link data: 172.16.0.2; Type: 1; Num. of TOS: 0; TOS metric: 1 2. Link ID: 172.16.0.0; Link data: 255.255.255.0; Type: 3; Num. of TOS: 0; TOS metric: 1 3. Link ID: 100.100.100.1; Link data: 255.255.255.255; Type: 3; Num. of TOS: 0; TOS metric: 1 Link state ID: 121.121.121.1; Advertising router: 121.121.121.1; Age: 1595 secs; Sequence number: 0x80000002; Checksum: 0x00004FEE Advertisement length: 60 (first 58 chars displayed) Advertisement: 0x000102017979790179797901800000024fee003c0200000378787801ac Options: E Bits: E Links: 3 Router links: 1. Link ID: 120.120.120.1; Link data: 172.16.0.1; Type: 1; Num. of TOS: 0; TOS metric: 1 2. Link ID: 172.16.0.0; Link data: 255.255.255.0; Type: 3; Num. of TOS: 0; TOS metric: 1 3. Link ID: 101.101.101.1; Link data: 255.255.255.255; Type: 3; Num. of TOS: 0; TOS metric: 1

```text
# show ip ospf database external
```

Link Type Link ID ADV Router Age (secs) Sequence Checksum --------- ------- ---------- ---------- -------- -------- 5 - external 10.10.10.0 2.2.2.2 254 0x80000009 0x00002D77 5 - external 20.20.20.0 2.2.2.2 414 0x80000006 0x0000C3C6

```text
# show ip ospf database external detail
```

Link type: type-5, external; Link ID: 10.10.10.0; Advertising router: 2.2.2.2; Age: 364 secs; Sequence number: 0x80000009; Checksum: 0x00002D77; Advertisement: 0x000102050a0a0a0002020202800000092d770024ffffffff8000000000; Forwarding Address: 0.0.0.0; Metric Type: 2; Metric: 0; Link type: type-5, external; Link ID: 20.20.20.0; Advertising router: 2.2.2.2; Age: 524 secs; Sequence number: 0x80000006; Checksum: 0x0000C3C6; Advertisement: 0x00010205141414000202020280000006c3c60024fffffffe8000000000; Forwarding Address: 0.0.0.0; Metric Type: 2; Metric: 0;

**Output Terms:**

Output Description ADV router Indicates the advertising router. Advertising router Indicates the advertising router. Output Description Advertisement Indicates the LSA in the hex format. Advertisement Indicates the length in bytes of the LSA. length Age Indicates the link state age. Area Indicates the OSPF area ID. Bits Indicates the bits values of the “Options” field. Checksum Indicates the link state checksum. Links Indicate the number of active links. Link data Indicates the router interface address. Link ID Indicates the link ID. Link state ID Indicates the link state ID. Link type Indicates the link type. OSPF Router with Indicates the Router ID. id Options Indicates the optional capabilities. Process ID Indicates the OSPF process ID. Sequence Indicates the link state sequence. Output Description Sequence number Indicates the link state sequence. TOS Indicates the type of service. Type Indicates the link type.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip ospf interface`

> **Página:** 870 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about the OSPF interfaces.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
show ip ospf interface show ip ospf interface brief [ interface-ip [ process-id ]] show ip ospf interface detail [ interface-ip [ process-id ]] show ip ospf interface statistics [ interface-ip [ process-id ]]
```

**Parameters:**

- `brief` — Shows resumed information about the OSPF interfaces. — *Valores:* N/A · *Default:* N/A
- `detail` — Shows detailed information about the OSPF interfaces. — *Valores:* N/A · *Default:* N/A
- `statistics` — Shows various statistics about the OSPF interfaces. — *Valores:* N/A · *Default:* N/A
- `interface-ip` — Shows only information about the specified OSPF interface. — *Valores:* 0.0.0.0-255.255.255.255. · *Default:* N/A
- `process-id` — Shows only information about the specified OSPF process. — *Valores:* 1-65535. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 2.2 | The statistics parameter was updated. |
| 4.6 | The State output was renamed to If-state. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show ip ospf interface
```

Codes for operation state (If-state): BDR - backup designated router; DR - designated router; ODR - other designated router; P2P - point-to-point; DWN - down; LBK - loopback; WTG - waiting Interface-name Area Interface-address If-State --------------- --------------- ----------------- -------- vlan100 0.0.0.0 10.10.10.1 P2P

```text
# show ip ospf interface brief
```

Codes for operation state (If-state): BDR - backup designated router; DR - designated router; ODR - other designated router; P2P - point-to-point; DWN - down; LBK - loopback; WTG - waiting Interface-name Area Interface-address If-state --------------- --------------- ----------------- -------- vlan100 0.0.0.0 10.10.10.1 P2P

```text
# show ip ospf interface detail
```

Interface-name: vlan100; Interface ID: 201326692; Admin state: enabled; MTU: 1500; Operational status: up; OSPF interface state: point-to-point; Link IP address: 10.10.10.1; Mask: 255.255.255.254; Area: 0.0.0.0; Router ID: 1.1.1.1; Network type: point-to-point; Process ID: 1; Instance ID: n/a; Cost: 1; Priority: 1; Designated router: none; Backup designated router: none; Number of OSPF interface state changes or error: 104; LSA count: 0; Checksum: 0x00000000; Timer intervals configured: Hello: 10 secs; Dead: 40 secs; Transit delay: 1 sec; Retransmit: 5 secs;

```text
# show ip ospf interface statistics
ip ospf interface statistics 10.10.10.1 1
rx-invalid 0
rx-invalid-byte 0
rx-hello 1279973
rx-hello-byte 87038156
rx-db-description 10
rx-db-des-byte 700
rx-ls-req 5
rx-ls-req-byte 280
rx-ls-upd 388
rx-ls-upd-byte 37188
rx-ls-ack 388
rx-ls-ack-byte 24832
tx-failed 0
tx-failed-byte 0
tx-hello 1280018
tx-hello-byte 87041200
tx-db-des 13
tx-db-des-byte 856
tx-ls-req 5
tx-ls-req-byte 280
tx-ls-upd 388
tx-ls-upd-byte 37188
tx-ls-ack 388
tx-ls-ack-byte 24832
length 0
checksum 0
version 0
bad-source 0
area-mismatch 0
self-originated 0
duplicate-id 0
hello 103
mtu-mismatch 0
nbr-ignored 0
authentication 0
wrong-protocol 0
resource-err 0
bad-lsa-len 0
lsa-bad-type 0
lsa-bad-len 0
lsa-bad-data 0
lsa-bad-checksum 0
auth-mismatch 0
auth-failure 0
hello-mismatch 102
dead-mismatch 1
options-mismatch 0
packet-local-addr 0
bad-packet 0
```

**Output Terms:**

Output Description Interface-name Indicates the name of the OSPF interface. Area Indicates the area ID of the OSPF interface. Interface-address Indicates the IP address of the OSPF interface. If-state Indicates the state of the OSPF interface. Indicates the number of OSPF packet header ‘area mismatch’ errors area-mismatch detected on each interface. Indicates the number of OSPF packet header authentication errors authentication detected on each interface. Indicates the number of OSPF packets received on each interface auth-failure that were dropped because of authentication failure. Indicates the number of OSPF packets received on each interface auth-mismatch that were dropped because of a bad authentication type. Indicates the number of OSPF LS Update packets received on each bad-lsa-len interface that were discarded because of a bad LSA length. Output Description Indicates the number of OSPF packets received on each interface bad-packet that have been dropped for a reason which does not have a more specific type defined. Indicate the number of OSPF packet header ‘bad source’ errors debad-source tected on each interface. Indicates the number of OSPF packet header checksum errors dechecksum tected on each interface. Indicates the number of OSPF Hello packets received on each interdead-mismatch face that were dropped because of a bad Router Dead Interval. Indicates the number of OSPF packet header ‘duplicate id’ errors duplicate-id detected on each interface. Indicates the number of OSPF packet header ‘Hello’ errors detected hello on each interface. Indicates the number of OSPF Hello packets received on each interhello-mismatch face that were dropped because of a bad Hello Interval. Indicates the number of OSPF packet header length errors detected length on each interface. Indicates the number of OSPF LSAs received on each interface that lsa-bad-checksum were ignored because of a bad LSA checksum value. Indicates the number of OSPF LSAs received on each interface that lsa-bad-data were ignored because of a bad LSA data. Indicates the number of OSPF LSAs received on each interface that lsa-bad-len were ignored because of a bad LSA length. Output Description Indicates the number of OSPF LSAs received on each interface that lsa-bad-type were ignored because of a bad LSA type. Indicates the number of OSPF packet header ‘MTU mismatch’ errors mtu-mismatch detected on each interface. Indicates the number of OSPF packet header ‘neighbor ignored’ ernbr-ignored rors detected on each interface. Indicates the number of OSPF Hello packets received on each interoptions-mismatch face that were dropped because of bad Optional Capabilities. Indicates the number of OSPF Hello packets received on each interpacket-local-addr face that were dropped because they appear to come from the local router. Indicates the number of OSPF packet header resource errors deresource-err tected on each interface. Indicates the number of bytes received in OSPF Database Descriprx-db-des-byte tion packets on each interface. Indicates the number of OSPF Database Description packets rerx-db-description ceived on each interface. Indicates the number of OSPF Hello packets received on each interrx-hello face. Indicates the number of bytes received in OSPF Hello packets on rx-hello-byte each interface. Indicates the number of OSPF packets with an invalid type field rerx-invalid ceived on each interface. Output Description Indicates the number of bytes received in OSPF packets with an inrx-invalid-byte valid type field on each interface. Indicates the number of OSPF LS Acknowledgement packets received rx-ls-ack on each interface. Indicates the number of bytes received in OSPF LS Acknowledgerx-ls-ack-byte ment packets on each interface. Indicates the number of OSPF LS Request packets received on each rx-ls-req interface. Indicates the number of bytes received in OSPF LS Request packets rx-ls-req-byte on each interface. Indicates the number of OSPF LS Update packets received on each rx-ls-upd interface. Indicates the number of bytes received in OSPF LS Update packets rx-ls-upd-byte on each interface. Indicates the number of OSPF packet header ‘self-originated’ errors self-originated detected on each interface. Indicates the number of OSPF Database Description packets sent on tx-db-des each interface. Indicates the number of bytes sent in OSPF Database Description tx-db-des-byte packets on each interface. Indicates the number of packets that OSPF could not send on each tx-failed interface. Indicates the number of bytes sent in packets that OSPF could not tx-failed-byte send on each interface. Output Description tx-hello Indicates the number of OSPF Hello packets sent on each interface. Indicates the number of bytes sent in OSPF Hello packets on each tx-hello-byte interface. Indicates the number of OSPF LS Acknowledgement packets sent on tx-ls-ack each interface. Indicates the number of bytes sent in OSPF LS Acknowledgement tx-ls-ack-byte packets on each interface. Indicates the number of OSPF LS Request packets sent on each intx-ls-req terface. Indicates the number of bytes sent in OSPF LS Request packets on tx-ls-req-byte each interface. Indicates the number of OSPF LS Update packets sent on each intertx-ls-upd face. Indicates the number of bytes sent in OSPF LS Update packets on tx-ls-upd-byte each interface. Indicates the number of OSPF packet header version errors detected version on each interface. Indicates the number of OSPF packet header ‘wrong protocol’ errors wrong-protocol detected on each interface.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ip ospf neighbor`

> **Página:** 879 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about the OSPF neighbors.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
show ip ospf neighbor show ip ospf neighbor brief [Router-ID [process-id]] show ip ospf neighbor detail [Router-ID [process-id]]
```

**Parameters:**

- `brief` — Shows resumed information about the OSPF neighbors. — *Valores:* N/A · *Default:* N/A
- `detail` — Shows detailed information about the OSPF neighbors. — *Valores:* N/A · *Default:* N/A
- `Router-ID` — Shows only information about the specified OSPF neighbor. — *Valores:* 0.0.0.0-255.255.255.255. · *Default:* N/A
- `process-id` — Shows only information about the specified OSPF process. — *Valores:* 1-65535. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |
| 4.6 | The interface state output was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show ip ospf neighbor
```

State codes: atmpt - attempt; exchg - exchange; exst - exchange start; load - loading; 2-way - two-way; Neighbor interface state codes: BDR - backup designated router; DR - designated router; ODR - other designated router; P2P - point-to-point; Neighbor-ID Pri State If-state Interface-address Interface-name --------------- --- ----- -------- ----------------- -------------- 2.2.2.2 1 full BDR 10.10.10.0 vlan100

```text
# show ip ospf neighbor brief
```

State codes: atmpt - attempt; exchg - exchange; exst - exchange start; load - loading; 2-way - two-way; Neighbor interface state codes: BDR - backup designated router; DR - designated router; ODR - other designated router; P2P - point-to-point; Neighbor-ID Pri State If-State Interface-address Interface-name --------------- --- ----- -------- ----------------- -------------- 2.2.2.2 1 full BDR 10.10.10.0 vlan100

```text
# show ip ospf neighbor detail
Neighbor-ID: 2.2.2.2; Interface-address: 10.10.10.0;
Area: 0.0.0.0; Interface-name: vlan100;
```

Relationship state with neighbor: full; Oper status: up; Neighbor interface state: backup designated router; Neighbor priority: 1; Options: 0x42; Re-transmission queue length: 0; Number of neighbor relationship state changes or error: 6; Permanence: dynamic; Hello suppressed: no; Requested LSAs: 0; Dead timer due in: 00:00:37 (hrs:mins:secs); Hitless restart status: not helping; Remaining hitless restart interval: none; Hitless restart result: none;

```text
# show ip ospf neighbor detail 10.10.10.0
Neighbor-ID: 2.2.2.2; Interface-address: 10.10.10.0;
Area: 0.0.0.0; Interface-name: vlan100;
```

Relationship state with neighbor: full; Oper status: up; Neighbor interface state: backup designated router; Neighbor priority: 1; Options: 0x42; Re-transmission queue length: 0; Number of neighbor relationship state changes or error: 6; Permanence: dynamic; Hello suppressed: no; Requested LSAs: 0; Dead timer due in: 00:00:31 (hrs:mins:secs); Hitless restart status: not helping; Remaining hitless restart interval: none; Hitless restart result: none;

```text
# show ip ospf neighbor detail 10.10.10.0 1
Neighbor-ID: 2.2.2.2; Interface-address: 10.10.10.0;
Area: 0.0.0.0; Interface-name: vlan100;
```

Relationship state with neighbor: full; Oper status: up; Neighbor interface state: backup designated router; Neighbor priority: 1; Options: 0x42; Re-transmission queue length: 0; Number of neighbor relationship state changes or error: 6; Permanence: dynamic; Hello suppressed: no; Requested LSAs: 0; Dead timer due in: 00:00:36 (hrs:mins:secs); Hitless restart status: not helping; Remaining hitless restart interval: none; Hitless restart result: none;

**Output Terms:**

Output Description Neighbor-ID Indicates the router ID value of the OSPF neighbor router-ID. Pri Indicates the priority value of the OSPF neighbor. State Indicates the adjacency state with the OSPF neighbor. If-state Indicates the interface state of the OSPF neighbor. Interface-address Indicates the interface address of the OSPF neighbor. Interface-name Indicates the interface name of the OSPF neighbor.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A OSPFV3 This topic describes the commands related to management of OSPFv3 topologies such as commands to configure the OSPFv3 parameters or to inspect the protocol status.


## OSPFv3

### `clear ospfv3`

> **Página:** 883 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Clears OSPFv3 information.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
clear ospfv3 process process-id
```

**Parameters:**

- `process process-id` — Clears OSPFv3 information for the specified OSPFv3 process ID. — *Valores:* 1-65535. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to clear OSPFv3 process.

```text
# clear ospfv3 process 1
```

**Impacts and precautions:**

This command will restart all OSPFv3 adjacencies from the specified router instance.

**Hardware restrictions:**

N/A


### `router ospfv3`

> **Página:** 885 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an OSPFv3 router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure an OSPFv3 router.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1
(config-ospfv3-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 administrative-status`

> **Página:** 887 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the administrative status of an OSPFv3 router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the OSPFv3 router. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the administrative status.

```text
# config
Entering configuration mode terminal
(config)# router ospfv3 1 administrative-status down
(config-ospfv3-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 advertise-max-metric`

> **Página:** 889 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the max-metric advertisement of an OSPFv3 router to overload the configured metric with the maximum possible value(65536) during a pre-determined time after the OSPFv3 process start.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4920.

**Syntax:**

```text
router ospfv3 process-id [vrf vrf-name] max-metric advertise router ospfv3 process-id [vrf vrf-name] max-metric include-stub router ospfv3 process-id [vrf vrf-name] max-metric time-to-advertise seconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the OSPFv3 router process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this router will be associated with. The VRF ‘global’ is implied if no parameter is specified. It is not possible to associate the VRF ‘mgmt’ with an OSPFv3 router. — *Valores:* string. · *Default:* global
- `advertise` — Enable OSPFv3 to advertise all the non-stub links in its router LSA with the maximum valid value during a specified period or time after the OSPFv3 process start. — *Valores:* N/A · *Default:* N/A
- `include-stub` — Enable OSPFv3 to advertise all the stub links in addition to non-stub links in its router LSA with the maximum valid value during a specified period or time after the OSPFv3 process start. — *Valores:* N/A · *Default:* N/A
- `time-to-advertise seconds` — The amount of time OSPFv3 advertises all the non-stub links in its router LSA with the maximum valid value after OSPFv3 activates. Once this time has passed, the non-stub links will be advertised with their normal metrics. — *Valores:* 1-86400. · *Default:* 600.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 9.8 | These commands were introduced. |

**Usage Guidelines:**

These commands can be executed directly via CLI.v3 Example: This example shows how to configure the advertise max-metric to 5 minutes.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1
(config-ospfv3-1-vrf-global)# advertise-max-metric
(config-ospfv3-1-vrf-global)# time-to-advertise 300
(config-ospfv3-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 area`

> **Página:** 892 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the area of a router OSPFv3.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area-id` — Specifies the Router OSPFv3 area identifier. May be specified in decimal or in dot-decimal notation. — *Valores:* 1-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a router ospfv3 area.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1 area 5
(config-area-5)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 area administrative-status`

> **Página:** 894 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the administrative status of an OSPFv3 area.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area area-id` — Specifies the Router OSPFv3 area identifier. May be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `administrative-status status` — Activates (up) or deactivates (down) the OSPFv3 area. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the administrative status.

```text
# config
Entering configuration mode terminal
(config)# router ospfv3 1 area 0 administrative-status down
(config-area-0)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 area interface`

> **Página:** 896 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Enables the OSPFv3 protocol on an specified L3 or loopback interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id interface interface-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area-id` — Specifies the Router OSPFv3 area identifier. May be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface-name` — Specifies L3 and loopback interfaces for the Router OSPFv3. The L3 and loopback interfaces must be created before the commit. — *Valores:* Any L3 and loopback interfaces. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a router ospfv3 interface.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1 area 5 interface l3-vlan1
(config-interface-l3-vlan1)# top
(config)# router ospfv3 1 area 5 interface loopback-1
(config-interface-loopback-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 area interface administrative-status`

> **Página:** 898 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the administrative status of an OSPFv3 area interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id interface interface-name administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area area-id` — Specifies the Router OSPFv3 area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the Router OSPFv3. The L3 interface must be created before the commit. — *Valores:* L3 interface. · *Default:* N/A
- `administrative-status status` — Activates (up) or deactivates (down) the L3 interface. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the administrative status.

```text
# config
Entering configuration mode terminal
(config)# router ospfv3 1 area 0
(config-area-0)# interface l3-vlan100 administrative-status down
(config-ospfv3-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 area interface cost`

> **Página:** 901 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Explicitly sets the OSPFv3 routing cost of an L3 interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id interface interface-name cost cost
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area area-id` — Specifies the Router OSPFv3 area identifier. May be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the Router OSPFv3. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `cost cost` — Explicitly sets the OSPFv3 routing cost of an L3 interface. — *Valores:* 1-65535 · *Default:* 1.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the cost. Example: This example shows how to configure the cost.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1 area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 cost 2
(config-ospfv3-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 area interface dead-interval`

> **Página:** 904 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures how long the OSPFv3 process will wait before declaring a neighbor down if it stops receiving Hello packets.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id interface interface-name dead-interval seconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area area-id` — Specifies the Router OSPFv3 area identifier. May be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the Router OSPFv3. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `dead-interval seconds` — Interval after which a neighbor is declared down. — *Valores:* 2-65535. · *Default:* 40.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the dead-interval. Example: This example shows how to configure the dead interval.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1 area 0 interface l3-vlan100
(config-interface-l3-vlan100)# dead-interval 50
(config-interface-l3-vlan100)# commit
```

**Impacts and precautions:**

A mismatch in the OSPFv3 dead-intervals between neighbors will not permit the adjacency to be established or cause it to goes down.

**Hardware restrictions:**

N/A


### `router ospfv3 area interface hello-interval`

> **Página:** 907 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the interval in which Hello packets will be sent.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id interface interface-name hello-interval seconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area area-id` — Specifies the Router OSPFv3 area identifier. May be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the Router OSPFv3. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `hello-interval seconds` — Sets the interval in which a Hello packet will be sent. — *Valores:* 1-65535. · *Default:* 10.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the hello-interval. Example: This example shows how to configure the Hello interval.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1 area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 hello-interval 20
(config-interface-l3-vlan100)# commit
```

**Impacts and precautions:**

A mismatch in the OSPFv3 hello-intervals between neighbors will not permit the adjacency to be established or cause it to goes down.

**Hardware restrictions:**

N/A


### `router ospfv3 area interface mtu-ignore`

> **Página:** 910 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Disables OSPFv3 Maximum Transmission Unit (MTU) mismatch detection on received Database Description (DBD) packets.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id interface interface-name mtu-ignore
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area area-id` — Specifies the Router OSPFv3 area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies L3 interface for the Router OSPFv3. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `mtu-ignore` — Sets the interface to ignore the MTU mismatch detection on received DBD packets. — *Valores:* N/A · *Default:* N/A

**Default:** Disabled.

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the mtu-ignore. Example: This example shows how to configure the mtu-ignore.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1 area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 mtu-ignore
(config-ospfv3-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 area interface network-type`

> **Página:** 913 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the network type of an OSPFv3 L3 interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id interface l3-interface-name network-type type
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area area-id` — Specifies the Router OSPFv3 area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* N/A
- `interface l3-interface-name` — Specifies L3 interface for the Router OSPFv3. The L3 interface must be created before the commit. — *Valores:* any L3 interface. · *Default:* N/A
- `network-type type` — Defines the network type to be used for this interface. For pointto-point, the connection is between a single source and a single destination. — *Valores:* point-to-point. · *Default:* point-to-point.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced |

**Usage Guidelines:**

Commands to configure the network-type. Example: This example shows how to configure the network-type.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1 area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 network-type point-to-point
(config-ospfv3-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 area interface passive`

> **Página:** 916 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an OSPFv3 interface as passive.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id interface interface-name passive
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area area-id` — Specifies the Router OSPFv3 area identifier. It may be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* 0.
- `interface interface-name` — Specifies an L3 interface for the Router OSPFv3. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `passive` — Sets the interface as passive. — *Valores:* N/A · *Default:* N/A

**Default:** Disabled.

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced |

**Usage Guidelines:**

Passive interfaces neither establish adjacencies nor send OSPFv3 updates, but it is still advertised as part of the OSPFv3 routing domain. Commands to configure the passive interface. Example: This example shows how to configure the interface as passive.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1 area 0.0.0.0
(config-area-0.0.0.0)# interface l3-vlan100 passive
(config-ospfv3-area-intf-l3-vlan100)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 area range`

> **Página:** 919 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Summarizes routes matching IPv6 address/prefix length at an area border.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id area area-id range x:x:x:x::x/y [advertise | not-advertise]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area area-id` — Specifies the Router OSPFv3 area identifier. May be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295. 0.0.0.0-255.255.255.255. · *Default:* N/A
- `range x:x:x:x::x/y` — Specifies the IPv6 network portion of the range. All inter-area network addresses that match the specified area range are summarized. — *Valores:* Must be a valid IPv6 network address and prefix length. · *Default:* N/A
- `advertise` — Advertises the address range. — *Valores:* N/A · *Default:* N/A
- `not-advertise` — Does not advertise the range. — *Valores:* N/A · *Default:* N/A

**Default:** advertise.

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to summarize a route matching address/prefix length.

```text
# config
Entering configuration mode terminal
(config)# router ospfv3 1 area 0 range 2001:db8::/64
(config-range-2001:db8::/64)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 maximum paths`

> **Página:** 922 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the maximum number of equal-cost multi-paths (ECMP) for the OSPFv3 router process.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id maximum paths number-of-paths
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `maximum paths number-of-paths` — Specifies the maximum number of paths with equal cost. — *Valores:* 1-16. · *Default:* 1.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the maximum number of paths of a router ospfv3.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1
(config-ospfv3-1)# maximum paths 4
(config-ospfv3-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 redistribute`

> **Página:** 924 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Redistributes external routes into the domain of this OSPFv3 router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id redistribute {connected | static} [match-address x:x:x:x::x/x]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `redistribute connected` — Redistributes connected routes into the domain of this OSPFv3 router. — *Valores:* N/A · *Default:* N/A
- `redistribute static` — Redistributes static routes, including black-holes, into the domain of this OSPFv3 router. — *Valores:* N/A · *Default:* N/A
- `match-address x:x:x:x::x/x` — Redistributes specific routes, that match the supplied prefix/mask filter, into the domain of this OSPFv3 router. — *Valores:* Must be a valid IPv6 prefix/mask. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. Introduced black-hole redistribution with the redistribute static com9.2 mand. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the route redistribution.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1 redistribute connected
(config-redistribute-connected)# top
(config)# router ospfv3 1 redistribute static
(config-redistribute-static)# top
(config)# router ospfv3 1 redistribute connected match-address 2001:db8::/64
(config-redistribute-connected)# top
(config)# router ospfv3 1 redistribute static match-address 2001:db8::/64
(config-redistribute-static)# commit
```

**Impacts and precautions:**

Redistributed routes always use metric-type 2 and the metric value is the original value of the external route.

**Hardware restrictions:**

N/A


### `router ospfv3 router-id`

> **Página:** 927 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the router identifier of an OSPFv3 router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id router-id id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `router-id id` — Specifies the Router OSPFv3 identifier expressed in IPv4 address. — *Valores:* a.b.c.d. · *Default:* 0.0.0.0.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the router-id of a router ospfv3.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1 router-id 1.1.1.1
(config-ospfv3-1)# commit
```

**Impacts and precautions:**

Changing the OSPFv3 router-id will restart the OSPFv3 router process.

**Hardware restrictions:**

N/A


### `router ospfv3 timers lsa-arrival`

> **Página:** 929 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the minimum interval in which the same link-state advertisement (LSA) from OSPFv3 neighbors is accepted by a router OSPFv3.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id timers lsa-arrival milliseconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `lsa-arrival` — Specifies the minimum delay between accepting the same LSA in milliseconds. — *Valores:* 0-600000. · *Default:* 100.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. The default value of parameter lsa-arrival has been changed to 100ms. 4.9 |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a router ospfv3 timers lsa-arrival.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1
(config-ospfv3-1)# timers lsa-arrival 5000
(config-timers)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 timers throttle lsa-originate`

> **Página:** 931 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the rate-limiting for link-state advertisement (LSA) generation of a router OSPFv3.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id timers throttle lsa-originate hold-interval milliseconds | max-interval milliseconds | start-interval milliseconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `hold-interval` — Specifies the minimum delay between originating the same LSA in milliseconds. — *Valores:* 0-600000. · *Default:* 500.
- `max-interval` — Specifies the maximum delay between originating the same LSA in milliseconds. — *Valores:* 0-600000. · *Default:* 5000.
- `start-interval` — Specifies the start delay to generate the first LSA occurrence in milliseconds. — *Valores:* 0-600000. · *Default:* 100.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. The default values of parameters hold-interval, max-interval and 4.9 start-interval have been changed. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a router ospf timers throttle lsa-originate.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1
(config-ospfv3-1)# timers throttle
(config-throttle)# lsa-originate hold-interval 1000
(config-throttle)# lsa-originate max-interval 10000
(config-throttle)# lsa-originate start-interval 500
(config-throttle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router ospfv3 timers throttle spf`

> **Página:** 934 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the scheduling for Shortest Path First (SPF) calculations of a router OSPFv3.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router ospfv3 process-id timers throttle spf hold-interval milliseconds | max-interval milliseconds | start-interval milliseconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `hold-interval` — Specifies the minimum wait time between SPF calculations in milliseconds. — *Valores:* 0-600000. · *Default:* 500.
- `max-interval` — Specifies the maximum wait time for SPF calculation in milliseconds. — *Valores:* 0-600000. · *Default:* 5000.
- `start-interval` — Specifies the delay between receiving a change to start SPF calculation in milliseconds. — *Valores:* 0-600000. · *Default:* 100.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a router ospfv3 timers throttle spf.

```text
# config terminal
Entering configuration mode terminal
(config)# router ospfv3 1
(config-ospfv3-1)# timers throttle
(config-throttle)# spf hold-interval 1000
(config-throttle)# spf max-interval 10000
(config-throttle)# spf start-interval 500
(config-throttle)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ipv6 ospf`

> **Página:** 937 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about the OSPFv3 routing processes.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show ipv6 ospf [brief [process-id]]
```

**Parameters:**

- `brief` — Shows summarized information about the routing OSPFv3 processes. — *Valores:* N/A · *Default:* N/A
- `process-id` — Shows only information about the specified OSPFv3 process. — *Valores:* 1-65535. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show ipv6 ospf
```

Router-ID Version Admin Op-status Routing-process --------------- ------- ----- --------- --------------- 1.1.1.1 3 up up 1

```text
# show ipv6 ospf brief
```

Router-ID Version Admin Op-status Routing-process --------------- ------- ----- --------- --------------- 1.1.1.1 3 up up 1

**Output Terms:**

Output Description Router-ID Indicates the router identifier of the OSPFv3 routing process. Version Indicates the OSPFv3 protocol version. Output Description Admin Indicates the administrative status of the OSPFv3 routing process. Op-status Indicates the operational status of the OSPFv3 routing process. Routing-process Indicates the process identifier of the OSPFv3 routing process.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ipv6 ospf database`

> **Página:** 940 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows a set of information related to the OSPFv3 database.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show ipv6 ospf [process-id [area-id]] database [inter-area-prefix | inter-arearouter | intra-area-prefix | router] [adv-router adv-router-id | self-originate] [link-state-id] [brief | detail] show ipv6 ospf database external [{brief | detail} [process-id]] show ipv6 ospf database link [{brief | detail} [process-id]]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `process-id` — Specifies the Router OSPFv3 process identifier. — *Valores:* 1-65535. · *Default:* N/A
- `area-id` — Specifies the Router OSPFv3 area identifier. May be specified in decimal or in dot-decimal notation. — *Valores:* 0-4294967295 | 0.0.0.0-255.255.255.255. · *Default:* N/A
- `inter-area-prefix` — Shows only information about inter-area prefix LSAs. — *Valores:* N/A · *Default:* N/A
- `inter-area-router` — Shows only information about inter-area router LSAs. — *Valores:* N/A · *Default:* N/A
- `intra-area-prefix` — Shows only information about intra-area prefix LSAs. — *Valores:* N/A · *Default:* N/A
- `router` — Shows only information about router LSAs. — *Valores:* N/A · *Default:* N/A
- `adv-router adv-router-id` — Shows only information about LSAs advertised by the specified router. — *Valores:* 0.0.0.0-255.255.255.255. · *Default:* N/A
- `self-originate` — Shows only information about self-originated LSAs (from the local router). — *Valores:* N/A · *Default:* N/A
- `link-state-id` — Shows only information identified by the specified Link State ID. — *Valores:* 0.0.0.0-255.255.255.255. · *Default:* N/A
- `brief` — Shows resumed information about the OSPFv3 database. — *Valores:* N/A · *Default:* N/A
- `detail` — Shows detailed information about the OSPFv3 database. — *Valores:* N/A · *Default:* N/A
- `external` — Shows only information about external LSAs. — *Valores:* N/A · *Default:* N/A
- `link` — Shows only information about link LSAs. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

These commands can be executed directly via CLI. Example: These examples show how to use show commands for OSPFv3 database information.

```text
# show ipv6 ospf database brief
```

Codes: IA - inter area, iA - intra area, net - network, prf - prefix, rtr - router, TE - traffic-engineering OSPF Router with ID (1.1.1.3) Process ID (1) Area 0.0.0.1; Link type Link ID ADV router Age (secs) Sequence Checksum --------- ------- ---------- ---------- -------- -------- 0x2001-router 0.0.0.0 1.1.1.2 547 0x8000000B 0x0000015D 0x2001-router 0.0.0.0 1.1.1.3 546 0x80000002 0x0000F374 0x2003-IA prf 0.0.0.1 1.1.1.2 460 0x80000008 0x0000B26E 0x2004-IA rtr 0.0.0.1 1.1.1.2 446 0x80000008 0x00001401 0x2009-iA prf 0.0.0.1 1.1.1.2 547 0x8000000F 0x00008DD0 0x2009-iA prf 0.0.0.1 1.1.1.3 546 0x80000002 0x00008B79

```text
# show ipv6 ospf database detail
```

OSPF Router with ID (1.1.1.2) Process ID (1) Area 0.0.0.0; Link type: router; Link state ID: 0.0.0.0; Advertising router: 1.1.1.1; Age: 747 secs; Sequence number: 0x8000028B; Checksum: 0x00005A4D Advertisement length: 40 (first 58 chars displayed) Advertisement: 0x0001200100000000010101018000028b5a4d002802000013010000010c Options: R, E, V6 Bits: E Number of interfaces: 1 Interfaces: 1. Interface-ID: 201326692; Neighbor interface-ID: 201326692; Neighbor router-ID: 1.1.1.2; Type: 1; Metric: 1 Link state ID: 0.0.0.0; Advertising router: 1.1.1.2; Age: 752 secs; Sequence number: 0x800000C3; Checksum: 0x0000D699 Advertisement length: 40 (first 58 chars displayed) Advertisement: 0x000120010000000001010102800000c3d699002803000013010000010c Options: R, E, V6 Bits: E, B Number of interfaces: 1 Interfaces: 1. Interface-ID: 201326692; Neighbor interface-ID: 201326692; Neighbor router-ID: 1.1.1.1; Type: 1; Metric: 1 Area 0.0.0.0; Link type: inter-area-prefix; Link state ID: 0.0.0.1; Advertising router: 1.1.1.2; Age: 752 secs; Sequence number: 0x800000BD; Checksum: 0x0000C344 Advertisement length: 36 (first 58 chars displayed) Advertisement: 0x000120030000000101010102800000bdc3440024000000014000000020 Address prefix: 2005:600::/64; Metric: 1; Prefix Options: None Link state ID: 0.0.0.36; Advertising router: 1.1.1.2; Age: 1690 secs; Sequence number: 0x80000003; Checksum: 0x0000ABF6 Advertisement length: 36 (first 58 chars displayed) Advertisement: 0x00012003000000240101010280000003abf60024000000024000000020 Address prefix: 2005:200::/64; Metric: 2; Prefix Options: None Link state ID: 0.0.0.37; Advertising router: 1.1.1.2; Age: 1690 secs; Sequence number: 0x80000003; Checksum: 0x00003655 Advertisement length: 40 (first 58 chars displayed) Advertisement: 0x0001200300000025010101028000000336550028000000025000000020 Address prefix: 2005:202::/80; Metric: 2; Prefix Options: None Area 0.0.0.0; Link type: inter-area-router; Link state ID: 0.0.0.18; Advertising router: 1.1.1.2; Age: 1690 secs; Sequence number: 0x80000003; Checksum: 0x00008F77 Advertisement length: 32 (first 58 chars displayed) Advertisement: 0x000120040000001201010102800000038f770020000000130000000101 Destination router ID: 1.1.1.3; Metric: 1; Options: R, E, V6 Area 0.0.0.0; Link type: intra-area-prefix; Link state ID: 0.0.0.1; Advertising router: 1.1.1.2; Age: 752 secs; Sequence number: 0x800000C3; Checksum: 0x00000A24 Advertisement length: 52 (first 58 chars displayed) Advertisement: 0x000120090000000101010102800000c30a240034000120010000000001 Referenced LS type: router Referenced LS ID: 0.0.0.0 Referenced advertising router: 1.1.1.2 Number of prefixes: 1 Prefixes: 1. Address prefix: 2005:555::1/128; Metric: 0; Prefix Options: LA

```text
# show ipv6 ospf database external brief
```

Link Type Link ID ADV Router Age (secs) Sequence Checksum --------- ------- ---------- ---------- -------- -------- 0x4005-AS-ext 0.0.0.1 200.200.200.1 11 0x80000001 0x00001F33

```text
# show ipv6 ospf database external detail
```

Link type: AS-external; Link ID: 0.0.0.1; Advertising router: 200.200.200.1; Age: 77 secs; Sequence number: 0x80000001; Checksum: 0x00001F33; Advertisement: 0x0001400500000001c8c8c801800000011f33; Address Prefix: 2001:100::/64; Forwarding Address: n/a; Metric: 0; Metric Type: 1; Prefix Options: None;

```text
# show ipv6 ospf database link
```

Link ID ADV Router Age (secs) Sequence Checksum ------- ---------- ---------- -------- -------- 12.0.0.100 200.200.200.1 74 0x80000001 0x0000FB0C 0.0.0.100 200.200.200.2 72 0x80000001 0x00003D44

```text
# show ipv6 ospf database link detail 1
```

Link type: link; Link ID: 12.0.0.200; Advertising router: 1.1.1.2; Area ID: 0.0.0.1; Interface IP address: n/a; Interface index: 201326792; Age: 1328 secs; Sequence number: 0x8000000B; Checksum: 0x0000E377; Advertisement length: 128; (first 58 chars displayed..) Advertisement: 0x053000080c0000c8010101028000000be37701bc01000013fe80000000; Router priority: 1 Options: R, E, V6 Link-local Interface Address: fe80::801:9ff:fec5:100 Number of prefixes: 20 Prefixes: 1. Address prefix: 2005:919::3/128; Prefix Options: LA 2. Address prefix: 2005:918::3/128; Prefix Options: LA 3. Address prefix: 2005:917::3/128; Prefix Options: LA 4. Address prefix: 2005:916::3/128; Prefix Options: LA 5. Address prefix: 2005:915::3/128; Prefix Options: LA 6. Address prefix: 2005:914::3/128; Prefix Options: LA 7. Address prefix: 2005:913::3/128; Prefix Options: LA 8. Address prefix: 2005:912::3/128; Prefix Options: LA 9. Address prefix: 2005:911::7/128; Prefix Options: LA 10. Address prefix: 2005:810::7/128; Prefix Options: LA 11. Address prefix: 2005:809::7/128; Prefix Options: LA 12. Address prefix: 2005:808::7/128; Prefix Options: LA 13. Address prefix: 2005:707::7/128; Prefix Options: LA 14. Address prefix: 2005:706::2/128; Prefix Options: LA 15. Address prefix: 2005:705::2/128; Prefix Options: LA 16. Address prefix: 2005:604::2/128; Prefix Options: LA (First 16 prefixes displayed) Link type: link; Link ID: 12.0.0.200; Advertising router: 1.1.1.3; Area ID: 0.0.0.1; Interface IP address: n/a; Interface index: 201326792; Age: 62 secs; Sequence number: 0x80000001; Checksum: 0x0000A79C; Advertisement length: 128; (first 58 chars displayed..) Advertisement: 0x003d00080c0000c80101010380000001a79c005401000013fe80000000; Router priority: 1 Options: R, E, V6 Link-local Interface Address: fe80::801:9ff:fe00:100 Number of prefixes: 2 Prefixes: 1. Address prefix: 2005:202::5/128; Prefix Options: LA 2. Address prefix: 2005:200::1/128; Prefix Options: LA

**Output Terms:**

Output Description Address prefix Indicates the IPv6 address prefix. Age Indicates the link state age. ADV router Indicates the advertising router. Advertisement Indicates in the hex format the LSA. Advertisement Indicates the length in bytes of the LSA. length Output Description Advertising router Indicates the advertising router. Area Indicates the OSPFv3 area ID. Indicates the bits that represent various router roles within the Bits OSPFv3 domain. Checksum Indicates the link state checksum. Destination Indicates the router-ID of the destination router. Router-ID Forwarding Address Indicates the forwarding address. Interface-ID Indicates the local interface ID. Interface index Indicates the local interface index. Interface IP Indicates the interface IPv6 address. address Link ID Indicates the link ID. Link-local Indicates the originating router’s link-local interface address. Interface Address Link state ID Indicates the link state ID. Link type Indicates the link type. Metric Indicates the link metric. Output Description Neighbor Indicates the remote neighbor interface ID. interface-ID Neighbor router-ID Indicates the router-ID from the neighbor router. Number of Indicates the number of OSPFv3 interfaces on the router. interfaces Number of prefixes Indicates the number of prefixes present into the LSA. Options Indicates the optional capabilities. OSPFv3 Router with Indicates the Router-ID. ID Prefix options Indicates the prefix optional capabilities. Process ID Indicates the OSPFv3 process ID. Referenced advertising router Indicates the originating router-ID. Referenced LS ID Indicates the link state ID. Referenced LS Type Indicates the type of LSA to which these prefixes are associated with. Router priority Indicates the router priority. Sequence Indicates the link state sequence. Output Description Sequence number Indicates the link state sequence number. Type Indicates the link type.

**Impacts and precautions:**

Only first 16 prefixes are displayed in database link show. The full prefixes list can be viewed in the intra-area LSAs using the show ipv6 ospf database detail command.

**Hardware restrictions:**

N/A


### `show ipv6 ospf neighbor`

> **Página:** 949 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about the OSPFv3 neighbors.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
show ipv6 ospf neighbor show ipv6 ospf neighbor brief [Router-ID] show ipv6 ospf neighbor detail [Router-ID]
```

**Parameters:**

- `brief` — Shows resumed information about the OSPFv3 neighbors. — *Valores:* N/A · *Default:* N/A
- `detail` — Shows detailed information about the OSPFv3 neighbors. — *Valores:* N/A · *Default:* N/A
- `Router-ID` — Shows only information about the specified OSPFv3 neighbor. — *Valores:* 0.0.0.0-255.255.255.255. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show ipv6 ospf neighbor
```

State codes: atmpt - attempt; exchg - exchange; exst - exchange start; load - loading; 2-way - two-way; Neighbor-ID Pri State Interface-address Interface-name --------------- --- ----- ------------------------- -------------- 10.10.10.2 1 full fe80::204:dfff:fe5c:1089 vlan100

```text
# show ipv6 ospf neighbor brief
```

State codes: atmpt - attempt; exchg - exchange; exst - exchange start; load - loading; 2-way - two-way; Neighbor-ID Pri State Interface-address Interface-name --------------- --- ----- ------------------------- -------------- 10.10.10.2 1 full fe80::204:dfff:fe5c:1089 vlan100

```text
# show ipv6 ospf neighbor detail
Neighbor-ID: 10.10.10.2; Interface-address: fe80::204:dfff:fe5c:1089;
Area: 0.0.0.0; Interface-name: vlan100;
```

Relationship state with neighbor: full; Oper status: up; Neighbor priority: 1; Options: 0x13; Re-transmission queue length: 0; Number of neighbor relationship state changes or error: 6; Hello suppressed: no; Requested LSAs: 0; Dead timer due in: 00:00:35 (hrs:mins:secs); Hitless restart status: not helping; Remaining hitless restart interval: none; Hitless restart result: none;

**Output Terms:**

Output Description Neighbor-ID Indicates the router ID value of the OSPFv3 neighbor router-ID. Pri Indicates the priority value of the OSPFv3 neighbor. State Indicates the adjacency state with the OSPFv3 neighbor. Interface-address Indicates the interface address of the OSPFv3 neighbor. Interface-name Indicates the interface name of the OSPFv3 neighbor.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A VRRP This topic describes the commands related to management of VRRP topologies such as commands to configure the VRRP parameters or to inspect the protocol status.


## VRRP

### `router vrrp`

> **Página:** 952 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a VRRP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp
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

This command can be executed directly via CLI. Example: This example shows how to configure a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router vrrp interface`

> **Página:** 954 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures VRRP on a L3 interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Currently it is supported up to 32 protected L3 interfaces. i.e 32 instances of VRRP. Example: This example shows how to configure VRRP in a L3 interface.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router vrrp interface address-family`

> **Página:** 956 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures VRRP for an address family.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name address-family {ipv4 | ipv6}
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `address-family {ipv4 | ipv6}` — Specifies the address family for which VRRP will be enabled on this interface. — *Valores:* IPv4 or IPv6. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure VRRP for an address family.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# address-family ipv4
(config-vrrp-if-address-family)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router vrrp interface address-family vr-id`

> **Página:** 958 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the virtual router identifier for a VRRP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name address-family {ipv4 | ipv6} vr-id id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `address-family {ipv4 | ipv6}` — Specifies the address family for which VRRP will be enabled on this interface. — *Valores:* IPv4 or IPv6. · *Default:* N/A
- `vr-id id` — Specifies the virtual router identifier. — *Valores:* 1-255. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure VR-ID for a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# address-family ipv4
(config-vrrp-if-address-family)# vr-id 10
(config-vrrp-if-address-family)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router vrrp interface address-family vr-id address`

> **Página:** 960 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a virtual address for a VRRP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name address-family {ipv4 | ipv6} vr-id id address { a.b.c.d | x:x:x:x::x | link-local { auto-configuration | x:x:x:x::x } }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `address-family { ipv4 | ipv6 }` — Specifies the address family for which VRRP will be enabled on this interface. — *Valores:* IPv4 or IPv6. · *Default:* N/A
- `vr-id id` — Specifies the virtual router identifier. — *Valores:* 1-255. · *Default:* N/A
- `address { a.b.c.d | x:x:x:x::x }` — Specifies an IPv4 or IPv6 address to be a virtual address for this VRRP router. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* N/A
- `address link-local { auto-configuration | x:x:x:x::x }` — Configures automatically the virtual IPv6 64-bit Extended Unique Identifier link-local address obtained through VRRP MAC address or specifies an IPv6 link-local address to be a virtual address for this VRRP router. — *Valores:* x:x:x:x::x. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Configuring the virtual IPv6 link-local address is mandatory to enable VRRP with IPv6 address family, and this command will be available only for this address family. Examples: This example shows how to configure virtual IPv4 address for a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# address-family ipv4
(config-vrrp-if-address-family)# vr-id 10
(config-vrrp-if-address-family-10)# address 10.10.10.1
(config-vrrp-if-address-family-10)# commit
```

This example shows how to configure virtual IPv6 link-local address and virtual IPv6 address for a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan101
(config-vrrp-if)# address-family ipv6
(config-vrrp-if-address-family)# vr-id 11
(config-vrrp-if-address-family-11)# address link-local auto-configuration
(config-vrrp-if-address-family-11)# address 2001:db8::1
(config-vrrp-if-address-family-11)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router vrrp interface address-family vr-id administrative-status`

> **Página:** 963 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status of a VRRP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name address-family {ipv4 | ipv6} vr-id id administrative-status status
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `address-family {ipv4 | ipv6}` — Specifies the address family for which VRRP will be enabled on this interface. — *Valores:* IPv4 or IPv6. · *Default:* N/A
- `vr-id id` — Specifies the virtual router identifier. — *Valores:* 1-255. · *Default:* N/A
- `administrative-status status` — Activate (up) or deactivate (down) the VRRP router. — *Valores:* up | down. · *Default:* up.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the administrative status for a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# address-family ipv4
(config-vrrp-if-address-family)# vr-id 10
(config-vrrp-if-address-family-10)# administrative-status down
(config-vrrp-if-address-family-10)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router vrrp interface address-family vr-id advertisement-interval`

> **Página:** 966 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the advertisement interval for a VRRP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name address-family {ipv4 | ipv6} vr-id id advertisement-interval interval
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `address-family {ipv4 | ipv6}` — Specifies the address family for which VRRP will be enabled on this interface. — *Valores:* IPv4 or IPv6. · *Default:* N/A
- `vr-id id` — Specifies the virtual router identifier. — *Valores:* 1-255. · *Default:* N/A
- `advertisement-interval interval` — Specifies a maximum advertisement interval value between advertisement messages, in seconds, sent by this VRRP router. — *Valores:* 1-40. · *Default:* 1.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the advertisement interval for a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# address-family ipv4
(config-vrrp-if-address-family)# vr-id 10
(config-vrrp-if-address-family-10)# advertisement-interval 40
(config-vrrp-if-address-family-10)# commit
```

**Impacts and precautions:**

Low maximum advertisement interval will generate messages at a high rate and may affect bandwidth throughput.

**Hardware restrictions:**

N/A


### `router vrrp interface address-family vr-id authentication`

> **Página:** 969 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the authentication of a VRRP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name address-family {ipv4 | ipv6} vr-id id authentication simple-text password
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `address-family {ipv4 | ipv6}` — Specifies the address family for which VRRP will be enabled on this interface. — *Valores:* IPv4 or IPv6. · *Default:* N/A
- `vr-id id` — Specifies the virtual router identifier. — *Valores:* 1-255. · *Default:* N/A
- `authentication simple-text password` — Specify a simple text password authentication for the VRRP router. — *Valores:* Simple text password. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the simple text password authentication for a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# address-family ipv4
(config-vrrp-if-address-family)# vr-id 10
(config-vrrp-if-address-family-10)# authentication simple-text test123
(config-vrrp-if-address-family-10)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router vrrp interface address-family vr-id preempt`

> **Página:** 972 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the preemption for a VRRP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name address-family {ipv4 | ipv6} vr-id id preempt preempt
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `address-family {ipv4 | ipv6}` — Specifies the address family for which VRRP will be enabled on this interface. — *Valores:* IPv4 or IPv6. · *Default:* N/A
- `vr-id id` — Specifies the virtual router identifier. — *Valores:* 1-255. · *Default:* N/A
- `preempt preempt` — Controls whether a higher-priority Backup router preempts a lower-priority Master router. — *Valores:* true | false. · *Default:* true.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the preemption for a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# address-family ipv4
(config-vrrp-if-address-family)# vr-id 10
(config-vrrp-if-address-family-10)# preempt false
(config-vrrp-if-address-family-10)# commit
```

**Impacts and precautions:**

To minimize unnecessary service disruptions, in both versions of VRRP (v2 and v3), a backup non-owner virtual router will not preempt a master virtual router with same priority, as stated by RFC 3768 and RFC 5798. The evaluation of routers primary IP Address on an election process will only happen when a master non-owner virtual router receives an advertisement with same priority, therefore must be two or more master non-owner virtual routers.

**Hardware restrictions:**

N/A


### `router vrrp interface address-family vr-id priority`

> **Página:** 975 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the priority for a VRRP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name address-family {ipv4 | ipv6} vr-id id priority priority
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `address-family {ipv4 | ipv6}` — Specifies the address family for which VRRP will be enabled on this interface. — *Valores:* IPv4 or IPv6. · *Default:* N/A
- `vr-id id` — Specifies the virtual router identifier. — *Valores:* 1-255. · *Default:* N/A
- `priority priority` — Specifies a priority value to be advertised by this VRRP router during Master election. — *Valores:* 1-254. · *Default:* 100.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Priority value of 255 will be automatically assigned to the VRRP router address owner. Example: This example shows how to configure the priority for a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# address-family ipv4
(config-vrrp-if-address-family)# vr-id 10
(config-vrrp-if-address-family-10)# priority 150
(config-vrrp-if-address-family-10)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router vrrp interface address-family vr-id track`

> **Página:** 978 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the track interface of a VRRP router.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name address-family {ipv4 | ipv6} vr-id id track {interface l3-interface-name | decrement decrement-priority}
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `address-family {ipv4 | ipv6}` — Specifies the address family for which VRRP will be enabled on this interface. — *Valores:* IPv4 or IPv6. · *Default:* N/A
- `vr-id id` — Specifies the virtual router identifier. — *Valores:* 1-255. · *Default:* N/A
- `track decrement decrement-priority` — Specifies the value to decrement priority by when all tracked interfaces are operationally down. — *Valores:* 1-253. · *Default:* 50.
- `track interface l3-interface-name` — Specifies L3 interfaces to track their operational state. — *Valores:* Any L3 interface. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Track feature only acts decrementing priority if VRRP router is not the address owner. Priority will be decremented only if all tracked L3 interfaces are operationally down. Example: This example shows how to configure the track interface and decrement for a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# address-family ipv4
(config-vrrp-if-address-family)# vr-id 10
(config-vrrp-if-address-family-10)# track decrement 60
(config-vrrp-if-address-family-10)# track interface l3-uplink1
(config-vrrp-if-address-family-10)# track interface l3-uplink2
(config-vrrp-if-address-family-10)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `router vrrp interface address-family vr-id version`

> **Página:** 981 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the VRRP router protocol version.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
router vrrp interface l3-interface-name address-family {ipv4 | ipv6} vr-id id version vrrp-version
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies an L3 interface in which VRRP will be enabled. The L3 interface must be created before the commit. — *Valores:* Any L3 interface. · *Default:* N/A
- `address-family {ipv4 | ipv6}` — Specifies the address family for which VRRP will be enabled on this interface. — *Valores:* IPv4 or IPv6. · *Default:* N/A
- `vr-id id` — Specifies the virtual router identifier. — *Valores:* 1-255. · *Default:* N/A
- `version vrrp-version` — Specifies the virtual router protocol version. — *Valores:* v2 | v3. · *Default:* v3.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This this command will be available only for IPv4 address family. Examples: This example shows how to configure protocol version for a VRRP router.

```text
(config)# router vrrp
(config-vrrp)# interface l3-vlan100
(config-vrrp-if)# address-family ipv4
(config-vrrp-if-address-family)# vr-id 10
(config-vrrp-if-address-family-10)# version v2
(config-vrrp-if-address-family-10)# commit
```

**Impacts and precautions:**

Changing the VRRP router protocol version will restart the VRRP router process.

**Hardware restrictions:**

N/A PBR This topic describes the commands related to management of PBR topologies such as commands to configure the PBR parameters or to inspect the protocol status.


## PBR

### `router pbr`

> **Página:** 984 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create policy-based rules that are applied before the normal layer 3 routing. Also allows enforcing the L3 routing as a rule exception.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4360, DM4370, DM4376, DM4378, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
router pbr id [ priority { rule_priority } description { description_string } match { source ipv4-address ipv4/mask } match { destination ipv4-address ipv4/mask } match { interface interface-name . . . } action { l3-routing | next-hop ipv4 } ]
```

**Parameters:**

- `id` — The PBR rule id. Up to 64 rules can be configured. — *Valores:* 1-64 · *Default:* N/A
- `priority rule_priority` — The PBR rule priority. Lower values have higher priority. Must be unique between all PBR rules. Priority is a mandatory configuration. — *Valores:* 0-255 · *Default:* N/A
- `description description_string` — The PBR rule description. A user field to help identify the rule meaning. Enclose the content in double quotes for multi word description. — *Valores:* string up to 32 characters. · *Default:* N/A
- `match source ipv4-address ipv4/mask` — A PBR rule match for source IPv4 host or subnet address. Any packet with source IP (or masked range) that matches with the configured one will be forwarded by the PBR rule. For a single IP match, the mask can be ommited. At least one match type (source, destination or interface) must be provided. — *Valores:* A.B.C.D[/mask] IPv4 host or subnet address · *Default:* N/A
- `match destination ipv4-address ipv4/mask` — A PBR rule match for destination IPv4 host or subnet address. Any packet with destination IP (or range) that matches with the configured one will be forwarded by the PBR rule. For a single IP match, the mask can be ommited. At least one match type (source, destination or interface) must be provided. — *Valores:* A.B.C.D[/mask] IPv4 host or subnet address · *Default:* N/A
- `match interface interface-name . . .` — A PBR rule match for input interface names. Any packet that enters the switch trough any of the named interfaces will be forwarded by the PBR rule. Several interfaces can be configured in the rule. At least one match type (source, destination or interface) must be provided. — *Valores:* interface-type-chassis/slot/port - The interface name. Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, gpon · *Default:* N/A
- `action l3-routing` — A PBR rule action that overrides another PBR rule, by enforcing the use of the L3-routing. This can be used to add an exception to a much broader rule. This kind of exception must have a higher priority than the rule it is meant to override. Only one action type (l3-routing, next-hop) must be provided. — *Valores:* none · *Default:* N/A
- `action next-hop ipv4` — A PBR rule action that forwards all matched traffic to an specific host. Only one action type (l3-routing, next-hop) must be provided. — *Valores:* A.B.C.D IPv4 host · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.10 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a PBR rule for: • “Client X” • With priority 10 • For packets that enter through interfaces gigabit-ethernet-1/1/1 and 1/1/2 • Comming from IPs 10.0.0.1 to 10.0.0.254 • That will be forwarded to 172.22.16.10

```text
(config)# router pbr 1
(config-pbr-1)# priority 10
(config-pbr-1)# description "Client X"
(config-pbr-1)# match interface gigabit-ethernet-1/1/1 gigabit-ethernet-1/1/2
(config-pbr-1)# match source ipv4-address 10.0.0.0/24
(config-pbr-1)# action next-hop 172.22.16.10
(config-pbr-1)# commit
```

Example: This example adds an exception to the role 1: • “Client X” • With priority 5 • For packets that enter through interfaces gigabit-ethernet-1/1/1 and 1/1/2 • Comming from IP 10.0.0.15 • That will be forwarded by L3 routing

```text
(config)# router pbr 2
(config-pbr-2)# priority 5
(config-pbr-2)# description "Client X3 exception"
(config-pbr-2)# match interface gigabit-ethernet-1/1/1 gigabit-ethernet-1/1/2
(config-pbr-2)# match source ipv4-address 10.0.0.15
(config-pbr-2)# action l3-routing
(config-pbr-2)# commit
```

Example: This example adds another rule, now with destination match: • “Client Z” • With priority 20 • For packets that enter through any interface • Destinated to IP 172.20.100.100 • That will be forwarded to 172.20.0.1

```text
(config)# router pbr 3
(config-pbr-3)# priority 20
(config-pbr-3)# description "Client Z"
(config-pbr-3)# match destination ipv4-address 172.20.100.100
(config-pbr-3)# action next-hop 172.20.0.1
(config-pbr-3)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show router pbr`

> **Página:** 989 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display information about Policy-based routes status and configuration. When ommited the rule-id, the show displays all configured rules status.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4360, DM4370, DM4376, DM4378, DM4611, DM4612, DM4616, DM4618, DM4920.

**Syntax:**

```text
show router pbr [ rule-id ]
```

**Parameters:**

- `rule-id` — The rule id whose status is desired to show. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.12 | This command was introduced. |

**Usage Guidelines:**

Given the equipment has a PBR configuration. A show will present:

```text
# show router pbr
Match Match Action Hardware
```

ID Priority Source IP Dest. IP Match Interface Next-Hop Status Description --------------------------------------------------------------------------------------------------------- 1 1 - 3.3.3.3/24 gigabit-ethernet-1/1/1 1.1.1.1 installing - hundred-gigabit-ethernet-1/1/1 2 40 2.2.2.1 - gigabit-ethernet-1/1/3 2.2.1.1 installed Client X 3 10 1.1.1.1 - - l3-routing pending IPTV 4 5 2.2.2.2 - - l3-routing pending -

```text
#
</code> <newline>
```

When the rule id is specified:

```text
# show router pbr 1
Match Match Action Hardware
```

ID Priority Source IP Dest. IP Match Interface Next-Hop Status Description --------------------------------------------------------------------------------------------------------- 1 1 - 3.3.3.3/24 gigabit-ethernet-1/1/1 1.1.1.1 installing - hundred-gigabit-ethernet-1/1/1

```text
#
```

**Output Terms:**

Output Description ID The PBR rule Id. Priority The Priority of the rule. Lower values are applied first. The Source IP that should match (in the packets) to the rule be enMatch Source IP forced. Match Destination The Destination IP that should match (in the packets) to the rule be IP enforced. Output Description The Inbound interface(s) that should match (in the packets) to the Match Interface rule be enforced. The action that will be applied to the packet: Action Next-hop -Redirect to a configured IP address; -Proceed with l3-routing. Informs if the rule is installed and effective in the hardware: -Pending: The configured next-hop is not available or the rule pends installation; Hardware Status -Installing: The rule is being installed and will be available soon; -Installed: The rule is installed and will be enforced on any matched packet. Description The rule description as configured by the user.

**Impacts and precautions:**

None

**Hardware restrictions:**

None VRF This topic describes the commands related to management of VRF topologies such as commands to configure the VRF parameters or to inspect the protocol status.


## VRF

### `vrf`

> **Página:** 992 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Creates a VRF.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
vrf vrf-name [ description vrf-description ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vrf-name` — Specifies the name of the VRF. Only accepts alphanumeric characters, ‘_’ and ‘-’. — *Valores:* string (length 1 - 32). · *Default:* N/A
- `description vrf-description` — Specifies the description of the VRF. It may point out a more meaningful text about its purpose. — *Valores:* string (length 1 - 32). · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 4.4 | The description parameter was introduced. |

**Usage Guidelines:**

Use the vrf command to create a new virtual routing forwarding instance for the system. There are two VRFs already created, global is the default VRF and mgmt is a VRF dedicated to out-of-band management interface. Neither of them cahttps://gerrit.ped.datacom.net.br/159428n be changed or deleted. Example: This example shows how to configure a new VRF named “green” for the system.

```text
(config)# vrf green
(config)# commit
```

Commit complete.

**Impacts and precautions:**

The overall number of available VRFs includes both the system’s reserved global and mgmt. The word all is reserved for VRF filter purposes, thus no VRF named all can be created.

**Hardware restrictions:**

The following platforms support only the system VRFs global and mgmt: • DM4050 • DM4340 • DM4610 • DM4611 • DM4612 • DM4615 • DM4616 • DM4618 • DM4920


### `vrf address-family ipv4 unicast`

> **Página:** 995 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Creates an address-family associated with VRF.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
vrf vrf-name address-family { ipv4 } unicast
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vrf-name` — Specifies the name of the VRF. Only accepts alphanumeric characters, ‘_’ and ‘-’. — *Valores:* string (length 1 - 32). · *Default:* N/A
- `address-family { ipv4 }` — Selects the address family identifier (AFI). — *Valores:* ipv4. IPv4 address family. · *Default:* N/A
- `unicast` — Selects the subsequent address family identifier (SAFI). — *Valores:* unicast. IPv4 unicast routes. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.2 | This command was introduced. |
| 7.0 | This command was removed. |

**Usage Guidelines:**

This command can be executed directly via CLI. This example shows how to configure an address-family ipv4 unicast in the VRF.

```text
(config)# vrf green address-family ipv4 unicast
(config-address-family-ipv4/unicast)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `vrf rd`

> **Página:** 997 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Creates a route distinguisher.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
vrf vrf-name rd { ASN:nn | IPv4:nn }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vrf-name` — Specifies the name of the VRF. Only accepts alphanumeric characters, ‘_’ and ‘-’. Note: VRFs used in L3VPN must have up to 31 characters. — *Valores:* string (length 1 - 31). · *Default:* N/A
- `rd { ASN:nn | IPv4:nn }` — Specifies the VRF route distinguisher. — *Valores:* ASN:nn or IPv4:nn format. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.2 | This command was introduced. |

**Usage Guidelines:**

Use the rd command in order to associate a route distinguisher with a VRF. Example: This example shows how to configure a new route distinguisher in ASN:nn format.

```text
(config)# vrf green rd 65000:1000
(config-vrf-green)# commit
```

This example shows how to configure a new route distinguisher in IPv4:nn format.

```text
(config)# vrf green rd 10.20.2.3:1000
(config-vrf-green)# commit
```

**Impacts and precautions:**

Route distinguisher must be unique in the system. The VRFs global and mgmt do not support route distinguisher configuration.

**Hardware restrictions:**

N/A


### `vrf route-target`

> **Página:** 999 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a route target to be exported or imported.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4340, DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
vrf vrf-name route-target { export | import } route-target-number
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vrf-name` — Specifies the name of the VRF. Only accepts alphanumeric characters, ‘_’ and ‘-’. Note: VRFs used in L3VPN must have up to 31 characters. — *Valores:* string (length 1 - 31). · *Default:* N/A
- `route-target export` — Selects the route target to be exported from this VRF. — *Valores:* N/A · *Default:* N/A
- `route-target import` — Selects the route target to be imported to this VRF. — *Valores:* N/A · *Default:* N/A
- `route-target-number` — Specifies the route target. — *Valores:* ASN:nn or IPv4:nn format. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.2 | This command was introduced. |
| 7.0 | The address-family option was removed. |

**Usage Guidelines:**

A route distinguisher must be previously associated with this VRF. This example shows how to configure a route target in ASN:nn format to be exported. ((config-vrf-red))# route-target export 1:2

```text
(config-route-target-export/1:2)# commit
```

This example shows how to configure a route target in ASN:nn format to be imported. ((config-vrf-red))# route-target import 1:4

```text
(config-route-target-import/1:4)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A CHAPTER 7: MPLS This chapter describes the commands related to management of MPLS topologies in the DmOS CLI. MPLS features are available under specific license control. Please contact the Technical Support for further information. INFRA This topic describes the commands related to management of basic MPLS infrastructure such as commands to configure MPLS generic behavior parameters.
