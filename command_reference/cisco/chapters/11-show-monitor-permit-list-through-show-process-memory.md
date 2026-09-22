# Capítulo 11: show monitor permit list through show process memory

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## show gsr through show monitor event trace

### show monitor permit list through show process

### memory

• show monitor permit list through show process memory, on page 772

### show monitor permit list through show process memory

### `show monitor permit-list`

> **Página:** 796 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the permit-list state and interfaces configured, use the show monitor permit-list command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show monitor permit-list
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SXE | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to display the permit-list state and interfaces configured:

```text
show monitor permit-list
SPAN Permit-list :Admin Enabled
Permit-list ports :Gi5/1-4,Gi6/1
Router(config)#
```


### `show monitor session`

> **Página:** 796 · **Modo:** User EXEC (>) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display information about the ERSPAN, SPAN and RSPAN sessions, use the show monitor session command in user EXEC mode.

**Syntax:**

```text
show monitor session [range session-range | local | remote | allsession]
show monitor session [erspan-destination | erspan-source | egress replication-mode capability |
detail]
```

**Parameters (Syntax Description):**

- `range session-range` — ( Optional) D is p l a y s a range of sessions; v a l id values are from1 to66.
- `local` — ( Optional) D is p l a y s only l o c a l SPAN sessions.
- `remote` — ( Optional) D is p l a y s both R SPAN source and destination sessions.
- `all` — ( Optional) D is p l a y s all sessions.
- `session` — ( Optional) Number of these s s i on; v a l id values are from1 to66.
- `erspan-destination` — ( Optional) D is p l a y s information about the destination E R SPAN sessions only. This keyword is not supported on the Supervisor Engine2.
- `erspan-source` — ( Optional) D is p l a y s information about the source E R SPAN sessions only. This keyword is not supported on the Supervisor Engine2.
- `egress replication-mode c apa b i l it y` — ( Optional) D is p l a y s the o p e r at i on a l mode and configure d mode of the session and module session c apa b i l it i e s.
- `detail` — ( Optional) D is p l a y s detailed session information.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC (>)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | This command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support was added for the Supervisor Engine2. |
| 12.2(18)SXE | Support was added for the e r span-destination and e r span-source keywords on the Supervisor E n g in e720 only. |
| 12.2(18)SXF | This command was u p d at e d as f o l low s: • Support was added for the Supervisor E n g in e32. • E R SPAN is supported in any switch f a b r i c module f u n c t i on a l it y switch in g mode. |
| 12.2(33)SXH | The egress replication-mode c apa b i l it y keywords were added. |

**Usage Guidelines:**

The erspan-destination and erspan-sourcekeywords are not supported on Catalyst 6500 series switches that are configured with a Supervisor Engine 2. In releases prior to Release 12.2(18)SXF, ERSPAN is supported on Catalyst 6500 series switches that are operating in compact switch fabric module functionality switching mode only. Release 12.2(18)SXF and later releases support ERSPAN in any switch fabric module functionality switching mode. If the switch fabric module functionality switching mode is set to compact, the output of the show commands display “dcef mode” for fabric-enabled modules with DFC3 installed and display “fabric mode” for other fabric-enabled modules. If the switch fabric module functionality switching mode is set to truncated, the output of the show commands display “fabric mode” for all fabric-enabled modules. When entering a range of sessions, use a dash (-) to specify a range and separate multiple entries with a comma (,). Do not enter spaces before or after the comma or the dash. You can enter multiple ranges by separating the ranges with a comma. If you enter the show monitor session command without specifying a session, the information for all sessions is displayed.

**Example:**

This example shows how to display the saved version of the monitor configuration for a specific session:

```text
Router# show monitor session 2
Session 2
------------
Type : Remote Source Session
Source Ports:
RX Only: Fa1/1-3
Dest RSPAN VLAN: 901
```

This example shows how to display the detailed information from a saved version of the monitor configuration for a specific session:

```text
Router# show monitor session 2 detail
Session 2
------------
Type : Remote Source Session
Source Ports:
RX Only: Fa1/1-3
TX Only: None
Both: None
Source VLANs:
RX Only: None
TX Only: None
Both: None
Source RSPAN VLAN: None
Destination Ports: None
Filter VLANs: None
Dest RSPAN VLAN: 901
```

This example shows how to display information about the egress replication mode only:

```text
Router# show monitor session egress replication-mode capability
No SPAN configuration is present in the system.
-------------------------------------------------------
Global Egress SPAN Replication Mode Capability:
Slot Egress Replication Capability
No LSPAN RSPAN ERSPAN
-------------------------------------------------------
3 Distributed Distributed Distributed
5 Distributed Distributed Distributed
```

This example shows how to display information about the destination ERSPAN sessions only:

```text
show monitor session erspan-destination
Session 2
---------
Type : ERSPAN Destination Session
Status : Admin Disabled
```

This example shows how to display detailed information about the destination ERSPAN sessions only:

```text
Router# show monitor session erspan-destination detail
Session 2
---------
Type : ERSPAN Destination Session
Status : Admin Disabled
Description : -
Source Ports :
RX Only : None
TX Only : None
Both : None
Source VLANs :
RX Only : None
TX Only : None
Both : None
Source RSPAN VLAN : None
Destination Ports : None
Filter VLANs : None
Destination RSPAN VLAN : None
Source IP Address : None
Source IP VRF : None
Source ERSPAN ID : None
Destination IP Address : None
Destination IP VRF : None
Destination ERSPAN ID : None
Origin IP Address : None
IP QOS PREC : 0
IP TTL : 255
```

This example shows how to display information about the source ERSPAN sessions only:

```text
show monitor session erspan-source
Session 1
---------
Type : ERSPAN Source Session
Status : Admin Disabled
Session 3
---------
Type : ERSPAN Source Session
Status : Admin Disabled
```

This example shows how to display detailed information about the source ERSPAN sessions only:

```text
Router# show monitor session erspan-source detail
Session 1
---------
Type : ERSPAN Source Session
Status : Admin Disabled
Description : -
Source Ports :
RX Only : None
TX Only : None
Both : None
Source VLANs :
RX Only : None
TX Only : None
Both : None
Source RSPAN VLAN : None
Destination Ports : None
Filter VLANs : None
Destination RSPAN VLAN : None
Source IP Address : None
Source IP VRF : None
Source ERSPAN ID : None
Destination IP Address : None
Destination IP VRF : None
Destination ERSPAN ID : None
Origin IP Address : None
IP QOS PREC : 0
IP TTL : 255
Session 3
---------
Type : ERSPAN Source Session
Status : Admin Disabled
Description : -
Source Ports :
RX Only : None
TX Only : None
Both : None
Source VLANs :
RX Only : None
TX Only : None
Both : None
Source RSPAN VLAN : None
Destination Ports : None
Filter VLANs : None
Destination RSPAN VLAN : None
Source IP Address : None
Source IP VRF : None
Source ERSPAN ID : None
Destination IP Address : None
Destination IP VRF : None
Destination ERSPAN ID : None
Origin IP Address : None
IP QOS PREC : 0
IP TTL : 255
```

This example shows how to display the operational mode and configured mode of the session and module session capabilities:

```text
Router# show monitor session egress replication-mode capability
Session 65 Type Local Session
-----------------------------------------------
Operational mode of egress span replication : Centralized
Configured mode of egress span replication : Distributed/Default
Slot Egress Replication Capability
-----------------------------------------------
1 Centralized
3 Centralized
5 Centralized
```


### `show msfc`

> **Página:** 801 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display Multilayer Switching Feature Card (MSFC) information, use the show msfc command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show msfc {buffers | eeprom | fault | netint | tlb}
```

**Parameters (Syntax Description):**

- `buffers` — D is p l a y s buffer-alloc at i on information.
- `eeprom` — D is p l a y s the in t e r n a l information.
- `fault` — D is p l a y s f a u l t information.
- `netint` — D is p l a y s network-interrupt information.
- `tlb` — D is p l a y s information about the T L B register s.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

These examples display the show msfc command output:

```text
Router# show msfc buffers
Reg. set Min Max
TX 640
ABQ 640 16384
0 0 40
1 6715 8192
2 0 0
3 0 0
4 0 0
5 0 0
6 0 0
7 0 0
Threshold = 8192
Vlan Sel Min Max Cnt Rsvd
1016 1 6715 8192 0 0
Router# show msfc eeprom
RSFC CPU IDPROM:
IDPROM image:
(FRU is 'Cat6k MSFC 2 daughterboard')
IDPROM image block #0:
hexadecimal contents of block:
00: AB AB 01 90 13 22 01 00 00 02 60 03 00 EA 43 69 ....."....`...Ci
10: 73 63 6F 20 53 79 73 74 65 6D 73 00 00 00 00 00 sco Systems.....
20: 00 00 57 53 2D 46 36 4B 2D 4D 53 46 43 32 00 00 ..WS-F6K-MSFC2..
30: 00 00 00 00 00 00 53 41 44 30 36 32 31 30 30 36 ......SAD0621006
40: 37 00 00 00 00 00 00 00 00 00 37 33 2D 37 32 33 7.........73-723
50: 37 2D 30 33 00 00 00 00 00 00 41 30 00 00 00 00 7-03......A0....
60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
70: 00 00 00 02 00 03 00 00 00 00 00 09 00 05 00 01 ................
80: 00 03 00 01 00 01 00 02 00 EA FF DF 00 00 00 00 ................
block-signature = 0xABAB, block-version = 1,
block-length = 144, block-checksum = 4898
*** common-block ***
IDPROM capacity (bytes) = 256 IDPROM block-count = 2
FRU type = (0x6003,234)
OEM String = 'Cisco Systems'
Product Number = 'WS-F6K-MSFC2'
Serial Number = 'SAD06210067'
Manufacturing Assembly Number = '73-7237-03'
Manufacturing Assembly Revision = 'A0'
Hardware Revision = 2.3
Manufacturing bits = 0x0 Engineering bits = 0x0
SNMP OID = 9.5.1.3.1.1.2.234
Power Consumption = -33 centiamperes RMA failure code = 0-0-0-0
*** end of common block ***
IDPROM image block #1:
hexadecimal contents of block:
00: 60 03 01 62 0A C2 00 00 00 00 00 00 00 00 00 00 `..b............
10: 00 00 00 00 00 01 00 23 00 08 7C A4 CE 80 00 40 .......#..|....@
20: 01 01 00 01 00 00 00 00 00 00 00 00 00 00 00 00 ................
30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
40: 14 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
50: 10 00 4B 3C 41 32 80 80 80 80 80 80 80 80 80 80 ..K<A2..........
60: 80 80 ..
block-signature = 0x6003, block-version = 1,
block-length = 98, block-checksum = 2754
*** linecard specific block ***
feature-bits = 00000000 00000000
hardware-changes-bits = 00000000 00000001
card index = 35
mac base = 0008.7CA4.CE80
mac_len = 64
num_processors = 1
epld_num = 1
epld_versions = 0001 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 00
00 0000 0000
port numbers:
pair #0: type=14, count=01
pair #1: type=00, count=00
pair #2: type=00, count=00
pair #3: type=00, count=00
pair #4: type=00, count=00
pair #5: type=00, count=00
pair #6: type=00, count=00
pair #7: type=00, count=00
sram_size = 4096
sensor_thresholds =
sensor #0: critical = 75 oC, warning = 60 oC
sensor #1: critical = 65 oC, warning = 50 oC
sensor #2: critical = -128 oC (sensor not present), warning = -128 oC (senso
r not present)
sensor #3: critical = -128 oC (sensor not present), warning = -128 oC (senso
r not present)
sensor #4: critical = -128 oC (sensor not present), warning = -128 oC (senso
r not present)
sensor #5: critical = -128 oC (sensor not present), warning = -128 oC (senso
r not present)
sensor #6: critical = -128 oC (sensor not present), warning = -128 oC (senso
r not present)
sensor #7: critical = -128 oC (sensor not present), warning = -128 oC (senso
r not present)
*** end of linecard specific block ***
End of IDPROM image
Router# show msfc fault
Reg. set Min Max
TX 640
ABQ 640 16384
0 0 40
1 6715 8192
2 0 0
3 0 0
4 0 0
5 0 0
6 0 0
7 0 0
Threshold = 8192
Vlan Sel Min Max Cnt Rsvd
1016 1 6715 8192 0 0
Router# show msfc netint
Network IO Interrupt Throttling:
throttle count=0, timer count=0
active=0, configured=1
netint usec=3999, netint mask usec=400
Router# show msfc tlb
Mistral revision 3
TLB entries : 37
Virt Address range Phy Address range Attributes
0x10000000:0x1001FFFF 0x010000000:0x01001FFFF CacheMode=2, RW, Valid
0x10020000:0x1003FFFF 0x010020000:0x01003FFFF CacheMode=2, RW, Valid
0x10040000:0x1005FFFF 0x010040000:0x01005FFFF CacheMode=2, RW, Valid
0x10060000:0x1007FFFF 0x010060000:0x01007FFFF CacheMode=2, RW, Valid
0x10080000:0x10087FFF 0x010080000:0x010087FFF CacheMode=2, RW, Valid
0x10088000:0x1008FFFF 0x010088000:0x01008FFFF CacheMode=2, RW, Valid
0x18000000:0x1801FFFF 0x010000000:0x01001FFFF CacheMode=0, RW, Valid
0x19000000:0x1901FFFF 0x010000000:0x01001FFFF CacheMode=7, RW, Valid
0x1E000000:0x1E1FFFFF 0x01E000000:0x01E1FFFFF CacheMode=2, RW, Valid
0x1E880000:0x1E881FFF 0x01E880000:0x01E881FFF CacheMode=2, RW, Valid
0x1FC00000:0x1FC7FFFF 0x01FC00000:0x01FC7FFFF CacheMode=2, RO, Valid
0x30000000:0x3001FFFF 0x070000000:0x07001FFFF CacheMode=2, RW, Valid
0x40000000:0x407FFFFF 0x000000000:0x0007FFFFF CacheMode=3, RO, Valid
0x40800000:0x40FFFFFF 0x000800000:0x000FFFFFF CacheMode=3, RO, Valid
0x41000000:0x417FFFFF 0x001000000:0x0017FFFFF CacheMode=3, RO, Valid
0x41800000:0x419FFFFF 0x001800000:0x0019FFFFF CacheMode=3, RO, Valid
0x41A00000:0x41A7FFFF 0x001A00000:0x001A7FFFF CacheMode=3, RO, Valid
0x41A80000:0x41A9FFFF 0x001A80000:0x001A9FFFF CacheMode=3, RO, Valid
0x41AA0000:0x41ABFFFF 0x001AA0000:0x001ABFFFF CacheMode=3, RO, Valid
0x41AC0000:0x41AC7FFF 0x001AC0000:0x001AC7FFF CacheMode=3, RO, Valid
0x41AC8000:0x41ACFFFF 0x001AC8000:0x001ACFFFF CacheMode=3, RO, Valid
0x41AD0000:0x41AD7FFF 0x001AD0000:0x001AD7FFF CacheMode=3, RO, Valid
0x41AD8000:0x41AD9FFF 0x001AD8000:0x001AD9FFF CacheMode=3, RO, Valid
0x41ADA000:0x41ADBFFF 0x001ADA000:0x001ADBFFF CacheMode=3, RW, Valid
0x41ADC000:0x41ADDFFF 0x001ADC000:0x001ADDFFF CacheMode=3, RW, Valid
0x41ADE000:0x41ADFFFF 0x001ADE000:0x001ADFFFF CacheMode=3, RW, Valid
0x41AE0000:0x41AFFFFF 0x001AE0000:0x001AFFFFF CacheMode=3, RW, Valid
0x41B00000:0x41B7FFFF 0x001B00000:0x001B7FFFF CacheMode=3, RW, Valid
0x41B80000:0x41BFFFFF 0x001B80000:0x001BFFFFF CacheMode=3, RW, Valid
0x41C00000:0x41DFFFFF 0x001C00000:0x001DFFFFF CacheMode=3, RW, Valid
0x41E00000:0x41FFFFFF 0x001E00000:0x001FFFFFF CacheMode=3, RW, Valid
0x42000000:0x43FFFFFF 0x002000000:0x003FFFFFF CacheMode=3, RW, Valid
0x44000000:0x45FFFFFF 0x004000000:0x005FFFFFF CacheMode=3, RW, Valid
0x46000000:0x47FFFFFF 0x006000000:0x007FFFFFF CacheMode=3, RW, Valid
0x06E00000:0x06FFFFFF 0x006E00000:0x006FFFFFF CacheMode=2, RW, Valid
0x07000000:0x077FFFFF 0x007000000:0x0077FFFFF CacheMode=2, RW, Valid
0x07800000:0x07FFFFFF 0x007800000:0x007FFFFFF CacheMode=2, RW, Valid
```


### `show pagp`

> **Página:** 804 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display port-channel information, use the show pagp command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show pagp [group-number] {counters | internal | neighbor | pgroup}
```

**Parameters (Syntax Description):**

- `group-number` — ( Optional) C h an n e l-group number; v a l id values are a maximum of64 values from1 to282.
- `counters` — D is p l a y s the traffic information.
- `in t e r n a l` — D is p l a y s the in t e r n a l information.
- `n e i g h b or` — D is p l a y s then e i g h b or information.
- `pgroup` — D is p l a y s the a c t i v e port c h an n e l s.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You can enter any show pagp command to display the active port-channel information. To display the nonactive information, enter the show pagp command with a group. The port-channel numbervalues from 257 to 282 are supported on the CSM and the FWSM only.

**Example:**

This example shows how to display information about the PAgP counters:

```text
show pagp
counters
Information Flush
Port Sent Recv Sent Recv
--------------------------------------
Channel group: 1
Fa5/4 2660 2452 0 0
Fa5/5 2676 2453 0 0
Channel group: 2
Fa5/6 289 261 0 0
Fa5/7 290 261 0 0
Channel group: 1023
Fa5/9 0 0 0 0
Channel group: 1024
Fa5/8 0 0 0 0
```

This example shows how to display internal PAgP information:

```text
Router# show pagp
1 internal
Flags: S - Device is sending Slow hello. C - Device is in Consistent state.
A - Device is in Auto mode.
Timers: H - Hello timer is running. Q - Quit timer is running.
S - Switching timer is running. I - Interface timer is running.
Channel group 1
Hello Partner PAgP Learning
Port Flags State Timers Interval Count Priority Method
Fa5/4 SC U6/S7 30s 1 128 Any
Fa5/5 SC U6/S7 30s 1 128 Any
```

This example shows how to display PAgP-neighbor information for all neighbors:

```text
Router# show pagp
neighbor
Flags: S - Device is sending Slow hello. C - Device is in Consistent state.
A - Device is in Auto mode. P - Device learns on physical port.
Channel group 1 neighbors
Partner Partner Partner Partner Group
Port Name Device ID Port Age Flags Cap.
Fa5/4 JAB031301 0050.0f10.230c 2/45 2s SAC 2D
Fa5/5 JAB031301 0050.0f10.230c 2/46 27s SAC 2D
Channel group 2 neighbors
Partner Partner Partner Partner Group
Port Name Device ID Port Age Flags Cap.
Fa5/6 JAB031301 0050.0f10.230c 2/47 10s SAC 2F
Fa5/7 JAB031301 0050.0f10.230c 2/48 11s SAC 2F
Channel group 1023 neighbors
Partner Partner Partner Partner Group
Port Name Device ID Port Age Flags Cap.
Channel group 1024 neighbors
Partner Partner Partner Partner Group
Port Name Device ID Port Age Flags Cap.
```


### `show parser dump`

> **Página:** 806 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** Note Effective with Cisco IOS Release 15.0(1)M, the show parser dump command is not available in Cisco IOS software. To display the command-line interface (CLI) syntax options for all command modes or for a specified command mode, use the show parser dump command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show parser dump {command-mode | all} [privilege-level level] [extend] [breakage]
```

**Parameters (Syntax Description):**

- `command-mode` — A keyword in d i c at in gt h e command mode. The output will include the syntax for commands only in the specified command mode. The list of command mode keywords will v a r y d e p end in g on your software image. Use the show parser dump? command to d is p l a y the list of command mode keyword options. For f u r the r as s is t an c e in d e t e r min in gt h e p r o p e r command mode, see the“ Cisco IOS Command Modes” Release 12.2 document, a v a i l a b l e on Cisco. com.
- `all` — In d i c at e s that all commands in all modes should be d is p l a y e d in the output. Caution This keyword generate save r y l a r g e a mount of output, which may e x c e e d your system or buffer memory.
- `privilege-level level` — ( Optional) List s C L I commands only with the privilege levels p e c if i e d in the level argument.
- `extend` — ( Optional) Enable s the e x t end e d d is p l a y mode. The e x t end e d parser d is p l a y shows the keyword and argument descriptions t y p i c all y show n with the command-line help (? command). Note This keyword can p r o d u c e a l a r g e a mount of output.
- `break age` — ( Optional) Enable s detect i on of p o t e n t i a l parser c h a in syntax break age. This keyword is in t end e d for in t e r n a l use.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(4)T | This command was introduced. |
| 12.2(13)T | This command was e n h an c e d to r e s o l v e c e r t a in exec u t i one r r or s. |
| 12.0(23)S | This command was e n h an c e d to r e s o l v e c e r t a in exec u t i one r r or s. |
| 15.0(1)M | This command was removed. |

**Usage Guidelines:**

This command was developed to allow the exploration of the CLI command syntax without requiring the user to actually enter a specific mode and use the ? command-line help. Caution Use caution when entering this command with the all keyword. A large amount of output can be generated by this command, which may easily exceed buffer or system memory on smaller platforms. Also, some configuration modes have hundreds of valid commands. For large dumps, use of the redirection to a file using the | redirect URL syntax at the end of the command is highly recommended. (See the documentation for the command for more information on using this command extension.) showcommand redirect Output for this command will show the syntax options for all commands available in the specified mode. The number preceding the command shows the privilege level associated with that command. For example, the line

```text
15 type dhcp
```

indicates that the type dhcp command has a privilege level of 15 assigned to it. For information about privilege levels, see the “Configuring Passwords and Privileges” chapter in the Cisco IOS Security Configuration Guide Any given command-line string should indicate the full syntax needed to make the command complete and valid. In other words, the command-line string ends where the carriage return (Enter) could be entered, as indicated in command-line help by the <cr> syntax. You will typically see multiple forms of a command, each showing a valid syntax combination. For example, each of the following syntax combinations, as seen in the output of the show parser dump rtr | include dhcp command, is a valid command:

```text
type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82> circuit-id <string>
type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82> remote-id <string>
type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82> subnet-mask <ipmask>
type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82>
type dhcp dest-ipaddr <address> source-ipaddr <address>
type dhcp dest-ipaddr <address>
type dhcp
```

Use of the show command extensions | begin, | include, and | exclude is recommended for this command because these extensions allow you to filter the output to display only the commands you are interested in. The redirection extensions | redirect, | append, and | tee allow you to redirect the output of this command to local or remote storage as a file. As with most show commands, you can typically exit from the --More-- prompt back to EXEC mode using Ctrl-Z. For some connections, Ctrl-Shift-6 (Ctrl^) or Ctrl-Shift-6-X should be used instead.

**Example:**

The following example shows a typical list of command mode keywords. The fields are self-explanatory.

