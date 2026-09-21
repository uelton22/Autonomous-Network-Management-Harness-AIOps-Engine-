# Capítulo 18: VXLAN Commands

> Fonte: `doc_huawei_datacom/huawei` · Huawei VRP Issue 14 (2021-10-20) · S1720, S2700, S5700, and S6720 Series Ethernet Switches

## VXLAN Configuration Commands

18.1 VXLAN Configuration Commands 18.1.1 Command Support 18.1.2 arp static bridge-domain 18.1.3 arp static vni 18.1.4 bridge-domain (Layer 2 sub-interface view) 18.1.5 bridge-domain (system view) 18.1.6 broadcast-suppression (BD view) 18.1.7 description (BD view) 18.1.8 display bridge-domain 18.1.9 display bridge-domain statistics 18.1.10 display interface nve 18.1.11 display interface vbdif 18.1.12 display mac-address bridge-domain 18.1.13 display snmp-agent trap feature-name adpvxlan all 18.1.14 display vxlan peer 18.1.15 display vxlan statistics 18.1.16 display vxlan tunnel 18.1.17 display vxlan vni 18.1.18 encapsulation (Layer 2 sub-interface view) 18.1.19 interface nve 18.1.20 interface vbdif 18.1.21 l2 binding vlan 18.1.22 multicast-suppression (BD view) 18.1.23 mac-address static bridge-domain 18.1.24 mac-address static bridge-domain vni 18.1.25 reset bridge-domain statistics 18.1.26 reset vxlan statistics 18.1.27 service type vxlan-tunnel 18.1.28 set vxlan resource super-mode 18.1.29 snmp-agent trap enable feature-name adpvxlan 18.1.30 source (NVE interface view) 18.1.31 statistics enable (BD view) 18.1.32 undo mac-address bridge-domain 18.1.33 unknown-unicast-suppression (BD view) 18.1.34 vni head-end peer-list 18.1.35 vxlan statistics enable 18.1.36 vxlan vni (BD view) Only the S5720HI, S6720S-EI, and S6720EI support VXLAN.

### `arp static bridge-domain`

> **Página:** 2 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The arp static bridge-domain command configures a static ARP entry on an interface of a VXLAN network. The undo arp static bridge-domain command deletes a static ARP entry configured on an interface of a VXLAN network. By default, no static ARP entry is configured on an interface of a VXLAN network.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
arp static ip-address mac-address bridge-domain bd-id [ vid vlan-id1 [ cevid
vlan-id2 ] ] interface interface-type interface-number.subnum
undo arp static ip-address mac-address bridge-domain bd-id [ vid vlan-id1
[ cevid vlan-id2 ] ] interface interface-type interface-number.subnum
arp static ip-address mac-address bridge-domain bd-id [ vid vlan-id3 ] interface
interface-type interface-number
undo arp static ip-address mac-address bridge-domain bd-id [ vid vlan-id3 ]
interface interface-type interface-number
```

**Parameters:**

- `ip-address` — Specifies a destination IP address. — *Valores:* The value is in dotted decimal notation.
- `mac-address` — Specifies the destination MAC address mapping the destination IP address. — *Valores:* The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits.
- `bd-id` — Specifies a BD ID. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super-mode command is used to set the super VXLAN resource mode.
- `vid vlan-id1` — Specifies the outer VLAN ID in the packet received by a sub-interface. — *Valores:* The value is an integer that ranges from 1 to 4094.
- `cevid vlan-id2` — Specifies the inner VLAN ID in the packet received by a sub-interface. — *Valores:* The value is an integer that ranges from 1 to 4094.
- `interface interface- type interface- number.subnum` — Specifies an sub- interface. — *Valores:* -
- `vid vlan-id3` — Specifies the VLAN ID in the packet received by a interface. — *Valores:* The value is an integer that ranges from 1 to 4094.
- `interface interface- type interface- number` — Specifies an nterface. — *Valores:* -

**Usage Guidelines:**

**Usage Scenario**

Static ARP entries are manually configured and maintained. They will not be aged out or overridden by dynamic ARP entries. Therefore, you can run the arp static bridge-domain command on an interface of a VXLAN network to configure static ARP entries to increase communication security. Static ARP entries enable the local device and a specified device to communicate with each other using only specified MAC addresses. Attackers cannot modify mappings between IP addresses and MAC addresses in static ARP entries.

**Prerequisites**

The outbound interface has been added to a VLAN and bound to a BD.

**Precautions**

- If a static ARP entry already exists, the new configuration cannot be delivered.

- The specified ip-address must be in the same network segment as the outbound interface address in the ARP entry.

- To specify the vid vlan-id and cevid vlan-id parameters, set the same encapsulation type as that on the interface first.

- When you configure a static ARP entry on an interface of the S6720EI and S6720S-EI, you must configure a static MAC address entry for the MAC address in the ARP entry. Otherwise, the switch will broadcast traffic from this MAC address.

**Example:**

```text
# On the outbound interface GE0/0/1, configure a static ARP entry with the IP
```

address and MAC address 10.1.1.2 and aaaa-fccc-1212, respectively.

```text
<HUAWEI> system-view
[HUAWEI] vlan 10
[HUAWEI-vlan10] quit
[HUAWEI] interface GigabitEthernet 0/0/1
[HUAWEI-GigabitEthernet0/0/1] port link-type trunk
[HUAWEI-GigabitEthernet0/0/1] port trunk allow-pass vlan 10
[HUAWEI-GigabitEthernet0/0/1] quit
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] l2 binding vlan 10
[HUAWEI-bd10] quit
[HUAWEI] interface vbdif 10
[HUAWEI-Vbdif10] ip address 10.1.1.1 255.255.255.0
[HUAWEI-Vbdif10] quit
[HUAWEI] arp static 10.1.1.2 aaaa-fccc-1212 bridge-domain 10 vid 10 interface GigabitEthernet 0/0/1
```


### `arp static vni`

> **Página:** 4 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The arp static vni command configures a static ARP entry for a VXLAN tunnel. The undo arp static vni command deletes a static ARP entry of a VXLAN tunnel. By default, no static ARP entry is configured for a VXLAN tunnel.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
arp static ip-address mac-address vni vni-id source-ip ip-address peer-ip ip-address
undo arp static ip-address mac-address vni vni-id source-ip ip-address peer-ip ip-address
```

**Parameters:**

- `ip-address` — Specifies a destination IP address. — *Valores:* The value is in dotted decimal notation.
- `mac-address` — Specifies the destination MAC address mapping the destination IP address. — *Valores:* The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits.
- `vni-id` — Specifies the VNI ID. — *Valores:* The value is an integer that ranges from 1 to 16777215.
- `source-ip ip- address` — Specifies the IP address of the source VTEP. — *Valores:* The value is in dotted decimal notation.
- `peer-ip ip- address` — Specifies the IP address of the destination VTEP. — *Valores:* The value is in dotted decimal notation.

**Usage Guidelines:**

**Usage Scenario**

Static ARP entries are manually configured and maintained. They will not be aged out or overridden by dynamic ARP entries. Running the arp static vni command on a device to configure static ARP entries for a VXLAN tunnel increases communication security. Static ARP entries enable the local device and a specified device to communicate with each other using only specified MAC addresses. Attackers cannot modify mappings between IP addresses and MAC addresses in static ARP entries.

**Prerequisites**

A VXLAN tunnel and a Layer 3 gateway have been configured.

**Precautions**

- If a static ARP entry already exists, the new configuration cannot be delivered.

- The specified IP address must be in the same network segment as the outbound interface address in the ARP entry.

**Example:**

```text
# Configure a static ARP entry for a VXLAN tunnel that maps the IP address
```

10.0.0.2 to the MAC address aaaa-fccc-1212.

```text
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] vxlan vni 5000
[HUAWEI-bd10] quit
[HUAWEI] interface vbdif 10
[HUAWEI-Vbdif10] ip address 10.0.0.10 255.255.255.0
[HUAWEI-Vbdif10] quit
[HUAWEI] interface nve 1
[HUAWEI-Nve1] source 10.1.1.1
[HUAWEI-Nve1] vni 5000 head-end peer-list 10.2.2.2
[HUAWEI-Nve1] quit
[HUAWEI] arp static 10.0.0.2 aaaa-fccc-1212 vni 5000 source-ip 10.1.1.1 peer-ip 10.2.2.2
```


### `bridge-domain (Layer 2 sub-interface view)`

> **Página:** 6 · **Views (Modo):** Layer 2 sub-interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The bridge-domain command associates a Layer 2 sub-interface with a BD. The undo bridge-domain command restores the default settings. By default, no Layer 2 sub-interface is associated with a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
bridge-domain bd-id
undo bridge-domain [ bd-id ]
```

**Parameters:**

- `bd-id` — Specifies the ID of the BD that is associated with a Layer 2 sub- interface. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super- mode command is used to set the super VXLAN resource mode.

**Usage Guidelines:**

**Usage Scenario**

VXLAN needs to be deployed on a downlink interface to provide access services and an uplink interface to establish a VXLAN tunnel. On the access side, two methods are available for creating a large Layer 2 BD.

- Based on VLAN: You can associate one or multiple VLANs with a BD to add users in these VLANs to the BD. This VLAN-based mode implements largergranularity control, but is easy to configure. It applies to VXLAN deployment on a live network.

- Based on encapsulation mode: The device sends packets of different encapsulation modes to different Layer 2 sub-interfaces based on the VLAN tags contained in the packets. You can bind a Layer 2 sub-interface to a BD to add specified users to the BD. This mode implements refined and flexible control but requires more complex configuration. It applies to VXLAN deployment on a new network. To create a BD based on encapsulation mode, create a Layer 2 sub-interface first. Then run the encapsulation (Layer 2 sub-interface view) command to configure a supported encapsulation mode on the sub-interface. After you run the bridge-domain (Layer 2 sub-interface view) command to associate a Layer 2 sub-interface with a BD, packets containing the same VLAN tag from different LANs can communicate at Layer 2.

**Prerequisites**

- Run the command 18.1.5 bridge-domain (system view) to create the BD.

- Run the command interface to create the Layer 2 VXLAN sub-interface.

**Precautions**

One Layer 2 sub-interface can be associated with only one BD. For the BD that bind to the Layer 2 sub-interfaces which use dot1q encapsulation, the VBDIF interface of this BD cannot be created on the device.

**Example:**

```text
# Associate Layer 2 sub-interface GE0/0/1.1 with BD 10.
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] quit
[HUAWEI] interface GigabitEthernet 0/0/1
[HUAWEI-GigabitEthernet0/0/1] port link-type hybrid
[HUAWEI-GigabitEthernet0/0/1] quit
[HUAWEI] interface gigabitethernet 0/0/1.1 mode l2
[HUAWEI-GigabitEthernet0/0/1.1] bridge-domain 10
```


### `bridge-domain (system view)`

> **Página:** 8 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The bridge-domain command creates a bridge domain (BD) and displays the BD view, or directly displays the view of an existing BD view. The undo bridge-domain command deletes a BD. By default, no BD is created.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
bridge-domain bd-id
undo bridge-domain bd-id
```

**Parameters:**

- `bd-id` — Specifies the ID of a BD. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super-mode command is used to set the super VXLAN resource mode.

**Usage Guidelines:**

BDs are Layer 2 bridge domains on a large Layer 2 network constructed using VXLAN. VXLAN packets can be forwarded at Layer 2 within a BD through a VXLAN tunnel. After you run the bridge-domain command to create a BD, you can complete other VXLAN configurations in the BD.

**Example:**

```text
# Create BD 10 and enter the view of BD 10.
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10]
```


### `broadcast-suppression (BD view)`

> **Página:** 9 · **Views (Modo):** BD view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The broadcast-suppression command enables broadcast traffic suppression in a bridge domain (BD). The undo broadcast-suppression command disables broadcast traffic suppression in a BD. By default, broadcast traffic suppression is disabled in a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
broadcast-suppression cir cir-value [ cbs cbs-value ]
undo broadcast-suppression
```

**Parameters:**

- `cir cir-value` — Specifies the committed information rate (CIR), which is the allowed rate at which traffic can pass through. — *Valores:* The value is an integer that ranges from 0 to 10000000, in kbit/s.
- `cbs cbs-value` — Specifies the committed burst size (CBS), which is the maximum size of traffic that can pass through. — *Valores:* The value is an integer that ranges from 10000 to 4294967295, in bytes. If the cbs is not set, the default cbs-value is 125 times the cir-value.

**Usage Guidelines:**

When a large number of broadcast packets are transmitted on a network, a lot of network resources are occupied, and services on the network are affected. You can run the broadcast-suppression command to enable broadcast traffic suppression in a BD and configure the maximum number of broadcast packets that can pass through a BD. When the broadcast traffic volume exceeds the specified threshold, the system discards excess broadcast packets.

**Example:**

```text
# Set the CIR value for broadcast traffic in BD 10 to 100 kbit/s.
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] broadcast-suppression cir 100
```


### `description (BD view)`

> **Página:** 10 · **Views (Modo):** BD view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The description command configures the description of a bridge domain (BD). The undo description command deletes the description of a BD. By default, no description is configured for a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
description description
undo description
```

**Parameters:**

- `description` — Specifies the BD description. — *Valores:* The value is a string of 1 to 80 case- sensitive characters without spaces and question marks.

**Usage Guidelines:**

If you have configured multiple BDs using the bridge-domain (system view) command, run the description command in the corresponding BD view to configure the description for each BD. BD description helps you quickly understand the function of each BD, facilitating service management.

**Example:**

```text
# Configure description vxlan for BD 10.
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] description vxlan
```


### `display bridge-domain`

> **Página:** 11 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display bridge-domain command displays the BD configuration.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display bridge-domain [ bd-id [ brief | verbose ] ]
```

**Parameters:**

- `bd-id` — Displays the configuration of a specified BD. If this parameter is not specified, the device displays the configuration of all BDs. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super-mode command is used to set the super VXLAN resource mode.
- `brief` — Displays brief BD configuration. — *Valores:* -
- `verbose` — Displays detailed BD configuration. — *Valores:* -

**Usage Guidelines:**

After BDs are created on a device, you can run the display bridge-domain command to view the configuration of a specified BD or all BDs.

**Example:**

```text
# Display the configuration of all BDs.
<HUAWEI> display bridge-domain
STAT: Statistics;
--------------------------------------------------------------------------------
BDID State STAT Description
--------------------------------------------------------------------------------
10 down disable vxlan
20 up disable vxlan
--------------------------------------------------------------------------------
The total number of bridge-domains is : 2
# Display the detailed configuration of BD 10.
<HUAWEI> display bridge-domain 10 verbose
Bridge-domain ID :10
Description :vxlan
State :Down
Statistics :Disable
Broadcast-suppression CIR(kbit/s) :- CBS(byte) :-
Multicast-suppression CIR(kbit/s) :10000000 CBS(byte) :4294967295
Unknown-unicast-suppression CIR(kbit/s) :0 CBS(byte) :655355
--------------------------------------------------------------------------------
Interface State
--------------------------------------------------------------------------------
GigabitEthernet1/0/1.1 down
--------------------------------------------------------------------------------
VLAN State
--------------------------------------------------------------------------------
2 down
3 down
10 down
--------------------------------------------------------------------------------
```

Table 18-1 Description of the display bridge-domain command output

| Item | Description |
| --- | --- |
| BDID/Bridge- domain ID | ID of a BD. To set the BD ID, run the 18.1.5 bridge-domain (system view) command in the system view. |
| State | BD status: ● up: The BD is bound to a Layer 2 sub-interface, VLAN, or VNI, and at least one of the bound Layer 2 sub- interface, VLAN, and VNI is Up. ● down: The BD is not bound to a Layer 2 sub-interface, VLAN, or VNI; alternatively, the BD is bound to a Layer 2 sub-interface, VLAN, or VNI and the bound Layer 2 sub-interface, VLAN, and VNI are Down. |
| STAT/Statistics | Whether traffic statistics collection is enabled for the BD: ● disable ● enable |
| Description | BD description. To configure the description of a BD, run the description (BD view) command. |
| The total number of bridge-domains is | Total number of BDs on the device. |
| Broadcast- suppression CIR(kbit/s) CBS(byte) | CIR and CBS in a BD specified by the broadcast suppression function. The unit is kbit/s and byte, respectively. |

| Item | Description |
| --- | --- |
| Multicast- suppression CIR(kbit/s) CBS(byte) | CIR and CBS in a BD specified by the multicast suppression function. The unit is kbit/s and byte, respectively. |
| Unknown-unicast- suppression CIR(kbit/s) CBS(byte) | CIR and CBS in a BD specified by the unknown unicast suppression function. The unit is kbit/s and byte, respectively. |
| Interface State | Member interface in a BD and its status. ● up: The link layer protocol of the interface is in the Up state. ● down: The link layer protocol of the interface is Down. |
| VLAN State | Status of the VLAN associated with the BD. ● up ● down The status of a VLAN is determined by the status of member interfaces in the VLAN. A VLAN is Up only when at least one member interface in the VLAN is Up. |


### `display bridge-domain statistics`

> **Página:** 13 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display bridge-domain statistics command displays packet statistics in a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display bridge-domain bd-id statistics
```

**Parameters:**

- `bd-id` — Displays packet statistics in a specified BD. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super-mode command is used to set the super VXLAN resource mode.

**Usage Guidelines:**

You can run the display bridge-domain statistics command to view packet statistics in a BD. The information helps you locate faults and simplifies VXLAN network maintenance. Before using this command to view packet statistics in a BD, run the 18.1.31 statistics enable (BD view) command in the BD view to enable packet statistics collection in the BD.