```text
show parser dump ?
aaa-attr-list AAA attribute list config mode
aaa-user AAA user definition
accept-dialin VPDN group accept dialin configuration mode
accept-dialout VPDN group accept dialout configuration mode
acct_mlist AAA accounting methodlist definitions
address-family Address Family configuration mode
aic Alarm Interface Card configuration mode
all For all modes
alps-ascu ALPS ASCU configuration mode
alps-circuit ALPS circuit configuration mode
appfw-application-aim Appfw for AIM Configuration Mode
appfw-application-msnmsgr Appfw for MSN Messenger Configuration Mode
appfw-application-ymsgr Appfw for Yahoo! Messenger Configuration Mode
appfw-policy Application FW Policy Configuration Mode
application-http Appfw for HTTP Configuration Mode
archive Archive the router configuration mode
atalk-test Appletalk test mode
atm-bm-config ATM bundle member configuration mode
atm-bundle-config ATM bundle configuration mode
atm-l2trans-pvc-config ATM L2transport PVC configuration mode
atm-l2trans-pvp-config ATM L2transport PVP configuration mode
atm-pvc-range-config ATM PVC Range configuration mode
atm-range-pvc-config ATM PVC in Range configuration mode
atm-svc-bm-config ATM SVC bundle member configuration mode
atm-svc-bundle-config ATM SVC bundle configuration mode
atm-vc-config ATM virtual circuit configuration mode
atmsig_e164_table_mode ATMSIG E164 Table
auto-ip-sla-mpls Auto IP SLA MPLS LSP Monitor configs
auto-ip-sla-mpls-lpd-params Auto IP SLA MPLS LPD params configs
auto-ip-sla-mpls-params Auto IP SLA MPLS LSP Monitor Params configs
banner Banner Input mode
bba-group BBA Group configuration mode
boomerang Boomerang configuration mode
bsm-cfg BSM config definition
bulkstat-objlist Bulk-stat Object list configuration mode
bulkstat-schemadef Bulk-stat schema configuration mode
bulkstat-transfer Bulk Stat configuration mode
cascustom Cas custom configuration mode
call-filter-matchlist Call Filter matchlist configuration mode
call-home call-home config mode
call-home-profile call-home profile config mode
call-router AnnexG configuration mode
cascustom Cas custom configuration mode
cause-code-list Voice Cause Code List configuration mode
cfg-path IP Host backup configuration mode
cfg-pt-ruleset Protocol Translation ruleset configuration mode
cip-vadp Virtual Adapter configuration mode
cip-vlan Virtual Lan configuration mode
clid-group CLID group configuration mode
cm-ac AC-AC connect configuration mode
cm-fallback cm-fallback configuration mode
cns-connect-intf-config CNS Connect Intf Info Mode
cns-connect-config CNS Connect Info Mode
cns-tmpl-connect-config CNS Template Connect Info Mode
cns_inventory_submode CNS Inventory SubMode
codec-profile Codec Profile configuration mode
conf-dia-attr-list Diameter attribute list config mode
conf-dia-peer Diameter peer config mode
conf-dia-sg Diameter peer group config mode
config-ip-sla-http-rr IP SLAs HTTP raw request Configuration
config-l2tp-class l2tp-class configuration mode
config-tgrep TRIP-Lite configuration mode
config-rtr-http-rr RTR HTTP raw request Configuration
config-x25-huntgroup X.25 hunt group configuration mode
config_app_global Configure global settings
config_app_map Configure application mapping
config_app_monitor Configure application monitoring
config_app_session Define script processes
config_voice Define application services, modules, groups
config_voice_app Define application parameters
configure Global configuration mode
congestion Frame Relay congestion configuration mode
control-plane Control Plane configuration mode
control-plane-cef-exception-mode Control Plane cef-exception configuration mode
control-plane-host-mode Control Plane host configuration mode
control-plane-transit-mode Control Plane transit configuration mode
controller Controller configuration mode
cpf-classmap Class-map configuration mode
cpf-policyclass Class-in-Policy configuration mode
cpf-policymap Policy-map configuration mode
cpu config-owner-cpu
crypto-ca-cert-chain Crypto certificate entry mode
crypto-ca-cert-comm Certificate query mode
crypto-ca-cert-map Certificate map entry mode
crypto-ca-profile-enroll Certificate enrollment profile entry mode
crypto-ca-root Certificate authority trusted root entry mode
crypto-ca-trustpoint Certificate authority trustpoint entry mode
crypto-cs-server Certificate Server entry mode
crypto-gdoi-group Crypto GDOI group policy config mode
crypto-identity Crypto identity config mode
crypto-ikmp Crypto ISAKMP config mode
crypto-ikmp-browser-proxy Crypto ISAKMP browser proxy config mode
crypto-ikmp-client-fw Crypto ISAKMP client firewall policy config mode
crypto-ikmp-group Crypto ISAKMP group policy config mode
crypto-ikmp-peer Crypto ISAKMP peer policy configuration mode
crypto-ipsec-profile IPSec policy profile mode
crypto-keyring Crypto Keyring command mode
crypto-map Crypto map config mode
crypto-map-fail-close Crypto map fail close mode
crypto-pubkey Crypto subsystem public key entry mode
crypto-transform Crypto transform config mode
crypto-tti-petitioner TTI Petitioner entry mode
crypto-tti-registrar TTI Registrar entry mode
decnet-map DECnet map configuration mode
dfp-submode DFP config mode
dhcp DHCP pool configuration mode
dhcp-class DHCP class configuration mode
dhcp-pool-class Per DHCP pool class configuration mode
dhcp-relay-info DHCP class relay agent info configuration mode
dhcp-subnet-secondary Per DHCP secondary subnet configuration mode
dnis-group DNIS group configuration mode
dns-view DNS View configuration mode
dns-view-list DNS View-list configuration mode
dns-view-list-member DNS View-list member configuration mode
dspfarm DSP farm configuration mode
dspfarmprofile Profile configuration mode
dynupd-http Dynamic DNS update HTTP configuration mode
dynupd-method Dynamic DNS update method configuration mode
emergency-response-location voice emergency response location configuration mode
emergency-response-settings voice emergency response settings configuration mode
emergency-response-zone voice emergency response zone configuration mode
enum_rule enum configuration mode
ephone ephone configuration mode
ephone-dn ephone-dn configuration mode
ephone-dn-template ephone-dn-template configuration mode
ephone-hunt ephone-hunt configuration mode
ephone-template ephone-template configuration mode
ephone-type ephone-type configuration mode
ether_cfm Ethernet CFM configuration mode
event Event MIB event configuration mode
event-action-notification Event MIB event action notification configuration mode
event-action-set Event MIB event action set configuration mode
event-objlist Event MIB object list configuration mode
event-trigger Event MIB event trigger configuration mode
event-trigger-boolean Event MIB event trigger boolean configuration mode
event-trigger-existence Event MIB event trigger existence configuration mode
event-trigger-object-id Event MIB trigger object id configuration mode
event-trigger-threshold Event MIB event trigger threshold configuration mode
exec Exec mode
expr-expression Expression configuration mode
expr-object Expression Object configuration mode
extcomm-list IP Extended community-list configuration mode
fh_applet FH Applet Entry Configuration
fh_applet_trigger FH Applet Trigger Configuration
filter Output filter mode
filterserver AAA filter server definitions
flow-cache Flow aggregation cache config mode
flow-sampler-map Flow sampler map config mode
flowexp Flow Exporter configuration mode
flowmon Flow Monitor configuration mode
flowrec Flow Record configuration mode
fr-fr FR/FR connection configuration mode
fr-pw FR/PW connection configuration mode
fr-vcb-bmode FR VC Bundle mode
fr-vcb-mmode FR VC Bundle Member mode
frf5 FR/ATM Network IWF configuration mode
frf8 FR/ATM Service IWF configuration mode
funi-vc-config FUNI virtual circuit configuration mode
gatekeeper Gatekeeper config mode
gateway Gateway configuration mode
gdoi-coop-ks-config Crypto GDOI server redundancy config mode
gdoi-local-server Crypto GDOI local server policy config mode
gdoi-sa-ipsec Crypto GDOI local server IPsec SA policy config mode
gg_fcpa-config FC tunnel configuration mode
gk_altgk_cluster GK Commands for Cluster defn
gk_be_annexg GK Commands for H.323 AnnexG configuration
gk_srv_trigger_arq GK Server ARQ Trigger config mode
gk_srv_trigger_brq GK Server BRQ Trigger config mode
gk_srv_trigger_drq GK Server DRQ Trigger config mode
gk_srv_trigger_irr GK Server IRR Trigger config mode
gk_srv_trigger_lcf GK Server LCF Trigger config mode
gk_srv_trigger_lrj GK Server LRJ Trigger config mode
gk_srv_trigger_lrq GK Server LRQ Trigger config mode
gk_srv_trigger_rai GK Server RAI Trigger config mode
gk_srv_trigger_rrq GK Server RRQ Trigger config mode
gk_srv_trigger_urq GK Server URQ Trigger config mode
gw Webvpn virtual gateway configuration
gw-accounting-aaa Gateway accounting aaa configuration mode
gw-accounting-file Gateway accounting file configuration mode
hostlist Host list configuration mode
identity-policy-mode identity policy configuration mode
identity-profile-mode identity profile configuration mode
interface Interface configuration mode
interface range Interface range configuration mode
interface-dlci Frame Relay dlci configuration mode
ip-explicit-path IP explicit path configuration mode
ip-sla IP SLAs entry configuration
ip-sla-am-grp IP SLAs auto group config
ip-sla-am-grp-auto IP SLAs auto group dest-auto config
ip-sla-am-schedule IP SLAs auto schedule config
ip-sla-dhcp IP SLAs dhcp configuration
ip-sla-dns IP SLAs dns configuration
ip-sla-echo IP SLAs echo configuration
ip-sla-ethernet-echo IP SLAs Ethernet Echo configuration
ip-sla-ethernet-jitter IP SLAs Ethernet Jitter configuration
ip-sla-ethernet-monitor IP SLAs Ethernet configs
ip-sla-ethernet-monitor-params IP SLAs Ethernet Params configs
ip-sla-frameRelay IP SLAs FrameRelay configuration
ip-sla-ftp IP SLAs ftp configuration
ip-sla-http IP SLAs http configuration
ip-sla-icmp-ech-params IP SLAs icmpEcho Parameters
ip-sla-icmp-jtr-params IP SLAs icmpJitter Parameters
ip-sla-icmpjitter IP SLAs icmpjitter configuration
ip-sla-jitter IP SLAs jitter configuration
ip-sla-pathEcho IP SLAs pathEcho configuration
ip-sla-pathJitter IP SLAs pathJitter configuration
ip-sla-tcp-conn-params IP SLAs tcpConnect Parameters
ip-sla-tcpConnect IP SLAs tcpConnect configuration
ip-sla-tplt-dest IP SLAs auto destination submode
ip-sla-tplt-icmp-ech IP SLAs auto template icmpEcho
ip-sla-tplt-icmp-jtr IP SLAs auto template icmpJitter
ip-sla-tplt-tcp-conn IP SLAs auto template tcpConnect
ip-sla-tplt-udp-ech IP SLAs auto template udpEcho
ip-sla-tplt-udp-jtr IP SLAs auto template udpJitter
ip-sla-udp-ech-params IP SLAs udpEcho Parameters
ip-sla-udp-jtr-params IP SLAs udpJitter Parameters
ip-sla-udpEcho IP SLAs udpEcho configuration
ip-sla-voip IP SLA voip configuration
ip-sla-voip-rtp IP SLAs rtp configuration
ip-vrf Configure IP VRF parameters
ipc-zone-assoc-protocol-sctp ipc protocol sctp mode
ipczone IPC Zone config mode
ipczone-assoc IPC Association config mode
ipenacl IP named extended access-list configuration mode
iphc-profile-mode IPHC Profile configuration mode
ipmobile-test IP Mobility test mode
ipnat-pool IP NAT pool configuration mode
ipnat-portmap IP NAT portmap configuration mode
ipnat-sbc IP NAT SIP-SBC config mode
ipnat-sbc-vrf IP NAT SIP-SBC vrf config mode
ipnat-snat IP SNAT configuration mode
ipnat-snat-backup IP SNAT Backup configuration mode
ipnat-snat-primary IP SNAT Primary configuration mode
ipnat-snat-redundancy IP SNAT Redundancy configuration mode
ips-seap-rules IPS event action rules configuration mode
ips-sigdef-sig IPS signature number name configuration mode
ipscataction IPS Category name configuration mode
ipsnacl IP named simple access-list configuration mode
ipssigau IPS Auto Update configuration mode
ipssigcat IPS signature category configuration mode
ipssigdef-action IPS Signature actions configuration mode
ipssigdef-engine IPS signature def Engine configuration mode
ipssigdef-status IPS signature def Status mode
ipv6-mobile-router MIPv6 router configuration mode
ipv6-router IPv6 router configuration mode
ipv6acl IPv6 access-list configuration mode
ipv6dhcp IPv6 DHCP configuration mode
ipv6dhcpvs IPv6 DHCP Vendor-specific configuration mode
ipx-router IPX router configuration mode
ipxenacl IPX named extended access-list configuration mode
ipxsapnacl IPX named SAP access-list configuration mode
ipxsnacl IPX named standard access-list configuration mode
ipxsumnacl IPX named Summary access-list configuration mode
isakmp-profile Crypto ISAKMP profile command mode
iua-cfg ISDN user adaptation layer configuration
key-chain Key-chain configuration mode
key-chain-key Key-chain key configuration mode
kron-occurrence Kron Occurrence SubMode
kron-policy Kron Policy SubMode
l2 vfi configuration mode
line Line configuration mode
lw-vlan-id VLAN-id configuration mode
lw-vlan-range VLAN-range configuration mode
local-prof Local profile configuration mode
log_config Log configuration changes made via the CLI
lsp-attribute-list LSP attribute list configuration mode
map-class Map class configuration mode
map-list Map list configuration mode
memory config-owner-memory
mgcpprofile MGCP Profile configuration mode
mipv6-config-ha Mobile IPv6 HA mode
mipv6-config-ha-host Mobile IPv6 Home Agent Host config mode
mobile-map Mobile Map mode
mobile-networks Mobile Networks mode
mobile-router Mobile Router mode
mplsmfistaticifrewrite MPLS MFI static if rewrite configuration mode
mplsmfistaticrewrite MPLS MFI static rewrite configuration mode
mripv6-config-ha-host Mobile IPv6 Home Agent Host config mode
mrm-manager IP Multicast Routing Monitor config mode
neighbor Neighbor configuration mode
network-object-group ACL Object Group configuration
null-interface Null interface configuration mode
null-interface Null interface configuration mode
nxg-service-relationship Service Relationship configuration mode
nxg-usage-indication Usage Indication configuration mode
oam LSP Verification configuration mode
oer_br OER border router configuration submode
oer_mc OER master controller configuration submode
oer_mc_api_provider OER MC API Provider configuration submode
oer_mc_br OER managed border router configuration submode
oer_mc_br_if OER Border Exit configuration submode
oer_mc_learn OER Top Talker and Delay learning configuration submode
oer_mc_learn_list OER learn list configuration submode
oer_mc_map oer-map config mode
parameter_map_cfg parameter-map configuration mode
policy-list IP Policy List configuration mode
preauth AAA Preauth definitions
profile Subscriber profile configuration mode
pseudowire-class Pseudowire-class configuration mode
public-key-chain Crypto public key identification mode
public-key-chain-key Crypto public key entry mode
public-key-chain-key-ring Crypto public key entry mode
qosclassmap QoS Class Map configuration mode
qosclasspolice QoS Class Police configuration mode
qospolicymap QoS Policy Map configuration mode
qospolicymapclass QoS Policy Map class configuration mode
radius-attrl Radius Attribute-List Definition
radius-locsvr Radius Application configuration
red-group random-detect group configuration mode
redundancy redundancy config mode
regex-translation-rule voip translation-rule configuration mode
request-dialin VPDN group request dialin configuration mode
request-dialout VPDN group request dialout configuration mode
rf-mode-interdev-local ipc sctp local config mode
rf-mode-interdev-remote ipc sctp remote config mode
rf-mode-interdevice redundancy config mode
rlm-group RLM Group configuration mode
rlm-group-sc RLM server/client link configuration mode
roles Role configuration mode
route-map Route map config mode
router Router configuration mode
rsvp-local-if-policy RSVP local policy interface configuration mode
rsvp-local-policy RSVP local policy configuration mode
rsvp-local-subif-policy RSVP local policy sub-interface configuration mode
rtr SAA entry configuration
saa-dhcp SAA dhcp configuration
saa-dns SAA dns configuration
saa-echo SAA echo configuration
saa-frameRelay SAA FrameRelay configuration
saa-ftp SAA ftp configuration
saa-http SAA http configuration
saa-jitter SAA jitter configuration
saa-pathEcho SAA pathEcho configuration
saa-pathJitter SAA pathJitter configuration
saa-slm-ctrlr-if SAA SLM controller/interface configuration
saa-slmFrIf SAA SLM FrameRelay Interface configuration
saa-slmfr SAA SLM Frame Relay configuration
saa-tcpConnect SAA tcpConnect configuration
saa-udpEcho SAA udpEcho configuration
sg-radius Radius Server-group Definition
sampler Sampler configuration mode
sccpccmgroup SCCP CCM group configuration mode
sccpplar SCCP PLAR configuration mode
sctp-export SCTP export configuration commands
seczonecfg Security Zone Configuration Mode
seczonepaircfg Security Zone Pair Configuration Mode
sep-init-config WSMA Initiator profile Mode
sep-listen-config WSMA Listener profile Mode
service-object-group ACL Object Group configuration
serviceflow Service Flow configuration mode
sg-tacacs+ Tacacs+ Server-group Definition
signaling-class Signaling class configuration mode
sip-ua SIP UA configuration mode
sla-lspPing IP SLAs lsp ping configuration
sla-lspTrace IP SLAs lsp trace configuration
slb-mode-dfp SLB DFP configuration mode
slb-mode-real SLB real server configuration mode
slb-mode-sfarm SLB server farm configuration mode
slb-mode-vserver SLB virtual server configuration mode
source-group Voice Source Group configuration mode
srst-video cm-fallback video configuration mode
sss-subscriber SSS subscriber configuration mode
subinterface Subinterface configuration mode
subscriber-policy Subscriber policy configuration mode
tablemap Table Map configuration mode
tcl Tcl mode
tdm-conn TDM connection configuration mode
telephony-service telephony-service configuration mode
telephony-service-group Telephony service group configuration mode
telephony-service-video Telephony service video configuration mode
template Template configuration mode
template peer-policy peer-policy configuration mode
template peer-session peer-session configuration mode
test_cpu config-owner-test_cpu
test_mem config-owner-test_mem
tidp-group TIDP Group configuration mode
tidp-keyset TIDP key-set configuration mode
tn3270s-dlur tn3270 server DLUR configuration mode
tn3270s-dlur-pu tn3270 server DLUR PU configuration mode
tn3270s-dlur-sap tn3270 server DLUR SAP configuration mode
tn3270s-listen-point tn3270 server Listen-Point configuration mode
tn3270s-listen-point-pu tn3270 server Listen-Point PU configuration mode
tn3270s-pu tn3270 server PU configuration mode
tn3270s-resp-time tn3270 server response time client group configuration mode
tn3270s-security tn3270 server Security Configuration mode
tn3270s-security-profile tn3270 server Security Profile Configuration mode
tn3270s-svr tn3270 server configuration mode
top-talkers Netflow top talkers config mode
tracking-config Tracking configuration mode
trange time-range configuration mode
translation-profile Voice Translation Profile configuration mode
translation-rule Translation Rule configuration mode
trunk-group Trunk group configuration mode
vc-class VC class configuration mode
vc-group VC group configuration mode
view View configuration mode
vlan VLAN database editing buffer
vm-integration voicemail integration configuration mode
voice-cause-code Voice Cause Code configuration mode
voice-gateway voice gateway configuration mode
voice-mlpp voice mlpp configuration mode
voice-service Voice service configuration mode
voice-service-h323 Voice service h323 configuration mode
voice-service-session Voice service session configuration mode
voice-service-sip Voice service sip configuration mode
voice-service-stun Voice service stun configuration mode
voice-uri-class Voice URI Class configuration mode
voicecl-cptone Voice Class CPTone configuration mode
voicecl-cptone-dt CPtone dualtone configuration mode
voicecl-dt-detect Voice Class Dualtone Detect configuration mode
voiceclass Voice Class configuration mode
voicednismaps Dnis Map Configuration
voiceport Voice configuration mode
voipdialpeer Dial Peer configuration mode
voipdpcor Dial Peer Class of Restriction configuration mode
voipdpcorlist Dial Peer Class of Restriction List configuration mode
vpdn-group VPDN group configuration mode
vpdn-template VPDN template configuration mode
vrf Configure VRF parameters
webvpn Webvpn virtual context configuration
webvpn-acl Webvpn ACL configuration
webvpn-cifs-url Webvpn CIFS URL list configuration
webvpn-group-policy Webvpn group policy configuration
webvpn-nbnslist Webvpn VW ctxt NBNS list configuration
webvpn-port-fwd Webvpn port-forward list configuration
webvpn-sso-server SSO Server configuration
webvpn-time-range Webvpn time range configuration
webvpn-url Webvpn URL list configuration
webvpn-url-rewrite Webvpn url-rewrite list configuration
x25-profile X.25 profile configuration mode
xconnect-conn-config Xconnect connect configuration submode
xconnect-dlci-config Xconnect FR DLCI configuration submode
xconnect-if-config Xconnect interface configuration submode
xconnect-pvc-config Xconnect atm l2transport PVC configuration submode
xconnect-pvp-config Xconnect atm l2transport PVP configuration submode
xconnect-subif-config Xconnect sub-interface configuration submode
xml-app XML Application configuration mode
xml-transport XML Transport configuration mode
```

In the following example, only commands in RTR configuration mode are shown:

```text
Router# show parser dump rtr
Mode Name :rtr
15 type udpEcho dest-ipaddr <address> dest-port <1-65535> source-ipaddr <address> source-port
<1-65535> control enable
15 type udpEcho dest-ipaddr <address> dest-port <1-65535> source-ipaddr <address> source-port
<1-65535> control disable
15 type udpEcho dest-ipaddr <address> dest-port <1-65535> source-ipaddr <address> source-port
<1-65535>
15 type udpEcho dest-ipaddr <address> dest-port <1-65535> source-ipaddr <address>
15 type udpEcho dest-ipaddr <address> dest-port <1-65535>
15 type tcpConnect dest-ipaddr <address> dest-port <1-65535> source-ipaddr <address>
source-port <1-65535> control enable
15 type tcpConnect dest-ipaddr <address> dest-port <1-65535> source-ipaddr <address>
source-port <1-65535> control disable
15 type tcpConnect dest-ipaddr <address> dest-port <1-65535> source-ipaddr <address>
source-port <1-65535>
15 type tcpConnect dest-ipaddr <address> dest-port <1-65535> source-ipaddr <address>
15 type tcpConnect dest-ipaddr <address> dest-port <1-65535>
15 type jitter dest-ipaddr <address> dest-port <1-65535> source-ipaddr <address>
15 type jitter dest-ipaddr <address> dest-port <1-65535> source-port <1-65535>
15 type jitter dest-ipaddr <address> dest-port <1-65535> control enable
15 type jitter dest-ipaddr <address> dest-port <1-65535> control disable
15 type jitter dest-ipaddr <address> dest-port <1-65535> num-packets <1-60000>
15 type jitter dest-ipaddr <address> dest-port <1-65535> interval <1-60000>
15 type jitter dest-ipaddr <address> dest-port <1-65535>
15 type echo protocol ipIcmpEcho <address> source-ipaddr <address>
15 type echo protocol ipIcmpEcho <address>
15 type ftp operation get url <string> source-ipaddr <address> mode active
15 type ftp operation get url <string> source-ipaddr <address> mode passive
15 type ftp operation get url <string> source-ipaddr <address>
15 type ftp operation get url <string>
15 type http operation get url <string> name-server <address> version <string> source-ipaddr
<address> source-port <1-65535> cache
15 type http operation get url <string> name-server <address> version <string> source-ipaddr
<address> source-port <1-65535> cache
15 type http operation get url <string> name-server <address> version <string> source-ipaddr
<address> source-port <1-65535> cache
15 type http operation get url <string> name-server <address> version <string> source-ipaddr
<address> source-port <1-65535>
15 type http operation get url <string> name-server <address> version <string> source-ipaddr
<address>
15 type http operation get url <string> name-server <address> version <string>
15 type http operation get url <string> name-server <address>
15 type http operation get url <string>
15 type http operation raw
15 type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82> circuit-id <string>
15 type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82> remote-id <string>
15 type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82> subnet-mask
<ipmask>
15 type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82>
15 type dhcp dest-ipaddr <address> source-ipaddr <address>
15 type dhcp dest-ipaddr <address>
15 type dhcp
15 type dns target-addr <string> name-server <address> source-ipaddr <address> source-port
<1-65535>
15 type dns target-addr <string> name-server <address> source-ipaddr <address>
15 type dns target-addr <string> name-server <address>
15 type pathEcho protocol ipIcmpEcho <address> source-ipaddr <address>
15 type pathEcho protocol ipIcmpEcho <address>
15 type pathJitter dest-ipaddr <address> source-ipaddr <address>
15 type pathJitter dest-ipaddr <address> num-packets <1-100>
15 type pathJitter dest-ipaddr <address> interval <1-1000>
15 type pathJitter dest-ipaddr <address> targetOnly
15 type pathJitter dest-ipaddr <address>
15 type slm frame-relay pvc
15 type slm controller T1 <controller>
15 type slm controller E1 <controller>
15 type slm controller T3 <controller>
15 type slm controller E3 <controller>
15 exit
```

In the following example, only those commands in RTR configuration mode containing the keyword dhcp are shown:

```text
show parser dump rtr | include dhcp
15 type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82> circuit-id <string>
15 type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82> remote-id <string>
15 type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82> subnet-mask
<ipmask>
15 type dhcp dest-ipaddr <address> source-ipaddr <address> option <82-82>
15 type dhcp dest-ipaddr <address> source-ipaddr <address>
15 type dhcp dest-ipaddr <address>
15 type dhcp
```

The following example shows how the extend keyword displays the syntax descriptions that match those shown using the ? command-line help:

```text
Router# show parser dump rtr extend
Mode Name :rtr
15 type udpEcho dest-ipaddr <address> dest-port <1-65535> source-ipaddr <address> source-port
<1-65535> control enable
type : Type of entry
udpEcho : UDP Echo Operation
dest-ipaddr : Destination address
<address> : IP address or hostname
dest-port : Destination Port
<1-65535> : Port Number
source-ipaddr : Source address
<address> : IP address or hostname
source-port : Source Port
<1-65535> : Port Number
control : Enable or disable control packets
enable : Enable control packets exchange (default)
! Ctrl-Z used here to interrupt output and return to CLI prompt.
Router# config terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)# rtr 1
Router(config-rtr)#
type udpEcho ?
dest-ipaddr Destination address
Router(config-rtr)# type udpEcho dest-ipaddr ?
Hostname or A.B.C.D IP address or hostname
Router(config-rtr)# type udpEcho dest-ipaddr HOSTNAME ?
dest-port Destination Port
Router(config-rtr)# type udpEcho dest-ipaddr HOSTNAME dest-port ?
<1-65535> Port Number
Router(config-rtr)# type udpEcho dest-ipaddr HOSTNAME dest-port 1 ?
control Enable or disable control packets
source-ipaddr Source address
source-port Source Port
<cr>
Router(config-rtr)#
type udpEcho dest-ipaddr HOSTNAME dest-port 1 control ?
disable Disable control packets exchange
enable Enable control packets exchange (default)
```

In the following example, show parser dump output is redirected to a file on a remote TFTP server:

```text
show parser dump exec extend | redirect
tftp://209.165.200.225/userdirectory/123-exec-commands.txt
In the following example, the show parser dump
command is not available in Cisco IOS software because this command was removed in Cisco
IOS 15.0(1)M:
Router# show parser dump all
Command accepted, but obsolete, parser dumper has been deprecated
```


### `show parser macro`