**Example:**

```text
# Display packet statistics in BD 10.
<HUAWEI> display bridge-domain 10 statistics
Total:
--------------------------------------------------------------------------
Item Packets Bytes
--------------------------------------------------------------------------
Inbound 10 1520
Outbound 10 1520
--------------------------------------------------------------------------
Slot 0:
--------------------------------------------------------------------------
Item Packets Bytes
--------------------------------------------------------------------------
Inbound 10 1520
Outbound 10 1520
--------------------------------------------------------------------------
```

Table 18-2 Description of the display bridge-domain statistics command output

| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Item | Statistical item. |
| Packets | Number of packets. |
| Bytes | Number of bytes. |
| Inbound | Statistics on packets going in to a BD. |
| Outbound | Statistics on packets leaving a BD. |


### `display interface nve`

> **Página:** 14 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display interface nve command displays Network Virtualization Edge (NVE) interface information.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display interface nve [ nve-number | main ]
```

**Parameters:**

- `nve-number` — Specifies the number of an NVE interface. If nve-number is not specified, information about all NVE interfaces is displayed. — *Valores:* The value is 1.
- `main` — Displays the running status and statistics of the main interface. — *Valores:* -

**Usage Guidelines:**

To monitor the NVE interface status or locate an NVE interface fault on the VXLAN network, run the display interface nve command to check the running status and statistics of the NVE interface.

**Example:**

```text
# Display the running status of the NVE interface.
<HUAWEI> display interface nve 1
Nve1 current state : UP
Line protocol current state : UP
Description:
Route Port
Current system time: 2017-03-28 19:50:24
```

Table 18-3 Description of the display interface nve command output

| Item | Description |
| --- | --- |
| Nve1 current state | Physical status of the NVE interface. The physical status of the successfully created NVE interface is always Up. |
| Line protocol current state | Link layer protocol status of the NVE interface. The link layer protocol status of the successfully created NVE interface is always Up. |

| Item | Description |
| --- | --- |
| Description | Description of the NVE interface. |
| Route Port | The interface is a Layer 3 interface. |
| Current system time | System time. |


### `display interface vbdif`

> **Página:** 16 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display interface vbdif command displays the status, configuration, and statistics of a VBDIF interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display interface vbdif [ bd-id | main ]
```

**Parameters:**

- `bd-id` — Displays the status, configuration, and statistics of a VBDIF interface with a specified BD ID. If no BD ID is specified, the status, configuration, and statistics of all VBDIF interfaces are displayed. — *Valores:* The BD ID of a VBDIF interface must already exist.
- `main` — Displays the running status and statistics of the main interface. — *Valores:* -

**Usage Guidelines:**

**Usage Scenario**

To monitor an interface or locate an interface fault, you can use the display interface vbdif command to view the interface status, interface configuration, and traffic statistics on the interface. The information helps you locate faults in the system or on an interface.

**Prerequisites**

The specified VBDIF interface has been created.

**Example:**

```text
# Display information of VBDIF interface with BD ID 20.
<HUAWEI> display interface vbdif 20
Vbdif20 current state : UP
Line protocol current state : UP
Last line protocol up time : 2015-07-08 11:25:34
Description:
Route Port,The Maximum Transmit Unit is 1500
Internet Address is 192.168.20.1/24
IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is
0000-5e00-0101
Current system time: 2015-07-08 14:09:59
Input bandwidth utilization : --
Output bandwidth utilization : --
```

Table 18-4 Description of the display interface vbdif command output

| Item | Description |
| --- | --- |
| Vbdif20 current state | Physical status of a VBDIF interface. ● UP: The physical status of the interface is Up. ● DOWN: The physical status of the interface is Down. ● Administratively down: The administrator has run the shutdown command on the VBDIF interface. |
| Line protocol current state | Link-layer protocol status of a VBDIF interface. ● UP: The link-layer protocol of the interface is Up. ● DOWN: The link-layer protocol of the interface is Down, or no IP address is assigned to the interface. |
| Last line protocol up time | Last time the link-layer protocol of an interface goes Up. NOTE This field is displayed only when the link-layer protocol status is Up. |
| Description | Description of a VBDIF interface. The description helps you learn the functions of the interface. |
| Route Port | Layer 3 interface. |
| The Maximum Transmit Unit is | Maximum transmit unit (MTU) of an interface. The default MTU is 1500 bytes. Packets whose size is greater than the MTU are fragmented before being transmitted. If non-fragmentation is configured, these packets are discarded. |
| Internet Address is | IP address of an interface. If no IP address is configured for the current interface, the command output is displayed as "Internet protocol processing: disabled." |

| Item | Description |
| --- | --- |
| IP Sending Frames' Format is | Format of the Ethernet frames sent by a VBDIF interface. The default value is PKTFMT_ETHNT_2. A VBDIF interface can identify the received Ethernet frames of the following formats: ● PKTFMT_ETHNT_2 ● Ethernet_SNAP ● 802.2 ● 802.3 |
| Hardware address is | Physical address of an interface. |
| Current system time | System time. |
| Input | Number of packets received by the interface. |
| Output | Number of packets sent by the interface |


### `display mac-address bridge-domain`

> **Página:** 18 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display mac-address bridge-domain command displays MAC address entries of a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display mac-address [ mac-address ] bridge-domain bd-id [ verbose ]
```

**Parameters:**

- `mac-address` — Displays an entry with a specified MAC address. — *Valores:* The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. The MAC address cannot be FFFF-FFFF-FFFF, 0000-0000-0000, or a multicast MAC address.
- `bd-id` — Displays MAC address entries of a specified BD. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super-mode command is used to set the super VXLAN resource mode.
- `verbose` — Displays detailed information about MAC address entries. — *Valores:* -

**Usage Guidelines:**

**Usage Scenario**

The MAC address table of a switch stores MAC addresses of other devices. The switch queries the MAC address table to quickly locate the outbound interface for data forwarding. You can run the display mac-address bridge-domain command to view MAC address entries of a specified BD.

**Follow-up Procedure**

If any MAC address entry in the command output is incorrect, run the undo mac-address command to delete the entry or run the mac-address static command to add a correct one.

**Example:**

```text
# Display MAC address entries of BD 20.
<HUAWEI> system-view
[HUAWEI] display mac-address bridge-domain 20
-------------------------------------------------------------------------------
MAC Address VLAN/VSI/BD Learned-From Type
-------------------------------------------------------------------------------
0003-0005-0006 -/-/20 GE0/0/23.5 static
-------------------------------------------------------------------------------
Total items displayed = 1
# Display detailed information about MAC address entries of BD 20.
<HUAWEI> system-view
[HUAWEI] display mac-address bridge-domain 20 verbose
-------------------------------------------------------------------------------
MAC Address : 0003-0005-0006 BD : 20
Learned-From: GE0/0/23.5 Type : static
-------------------------------------------------------------------------------
Total items displayed = 1
```

Table 18-5 Description of the display mac-address bridge-domain command output

| Item | Description |
| --- | --- |
| MAC Address | MAC address. |
| VLAN/VSI/BD | ID of the VLAN, name of the virtual switch instance (VSI), or ID of the BD to which the MAC address belongs. |
| Learned-From | Interface on which a MAC address is learned. |

| Item | Description |
| --- | --- |
| Type | Type of a MAC address entry: ● static: a static MAC address entry, which is manually configured and will not be aged out. ● blackhole: a blackhole MAC address entry, which is manually configured and will not be aged out. |


### `display snmp-agent trap feature-name adpvxlan all`

> **Página:** 20 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display snmp-agent trap feature-name adpvxlan all command displays all trap messages of the ADPVXLAN module.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display snmp-agent trap feature-name adpvxlan all
```

**Usage Guidelines:**

The Simple Network Management Protocol (SNMP) is a standard network management protocol widely used on TCP/IP networks. It uses a central computer (a network management station) that runs network management software to manage network elements. The management agent on the network element automatically reports traps to the network management station. After that, the network administrator immediately takes measures to resolve the problem. The display snmp-agent trap feature-name adpvxlan all command displays whether all trap functions of the ADPVXLAN module are enabled.

**Example:**

```text
# Display all trap messages of the ADPVXLAN module.
<HUAWEI>display snmp-agent trap feature-name adpvxlan all
------------------------------------------------------------------------------
Feature name: ADPVXLAN
Trap number : 3
------------------------------------------------------------------------------
Trap name Default switch status Current switch status
hwNotsuppDecapVxlanFragPackets on on
hwVxlanTnlCfgFailed on on
hwNotsuppDecapVxlanPackets on on
```

Table 18-6 Description of the display snmp-agent trap feature-name adpvxlan all command output