> **Página:** 818 · **Modo:** Privileged EXEC (#) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the smart port macros, use the show parser macro command in privileged EXEC mode.

**Syntax:**

```text
show parser macro [name macro-name | brief | description [interface interface]]
```

**Parameters (Syntax Description):**

- `name macro-name` — ( Optional) D is p l a y s as p e c if i c macro.
- `brief` — ( Optional) D is p l a y s the configure d macro names.
- `description` — ( Optional) D is p l a y s the macro description for all interfaces.
- `interface interface` — ( Optional) D is p l a y s the macro description for the specified interface.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SXH | This command was introduced. |

**Example:**

The following example shows how to display the macro description:

```text
Router# show parser macro description
Interface Macro Description
--------------------------------------------------------------
Fa1/2 desktop-config
--------------------------------------------------------------
```

The following example shows how to display the contents of the cisco-router smart port macro:

```text
Router# show parser macro name cisco-router
Macro name : cisco-router
Macro type : default interface
# macro keywords $NVID
# Do not apply to EtherChannel/Port Group
# Access Uplink to Distribution
switchport
# Define unique Native VLAN on trunk ports
# Recommended value for native vlan (NVID) should not be 1
switchport trunk native vlan $NVID
# Update the allowed VLAN range (VRANGE) such that it
# includes data, voice and native VLANs
# switchport trunk allowed vlan VRANGE
# Hardcode trunk and disable negotiation to
# speed up convergence
switchport trunk encapsulation dot1q
switchport mode trunk
switchport nonegotiate
# Configure qos to trust this interface
auto qos voip trust
mls qos trust dscp
# Ensure fast access to the network when enabling the interface.
# Ensure that switch devices cannot become active on the interface.
spanning-tree portfast
spanning-tree bpduguard enable
```

The following example shows how to list the Cisco-provided smart port macros:

```text
Router# show parser macro brief | include default
default global : cisco-global
default interface: cisco-desktop
default interface: cisco-phone
default interface: cisco-switch
default interface: cisco-router
```


### `show parser statistics`

> **Página:** 819 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To displays statistics about the last configuration file parsed and the status of the Parser Cache feature, use the show parser statistics command in privileged EXEC mode.

**Syntax:**

```text
show parser statistics
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.1(5)T | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The show parser statistics command displays two sets of data: • The number of commands in the configuration file that was last copied into the running configuration, and the time it took for the system to parse them (a configuration file can be loaded into the running configuration at system startup, or by issuing commands such as the copy source running-config command). • The status of the Parser Cache feature (enabled or disabled) and the number of command matches (indicated by hits/misses) since the system was started or since the parser cache was cleared. The Parser Cache feature optimizes the parsing (translation and execution) of Cisco IOS software configuration command lines by remembering how to parse recently encountered command lines, decreasing the time required to process large configuration files.

**Example:**

The following example shows sample output from the show parser statistics command:

```text
Router# show parser statistics
Last configuration file parsed:Number of Commands:1484, Time:1272 ms
Parser cache:disabled, 0 hits, 2 misses
```

In this example, the Parser Cache feature is disabled, but shows the hit/miss statistics for the two commands issued while the parser cache was last enabled. The table below describes the key output fields.

| Lastconfigurationfile parsed: | Displaysstatisticsonthelastconfigurationfilecopiedintotherunning configuration(atstartuporusingthecopycommand). |
| --- | --- |
| Numberofcommands: | Thenumberofcommandlinesinthelastconfigurationfileparsed. |
| Time: | Time(inmilliseconds)takenforthesystemtoloadthelastconfigurationfile. |
| Parsercache: | DisplayswhethertheParserCachefeatureisenabledordisabled,andthehit/miss statisticsrelatedtothefeature.Statisticsarestoredsincetheinitializationofthe system,orsincethelasttimetheparsercachewascleared. |
| hits | Numberofcommandstheparsercachewasabletoparsemoreefficientlyby matchingthemtosimilarcommandsexecutedpreviously. |
| misses | Numberofcommandstheparsercachewasunabletomatchtopreviously executedcommands.TheperformanceenhancementprovidedbytheParser Cachefeaturecannotbeappliedtounmatchedcommands. |

In the following example the show parser statistics command is used to compare the parse-time of a large configuration file with the Parser Cache feature disabled and enabled. In this example, a configuration file with 1484 access list commands is loaded into the running configuration.

```text
Router# configure terminal
!parser cache is disabled
Router(config)# no parser cache
!configuration file is loaded into the running configuration
Router# copy slot0:acl_list running-config
Router# show parser statistics
Last configuration file parsed:Number of Commands:1484, Time:1272 ms
Parser cache:disabled, 0 hits, 2 misses
!the parser cache is reenabled
Router(config)# parser cache
!configuration file is loaded into the running configuration
Router# copy slot0:acl_list running-config
Router# show parser statistics
Last configuration file parsed:Number of Commands:1484, Time:820 ms
Parser cache:enabled, 1460 hits, 26 misses
```

These results show an improvement to the load time for the same configuration file from 1272 milliseconds (ms) to 820 ms when the Parser Cache feature was enabled. As indicated in the “hits” field of the show command output, 1460 commands were able to be parsed more efficiently by the parser cache.


### `show pci`

> **Página:** 821 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the peripheral component interconnect (PCI) hardware registers or bridge registers for the Cisco 7200 series routers, use the show pcicommand in EXEC mode.

**Syntax:**

```text
show pci {hardware | bridge [register]}
```

**Parameters (Syntax Description):**

- `hardware` — D is p l a y s PCI hardware register s.
- `bridge` — D is p l a y s PCI bridge register s.
- `register` — ( Optional) Number of as p e c if i c bridge register in the range from0 to7. If not specified, this command d is p l a y s information about all register s.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The output of this command is generally useful for diagnostic tasks performed by technical support only. Note The show pci hardware EXEC command displays a substantial amount of information.

**Example:**

The following is sample output for the PCI bridge register 1 on a Cisco 7200 series router:

```text
Router# show pci bridge 1
Bridge 4, Port Adaptor 1, Handle=1
DEC21050 bridge chip, config=0x0
(0x00): cfid = 0x00011011
(0x04): cfcs = 0x02800147
(0x08): cfccid = 0x06040002
(0x0C): cfpmlt = 0x00010010
(0x18): cfsmlt = 0x18050504
(0x1C): cfsis = 0x22805050
(0x20): cfmla = 0x48F04880
(0x24): cfpmla = 0x00004880
(0x3C): cfbc = 0x00000000
(0x40): cfseed = 0x00100000
(0x44): cfstwt = 0x00008020
```

The following is partial sample output for the PCI hardware register, which also includes information on all the PCI bridge registers on a Cisco 7200 series router:

```text
Router# show pci hardware
GT64010 External PCI Configuration registers:
Vendor / Device ID : 0xAB114601 (b/s 0x014611AB)
Status / Command : 0x17018002 (b/s 0x02800117)
Class / Revision : 0x00000006 (b/s 0x06000000)
Latency : 0x0F000000 (b/s 0x0000000F)
RAS[1:0] Base : 0x00000000 (b/s 0x00000000)
RAS[3:2] Base : 0x00000001 (b/s 0x01000000)
CS[2:0] Base : 0x00000000 (b/s 0x00000000)
CS[3] Base : 0x00000000 (b/s 0x00000000)
Mem Map Base : 0x00000014 (b/s 0x14000000)
IO Map Base : 0x01000014 (b/s 0x14000001)
Int Pin / Line : 0x00010000 (b/s 0x00000100)
Bridge 0, Downstream MB0 to MB1, Handle=0
DEC21050 bridge chip, config=0x0
(0x00): cfid = 0x00011011
(0x04): cfcs = 0x02800143
(0x08): cfccid = 0x06040002
(0x0C): cfpmlt = 0x00011810
(0x18): cfsmlt = 0x18000100
(0x1C): cfsis = 0x02809050
(0x20): cfmla = 0x4AF04880
(0x24): cfpmla = 0x4BF04B00
(0x3C): cfbc = 0x00000000
(0x40): cfseed = 0x00100000
(0x44): cfstwt = 0x00008020
```


### `show pci hardware`

> **Página:** 822 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the Host-PCI bridge, use the show pci hardware command in EXEC mode.

**Syntax:**

```text
show pci hardware
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The output of this command is generally useful for diagnostic tasks performed by technical support only:

```text
Router# show pci hardware
hardware PCI hardware registers
Each device on the PCI bus is assigned a PCI device number. For the
C2600, device numbers are as follows:
Device Device number
0 First LAN device
1 Second LAN device
2 AIM device (if present)
3 Not presently used
4 Port module - first PCI device
5 Port module - second PCI device
6 Port module - third PCI device
7 Port module - fourth PCI device
8-14 Not presently used
15 Xilinx PCI bridge
```

**Example:**

The following is partial sample output for the PCI hardware register, which also includes information on all the PCI bridge registers.

```text
router# show pci hardware
XILINX Host-PCI Bridge Registers:
Vendor / Device ID: 0x401310EE
Status / Command: 0x040001C6
PCI Slave Base Reg 0: 0x00000000
PCI Slave Base Reg 1: 0x04000000
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Device/VendorID | IdentifiesthePCIvendoranddevice.Thevalue0x401310EEidentifiesthedevice astheXilinx-basedHost-PCIbridgefortheCisco2600router. |
| Status/Command | ProvidesstatusoftheHost-PCIbridge.RefertothePCISpecificationformore information. |
| PCISlaveBaseReg0 | ThebaseaddressofPCITargetRegion0fortheHost-PCIbridge.Thisregionis usedforBig-EndiantransfersbetweenPCIdevicesandmemory. |
| PCISlaveBaseReg1 | ThebaseaddressofPCITargetRegion1fortheHost-PCIbridge.Thisregionis usedforLittle-EndiantransfersbetweenPCIdevicesandmemory. |


### `show perf-meas`

> **Página:** 823 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the performance measurement of the router, use the show perf-meascommand in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show perf-meas [report-types | all]
```

**Parameters (Syntax Description):**

- `report-types` — ( optional) R e ports type. The values are: •2 t-to-h d l c-D is p l a y2 t-to-h d l c r e port2 t-to-modem D is p l a y2 t-to-modem report • all-D is p l a y all r e ports • f e-to-h d l c-D is p l a y s f e-to-h d l c r e port • f e-to-modem-D is p l a y s f e-to-modem r e port • h d l c-to-2 t-D is p l a y h d l c-to-2 t r e port • h d l c-to-f e-D is p l a y h d l c-to-f e r e port • modem-to-2 t-D is p l a ymodem-to-2 t r e port • modem-to-f e-D is p l a y s modem-to-f e r e port
- `all` — ( Optional) D is p l a y all r e ports.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |

**Usage Guidelines:**

Use the show perf-meascommand to display the performance measurement of the router.

**Example:**

The following is sample output from the show perf-meascommand. The field descriptions are self-explanatory.

```text
show perf-meas
****** P E R FOR M A N C E M E A S U R E M E N T ******
----------------------------------------------
Fastswitch packets from: Fast-Ethernet to Fast-Ethernet
- Min Time: 0 micro seconds
- Avg Time: 0 micro seconds
- Max Time: 0 micro seconds
- Total number Fastswitch-packets: 0
- Number of packets from output queue (non-Fastswitch): 0
-------------------------------------------------------------------------------|
| Perf Ctr Min | Perf Ctr Avg | Perf Ctr Max |
-------------------------------------------------------------------------------|
Clock Cycles | 0 | 0 | 0 |
Total-Issued Instructions | 0 | 0 | 0 |
Floating Point Instructions Issued| 0 | 0 | 0 |
Integer Instructions Issued | 0 | 0 | 0 |
Load Instructions Issued | 0 | 0 | 0 |
Store Instructions Issued | 0 | 0 | 0 |
Dual-Issued Instruction Pairs | 0 | 0 | 0 |
Branch Pre-Fetches | 0 | 0 | 0 |
Slip Cycles | 0 | 0 | 0 |
Stall Cycles | 0 | 0 | 0 |
On-Chip Secondary Cache Misses | 0 | 0 | 0 |
Primary Instruction Cache Misses | 0 | 0 | 0 |
Primary Data Cache Misses | 0 | 0 | 0 |
DTLB Misses | 0 | 0 | 0 |
ITLB Misses | 0 | 0 | 0 |
Joint TLB Instruction Misses | 0 | 0 | 0 |
Joint TLB Data Misses | 0 | 0 | 0 |
Taken Branch Instructions | 0 | 0 | 0 |
Branch Instructions Issued | 0 | 0 | 0 |
OCS Cache Write-Backs | 0 | 0 | 0 |
Data Cache Write-Backs | 0 | 0 | 0 |
Pending Load Stall Cycles | 0 | 0 | 0 |
Number of Re-Misses | 0 | 0 | 0 |
FP Possible Exception Stall Cycle | 0 | 0 | 0 |
-------------------------------------------------------------------------------|
```


### `show platform`

> **Página:** 825 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display platform information, use the show platform command in privileged EXEC mode. Cisco 4400 Series Integrated Services Routers Cisco ASR 1000 Series Aggregation Services Routers

**Syntax:**

```text
show platform {buffers | copp rate-limit {arp | dhcp | atm-oam | ethernet-oam | icmp | igmp |
pppoe-discovery | atom ether-vc | all} | np copp [ifnum] [detail] | dma | eeprom | fault | hardware
capacity | hardware pfc mode | internal-vlan | interrupts | netint | software ipv6-multicast connected
| stats | tech-support {ipmulticast [vrf vrf-name] group-ip-addr src-ip-addr | unicast [vrf vrf-name]
destination-ip-addr destination-mask [global]} | tlb | vfi dot1q-transparency | vlans}
show platform
show platform
```

**Parameters (Syntax Description):**

- `buffers` — D is p l a y s buffer-alloc at i on information.
- `copprate-limit` — D is p l a y s Cisco Control Plane P o l i c in g( C o P P) r at e-limit information on the Cisco7600 S IP-400.
- `arp` — Specifies Address R e s o l u t i on P r o to c o l( A R P) p a c k e t traffic.
- `dhcp` — Specifies Dynamic Host Configuration P r o to c o l( D H C P) p a c k e t traffic.
- `atm-oam` — Specifies AT MOp e r at i on, A d min is t r at i on, and M a in t e n an c e( OAM) p a c k e t traffic.
- `ethernet-oam` — Specifies E the r n e t OAM p a c k e t traffic.
- `icmp` — Specifies In t e r n e t Connection Management P r o to o c o l R at e limit e r.
- `igmp` — Specifies In t e r n e t Group Management Potocol R at e limit e r.
- `pppoe-discovery` — Specifies P o in t-to-P o in t P r o to c o l over E the r n e t( PPP o E) d is c over y p a c k e t information.
- `atomether-vc` — Shows whether IP or route d mode in t e r w or k in g is configure d.
- `all` — D is p l a y s r at e-limit information for all protocols.
- `npcopp` — D is p l a y s debug information for a g i v e n Co P P session ID or for all Co PP sessions.
- `ifnum` — ( Optional) As e s s i on ID.
- `detail` — ( Optional) Shows full r at e-limit e d values.
- `dma` — D is p l a y s Direct Memory Access( D M A) c h an n e l information.
- `eeprom` — D is p l a y s CPU E E P ROM information.
- `fault` — D is p l a y s the f a u l t d at e.
- `hardware capacity` — D is p l a y s the c apa c it i e s and u t i l i z at i on s for hardware resource s; see the show platform hardware capacity command.
- `hardware p f c mode` — D is p l a y s the type of install e d Policy Feature Card(PFC).
- `internal-vlan` — D is p l a y s the in t e r n a l VLAN.
- `interrupt s` — D is p l a y s m8500 interrupt counters.
- `netint` — D is p l a y s the platform network-interrupt information.
- `softwareipv6-multicastconnected` — D is p l a y s all the IP v6 s u b n e t Access Control List( A C L) e n t r i e s on the Route Processor( R P); see the show platform software ip v6-m u l t i c as t command.
- `stats` — D is p l a y s C on s t e l l at i on W AN( C W AN) statistics.
- `tech-supportipmulticast` — D is p l a y s IP m u l t i c as t-related information for Tech n i c a l As s is t an c e Center (TAC).
- `vrf vrf-name` — ( Optional) D is p l a y s the Virtual Private Network( V P N) r out in g and for w a r d in g( VRF) in s t an c e.
- `group-ip-addr` — Group IP address.
- `src-ip-addr` — Source IP address.
- `unicast` — D is p l a y s IP u n i c as t-related information for TAC.
- `destination-ip-addr` — Destination IP address.
- `destination-mask` — Destination mask.
- `global` — ( Optional) D is p l a y s global output.
- `tlb` — D is p l a y s information about the t r an s l at i on l o o k-as id e buffer( T L B) register.
- `vfi` — D is p l a y s C W AN v i r t u a l for w a r d in g in s t an c e( V F I) commands.
- `dot1q-transparency` — D is p l a y s the do t1 q t r an s p are n c y set t in g.
- `vlans` — D is p l a y s h id d e n VLAN-to-W AN interface map ping.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Cisco IOS Release12.2(17 d) S X B. This command was changed to include the hardware p f c mode keywords. |
| 12.2(18)SXD | This command was modified to include the software ip v6-m u l t i c as t c on n e c t e d keywords. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SRC | This command was modified to include a d d it i on a l keywords to support Co P P e n h an c e m e n t s on the Cisco7600 S IP-400 on the Cisco7600 s e r i e s router. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1. |
| 12.2(33)SRD | This command was modified. The at o m e the r-v c keyword was added. |
| CiscoIOSXERelease3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |
| CiscoIOSXEGibraltar16.11.1 | Output no w in d i c at e s when a P S U slot is e m p t y. In e a r l i e r releases, the state of an e m p t y P S U slot ap p e are d in the command output as" p s, f a i l". Seethe examples for differences in in d i c at i on options for Cisco AS R1000 S e r i e s and ISR4000 S e r i e s routers. |

**Usage Guidelines:**

This command is similar to the show msfc command. This command can be used to verify the existence of a second Cisco IOS process on a single Cisco ASR 1000 RP on a Cisco ASR 1002 router or Cisco ASR 1004 router. When this command is used with the atom ether-vc keyword, it is used on the line-card console.

**Example:**

The following sample output from the show platform buffers command displays buffer-allocation information:

```text
Router# show platform buffers
Reg. set Min Max
TX 640
ABQ 640 16384
0 0 40
1 6715 8192
2 0 0
3 0 0
4 0 0
5 0 0
6 0 0
7 0 0
Threshold = 8192
Vlan Sel Min Max Cnt Rsvd
1019 1 6715 8192 0 0
```

Cisco ISR 4400 Series Routers The following example displays online status information for a Cisco ISR 4451-X/K9.

```text
Router# show platform
Chassis type: ISR4451-X/K9
Slot Type State Insert time (ago)
--------- ------------------- --------------------- -----------------
0 ISR4451-X/K9 ok 00:06:51
0/0 ISR4451-X-4x1GE ok 00:05:31
0/1 NIM-ES2-8-P ok 00:05:31
1 ISR4451-X/K9 ok 00:06:51
1/0 UCS-EN120S-M2/K9 ok 00:05:31
2 ISR4451-X/K9 ok 00:06:51
R0 ISR4451-X/K9 ok, active 00:06:51
F0 ISR4451-X/K9 ok, active 00:06:51
P0 PWR-4450-1000W-AC ok 00:06:29
P1 PWR-4450-1000W-AC ok 00:06:29
P2 ACS-4450-FANASSY ok 00:06:29
POE0 PWR-POE-4450 ok 00:06:29
GE-POE PWR-GE-POE-4400 ok 00:06:29
Slot CPLD Version Firmware Version
--------- ------------------- ---------------------------------------
0 15010638 16.7(4r)
1 15010638 16.7(4r)
2 15010638 16.7(4r)
R0 15010638 16.7(4r)
F0 15010638 16.7(4r)
```

The table below describes the fields that appear in the above example

| Field | Description |
| --- | --- |
| Slot | Chassisslotnumber |
| Type | Typeofmodule |
| State | Statusofthemodule |
| Insert time | Periodoftime((hh:mm:ssformat)sincethemodulehasbeenupandrunning |

Cisco ASR 1000 Series Routers The following example displays online status information for the shared port adapters (SPAs), Cisco ASR 1000 SPA Interface Processor (SIP), Cisco ASR 1000 Embedded Services Processor (ESP), Cisco ASR 1000 RP, power supplies, and fans. The ESPs are shown as F0 and F1. The RPs are shown as R0 and R1. The State column should display “ok” for SIPs, SPAs, power supplies, and fans. For RPs and ESPs, the State column should display “ok, active” or “ok, standby.”

```text
Router# show platform
Chassis type: ASR1006
Slot Type State Insert time (ago)
--------- ------------------- --------------------- -----------------
0 ASR1000-SIP10 ok 18:23:58
0/0 SPA-5X1GE-V2 ok 18:22:38
0/1 SPA-8X1FE-TX-V2 ok 18:22:33
0/2 SPA-2XCT3/DS0 ok 18:22:38
1 ASR1000-SIP10 ok 18:23:58
1/0 SPA-2XOC3-POS ok 18:22:38
1/1 SPA-8XCHT1/E1 ok 18:22:38
1/2 SPA-2XT3/E3 ok 18:22:38
R0 ASR1000-RP1 ok, active 18:23:58
R1 ASR1000-RP1 ok, standby 18:23:58
F0 ASR1000-ESP10 ok, active 18:23:58
F1 ASR1000-ESP10 ok, standby 18:23:58
P0 ASR1006-PWR-AC ok 18:23:09
P1 ASR1006-FAN ok 18:23:09
Slot CPLD Version Firmware Version
--------- ------------------- ---------------------------------------
0 06120701 12.2(33r)XN2
1 06120701 12.2(33r)XN2
R0 07082312 12.2(33r)XN2
R1 07082312 12.2(33r)XN2
F0 07051680 12.2(33r)XN2
F1 07051680 12.2(33r)XN2
```

Empty PSU slot This example shows an "empty" state for slot P1. It applies to Cisco ISR 4000 Series and ASR 1000 Series routers.

```text
Device#show platform
Chassis type: ASR1002-X
Slot Type State Insert time (ago)
--------- ------------------- --------------------- -----------------
0 ASR1002-X ok 1d18h
0/0 6XGE-BUILT-IN ok 1d18h
0/1 SPA-8X1GE-V2 ok 1d18h
R0 ASR1002-X ok, active 1d18h
F0 ASR1002-X ok, active 1d18h
P0 ASR1002-PWR-AC ok 1d18h
P1 Unknown empty never
```

Cisco ISR 4000 with two PSUs, no power cord attached to P1 or bad input detected This example shows "fail, badinput" for P1. On ISR 4000 Series routers, the possible states are: • "fail, badinput": No power cord attached or bad input detected • “fail, badoutput”: Bad output detected • “fail, badcookie”: Failed to read the status of the PSU

```text
Device#show platform
Chassis type: ISR4431/K9
Slot Type State Insert time (ago)
--------- ------------------- --------------------- -----------------
0 ISR4431/K9 ok 19:32:35
0/0 ISR4431-X-4x1GE ok 19:30:27
0/1 NIM-SSD ok 19:30:27
R0 ISR4431/K9 ok, active 19:32:35
F0 ISR4431/K9 ok, active 19:32:35
P0 PWR-4430-AC ok 19:32:03
P1 Unknown fail, badinput 19:32:03
P2 ACS-4430-FANASSY ok 19:32:03
```

Cisco ASR 1000 with two PSUs, no power cord attached to P1, PSU turned off, or PSU failed This example shows the "ps, fail" state for slot P1.

```text
Device#show platform
Chassis type: ASR1002-X
Slot Type State Insert time (ago)
--------- ------------------- --------------------- -----------------
0 ASR1002-X ok 1d18h
0/0 6XGE-BUILT-IN ok 1d18h
0/1 SPA-8X1GE-V2 ok 1d18h
R0 ASR1002-X ok, active 1d18h
F0 ASR1002-X ok, active 1d18h
P0 ASR1002-PWR-AC ok 1d18h
P1 ASR1002-PWR-AC ps, fail 1d18h
```

Cisco ASR 1000 Series Routers--Verifying Dual Cisco IOS Processes on Single RP In the following example, a second Cisco IOS process is enabled on a Cisco ASR 1004 router using stateful switchover (SSO). The output of the show platform command is provided before and after the SSO configuration to verify that the second Cisco IOS process is enabled and active.

```text
Router# show platform
Chassis type: ASR1004
Slot Type State Insert time (ago)
--------- ------------------- --------------------- -----------------
0 ASR1000-SIP10 ok 00:04:39
0/0 SPA-5X1GE-V2 ok 00:03:23
0/1 SPA-2XT3/E3 ok 00:03:18
R0 ASR1000-RP1 ok, active 00:04:39
F0 ASR1000-ESP10 ok, active 00:04:39
P0 ASR1004-PWR-AC ok 00:03:52
P1 ASR1004-PWR-AC ok 00:03:52
Slot CPLD Version Firmware Version
--------- ------------------- ---------------------------------------
0 07091401 12.2(33r)XN2
R0 07062111 12.2(33r)XN2
F0 07051680 12.2(33r)XN2
Router# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)# redundancy
Router(config-red)# mode sso
*May 27 19:43:43.539: %CMRP-6-DUAL_IOS_REBOOT_REQUIRED: R0/0: cmand: Configuration must
be saved and the chassis must be rebooted for IOS redundancy changes to take effect
Router(config-red)# exit
Router(config)# exit
*May 27 19:44:04.173: %SYS-5-CONFIG_I: Configured from console by user on console
Router# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
Router# reload
Proceed with reload? [confirm]
*May 27 19:45:16.917: %SYS-5-RELOAD: Reload requested by user on console. Reload Reason:
Reload command.
<reload output omitted for brevity>
Router# show platform
Chassis type: ASR1004
Slot Type State Insert time (ago)
--------- ------------------- --------------------- -----------------
0 ASR1000-SIP10 ok 00:29:34
0/0 SPA-5X1GE-V2 ok 00:28:13
0/1 SPA-2XT3/E3 ok 00:28:18
R0 ASR1000-RP1 ok 00:29:34
F0 ASR1000-ESP10 ok, active 00:29:34
P0 ASR1004-PWR-AC ok 00:28:47
P1 ASR1004-PWR-AC ok 00:28:47
Slot CPLD Version Firmware Version
--------- ------------------- ---------------------------------------
0 07091401 12.2(33r)XN2
R0 07062111 12.2(33r)XN2
F0 07051680 12.2(33r)XN2
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Slot | Chassisslot. |
| Type | Hardwaretype. |

| Field | Description |
| --- | --- |
| State | Onlinestateofthehardware.Oneofthefollowingvalues: AllHardware •booting--Hardwareisinitializingandsoftwareisbooting. •disabled--Hardwareisnotoperational. •init--HardwareorCiscoIOSprocessisinitializing. •ok--Hardwareisoperational. •shutdown--Hardwarewasadministrativelyshutdownusingthenoshutdown command. •unknown--Hardwareisnotoperational;stateisunknown. RPorESP •init,standby--StandbyRPorESPisoperationalbutisnotyetinahighavailability (HA)state.AnRPorESPswitchoverisnotyetpossible. •ok,active--ActiveRPorESPisoperational. •ok,standby--StandbyRPorESPisoperational.ThestandbyRPorESPisreadyto becomeactiveintheeventofaswitchover. SPA •admindown--SPAwasdisabledusingtheshutdowncommand. •inserted--SPAisbeinginserted. •missing--SPAwasremoved. •outofservice--SPAisnotoperational. •retrievalerror--AnerroroccurredwhileretrievingtheSPAstate;stateisunknown. •stopped--SPAwasgracefullydeactivatedusingthehw-modulesubslotstop command. FanorPowerSupply •fan,fail--Fanisfailing. •Empty--Powersupplyismissing. •ps,fail--Powersupplyisfailing. |
| Inserttime(ago) | Amountoftime(hh:mm:ssformat)thehardwarehasbeenonline. |
| CPLDVersion | Complexprogrammablelogicdeviceversionnumber. |
| FirmwareVersion | Firmware(ROMmon)versionnumber. |

Cisco 7600 Series Routers with Cisco 7600 SIP-400 The following sample output from the show platform copp rate-limit arp command displays the list of interfaces on which a rate limiter is active for ARP, along with the count of confirmed and exceeded packets for the rate limiter:

```text
show platform copp rate-limit arp
Rate limiter Information for Protocol arp:
Rate Limiter Status: Enabled
Rate : 20 pps
Max Observation Period : 60 seconds
Per Interface Rate Limiter Information
Interface Conformed Pkts Exceeded Pkts Enabled Obs Period (Mts)
GigabitEthernet5/1 0 0 No -
GigabitEhternet5/1.1 14 0 No -
GigabitEthernet5/1.2 28 2 No -
GigabitEthernet5/2 0 0 No -
GigabitEthernet5/2.1 180 4 Yes 35
GigabitEthernet5/2.2 200 16 Yes Max
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| RateLimiterStatus | Indicatesifaratelimiterhasbeenenabledontheinterface. |
| Rate | Indicatestheconfiguredrateinpacketspersecond(pps)orbitspersecond(bps). |
| MaxObservationPeriod | Indicatestheconfiguredobservationperiod,inseconds,beforetheper-interface ratelimiterisautomaticallyturnedoff. |
| PerInterfaceRate LimiterInformation | Displaysthelistofinterfacesonwhichtheratelimiterisactive.Inthisexample: •GigabitEthernet5/1.1isfreefromattack. •GigabitEthernet5/2.1hasanexceedcountof4,andhasaratelimiterenabled. Theobservationperiodis35minutes,whichindicatesthatcurrentlythe interfaceisfreefromattackandisbeingkeptunderobservation.Theinterface willremainunderobservationforanadditional35minutes.Ifitremainsfree fromattackafterthattime,theratelimiterisautomaticallyremoved. •GigabitEthernet5/2.2hasanexceedcountof16andhasaratelimiterenabled. TheobservationperiodhasbeendesignatedasMax.Thisindicatesthatthe interfaceisstillunderattackandhasnotyetenteredtheobservationtime window. |

The following sample from the show platform eeprom command displays CPU EEPROM information:

```text
Router# show platform eeprom
MSFC CPU IDPROM:
IDPROM image:
IDPROM image block #0:
hexadecimal contents of block:
00: AB AB 02 9C 13 5B 02 00 00 02 60 03 03 E9 43 69 .....[....`...Ci
10: 73 63 6F 20 53 79 73 74 65 6D 73 00 00 00 00 00 sco Systems.....
20: 00 00 57 53 2D 58 36 4B 2D 53 55 50 33 2D 50 46 ..WS-X6K-SUP3-PF
30: 43 33 00 00 00 00 53 41 44 30 36 34 34 30 31 57 C3....SAD064401W
40: 4C 00 00 00 00 00 00 00 00 00 37 33 2D 37 34 30 L.........73-740
50: 34 2D 30 37 00 00 00 00 00 00 30 35 00 00 00 00 4-07......05....
60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
70: 00 00 00 00 02 BD 00 00 00 00 00 09 00 05 00 01 ................
80: 00 03 00 01 00 01 00 02 03 E9 00 00 00 00 00 00 ................
90: 00 00 00 00 00 00 00 00 00 00 00 00 ............
block-signature = 0xABAB, block-version = 2,
block-length = 156, block-checksum = 4955
*** common-block ***
IDPROM capacity (bytes) = 512 IDPROM block-count = 2
FRU type = (0x6003,1001)
OEM String = 'Cisco Systems'
Product Number = 'WS-X6K-SUP3-PFC3'
Serial Number = 'SAD064401WL'
Manufacturing Assembly Number = '73-7404-07'
Manufacturing Assembly Revision = '05'
Hardware Revision = 0.701
Manufacturing bits = 0x0 Engineering bits = 0x0
SNMP OID = 9.5.1.3.1.1.2.1001
Power Consumption = 0 centiamperes RMA failure code = 0-0-0-0
CLEI =
*** end of common block ***
IDPROM image block #1:
hexadecimal contents of block:
00: 60 03 02 67 0C 24 00 00 00 00 00 00 00 00 00 00 `..g.$..........
10: 00 00 00 00 00 00 00 51 00 05 9A 3A 7E 9C 00 00 .......Q...:~...
20: 02 02 00 01 00 01 00 00 00 00 00 00 00 00 00 00 ................
30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
40: 14 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
50: 00 00 81 81 81 81 80 80 80 80 80 80 80 80 80 80 ................
60: 80 80 06 72 00 46 37 ...r.F7
block-signature = 0x6003, block-version = 2,
block-length = 103, block-checksum = 3108
*** linecard specific block ***
feature-bits = 00000000 00000000
hardware-changes-bits = 00000000 00000000
card index = 81
mac base = 0005.9A3A.7E9C
mac_len = 0
num_processors = 2
epld_num = 2
epld_versions = 0001 0001 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
port numbers:
pair #0: type=14, count=01
pair #1: type=00, count=00
pair #2: type=00, count=00
pair #3: type=00, count=00
pair #4: type=00, count=00
pair #5: type=00, count=00
pair #6: type=00, count=00
pair #7: type=00, count=00
sram_size = 0
sensor_thresholds =
sensor #0: critical = -127 oC (sensor present but ignored), warning = -127 oC (sensor
present but ignored)
sensor #1: critical = -127 oC (sensor present but ignored), warning = -127 oC (sensor
present but ignored)
sensor #2: critical = -128 oC (sensor not present), warning = -128 oC (sensor not
present)
sensor #3: critical = -128 oC (sensor not present), warning = -128 oC (sensor not
present)
sensor #4: critical = -128 oC (sensor not present), warning = -128 oC (sensor not
present)
sensor #5: critical = -128 oC (sensor not present), warning = -128 oC (sensor not
present)
sensor #6: critical = -128 oC (sensor not present), warning = -128 oC (sensor not
present)
sensor #7: critical = -128 oC (sensor not present), warning = -128 oC (sensor not
present)
max_connector_power = 1650
cooling_requirement = 70
ambient_temp = 55
*** end of linecard specific block ***
```

The following sample output from the show platform fault command displays fault-date information:

```text
Router# show platform fault
Fault History Buffer:
rsp72043_rp Software (rsp72043_rp-ADVENTERPRISEK9_DBG-M), Version 12.2(32.8.1)RE
C186 ENGINEERING WEEKLY BUILD, synced to V122_32_8_11_SR186
Compiled Wed 08-Apr-09 09:22 by abcd
Uptime 2w3d
Exception Vector: 0x1500 PC 0x0B13DD4C MSR 0x00029200 LR 0x0B13DD10
r0 0x0B13DD10 r1 0x1C58A1C8 r2 0xFFFCFFFC r3 0x189EDEF4
r4 0x00000000 r5 0x00000000 r6 0x1C58A1B0 r7 0x00029200
r8 0x00029200 r9 0x00000000 r10 0x00000001 r11 0x189EDEF0
r12 0x0000001B r13 0x04044000 r14 0x08736008 r15 0x115C0000
r16 0x00000000 r17 0x00000000 r18 0x00000000 r19 0x1B751358
r20 0x00000000 r21 0x00000000 r22 0x00000000 r23 0x00000000
r24 0x00000000 r25 0x00000000 r26 0x00000000 r27 0x00000001
r28 0x13255EC0 r29 0x1C59BD00 r30 0x13255EC0 r31 0x00000000
dec 0x00007333 tbu 0x00004660 tbl 0x594BBFC4 pvr 0x80210020
dear 0x00000000 dbcr0 0x41000000 dbcr1 0x00000000 dbcr2 0x00000000
iac1 0x00000000 iac2 0x00000000 dac1 0x00000000 dac2 0x00000000
```

The following sample output from the show platform hardware pfc mode command displays the PFC-operating mode:

```text
Router# show platform hardware pfc mode
PFC operating mode : PFC3A
```

This example shows how to display platform network-interrupt information:

```text
Router# show platform netint
Network IO Interrupt Throttling:
throttle count=0, timer count=0
active=0, configured=1
netint usec=3999, netint mask usec=800
inband_throttle_mask_hi = 0x0
inband_throttle_mask_lo = 0x800000
```

This following sample output from the show platform tlb command displays the TLB-register information:

```text
Router# show platform tlb
Mistral revision 5
TLB entries : 42
Virt Address range Phy Address range Attributes
0x10000000:0x1001FFFF 0x010000000:0x01001FFFF CacheMode=2, RW, Valid
0x10020000:0x1003FFFF 0x010020000:0x01003FFFF CacheMode=2, RW, Valid
0x10040000:0x1005FFFF 0x010040000:0x01005FFFF CacheMode=2, RW, Valid
0x10060000:0x1007FFFF 0x010060000:0x01007FFFF CacheMode=2, RW, Valid
0x10080000:0x10087FFF 0x010080000:0x010087FFF CacheMode=2, RW, Valid
0x10088000:0x1008FFFF 0x010088000:0x01008FFFF CacheMode=2, RW, Valid
0x18000000:0x1801FFFF 0x010000000:0x01001FFFF CacheMode=0, RW, Valid
0x19000000:0x1901FFFF 0x010000000:0x01001FFFF CacheMode=7, RW, Valid
0x1E000000:0x1E1FFFFF 0x01E000000:0x01E1FFFFF CacheMode=2, RW, Valid
0x1E880000:0x1E899FFF 0x01E880000:0x01E899FFF CacheMode=2, RW, Valid
0x1FC00000:0x1FC7FFFF 0x01FC00000:0x01FC7FFFF CacheMode=2, RO, Valid
0x30000000:0x3001FFFF 0x070000000:0x07001FFFF CacheMode=2, RW, Valid
0x40000000:0x407FFFFF 0x000000000:0x0007FFFFF CacheMode=3, RO, Valid
0x58000000:0x59FFFFFF 0x088000000:0x089FFFFFF CacheMode=3, RW, Valid
0x5A000000:0x5BFFFFFF 0x08A000000:0x08BFFFFFF CacheMode=3, RW, Valid
0x5C000000:0x5DFFFFFF 0x08C000000:0x08DFFFFFF CacheMode=3, RW, Valid
0x5E000000:0x5FFFFFFF 0x08E000000:0x08FFFFFFF CacheMode=3, RW, Valid
```

This example shows how use the atom ether-vc keyword to display line-card information for an ES20 line card in slot 3.

```text
Router# show platform copp rate-limit atom ether-vc
AToM Ether VC Index(12902): segtype(3) seghandle(0x5ECF7F34)
Disposition : flags(97) vlanid(502) local_vc_label(22691)
ForwardingTable: oper(12) flags(0x2100) vlan(502) dest_index(0x9ED)
Imposition: flags(0x21) egress_idx(0x0) ifnum(28)
tx_tvc(0x7D83) rvclbl[0](3356) rigplbl[1](1011) label[2](0)
label[3](0) ltl(0x9ED) mac(0014.1c80.f600) qos_info(0x0)
Platform Data:
loc_lbl acif_num fw_idx cword eg_ifnum ckt_idx vlan ac_hdl vc_hash
22691 615 0x0 0x3 28 0x8003 502 0x5ECF7F34 0x3266
Platform Index(0x81F68003) is_sw(1) is_vfi(0) vlan(502) pseudo_port_offset(3) tx_tvc(0x7D83)
Statistics : Packets Bytes Drop Pkts Drop Bytes ID
Disposition: 0 0 0 0 0
Imposition : 0 0 0 0 0
Vlan func[1]: 502 (0x1F6) func(0:invalid) feat (0x0 )
Tx TVC Table
idx ltl h pt cw vt efp adj v imp
x---- x-- d d- d- d- x--- x--- d x---
SIP10G EoMPLS disp detailed info:
t vclbl VLAN Type disp-idx
- d------- x---(d---) ------- x-------
0 00022691 01F6(0502) ether 00001692
SIP10G EoMPLS ipiw disp detailed info:
ipiw mac valid CE-MAC Address
b--- b-------- --------------
0001 000000001 0016.9c6e.7480
VC Summary: vlan(502) VC count(1)
```


### `show platform bridge`

> **Página:** 837 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display distributed or hardware-based bridging information, use the show platform bridgecommand in privileged EXEC mode.

**Syntax:**

```text
show platform bridge [interface-type interface-number] [vlan vlan-id] [summary]
```

**Parameters (Syntax Description):**

- `interface-typeinterface-number` — ( Optional) Interface type and number.
- `vlan vlan-id` — ( Optional) D is p l a y s VLAN b r id g in g information.
- `summary` — ( Optional) D is p l a y s as u m m a r y of b r id g in g information.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRA | This command was introduced. |

**Example:**

The following is sample output from the show platform bridgecommand:

```text
Router# show platform bridge
VLAN Interface CircuitId LTL PseudoPort State Options
12 PO1/1/3.1 102 0xC3F 1/256 up dot1q
13 PO1/1/3.1 103 0xC3F 1/256 up dot1q
14 PO1/1/3.2 104 0xC3F 1/256 up default
15 PO1/1/3.2 105 0xC3F 1/256 up default
16 PO1/1/3.3 106 0xC3F 1/256 up dot1q-tunnel
17 PO1/1/3.3 107 0xC3F 1/256 up dot1q-tunnel
41 Gi8/0/17 1201 0xDE2 8/227 up access
41 Gi8/0/17 1202 0xDE3 8/228 up access
41 Gi8/0/17 1203 0xDE4 8/229 up access
41 Gi8/0/17 1204 0xDE5 8/230 up access
41 Gi8/0/17 1205 0xDE6 8/231 up access
41 Gi8/0/17 1206 0xDE7 8/232 up access
41 Gi8/0/17 1207 0xDE8 8/233 up access
41 Gi8/0/17 1208 0xDE9 8/234 up access
41 Gi8/0/17 1209 0xDEA 8/235 up access
41 Gi8/0/17 1210 0xDEB 8/236 up access
41 Gi8/0/17 1211 0xDEC 8/237 up access
41 Gi8/0/17 1212 0xDED 8/238 up access
41 Gi8/0/17 1213 0xDEE 8/239 up access
41 Gi8/0/17 1214 0xDEF 8/240 up access
41 Gi8/0/17 1215 0xDF0 8/241 up access
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| VLAN | TheVLANforwhichbridgingisconfigured. |
| Interface | TheWANinterfaceonwhichbridgingisconfigured.ThiscanbeanATM,GigabitEthernet, POS,orSerialinterface. |
| CircuitId | ThecircuitID.Therangeisfrom0to65536. |
| LTL | Thelocaltargetlogic(LTL)oftheinterface.LTLis13bitslong. Theformatiseeesssspppppp(e:extendedportbits,s:slotbits,p:portbits). Extendedbitsalongwithportbitsidentifythepseudoportandslotbitsidentifiestheslot. |
| PseudoPort | Inthecaseofflexwan,theportnumberingisfrom133to192forBay0and197to256forBay 1.Thereare60portsperpacketprocessingengine(PPE).FortheSIP200,thepseudoportsare intherangeof137to256. |
| State | Stateindicatesthestatusofthephysicalinterfaceonwhichbridgingisconfigured.Thestateis eitherupordown.Ifthestateisdown,thenthereisaproblemanddebuggingneedstobedone. |
| Options | Optionsspecifywhethersplit-horizonisenabledontheWANinterface.Thiscanbeaccess, default,dot1q,ordot1q-tunnel. |


### `show platform cfm`

> **Página:** 838 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display connectivity fault management (CFM) commands, use the show platform cfmcommand in privileged EXEC mode.

**Syntax:**

```text
show platform cfm {epl | info | interface {fastethernet | gigabitethernet | port-channel} number
{fwd_vlan vlan-number | level | vlan_list}}
```

**Parameters (Syntax Description):**

- `epl` — D is p l a y s CFM E the r n e t private line( E P L) detail s.
- `info` — D is p l a y s the CFM Platform A d ap t at i on L a y e r( P A L) information.
- `interface` — Specifies the interface type.
- `fast e the r n e t` — Specifies the Fast E the r netint e r f a c e.
- `g i g a b it e the r n e t` — Specifies the Gigabit E the r netint e r f a c e.
- `port-channel` — Specifies the port-c h an n e l interface.
- `number` — Interface number.
- `f w d_ vlan` — D is p l a y s the CFM for w a r d VLAN list.
- `vlan-number` — VLAN number.
- `level` — D is p l a y s the CFM level for the interface.
- `vlan_ list` — Specifies CFM VLAN list.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRA | This command was introduced. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |

**Example:**

The following is sample output from the show platform cfm infocommand. The field descriptions are self-explanatory.

```text
Router# show platform cfm info
CFM is disabled
CFM unicast MAC 00d0.2b6c.b103, CFM multicast MAC 0180.c200.0030, AEB multicast MAC
0100.0ccc.ccc0
CFM Ingress Control Packet System Statistics:
Current software Rate Limit Setting: 1100 pkts/sec
Statistics are collected in intervals of 3 seconds.
Allow the first 3300 packets to pass each interval, drop thereafter
Current Ingress Count in this interval: 0 pkts
In this interval have we Exceeded Rate and Dropped pkts: NO
For the last 3 intervals the maximum sample had 0 packets in one interval.
```


### `show platform diag`

> **Página:** 839 · **Modo:** privileged EXEC (#) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display diagnostic and debug information for individual platform components, use the show platform diag command in privileged EXEC mode.

**Syntax:**

```text
show platform diag
```

**Parameters (Syntax Description):**

- `diag` — D is p l a y s diagnostic and debug information for the platform c o m p one n t s.

**Command Default:** This command has no default settings.

**Command Modes:** privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXERelease2.2 | This command was introduced on the Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Usage Guidelines:**

This command can be used to display debug and diagnostic information and indicate the status of field replaceable unit (FRU) components in any Cisco ASR 1000 Series Router.

**Example:**

The following example displays diagnostic information for the Cisco ASR 1000 SPA Interface Processor (SIP), shared port adapters (SPAs), Cisco ASR 1000 Embedded Services Processor (ESP), Cisco ASR 1000 Route Processors (RP), and power supplies. The ESP is shown as F0 or F1. The RPs are shown as R0 or R1. The power supplies are shown as P0 and P1

```text
Router#show platform diag
Chassis type: ASR1004
Slot: 0, ASR1000-SIP10
Running state : ok
Internal state : online
Internal operational state : ok
Physical insert detect time : 00:00:48 (4d22h ago)
Software declared up time : 00:01:40 (4d22h ago)
CPLD version : 07091401
Firmware version : 12.2(33r)XNB
Sub-slot: 0/0, SPA-5X1GE-V2
Operational status : ok
Internal state : inserted
Physical insert detect time : 00:00:36 (4d22h ago)
Logical insert detect time : 00:02:23 (4d22h ago)
Sub-slot: 0/1, SPA-2XT3/E3
Operational status : ok
Internal state : inserted
Physical insert detect time : 00:00:36 (4d22h ago)
Logical insert detect time : 00:02:23 (4d22h ago)
Slot: R0, ASR1000-RP1
Running state : ok
Internal state : online
Internal operational state : ok
Physical insert detect time : 00:00:48 (4d22h ago)
Software declared up time : 00:00:48 (4d22h ago)
CPLD version : 07062111
Firmware version : 12.2(33r)XNB
Sub-slot: R0/0,
Running state : ok, active
Logical insert detect time : 00:00:48 (4d22h ago)
Became HA Active time : 00:04:56 (4d22h ago)
Sub-slot: R0/1,
Running state : ok, standby
Logical insert detect time : 00:02:50 (4d22h ago)
Slot: F0, ASR1000-ESP10
Running state : ok, active
Internal state : online
Internal operational state : ok
Physical insert detect time : 00:00:48 (4d22h ago)
Software declared up time : 00:01:40 (4d22h ago)
Hardware ready signal time : 00:00:49 (4d22h ago)
Packet ready signal time : 00:01:49 (4d22h ago)
CPLD version : 07051680
Firmware version : 12.2(33r)XNB
Slot: P0, ASR1004-PWR-AC
State : ok
Physical insert detect time : 00:01:40 (4d22h ago)
Slot: P1, ASR1004-PWR-AC
State : ok
Physical insert detect time : 00:01:40 (4d22h ago)
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Runningstate | ThecurrentonlinerunningstateoftheFRUcomponent. |
| Internalstate | TheinternaldebugstateoftheFRUcomponentfordiagnosticpurposes. |
| Internaloperationalstate | TheinternaloperationalstateoftheFRUcomponentfordiagnosticpurposes. |
| Physicalinsertdetecttime | ThetimeofthemostrecentphysicalinsertionoftheFRUcomponentdetected bytheplatformcode. |
| Softwaredeclareduptime | ThetimethatthesoftwareontheFRUcomponentwasdeclaredrunningbythe platformcode. |
| Hardwarereadysignaltime | Thetimethatthehardwarereadysignalwasdetectedbytheplatformcode. |
| Packetreadysignaltime | ThetimethattheEmbeddedServiceProcessor(ESP)packetreadysignalwas detectedbytheplatformcode. |
| CPLDversion | TheComplexProgrammableLogicDeviceversionnumber. |
| Firmwareversion | TheFirmware(ROMmon)versionnumber. |
| Logicalinsertdetecttime | ThetimethattheSPAwaslogicallydetectedbytheplatformcode. |
| BecameHAActivetime | ThetimethatthisFRUbecameHighAvailability(HA)activestatus. |


### `show platform hardware capacity`

> **Página:** 841 · **Modo:** Privileged EXEC (#) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the capacities and utilizations for the hardware resources, use the show platform hardware capacity command in privileged EXEC mode.

**Syntax:**

```text
show platform hardware capacity [resource-type]
```

**Parameters (Syntax Description):**

- `resource-type` — ( Optional) Hardware resource type; see the“ Usage Guidelines” section for the v a l id values.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SXF | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. Support was added for the i b can d r e write-e n g in e keywords. |

**Usage Guidelines:**

The valid values for resource-type are as follows: • acl --Displays the capacities and utilizations for ACL/QoS TCAM resources. • cpu --Displays the capacities and utilizations for CPU resources. • eobc --Displays the capacities and utilizations for Ethernet out-of-band channel resources. • fabric --Displays the capacities and utilizations for Switch Fabric resources. • flash --Displays the capacities and utilizations for Flash/NVRAM resources. • forwarding --Displays the capacities and utilizations for Layer 2 and Layer 3 forwarding resources. • ibc --Displays the capacities and utilizations for interboard communication resources. • interface --Displays the capacities and utilizations for interface resources. • monitor --Displays the capacities and utilizations for SPAN resources. • multicast --Displays the capacities and utilizations for Layer 3 multicast resources. • netflow --Displays the capacities and utilizations for NetFlow resources. • pfc --Displays the capacities and utilizations for all the PFC resources including Layer 2 and Layer 3 forwarding, NetFlow, CPU rate limiters, and ACL/QoS TCAM resources. • power --Displays the capacities and utilizations for power resources. • qos --Displays the capacities and utilizations for QoS policer resources. • rate-limit --Displays the capacities and utilizations for CPU rate limiter resources. • rewrite-engine --Displays the packet drop and performance counters of the central rewrite engine on supervisors and line cards. For detailed information, see the show platform hardware capacity rewrite-engine command documentation. • system --Displays the capacities and utilizations for system resources. • vlan --Displays the capacities and utilizations for VLAN resources. The show platform hardware capacity cpucommand displays the following information: • CPU utilization for the last 5 seconds (busy time and interrupt time), the percentage of the last 1-minute average busy time, and the percentage of the last 5-minute average busy time. • Processor memory total available bytes, used bytes, and percentage used. • I/O memory total available bytes, used bytes, and percentage used. The show platform hardware capacity eobccommand displays the following information: • Transmit and receive rate • Packets received and packets sent • Dropped received packets and dropped transmitted packets The show platform hardware capacity forwarding command displays the following information: • The total available entries, used entries, and used percentage for the MAC tables. • The total available entries, used entries, and used percentage for the FIB TCAM tables. The display is done per protocol base. • The total available entries, used entries, and used percentage for the adjacency tables. The display is done for each region in which the adjacency table is divided. • The created entries, failures, and resource usage percentage for the NetFlow TCAM and ICAM tables. • The total available entries and mask, used entries and mask, reserved entries and mask, and entries and mask used percentage for the ACL/QoS TCAM tables. The output displays the available, used, reserved, and used percentage of the labels. The output displays the resource of other hardware resources that are related to the ACL/QoS TCAMs (such as available, used, reserved, and used percentage of the LOU, ANDOR, and ORAND). • The available, used, reserved, and used percentage for the CPU rate limiters. The show platform hardware capacity interface command displays the following information: • Tx/Rx drops--Displays the sum of transmit and receive drop counters on each online module (aggregate for all ports) and provides the port number that has the highest drop count on the module. • Tx/Rx per port buffer size--Summarizes the port-buffer size on a per-module basis for modules where there is a consistent buffer size across the module. The show platform hardware capacity monitor command displays the following SPAN information: • The maximum local SPAN sessions, maximum RSPAN sessions, maximum ERSPAN sessions, and maximum service module sessions. • The local SPAN sessions used/available, RSPAN sessions used/available, ERSPAN sessions used/available, and service module sessions used/available. The show platform hardware capacity multicast command displays the following information: • Multicast Replication Mode: ingress and egress IPv4 and IPv6 modes. • The MET table usage that indicates the total used and the percentage used for each module in the system. • The bidirectional PIM DF table usage that indicates the total used and the percentage used. The show platform hardware capacity systemcommand displays the following information: • PFC operating mode (PFC Version: PFC3A, PFC3B, unknown, and so forth) • Supervisor redundancy mode (RPR, RPR+, SSO, none, and so forth) • Module-specific switching information, including the following information: • Part number (WS-SUP720-BASE, WS-X6548-RJ-45, and so forth) • Series (supervisor engine, fabric, CEF720, CEF256, dCEF256, or classic) • CEF Mode (central CEF, dCEF) The show platform hardware capacity vlan command displays the following VLAN information: • Total VLANs • VTP VLANs that are used • External VLANs that are used • Internal VLANs that are used • Free VLANs

**Example:**

This example shows how to display CPU capacity and utilization information for the route processor, the switch processor, and the LAN module in the Cisco 7600 series router:

```text
show platform hardware capacity cpu
CPU Resources
CPU utilization: Module 5 seconds 1 minute 5 minutes
1 RP 0% / 0% 1% 1%
1 SP 5% / 0% 5% 4%
7 69% / 0% 69% 69%
8 78% / 0% 74% 74%
Processor memory: Module Bytes: Total Used %Used
1 RP 176730048 51774704 29%
1 SP 192825092 51978936 27%
7 195111584 35769704 18%
8 195111584 35798632 18%
I/O memory: Module Bytes: Total Used %Used
1 RP 35651584 12226672 34%
1 SP 35651584 9747952 27%
7 35651584 9616816 27%
8 35651584 9616816 27%
```

This example shows how to display EOBC-related statistics for the route processor, the switch processor, and the DFCs in the Cisco 7600 series router:

```text
Router# show platform hardware capacity eobc
EOBC Resources
Module Packets/sec Total packets Dropped packets
1 RP Rx: 61 108982 0
Tx: 37 77298 0
1 SP Rx: 34 101627 0
Tx: 39 115417 0
7 Rx: 5 10358 0
Tx: 8 18543 0
8 Rx: 5 12130 0
Tx: 10 20317 0
```

This example shows how to display the current and peak switching utilization:

```text
Router# show platform hardware capacity fabric
Switch Fabric Resources
Bus utilization: current is 100%, peak was 100% at 12:34 12mar45
Fabric utilization: ingress egress
Module channel speed current peak current peak
1 0 20G 100% 100% 12:34 12mar45 100% 100% 12:34 12mar45
1 1 20G 12% 80% 12:34 12mar45 12% 80% 12:34 12mar45
4 0 20G 12% 80% 12:34 12mar45 12% 80% 12:34 12mar45
13 0 8G 12% 80% 12:34 12mar45 12% 80% 12:34 12mar45
```

This example shows how to display information about the total capacity, the bytes used, and the percentage that is used for the Flash/NVRAM resources present in the system:

```text
show platform hardware capacity flash
Flash/NVRAM Resources
Usage: Module Device Bytes: Total Used %Used
1 RP bootflash: 31981568 15688048 49%
1 SP disk0: 128577536 105621504 82%
1 SP sup-bootflash: 31981568 29700644 93%
1 SP const_nvram: 129004 856 1%
1 SP nvram: 391160 22065 6%
7 dfc#7-bootflash: 15204352 616540 4%
8 dfc#8-bootflash: 15204352 0 0%
```

This example shows how to display the capacity and utilization of the EARLs present in the system:

```text
Router# show platform hardware capacity forwarding
L2 Forwarding Resources
MAC Table usage: Module Collisions Total Used %Used
6 0 65536 11 1%
VPN CAM usage: Total Used %Used
512 0 0%
L3 Forwarding Resources
FIB TCAM usage: Total Used %Used
72 bits (IPv4, MPLS, EoM) 196608 36 1%
144 bits (IP mcast, IPv6) 32768 7 1%
detail: Protocol Used %Used
IPv4 36 1%
MPLS 0 0%
EoM 0 0%
IPv6 4 1%
IPv4 mcast 3 1%
IPv6 mcast 0 0%
Adjacency usage: Total Used %Used
1048576 175 1%
Forwarding engine load:
Module pps peak-pps peak-time
6 8 1972 02:02:17 UTC Thu Apr 21 2005
Netflow Resources
TCAM utilization: Module Created Failed %Used
6 1 0 0%
ICAM utilization: Module Created Failed %Used
6 0 0 0%
Flowmasks: Mask# Type Features
IPv4: 0 reserved none
IPv4: 1 Intf FulNAT_INGRESS NAT_EGRESS FM_GUARDIAN
IPv4: 2 unused none
IPv4: 3 reserved none
IPv6: 0 reserved none
IPv6: 1 unused none
IPv6: 2 unused none
IPv6: 3 reserved none
CPU Rate Limiters Resources
Rate limiters: Total Used Reserved %Used
Layer 3 9 4 1 44%
Layer 2 4 2 2 50%
ACL/QoS TCAM Resources
Key: ACLent - ACL TCAM entries, ACLmsk - ACL TCAM masks, AND - ANDOR,
QoSent - QoS TCAM entries, QOSmsk - QoS TCAM masks, OR - ORAND,
Lbl-in - ingress label, Lbl-eg - egress label, LOUsrc - LOU source,
LOUdst - LOU destination, ADJ - ACL adjacency
Module ACLent ACLmsk QoSent QoSmsk Lbl-in Lbl-eg LOUsrc LOUdst AND OR ADJ
6 1% 1% 1% 1% 1% 1% 0% 0% 0% 0% 1%
```

This example shows how to display the interboard communication resources:

```text
Router# show platform hardware capacity ibc
IBC Resources
Module Packets/sec Total packets Dropped packets
1 RP Rx: 3 5001419 0
Tx: 1 1943884 0
```

This example shows how to display the interface resources:

```text
Router# show platform hardware capacity interface
Interface Resources
Interface drops:
Module Total drops: Tx Rx Highest drop port: Tx Rx
9 0 2 0 48
Interface buffer sizes:
Module Bytes: Tx buffer Rx buffer
1 12345 12345
5 12345 12345
```

This example shows how to display SPAN information:

```text
Router# show platform hardware capacity monitor
SPAN Resources
Source sessions: 2 maximum, 0 used
Type Used
Local 0
RSPAN source 0
ERSPAN source 0
Service module 0
Destination sessions: 64 maximum, 0 used
Type Used
RSPAN destination 0
ERSPAN destination (max 24) 0
```

This example shows how to display the capacity and utilization of resources for Layer 3 multicast functionality:

```text
Router# show platform hardware capacity
multicast
L3 Multicast Resources
IPv4 replication mode: ingress
IPv6 replication mode: ingress
Bi-directional PIM Designated Forwarder Table usage: 4 total, 0 (0%) used
Replication capability: Module IPv4 IPv6
5 egress egress
9 ingress ingress
MET table Entries: Module Total Used %Used
5 65526 6 0%
```

This example shows how to display information about the system power capacities and utilizations:

```text
Router# show platform hardware capacity power
Power Resources
Power supply redundancy mode: administratively combined
operationally combined
System power: 1922W, 0W (0%) inline, 1289W (67%) total allocated
Powered devices: 0 total
```

This example shows how to display the capacity and utilization of QoS policer resources per EARL in the Cisco 7600 series router:

```text
show platform hardware capacity qos
QoS Policer Resources
Aggregate policers: Module Total Used %Used
1 1024 102 10%
5 1024 1 1%
Microflow policer configurations: Module Total Used %Used
1 64 32 50%
5 64 1 1%
```

This example shows how to display information about the key system resources:

```text
Router# show platform hardware capacity system
System Resources
PFC operating mode: PFC3BXL
Supervisor redundancy mode: administratively rpr-plus, operationally rpr-plus
Switching Resources: Module Part number Series CEF mode
5 WS-SUP720-BASE supervisor CEF
9 WS-X6548-RJ-45 CEF256 CEF
```

This example shows how to display VLAN information:

```text
show platform hardware capacity vlan
VLAN Resources
VLANs: 4094 total, 10 VTP, 0 extended, 0 internal, 4084 free
```


### `show platform isg`

> **Página:** 848 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display Constellation WAN (CWAN) iEdge Route Processor information, use the show platform isgcommand in privileged EXEC mode.

**Syntax:**

```text
show platform isg {memory {detailed} | msi-all | slot | session-count | {slot-number | all} | uid |
{subscriber-session UID | all} | vrf | {vrf-number | all}}
```

**Parameters (Syntax Description):**

- `memory` — D is p l a y s memory usage information.
- `detailed` — D is p l a y s detailed memory usage information.
- `msi-all` — D is p l a y s C W AN M u l t is e r v i c e Interface( M S I) information.
- `slot` — D is p l a y s a c t i v e slot session information.
- `session-count` — D is p l a y s CWANi E d g e session count information.
- `slot-number` — Slot number.
- `all` — D is p l a y s information about all CWANi E d g e slot s.
- `uid` — D is p l a y s C W AN information b as e do n Unique ID.
- `subscriber-sessionUID` — D is p l a y s C W AN information for as p e c if i c ID(1-4294967295).
- `all` — D is p l a y s information for all subscriber session IDs.
- `vrf` — D is p l a y s CWANi Edge V P N r out in g and for w a r d in g( VRF) information.
- `vrf-number` — VRFID.
- `all` — D is p l a y s information about all CWANVRFs.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRC | This command was introduced. |
| 15.0(1)S | The memory, session-count, and u id keywords were added. |

**Example:**

The following is sample output from the show platform isg vrf allcommand. The field descriptions are self-explanatory.

```text
Router# show platform isg vrf all
dbg_stdby_cd_fibobj 35042
dbg_stdby_cd_rem_fibobj 492
dbg_stdby_cd_no_objhdl 1120
dbg_stdby_cd_no_ps 0
dbg_stdby_unpck_vrf_node 1612
dbg_stdby_unpck_pl_hdl 33922
dbg_stdby_unpck_rem_vrf_node 0
```


### `show platform oam`

> **Página:** 849 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display Operation, Administration, and Maintenance (OAM) information of a platform, use the show platform oamcommand in privileged EXEC mode.

**Syntax:**

```text
show platform oam {link-monitor [interface type number] | loopback}
```

**Parameters (Syntax Description):**

- `link-monitor` — D is p l a y s link monitor in g information.
- `interface type number` — ( Optional) D is p l a y s the interface name and number.
- `l o o p b a c k` — D is p l a y s information about the l o o p b a c k ports.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRC | This command was introduced. |

**Example:**

The following is sample output from the show platform oam link-monitor interface GigabitEthernet 1/1command. The fields are self-explanatory.

```text
show platform oam link-monitor interface GigabitEthernet 1/1
Interface Gi1/1:
first_poll = 0
symprd_tlv_sent = 0
frmprd_tlv_sent = 0
frm_poll_cnt = 1
frmsec_poll_cnt = 10
rxcrc_poll_cnt = 1
txcrc_poll_cnt = 1
symbol_period_start = 00:00:01.752
prev_rx_error_frames = 2
total_rx_error_frames = 0
error_frame_period_start = 2
total_frame_period_start = 20
prev_error_frame_seconds = 0
total_error_frame_seconds = 0
prev_rx_crc_error_frames = 0
prev_tx_crc_error_frames = 2
total_frm_tlvs = 0
total_frmsec_tlvs = 0
total_symprd_tlvs = 0
total_frmprd_tlvs = 0
```


### `show platform redundancy`

> **Página:** 850 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display platform-specific Constellation WAN (CWAN) redundancy information, use the show platform redundancycommand in privileged EXEC mode.

**Syntax:**

```text
show platform redundancy {atm | ccb slot-number cpu-number | cwpa-ce3 | cwpa-ct3 | cwpa-e1 |
cwpa-stm1 | cwpa-t1 | frame-relay | hdlc | if-config {slot-number cpu-number [bay-number] |
default-retvals} | mlp | multilink-vc | osm-chocx | osm-ct3 | ppp | shadowstate | spa-chocx | spa-ct3 |
switchover}
```

**Parameters (Syntax Description):**

- `atm` — D is p l a y s C W AN AT M redundancy state information.
- `ccp` — D is p l a y s the C W AN Configuration Control B lock( C C B) list.
- `slot-number` — Slot number.
- `cpu-number` — CPU number.
- `cwpa-ce3` — D is p l a y s C W AN port a d ap t e r( C W P A) C h an n e l i z e d E3( C E3) redundancy state information.
- `cwpa-ct3` — D is p l a y s C W P A-C T3 redundancy state information.
- `cwpa-e1` — D is p l a y s C W P A-E1 redundancy state information.
- `cwpa-stm1` — D is p l a y s C W P ASync h r on o u s T r an s port Module level-1( S T M-1) v i r t u a l c i r c u it( V C) information.
- `cwpa-t1` — D is p l a y s C W P A-T1 redundancy state information.
- `frame-relay` — D is p l a y s C W AN F r a m e R e l a y redundancy state information.
- `hdlc` — D is p l a y s C W AN H i g h-Level Data Link Control( H D L C) redundancy state information.
- `if-config` — D is p l a y s the C W AN IF-configuration list.
- `bay-number` — ( Optional) S h are d Port A d ap t e r( S P A) b a y number.
- `default-retvals` — D is p l a y s default IF-configuration return values.
- `mlp` — D is p l a y s C W AN M u l t i link P o in t-to-P o in t P r o to c o l( M L P) redundancy state information.
- `multilink-vc` — D is p l a y s C W AN M u l t i link V C information.
- `osm-chocx` — D is p l a y s C W AN O p t i c a l Service s Module( O S M) C h an n e l i z e d O C-12/ O C-3 line card ( C H O C X) redundancy state information.
- `osm-ct3` — D is p l a y s C W AN O S M-C T3 redundancy state information.
- `ppp` — D is p l a y s C W AN PPP redundancy state information.
- `s had o w state` — D is p l a y s the C W AN interface d e s c r ip to r b lock( IDB) s had o w state.
- `spa-chocx` — D is p l a y s C H O C X S P A V C information.
- `spa-ct3` — D is p l a y s C T3 S P A V C information.
- `switch over` — D is p l a y s C W AN switch over redundancy information.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRC | This command was introduced. |

**Example:**

The following is sample output from the show platform redundancycommand with the if-config keyword. The fields are self-explanatory.

```text
Router# show platform redundancy if-config 4 0
Current number of elements = 0
Current maximum elements = 128
List was grown = 0 times
Number of elements sorted = 0
List errors = 0
List flags = 0x1E
Current element pointer = 0x0
List pointer = 0x50A27438
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
| C=Command T=Type P=Port t=timedOut D=Dirty S=Sync |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
| C | T | P | key address | t | D | S | value |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
```


### `show platform software filesystem`

> **Página:** 851 · **Modo:** Privileged EXEC (#) Diagnostic (diag) · **Default:** No default behavior or values · **Leitura (show/clear/…):** sim

**Description:** To display information about file systems, use the show platform software filesystemcommand in privileged EXEC or diagnostic mode.

**Syntax:**

```text
show platform software filesystem {bootflash: | stby-bootflash: | fpd: | harddisk: | stby-harddisk: |
obfl: | stby-obfl: | usb0: | stby-usb0: | usb1: | stby-usb1:} [all] [details]
```

**Parameters (Syntax Description):**

- `bootflash:` — Filesystem on the bootflash device.
- `s t by-bootflash:` — S t and by filesystem on the bootflash device( if the s t and by Route Processor[ R P] is p reset).
- `fpd:` — S y n the t i c filesystem that is used by the f i e l d-p r o g r a m m a b l e device( F P D) upgrade process--for Cisco Tech n i c a l Support only.
- `h a r d disk:` — Filesystem on the h a r d disk device.
- `s t by-h a r d disk:` — S t and by filesystem on the h a r d disk device( if the s t and by R P is p reset).
- `obfl:` — Filesystem on the on b o a r d f a i l u r e logging( O B F L) device.
- `s t by-o b f l:` — S t and by filesystem on the O B F L device( if the s t and by R P is p reset).
- `usb0:` — Filesystem on the USB0 device( if install e d).
- `s t by-usb0:` — S t and by filesystem on the USB0 device( if the s t and by R P is p reset).
- `usb1:` — Filesystem on the USB1 device( if install e d).
- `s t by-usb1:` — S t and by filesystem on the USB1 device( if the s t and by R P is p reset).
- `all` — ( Optional) All p o s s i b l e device information.
- `details` — ( Optional) Filesystem detail s.

**Command Default:** No default behavior or values

**Command Modes:** Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers. |

**Usage Guidelines:**

Use this command to ascertain the presence or absence of specific files and to determine space usage in the file system. This command is helpful to monitor the growth of log file sizes, because rapid growth of log files could indicate possible problems with the router.

**Example:**

The following example displays information about the files in the bootflash file system. It also shows the number of bytes used out of the total available in the bootflash file system.

```text
Router# show platform software filesystem bootflash:
-#- --length-- ---------date/time--------- path
1 4096 Apr 01 2008 13:34:30 +00:00 /bootflash/
2 16384 Dec 04 2007 04:32:46 +00:00 /bootflash/lost+found
3 4096 Dec 04 2007 06:06:24 +00:00 /bootflash/.ssh
4 963 Dec 04 2007 06:06:16 +00:00 /bootflash/.ssh/ssh_host_key
5 627 Dec 04 2007 06:06:16 +00:00 /bootflash/.ssh/ssh_host_key.pub
6 1675 Dec 04 2007 06:06:18 +00:00 /bootflash/.ssh/ssh_host_rsa_key
7 382 Dec 04 2007 06:06:18 +00:00 /bootflash/.ssh/ssh_host_rsa_key.pub
8 668 Dec 04 2007 06:06:24 +00:00 /bootflash/.ssh/ssh_host_dsa_key
9 590 Dec 04 2007 06:06:24 +00:00 /bootflash/.ssh/ssh_host_dsa_key.pub
10 4096 Dec 04 2007 06:06:36 +00:00 /bootflash/.rollback_timer
11 4096 Mar 18 2008 17:31:17 +00:00 /bootflash/.prst_sync
12 4096 Dec 04 2007 04:34:45 +00:00 /bootflash/.installer
13 205951180 Mar 18 2008 17:23:03 +00:00 /bootflash/asr1000rp1-advipservicesk
14 46858444 Mar 18 2008 17:28:55 +00:00 /bootflash/asr1000rp1-espbase.02.01.
15 20318412 Mar 18 2008 17:28:56 +00:00 /bootflash/asr1000rp1-rpaccess-k9.02
16 22266060 Mar 18 2008 17:28:57 +00:00 /bootflash/asr1000rp1-rpbase.02.01.0
17 21659852 Mar 18 2008 17:28:57 +00:00 /bootflash/asr1000rp1-rpcontrol.02.0
18 45934796 Mar 18 2008 17:28:58 +00:00 /bootflash/asr1000rp1-rpios-advipser
19 34169036 Mar 18 2008 17:28:59 +00:00 /bootflash/asr1000rp1-sipbase.02.01.
20 22067404 Mar 18 2008 17:29:00 +00:00 /bootflash/asr1000rp1-sipspa.02.01.0
21 7180 Mar 18 2008 17:29:00 +00:00 /bootflash/packages.conf
461897728 bytes available (419782656 bytes used)
```

The following example displays information only about the bootflash file system itself, such as file system type and access permissions:

```text
Router# show platform software filesystem bootflash: details
Filesystem: bootflash
Filesystem Path: /bootflash
Filesystem Type: ext2
Mounted: Read/Write
```

The table below describes the significant fields shown in the displays of file system information.

| Field | Description |
| --- | --- |
| # | Displaylinenumber. |
| Length | Filesizeinbytes. |
| Date/Time | Dateandtimethefilesystemwascreated. |
| Path | Fullpathofafileinthefilesystem. |
| FilesystemPath | Rootofthefilesystem. |
| FilesystemType | Typeoffilesystem.Oneofthefollowingvalues: •ext2--Secondextendedfilesystem. •jffs2--Journalingflashfilesystem,version2. •vfat--Virtualfileallocationtable(FAT16or FAT32). |
| Mounted | Accesspermissionstothefilesystem. |


### `show platform software memory`

> **Página:** 854 · **Modo:** Privileged EXEC (#) Diagnostic (diag) · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To display memory information for the specified process, use the show platform software memorycommand in privileged EXEC or diagnostic mode.

**Syntax:**

```text
show platform software memory [database | messaging] {chassis-manager slot | cpp-control-process
process | cpp-driver process | cpp-ha-server process | cpp-service-process process | forwarding-manager
slot | host-manager slot | interface-manager slot | ios slot | logger slot | pluggable-services slot |
shell-manager slot} [brief]
```

**Parameters (Syntax Description):**

- `data b as e data b as e` — ( Optional) D is p l a y s data b as e memory information for the specified process.
- `m e s s a g in g` — ( Optional) D is p l a y s m e s s a g in g memory information for specified process. The information d is p l a y e d is for in t e r n a l debugging p u r p o s e s only.
- `chassis-manager slot` — D is p l a y s memory information for the Chassis M an age r process in the specified slot. P o s s i b l e slot values are: •0--Cisco AS R1000 S e r i e s S P A Interface Processor( S IP) slot0 •1--Cisco AS R1000 S e r i e s S IP slot1 •2--Cisco AS R1000 S e r i e s S IP slot2 • f0--Cisco AS R1000 S e r i e s E m be d d e d Service s Processor( E S P) slot0 • f1--Cisco AS R1000 S e r i e s E S P slot1 • f p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s ESP • f p s t and by--S t and by Cisco AS R1000 S e r i e s ESP • r0--Cisco AS R1000 S e r i e s Route Processor( R P) slot0 • r1--Cisco AS R1000 S e r i e s RPslot1 • r p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s RP • r p s t and by--S t and by Cisco AS R1000 S e r i e s RP
- `cpp-control-process` — D is p l a y s memory information for the specified Cisco Packet Processor( C P P) Client Control process. P o s s i b l e process values are: • c p p a c t i v e--A c t i v e C P P Client Control process • c p p s t and by--S t and by C P P Client Control process The information d is p l a y e d is for in t e r n a l debugging p u r p o s e s only.
- `cpp-driver` — D is p l a y s memory information for the specified C P P Driver process. P o s s i b l e process values are: • c p p a c t i v e--A c t i v e C P P Driver process • c p p s t and by--S t and by C P P Driver process The information d is p l a y e d is for in t e r n a l debugging p u r p o s e s only.
- `cpp-ha-server` — D is p l a y s memory information for the specified CPPHigh A v a i l a b i l it y( H A) Server process. P o s s i b l e process values are: • c p p a c t i v e--A c t i v e C P P HAS e r v e r process • c p p s t and by--S t and by C P P HAS e r v e r process The information d is p l a y e d is for in t e r n a l debugging p u r p o s e s only.
- `cpp-service-process` — D is p l a y s memory information for the specified C P P Client Service process. P o s s i b l e process values are: • c p p a c t i v e--A c t i v e C P P Client Service process • c p p s t and by--S t and by C P P Client Service process The information d is p l a y e d is for in t e r n a l debugging p u r p o s e s only.
- `forwarding-manager slot` — D is p l a y s memory information for the For w a r d in g M an age r process in the specified slot. P o s s i b l e slot values are: • f0--Cisco AS R1000 S e r i e s E S P slot0 • f1--Cisco AS R1000 S e r i e s E S P slot1 • f p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s ESP • f p s t and by--S t and by Cisco AS R1000 S e r i e s ESP • r0--Cisco AS R1000 S e r i e s RPslot0 • r1--Cisco AS R1000 S e r i e s RPslot1 • r p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s RP • r p s t and by--S t and by Cisco AS R1000 S e r i e s RP
- `host-manager slot` — D is p l a y s memory information for the Host M an age r process in the specified slot. P o s s i b l e slot values are: •0--Cisco AS R1000 S e r i e s S IP slot0 •1--Cisco AS R1000 S e r i e s S IP slot1 •2--Cisco AS R1000 S e r i e s S IP slot2 • f0--Cisco AS R1000 S e r i e s E S P slot0 • f1--Cisco AS R1000 S e r i e s E S P slot1 • f p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s ESP • f p s t and by--S t and by Cisco AS R1000 S e r i e s ESP • r0--Cisco AS R1000 S e r i e s RPslot0 • r1--Cisco AS R1000 S e r i e s RPslot1 • r p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s RP • r p s t and by--S t and by Cisco AS R1000 S e r i e s RP
- `interface-manager slot` — D is p l a y s memory information for the Interface M an age r process in the specified slot. P o s s i b l e slot values are: •0--Cisco AS R1000 S e r i e s S IP slot0 •1--Cisco AS R1000 S e r i e s S IP slot1 •2--Cisco AS R1000 S e r i e s S IP slot2 • r0--Cisco AS R1000 S e r i e s RPslot0 • r1--Cisco AS R1000 S e r i e s RPslot1 • r p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s RP • r p s t and by--S t and by Cisco AS R1000 S e r i e s RP
- `ios slot` — D is p l a y s memory information for the IOS process in the specified slot. P o s s i b l e slot values are: •0/0--Cisco AS R1000 S e r i e s S IP slot0, b a y0 •0/1--Cisco AS R1000 S e r i e s S IP slot0, b a y1 •0/2--Cisco AS R1000 S e r i e s S IP slot0, b a y2 •0/3--Cisco AS R1000 S e r i e s S IP slot0, b a y3 •1/0--Cisco AS R1000 S e r i e s S IP slot1, b a y0 •1/1--Cisco AS R1000 S e r i e s S IP slot1, b a y1 •1/2--Cisco AS R1000 S e r i e s S IP slot1, b a y2 •1/3--Cisco AS R1000 S e r i e s S IP slot1, b a y3 •2/0--Cisco AS R1000 S e r i e s S IP slot2, b a y0 •2/1--Cisco AS R1000 S e r i e s S IP slot2, b a y1 •2/2--Cisco AS R1000 S e r i e s S IP slot2, b a y2 •2/3--Cisco AS R1000 S e r i e s S IP slot2, b a y3 • r0--Cisco AS R1000 S e r i e s RPslot0 • r1--Cisco AS R1000 S e r i e s RPslot1 • r p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s RP • r p s t and by--S t and by Cisco AS R1000 S e r i e s RP
- `logger slot` — D is p l a y s memory information for the log g e r process in the specified slot. P o s s i b l e slot values are: •0--Cisco AS R1000 S e r i e s S IP slot0 •1--Cisco AS R1000 S e r i e s S IP slot1 •2--Cisco AS R1000 S e r i e s S IP slot2 • f0--Cisco AS R1000 S e r i e s E S P slot0 • f1--Cisco AS R1000 S e r i e s E S P slot1 • f p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s ESP • f p s t and by--S t and by Cisco AS R1000 S e r i e s ESP • r0--Cisco AS R1000 S e r i e s RPslot0 • r1--Cisco AS R1000 S e r i e s RPslot1 • r p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s RP • r p s t and by--S t and by Cisco AS R1000 S e r i e s RP
- `p l u g g a b l e-service s slot` — D is p l a y s memory information for the p l u g g a b l e-service s process in the specified slot. P o s s i b l e slot values are: • r0--Cisco AS R1000 S e r i e s RPslot0 • r1--Cisco AS R1000 S e r i e s RPslot1 • r p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s RP • r p s t and by--S t and by Cisco AS R1000 S e r i e s RP
- `shell-manager slot` — D is p l a y s memory information for the Shell M an age r process in the specified slot. P o s s i b l e slot values are: • r0--Cisco AS R1000 S e r i e s RPslot0 • r1--Cisco AS R1000 S e r i e s RPslot1 • r p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s RP • r p s t and by--S t and by Cisco AS R1000 S e r i e s RP
- `brief` — ( Optional) D is p l a y s a b b r e v i at e d memory information for the specified process.

**Command Default:** No default behavior or values.

**Command Modes:** Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers. |

**Usage Guidelines:**

The specification of the database and brief keywords are optional. The specification of a process and slot are required.

**Example:**

The following example displays memory information for the Forwarding Manager process for Cisco ASR 1000 Series RP slot 0:

```text
Router# show platform software memory forwarding-manager r0
Module: cdllib
allocated: 900, requested: 892, overhead: 8
Allocations: 2, failed: 0, frees: 1
Module: eventutil
allocated: 117379, requested: 117059, overhead: 320
Allocations: 46, failed: 0, frees: 6
Module: uipeer
allocated: 9264, requested: 9248, overhead: 16
Allocations: 3, failed: 0, frees: 1
Module: Summary
allocated: 127543, requested: 127199, overhead: 344
Allocations: 51, failed: 0, frees: 8
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Module: | Nameofsubmodule. |
| allocated: | Memory,allocatedinbytes. |
| requested: | Numberofbytesrequestedbyapplication. |
| overhead: | Allocationoverhead. |
| Allocations: | Numberofdiscreteallocationeventattempts. |
| failed: | Numberofallocationattemptsthatwereattempted,butfailed. |
| frees: | Numberoffreeevents. |

The following example displays abbreviated (brief keyword) memory information for the Chassis Manager process for Cisco ASR 1000 Series ESP slot 0:

```text
Router# show platform software memory chassis-manager f0 brief
module allocated requested allocs frees
------------------------------------------------------------------------
CPP Features 692 668 3 0
Summary 497816 495344 323 14
chunk 419322 419290 4 0
eventutil 68546 66146 312 12
uipeer 9256 9240 4 2
```

The table below describes the significant fields shown in the brief keyword display.

| Field | Description |
| --- | --- |
| module | Nameofsubmodule. |
| allocated | Memory,allocatedinbytes. |
| requested | Numberofbytesrequestedbyapplication. |
| allocs | Numberofdiscreteallocationeventattempts. |
| frees | Numberoffreeevents. |


### `show platform software mount`

> **Página:** 859 · **Modo:** Privileged EXEC (#) Diagnostic (diag) · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To display the mounted file systems, both physical and virtual, for a Cisco ASR 1000 Series SPA Interface Processor (SIP), Cisco ASR 1000 Series Embedded Services Processor (ESP), or Cisco ASR 1000 Series Route Processor (RP), use the show platform software mountcommand in privileged EXEC or diagnostic mode.

**Syntax:**

```text
show platform software mount [slot [brief]]
```

**Parameters (Syntax Description):**

- `slot` — ( Optional) D is p l a y s mount e d filesystem s for the specified slot. P o s s i b l e slot values are: •0--Cisco AS R1000 S e r i e s S IP slot0 •1--Cisco AS R1000 S e r i e s S IP slot1 •2--Cisco AS R1000 S e r i e s S IP slot2 • f0--Cisco AS R1000 S e r i e s E S P slot0 • f1--Cisco AS R1000 S e r i e s E S P slot1 • f p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s ESP • f p s t and by--S t and by Cisco AS R1000 S e r i e s ESP • r0--Cisco AS R1000 S e r i e s RPslot0 • r1--Cisco AS R1000 S e r i e s RPslot1 • r p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s RP • r p s t and by--S t and by Cisco AS R1000 S e r i e s RP
- `brief` — ( Optional) D is p l a y s a b b r e v i at e d mount e d filesystem information.

**Command Default:** No default behavior or values.

**Command Modes:** Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers. |

**Usage Guidelines:**

If no slot is specified, the command returns mounted file systems for the active RP. This command allows you to ascertain the presence or absence of specific system mounts. For example, this command might be used to determine /tmp-related mounts, which are used to create many run-time directories and files. Users may be requested to execute this command to collect information about the underlying configuration of the platform software. The RP output can differ depending on how the router was booted, and whether there are USB devices inserted. The SIP and ESP output can differ depending on whether the chassis is a dual or single RP.

**Example:**

The following example displays mounted file systems for the active RP:

```text
Router# show platform software mount
Filesystem Used Available Use% Mounted on
rootfs 0 0 - /
proc 0 0 - /proc
sysfs 0 0 - /sys
none 524 1037640 1% /dev
/dev/bootflash1 298263 42410 88% /bootflash
/dev/harddisk1 609208 4025132 14% /misc/scratch
/dev/loop1 28010 0 100% /tmp/sw/mount/2007-10-14_...
/dev/loop2 26920 0 100% /tmp/sw/mount/2007-10-14_...
/dev/loop3 48236 0 100% /tmp/sw/mount/2007-10-14_...
/dev/loop4 6134 0 100% /tmp/sw/mount/2007-10-14_...
/dev/loop5 43386 0 100% /tmp/sw/mount/2007-10-14_...
/dev/loop6 30498 0 100% /tmp/sw/mount/2007-10-14_...
/dev/loop7 14082 0 100% /tmp/sw/mount/2007-10-14_...
none 524 1037640 1% /dev
/proc/bus/usb 0 0 - /proc/bus/usb
/dev/mtdblock1 460 1588 23% /obfl
automount(pid4165) 0 0 - /vol
```

The following example displays mounted file systems for the Cisco ASR 1000 Series ESP in ESP slot 0:

```text
Router# show platform software mount f0
Filesystem Used Available Use% Mounted on
rootfs 0 0 - /
proc 0 0 - /proc
sysfs 0 0 - /sys
none 10864 507124 3% /dev
/dev/loop1 41418 0 100% /tmp/sw/fp/0/0/fp/mount
none 10864 507124 3% /dev
/proc/bus/usb 0 0 - /proc/bus/usb
/dev/mtdblock1 504 1544 25% /obfl
automount(pid3210) 0 0 - /misc1
```

The following example displays mounted file systems for the active Cisco ASR 1000 Series RP:

```text
show platform software mount rp active
Filesystem Used Available Use% Mounted on
rootfs 0 0 - /
proc 0 0 - /proc
sysfs 0 0 - /sys
none 436 1037728 1% /dev
/dev/bootflash1 256809 83864 76% /bootflash
/dev/harddisk1 252112 4382228 6% /misc/scratch
/dev/loop1 30348 0 100% /tmp/sw/mount/2007-09-27_...
/dev/loop2 28394 0 100% /tmp/sw/mount/2007-09-27_...
/dev/loop3 42062 0 100% /tmp/sw/mount/2007-09-27_...
/dev/loop4 8384 0 100% /tmp/sw/mount/2007-09-27_...
/dev/loop5 41418 0 100% /tmp/sw/mount/2007-09-27_...
/dev/loop6 21612 0 100% /tmp/sw/mount/2007-09-27_...
/dev/loop7 16200 0 100% /tmp/sw/mount/2007-09-27_...
none 436 1037728 1% /dev
/proc/bus/usb 0 0 - /proc/bus/usb
/dev/mtdblock1 484 1564 24% /obfl
automount(pid4004) 0 0 - /vol
```

The table below describes the significant fields shown in the SIP slot (0, 1, or 2) displays.

| Field | Description |
| --- | --- |
| Filesystem | Logicalnameofthefilesystemdevice. |

| Field | Description |
| --- | --- |
| Used | Numberof1Kbblocksused. |
| Available | Numberoffree1Kbblocksavailable. |
| Use% | Percentageof1Kbblocksusedofthetotalavailable. |
| Mountedon | Canonicalpathtothemountedfilesystem. |

The following example displays abbreviated (brief keyword) mounted file system information for Cisco ASR 1000 Series SIP slot 0:

```text
Router# show platform software mount 0 brief
Mount point: rootfs
Type : rootfs
Location : /
Options : rw
Mount point: proc
Type : proc
Location : /proc
Options : rw
Mount point: sysfs
Type : sysfs
Location : /sys
Options : rw
Mount point: none
Type : tmpfs
Location : /dev
Options : rw
Mount point: /dev/loop1
Type : iso9660
Location : /tmp/sw/cc/0/0/cc/mount
Options : ro
Mount point: none
Type : tmpfs
Location : /dev
Options : rw
Mount point: /proc/bus/usb
Type : usbfs
Location : /proc/bus/usb
Options : rw
Mount point: /dev/mtdblock1
Type : jffs2
Location : /obfl
Options : rw,noatime,nodiratime
Mount point: automount(pid3199)
Type : autofs
Location : /misc1
Options : rw,fd=5,pgrp=3199,timeout=60,minproto=2,maxproto=4,indirect
```

The tab le below describes the significant fields shown in the brief keyword display.

| Field | Description |
| --- | --- |
| Mountpoint: | Logicalnameofthefilesystemdevice. |
| Type: | Filesystemtype. |
| Location: | Canonicalpathtothemountedfilesystem. |
| Options: | Mountpointtype-specificflagsandsettings. |


### `show platform software process list`

> **Página:** 863 · **Modo:** Privileged EXEC (#) Diagnostic (diag) · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To display a list of the processes running in a given slot, use the show platform software process listcommand in privileged EXEC or diagnostic mode. | summary]

**Syntax:**

```text
show platform software process list slot [name process-name | process-id process-id | sort memory
```

**Parameters (Syntax Description):**

- `slot` — D is p l a y s running process information for the specified slot. P o s s i b l e slot values are: •0--Cisco AS R1000 S e r i e s S P A Interface Processor( S IP) slot0 •1--Cisco AS R1000 S e r i e s S IP slot1 •2--Cisco AS R1000 S e r i e s S IP slot2 • f0--Cisco AS R1000 S e r i e s E m be d d e d Service s Processor( E S P) slot0 • f1--Cisco AS R1000 S e r i e s E S P slot1 • f p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s ESP • f p s t and by--S t and by Cisco AS R1000 S e r i e s ESP • r0--Cisco AS R1000 S e r i e s Route Processor( R P) slot0 • r1--Cisco AS R1000 S e r i e s RPslot1 • r p a c t i v e--A c t i v e Cisco AS R1000 S e r i e s RP • r p s t and by--S t and by Cisco AS R1000 S e r i e s RP
- `nameprocess-name` — ( Optional) D is p l a y s information for the specified process name.
- `process-idprocess-id` — ( Optional) D is p l a y s information for the specified process ID.
- `s or t memory` — ( Optional) S or t s the processes by memory.
- `summary` — ( Optional) D is p l a y s summary process information for the running host.

**Command Default:** No default behavior or values.

**Command Modes:** Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers. |

**Usage Guidelines:**

The name and process-id keywords can be used to narrow the process list display down to specific processes. The sort keyword can be used to sort the process list by memory size. The summary keyword can be used to display summary information about running processes.

**Example:**

The following example displays information about running processes for Cisco ASR 1000 Series SIP slot 0:

```text
Router# show platform software process list 0
Name Pid PPid Group Id Status Priority Size
------------------------------------------------------------------------------
init 1 0 1 S 20 1974272
ksoftirqd/0 2 1 1 S 39 0
events/0 3 1 1 S 15 0
khelper 4 1 1 S 15 0
kthread 5 1 1 S 15 0
kblockd/0 19 5 1 S 15 0
khubd 23 5 1 S 15 0
pdflush 59 5 1 S 20 0
pdflush 60 5 1 S 20 0
kswapd0 61 5 1 S 15 0
aio/0 62 5 1 S 15 0
xfslogd/0 63 5 1 S 15 0
xfsdatad/0 64 5 1 S 15 0
mtdblockd 626 1 1 S 20 0
loop0 1370 1 1 S 0 0
portmap 1404 1 1404 S 20 2076672
portmap 1406 1 1406 S 20 2076672
loop1 1440 1 1 S 0 0
udevd 2104 1 2104 S 16 1974272
jffs2_gcd_mtd1 2796 1 1 S 30 0
klogd 3093 1 3093 S 20 1728512
automount 3199 1 3199 S 20 2396160
xinetd 3214 1 3214 S 20 3026944
xinetd 3216 1 3216 S 20 3026944
pvp.sh 3540 1 3540 S 20 3678208
inotifywait 3575 3540 3575 S 20 1900544
pman.sh 3614 3540 3614 S 20 3571712
pman.sh 3714 3540 3714 S 20 3571712
btrace_rotate.s 3721 3614 3721 S 20 3133440
agetty 3822 1 3822 S 20 1720320
mcp_chvrf.sh 3823 1 3823 S 20 2990080
sntp 3824 1 3824 S 20 2625536
issu_switchover 3825 1 3825 S 20 3899392
xinetd 3827 3823 3823 S 20 3026944
cmcc 3862 3714 3862 S 20 26710016
pman.sh 3883 3540 3883 S 20 3571712
pman.sh 4014 3540 4014 S 20 3575808
hman 4020 3883 4020 R 20 19615744
imccd 4114 4014 4114 S 20 31539200
inotifywait 4196 3825 3825 S 20 1896448
pman.sh 4351 3540 4351 S 20 3575808
plogd 4492 4351 4492 S 20 22663168
inotifywait 4604 3721 4604 S 20 1900544
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Name | Nameoftheprocess. |
| Pid | ProcessID. |
| PPid | ParentProcessID. |
| GroupId | ProcessgroupID. |
| Status | Processstatus. |
| Priority | Processpriority. |
| Size | Virtualmemorysize(inbytes). |

The following example displays information about a specific named process for Cisco ASR 1000 Series SIP slot 0:

```text
Router# show platform software process list 0 name sleep
Name: sleep
Process id : 25938
Parent process id: 3891
Group id : 3891
Status : S
Session id : 3816
User time : 0
Kernel time : 0
Priority : 20
Virtual bytes : 2482176
Resident pages : 119
Resident limit : 4294967295
Minor page faults: 182
Major page faults: 0
```

The following example displays information about a specific process identifier for Cisco ASR 1000 Series SIP slot 0:

```text
show platform software process list 0 process-id 1
Name: init
Process id : 1
Parent process id: 0
Group id : 1
Status : S
Session id : 1
User time : 1
Kernel time : 741
Priority : 20
Virtual bytes : 1974272
Resident pages : 161
Resident limit : 4294967295
Minor page faults: 756
Major page faults: 0
```

The table below describes the significant fields shown in the name and process-id keyworddisplays.

| Field | Description |
| --- | --- |
| Name | Nameoftheprocess. |
| Processid | ProcessID. |
| Parentprocessid | ParentprocessID. |
| Groupid | ProcessgroupID. |
| Status | Processstatus. |
| Sessionid | ProcesssessionID. |
| Usertime | Time(inseconds)spentinusermode. |
| Kerneltime | Time(inseconds)spentinkernelmode. |
| Priority | Processpriority. |
| Virtualbytes | Virtualmemorysize(inbytes). |
| Residentpages | Residentpagesize. |
| Residentlimit | CurrentlimitonResidentpages. |
| Minorpagefaults | Numberofminorpagefaults. |
| Majorpagefaults | Numberofmajorpagefaults. |

The following example displays process summary information for Cisco ASR 1000 Series SIP slot 0:

```text
Router# show platform software process list 0 summary
Total number of processes: 54
Running : 4
Sleeping : 50
Disk sleeping : 0
Zombies : 0
Stopped : 0
Paging : 0
Up time : 1562
Idle time : 1511
User time : 1606
Kernel time : 1319
Virtual memory : 587894784
Pages resident : 45436
Major page faults: 25
Minor page faults: 149098
Architecture : ppc
Memory (kB)
Physical : 524288
Total : 479868
Used : 434948
Free : 44920
Active : 183020
Inactive : 163268
Inact-dirty : 0
Inact-clean : 0
Dirty : 0
AnonPages : 76380
Bounce : 0
Cached : 263764
Commit Limit : 239932
Committed As : 201452
High Total : 0
High Free : 0
Low Total : 479868
Low Free : 44920
Mapped : 59996
NFS Unstable : 0
Page Tables : 1524
Slab : 73760
VMmalloc Chunk : 426840
VMmalloc Total : 474856
VMmalloc Used : 47372
Writeback : 0
Swap (kB)
Total : 0
Used : 0
Free : 0
Cached : 0
Buffers (kB) : 6144
Load Average
1-Min : 0.00
5-Min : 0.00
15-Min : 0.00
```

The table below describes the significant fields shown in the summary keyword display.

| Field | Description |
| --- | --- |
| Totalnumberofprocesses | Totalnumberofprocessesinallpossiblestates. |
| Running | Numberofprocessesintherunningstate. |
| Sleeping | Numberofprocessesinthesleepingstate. |
| Disksleeping | Numberofprocessesinthedisk-sleepingstate. |
| Zombies | Numberofprocessesinthezombiestate. |
| Stopped | Numberofprocessesinthestoppedstate. |
| Paging | Numberofprocessesinthepagingstate. |
| Uptime | SystemUptime(inseconds). |
| Idletime | SystemIdletime(inseconds). |

| Field | Description |
| --- | --- |
| Usertime | Systemtime(inseconds)spentinusermode. |
| Kerneltime | Systemtime(inseconds)spentinkernelmode. |
| Virtualmemory | Virtualmemorysize(inbytes). |
| Pagesresident | Residentpagesize. |
| Majorpagefaults | Numberofmajorpagefaults. |
| Minorpagefaults | Numberofminorpagefaults. |
| Architecture | SystemCPUarchitecture:PowerPC(ppc). |
| Memory(kB) | Systemmemoryheading. |
| Physical | Totalphysicalmemory(inkilobytes). |
| Total | Totalavailablememory(inkilobytes).Thisvaluerepresentsthephysicalmemory availableforkerneluse. |
| Used | Usedmemory(inkilobytes). |
| Free | Freememory(inkilobytes). |
| Active | Mostrecentlyusedmemory(inkilobytes). |
| Inactive | Memory(inkilobytes)thathasbeenlessrecentlyused.Itismoreeligibletobe reclaimedforotherpurposes. |
| Inact-dirty | Memory(inkilobytes)thatmayneedtobewrittentopersistentstore(cacheor disk). |
| Inact-clean | Memory(inkilobytes)thatisreadilyavailableforre-use. |
| Dirty | Memory(inkilobytes)thatiswaitingtogetwrittenbacktothedisk. |
| AnonPages | Memory(inkilobytes)thatisallocatedwhenaprocessrequestsmemoryfrom thekernelviathemalloc()systemcall.Thismemoryhasnofilebackingondisk. |
| Bounce | Memory(inkilobytes)thatisallocatedtobouncebuffers. |
| Cached | AmountofphysicalRAM(inkilobytes)usedascachememory. |
| CommitLimit | Totalamountofmemory(inkilobytes)currentlyavailabletobeallocatedon thesystem.Thislimitisonlyadheredtoifstrictovercommitaccountingis enabled. |
| CommittedAs | Totalamountofmemory(inkilobytes)presentlyallocatedonthesystem.The committedmemoryisasumofallofthememorythathasbeenallocatedby processes,evenifithasnotbeenusedbythemasofyet. |
| HighTotal | Totalamountofmemory(inkilobytes)thatisnotdirectlymappedintokernel space.TheHighTotalvaluecanvarybasedonthetypeofkernelused. |

| Field | Description |
| --- | --- |
| HighFree | Amountoffreememory(inkilobytes)thatisnotdirectlymappedintokernel space.TheHighFreevaluecanvarybasedonthetypeofkernelused. |
| LowTotal | Totalamountofmemory(inkilobytes)thatisdirectlymappedintokernelspace. TheLowTotalvaluecanvarybasedonthetypeofkernelused. |
| LowFree | Amountoffreememory(inkilobytes)thatisdirectlymappedintokernelspace. TheLowFreevaluecanvarybasedonthetypeofkernelused. |
| Mapped | Totalamountofmemory(inkilobytes)thathasbeenusedtomapdevices,files, orlibrariesusingthemmapcommand. |
| NFSUnstable | Totalamountofmemory(inkilobytes)usedforunstableNFSpages.Unstable NFSpagesarepagesthathavebeenwrittenintothepagecacheontheserver, buthavenotyetbeensynchronizedtodisk. |
| PageTables | Totalamountofmemory(inkilobytes)dedicatedtothelowestpagetablelevel. |
| Slab | Totalamountofmemory(inkilobytes)usedbythekerneltocachedatastructures foritsownuse. |
| VMallocChunk | Largestcontiguousblockofavailablevirtualaddressspace(inkilobytes)that isfree. |
| VMallocTotal | Totalamountofmemory(inkilobytes)oftotalallocatedvirtualaddressspace. |
| VMallocUsed | Totalamountofmemory(inkilobytes)ofusedvirtualaddressspace. |
| Writeback | Memory(inkilobytes)thatisactivelybeingwrittenbacktothedisk. |
| Swap(kB) | Swapmemoryheading. |
| Total | Totalswapmemory(inkilobytes). |
| Used | Usedswapmemory(inkilobytes). |
| Free | Freeswapmemory(inkilobytes). |
| Cached | Cachedswapmemory(inkilobytes). |
| Buffers(kB) | Buffersheading. |
| LoadAverage | Indicatorsofsystemload. |
| 1-Min | Averagenumberofprocessesrunningforthelastminute. |
| 5-Min | Averagenumberofprocessesrunningforthelast5minutes. |
| 15-Min | Averagenumberofprocessesrunningforthelast15minutes. |

The following example displays process summary information for Cisco ASR 1000 Series sorted by memory size:

```text
Router#show platform software process list R0 sort memory
Name Pid PPid Group Id Status Priority Size
------------------------------------------------------------------------------
linux_iosd-imag 27982 26696 27982 S 20 4294967295
fman_rp 25857 25309 25857 S 20 684867584
vman 30685 29587 30685 S 20 194850816
smand 30494 28948 30494 S 20 103538688
libvirtd 5260 5254 5254 S 20 83197952
python 10234 10233 10210 S 20 29765632
python 10975 10234 10975 S 20 29765632
python 10977 10234 10977 S 20 29765632
python 10978 10234 10978 S 20 29765632
python 10979 10234 10979 S 20 29765632
python 10981 10234 10981 S 20 29765632
automount 15682 1 15682 S 20 25092096
cmand 25530 24760 25530 S 20 23789568
imand 27198 26090 27198 S 20 22040576
psd 31284 28535 31284 S 20 16019456
emd 25712 24917 25712 S 20 15302656
hman 26622 25617 26622 R 20 14544896
plogd 28878 27718 28878 S 20 12349440
btrace_rotate.s 25251 24643 25251 S 20 6008832
sort_files_by_i 30092 29066 30092 S 20 5234688
periodic.sh 28469 27490 28469 S 20 4812800
rotee 5403 1 5396 S 20 4788224
rotee 5412 1 5411 S 20 4788224
rotee 5438 1 5437 S 20 4788224
rotee 5482 1 5481 S 20 4788224
rotee 9844 1 9843 S 20 4788224
rotee 9958 1 9957 S 20 4788224
rotee 16942 1 16941 S 20 4788224
rotee 16946 1 16945 S 20 4788224
rotee 24383 1 24382 S 20 4788224
rotee 24742 1 24741 S 20 4788224
rotee 24960 1 24959 S 20 4788224
rotee 25107 1 25106 S 20 4788224
rotee 25534 1 25533 S 20 4788224
rotee 25542 1 25541 S 20 4788224
rotee 25880 1 25879 S 20 4788224
rotee 26390 1 26389 S 20 4788224
rotee 26881 1 26880 S 20 4788224
rotee 27728 1 27727 S 20 4788224
rotee 27882 1 27881 S 20 4788224
rotee 28867 1 28866 S 20 4788224
rotee 29220 1 29219 S 20 4788224
rotee 29257 1 29256 S 20 4788224
rotee 29405 1 29404 S 20 4788224
rotee 29784 1 29783 S 20 4788224
oom.sh 5560 5246 5560 S 20 4427776
reflector.sh 15598 1 15598 S 20 3997696
droputil.sh 15600 1 15600 S 20 3997696
pvp.sh 24336 1 24335 S 20 3870720
pman.sh 29066 24336 24335 S 14 3805184
pman.sh 24643 24336 24335 S 14 3801088
pman.sh 27490 24336 24335 S 14 3801088
pman.sh 26696 24336 24335 S 14 3788800
pman.sh 9679 24336 24335 S 14 3784704
pman.sh 9812 24336 24335 S 14 3784704
pman.sh 24760 24336 24335 S 14 3784704
pman.sh 24917 24336 24335 S 14 3784704
pman.sh 25309 24336 24335 S 14 3784704
pman.sh 25617 24336 24335 S 14 3784704
pman.sh 26090 24336 24335 S 14 3784704
pman.sh 27718 24336 24335 S 14 3784704
pman.sh 28535 24336 24335 S 14 3784704
pman.sh 28948 24336 24335 S 14 3784704
pman.sh 29587 24336 24335 S 14 3784704
chasync.sh 5248 1 5248 S 20 3620864
lighttpd 11522 11521 10223 S 20 3543040
iptbl.sh 5252 1 5252 S 20 3477504
rollback_timer. 5226 1 5226 S 20 3014656
oom.sh 5246 1 5246 S 20 2977792
wui-lighttpd-la 10223 9812 10223 S 20 2605056
wui-app-launch. 10210 9679 10210 S 20 2600960
mcp_chvrf.sh 10233 10210 10210 S 20 2596864
mcp_chvrf.sh 11521 10223 10223 S 20 2596864
auxinit.sh 15593 1 15593 S 20 2584576
mcp_chvrf.sh 5223 1 5223 S 20 2580480
mcp_chvrf.sh 5224 1 5224 S 20 2580480
libvirtd.sh 5254 1 5254 S 20 2576384
xinetd 5231 5223 5223 S 20 2183168
xinetd 5232 5224 5224 S 20 2183168
xinetd 15714 1 15714 S 20 2183168
xinetd 15716 1 15716 S 20 2183168
sleep 30979 28469 28469 S 20 1925120
sleep 31820 5560 5560 S 20 1925120
sleep 32645 30092 30092 S 20 1925120
sntp 5225 1 5225 S 20 1863680
init 1 0 1 S 20 1859584
portmap 2654 1 2654 S 20 1806336
rpc.mountd 15751 1 15751 S 20 1789952
inotifywait 5459 5248 5459 S 20 1761280
inotifywait 16968 15598 16968 S 20 1761280
inotifywait 17050 15600 17050 S 20 1761280
inotifywait 24572 24336 24335 S 20 1761280
inotifywait 5462 5226 5462 S 20 1757184
inotifywait 5522 5252 5522 S 20 1757184
udevd 13853 1 13853 S 16 1757184
inotifywait 32725 25251 32725 S 20 1757184
klogd 24325 1 24325 S 20 1650688
kthreadd 2 0 0 S 15 0
migration/0 3 2 0 S 4294967196 0
ksoftirqd/0 4 2 0 S 15 0
watchdog/0 5 2 0 S 4294967196 0
migration/1 6 2 0 S 4294967196 0
ksoftirqd/1 7 2 0 S 15 0
watchdog/1 8 2 0 S 4294967196 0
events/0 9 2 0 S 15 0
events/1 10 2 0 S 15 0
khelper 11 2 0 S 15 0
netns 14 2 0 S 15 0
kblockd/0 59 2 0 S 15 0
kblockd/1 60 2 0 S 15 0
kacpid 61 2 0 S 15 0
kacpi_notify 62 2 0 S 15 0
cqueue 144 2 0 S 15 0
ata/0 148 2 0 S 15 0
ata/1 149 2 0 S 15 0
ata_aux 150 2 0 S 15 0
ksuspend_usbd 151 2 0 S 15 0
khubd 156 2 0 S 15 0
kseriod 159 2 0 S 15 0
pdflush 210 2 0 S 20 0
pdflush 211 2 0 S 20 0
kswapd0 212 2 0 S 15 0
aio/0 256 2 0 S 15 0
aio/1 257 2 0 S 15 0
scsi_eh_0 1077 2 0 S 15 0
scsi_eh_1 1079 2 0 S 15 0
scsi_eh_2 1081 2 0 S 15 0
scsi_eh_3 1083 2 0 S 15 0
scsi_eh_4 1115 2 0 S 15 0
usb-storage 1116 2 0 S 15 0
scsi_eh_5 1129 2 0 S 15 0
usb-storage 1130 2 0 S 15 0
scsi_eh_6 1133 2 0 S 15 0
usb-storage 1134 2 0 S 15 0
rpciod/0 2333 2 0 S 15 0
rpciod/1 2336 2 0 S 15 0
nfsiod 2345 2 0 S 15 0
loop0 2424 2 0 S 0 0
loop1 2708 2 0 S 0 0
loop2 2745 2 0 S 0 0
loop3 2782 2 0 S 0 0
loop4 2819 2 0 S 0 0
loop5 2928 2 0 S 0 0
loop6 2965 2 0 S 0 0
loop7 3002 2 0 S 0 0
loop8 3075 2 0 S 0 0
lockd 15741 2 0 S 15 0
nfsd 15742 2 0 S 15 0
nfsd 15743 2 0 S 15 0
nfsd 15744 2 0 S 15 0
nfsd 15745 2 0 S 15 0
nfsd 15746 2 0 S 15 0
nfsd 15747 2 0 S 15 0
nfsd 15748 2 0 S 15 0
nfsd 15749 2 0 S 15 0
lsmpi-refill 15852 2 0 S 15 0
lsmpi-xmit 15853 2 0 S 15 0
lsmpi-rx 15854 2 0 S 15 0
ddr_err_monitor 16267 2 0 S 15 0
mtdblockd 16292 2 0 S 15 0
scansta 16315 2 0 S 15 0
```


### `show platform process slot`

> **Página:** 872 · **Modo:** Privileged EXEC (#) · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To monitor the software-running process in a given slot, use the show platform software process slotcommand in privileged EXEC or diagnostic mode.

**Syntax:**

```text
show platform software process slot slot monitor [cycles cycles][interval delay][lines
lines-of-output]
```

**Parameters (Syntax Description):**

- `slot` — Specifies the Field Replace U n it( F R U) where the command isr u n.
- `slot` — Slot information.
- `monitor` — Monitor s the running processes.
- `cycles` — Check s the processes m u l t ip l e time s.
- `cycles` — Number of time s the command isr u n d u r in g as in g l e in v o c at i on of the command. The range is from1 to4294967295. The default is5.
- `interval` — Set s delay interval after each command r u n.
- `delay` — Delay be t we e n two s u c c e s s i v e r u n s of the command. The range is from0 to300. The default is3.
- `lines` — Set s then u m be r of output lines that are d is p l a y e d.
- `lines-of-output` — Number of output lines d is p l a y e d. The range is from0 to512.0 d is p l a y s all the lines. Note Then u m be r of lines is d e t e r min e d by the current terminal length.

**Command Default:** No default behavior or values.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXERelease3.1.0S | This command was introduced in are l e as e e a r l i e r than Release3.1.0 S on Cisco AS R1000 S e r i e s Routers. |

**Example:**

The following is a sample output of the show platform software process slot command. Only 23 lines are displayed because the lines-of-output argument is set to 23:

```text
Router# show platform software process slot 0 monitor cycles 3 interval 2 lines 23
top - 19:29:32 up 1 day, 4:46, 0 users, load average: 0.10, 0.11, 0.09
Tasks: 78 total, 4 running, 74 sleeping, 0 stopped, 0 zombie
Cpu(s): 3.0%us, 2.9%sy, 0.0%ni, 93.9%id, 0.0%wa, 0.1%hi, 0.1%si, 0.0
Mem: 449752k total, 328940k used, 120812k free, 6436k buffers
Swap: 0k total, 0k used, 0k free, 155396k cached
PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
7223 root 20 0 124m 46m 23m R 2.0 10.5 11:13.01 mcpcc-lc-ms
8135 root 20 0 123m 46m 25m R 2.0 10.6 35:59.75 mcpcc-lc-ms
1 root 20 0 2156 644 556 S 0.0 0.1 0:02.05 init
2 root 15 -5 0 0 0 S 0.0 0.0 0:00.04 kthreadd
3 root 15 -5 0 0 0 S 0.0 0.0 0:00.00 ksoftirqd/0
4 root RT -5 0 0 0 S 0.0 0.0 0:00.00 watchdog/0
5 root 15 -5 0 0 0 S 0.0 0.0 0:00.04 events/0
6 root 15 -5 0 0 0 S 0.0 0.0 0:00.10 khelper
9 root 15 -5 0 0 0 S 0.0 0.0 0:00.00 netns
55 root 15 -5 0 0 0 S 0.0 0.0 0:00.00 kblockd/0
63 root 15 -5 0 0 0 S 0.0 0.0 0:00.00 ata/0
64 root 15 -5 0 0 0 S 0.0 0.0 0:00.00 ata_aux
70 root 15 -5 0 0 0 S 0.0 0.0 0:00.00 khubd
73 root 15 -5 0 0 0 S 0.0 0.0 0:00.00 kseriod
118 root 20 0 0 0 0 S 0.0 0.0 0:00.00 pdflush
119 root 20 0 0 0 0 S 0.0 0.0 0:00.00 pdflush
top - 19:29:35 up 1 day, 4:46, 0 users, load average: 0.41, 0.17, 0.11
--More--
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| %CPU | CPUUsage |

| Field | Description |
| --- | --- |
| %MEM | MemoryUsage |
| COMMAND | Commandnameorcommandline |
| NI | Nicevalue |
| PID | ProcessID |
| PR | Priority |
| RES | Residentmemorysize(inkb) |
| S | Processstatus |
| SHR | Sharedmemorysize(inkb) |
| TIME+ | Elapsedexecutiontime |
| USER | Username |
| VIRT | Virtualmemorysize(inkb) |


### `show platform software snapshot status`

> **Página:** 874 · **Modo:** Privileged EXEC (#) Diagnostic Mode (diag) · **Default:** No default behavior or values · **Leitura (show/clear/…):** sim

**Description:** To display the status of a bootflash snapshot action, use the show platform software snapshot status command in privilege EXEC mode.

**Syntax:**

```text
show platform software snapshot slot status
```

**Parameters (Syntax Description):**

- `snapshot` — Request s snapshot a c t i on s.
- `slot` — Specifies the hardware slot. Options include: • number--Then u m be r of the S IP slot of the hardware module where the trace level is being set. For in s t an c e, if you w an t e d to specify the SIPin S IP slot2 of the router, enter2 as the number. •f0--The ESPin E S P slot0. •f1--The ESPin E S P slot1 • f p a c t i v e--The a c t i v e ESP. • f p s t and by--The s t and by ESP. •r0--The RPin RPslot0. •r1--The RPin RPslot1. • r p a c t i v e--The a c t i v e RP. • r p s t and by--The s t and by RP.
- `status` — D is p l a y s the status of snapshot o p e r at i on s.

**Command Default:** No default behavior or values

**Command Modes:** Privileged EXEC (#) Diagnostic Mode (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXERelease2.1 | This command was introduced. |

**Usage Guidelines:**

Use the show platform software snapshot status command to view the status of a bootflash snapshot request.

**Example:**

This example shows how to view the status of bootflash snapshot requests on the processor in the RO slot.

```text
router#show platform software snapshot R0 status
```


### `show platform software tech-support`

> **Página:** 875 · **Modo:** Privileged EXEC (#) Diagnostic (diag) · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To display system information or create a technical support information tar file for Cisco Technical Support, use the show platform software tech-supportcommand in privileged EXEC or diagnostic mode.

**Syntax:**

```text
show platform software tech-support [file {bootflash:filename.tgz | fpd:filename.tgz |
harddisk:filename.tgz | obfl:filename.tgz | stby-bootflash:filename.tgz | stby-harddisk:filename.tgz |
stby-obfl:filename.tgz | stby-usb0:filename.tgz | stby-usb1:filename.tgz}]
```

**Parameters (Syntax Description):**

- `file` — ( Optional) Creates a tech n i c a l support information tar file for the specified
- `file` — ( Optional) C r e at e s at e c h n i c a l support information tar file for the specified destination file path.
- `bootflash: filename.tgz` — C r e at e s at e c h n i c a l support information tar file for the bootflash memory filesystem on the a c t i v e RP.
- `f p d: file name. tgz` — C r e at e s at e c h n i c a l support information tar file for the f i e l d-p r o g r a m m a b l e device( F P D) image package on the a c t i v e RP. The information d is p l a y e d is for in t e r n a l debugging p u p o s e s only.
- `h a r d disk: file name. tgz` — C r e at e s at e c h n i c a l support information tar file for the h a r d disk filesystem on the a c t i v e RP.
- `o b f l: file name. tgz` — C r e at e s at e c h n i c a l support information tar file for the filesystem for Onboard Failure Logging( o b f l) files. The information d is p l a y e d is for in t e r n a l debugging p u p o s e s only.
- `s t by-bootflash: file name. tgz` — C r e at e s at e c h n i c a l support information tar file for the bootflash memory filesystem on the s t and by RP. The information d is p l a y e d is for in t e r n a l debugging p u p o s e s only.
- `s t by-h a r d disk: file name. tgz` — C r e at e s at e c h n i c a l support information tar file for the h a r d disk filesystem on the s t and by RP. The information d is p l a y e d is for in t e r n a l debugging p u p o s e s only.
- `s t by-o b f l: file name. tgz` — C r e at e s at e c h n i c a l support information tar file for the Onboard Failure Logging( o b f l) files on the s t and by RP. The information d is p l a y e d is for in t e r n a l debugging p u p o s e s only.
- `s t by-usb0: file name. tgz` — C r e at e s at e c h n i c a l support information tar file for U n i v e r s a l Serial Bus(USB) memory. The information d is p l a y e d is for in t e r n a l debugging p u p o s e s only.
- `s t by-usb1: file name. tgz` — C r e at e s at e c h n i c a l support information tar file for U n i v e r s a l Serial Bus(USB) memory. The information d is p l a y e d is for in t e r n a l debugging p u p o s e s only.

**Command Default:** No default behavior or values.

**Command Modes:** Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers. |

**Usage Guidelines:**

If the file keyword is specified, the specification of the bootflash: or harddisk: keyword and filename is required. The show platform software tech-support command without a destination file path specification returns a large volume of information in a short period of time. You should save the output of the show platform software tech-support command in a log file to send to Cisco Technical Support for analysis.

**Example:**

The following example displays system information for Cisco Technical Support:

```text
Router# show platform software tech-support
---- show version installed -----
Type: provisioning file, Version: unknown
Provisioned on: RP0, Status: active
File: packages.conf.super
Modified: 2007-11-07 15:06:12.212303000 +0000
SHA1 (header): d929d995d5ba2d3dedf67137c3e0e321b1727d7b
SHA1 (calculated): d929d995d5ba2d3dedf67137c3e0e321b1727d7b
SHA1 (external): a16881b6a7e3a5593b63bf211f72b8af9c534063
instance address : 0X890DE9B4
fast failover address : 00000000
cpp interface handle 0
instance address : 0X890DE9B8
fast failover address : 00000000
cpp interface handle 0
instance address : 0X890DE9BC
fast failover address : 00000000
...
```

Note The show platform software tech-support command returns a large volume of information in a short period of time. The example above has been abbreviated for the purposes of this description. The following example creates a technical support information tar file for the boot flash memory file system on the active RP:

```text
Router# show platform software tech-support file bootflash:tech_support_output.tgz
Running tech support command set; please wait...
Creating file 'bootflash:target_support_output.tgz.tgz' ...
File 'bootflash:target_support_output.tgz.tgz' created successfully
```

The following example creates a technical support information tar file for the hard disk file system on the active RP:

```text
Router# show platform software tech-support file harddisk:tech_support_output.tgz
Running tech support command set; please wait...
Creating file 'harddisk:tech_support_ouput.tgz.tgz' ...
File 'harddisk:tech_support_ouput.tgz.tgz' created successfully
```


### `show platform subscriber-group`

> **Página:** 877 · **Modo:** Privileged EXEC (#) · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To display the subscriber group information, use the show platform subscriber-groupcommand in privileged EXEC mode.

**Syntax:**

```text
show platform subscriber-group {vrf-number | all} [detail]
```

**Parameters (Syntax Description):**

- `vrf-number` — VRF id e n t if i c at i on number. D is p l a y s V P N r out in g and for w a r d in g( VRF) information for the specified VRFID.
- `all` — D is p l a y s information about all VRFs.
- `detail` — D is p l a y s detailed information about the subscriber group.

**Command Default:** No default behavior or values.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.1(1)S | This command was introduced. |

**Example:**

This is sample output from the show platform subscriber-group allcommand:

```text
show platform subscriber-group all
Container0[:0] No of access sub-if(s) 1
Vlan 1014 p_cnt 1 Old Vlan 0 ip T
Container2[VRF2:2] No of access sub-if(s) 1
Vlan 1018 p_cnt 1 Old Vlan 0 ip T
```

This is sample output from the show platform subscriber-group 0 detailcommand:

```text
Router#show platform subscriber-group 0 detail
------------------------------------------
VRF[:0] Container0 No of access sub-if(s) 1 Vlan 1014
Access Interfaces:
GigabitEthernet2/10.2
```


### `show platform supervisor`

> **Página:** 878 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display platform supervisor information, use the show platform supervisorcommand in privileged EXEC mode.

**Syntax:**

```text
show platform supervisor mtu slot slot-number port port-number
```

**Parameters (Syntax Description):**

- `mtu` — D is p l a y s supervisor o p e r at in g Maximum T r an m is s i on Unit(MTU).
- `slot slot-number` — D is p l a y s information for the specified slot.
- `port port-number` — D is p l a y s information for the specified port.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRA | This command was introduced. |

**Example:**

The following is sample output from the show platform supervisorcommand. The fields are self-explanatory.

```text
Router# show platform supervisor mtu slot 5 port 1
User configured MTU : 9216
Real Operating MTU : 9236
```


### `show power`

> **Página:** 879 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display information about the power status, use the show powercommand in user EXEC or privileged EXEC mode. | used | details | history ]

**Syntax:**

```text
show power [ available | inline [ interface number | module number ] | redundancy-mode |
status { all | fan-tray fan-tray-number | module slot | power-supply pwr-supply-number } | total
```

**Parameters (Syntax Description):**

- `a v a i l a b l e` — ( Optional) D is p l a y s the a v a i l a b l e system power( m a r g in).
- `inline` — ( Optional) D is p l a y s the in line power status.
- `interface number` — ( Optional) Specifies the interface type; p o s s i b l e v a l id values are e the r n e t, fast e the r n e t, g i g a b it e the r n e t, t e n g i g a b it e the r n e t, n u l l, port-c h an n e l, andvlan. See the“ Usage Guidelines” section for a d d it i on a l information.
- `module number` — D is p l a y s the power status for as p e c if i c module.
- `redundancy-mode` — ( Optional) D is p l a y s the power-sup p l y redundancy mode.
- `status` — ( Optional) D is p l a y s the power status.
- `all` — D is p l a y s all the F R U type s.
- `fan-tray fan-tray-number` — D is p l a y s the power status for the f an t r a y.
- `module slot` — D is p l a y s the power status for as p e c if i c module.
- `power-supply pwr-supply-number` — D is p l a y s the power status for as p e c if i c power sup p l y; v a l id values are 1and2
- `total` — ( Optional) D is p l a y s the to t a l power that is a v a i l a b l e from the power sup p l i e s.
- `used` — ( Optional) D is p l a y s the to t a l power that is b u d get e d for power e d-on items.
- `details` — ( Optional) D is p l a y s the power c on s u m p t i on detail s for each c o m p one n t.
- `history` — ( Optional) D is p l a y s the power c on s u m p t i on history for the device.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17a)SX1 | The output was changed to include the to t a l system-power information. |
| 12.2(17b)SXA | This command was changed to include information about the in line power status for as p e c if i c module. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release 12.2(17d)SXB. |
| 12.2(18)SXF | The output was changed to include information about the h i g h-capacity power sup p l i e s. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXE 17.16.1a | The keywords usage and detail were introduced for the following platform s: •Cisco Catalyst8200 S e r i e s Edge Platform s •Cisco Catalyst8300 S e r i e s Edge Platform s •Cisco Catalyst8500 and8500 L S e r i e s Edge Platform s |

**Usage Guidelines:**

The interface-number argument designates the module and port number. Valid values for interface-number depend on the specified interface type and the chassis and module that are used. For example, if you specify a Gigabit Ethernet interface and have a 48-port 10/100BASE-T Ethernet module that is installed in a 13-slot chassis, valid values for the module number are from 1 to 13 and valid values for the port number are from 1 to 48. Valid values for vlan-id are from 1 to 4094. The Inline power field in the show poweroutput displays the inline power that is consumed by the modules. For example, this example shows that module 9 has consumed 0.300 A of inline power:

```text
Inline power # current
module 9 0.300A
```

**Example:**

This example shows how to display the available system power:

```text
Router>
show power
available
system power available = 20.470A
Router>
```

This example shows how to display power-supply redundancy mode:

```text
show power
redundancy-mode
system power redundancy mode = redundant
```

This command shows how to display the system-power status:

```text
Router> show power
system power redundancy mode = combined
system power total = 3984.12 Watts (94.86 Amps @ 42V)
system power used = 1104.18 Watts (26.29 Amps @ 42V)
system power available = 2879.94 Watts (68.57 Amps @ 42V)
Power-Capacity PS-Fan Output Oper
PS Type Watts A @42V Status Status State
---- ------------------ ------- ------ ------ ------ -----
1 WS-CAC-3000W 2830.80 67.40 OK OK on
2 WS-CAC-1300W 1153.32 27.46 OK OK on
Note: PS2 capacity is limited to 2940.00 Watts (70.00 Amps @ 42V)
when PS1 is not present
Pwr-Allocated Oper
Fan Type Watts A @42V State
---- ------------------ ------- ------ -----
1 FAN-MOD-9 241.50 5.75 OK
2 241.50 5.75 failed
Pwr-Requested Pwr-Allocated Admin Oper
Slot Card-Type Watts A @42V Watts A @42V State State
---- ------------------ ------- ------ ------- ------ ----- -----
1 WS-X6K-SUP2-2GE 145.32 3.46 145.32 3.46 on on
2 - - 145.32 3.46 - -
3 WS-X6516-GBIC 118.02 2.81 118.02 2.81 on on
5 WS-C6500-SFM 117.18 2.79 117.18 2.79 on on
7 WS-X6516A-GBIC 214.20 5.10 - - on off (insuff cooling capacity)
8 WS-X6516-GE-TX 178.50 4.25 178.50 4.25 on on
9 WS-X6816-GBIC 733.98 17.48 - - on off (connector rating exceeded)
Router>
```

This example shows how to display the power status for all FRU types:

```text
show power
status all
FRU-type # current admin state oper
power-supply 1 27.460A on on
module 1 4.300A on on
module 2 4.300A - - (reserved)
module 5 2.690A on on
```

This example shows how to display the power status for a specific module:

```text
show power
status module 1
FRU-type # current admin state oper
module 1 -4.300A on on
```

This example shows how to display the power status for a specific power supply:

```text
show power
status power-supply 1
FRU-type # current admin state oper
power-supply 1 27.460A on on
```

This example displays information about the high-capacity power supplies:

```text
show power
status power-supply 2
Power-Capacity PS-Fan Output Oper
PS Type Watts A @42V Status Status State
---- ------------------ ------- ------ ------ ------ -----
1 WS-CAC-6000W 2672.04 63.62 OK OK on
2 WS-CAC-9000W-E 2773.68 66.04 OK OK on
```

This example shows how to display the total power that is available from the power supplies:

```text
show power
total
system power total = 27.460A
```

This example shows how to display the total power that is budgeted for powered-on items:

```text
show power
used
system power used = -6.990A
```

This command shows how to display the inline power status on the interfaces:

```text
show power
inline
Interface Admin Oper Power ( mWatt ) Device
-------------------- ----- ---------- --------------- -----------
FastEthernet9/1 auto on 6300 Cisco 6500 IP Phone
FastEthernet9/2 auto on 6300 Cisco 6500 IP Phone
. <Output truncated>
```

This command shows how to display the inline power status for a specific module:

```text
Router
# show power
inline mod 7
Interface Admin Oper Power Device Class
(Watts)
---------- ----- ---------- ------- -------------- -----------
Gi7/1 auto on 6.3 Cisco IP Phone 7960 n/a
Gi7/2 static power-deny 0 Ieee PD 3
. <Output truncated>
```

This example shows how to display power usage details:

```text
Router# show power detail
Component Power:
Slot Type Instant Peak Budget Unit Direction
-------- ------------------ -------- -------- -------- -------- --------
P0 PWR-CC1-650WAC 143 152 142 Watts Input
P0 PWR-CC1-650WAC 129 136 126 Watts Output
P1 PWR-CC1-1000WAC 22 26 19 Watts Input
P1 PWR-CC1-1000WAC 3 4 3 Watts Output
P2 C8300-FAN-2R 7 12 7 Watts
POE0 PWR-CC1-MOD-POE 75 80 75 Watts Input
POE1 PWR-POE-4450 96 96 96 Watts Input
0/1 NIM-ES2-8-P 4 4 4 Watts
0/2 NIMX-M-1TE-SFP 5 5 5 Watts
R0 C8300-2N2S-4T2X 43 49 39 Watts
System Power:
Instant Peak Budget Unit
-------- -------- -------- --------
165 176 162 Watts
System Energy:
Meter Reset Time Meter Update Time System Energy in WattSec
----------------------- ----------------------- -----------------------------
2024-08-22 23:13:12 UTC 2024-08-23 21:58:12 UTC 13665000
Metered System Energy:
Meter Update Hourly Metered Metered Energy in WattSec (5min Buckets)
Time Value (WattSec)
----------------------- ----------------
------------------------------------------------------------------------
2024-08-23 21:58:12 UTC 602100
49800-50100-50100-50100-50100-50400-50400-50700-50100-50100-50100-50100
```

This example shows how to display power usage history:

```text
Router# show power history
170 **********************************************************
160 **********************************************************
150 **********************************************************
140 **********************************************************
130 **********************************************************
120 **********************************************************
110 **********************************************************
100 **********************************************************
90 **********************************************************
80 **********************************************************
70 **********************************************************
60 **********************************************************
50 **********************************************************
40 **********************************************************
30 **********************************************************
20 **********************************************************
10 **********************************************************
0....5....1....1....2....2....3....3....4....4....5....5....6
0 5 0 5 0 5 0 5 0 5 0
Power(Watts) per minute (last 60 minutes)
* = maximum Power(Watts) # = average Power(Watts)
170 ##############
160 ##############
150 ##############
140 ##############
130 ##############
120 ##############
110 ##############
100 ##############
90 ##############
80 ##############
70 ##############
60 ##############
50 ##############
40 ##############
30 ##############
20 ##############
10 ##############
0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
0 5 0 5 0 5 0 5 0 5 0 5 0
Power(Watts) per hour (last 72 hours)
* = maximum Power(Watts) # = average Power(Watts)
```


### `show processes`

> **Página:** 884 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the active Cisco IOS, Cisco IOS XE, or the Cisco IOS Software Modularity POSIX-style processes, use the show processes command in user EXEC or privileged EXEC mode. Cisco IOS Software Cisco IOS Software Modularity Images and Cisco Catalyst 4500e Series Switches Running Cisco IOS XE Software

**Syntax:**

```text
show processes [heapcheck | historyprocess-id | timercheck]
show processes
```

**Parameters (Syntax Description):**

- `heapcheck` — ( Optional) D is p l a y s the scheduler heapcheck configuration.
- `history` — ( Optional) For Cisco IOS processes only. D is p l a y s the process history in an or d e r e d format.
- `process-id` — ( Optional) For Cisco IOS processes only. An integer that specifies the process for which memory and CPU u t i l i z at i on data will be return e d.
- `timercheck` — ( Optional) For Cisco IOS processes only. D is p l a y s the processes configure d for at i m e r check.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(2)T | This command was modified. The history keyword was added. |
| 12.3(2)T | This command was modified. The process-ida r g u m e n t was added. |
| 12.2(18)SXF4 | This command was modified. The syntax was modified to support Cisco IOS Software M o d u l a r it y image s. |
| 12.3(14)T | This command was modified. The timercheck keyword was added. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1. |
| CiscoIOSXERelease3.1.0.SG | This command was introduced on the Cisco Catalyst4500 e Series Switch e s. |
| 15.1(2)S | This command was integrated into Cisco IOS Release15.1(2) S. |
| 15.2(1)T | The heapcheck keyword was added. |

**Usage Guidelines:**

Cisco IOS Software Modularity Although no optional keywords or arguments are supported for the base show processes command when a Software Modularity image is running, more details about processes are displayed using the show processes cpu, show processes detailed, show processes kernel,and show processes memory commands. Cisco IOS Software The following example shows how to display the scheduler heapcheck configuration using the show process heapcheck command

```text
Router# show processes heapcheck
Scheduler Heapcheck Enabled : N
Scheduler Heapcheck Active : N
```

The following is sample output from the show processes command:

```text
Router# show processes
CPU utilization for five seconds: 21%/0%; one minute: 2%; five minutes: 2%
PID QTy PC Runtime (ms) Invoked uSecs Stacks TTY Process
1 Cwe 606E9FCC 0 1 0 5600/6000 0 Chunk Manager
2 Csp 607180F0 0 121055 0 2608/3000 0 Load Meter
3 M* 0 8 90 88 9772/12000 0 Exec
4 Mwe 619CB674 0 1 023512/24000 0 EDDRI_MAIN
5 Lst 606F6AA4 82064 61496 1334 5668/6000 0 Check heaps
6 Cwe 606FD444 0 127 0 5588/6000 0 Pool Manager
7 Lwe 6060B364 0 1 0 5764/6000 0 AAA_SERVER_DEADT
8 Mst 6063212C 0 2 0 5564/6000 0 Timers
9 Mwe 600109D4 0 2 0 5560/6000 0 Serial Backgroun
10 Mwe 60234848 0 2 0 5564/6000 0 ATM Idle Timer
11 Mwe 602B75F0 0 2 0 8564/9000 0 ATM AutoVC Perio
12 Mwe 602B7054 0 2 0 5560/6000 0 ATM VC Auto Crea
13 Mwe 606068B8 0 2 0 5552/6000 0 AAA high-capacit
14 Msi 607BABA4 251264 605013 415 5628/6000 0 EnvMon
15 Mwe 607BFF8C 0 1 0 8600/9000 0 OIR Handler
16 Mwe 607D407C 0 10089 0 5676/6000 0 IPC Dynamic Cach
17 Mwe 607CD03C 0 1 0 5632/6000 0 IPC Zone Manager
18 Mwe 607CCD80 0 605014 0 5708/6000 0 IPC Periodic Tim
19 Mwe 607CCD24 0 605014 0 5704/6000 0 IPC Deferred Por
20 Mwe 607CCE2C 0 1 0 5596/6000 0 IPC Seat Manager
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| CPUutilizationforfive seconds | CPUutilizationforthelast5seconds.Thesecondnumberindicatesthe percentageofCPUtimespentattheinterruptlevel. |
| oneminute | CPUutilizationforthelastminute. |
| fiveminutes | CPUutilizationforthelast5minutes. |
| PID | ProcessID. |
| Q | Processqueuepriority.Possiblevalues:C(critical),H(high),M(medium), andL(low). |
| Ty | Schedulertest.Possiblevalues: •*(currentlyrunning) •E(waitingforanevent) •S(readytorun,voluntarilyrelinquishedprocessor) •rd(readytorun,wakeupconditionshaveoccurred) •we(waitingforanevent) •sa(sleepinguntilanabsolutetime) •si(sleepingforatimeinterval) •sp(sleepingforatimeintervalasanalternatecall •st(sleepinguntilatimerexpires) •hg(hung:theprocesswillneverexecuteagain) •xx(dead:theprocesshasterminated,buthasnotyetbeendeleted) |
| PC | Currentprogramcounter. |
| Runtime(ms) | CPUtimethattheprocesshasused(inmilliseconds). |
| Invoked | Numberoftimesthattheprocesshasbeeninvoked. |
| uSecs | MicrosecondsofCPUtimeforeachprocessinvocation. |
| Stacks | Lowwatermark/Totalstackspaceavailable(inbytes). |

| Field | Description |
| --- | --- |
| TTY | Terminalthatcontrolstheprocess. |
| Process | Nameoftheprocess. |

Note Because platforms have a 4- to 8- millisecond clock resolution, run times are considered reliable only after a large number of invocations or a reasonable, measured run time. For a list of process descriptions, see http://www.cisco.com/en/US/products/sw/iosswrel/ps1828/products_tech_note09186a00800a65d0.shtml. The following is sample output from the show processes history command:

```text
Router# show processes history
PID Exectime(ms) Caller PC Process Name
3 12 0x0 Exec
16 0 0x603F4DEC GraphIt
21 0 0x603CFEF4 TTY Background
22 0 0x6042FD7C Per-Second Jobs
67 0 0x6015CD38 SMT input
39 0 0x60178804 FBM Timer
16 0 0x603F4DEC GraphIt
21 0 0x603CFEF4 TTY Background
22 0 0x6042FD7C Per-Second Jobs
16 0 0x603F4DEC GraphIt
21 0 0x603CFEF4 TTY Background
22 0 0x6042FD7C Per-Second Jobs
67 0 0x6015CD38 SMT input
39 0 0x60178804 FBM Timer
24 0 0x60425070 Compute load avgs
11 0 0x605210A8 ARP Input
69 0 0x605FDAF4 DHCPD Database
69 0 0x605FD568 DHCPD Database
51 0 0x60670B3C IP Cache Ager
69 0 0x605FD568 DHCPD Database
36 0 0x606E96DC SSS Test Client
69 0 0x605FD568 DHCPD Database
--More--
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| PID | ProcessID. |
| Exectime(ms) | Executiontime(inmilliseconds)ofthemostrecentrunorthetotalexecutiontimeofthe mostrecentconsecutiveruns. |
| CallerPC | Currentprogramcounterofthisprocessbeforeitwassuspended. |
| ProcessName | Nameoftheprocess. |

The following is sample output from the show processes process-id command:

```text
show processes 6
Process ID 6 [Pool Manager], TTY 0
Memory usage [in bytes]
Holding: 921148, Maximum: 940024, Allocated: 84431264, Freed: 99432136
Getbufs: 0, Retbufs: 0, Stack: 12345/67890
CPU usage
PC: 0x60887600, Invoked: 188, Giveups: 100, uSec: 24
5Sec: 3.03%, 1Min: 2.98%, 5Min: 1.55%, Average: 0.58%,
Age: 662314 msec, Runtime: 3841 msec
State: Running, Priority: Normal
```

The table below describes the fields shown in the display.

| Field | Description |
| --- | --- |
| ProcessID | ProcessIDnumberandprocessname. |
| TTY | Terminalthatcontrolstheprocess. |
| Memoryusage[inbytes] | Thissectioncontainsfieldsthatshowthememoryusedbythespecifiedprocess. |
| Holding | Amountofmemorycurrentlyallocatedtotheprocess. |
| Maximum | Maximumamountofmemoryallocatedtotheprocesssinceitsinvocation. |
| Allocated | Bytesofmemoryallocatedbytheprocess. |
| Freed | Bytesofmemoryfreedbytheprocess. |
| Getbufs | Numberoftimesthattheprocesshasrequestedapacketbuffer. |
| Retbufs | Numberoftimesthattheprocesshasrelinquishedapacketbuffer. |
| Stack | Lowwatermark/Totalstackspaceavailable(inbytes). |
| CPUusage | ThissectioncontainsfieldsthatshowtheCPUresourcesusedbythespecified process. |
| PC | Currentprogramcounterofthisprocessbeforeitwassuspended. |
| Invoked | Numberoftimesthattheprocessexecutedsinceitsinvocation. |
| Giveups | NumberoftimesthattheprocessvoluntarilygaveuptheCPU. |
| uSec | MicrosecondsofCPUtimeforeachprocessinvocation. |
| 5Sec | CPUutilizationbyprocessinthelastfiveseconds. |
| 1Min | CPUutilizationbyprocessinthelastminute. |
| 5Min | CPUutilizationbyprocessinthelastfiveminutes. |
| Average | TheaverageamountofCPUutilizationbytheprocesssinceitsinvocation. |

| Field | Description |
| --- | --- |
| Age | Millisecondssincetheprocesswasinvoked. |
| Runtime | CPUtimethattheprocesshasused(inmilliseconds). |
| State | Currentstateoftheprocess.Possiblevalues:Running,WaitingforEvent,Sleeping (MgdTimer),Sleeping(Periodic),Ready,Idle,Dead. |
| Priority | Thepriorityoftheprocess.Possiblevalues:Low,Normal,High. |

Cisco IOS Software Modularity The following is sample output from the show processescommand when a Cisco IOS Software Modularity image is running:

```text
Router# show processes
Total CPU utilization for 5 seconds: 99.7%; 1 minute: 98.9%; 5 minutes: 86.5%
PID TID Prio STATE Blocked Stack CPU Name
1 1 0 Ready 0 (128K) 2m28s procnto-cisco
1 2 63 Receive 1 0 (128K) 0.000 procnto-cisco
1 3 10 Receive 1 0 (128K) 0.000 procnto-cisco
1 4 11 Receive 1 0 (128K) 1.848 procnto-cisco
1 5 63 Receive 1 0 (128K) 0.000 procnto-cisco
1 6 63 Receive 1 0 (128K) 0.000 procnto-cisco
12290 1 10 Receive 1 12288(128K) 0.080 chkptd.proc
12290 2 10 Receive 8 12288(128K) 0.000 chkptd.proc
3 1 15 Condvar 1027388 12288(128K) 0.016 qdelogger
3 2 15 Receive 1 12288(128K) 0.004 qdelogger
3 3 16 Condvar 1040024 12288(128K) 0.004 qdelogger
4 1 10 Receive 1 4096 (128K) 0.016 devc-pty
6 1 62 Receive 1 8192 (128K) 0.256 devc-ser2681
6 2 63 Intr 8192 (128K) 0.663 devc-ser2681
7 1 10 Receive 1 32768(128K) 0.080 dumper.proc
7 2 10 Receive 1 32768(128K) 0.008 dumper.proc
7 3 10 Receive 1 32768(128K) 0.000 dumper.proc
7 4 10 Receive 1 32768(128K) 0.020 dumper.proc
7 5 10 Receive 1 32768(128K) 0.008 dumper.proc
4104 2 10 Receive 1 12288(128K) 0.000 pipe
4104 3 10 Receive 1 12288(128K) 0.000 pipe
--More--
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| PID | ProcessID. |
| TID | TaskID. |
| Prio | Processpriority. |
| STATE | Currentstateoftheprocess. |
| Blocked | Thread(withgivenprocessID)thatiscurrentlyblockedbytheprocess. |

| Field | Description |
| --- | --- |
| Stack | Size,inkilobytes,ofthememorystack. |
| CPU | CPUtime,inminutesandseconds,usedbytheprocess. |
| Name | Processname. |

Cisco Catalyst 4500e Series Switches Running Cisco IOS XE software The following is sample output from the show processes command:

```text
Switch# show processes
CPU utilization for five seconds: 1%; one minute: 4%; five minutes: 3%
PID TID Runtime(ms) Invoked uSecs Stacks Process
1 935 596 156971 84/8192 init
2 0 79 10405 0/8192 kthreadd
3 12 2206 5578 0/8192 migration/0
4 12 772 15601 0/8192 ksoftirqd/0
5 6 1089 6357 0/8192 migration/1
6 14 877 16484 0/8192 ksoftirqd/1
7 15 374 42475 0/8192 events/0
8 9 333 27531 0/8192 events/1
9 5 637 9070 0/8192 khelper
61 28 45 628533 0/8192 kblockd/0
62 80 175 461994 0/8192 kblockd/1
75 0 21 1238 0/8192 khubd
78 0 23 652 0/8192 kseriod
83 7 26 271115 0/8192 kmmcd
120 0 25 320 0/8192 pdflush
121 12 68 190382 0/8192 pdflush
122 0 29 172 0/8192 kswapd0
123 0 31 161 0/8192 aio/0
124 0 33 121 0/8192 aio/1
291 0 35 142 0/8192 kpsmoused
309 0 37 135 0/8192 rpciod/0
310 0 39 128 0/8192 rpciod/1
354 71 425 167583 84/8192 udevd
700 117 3257 35991 0/8192 loop1
716 0 55 1145 0/8192 loop2
732 115 2336 49574 0/8192 loop3
2203 86 627 138015 84/8192 dbus-daemon
2539 0 432 1974 84/8192 portmap
2545 0 434 2011 84/8192 portmap
2588 1 450 2384 84/8192 sshd
2602 2 444 6677 84/8192 xinetd
2606 1 444 3191 84/8192 xinetd
3757 0 71 70 84/8192 vsi work/0
--More--
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| CPUutilizationforfiveseconds | CPUutilizationforthelast5seconds.The3%indicatesthepercentageof CPUtimespentattheinterruptlevel. |
| oneminute | CPUutilizationforthelastminute. |
| fiveminutes | CPUutilizationforthelast5minutes. |
| PID | ProcessID. |
| TID | ThreadID. |
| Runtime(ms) | CPUtimethattheprocesshasused(inmilliseconds). |
| Invoked | Numberoftimesthattheprocesshasbeeninvoked. |
| uSecs | MicrosecondsofCPUtimeforeachprocessinvocation. |
| Stacks | Size,inkilobytes,ofthememorystack. |
| Process | Processname. |


### `show processes cpu`

> **Página:** 891 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display detailed CPU utilization statistics (CPU use per process) when Cisco IOS, Cisco IOS XE, or Cisco IOS Software Modularity images are running, use the show processes cpucommand in user EXEC or privileged EXEC mode. Cisco IOS Software Cisco IOS Software Modularity Cisco Catalyst 4500e Series Switches running IOS XE software | sorted]

**Syntax:**

```text
show processes cpu [history [table] | sorted [1min | 5min | 5sec]]
show processes cpu [detailed [process-idprocess-name] | history]
show processes cpu [detailed process [process-idprocess-name] | history [detailed | summary | table]
```

**Parameters (Syntax Description):**

- `history` — ( Optional) D is p l a y s CPU history in a g r ap h format.
- `table` — ( Optional) D is p l a y s CPU history in at a b l e format.
- `summary` — ( Optional) D is p l a y s as u m m a r y of the CPU history.
- `sorted` — ( Optional) D is p l a y s CPU u t i l i z at i on s or t e d by percentage.
- `1min` — ( Optional) S or t s CPU u t i l i z at i on b as e do n1 min u t e u t i l i z at i on.
- `5min` — ( Optional) S or t s CPU u t i l i z at i on b as e do n5 min u t e s u t i l i z at i on.
- `5sec` — ( Optional) S or t s CPU u t i l i z at i on b as e do n5 s e c on d s u t i l i z at i on.
- `detailed` — ( Optional) D is p l a y s more detailed information about Cisco IOS processes( not for POSIX processes).
- `process-id` — ( Optional) Process id e n t if i e r.
- `process-name` — ( Optional) Process name.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0 | This command was introduced. |
| 12.2(2)T | This command was modified. The history keyword was added. |
| 12.3(8) | This command was e n h an c e d to d is p l a y Address R e s o l u t i on P r o to c o l ( A R P) output. |
| 12.3(14)T | This command was e n h an c e d to d is p l a y A R P output. |
| 12.2(18)SXF4 | This command was e n h an c e d to support Cisco IOS Software M o d u l a r it y images. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B. |
| 12.2(33)SCB3 | This command was integrated into Cisco IOS Release12.2(33) S C B3. Support was added for Ciscou B R10012 and u B R7200 routers. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1. |
| 15.0(1)M | This command was modified. The output was modified to d is p l a y the CPU time in m i c r o s e c on d s that the process has used. |
| CiscoIOSXERelease3.1.0.SG | This command was introduced on the Cisco Catalyst4500 e Serfies Switch e s. |

**Usage Guidelines:**

Cisco IOS Software If you use the optional history keyword, three graphs are displayed for Cisco IOS images: • CPU utilization for the last 60 seconds • CPU utilization for the last 60 minutes • CPU utilization for the last 72 hours Maximum usage is measured and recorded every second; average usage is calculated on periods of more than one second. Consistently high CPU utilization over an extended period indicates a problem. Use the show processes cpu command to troubleshoot. Also, you can use the output of this command in the Cisco Output Interpreter tool to display potential issues and fixes. Output Interpreter is available to registered users of Cisco.com who are logged in and have Java Script enabled. For a list of system processes, go to http://www.cisco.com/en/US/products/sw/iosswrel/ps1828/products_tech_note09186a00800a65d0.shtml. Cisco IOS Software Modularity Cisco IOS Software Modularity images display only one graph that shows the CPU utilization for the last 60 minutes. The horizontal axis shows times (for example, 0, 5, 10, 15 minutes), and the vertical axis shows total percentage of CPU utilization (0 to 100 percent). Cisco IOS Software The following is sample output from the show processes cpu command without keywords:

```text
Router# show processes cpu
CPU utilization for five seconds: 0%/0%; one minute: 0%; five minutes: 0%
PID Runtime(uS) Invoked uSecs 5Sec 1Min 5Min TTY Process
1 4000 67 59 0.00% 0.00% 0.00% 0 Chunk Manager
2 4000 962255 0 0.00% 0.00% 0.00% 0 Load Meter
3 0 1 0 0.00% 0.00% 0.00% 0 cpf_process_tp
4 0 1 0 0.00% 0.00% 0.00% 0 EDDRI_MAIN
5 586520704 732013 6668 0.00% 0.11% 0.08% 0 Check heaps
6 4000 991 4 0.00% 0.00% 0.00% 0 Pool Manager
7 0 1 0 0.00% 0.00% 0.00% 0 DiscardQ Backg
8 0 2 0 0.00% 0.00% 0.00% 0 Timers
9 0 2 0 0.00% 0.00% 0.00% 0 ATM AutoVC Per
10 0 2 0 0.00% 0.00% 0.00% 0 ATM VC Auto Cr
11 2154956000 4809201 448 0.00% 0.03% 0.03% 0 EnvMon
PID Runtime(uS) Invoked uSecs 5Sec 1Min 5Min TTY Process
12 0 1 0 0.00% 0.00% 0.00% 0 OIR Handler
13 0 1 0 0.00% 0.00% 0.00% 0 Crash writer
14 0 1 0 0.00% 0.00% 0.00% 0 IPC Process le
15 0 80189 0 0.00% 0.00% 0.00% 0 IPC Dynamic Ca
16 0 1 0 0.00% 0.00% 0.00% 0 IPC Zone Manag
17 0 962246 0 0.00% 0.00% 0.00% 0 IPC Service No
18 0 4698177 0 0.00% 0.00% 0.00% 0 IPC Periodic T
19 0 4698177 0 0.00% 0.00% 0.00% 0 IPC Deferred P
20 0 1 0 0.00% 0.00% 0.00% 0 IPC Seat Manag
21 0 1 0 0.00% 0.00% 0.00% 0 IPC Seat Contr
22 0 962246 0 0.00% 0.00% 0.00% 0 IPC Loadometer
<snip>
```

The following is sample output of the one-hour portion of the output. The Y-axis of the graph is the CPU utilization. The X-axis of the graph is the increment within the time period displayed in the graph. This example shows the individual minutes during the previous hour. The most recent measurement is on the left of the X-axis.

```text
Router# show processes cpu history!--- One minute output omitted
80 * * * * * * * *
70 * * ***** * ** ***** *** **** ****** * ******* * *
60 #***##*##*#***#####*#*###*****#*###*#*#*##*#*##*#*##*****#
50 ##########################################################
40 ##########################################################
30 ##########################################################
20 ##########################################################
10 ##########################################################
0....5....1....1....2....2....3....3....4....4....5....5....
0 5 0 5 0 5 0 5 0 5
CPU% per minute (last 60 minutes)
* = maximum CPU% # = average CPU%!--- 72-hour output omitted
```

The top two rows, read vertically, display the highest percentage of CPU utilization recorded during the time increment. In this example, the CPU utilization for the last minute recorded is 66 percent. The device may have reached 66 percent only once during that minute, or it may have reached 66 percent multiple times. The device records only the peak reached during the time increment and the average over the course of that increment. The following is sample output from the show processes cpu command on a Cisco uBR10012 router:

```text
Router# show processes cpu
CPU utilization for five seconds: 2%/0%; one minute: 2%; five minutes: 2%
PID Runtime(us) Invoked uSecs 5Sec 1Min 5Min TTY Process
1 8 471 16 0.00% 0.00% 0.00% 0 Chunk Manager
2 4 472 8 0.00% 0.00% 0.00% 0 Load Meter
3 0 1 0 0.00% 0.00% 0.00% 0 IPC 0x50000 Vers
4 0 10 0 0.00% 0.00% 0.00% 0 C10K Card Event
5 0 65 0 0.00% 0.00% 0.00% 0 Retransmission o
6 0 5 0 0.00% 0.00% 0.00% 0 IPC ISSU Dispatc
7 5112 472 10830 0.63% 0.18% 0.18% 0 Check heaps
8 0 1 0 0.00% 0.00% 0.00% 0 Pool Manager
9 0 2 0 0.00% 0.00% 0.00% 0 Timers
10 0 2 0 0.00% 0.00% 0.00% 0 Serial Backgroun
11 0 786 0 0.00% 0.00% 0.00% 0 WBCMTS process
12 0 1 0 0.00% 0.00% 0.00% 0 AAA_SERVER_DEADT
13 0 1 0 0.00% 0.00% 0.00% 0 Policy Manager
14 0 1 0 0.00% 0.00% 0.00% 0 Crash writer
15 0 1 0 0.00% 0.00% 0.00% 0 RO Notify Timers
16 0 1 0 0.00% 0.00% 0.00% 0 RMI RM Notify Wa
17 0 2364 0 0.00% 0.00% 0.00% 0 Facility Alarm
18 0 41 0 0.00% 0.00% 0.00% 0 IPC Dynamic Cach
```

The following is sample output from the show processes cpu command that shows an ARP probe process:

```text
Router# show processes cpu | include ARP
17 38140 389690 97 0.00% 0.00% 0.00% 0 ARP Input
36 0 1 0 0.00% 0.00% 0.00% 0 IP ARP Probe
40 0 1 0 0.00% 0.00% 0.00% 0 ATM ARP INPUT
80 0 1 0 0.00% 0.00% 0.00% 0 RARP Input
114 0 1 0 0.00% 0.00% 0.00% 0 FR ARP
```

The following is sample output from the show processes cpu command on a Cisco 4400 Series ISR: The table below describes the fields shown in the output.

| Field | Description |
| --- | --- |
| CPUutilizationforfiveseconds | CPUutilizationforthelast5seconds.Thesecondnumberindicatesthe percentofCPUtimespentattheinterruptlevel. |
| oneminutes | CPUutilizationforthelastminute. |
| fiveminutess | CPUutilizationforthelast5minutes. |
| PID | ProcessID. |
| Runtime(us) | CPUtimethattheprocesshasused(inmicroseconds). |
| Invoked | Numberoftimesthattheprocesshasbeeninvoked. |
| uSecs | MicrosecondsofCPUtimeforeachprocessinvocation. |
| 5Sec | CPUutilizationbytaskinthelast5seconds. |
| 1Min | CPUutilizationbytaskinthelastminute. |
| 5Min | CPUutilizationbytaskinthelast5minutes. |
| TTY | Terminalthatcontrolstheprocess. |
| Process | Nameoftheprocess. |

Note Because platforms have a 4- to 8-microsecond clock resolution, run times are considered reliable only after several invocations or a reasonable, measured run time. Cisco IOS Software Modularity The following is sample output from the show processes cpu command when a Software Modularity image is running:

```text
Router# show processes cpu
Total CPU utilization for 5 seconds: 99.6%; 1 minute: 98.5%; 5 minutes: 85.3%
PID 5Sec 1Min 5Min Process
1 0.0% 0.1% 0.8% kernel
3 0.0% 0.0% 0.0% qdelogger
4 0.0% 0.0% 0.0% devc-pty
6 0.7% 0.2% 0.1% devc-ser2681
7 0.0% 0.0% 0.0% dumper.proc
4104 0.0% 0.0% 0.0% pipe
8201 0.0% 0.0% 0.0% mqueue
8202 0.0% 0.0% 0.0% fsdev.proc
8203 0.0% 0.0% 0.0% flashfs_hes_slot1.proc
8204 0.0% 0.0% 0.0% flashfs_hes_slot0.proc
8205 0.0% 0.0% 0.0% flashfs_hes_bootflash.proc
8206 0.0% 0.0% 0.0% dfs_disk2.proc
8207 0.0% 0.0% 0.0% dfs_disk1.proc
8208 0.0% 0.0% 0.0% dfs_disk0.proc
8209 0.0% 0.0% 0.0% ldcache.proc
8210 0.0% 0.0% 0.0% watchdog.proc
8211 0.0% 0.0% 0.0% syslogd.proc
8212 0.0% 0.0% 0.0% name_svr.proc
8213 0.0% 0.1% 0.0% wdsysmon.proc
--More--
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| TotalCPUutilizationforfive seconds | TotalCPUutilizationforthelast5seconds.Thesecondnumberindicates thepercentofCPUtimespentattheinterruptlevel. |
| 1minute | CPUutilizationforthelastminute. |
| 5minutes | CPUutilizationforthelast5minutes. |
| PID | ProcessID. |
| 5Sec | PercentageofCPUtimespentattheinterruptlevelforthisprocessduring thelastfiveseconds. |
| 1Min | PercentageofCPUtimespentattheinterruptlevelforthisprocessduring thelastminute. |
| 5Min | PercentageofCPUtimespentattheinterruptlevelforthisprocessduring thelastfiveminutes. |
| Process | Processname. |

The following is partial sample output from the show processes cpucommand with the detailedkeyword when a Software Modularity image is running:

```text
Router# show processes cpu detailed
Total CPU utilization for 5 seconds: 99.6%; 1 minute: 99.3%; 5 minutes: 88.6%
PID/TID 5Sec 1Min 5Min Process Prio STATE CPU
1 0.0% 0.7% 0.7% kernel 8.900
1 0.4% 0.7% 11.4% [idle thread] 0 Ready 2m28s
2 0.0% 0.0% 0.0% 63 Receive 0.000
3 0.0% 0.0% 0.0% 10 Receive 0.000
4 0.0% 0.0% 0.1% 11 Receive 1.848
5 0.0% 0.0% 0.0% 63 Receive 0.000
PID/TID 5Sec 1Min 5Min Process Prio STATE CPU
8214 0.0% 0.0% 0.0% sysmgr.proc 0.216
1 0.0% 0.0% 0.0% 10 Receive 0.132
2 0.0% 0.0% 0.0% 10 Sigwaitin 0.000
3 0.0% 0.0% 0.0% 10 Receive 0.004
4 0.0% 0.0% 0.0% 10 Receive 0.000
5 0.0% 0.0% 0.0% 10 Receive 0.000
6 0.0% 0.0% 0.0% 10 Receive 0.004
7 0.0% 0.0% 0.0% 10 Receive 0.000
8 0.0% 0.0% 0.0% 10 Receive 0.000
9 0.0% 0.0% 0.0% 10 Receive 0.000
10 0.0% 0.0% 0.0% 10 Receive 0.000
11 0.0% 0.0% 0.0% 10 Receive 0.000
12 0.0% 0.0% 0.0% 10 Receive 0.000
13 0.0% 0.0% 0.0% 10 Receive 0.028
14 0.0% 0.0% 0.0% 10 Receive 0.040
15 0.0% 0.0% 0.0% 10 Receive 0.000
16 0.0% 0.0% 0.0% 10 Receive 0.000
17 0.0% 0.0% 0.0% 10 Receive 0.004
18 0.0% 0.0% 0.0% 10 Receive 0.000
19 0.0% 0.0% 0.0% 10 Receive 0.000
20 0.0% 0.0% 0.0% 10 Receive 0.000
21 0.0% 0.0% 0.0% 10 Receive 0.004
22 0.0% 0.0% 0.0% 10 Receive 0.000
PID/TID 5Sec 1Min 5Min Process Prio STATE CPU
8215 0.0% 0.0% 0.0% kosh.proc 0.044
1 0.0% 0.0% 0.0% 10 Reply 0.044
PID/TID 5Sec 1Min 5Min Process Prio STATE CPU
12290 0.0% 0.0% 0.0% chkptd.proc 0.080
1 0.0% 0.0% 0.0% 10 Receive 0.080
2 0.0% 0.0% 0.0% 10 Receive 0.000
PID/TID 5Sec 1Min 5Min Process Prio STATE CPU
12312 0.0% 0.0% 0.0% sysmgr.proc 0.112
1 0.0% 0.0% 0.0% 10 Receive 0.112
2 0.0% 0.0% 0.0% 10 Sigwaitin 0.000
PID/TID 5Sec 1Min 5Min Process Prio STATE CPU
12316 0.0% 0.0% 0.0% installer.proc 0.072
1 0.0% 0.0% 0.0% 10 Receive 0.000
3 0.0% 0.0% 0.0% 10 Nanosleep 0.000
4 0.0% 0.0% 0.0% 10 Sigwaitin 0.000
6 0.0% 0.0% 0.0% 10 Receive 0.000
Process sbin/ios-base, type IOS, PID = 12317
CPU utilization for five seconds: 12%/9%; one minute: 13%; five minutes: 10%
Task Runtime(us) Invoked uSecs 5Sec 1Min 5Min TTY Task Name
1 219 1503 145 0.00% 0.00% 0.00% 0 Hot Service Task
2 23680 42384 558 2.39% 6.72% 4.81% 0 Service Task
3 6104 11902 512 3.51% 1.99% 1.23% 0 Service Task
4 1720 5761 298 1.91% 0.90% 0.39% 0 Service Task
5 0 5 0 0.00% 0.00% 0.00% 0 Chunk Manager
6 0 1 0 0.00% 0.00% 0.00% 0 Connection Mgr
7 4 106 37 0.00% 0.00% 0.00% 0 Load Meter
8 6240 7376 845 0.23% 0.15% 0.55% 0 Exec
9 379 62 6112 0.00% 0.07% 0.04% 0 Check heaps
10 0 1 0 0.00% 0.00% 0.00% 0 Pool Manager
11 3 2 1500 0.00% 0.00% 0.00% 0 Timers
12 0 1 0 0.00% 0.00% 0.00% 0 AAA_SERVER_DEADT
13 0 2 0 0.00% 0.00% 0.00% 0 AAA high-capacit
14 307 517 593 0.00% 0.05% 0.03% 0 EnvMon
15 0 1 0 0.00% 0.00% 0.00% 0 OIR Handler
16 283 58 4879 0.00% 0.04% 0.02% 0 ARP Input
17 0 2 0 0.00% 0.00% 0.00% 0 Serial Backgroun
18 0 81 0 0.00% 0.00% 0.00% 0 ALARM_TRIGGER_SC
19 0 2 0 0.00% 0.00% 0.00% 0 DDR Timers
20 0 2 0 0.00% 0.00% 0.00% 0 Dialer event
21 4 2 2000 0.00% 0.00% 0.00% 0 Entity MIB API
22 0 54 0 0.00% 0.00% 0.00% 0 Compute SRP rate
23 0 9 0 0.00% 0.00% 0.00% 0 IPC Dynamic Cach
24 0 1 0 0.00% 0.00% 0.00% 0 IPC Zone Manager
25 0 1 0 0.00% 0.00% 0.00% 0 IPC Punt Process
26 4 513 7 0.00% 0.00% 0.00% 0 IPC Periodic Tim
27 11 513 21 0.00% 0.00% 0.00% 0 IPC Deferred Por
28 0 1 0 0.00% 0.00% 0.00% 0 IPC Seat Manager
29 83 1464 56 0.00% 0.00% 0.00% 0 EEM ED Syslog
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| TotalCPUutilizationforfive seconds | TotalCPUutilizationforthelast5seconds.Thesecondnumberindicates thepercentofCPUtimespentattheinterruptlevel. |
| 1minute | CPUutilizationforthelastminute. |
| 5minutes | CPUutilizationforthelast5minutes. |
| PID/TID | ProcessIDortaskID. |
| 5Sec | PercentageofCPUtimespentattheinterruptlevelforthisprocessduring thelastfiveseconds. |
| 1Min | PercentageofCPUtimespentattheinterruptlevelforthisprocessduring thelastminute. |
| 5Min | PercentageofCPUtimespentattheinterruptlevelforthisprocessduring thelastfiveminutes. |
| Process | Processname. |
| Prio | Priorityleveloftheprocess. |
| STATE | Currentstateoftheprocess. |
| CPU | CPUutilizationoftheprocessinminutesandseconds. |
| type | Typeofprocess;canbeeitherIOSorPOSIX. |
| Task | Tasksequencenumber. |
| Runtime(us) | CPUtimethattheprocesshasused(inmicroseconds). |
| Invoked | Numberoftimesthattheprocesshasbeeninvoked. |
| uSecs | MicrosecondsofCPUtimeforeachprocessinvocation. |
| 5Sec | CPUutilizationbytaskinthelast5seconds. |

| Field | Description |
| --- | --- |
| 1Min | CPUutilizationbytaskinthelastminute. |
| 5Min | CPUutilizationbytaskinthelast5minutes. |
| TTY | Terminalthatcontrolstheprocess. |
| TaskName | Taskname. |

Cisco Catalyst 4500e Series Switches running IOS XE software The following is sample output from the show processes cpu command:

```text
Switch#show proc cpu
Core 0: CPU utilization for five seconds: 1%; one minute: 7%; five minutes: 5%
Core 1: CPU utilization for five seconds: 1%; one minute: 20%; five minutes: 12%
PID Runtime(ms) Invoked uSecs 5Sec 1Min 5Min TTY Process
1 935 596 156971 0.00 0.00 0.00 0 init
2 0 79 10405 0.00 0.00 0.00 0 kthreadd
3 13 2450 5575 0.00 0.00 0.00 0 migration/0
4 12 808 15237 0.00 0.00 0.00 0 ksoftirqd/0
5 8 1413 6170 0.00 0.00 0.00 0 migration/1
6 14 894 16370 0.00 0.00 0.00 0 ksoftirqd/1
7 31 1422 21961 0.00 0.00 0.00 0 events/0
8 32 1269 25403 0.00 0.00 0.00 0 events/1
9 5 637 9070 0.00 0.00 0.00 0 khelper
61 80 79 102031 0.00 0.00 0.00 0 kblockd/0
62 90 183 497142 0.00 0.00 0.00 0 kblockd/1
75 0 21 1238 0.00 0.00 0.00 0 khubd
78 0 23 652 0.00 0.00 0.00 0 kseriod
83 7 26 271115 0.00 0.00 0.00 0 kmmcd
--More--
```

The following is partial sample output from the show processes cpucommand with the detailedkeyword:

```text
switch#show proc cpu detailed
Core 0: CPU utilization for five seconds: 0%; one minute: 6%; five minutes: 5%
Core 1: CPU utilization for five seconds: 2%; one minute: 17%; five minutes: 12%
PID T C TID Runtime(ms) Invoked uSecs 5Sec 1Min 5Min TTY Process
(%) (%) (%)
1 L 935 596 156971 0.00 A 0.00 0.00 0 init
2 L 0 79 10405 0.00 A 0.00 0.00 0 kthreadd
3 L 13 2481 5573 0.00 A 0.00 0.00 0 migration/0
4 L 12 808 15237 0.00 A 0.00 0.00 0 ksoftirqd/0
5 L 8 1454 6157 0.00 A 0.00 0.00 0 migration/1
6 L 14 897 16341 0.00 A 0.00 0.00 0 ksoftirqd/1
7 L 31 1471 21661 0.00 A 0.00 0.00 0 events/0
8 L 33 1308 25496 0.00 A 0.00 0.00 0 events/1
9 L 5 637 9070 0.00 A 0.00 0.00 0 khelper
61 L 80 79 102031 0.00 A 0.00 0.00 0 kblockd/0
62 L 90 183 497142 0.00 A 0.00 0.00 0 kblockd/1
75 L 0 21 1238 0.00 A 0.00 0.00 0 khubd
78 L 0 23 652 0.00 A 0.00 0.00 0 kseriod
83 L 7 26 271115 0.00 A 0.00 0.00 0 kmmcd
120 L 0 25 320 0.00 A 0.00 0.00 0 pdflush
121 L 103 195 531687 0.00 A 0.00 0.00 0 pdflush
122 L 0 29 172 0.00 A 0.00 0.00 0 kswapd0
123 L 0 31 161 0.00 A 0.00 0.00 0 aio/0
124 L 0 33 121 0.00 A 0.00 0.00 0 aio/1
291 L 0 35 142 0.00 A 0.00 0.00 0 kpsmoused
--More--
```

The following is sample output from the show processes cpu history summarycommand:

```text
Switch#show processes cpu history summary
History information for system:
0....5....1....1....2....2....3....3....4....4....5....5....
0 5 0 5 0 5 0 5 0 5
CPU% per second (last 60 seconds)
* = maximum CPU% # = average CPU%
50 * *
30 * ** * ** * ** * **
20 # # #*##*#*##* * * *
10 * # ## ##
0....5....1....1....2....2....3....3....4....4....5....5....
0 5 0 5 0 5 0 5 0 5
CPU% per minute (last 60 minutes)
* = maximum CPU% # = average CPU%
50**
0....5....1....1....2....2....3....3....4....4....5....5....6....6....7.
0 5 0 5 0 5 0 5 0 5 0 5 0
CPU% per hour (last 72 hours)
* = maximum CPU% # = average CPU%
```

The following is sample output from the show processes cpu history detailedcommand:

```text
Switch#show processes cpu history detailed
History information for core 0:
0....5....1....1....2....2....3....3....4....4....5....5....
0 5 0 5 0 5 0 5 0 5
CPU% per second (last 60 seconds)
* = maximum CPU% # = average CPU%
60 *
20 ** * ** * * *
10 * * * * * * ** * * * *
0....5....1....1....2....2....3....3....4....4....5....5....
0 5 0 5 0 5 0 5 0 5
CPU% per minute (last 60 minutes)
* = maximum CPU% # = average CPU%
60*
30 *
0....5....1....1....2....2....3....3....4....4....5....5....6....6....7.
0 5 0 5 0 5 0 5 0 5 0 5 0
CPU% per hour (last 72 hours)
* = maximum CPU% # = average CPU%
History information for core 1:
10 *****
0....5....1....1....2....2....3....3....4....4....5....5....
0 5 0 5 0 5 0 5 0 5
CPU% per second (last 60 seconds)
* = maximum CPU% # = average CPU%
100 *
90 *
40 ********** * ** ** **
30 * *
10* *
0....5....1....1....2....2....3....3....4....4....5....5....
0 5 0 5 0 5 0 5 0 5
CPU% per minute (last 60 minutes)
* = maximum CPU% # = average CPU%
100*
90 *
0....5....1....1....2....2....3....3....4....4....5....5....6....6....7.
0 5 0 5 0 5 0 5 0 5 0 5 0
CPU% per hour (last 72 hours)
* = maximum CPU% # = average CPU%
Switch#show proc cpu history table
CPU utilization for five seconds: 1%/0% at 01:14:44
PID 5Sec Process
10319 6 iosd
CPU utilization for five seconds: 1%/0% at 01:14:49
PID 5Sec Process
10319 6 iosd
CPU utilization for five seconds: 1%/0% at 01:14:54
PID 5Sec Process
10319 6 iosd
CPU utilization for five seconds: 1%/0% at 01:14:59
PID 5Sec Process
10319 6 iosd
Switch#
```

The table below describes the fields shown in the output.

| Field | Description |
| --- | --- |
| Core(#) | CoreforwhichCPUutilizationisbeinggenerated. |
| CPUutilizationforfiveseconds | CPUutilizationforthelast5seconds.Thesecondnumberindicatesthe percentofCPUtimespentattheinterruptlevel. |
| oneminutes | CPUutilizationforthelastminute. |
| fiveminutess | CPUutilizationforthelast5minutes. |
| PID | ProcessID. |
| Runtime(us) | CPUtimethattheprocesshasused(inmicroseconds). |
| Invoked | Numberoftimesthattheprocesshasbeeninvoked. |
| uSecs | MicrosecondsofCPUtimeforeachprocessinvocation. |

| Field | Description |
| --- | --- |
| 5Sec | CPUutilizationbytaskinthelast5seconds. |
| 1Min | CPUutilizationbytaskinthelastminute. |
| 5Min | CPUutilizationbytaskinthelast5minutes. |
| TTY | Terminalthatcontrolstheprocess. |
| Process | Nameoftheprocess. |


### `show processes detailed`

> **Página:** 903 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** If no process ID or process name is specified, detailed information is displayed about all processes. · **Leitura (show/clear/…):** sim

**Description:** To display detailed information about POSIX and Cisco IOS processes when Cisco IOS Software Modularity or Cisco IOS XE images are running, use the show processes detailedcommand in user EXEC or privileged EXEC mode. Cisco IOS software Cisco Catalyst 4500e Series Switches running IOS XE software

**Syntax:**

```text
show processes detailed [process-idprocess-name]
show processes detailed [process-id]
```

**Parameters (Syntax Description):**

- `process` — ( Optional) Shows detail s about as p e c if i c process.
- `process-id` — ( Optional) Process id e n t if i e r.
- `process-name` — ( Optional) Process name.

**Command Default:** If no process ID or process name is specified, detailed information is displayed about all processes.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SXF4 | This command was introduced to support Software M o d u l a r it y image s. |
| CiscoIOSXERelease3.1.0.SG | This command was introduced on the Cisco Catalyst4500 e Serfies Switch e s. |

**Usage Guidelines:**

Use the show processes detailed command to gather detailed information about the number of tasks running, the process state, and other information about a process that is not displayed by the show processes command. On Cisco IOS XE images, show process detailed will also show process, thread and task details.

**Example:**

Example output varies between Cisco IOS software images and Cisco Catalyst 4500e Series Switches running IOS XE software. The following sections show output examples for each image. Cisco IOS Software The following is sample output from the show processes detailedcommand for the process named sysmgr.proc:

```text
show processes detailed sysmgr.proc
Job Id: 67
PID: 8210
Executable name: sysmgr.proc
Executable path: sbin/sysmgr.proc
Instance ID: 1
Args: -p
Respawn: ON
Respawn count: 1
Max. spawns per minute: 30
Last started: Mon Aug18 17:08:53 2003
Process state: Run
core: SHAREDMEM MAINMEM
Max. core: 0
Level: 39
PID TID Stack pri state Blked HR:MM:SS:MSEC FLAGS NAME
8210 1 52K 10 Receive 1 0:00:00:0071 00000000 sysmgr.proc
8210 2 52K 10 Sigwaitinfo 0:00:00:0000 00000000 sysmgr.proc
8210 3 52K 10 Receive 8 0:00:00:0003 00000000 sysmgr.proc
8210 4 52K 10 Reply 1 0:00:00:0003 00000000 sysmgr.proc
8210 5 52K 10 Receive 1 0:00:00:0000 00000000 sysmgr.proc
8210 6 52K 10 Receive 1 0:00:00:0015 00000000 sysmgr.proc
8210 7 52K 10 Receive 1 0:00:00:0000 00000000 sysmgr.proc
8210 8 52K 10 Receive 1 0:00:00:0000 00000000 sysmgr.proc
-----------------------------------------------------------------
Job Id: 78
PID: 12308
Executable name: sysmgr.proc
Executable path: sbin/sysmgr.proc
Instance ID: 2
Args: -p
Respawn: ON
Respawn count: 1
Max. spawns per minute: 30
Last started: Mon Aug18 17:08:54 2003
Process state: Run
core: SHAREDMEM MAINMEM
Max. core: 0
Level: 40
PID TID Stack pri state Blked HR:MM:SS:MSEC FLAGS NAME
12308 1 16K 10 Receive 1 0:00:00:0039 00000000 sysmgr.proc
12308 2 16K 10 Sigwaitinfo 0:00:00:0000 00000000 sysmgr.proc
-----------------------------------------------------------------
```

Cisco Catalyst 4500e Series Switches running IOS XE software The following is sample output from the show processes detailed command showing details of the iosd process:

```text
Switch#show proc cpu
Switch#show processes detailed process iosd
Process Id : 10319
Process Name : iosd
Parent Process Id : 9416
Group Id : 10319
Status : Sl
Session Id : 9415
User Time : 7875
Kernel Time : 2281
Priority :
Virtual Bytes : 1819336
Resident Pages : 953636
Resident Limit : 4194303
Minor PageFaults : 238050
Major PageFaults : 1088
Cmdline arguments : -n 2048 -m 256 -l lanbase
Thread Listing:
PID C TID Stack Pri TTY NAME
10319 1 10319 84 20 0 iosd
10319 0 10873 84 30 0 iosd
10319 0 10874 84 20 0 iosd
Task Listing:
PID QTy PC Runtime(ms) Invoked uSecs Stacks TTY Process
1 Cwe 29764508 4 7 0 504/35000 0 Chunk Manager
2 Csp 28101409 0 85 0 408/32000 0 Load Meter
3 Hwe 26994556 0 1 0 328/35000 0 Deferred Events
4 Mwe 27835771 0 6 0 7816/35000 0 SpanTree Helper
5 Mwe 27139064 0 1 0 328/35000 0 Retransmission of I
6 Mwe 27138527 0 1 0 328/35000 0 IPC ISSU Receive Pr
7 Lst 29780794 220 45 0 424/35000 0 Check heaps
8 Cwe 29784274 0 9 0 520/35000 0 Pool Manager
9 Mst 28412237 0 2 0 456/35000 0 Timers
10 Mwe 27212830 0 2 0 472/35000 0 Serial Background
11 Mwe 28504055 32 22 0 3176/35000 0 RF Slave Main Threa
12 Mwe 27808556 0 1 0 344/35000 0 ifIndex Receive Pro
13 Mwe 27917322 12 91 0 552/53000 0 IOSD ipc task
14 Mwe 27917399 0 2 0 584/53000 0 IOSD chasfs task
15 Mwe 28318114 0 2 0 1384/35000 0 cpf_msg_holdq_proce
16 Mwe 27927986 4 94 0 4904/35000 0 IOSd System Config
17 Cwe 27917853 0 227 0 536/35000 0 IOSD heartbeat proc
18 Mwe 28152849 8 14 0 488/35000 0 ARP Input
19 Lwe 28315806 0 1 0 312/35000 0 CEF MIB API
20 Lwe 28397268 0 1 0 280/35000 0 AAA_SERVER_DEADTIME
21 Mwe 28394584 0 2 0 456/35000 0 AAA high-capacity c
22 Mwe 28495535 0 1 0 392/41000 0 Policy Manager
23 Lwe 28553141 0 7 0 696/35000 0 Entity MIB API
24 Mwe 28793021 0 1 0 296/35000 0 IFS Agent Manager
--More--
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| JobId | Jobidentifier. |
| PID | ProcessID. |
| Executablename | Processname. |
| Executablepath | Pathandfilenameoftheprocess. |
| InstanceID | Instancenumber. |
| Args | Argumentssenttotheprocessatstartup. |
| Respawn | Abilitytorespawnprocess:onoroff. |
| Respawncount | Numberofrespawnsofthisprocesssincebootwherebootequalsone. |
| Max.spawnsperminute | Maximumnumberofrespawnsperminuteforthisprocess. |
| Laststarted | Dateandtimetheprocesswaslaststarted. |
| Processstate | Currentstateofprocess. |
| Core | Coredumpoptionsspecifiedfortheprocess. |
| Max.core | Maximumnumberofdumpsallowedforthisprocess. |
| Level | Internalnumberthatdeterminesthestartuporderfortheprocess. |
| TID | ThreadID. |
| Stack | Size,inkilobytes,ofthememorystack. |
| pri | Processpriority. |
| state | Currentstateofprocess. |
| Blked | Thread(withgivenprocessID)thatiscurrentlyblockedbytheprocess. |
| HR:MM:SS:MSEC | Time(inhours,minutes,seconds,andmilliseconds)usedbytheprocess. |
| FLAGS | Processflags(bitmask). |
| NAME | Processname. |


### `show processes interrupt mask buffer`

> **Página:** 907 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information in the interrupt mask buffer, use the show processes interrupt mask buffercommand in privileged EXEC mode.

**Syntax:**

```text
show processes interrupt mask buffer
```

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(2)T | This command was introduced. |

**Example:**

The following is sample output from the show processes interrupt mask buffer command. The output displays stack trace and relevant information about the places where interrupts have been masked more than the configured threshold time:

```text
Router# show processes interrupt mask buffer
Allowable interrupt mask time : 50 micro seconds
Allowable number of half pipeline ticks for this platform : 5000
Buffer Size : 50 entries
NETS Disable : 3
TTY Disable : 4
ALL Disable : 4
emt_call : 11
disable_interrupts : 12
PID Level Time Spent(us) Count Stack Trace
3 11 360 1 0x608C3C14 0x60894748 0x6089437C 0x608943AC 0x609CEC88
0x609CECFC 0x609C8524
3 11 322 1 0x608C3C14 0x608943BC 0x609CEC88 0x609CECFC 0x609C8524
0x60867C28 0x607C70B0
3 4 147 1 0x6078AED4 0x6078BE94 0x6078C750 0x6078C8D4 0x607E27F0
0x607E27C0 0x607E50B0
```


### `show processes interrupt mask detail`

> **Página:** 908 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about interrupt masking, use the show processes interrupt mask detailcommand in privileged EXEC mode.

**Syntax:**

```text
show processes interrupt mask detail [pid]
```

**Parameters (Syntax Description):**

- `detail` — D is p l a y s information about the to t a l a mount of time and then u m be r of time s interrupt s have been mask e d by all processes.
- `pid` — ( Optional) An integer that specifies the process id for which to d is p l a y the to t a l a c c u m u l at e d time and then u m be r of time s interrupt s have been mask e d.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(2)T | This command was introduced. |

**Example:**

The following is sample output from the show processes interrupt mask detail command. the output displays information about the total amount of time and number of times interrupts have been masked by all processes:

```text
Router# show processes interrupt mask detail
PID Time Spent(us) Count Process Name
2 6388 1791 Load Meter
3 7957 16831 Exec
5 6710 2813 Check heaps
```

The following is sample output from the show processes interrupt mask detail command with the process ID specified. The output displays the total time (accumulative), number of times interrupts have been masked by a specific process:

```text
Router# show processes interrupt mask detail 2
Process ID : 2
Process Name : Load Meter
Total Interrupt Masked Time : 6586 (us)
Total Interrupt Masked Count : 1845
```


### `show processes memory`

> **Página:** 909 · **Modo:** Privileged EXEC (#) · **Default:** The memory used by all types of system processes is displayed. Cisco IOS XE Software and Software Modularity The system memory followed by a one-line summary of memory information about each IOS XE or Software Modularity process is displayed. · **Leitura (show/clear/…):** sim

**Description:** To display the amount of memory used by each system process in Cisco IOS, Cisco IOS XE, or Cisco IOS Software Modularity images, use the show processes memory command in privileged EXEC mode. Cisco IOS Software Cisco IOS Software Modularity Cisco Catalyst 4500e Series Switches Running IOS XE software

**Syntax:**

```text
show processes memory [process-id | sorted [allocated | getbufs | holding]]
show processes memory [[detailed [[process-name[:instance-id]] | process-id taskid
task-id]]][alloc-summary | sorted {start | size | caller}]
show processes memory [detailed [process iosd | task task-id] | sorted [allocated | getbufs | holding]]
```

**Parameters (Syntax Description):**

- `Cisco IOS Software Syntax`
- `process-id` — ( Optional) Process ID( P ID) of as p e c if i c process. When you specify a process ID, only detail s for the specified process will be show n.
- `sorted` — ( Optional) D is p l a y s memory data s or t e d by the Allocate d, Get b u f s, or Hold in g c o l u m n. If the s or t e d keyword is used by its e l f, data is s or t e d by the Hold in g c o l u m n by default.
- `allocate d` — ( Optional) D is p l a y s memory data s or t e d by the Allocate d c o l u m n.
- `getbufs` — ( Optional) D is p l a y s memory data s or t e d by the Get b u f s( Get Buffers) column.
- `holding` — ( Optional) D is p l a y s memory data s or t e d by the Hold in g c o l u m n. This keyword is the default.
- `CiscoIOSSoftwareModularity Syntax` — ( Optional) D is p l a y s detailed information about ios p r o c processes.
- `detailed`
- `process-name` — ( Optional) Process name.
- `: instance-id` — ( Optional) In s t an c e name of e it h e r the Cisco IOS t as k or P O S I X process. The c o l on isr e q u i r e d.
- `process-id` — ( Optional) Process id e n t if i e r.
- `Cisco IOS Software Syntax`
- `taskid task-id` — ( Optional) D is p l a y s detailed memory usage of as p e c if i e d Cisco IOStask with in ap r o c e s s.
- `alloc-summary` — ( Optional) D is p l a y s summary P O S I X process memory usage p e r alloc at or.
- `sorted` — ( Optional) D is p l a y s P O S I X process memory usage s or t e d by start address, size, or the P C that c all e d the process.
- `start` — ( Optional) D is p l a y s P O S I X process memory usage s or t e d by the start address of the process.
- `size` — ( Optional) D is p l a y s P O S I X process memory usage s or t e d by the size of the process.
- `caller` — ( Optional) D is p l a y s P O S I X process memory usage s or t e d by the PCthat c all e d the process.

**Command Default:** The memory used by all types of system processes is displayed. Cisco IOS XE Software and Software Modularity The system memory followed by a one-line summary of memory information about each IOS XE or Software Modularity process is displayed.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.0(23)S | The s or t e d, allocate d, get b u f s, and hold in g keywords were added. |
| 12.2(13) | The s or t e d, allocate d, get b u f s, and hold in g keywords were added. |
| 12.2(13)S | The s or t e d, allocate d, get b u f s, and hold in g keywords were added. |
| 12.2(13)T | The s or t e d, allocate d, get b u f s, and hold in g keywords were added. |
| 12.0(28)S | The output of the h e a d e r line was u p d at e d to support the Memory Threshold in g feature. |
| 12.2(22)S | The output of the h e a d e r line was u p d at e d to support the Memory Threshold in g feature. |
| 12.3(7)T | The output of the h e a d e r line was u p d at e d to support the Memory Threshold in g feature. |
| 12.0(30)S | The summary information( first lines of output) for this command was s e p a r at e d from the r e s to f the output and l a be l e d by memory pool type( To t a l Process Memory, To t a l I/ O Memory, and s o on). This e n h an c e m e n t also c or r e c t e d at o t a l process memory m is m at c h error( m is m at c h be t we e n the show processes memory command, the show processes memory s or t e d command, and the show memory command and its v a r i an t s). |
| 12.2(28)S | The summary information( first lines of output) for this command was s e p a r at e d from the r e s to f the output and l a be l e d by memory pool type( To t a l Process Memory, To t a l I/ O Memory, and s o on). This e n h an c e m e n t also c or r e c t e d at o t a l process memory m is m at c h error( m is m at c h be t we e n the show processes memory command, the show processes memory s or t e d command, and the show memory command and its v a r i an t s). |
| 12.3(11)T | The summary information( first lines of output) for this command was s e p a r at e d from the r e s to f the output and l a be l e d by memory pool type( To t a l Process Memory, To t a l I/ O Memory, and s o on). This e n h an c e m e n t also c or r e c t e d at o t a l process memory m is m at c h error( m is m at c h be t we e n the show processes memory command, the show processes memory s or t e d command, and the show memory command and its v a r i an t s). |
| 12.2(18)SXF4 | The syntax was modified to support Cisco IOS Software M o d u l a r it y image s. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease 3.1.0.SG | This command was introduced on the Cisco Catalyst4500 e Series Switch e s. |
| CiscoIOSXERelease 3.3S | This command was in t r o d u c t e do n the Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Usage Guidelines:**

The show processes memory command and the show processes memory sorted command displays a summary of total, used, and free memory, followed by a list of processes and their memory impact. If the standard show processes memory process-id command is used, processes are sorted by their PID. If the show processes memory sorted command is used, the default sorting is by the Holding value. Output Prior to Releases 12.3(7)T, 12.2(22)S, and 12.0(28)S The first line (header line) of the show processes memory[sorted] command listed Total memory, Used memory, and Free memory values. Output in Releases 12.3(7)T, 12.3(8)T, and 12.2(22)S Through 12.2(27)S2, 12.0(28)S, and 12.0(29)S In Releases 12.3(7)T, 12.2(22)S, and 12.0(28)S, the Memory Thresholding feature was introduced. This feature affected the header line and the Holding column of the show processes memory command as described in this section. The value for Total in the show processes memory commandand the values listed in the Holding column showed the total (cumulative) value for the processor memory pools and the alternate memory pool* (typically, the I/O memory pool). However, the show processes memory sorted version of this command, and other commands, such as the show memory summary command, did not include the alternate memory pool in the totals; that is, these commands showed the total value for the Processor memory pool only. This caused an observed mismatch of memory totals between commands. If you are using these releases, use the output of the show memory summary command to determine the individual amounts of Total and Free memory for the Processor memory pool and the I/O memory pool. Output in Releases 12.3(11)T, 12.2(28)S, 12.0(30)S, and Later Releases Beginning in Releases 12.3(11)T, 12.2(28)S, and 12.0(30)S, the summary information (first output lines) for the show processes memory command is separated by memory pool. For example, there are now individual lines for Total Process Memory, Total I/O Memory, and Total PCI Memory. In these releases or later releases, your Total Process Memory should match the total process memory shown for other commands, such as the show memory summarycommand. About Alternate Memory Pools An “alternate memory pool” is a memory pool that can be used as an alternative to allocate memory when the target (main) memory pool has been filled. For example, many platforms have a memory type called “Fast” that is limited to a small size (because the memory media used for Fast memory is expensive). You can prevent memory allocations from failing once the available Fast memory has been used up, by configuring the normal Processor memory as an alternative memory pool for the Fast memory pool. Cisco IOS XE Software and Software Modularity Use the show processes memory command without any arguments and keywords to display the system memory followed by a one-line summary of memory information about each modular Cisco IOS process. Use the detailed keyword with this command to display detailed memory information about all processes. Other arguments and keywords are used to display Cisco IOS Software Modularity process memory information for a specified process name or process ID. On Cisco IOS XE images only, the detailed keyword will also show Cisco IOS task memory details. show processes memory Command for Cisco IOS Releases Prior to 12.3(7)T, 12.2(22)S, and 12.0(28)S The following is sample output from the show processes memory command:

```text
Router# show processes memory
Processor Pool Total: 25954228 Used: 8368640 Free: 17585588
PID TTY Allocated Freed Holding Getbufs Retbufs Process
0 0 8629528 689900 6751716 0 0 *Init*
0 0 24048 12928 24048 0 0 *Sched*
0 0 260 328 68 350080 0 *Dead*
1 0 0 0 12928 0 0 Chunk Manager
2 0 192 192 6928 0 0 Load Meter
3 0 214664 304 227288 0 0 Exec
4 0 0 0 12928 0 0 Check heaps
5 0 0 0 12928 0 0 Pool Manager
6 0 192 192 12928 0 0 Timers
7 0 192 192 12928 0 0 Serial Backgroun
8 0 192 192 12928 0 0 AAA high-capacit
9 0 0 0 24928 0 0 Policy Manager
10 0 0 0 12928 0 0 ARP Input
11 0 192 192 12928 0 0 DDR Timers
12 0 0 0 12928 0 0 Entity MIB API
13 0 0 0 12928 0 0 MPLS HC Counter
14 0 0 0 12928 0 0 SERIAL A'detect
78 0 0 0 12992 0 0 DHCPD Timer
79 0 160 0 13088 0 0 DHCPD Database
8329440 Total
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| ProcessorPoolTotal | Totalamountofmemory,inkilobytes(KB),heldfortheProcessormemorypool. |
| Used | Totalamountofusedmemory,inKB,intheProcessormemorypool. |
| Free | Totalamountoffreememory,inKB,intheProcessormemorypool. |
| PID | ProcessID. |
| TTY | Terminalthatcontrolstheprocess. |
| Allocated | Bytesofmemoryallocatedbytheprocess. |
| Freed | Bytesofmemoryfreedbytheprocess,regardlessofwhooriginallyallocatedit. |
| Holding | Amountofmemory,inKB,currentlyallocatedtotheprocess. |
| Getbufs | Numberoftimestheprocesshasrequestedapacketbuffer. |
| Retbufs | Numberoftimestheprocesshasrelinquishedapacketbuffer. |
| Process | Processname. |
| *Init* | Systeminitializationprocess. |
| *Sched* | Theschedulerprocess. |
| *Dead* | Processesasagroupthatarenowdead. |
| <value>Total | Totalamountofmemory,inKB,heldbyallprocesses(sumofthe“Holding”column). |

The following is sample output from the show processes memory command when the sorted keyword is used. In this case, the output is sorted by the Holding column, from largest to smallest.

```text
Router# show processes memory sorted
Processor Pool Total: 25954228 Used: 8371280 Free: 17582948
PID TTY Allocated Freed Holding Getbufs Retbufs Process
0 0 8629528 689900 6751716 0 0 *Init*
3 0 217304 304 229928 0 0 Exec
53 0 109248 192 96064 0 0 DHCPD Receive
56 0 0 0 32928 0 0 COPS
19 0 39048 0 25192 0 0 Net Background
42 0 0 0 24960 0 0 L2X Data Daemon
58 0 192 192 24928 0 0 X.25 Background
43 0 192 192 24928 0 0 PPP IP Route
49 0 0 0 24928 0 0 TCP Protocols
48 0 0 0 24928 0 0 TCP Timer
17 0 192 192 24928 0 0 XML Proxy Client
9 0 0 0 24928 0 0 Policy Manager
40 0 0 0 24928 0 0 L2X SSS manager
29 0 0 0 24928 0 0 IP Input
44 0 192 192 24928 0 0 PPP IPCP
32 0 192 192 24928 0 0 PPP Hooks
34 0 0 0 24928 0 0 SSS Manager
41 0 192 192 24928 0 0 L2TP mgmt daemon
16 0 192 192 24928 0 0 Dialer event
35 0 0 0 24928 0 0 SSS Test Client
--More--
```

The following is sample output from the show processes memory command when a process ID (process-id) is specified:

```text
show processes memory 1
Process ID: 1
Process Name: Chunk Manager
Total Memory Held: 8428 bytes
Processor memory holding = 8428 bytes
pc = 0x60790654, size = 6044, count = 1
pc = 0x607A5084, size = 1544, count = 1
pc = 0x6076DBC4, size = 652, count = 1
pc = 0x6076FF18, size = 188, count = 1
I/O memory holding = 0 bytes
show processes memory 2
Process ID: 2
Process Name: Load Meter
Total Memory Held: 3884 bytes
Processor memory holding = 3884 bytes
pc = 0x60790654, size = 3044, count = 1
pc = 0x6076DBC4, size = 652, count = 1
pc = 0x6076FF18, size = 188, count = 1
I/O memory holding = 0 bytes
```

show processes memory Command for Cisco IOS Releases Prior to 12.3(11)T, 12.2(28)S, and 12.0(30)S The following example shows the output of the show processes memorycommand before the changes to the summary information were made. Note that the Total in the show processes summary command output indicates total memory for all memory pools; in this example, the show processes memory total of 35423840 can be obtained by adding the Processor and I/O totals shown in the output of the show memory summarycommand. Note also that the show processes memory sorted command lists the Total Processor Memory (matches the show memory summary Processor Total), but the show processes memory command (without the sorted keyword) lists the total for all memory pools (Processor plus I/O memory).

```text
Router# show version | include IOS
Cisco IOS Software, 3600 Software (C3660-BIN-M), Version 12.3(9)
Router# show memory summary
Head Total(b) Used(b) Free(b) Lowest(b) Largest(b)
Processor 61E379A0 27035232 8089056 18946176 17964108 17963664
I/O 3800000 8388608
2815088 5573520 5561520 5573472
Router# show processes memory
Total: 35423840
, Used: 10904192, Free: 24519648
PID TTY Allocated Freed Holding Getbufs Retbufs Process
0 0 14548868 3004980 9946092 0 0 *Init*
0 0 12732 567448 12732 0 0 *Sched*
Router# show processes memory sorted
Total:
, Used: 8089188, Free: 18946044
PID TTY Allocated Freed Holding Getbufs Retbufs Process
0 0 14548868 3004980 9946092 0 0 *Init*
64 0 76436 3084 74768 0 0 CEF process
show version | include IOS
Cisco IOS Software, 3600 Software (c3660-p-mz), Version 12.0(29)S,
Router# show memory summary
Head Total(b) Used(b) Free(b) Lowest(b) Largest(b)
Processor 126CB10 49,331,668 6454676 42876992 42642208 42490796
Router# show processes memory
Total: 50,994,868
, Used: 6220092, Free: 44774776
PID TTY Allocated Freed Holding Getbufs Retbufs Process
0 0 6796228 627336 5325956 0 0 *Init*
0 0 200 29792 200 0 0 *Sched*
0 0 192 744 0 349000 0 *Dead*
1 0 0 0 12896 0 0 Chunk Manager
Router# show processes memory sorted
Total: 50,994,868
, Used: 6222644, Free: 44772224
PID TTY Allocated Freed Holding Getbufs Retbufs Process
0 0 6796228 627336 5325956 0 0 *Init*
13 0 39056 0 25264 0 0 Net Background
48 0 0 0 24896 0 0 L2X SSS manager
18 0 0 0 24896 0 0 IP Input
```

show processes memory Command for Cisco IOS Software Modularity In a Cisco IOS Software Modularity image IOS, each process maintains its own heap memory, which is taken from the system memory in blocks. The process reuses this memory as required. If all the memory that was requested in a block is no longer in use, then the process can return the memory block to the system. The following is sample output from the show processes memorycommand when a Cisco IOS Software Modularity image is running:

```text
Router# show processes memory
System Memory : 262144K total, 113672K used, 148472K free
PID Text Data Stack Dynamic Total Process
1 0 0 12 0 12 kernel
12290 52 8 28 196 284 dumper.proc
3 12 8 8 144 172 devc-pty
4 132 8 8 32 180 devc-ser2681
6 16 12 24 48 100 pipe
8199 12 12 8 48 80 mqueue
8200 16 24 48 452 540 fsdev.proc
8201 52 20 8 96 176 flashfs_hes_slot1.proc
8202 52 20 8 80 160 flashfs_hes_bootflash.proc
8203 52 20 8 128 208 flashfs_hes_slot0.proc
8204 20 68 12 164 264 dfs_disk1.proc
8205 20 68 12 164 264 dfs_disk0.proc
8206 36 4 8 144 192 ldcache.proc
8207 32 8 20 164 224 syslogd.proc
8208 24 4 28 464 520 name_svr.proc
8209 124 104 28 344 600 wdsysmon.proc
8210 100 144 52 328 624 sysmgr.proc
8211 12 4 28 64 108 kosh.proc
12308 100 144 16 144 404 sysmgr.proc
12309 24 4 12 112 152 chkptd.proc
12310 12 4 8 96 120 syslog_dev.proc
12311 44 4 24 248 320 fh_metric_dir.proc
12312 36 4 24 216 280 fh_fd_snmp.proc
12313 36 4 24 216 280 fh_fd_intf.proc
12314 32 4 24 216 276 fh_fd_timer.proc
12315 40 4 24 216 284 fh_fd_ioswd.proc
12316 28 4 24 200 256 fh_fd_counter.proc
12317 80 20 44 368 512 fh_server.proc
12326 140 40 28 280 488 tcp.proc
12327 48 4 24 256 332 udp.proc
12328 4 4 28 4660 4696 iprouting.iosproc
12329 4 4 36 600 644 cdp2.iosproc
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| total | Totalamountofmemory,inKB,onthedevice. |
| used | Amountofmemory,inKB,usedinthesystem. |
| free | Amountoffreememory,inKB,availableinthesystem. |
| PID | ProcessID. |
| Text | Amountofmemory,inKB,usedbythetextsegmentofthespecifiedprocess. |
| Data | Amountofmemory,inKB,usedbythedatasegmentofthespecifiedprocess. |
| Stack | Amountofmemory,inKB,usedbythestacksegmentofthespecifiedprocess. |
| Dynamic | Amountofmemory,inKB,usedbythedynamicsegmentofthespecifiedprocess. |
| Total | Totalamountofmemory,inKB,usedbythespecifiedprocess. |
| Process | Processname. |

The following example shows the output of the show processes memory detailedcommand wherein the process (ios-base) holds sufficient memory to process a request of the Cisco IOS tasks without having to request more memory from the system. So although the amount of memory of the Cisco IOS tasks increased, the ios-base process does not consume more system memory.

```text
show processes memory detailed 16424 sorted holding
System Memory : 2097152K total, 1097777K used, 999375K free, 0K kernel reserved
Lowest(b) : 1017212928
Process sbin/ios-base, type IOS, PID = 16424
248904K total, 0K text, 0K data, 168K stack, 248736K dynamic
Heap : 385874960 total, 261213896 used, 124661064 free
Task TTY Allocated Freed Holding Getbufs Retbufs TaskName
0 0 156853816 11168 156365472 0 0 *Init*
38 0 65671128 3320184 62248368 0 0 PF_Init Process
661 0 73106800 38231816 33093704 0 0 PIM Process
487 0 2656186248 3806507384 33039576 0 0 cmfib
652 0 56256064 19166160 27087872 0 0 MFIB_mrib_read
4 0 91088216 68828800 13093720 0 0 Service Task
629 0 2059320 132840 1927392 0 0 Const2 IPv6 Pro
49 0 2155730560 2153990528 1741536 0 9579588 DiagCard1/-1
0 0 2510481432 1396998880 1463056 2804860 23260 *Dead*
444 0 7333952 5940064 1410992 0 0 FM core
411 0 12865536 7934952 1396544 0 0 CMET MGR
310 0 113849160 121164584 1284240 0 0 Exec
```

The following is sample output from the show processes memorycommand with details about the memory of process 12322 and the task with the ID of 1:

```text
Router# show processes memory detailed 12322 taskid 1
System Memory : 262144K total, 113456K used, 148688K free
Process sbin/c7200-p-blob, type IOS, PID = 12322
16568K total, 16K text, 8K data, 64K stack, 16480K dynamic
Memory Summary for TaskID = 1
Holding = 10248
PC Size Count
0x7322FC74 9192 1
0x73236538 640 1
0x73231E8C 256 1
0x74175060 160 1
```

The table below describes the significant fields shown in the display that are different from the table above.

| Field | Description |
| --- | --- |
| type | Typeofprocess:POSIXorIOS. |
| MemorySummaryforTaskID | TaskID. |
| Holding | Amountofmemory,inbytes,currentlyheldbythetask. |
| PC | CallerPCofthetask. |
| Size | Amountofmemory,inbytes,usedbythistask. |
| Count | Numberoftimesthattaskhasbeencalled. |

The following is sample output from the show processes memorycommand with details about the memory of POSIX process ID 234567 with summary process memory usage per allocator:

```text
show processes memory detailed 234567 alloc-summary
System Memory : 262144K total, 113672K used, 148472K free
Process sbin/sysmgr.proc, type POSIX, PID = 12308
404K total, 100K text, 144K data, 16K stack, 144K dynamic
81920 heapsize, 68620 allocated, 8896 free
Allocated Blocks
Address Usize Size Caller
0x0806C358 0x00000478 0x000004D0 0x721C7290
0x0806D1E0 0x00000128 0x00000130 0x72B90248
0x0806D318 0x00003678 0x000036E0 0x72B9820C
0x0806D700 0x000002A0 0x000002C0 0x72B8EB58
0x0806D770 0x00000058 0x00000060 0x72BA5488
0x0806D7D8 0x000000A0 0x000000B0 0x72B8D228
0x0806D8A8 0x00000200 0x00000208 0x721A728C
0x0806FF78 0x00000068 0x00000070 0x72BA78EC
0x08071438 0x0000005C 0x00000068 0x72B908A8
0x08071508 0x0000010E 0x00000120 0x72BA7AFC
0x08072840 0x000000A8 0x000000C0 0x7270A060
0x08072910 0x0000010C 0x00000118 0x7273A898
0x08072A30 0x000000E4 0x000000F0 0x72749074
0x08072B28 0x000000B0 0x000000B8 0x7276E87C
0x08072BE8 0x0000006C 0x00000078 0x727367A4
0x08072C68 0x000000B8 0x000000C0 0x7271E2A4
0x08072D30 0x000000D0 0x000000D8 0x7273834C
0x08072E10 0x00000250 0x00000258 0x72718A70
0x08073070 0x000002F4 0x00000300 0x72726484
0x08073378 0x000006A8 0x000006B0 0x73EA4DC4
0x08073A30 0x00000060 0x00000068 0x7352A9F8
0x08073B38 0x00000068 0x00000070 0x72B92008
0x08073BB0 0x00000058 0x00000060 0x72B9201C
0x08073EB8 0x00002FB4 0x000031C0 0x08026FEC
0x08074028 0x000020B8 0x000020C0 0x72709C9C
0x08077400 0x000000A0 0x000000A8 0x721DED94
0x08078028 0x000022B8 0x000022C0 0x727446B8
0x0807C028 0x00002320 0x00002328 0x72B907C4
Free Blocks
Address Size
0x0806FFF0 0x00000010
0x080714A8 0x00000058
0x08073E18 0x00000098
0x08073FE8 0x00000018
0x08076FA0 0x00000328
0x080774B0 0x00000B50
0x0807FFB8 0x00000048
0x08080028 0x00003FD8
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| heapsize | Sizeoftheprocessheap,inKB,. |
| allocated | Amountofmemory,inKB,,allocatedfromtheheap. |
| free | Amountoffreememory,inKB,,intheheapforthespecifiedprocess. |

| Field | Description |
| --- | --- |
| Address | Blockaddress,inhexadecimal. |
| Usize | Blocksize,inhexadecimal,withoutthetrailerheader. |
| Size | Blocksize,inhexadecimal. |
| Caller | CallerPCoftheallocatorofthisblock. |

Cisco Catalyst 4500e Series Switches Running Cisco IOS XE software The following is sample output from the show processes memory command:

```text
Switch#show proc memory
System memory : 1943928K total, 733702K used, 1210221K free, 153224K kernel reserved
Lowest(b) : 642265088
PID Text Data Stack Dynamic RSS Total Process
1 252 480 84 444 1648 3648 init
2 0 0 0 0 0 0 kthreadd
3 0 0 0 0 0 0 migration/0
4 0 0 0 0 0 0 ksoftirqd/0
5 0 0 0 0 0 0 migration/1
6 0 0 0 0 0 0 ksoftirqd/1
7 0 0 0 0 0 0 events/0
8 0 0 0 0 0 0 events/1
9 0 0 0 0 0 0 khelper
61 0 0 0 0 0 0 kblockd/0
62 0 0 0 0 0 0 kblockd/1
75 0 0 0 0 0 0 khubd
78 0 0 0 0 0 0 kseriod
83 0 0 0 0 0 0 kmmcd
120 0 0 0 0 0 0 pdflush
121 0 0 0 0 0 0 pdflush
122 0 0 0 0 0 0 kswapd0
123 0 0 0 0 0 0 aio/0
124 0 0 0 0 0 0 aio/1
291 0 0 0 0 0 0 kpsmoused
309 0 0 0 0 0 0 rpciod/0
310 0 0 0 0 0 0 rpciod/1
354 92 180 84 136 456 2188 udevd
700 0 0 0 0 0 0 loop1
716 0 0 0 0 0 0 loop2
732 0 0 0 0 0 0 loop3
2203 424 164 84 132 1172 3180 dbus-daemon
2539 76 160 84 132 532 1788 portmap
2545 76 160 84 132 532 1788 portmap
2588 232 396 84 132 992 4596 sshd
2602 196 320 84 132 752 2964 xinetd
2606 196 320 84 132 748 2964 xinetd
3757 76 160 84 132 532 1788 vsi work/0
3758 76 160 84 132 532 1788 vsi work/1
--More--
```

The following is sample output from the command: show processes memory detailed

```text
Switch#show proc memory detailed
System memory : 1943928K total, 734271K used, 1209657K free, 153224K kernel reserved
Lowest(b) : 642265088
PID Text Data Stack Dynamic RSS Total Process
1 252 480 84 444 1648 3648 init
354 92 180 84 136 456 2188 udevd
2203 424 164 84 132 1172 3180 dbus-daemon
2539 76 160 84 132 532 1788 portmap
2545 76 160 84 132 532 1788 portmap
2588 232 396 84 132 992 4596 sshd
2602 196 320 84 132 752 2964 xinetd
2606 196 320 84 132 748 2964 xinetd
3757 76 160 84 132 532 1788 vsi work/0
3758 76 160 84 132 532 1788 vsi work/1
3891 848 148 84 88 1432 2984 check_gdb_statu
3895 72 160 84 132 580 1676 watchdog
4453 848 276 84 216 1512 3112 app_printf.sh
4465 848 272 84 212 1508 3108 app_printf.sh
4596 148 43972 84 528 5176 56664 slproc
TaskID TTY Allocated Freed Holding Getbufs Retbufs Task
1 0 327920 1544 367952 0 0 Chunk Manager
2 0 184 184 37032 0 0 Load Meter
3 0 0 0 40032 0 0 Deferred Events
4 0 17840 3888 40032 0 0 SpanTree Helper
5 0 0 0 40032 0 0 Retransmission of I
6 0 0 0 40032 0 0 IPC ISSU Receive Pr
7 0 0 0 40032 0 0 Check heaps
8 0 179248 173976 45304 144568 140316 Pool Manager
9 0 184 184 40032 0 0 Timers
10 0 184 184 40032 0 0 Serial Background
--More--
```

The following is sample output from the show processes memory detailedcommand specifying the Iosd process:

```text
Switch#show proc memory detailed process iosd
Processor Pool Total: 805306368 Used: 225960152 Free: 579346216
I/O Pool Total: 16777216 Used: 216376 Free: 16560840
PID TTY Allocated Freed Holding Getbufs Retbufs Process
0 0 226577984 4410320 211589320 0 0 *Init*
0 0 0 1591600 0 0 0 *Sched*
0 0 2568488 1960496 676992 5368513 362940 *Dead*
1 0 327920 1544 367952 0 0 Chunk Manager
2 0 184 184 37032 0 0 Load Meter
3 0 0 0 40032 0 0 Deferred Events
4 0 17840 3888 40032 0 0 SpanTree Helper
5 0 0 0 40032 0 0 Retransmission o
6 0 0 0 40032 0 0 IPC ISSU Receive
7 0 0 0 40032 0 0 Check heaps
8 0 210880 205608 45304 170080 165828 Pool Manager
9 0 184 184 40032 0 0 Timers
10 0 184 184 40032 0 0 Serial Backgroun
--More--
```

The following is sample output from the show processes memory sortedcommand:

```text
Switch#show proc memory sorted
System memory : 1943928K total, 734279K used, 1209649K free, 153224K kernel reserved
Lowest(b) : 642265088
PID Text Data Stack Dynamic RSS Total Process
10319 67716 798420 84 252 954524 1012856 iosd
4888 1132 200108 84 4076 26772 275408 ffm
4884 620 690480 84 5328 18564 728076 eicored
7635 144 181696 84 7464 16660 202620 cli_agent
9374 1048 298308 84 1128 11488 328992 licensed
10335 1676 257544 84 1252 11044 293848 licenseagentd
4852 208 208996 84 1848 10812 237632 ha_mgr
7566 168 249336 84 1408 8560 273668 installer
7585 268 167656 84 1616 8432 185556 snmp_subagent
4880 308 135080 84 968 8200 153944 os_info_p
4894 100 232936 84 1144 8072 252748 plogd
7410 68 233708 84 1172 7928 253840 dtmgr
10329 160 142384 84 832 7144 228360 cpumemd
4968 104 158828 84 1052 7080 178184 iifd
5047 88 165604 84 700 6196 181184 pdsd
4870 80 157452 84 728 6088 172244 sysmgr
4856 200 132816 84 688 5872 147940 oscore_p
--More--
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| ProcessorPoolTotal | Totalamountofmemory,inKB,heldfortheProcessormemorypool. |
| I/OPoolTotal | Totalamountofmemory,inKB,heldfortheI/Omemorypool. |
| Used | Totalamountofusedmemory,inKB,intheProcessor/I/Omemorypool. |
| Free | Totalamountoffreememory,ininKB,intheProcessor/I/Omemorypool. |
| PID | ProcessID. |
| TTY | Terminalthatcontrolstheprocess. |
| Allocated | Bytesofmemoryallocatedbytheprocess. |
| Freed | Bytesofmemoryfreedbytheprocess,regardlessofwhooriginallyallocatedit. |
| Holding | Amountofmemory,inKB,currentlyallocatedtotheprocess. |
| Getbufs | Numberoftimestheprocesshasrequestedapacketbuffer. |
| Retbufs | Numberoftimestheprocesshasrelinquishedapacketbuffer. |
| Process | Processname. |
| *Init* | Systeminitializationprocess. |
| *Sched* | Theschedulerprocess. |
| *Dead* | Processesasagroupthatarenowdead. |
| <value>Total | Totalamountofmemory,inKB,heldbyallprocesses(sumofthe“Holding”column). |