| Item | Description |
| --- | --- |
| Feature name | Name of the module to which a trap message belongs. |
| Trap number | Number of trap messages. |
| Trap name | Name of a trap message of the ADPVXLAN module: ● hwNotsuppDecapVxlanFragPackets: indicates that the device cannot decapsulate fragmented VXLAN packets by ADPVXLAN. ● hwVxlanTnlCfgFailed: indicates that the device failed to deliver entries during VXLAN tunnel establishment due to a hash conflict by ADPVXLAN. ● hwNotsuppDecapVxlanPackets: indicates that the VXLAN-incapable device failed to decapsulate received VXLAN packets by ADPVXLAN. |
| Default switch status | Status of the default trap function: ● on: indicates that the trap function is enabled. ● off: indicates that the trap function is disabled. |
| Current switch status | Status of the current trap function: ● on: indicates that the trap function is enabled. ● off: indicates that the trap function is disabled. |

**Related Topics:**

- 18.1.29 snmp-agent trap enable feature-name adpvxlan


### `display vxlan peer`

> **Página:** 21 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display vxlan peer command displays the IP address of the destination virtual tunnel end point (VTEP) of a Virtual Network Identifier (VNI).

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display vxlan peer [ vni vni-id ]
```

**Parameters:**

- `vni vni-id` — Displays the IP address of the destination VTEP of a specified VNI. — *Valores:* The value is an integer that ranges from 1 to 16777215.

**Usage Guidelines:**

**Usage Scenario**

After completing VXLAN configuration, you can run the display vxlan peer command to view information about the source and destination IP address bound to the VNI.

**Precautions**

Before running the display vxlan peer command, ensure that the device has been configured with VNIs. Otherwise, the command output is meaningless.

**Example:**

```text
# Display the IP address of the destination VTEP of a specified VNI.
<HUAWEI> display vxlan peer
Vni ID Source Destination Type
--------------------------------------------------------------
10 10.1.1.2 10.1.1.3 static
10 10.1.1.2 10.1.1.4 static
--------------------------------------------------------------
Number of peers : 2
```

Table 18-7 Description of the display vxlan peer command output

| Item | Description |
| --- | --- |
| Vni ID | ID of a VNI. To configure or modify a VNI ID, run the 18.1.36 vxlan vni (BD view) command. |
| Source | IP address of the source VTEP. To configure or modify the IP address of the source VTEP, run the 18.1.30 source (NVE interface view) command. |
| Destination | IP address of the destination VTEP. To configure or modify the IP address of the destination VTEP, run the vni head-end peer-list command. |

| Item | Description |
| --- | --- |
| Type | The IP address of the destination VTEP is configured in static mode, the IP address is configured using the vni head-end peer-list command. |
| Number of peers | Number of destination VTEPs. |


### `display vxlan statistics`

> **Página:** 23 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display vxlan statistics command displays VXLAN tunnel packet statistics.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display vxlan statistics source source-ip-address peer peer-ip-address [ vni vni-id ]
```

**Parameters:**

- `source source-ip- address` — Specifies the IPv4 address of the source VTEP. — *Valores:* The value is in dotted decimal notation.
- `peer peer-ip-address` — Specifies the IPv4 address of the destination VTEP. — *Valores:* The value is in dotted decimal notation.
- `vni vni-id` — Specifies a VNI ID. — *Valores:* The value is an integer that ranges from 1 to 16777215.

**Usage Guidelines:**

You can run the display vxlan statistics command to view VXLAN tunnel packet statistics. The information helps you locate faults and simplifies VXLAN network maintenance. Before using this command to view VXLAN tunnel packet statistics, run the 18.1.35 vxlan statistics enable command on an NVE interface to enable statistics collection on VXLAN tunnel packets.

**Example:**

```text
# Display statistics on VXLAN tunnel packets, with 10.10.1.1 and 10.1.1.1 as the
```

source and destination VTEP IP addresses.

```text
<HUAWEI> display vxlan statistics source 10.10.1.1 peer 10.1.1.1
Total:
--------------------------------------------------------------------------
Item Packets Bytes
--------------------------------------------------------------------------
Inbound 5 760
Outbound 5 760
--------------------------------------------------------------------------
Slot 30:
--------------------------------------------------------------------------
Item Packets Bytes
--------------------------------------------------------------------------
Inbound 5 760
Outbound 5 760
--------------------------------------------------------------------------
```

Table 18-8 Description of the display vxlan statistics command output

| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| Item | Statistical item. |
| Packets | Number of packets. |
| Bytes | Number of bytes. |
| Inbound | Packet statistics in the inbound direction of the VXLAN tunnel. |
| Outbound | Packet statistics in the outbound direction of the VXLAN tunnel. |


### `display vxlan tunnel`

> **Página:** 24 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display vxlan tunnel command displays information about VXLAN tunnels.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display vxlan tunnel [ tunnel-id ] [ verbose ]
```

**Parameters:**

- `tunnel-id` — Displays information about the VXLAN tunnel with a specified ID. If this parameter is not specified, the device displays information about all VXLAN tunnels. — *Valores:* The value is an integer that ranges from 1 to 4294967295.
- `verbose` — Displays detailed VXLAN tunnel information. — *Valores:* -

**Usage Guidelines:**

After VXLAN tunnels are established, you can run the display vxlan tunnel command to view VXLAN tunnel information.

**Example:**

```text
# Display VXLAN tunnel information.
<HUAWEI> display vxlan tunnel
Tunnel ID Source Destination State Type
----------------------------------------------------------------------------
4026531841 10.1.1.2 10.1.1.4 up static
----------------------------------------------------------------------------
Number of vxlan tunnel : 1
# Display detailed VXLAN tunnel information.
<HUAWEI> display vxlan tunnel verbose
Tunnel ID : 4026531841
Source : 10.1.1.2
Destination : 10.1.1.4
State : up
Type : static
----------------------------------------------------------------------------
Number of vxlan tunnel : 1
```

Table 18-9 Description of the display vxlan tunnel command output

| Item | Description |
| --- | --- |
| Tunnel ID | ID of a VXLAN tunnel. After a VXLAN tunnel is established, the ID is automatically generated by the device. |

| Item | Description |
| --- | --- |
| Source | Source IP address of the VXLAN tunnel. To configure the source IP address, run the source (NVE interface view) command. |
| Destination | Destination IP address of the VXLAN tunnel. |
| State | Status of the VXLAN tunnel: ● up: The VXLAN tunnel is reachable. ● down: The VXLAN tunnel is unreachable. |
| Type | The VXLAN tunnel type is static, the VXLAN tunnel status is determined by the configuration mode of peer-list in the vni head-end peer-list command. |
| Number of vxlan tunnel | Total number of VXLAN tunnels. |


### `display vxlan vni`

> **Página:** 26 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display vxlan vni command displays the VXLAN configuration of a specified VNI or all VNIs.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display vxlan vni [ vni-id [ verbose ] ]
```

**Parameters:**

- `vni-id` — Displays VXLAN information about a specified VNI. If this parameter is not specified, the device displays VXLAN configuration of all VNIs. — *Valores:* The value is an integer that ranges from 1 to 16777215.
- `verbose` — Displays detailed VXLAN information about a specified VNI. — *Valores:* -

**Usage Guidelines:**

Applications After VXLAN is configured, you can run the display vxlan vni command to view information about BDs associated with VNIs and VNI status.

**Precautions**

Before running the display vxlan vni command, ensure that the device has been configured with VNIs. Otherwise, the command output is meaningless.

**Example:**

```text
# Display VXLAN information about all VNIs.
<HUAWEI> display vxlan vni
VNI BD-ID State
-----------------------------------------
10 10 up
20 20 up
-----------------------------------------
Number of vxlan vni bound to BD is : 2
# Display detailed VXLAN information about VNI 10.
<HUAWEI> display vxlan vni 10 verbose
BD ID :10
State :up
Source :10.1.1.2
UDP Port :4789
Peer List :10.1.1.1 10.1.1.3
```

Table 18-10 Description of the display vxlan vni command output

| Item | Description |
| --- | --- |
| VNI | ID of a VNI. To configure or modify a VNI ID, run the vxlan vni command. |
| BD-ID (BD ID) | ID of the BD associated with a VNI. To configure or modify a BD ID, run the bridge-domain (system view) command. |

| Item | Description |
| --- | --- |
| State | VNI status: ● up ● down To ensure that the VNI status is up, the corresponding VXLAN tunnel must exist and be up for the VNI. If the VNI status is down, check whether Source and Peer List in this command output are the same as Source and Destination in the output of the display vxlan tunnel command. ● If they are different, no VXLAN tunnel exists for the specified VNI. Run the source (NVE interface view) or vni head-end peer-list command to change the source or destination IP address of the VXLAN tunnel to ensure that the corresponding VXLAN tunnel exists for the VNI. ● If they are the same, collect related configuration and contact technical support personnel. |
| Number of vxlan vni bound to BD is | Number of existing VNIs bound to BDs. |
| Source | IP address of the source VTEP. To configure the IP address of the source VTEP, run the source (NVE interface view) command. |
| Source IPv6 Address | IPv6 address of the source VTEP. To configure the IP address of the source VTEP, run the source (NVE interface view) command. |
| UDP Port | Destination UDP port. The port number is fixed as 4789. |
| Peer List | IP address of the destination VTEP. To configure the IP address of the destination VTEP, run the vni head-end peer- list command. |
| IPv6 Peer List | IPv6 address of the destination VTEP. To configure the IP address of the destination VTEP, run the vni head-end peer- list command. |


### `encapsulation (Layer 2 sub-interface view)`

> **Página:** 28 · **Views (Modo):** Layer 2 sub-interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The encapsulation command configures the encapsulation mode of packets allowed to pass a Layer 2 sub-interface. The undo encapsulation command deletes the encapsulation mode of packets allowed to pass a Layer 2 sub-interface. By default, the encapsulation mode of packets allowed to pass a Layer 2 sub-interface is not configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
encapsulation { dot1q vid pe-vid | default | untag | qinq vid vlan-vid ce-vid ce-vid }
undo encapsulation { dot1q vid pe-vid | default | untag | qinq vid vlan-vid ce-vid ce-vid }
```

**Parameters:**

- `dot1q` — Sets encapsulation mode of packets allowed to pass a Layer 2 sub-interface to Dot1q. This mode enables a Layer 2 sub-interface to receive packets with a VLAN tag. — *Valores:* -
- `vid pe-vid` — Specifies the outer VLAN ID in packets allowed to pass a Layer 2 sub-interface in Dot1q encapsulation mode. — *Valores:* The value is an integer that ranges from 2 to 4094.
- `default` — Sets the encapsulation mode of packets allowed to pass a Layer 2 sub-interface to default. This mode enables a Layer 2 sub-interface to receive all packets, regardless of whether they contain VLAN tags. — *Valores:* -
- `untag` — Sets the encapsulation mode of packets allowed to pass a Layer 2 sub-interface to untag. This mode enables a Layer 2 sub-interface to receive packets without VLAN tags. — *Valores:* -
- `qinq` — Sets encapsulation mode of packets allowed to pass a Layer 2 sub-interface to QinQ. This mode enables a Layer 2 sub-interface to receive packets with double VLAN tags. — *Valores:* -
- `vid vlan-vid` — Specifies the outer VLAN ID in double-tagged packets allowed to pass a Layer 2 sub-interface in QinQ encapsulation mode. — *Valores:* The value is an integer that ranges from 2 to 4094.
- `ce-vid ce-vid` — Specifies the inner VLAN ID in double-tagged packets allowed to pass a Layer 2 sub-interface in QinQ encapsulation mode. — *Valores:* The value is an integer that ranges from 1 to 4094.

**Usage Guidelines:**

**Usage Scenario**

On a VXLAN network, a Layer 2 sub-interface functions as a VXLAN service access point to forward data packets in a BD. Packets passing through a physical interface may contain one or two VLAN tags or no VLAN tag. After you run the encapsulation command in a Layer 2 sub-interface view to configure the encapsulation mode, the sub-interface can forward only specified types of packets.

**Prerequisites**

Run the command interface interface-type interface-number.subnum mode l2 to create a VXLAN Layer 2 sub-interface

**Precautions**

When configuring an encapsulation mode on a Layer 2 sub-interface, pay attention to the following points:

- The VLAN ID in dot1q mode or outer VLAN ID in qinq mode cannot be the same as the allowed VLAN of the corresponding main interface or the global VLAN.

- On the same main interface, the VLAN ID in dot1q mode and the outer VLAN ID in qinq mode must be different.

- After NAC authentication is configured on the main interface, the traffic encapsulation type on a Layer 2 sub-interface cannot be set to default.

- When the encapsulation mode of a Layer 2 sub-interface is default, the corresponding main interface cannot be added to any VLAN, including VLAN 1.

- Before the encapsulation mode of a Layer 2 sub-interface is set to default, the main interface has only one sub-interface.

- After the encapsulation mode of a Layer 2 sub-interface is set to default, no other sub-interface can be created on the main interface.

- When the encapsulation mode of a Layer 2 sub-interface is set to untag, other sub-interfaces of the main interface cannot be set to untag.

- You can configure only one encapsulation mode for each Layer 2 sub-interface. If an encapsulation mode has been configured for a Layer 2 sub-interface, run the undo encapsulation command to delete the original mode before you configure another mode.

**Example:**

```text
# Set the encapsulation mode of packets allowed to pass Layer 2 sub-interface
```

GE0/0/0.1 to Dot1q and the outer VLAN ID in the packets to 10.

```text
<HUAWEI> system-view
[HUAWEI] interface GigabitEthernet 0/0/1
[HUAWEI-GigabitEthernet0/0/1] port link-type hybrid
[HUAWEI-GigabitEthernet0/0/1] quit
[HUAWEI] interface gigabitethernet 0/0/1.1 mode l2
[HUAWEI-GigabitEthernet0/0/1.1] encapsulation dot1q vid 10
```


### `interface nve`

> **Página:** 31 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The interface nve command creates a Network Virtualization Edge (NVE) interface and displays the NVE interface view. The undo interface nve command deletes a specified NVE interface. By default, no NVE interface is created.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
interface nve nve-number
undo interface nve nve-number
```

**Parameters:**

- `nve-number` — Specifies the number of an NVE interface. — *Valores:* The value is 1.

**Usage Guidelines:**

**Usage Scenario**

To make full use of advantages of server virtualization, you can deploy VXLAN to connect to multiple tenants. VXLAN tunnel information needs to be configured on an NVE interface, so the interface nve command needs to be executed to create the NVE interface.

**Precautions**

After a VXLAN tunnel is configured, running the undo interface nve command will delete the specified NVE interface and all the configuration of the NVE interface.

**Example:**

```text
# Create an NVE interface.
<HUAWEI> system-view
[HUAWEI] interface nve 1
```


### `interface vbdif`

> **Página:** 32 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The interface vbdif command creates a VBDIF interface and displays the VBDIF interface view, or displays the view of an existing VBDIF interface. The undo interface vbdif command deletes a VBDIF interface. By default, no VBDIF interface is created.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
interface vbdif bd-id
undo interface vbdif bd-id
```

**Parameters:**

- `bd-id` — Specifies the ID of a BD. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super-mode command is used to set the super VXLAN resource mode.

**Usage Guidelines:**

**Usage Scenario**

IP routes are required for communication between VXLAN networks on different network segments and between VXLAN and non-VXLAN networks. To enable the communication, run the interface vbdif command to create a VBDIF interface for each BD and assign an IP address to the VBDIF interface. A VBDIF interface is a Layer 3 logical interface and can be configured with an IP address.

**Prerequisites**

The specified BD has been created.

**Example:**

```text
# Create a VBDIF interface for BD 10.
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] quit
[HUAWEI] interface vbdif 10
```


### `l2 binding vlan`

> **Página:** 33 · **Views (Modo):** BD view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The l2 binding vlan command associates a specified VLAN with a BD. The undo l2 binding vlan command restores the default settings. By default, a VLAN is associated with no BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
l2 binding vlan vlan-id
undo l2 binding vlan vlan-id
```

**Parameters:**

- `vlan-id` — Specifies a VLAN ID. — *Valores:* The value is an integer that ranges from 1 to 4094. Currently, VLAN 1 cannot be associated with a BD.

**Usage Guidelines:**

**Usage Scenario**

VXLAN needs to be deployed on a downlink interface to provide access services and an uplink interface to establish a VXLAN tunnel. On the access side, two methods are available for creating a large Layer 2 BD.

- Based on VLAN: You can associate one or multiple VLANs with a BD to add users in these VLANs to the BD. This VLAN-based mode implements largergranularity control, but is easy to configure. It applies to VXLAN deployment on a live network.

- Based on encapsulation mode: The device sends packets of different encapsulation modes to different Layer 2 sub-interfaces based on the VLAN tags contained in the packets. You can bind a Layer 2 sub-interface to a BD to add specified users to the BD. This mode implements refined and flexible control but requires more complex configuration. It applies to VXLAN deployment on a new network. After you run this command to associate specified VLANs with a BD, different VLANs associated with the same BD form a large Layer 2 network. Users belong to these VLANs can communicate at Layer 2 through VXLAN tunnels.

**Prerequisites**

The VLAN to be bound to the BD has been created using the 5.3.49 vlan command.

**Precautions**

- One VLAN can be associated with only one BD, but one BD can be associated with multiple VLANs.

- After a global VLAN is associated with a BD, you need to add corresponding interfaces to the VLAN.

- If a VLAN is configured as a voice VLAN, it cannot be associated with a BD.

**Example:**

```text
# Associate VLAN 10 with BD 10.
<HUAWEI> system-view
[HUAWEI] vlan 10
[HUAWEI-vlan10] quit
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] l2 binding vlan 10
```


### `multicast-suppression (BD view)`

> **Página:** 34 · **Views (Modo):** BD view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The multicast-suppression command enables multicast traffic suppression in a BD. The undo multicast-suppression command disables multicast traffic suppression in a BD. By default, multicast traffic suppression is disabled in a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
multicast-suppression cir cir-value [ cbs cbs-value ]
undo multicast-suppression
```

**Parameters:**

- `cir cir-value` — Specifies the committed information rate (CIR), which is the allowed rate at which traffic can pass through. — *Valores:* The value is an integer that ranges from 0 to 10000000, in kbit/s.
- `cbs cbs-value` — Specifies the committed burst size (CBS), which is the maximum size of traffic that can pass through. — *Valores:* The value is an integer that ranges from 10000 to 4294967295, in bytes. If the cbs is not set, the default cbs-value is 125 times the cir-value.

**Usage Guidelines:**

When a large number of multicast packets are transmitted on a network, a lot of network resources are occupied, and services on the network are affected. You can run the multicast-suppression command to enable multicast traffic suppression in a BD and configure the maximum number of multicast packets that can pass through a BD. When the multicast traffic volume exceeds the specified threshold, the system discards excess multicast packets.

**Example:**

```text
# Set the CIR value for multicast traffic in BD 10 to 100 kbit/s.
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] multicast-suppression cir 100
```


### `mac-address static bridge-domain`

> **Página:** 35 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The mac-address static bridge-domain command configures a static MAC address entry on a VXLAN access-side interface. The undo mac-address static bridge-domain command deletes a static MAC address entry on a VXLAN access-side interface. By default, no static MAC address entry is configured on a VXLAN access-side interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
mac-address static mac-address interface-type interface-number.subnum bridge-domain bd-id { default | untag | vid vlan-id1 [ ce-vid vlan-id2 ] }
undo mac-address static mac-address interface-type interface-number.subnum
bridge-domain bd-id { default | untag | vid vlan-id1 [ ce-vid vlan-id2 ] }
mac-address static mac-address interface-type interface-number bridge-domain
bd-id vid vlan-id3
undo mac-address static mac-address interface-type interface-number bridge-domain bd-id vid vlan-id3
```

**Parameters:**

- `mac-address` — Specifies the MAC address in the static MAC address entry. — *Valores:* The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. The MAC address cannot be FFFF-FFFF- FFFF, 0000-0000-0000, or a multicast MAC address.
- `interface-type interface- number.subnum` — Specifies that the outbound interface in the static MAC address entry is a Layer 2 sub-interface. — *Valores:* -
- `bd-id` — Specifies the BD to which the outbound interface belongs. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super-mode command is used to set the super VXLAN resource mode.
- `default` — Specifies that the outbound interface allows packets of the default type to pass. — *Valores:* -
- `untag` — Specifies that the outbound interface allows packets of the untag type to pass. — *Valores:* -
- `vid vlan-id1` — Specifies the outer VLAN ID in the packets allowed to pass the outbound interface. — *Valores:* The value is an integer that ranges from 1 to 4094.
- `ce-vid vlan-id2` — Specifies the inner VLAN ID in the packets allowed to pass the outbound interface. — *Valores:* The value is an integer that ranges from 1 to 4094.
- `interface-type interface-number` — Specifies that the outbound interface in the static MAC address entry is a specified interface. — *Valores:* -
- `vid vlan-id3` — Specifies the ID of the VLAN to which the outbound interface belongs. — *Valores:* The value is an integer that ranges from 1 to 4094.

**Usage Guidelines:**

**Usage Scenario**

When the device creates a MAC address table by learning source MAC addresses, the device cannot distinguish packets from authorized and unauthorized users. This threatens network security. If an unauthorized user uses the MAC address of an authorized user as the source MAC address of attack packets and connects to another interface of the device, the device learns an incorrect MAC address entry. The device incorrectly forwards the packets to the unauthorized user. Actually, the packets should be forwarded to the authorized user. You can run the mac-address static bridge-domain command to add a static MAC address entry to the MAC address table on the VXLAN access side. The static MAC address entry binds the MAC address to a specified interface, which prevents unauthorized users from intercepting data of authorized users. In addition, a manually configured static MAC address entry improves the unicast packet forwarding efficiency and saves bandwidth.

**Prerequisites**

- The interface has been added to a BD.

**Example:**

```text
# Configure a static MAC address entry on a VXLAN access-side interface. In the
```

entry, the destination MAC address is aaaa-fccc-1212 and the flow encapsulation type of the outbound interface is dot1q.

```text
<HUAWEI> system-view
[HUAWEI] interface gigabitethernet 0/0/1
[HUAWEI-GigabitEthernet0/0/1] port link-type hybrid
[HUAWEI-GigabitEthernet0/0/1] quit
[HUAWEI] bridge-domain 20
[HUAWEI-bd10] quit
[HUAWEI] interface gigabitethernet 0/0/1.1 mode l2
[HUAWEI-GigabitEthernet0/0/1.1] encapsulation dot1q vid 6
[HUAWEI-GigabitEthernet0/0/1.1] bridge-domain 20
[HUAWEI-GigabitEthernet0/0/1.1] quit
[HUAWEI] mac-address static aaaa-fccc-1212 GigabitEthernet 0/0/1.1 bridge-domain 20 vid 6
# Configure a static MAC address entry on the VXLAN access-side interface. In the
```

entry, the destination MAC address is aaaa-fccc-1213 and the outbound interface is added to a BD by the VLAN.

```text
<HUAWEI> system-view
[HUAWEI] vlan 8
[HUAWEI-vlan8] quit
[HUAWEI] interface gigabitethernet 0/0/1
[HUAWEI-GigabitEthernet0/0/1] port link-type hybrid
[HUAWEI-GigabitEthernet0/0/1] port hybrid tagged vlan 8
[HUAWEI-GigabitEthernet0/0/1] quit
[HUAWEI] bridge-domain 30
[HUAWEI-bd10] l2 binding vlan 8
[HUAWEI-bd10] quit
[HUAWEI] mac-address static aaaa-fccc-1213 GigabitEthernet 0/0/1 bridge-domain 30 vid 8
```


### `mac-address static bridge-domain vni`

> **Página:** 38 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The mac-address static bridge-domain vni command configures a static MAC address entry on a VXLAN tunnel-side interface. The undo mac-address static bridge-domain vni command deletes a static MAC address entry on a VXLAN tunnel-side interface. By default, no static MAC address entry is configured on a VXLAN tunnel-side interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
mac-address static mac-address bridge-domain bd-id source ip-address peer ip-address vni vni-id
undo mac-address static mac-address bridge-domain bd-id source ip-address
peer ip-address vni vni-id
```

**Parameters:**

- `mac-address` — Specifies the MAC address in the static MAC address entry. — *Valores:* The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. The MAC address cannot be FFFF-FFFF- FFFF, 0000-0000-0000, or a multicast MAC address.
- `bd-id` — Specifies the BD to which the outbound interface belongs. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super-mode command is used to set the super VXLAN resource mode.
- `source-ip- address` — Specifies the source IP address of the VXLAN tunnel. — *Valores:* The value is in dotted decimal notation.
- `peer ip- address` — Specifies the remote IP address of the VXLAN tunnel. — *Valores:* The value is in dotted decimal notation.
- `vni-id` — Specifies the ID of a VXLAN tunnel. — *Valores:* The value is an integer that ranges from 1 to 16777215.

**Usage Guidelines:**

**Usage Scenario**

When the device creates a MAC address table by learning source MAC addresses, the device cannot distinguish packets from authorized and unauthorized users. This threatens network security. If an unauthorized user uses the MAC address of an authorized user as the source MAC address of attack packets and connects to another interface of the device, the device learns an incorrect MAC address entry. The device incorrectly forwards the packets to the unauthorized user. Actually, the packets should be forwarded to the authorized user. You can run the mac-address static bridge-domain vni command to add a static MAC address entry to the MAC address table on the VXLAN tunnel side. The static MAC address entry binds the MAC address to a specified interface, which prevents unauthorized users from intercepting data of authorized users. In addition, a manually configured static MAC address entry improves the unicast packet forwarding efficiency and saves bandwidth.

**Prerequisites**

A VXLAN tunnel has been created.

**Example:**

```text
# On a VXLAN tunnel-side interface, configure a static MAC address entry with
```

the destination MAC address aaaa-fccc-1212.

```text
<HUAWEI> system-view
[HUAWEI] bridge-domain 20
[HUAWEI-bd10] vxlan vni 2000
[HUAWEI-bd10] quit
[HUAWEI] interface nve 1
[HUAWEI-Nve1] source 10.1.1.2
[HUAWEI-Nve1] vni 2000 head-end peer-list 10.1.2.2
[HUAWEI-Nve1] quit
[HUAWEI] mac-address static aaaa-fccc-1212 bridge-domain 20 source 10.1.1.2 peer 10.1.2.2 vni 2000
```


### `reset bridge-domain statistics`

> **Página:** 40 · **Views (Modo):** User view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The reset bridge-domain statistics command clears packet statistics in a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
reset bridge-domain bd-id statistics
```

**Parameters:**

- `bd-id` — Specifies the ID of a BD packet statistics of which are to be deleted. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super- mode command is used to set the super VXLAN resource mode.

**Usage Guidelines:**

**Usage Scenario**

Before you collect packet statistics in a specified BD within a specific period, run the reset bridge-domain statistics command to clear the existing statistics in the BD to ensure statistics accuracy.

**Precautions**

Packet statistics cannot be restored after you clear them; therefore, exercise caution before you run the reset bridge-domain statistics command.

**Example:**

```text
# Clear packet statistics in BD 10.
<HUAWEI> reset bridge-domain 10 statistics
```


### `reset vxlan statistics`

> **Página:** 41 · **Views (Modo):** User view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The reset vxlan statistics command clears VXLAN tunnel packet statistics.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
reset vxlan statistics source source-ip-address peer peer-ip-address [ vni vni-id ]
```

**Parameters:**

- `source source-ip- address` — Specifies the IPv4 address of the source VTEP. — *Valores:* The value is in dotted decimal notation.
- `peer peer-ip-address` — Specifies the IPv4 address of the destination VTEP. — *Valores:* The value is in dotted decimal notation.
- `vni vni-id` — Specifies a VNI ID. — *Valores:* The value is an integer that ranges from 1 to 16777215.

**Usage Guidelines:**

**Usage Scenario**

Before you collect VXLAN tunnel packet statistics within a specific period, run the reset vxlan statistics command to clear the existing statistics to ensure statistics accuracy.

**Precautions**

Packet statistics cannot be restored after you clear them; therefore, exercise caution before you run the reset vxlan statistics command.

**Example:**

```text
# Clear statistics on VXLAN tunnel packets, with 10.10.1.1 and 10.1.1.1 as the
```

source and destination VTEP IP addresses.

```text
<HUAWEI> reset vxlan statistics source 10.10.1.1 peer 10.1.1.1
```


### `service type vxlan-tunnel`

> **Página:** 42 · **Views (Modo):** Eth-Trunk interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The service type vxlan-tunnel command configures an Eth-Trunk as a VXLAN loopback interface. The undo service type vxlan-tunnel command cancels the configuration. By default, an Eth-Trunk is not a VXLAN loopback interface. NOTE Only the S6720EI and S6720S-EI switches support this command.

**Supported Platforms:** Only the S6720EI and S6720S-EI switches support this command.

**Syntax (Format):**

```text
service type vxlan-tunnel
undo service type vxlan-tunnel
```

**Usage Guidelines:**

**Usage Scenario**

The S6720EI and S6720S-EI switches can decapsulate received VXLAN packets and forward them at Layer 3 only after a VXLAN loopback interface is configured on them. As a result, you need to configure an Eth-Trunk as the VXLAN loopback interface when the S6720EI and S6720S-EI switches function as the Layer 3 VXLAN gateway.

**Follow-up Procedure**

Run the trunkport command to add member interfaces to the VXLAN loopback interface.

**Precautions**

- After an Eth-Trunk is configured as a VXLAN loopback interface, STP is automatically disabled on the Eth-Trunk. The Eth-Trunk then does not support STP configuration commands. After the configuration is canceled, STP is automatically enabled on the Eth-Trunk.

- Only one Eth-Trunk on a switch can be configured as the VXLAN loopback interface. VXLAN packets from all VBDIF interfaces are encapsulated and decapsulated by this loopback interface.

- An Eth-Trunk containing member interfaces cannot be configured as a VXLAN loopback interface.

- The configurations allowed on an Eth-Trunk to be configured as a loopback interface include description, enable snmp trap updown, jumboframe enable, qos phb marking enable, set flow-stat interval, shutdown, traffic-policy (interface view), and trust. If other configurations exist on the Eth-Trunk, the Eth-Trunk cannot be configured as a loopback interface.

- After an Eth-Trunk is configured as a loopback interface, the Eth-Trunk supports only the following configurations: authentication open ucl-policy enable, description, enable snmp trap updown, jumboframe enable, mixed-rate link enable, qos phb marking enable, set flow-stat interval, shutdown, statistic enable (interface view), traffic-policy (interface view), vcmp disable, and trust.

- Before running the undo service type vxlan-tunnel command, delete all the member interfaces from the Eth-Trunk.

**Example:**

```text
# Configure Eth-Trunk 1 as a VXLAN loopback interface.
<HUAWEI> system-view
[HUAWEI] interface Eth-Trunk 1
[HUAWEI-Eth-Trunk1] service type vxlan-tunnel
```

**Related Topics:**

- 5.2.72 trunkport


### `set vxlan resource super-mode`

> **Página:** 43 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The set vxlan resource super-mode command sets the super VXLAN resource mode. The undo set vxlan resource super-mode command restores the default VXLAN resource mode. By default, the device supports 4096 BDs. NOTE Only the S5720HI supports this command.

**Supported Platforms:** Only the S5720HI supports this command.

**Syntax (Format):**

```text
set vxlan resource super-mode
undo set vxlan resource super-mode
```

**Usage Guidelines:**

**Usage Scenario**

When VXLAN is configured, the device supports 4096 BDs by default. If you want more than 4096 BDs, run the set vxlan resource super-mode command to set the super VXLAN resource mode. After this command is configured, the device supports 16000 BDs.

**Precautions**

- After setting the super VXLAN resource mode, save the configuration and then restart the device to make the configuration take effect.

- When the super VXLAN resource mode is configured, the forwarding performance of some services may degrade, such as the IP multicast, VPLS, VLAN mapping, Layer 3 traffic forwarding of sub-interfaces, and VLAN stacking services.

**Example:**

```text
# Set the super VXLAN resource mode.
<HUAWEI> system-view
[HUAWEI] set vxlan resource super-mode
```


### `snmp-agent trap enable feature-name adpvxlan`

> **Página:** 44 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable feature-name adpvxlan command enables the trap function for the ADPVXLAN module. The undo snmp-agent trap enable feature-name adpvxlan command disables the trap function for the ADPVXLAN module. By default, the trap function is enabled for the ADPVXLAN module.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable feature-name adpvxlan [ trap-name
{ hwnotsuppdecapvxlanfragpackets | hwnotsuppdecapvxlanpackets |
hwvxlantnlcfgfailed } ]
undo snmp-agent trap enable feature-name adpvxlan [ trap-name
{ hwnotsuppdecapvxlanfragpackets | hwnotsuppdecapvxlanpackets |
hwvxlantnlcfgfailed } ]
```

**Parameters:**

- `trap-name` — Enables the traps of ADPVXLAN events of specified types. — *Valores:* -
- `hwnotsuppdecapvxlanfragpackets` — Enables the device to send trap when the device cannot decapsulate received fragmented VXLAN packets. — *Valores:* -
- `hwnotsuppdecapvxlanpackets` — Enables the device to send trap when the VXLAN-incapable device failed to decapsulate received VXLAN packets. — *Valores:* -
- `hwvxlantnlcfgfailed` — Enables the device to send trap when the device failed to deliver entries during VXLAN tunnel establishment due to a hash conflict. — *Valores:* -

**Usage Guidelines:**

The ADPVXLAN module is not configured with the function of excessive traps. To enable the traps of one or more events, you can specify trap-name.

**Example:**

```text
# Enables the device to send trap when the device cannot decapsulate received
```

fragmented VXLAN packets.

```text
<HUAWEI> system-view
[HUAWEI] snmp-agent trap enable feature-name adpvxlan trap-name
hwnotsuppdecapvxlanfragpackets
```

**Related Topics:**

- 18.1.13 display snmp-agent trap feature-name adpvxlan all


### `source (NVE interface view)`

> **Página:** 46 · **Views (Modo):** NVE interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The source command configures an IP address for a source VXLAN Tunnel Endpoint (VTEP). The undo source command deletes the IP address of the source VTEP. By default, no IP address is configured for a source VTEP.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
source ip-address
undo source [ ip-address ]
```

**Parameters:**

- `ip-address` — Specifies the IPv4 address of a source VTEP. — *Valores:* The value is in dotted decimal notation.

**Usage Guidelines:**

**Usage Scenario**

VXLAN needs to be deployed on a downlink interface to provide access services and an uplink interface to establish a VXLAN tunnel. To establish a VXLAN tunnel, configure IP addresses for the source and destination VTEPs. To configure an IP address for a source VTEP, run this command. When access service packets reach a Network Virtualization Edge (NVE), the VTEP encapsulates the packets based on the IP addresses of source and destination VTEPs and forwards them.

**Precautions**

- You can specify the IP address of a physical interface or a loopback interface as the IP address of the source VTEP. The address of a loopback interface is recommended.

- Generally, the NVE interfaces of different devices must be configured with different VTEP addresses; otherwise, traffic forwarding errors may occur.

- The IP address of a VBDIF interface cannot be configured as the IP address of the source VTEP of a VXLAN tunnel.

**Follow-up Procedure**

Run the vni head-end peer-list command to configure an IP address for a destination VTEP.

**Example:**

```text
# Set the IP address of the source VTEP to 10.1.1.2.
<HUAWEI> system-view
[HUAWEI] interface nve 1
[HUAWEI-Nve1] source 10.1.1.2
```


### `statistics enable (BD view)`

> **Página:** 47 · **Views (Modo):** BD view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The statistics enable command enables statistics collection in a BD. The undo statistics enable command disables statistics collection in a BD. By default, statistics collection is disabled in a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
statistics enable
undo statistics enable
```

**Usage Guidelines:**

Packet statistics in a BD provide information about the number of packets going into and leaving a BD. To view packet statistics in a BD, run the statistics enable and display bridge-domain statistics commands in sequence. The information helps you locate faults.

**Example:**

```text
# Enable packet statistics collection in BD 10.
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] statistics enable
```


### `undo mac-address bridge-domain`

> **Página:** 48 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The undo mac-address bridge-domain command deletes MAC address entries of a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
undo mac-address bridge-domain bd-id
```

**Parameters:**

- `bd-id` — Deletes MAC address entries of a specified BD. — *Valores:* The value is an integer that ranges from 1 to 4096. For the S5720HI, the value is an integer that ranges from 1 to 16000 after the 18.1.28 set vxlan resource super-mode command is used to set the super VXLAN resource mode.

**Usage Guidelines:**

The MAC address table space is limited on a device. If the number of MAC address entries reaches the upper limit, the device cannot learn new MAC address entries before some entries in the MAC address table are aged out. In this case, the device broadcasts packets from new users, wasting network resources. To solve the problem, you can run the undo mac-address bridge-domain command to manually delete unnecessary MAC address entries of a specified BD.

**Example:**

```text
# Delete MAC address entries of BD 20.
<HUAWEI> system-view
[HUAWEI] undo mac-address bridge-domain 20
```


### `unknown-unicast-suppression (BD view)`

> **Página:** 49 · **Views (Modo):** BD view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The unknown-unicast-suppression command enables unknown unicast traffic suppression in a BD. The undo unknown-unicast-suppression command disables unknown unicast traffic suppression in a BD. By default, unknown unicast traffic suppression is disabled in a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
unknown-unicast-suppression cir cir-value [ cbs cbs-value ]
undo unknown-unicast-suppression
```

**Parameters:**

- `cir cir-value` — Specifies the committed information rate (CIR), which is the allowed rate at which traffic can pass through. — *Valores:* The value is an integer that ranges from 0 to 10000000, in kbit/s.
- `cbs cbs-value` — Specifies the committed burst size (CBS), which is the maximum size of traffic that can pass through. — *Valores:* The value is an integer that ranges from 10000 to 4294967295, in bytes. If the cbs is not set, the default cbs-value is 125 times the cir-value.

**Usage Guidelines:**

When a large number of unknown unicast packets are transmitted on the network, a lot of network resources are occupied, and services on the network are affected. You can run the unknown-unicast-suppression command to enable unknown unicast traffic suppression in a BD and configure the maximum number of unknown unicast packets that can pass through a BD. When the unknown unicast traffic volume exceeds the specified threshold, the system discards excess unknown unicast packets.

**Example:**

```text
# Set the CIR value for unknown unicast traffic in BD 10 to 100 kbit/s.
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] unknown-unicast-suppression cir 100
```


### `vni head-end peer-list`

> **Página:** 50 · **Views (Modo):** NVE interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The vni head-end peer-list command configures an ingress replication list that contains the IP addresses of those remote VTEPs for a VXLAN network identifier (VNI). The undo vni head-end peer-list command deletes the ingress replication list of a VNI. By default, no ingress replication list is configured for any VNI.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
vni vni-id head-end peer-list ip-address &<1-10>
undo vni vni-id [ head-end peer-list ip-address &<1-10> ]
```

**Parameters:**

- `vni-id` — Specifies a VNI ID. — *Valores:* The value is an integer that ranges from 1 to 16777215.
- `ip-address` — Specifies the IPv4 address of a remote VTEP. — *Valores:* The value is in dotted decimal notation.

**Usage Guidelines:**

**Usage Scenario**

After the ingress of a VXLAN tunnel receives broadcast, unknown unicast, and multicast (BUM) packets, it replicates these packets and sends a copy to each VTEP in the ingress replication list. The ingress replication list is a collection of remote VTEP IP addresses to which the ingress of a VXLAN tunnel should send replicated BUM packets. If a source VTEP on a VXLAN connects to multiple remote VTEPs on the same VXLAN segment, run the vni head-end peer-list command to configure an ingress replication list that contains the IP addresses of those remote VTEPs. After the source NVE receives BUM packets, the local VTEP sends a copy of the BUM packets to every VTEP in the list.

**Precautions**

- You need to run the vni head-end peer-list command to configure the corresponding VTEP address even if the source VTEP matches only one destination VTEP.

- Run the ping command to check whether a reachable route exists between two ends of the tunnel. If there is a reachable route, the tunnel can be established and packets can be normally forwarded. If the two devices have a route to each other but the route is unreachable, the tunnel can still go Up but packets cannot be forwarded.

- Currently, the device can forward BUM packets only through ingress replication. To establish a VXLAN tunnel between the device and a nonHuawei device, ensure that ingress replication is also configured on the nonHuawei device. Otherwise, the VXLAN tunnel cannot be established.

**Example:**

```text
# Configure an ingress replication list for VNI 10, with the remote VTEPs' IP
```

addresses being 10.1.1.1 and 10.1.1.3.

```text
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] vxlan vni 10
[HUAWEI-bd10] quit
[HUAWEI] interface nve 1
[HUAWEI-Nve1] vni 10 head-end peer-list 10.1.1.1 10.1.1.3
```

**Related Topics:**

- 18.1.14 display vxlan peer


### `vxlan statistics enable`

> **Página:** 51 · **Views (Modo):** NVE interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The vxlan statistics enable command enables statistics collection on VXLAN tunnel packets. The undo vxlan statistics enable command disables statistics collection on VXLAN tunnel packets. By default, statistics collection on VXLAN tunnel packets is disabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
vxlan statistics peer peer-ip-address [ vni vni-id ] enable
undo vxlan statistics peer peer-ip-address [ vni vni-id ] enable
```

**Parameters:**

- `peer peer-ip- address` — Specifies the IPv4 address of the destination VTEP. — *Valores:* The value is in dotted decimal notation.
- `vni vni-id` — Specifies a VNI ID. If vni vni-id is specified, the device collects packet statistics based on the VXLAN tunnel and VNI. If vni vni-id is not specified, the device collects packet statistics based on the VXLAN tunnel only. — *Valores:* The value is an integer that ranges from 1 to 16777215.

**Usage Guidelines:**

VXLAN tunnel packet statistics provide information about the number of packets going into and leaving a VXLAN tunnel. To view VXLAN tunnel packet statistics, run the vxlan statistics enable and 18.1.15 display vxlan statistics commands in sequence. Packet statistics collection based on the VXLAN tunnel and VNI and packet statistics collection based on the VXLAN tunnel are mutually exclusive. For example, if the vxlan statistics peer 10.1.1.1 vni 10 enable command is configured, do not configure the vxlan statistics peer 10.1.1.1 enable command. If the vxlan statistics peer 10.1.1.1 enable command is configured, do not configure the vxlan statistics peer 10.1.1.1 vni 10 enable command.

**Example:**

```text
# Enable statistics collection on VXLAN tunnel packets with 10.1.1.1 as the
```

destination VTEP IP address.

```text
<HUAWEI> system-view
[HUAWEI] interface nve 1
[HUAWEI-Nve1] vxlan statistics peer 10.1.1.1 enable
```


### `vxlan vni (BD view)`

> **Página:** 52 · **Views (Modo):** BD view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The vxlan vni command associated a specified VNI with a BD. The undo vxlan vni command restores the default settings. By default, no VNI is associated with a BD.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
vxlan vni vni-id
undo vxlan vni vni-id
```

**Parameters:**

- `vni-id` — Specifies a VNI ID. — *Valores:* The value is an integer that ranges from 1 to 16777215.

**Usage Guidelines:**

Similar to VLAN ID, VNI is used to distinguish VXLAN segments. On the VXLAN network, one VXLAN segment is a large Layer 2 BD; therefore, VNI and BD have a one-to-one mapping relationship. You can run this command to configure the mapping relationship between VNIs and BDs. In this way, the VTEP can forward received packets through a correct VXLAN tunnel based on the mapping between BDs and VNIs.

**Example:**

```text
# Set the mapping between VNI 10 and BD 10.
<HUAWEI> system-view
[HUAWEI] bridge-domain 10
[HUAWEI-bd10] vxlan vni 10
```
