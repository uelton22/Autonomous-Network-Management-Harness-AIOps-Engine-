# Capítulo 12: show protocols through showmon

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## show monitor permit list through show process memory

### show protocols through showmon

• show protocols through showmon , on page 900

### show protocols through showmon

### `show protocols`

> **Página:** 924 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the configured protocols, use the show protocols command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show protocols [interface-name interface-number]
```

**Parameters (Syntax Description):**

- `interface-name` — • voaBypassIn --VOA-Bypass-In interface • voaBypassOut --VOA-Bypass-Out interface • voaFilterIn --VOA-Filter-In interface • voaFilterOut --VOA-Filter-Out interface • voaIn --VOA-In interface • voaOut --VOA-Out interface
- `interface-number` — ( Optional) Interface number. ( Optional) The type of interfaces. It can
- `be` — one of the following values: • ATM --ATM interface • Async --Async interface • Auto-Template --Auto-Template interface • BVI --Bridge-Group Virtual Interface • CDMA-Ix --CDMA Ix interface • C on t a in e r --C on t a in e r interface • CTunnel --C T u n n e l interface • Dialer --D i a l e r interface • Ethernet --Institute of Electriacl
- `E l e c t r on i c s` — Engineers (IEEE) 802.3 • FastEthernet --FastEthernet IEEE 802.3 • EsconPhy --ESCON interface • fcpa --Fiber Channel • Filter --F i l t e r interface • m u l t is e r v i c e --M u l t is e r v i c e interface • Pos-channel --POS Channel interfaces • SBC --Session Border Controller • SYSCLOCK --Telecom-Bus
- `Clock` — Control l e r • Tunnel --T u n n e l interface • Vif --PGM Multicast Host interface • V i r t u a l-Access --V i r t u a l access interface • Virtual-PPP --Virtual PPP interface • Virtual-Template --Virtual
- `template` — interface • Virtual-TokenRing --Virtual Token Ring • Vlan --Catalyst VLANs • vmi --Virtual Multipoint Interface

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.0(3)T | The command was integrated in are l e as e e a r l i e r than Cisco IOS Release12.0(3) T. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1. |

**Usage Guidelines:**

The show protocols command shows the global and interface-specific status of any configured Level 3 protocol.

**Example:**

The following is sample output from the show protocols command. The field names are self-explanatory.

```text
Router# show protocols
Global values:
Internet Protocol routing is enabled
FastEthernet0/0 is up, line protocol is up
Internet address is 10.4.9.14/24
vmi1 is down, line protocol is down
FastEthernet0/1 is up, line protocol is up
Internet address is 10.4.8.14/24
ATM2/0 is administratively down, line protocol is down
ATM2/0.1 is administratively down, line protocol is down
ATM2/0.2 is administratively down, line protocol is down
ATM2/0.200 is administratively down, line protocol is down
Ethernet3/0 is administratively down, line protocol is down
Ethernet3/0.1 is administratively down, line protocol is down
Ethernet3/1 is administratively down, line protocol is down
Ethernet3/2 is administratively down, line protocol is down
Ethernet3/3 is administratively down, line protocol is down
ATM6/0 is administratively down, line protocol is down
SSLVPN-VIF0 is up, line protocol is up
Interface is unnumbered. Using address of SSLVPN-VIF0 (0.0.0.0)
Virtual-Access1 is down, line protocol is down
Virtual-Template1 is down, line protocol is down
Virtual-Access2 is up, line protocol is up
Port-channel5 is down, line protocol is down
Port-channel5.1 is down, line protocol is down
Port-channel15 is down, line protocol is down
Virtual-Template100 is down, line protocol is down
Interface is unnumbered. Using address of vmi1 (0.0.0.0)
Dialer3 is up, line protocol is up
```

For more information on the parameters or protocols shown in this sample output, see the Cisco IOS IP Addressing Services Configuration Guide and the Cisco IOS IP Routing Protocols Configuration Guide.


### `show region`

> **Página:** 928 · **Modo:** Privileged EXEC (#) · **Default:** All memory regions are displayed. · **Leitura (show/clear/…):** sim

**Description:** To display valid memory regions (memory mapping) in use on your system, use the show region command in privileged EXEC mode.

**Syntax:**

```text
show region [address hex-address]
```

**Parameters (Syntax Description):**

- `address hex-address` — ( Optional) If a hexadecimal address is specified, this command will s e a r c h the region list for the specified address.

**Command Default:** All memory regions are displayed.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(13) | This command was introduced. |
| 12.0(23)S | This command was integrated into Cisco IOS Release12.0(23) S. |
| 12.2(25)S | This command was modified. The command output was u p d at e d to d is p l a y information about free region s. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SRE | This command was modified. The output was u p d at e d to d is p l a y h e ap region memory size in chunks of16 M B. |

**Usage Guidelines:**

This command can be useful for troubleshooting system bus errors. The system encounters a bus error when the processor tries to access a memory location that either does not exist (a software error) or does not respond properly (a hardware problem). To use the show region command to troubleshoot a bus error, note the memory location address from the show version command, the show context command, or from the system error message that alerted you to the bus error. The show region command can then be used to determine if that address is a valid memory location. For example, in the output of the show version command after a system restart caused by a bus error, you will see output similar to “System restarted by bus error at PC 0x30EE546, address 0xBB4C4.” In this case, the memory location that the router tried to access is 0xBB4C4. If the address falls within one of the ranges in the show region output, it means that the router was accessing a valid memory address, but the hardware corresponding to that address is not responding properly. This indicates a hardware problem. If the address reported by the bus error does not fall within the ranges displayed in the show region output, this error means that the router was trying to access an address that is not valid, which indicates that it is a Cisco IOS software problem. More detailed information is available on Cisco.com in Tech Note #7949, "Troubleshooting Bus Error Crashes". Transient Memory Allocation The Transient Memory Allocation feature is enabled on platforms like the Cisco 7200 series router and the Cisco 10000 series router. This feature allocates all transient memory in a separate memory address space (separate region), so that there is no interleaving of static and transient memory blocks. Hence, the output of the show region command will have heap region memory size in chunks of 16 MB.

**Example:**

The following is sample output from the show region command:

```text
show region
Region Manager:
Start End Size(b) Class Media Name
0x0C000000 0x0FFFFFFF 67108864 Iomem R/W iomem
0x20000000 0x2FFFFFFF 268435456 Local R/W extended_2
0x50000000 0x5FFFFFFF 268435456 Local R/W extended_1
0x60000000 0x7BFFFFFF 469762048 Local R/W main
0x600090F8 0x6200A807 33560336 IText R/O main:text
0x62014C50 0x62F5B1EF 16016800 IData R/W main:data
0x62F5B1F0 0x6333500F 4038176 IBss R/W main:bss
0x63335010 0x6359A0D3 2511044 Local R/W main:saved-data
0x6359A0D4 0x6459A0D3 16777216 Local R/W main:heap
0x7B000000 0x7BFFFFFF 16777216 Local R/W main:heap
0x80000000 0x8BFFFFFF 201326592 Local R/W main:(main_k0)
0xA0000000 0xABFFFFFF 201326592 Local R/W main:(main_k1)
Free Region Manager:
Start End Size(b) Class Media Name
0x6459A12C 0x7AFFFFA7 380001916 Local R/W heap
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Start | Startaddressofthememoryblock. |
| End | Endaddressofthememoryblock. |
| Size(b) | Sizeofthememoryblock. |
| Class | Classofthememory. |
| Media | Typeoftheregionmedia.Read-only(R/O),read-write(R/W),andsoon. |
| Name | Nameoftheregion. |
| Iomem | Input/output(I/O)memory.Itisatypeofpacketmemory. |
| Local | Localmemory. |
| IText | Imagetextmemory. |
| IData | Imagedatamemory. |
| IBss | Imageblindsourceseparation(BSS)memory. |

| Field | Description |
| --- | --- |
| R/W | Readandwritememory. |
| R/O | Read-onlymemory. |


### `show registry`

> **Página:** 930 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** If no options are specified, registry information is displayed for all registries. · **Leitura (show/clear/…):** sim

**Description:** To display the function registry information when Cisco IOS or Cisco IOS Software Modularity images are running, use the show registrycommand in user EXEC or privileged EXEC mode. Cisco IOS Software Cisco IOS Software Modularity

**Syntax:**

```text
show registry [registry-name [registry-number]] [brief | statistics]
show registry [name [registry-name [registry-number]]] [brief [name [registry-name
[registry-number]]] | preemptions | rpcp status | statistics [brief] [name [registry-name
[registry-number]]] [remote]] [process {process-nameprocess-id}]
```

**Parameters (Syntax Description):**

- `Cisco IOS Software Syntax`
- `registry-name` — ( Optional) Name of the registry to d is p l a y.
- `registry-number` — ( Optional) Number of the registry to d is p l a y.
- `brief` — ( Optional) D is p l a y s limit e d f u n c t i on s and service s information.
- `statistics` — ( Optional) D is p l a y s f u n c t i on registry statistics.
- `Cisco IOS Software M o d u l a r it y Syntax` — ( Optional) D is p l a y s information about as p e c if i c registry.
- `name`
- `registry-name` — ( Optional) Name of the registry to e x a min e.
- `registry-number` — ( Optional) Number of the registry to e x a min e.
- `brief` — ( Optional) D is p l a y s limit e d f u n c t i on s and service s information.
- `p r e e m p t i on s` — ( Optional) D is p l a y s registry p r e e m p t i on s information.
- `r p c p status` — ( Optional) D is p l a y s status of remote p r o c e d u r e c all( R P C) p r o x y.
- `Cisco IOS Software Syntax`
- `statistics` — ( Optional) D is p l a y s f u n c t i on registry statistics.
- `remote` — ( Optional) D is p l a y s names e r v e r in t e r a c t i on s and c all statistics.
- `process` — ( Optional) D is p l a y s process-s p e c if i c information.
- `process-name` — ( Optional) Process name.
- `process-id` — ( Optional) Process ID. Number in range from1 to4294967295.

**Command Default:** If no options are specified, registry information is displayed for all registries.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | This command was introduced. |
| 12.2(18)SXF4 | Keywords and arguments were added to support Software M o d u l a r it y image s and this command was integrated into Cisco IOS Release12.2(18) S X F4. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

Example output varies between Cisco IOS software images and Cisco IOS Software Modularity software images. To view the appropriate output, choose one of the following sections: • Cisco IOS Software • Cisco IOS Software Modularity Cisco IOS Software The following is sample output from the show registry command using the brief keyword:

```text
Router# show registry atm 3/0/0 brief
Registry objects: 1799 bytes: 213412
--
Registry 23: ATM Registry
Service 23/0:
Service 23/1:
Service 23/2:
Service 23/3:
Service 23/4:
Service 23/5:
Service 23/6:
Service 23/7:
Service 23/8:
Service 23/9:
Service 23/10:
Service 23/11:
Service 23/12:
Service 23/13:
Service 23/14:
Registry 25: ATM routing Registry
Service 25/0:
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Registryobjects | Numberofobjectsintheregistry. |
| bytes | Registrysize,inbytes. |
| Registry | Displaysthespecifiedregistryservicenumberandtypeofregistryservice. |

Cisco IOS Software Modularity The following is partial sample output from the show registry command when running a software Modularity image:

```text
Router# show registry
Registry information for ios-base:1:
=====================================================
----------------------------
AAA_ACCOUNTING : 11 services
/ 1 : List list[000]
/ 2 : List list[000]
/ 3 : Case size[020] list[000] default=0x7267C5D0 returnd
/ 4 : Case size[020] list[000] default=0x7267C5D0 returnd
16 0x72779400
/ 5 : Case size[020] list[000] default=0x7267C5D0 returnd
/ 6 : Case size[020] list[000] default=0x7267C5D0 returnd
16 0x7277915C
/ 7 : Retval size[020] list[000] default=0x7267C5E4 returno
/ 8 : Retval size[020] list[000] default=0x7267C5E4 returno
/ 9 : Retval size[020] list[000] default=0x7267C5E4 returno
/ 10 : Stub 0x7267C5E4 return_zero
/ 11 : Stub 0x76545BA0
AAA_ACCOUNTING : 11 services, 140 global bytes, 160 heap bytes
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Registryinformation | Displaystheregistryinformationbyprocessname. |
| services | Numberofservicesdisplayed. |
| globalbytes | Numberofbytesfortheservice, |

| Field | Description |
| --- | --- |
| heapbytes | Sizeoftheserviceheap,inbytes, |


### `show reload`

> **Página:** 933 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the reload status on the router, use the show reload command in EXEC mode.

**Syntax:**

```text
show reload
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

You can use the show reload command to display a pending software reload. To cancel the reload, use the reload cancel privileged EXEC command.

**Example:**

The following sample output from the show reload command shows that a reload is schedule for 12:00 a.m. (midnight) on Saturday, April 20:

```text
Router# show reload
Reload scheduled for 00:00:00 PDT Sat April 20 (in 12 hours and 12 minutes)
```


### `show reload history`

> **Página:** 933 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the reason for the device reload and its history, use the show reload history command in privileged EXEC mode.

**Syntax:**

```text
show reload history
```

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 4000 | Series Integrated Services Routers, Cisco 1000 Series Integrated Services Routers, and Cisco ASR 1000 Series Aggregation Services Router . Cisco IOS XE This command was modified from show reload-history to show reload history. 17.14.1a This command is supported on Cisco Catalyst 8200, 8300, and 8500 Series Edge Platforms, Cisco Catalyst 8000V Edge Software, Cisco 4000 Series Integrated Services Routers, Cisco 1000 Series Integrated Services Routers, and Cisco ASR |
| 1000 | Series Aggregation Services Routers. |

**Usage Guidelines:**

You can use this command when you want to view the reload history details. Note This command displays the history for a maximum of 10 reloads. Example The following is sample output of the show reload-history command:

```text
Device#show reload-history
Reload History:
Reload Index: 1
Reload Code: Reload
Reload Description: Reload Command
Reload Severity: Normal Reboot
Reload Time: 01:33:44 UTC Wed Nov 30 2022
Reload Index: 2
Reload Code: Critical Process Fault
Reload Description: Critical process stack_mgr fault on rp_0_0 (rc=137), system report at
bootflash:core/Yang_Test-system-report_20221130-012929-UTC.tar.gz
Reload Severity: Abnormal Reboot
Reload Time: 01:31:11 UTC Wed Nov 30 2022
Reload Index: 3
Reload Code: Image Install
Reload Description: Image Install
Reload Severity: Normal Reboot
Reload Time: 01:25:03 UTC Wed Nov 30 2022
Reload Index: 4
Reload Code: Critical Process Fault
Reload Description: Critical process rif_mgr fault on rp_0_0 (rc=137), system report at
bootflash:core/Yang_Test-system-report_20221130-011127-UTC.tar.gz
Reload Severity: Abnormal Reboot
Reload Time: 01:13:08 UTC Wed Nov 30 2022
Reload Index: 5
Reload Code: Reload
Reload Description: Reload Command
Reload Severity: Normal Reboot
Reload Time: 01:08:26 UTC Wed Nov 30 2022
Reload Index: 6
Reload Code: Critical Process Fault
Reload Description: Critical process wncmgrd fault on rp_0_0 (rc=137), system report at
bootflash:core/Yang_Test-system-report_20221130-010338-UTC.tar.gz
Reload Severity: Abnormal Reboot
Reload Time: 01:05:23 UTC Wed Nov 30 2022
Reload Index: 7
Reload Code: Reload
Reload Description: Reload Command
Reload Severity: Normal Reboot
Reload Time: 01:01:09 UTC Wed Nov 30 2022
Reload Index: 8
Reload Code: Reload
Reload Description: Reload Command
Reload Severity: Normal Reboot
Reload Time: 00:57:27 UTC Wed Nov 30 2022
Reload Index: 9
Reload Code: Reload
Reload Description: Reload Command
Reload Severity: Normal Reboot
Reload Time: 00:22:34 UTC Wed Nov 30 2022
Reload Index: 10
Reload Code: Fast Switchover
Reload Description: redundancy force-switchover
Reload Severity: Normal Reboot
Reload Time: 23:40:01 UTC Tue Nov 29 2022
```

Note The show reload-history command is applicable to Cisco IOS XE 17.13.1a release. Example The following is sample output of the show reload history command:

```text
Device#show reload history
Reload History:
Unit ID: rp0
Reload Index: 1
Reload Code: Reload
Reload Severity: Normal Reboot
Reload Description: Reload Command
Crash Data: -NA-
HA Status: Active
Software Version: 17.15.20240201:182652101
Reload Time: 17:54:47 UTC Mon Feb 5 2024
```

Note The show reload history command is applicable to Cisco IOS XE 17.14.1a and later releases.


### `show resource-pool queue`

> **Página:** 936 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display resource pool and queue information about the router, use the show resource-pool queuecommand in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show resource-pool queue {description | statistics}
```

**Parameters (Syntax Description):**

- `statistics` — D is p l a y s information about the resource-pool queue statistics.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |

**Usage Guidelines:**

Use the show resource-pool queuecommand to display the resource pool and queue information on the router.

**Example:**

The following is sample output from the show resource-pool queue descriptioncommand. The field descriptions are self-explanatory.

```text
Router# show resource-pool description
Resource-management call state description
State Description
--------------------------- -----------
RM_DNIS_AUTHOR : Waiting for DNIS author
RM_DNIS_AUTH_SUCCEEDED : Waiting for resource alloc
RM_DNIS_RES_ALLOCATED : Call established
RM_DNIS_REQ_IDLE : Disc while in RM_DNIS_AUTHOR/RM_DNIS_AUTH_SUCCEEDED
/RM_DNIS_REQ_IDLE_AUTHOR
RM_DNIS_REQ_IDLE_AUTHOR : New call while in RM_DNIS_REQ_IDLE
RM_RPM_RES_AUTHOR : Waiting for RPM author
RM_RPM_RES_ALLOCATING : Waiting for resource alloc
RM_RPM_RES_ALLOCATED : RPM call established
RM_RPM_AUTH_REQ_IDLE : Disc while in RM_RPM_RES_AUTHOR
/RM_RPM_AUTH_REQ_IDLE_AUTHOR
RM_RPM_RES_REQ_IDLE : Disc while in RM_RPM_RES_ALLOCATING
/RM_RPM_RES_REQ_IDLE_AUTHOR
RM_RPM_AUTH_REQ_IDLE_AUTHOR: New call while in RM_RPM_AUTH_REQ_IDLE
RM_RPM_RES_REQ_IDLE_AUTHOR : New call while in RM_RPM_RES_REQ_IDLE
RM_RPM_DISCONNECTING : RPM initiates disconnect and is waiting for ack
RM_RPM_DISCONNECTING_AUTHOR: New call while in RM_RPM_DISCONNECTING
5400-XM-1#sh resource-pool queue stat
```

The following is sample output from the show resource-pool queue statisticscommand:

```text
Router# show resource-pool statistics
Resource-management event queue information (queue depth 0)
Event In queue Total
--------------------------- ---------- ----------
DIALER_INCALL : 0 0
DIALER_DISCON : 0 0
GUARDTIMER_EXPIRY_EVENT : 0 0
RM_DNIS_AUTHOR_SUCCESS : 0 0
RM_DNIS_AUTHOR_FAIL : 0 0
RM_DNIS_RES_ALLOC_SUCCESS : 0 0
RM_DNIS_RES_ALLOC_FAIL : 0 0
RM_DNIS_RPM_REQUEST : 0 0
RM_RPM_RES_AUTHOR_SUCCESS : 0 0
RM_RPM_RES_AUTHOR_FAIL : 0 0
RM_RPM_RES_ALLOC_SUCCESS : 0 0
RM_RPM_RES_ALLOC_FAIL : 0 0
RM_RPM_DISC_ACK : 0 0
--------------------------- ---------- ----------
SUM : 0 0
Resource-management call information (0 active calls)
State Active Total
--------------------------- ---------- ----------
RM_DNIS_AUTHOR : 0 0
RM_DNIS_AUTH_SUCCEEDED : 0 0
RM_DNIS_RES_ALLOCATED : 0 0
RM_DNIS_REQ_IDLE : 0 0
RM_DNIS_REQ_IDLE_AUTHOR : 0 0
RM_RPM_RES_AUTHOR : 0 0
RM_RPM_RES_ALLOCATING : 0 0
RM_RPM_RES_ALLOCATED : 0 0
RM_RPM_AUTH_REQ_IDLE : 0 0
RM_RPM_RES_REQ_IDLE : 0 0
RM_RPM_AUTH_REQ_IDLE_AUTHOR: 0 0
RM_RPM_RES_REQ_IDLE_AUTHOR : 0 0
RM_RPM_DISCONNECTING : 0 0
RM_RPM_DISCONNECTING_AUTHOR: 0 0
--------------------------- ---------- ----------
SUM : 0 0
00:03:34 since last clear command
Other resource-management info:
Active Processes 4
Throttle limit 4 (0 calls rejected)
Event queue depth 0 (peak 0)
Pending calls 0 (peak 0)
Buffer queue depth 648 (low watermark 648)
```


### `show rhosts`

> **Página:** 937 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about current remote hosts, use the show rhostscommand in privileged EXEC mode.

**Syntax:**

```text
show rhosts
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(22)T | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release12.4(22) T. |
| 12.2(33)SRC | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release12.2(33) S R C. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release12.2(33) S X I. |
| CiscoIOS2.1XE | This command was integrated into Cisco IOS X E Release2.1. |

**Example:**

The following is sample output from the show rhosts command.

```text
show rhosts
Local user Host/Access list Remote user
tcp-scale-mcp1 12 tcp-scale-mcp2
tcp-scale-mcp1 12 tcp-scale-3
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Localuser | Displaysthenameoftheuseronthelocalrouter.Thisnamegetscommunicatedtothe networkadministratorortotheuserontheremotesystem. |
| Host/Accesslist | DisplaysthenameortheIPaddressoftheremotehostfromwhichthelocalrouterwill acceptremotelyexecutedcommands. |
| Remoteuser | Displaysthenameoftheuserontheremotehostfromwhichtherouterwillacceptremotely executedcommands. |


### `show rom-monitor`

> **Página:** 938 · **Modo:** User EXEC (>) Privileged EXEC (#) Diagnostic (diag) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To show both the read-only and the upgrade ROM monitor (ROMMON) image versions and also the ROMMON image running on the Cisco 7200 VXR or Cisco 7301 router, use the show rom-monitorcommand in user EXEC, privileged EXEC, or diagnostic mode. Supported Platforms Other than the Cisco ASR1000 Series Routers Cisco ASR 1000 Series Routers

**Syntax:**

```text
show rom-monitor
show rom-monitor slot
```

**Parameters (Syntax Description):**

- `slot` — Specifies the slot that c on t a in s the ROMMON. Options include: • number--Then u m be r of the S IP slot that r e q u i r e s the ROMMON upgrade. • F0--E m be d d e d Service Processor slot0. • F1--E m be d d e d Service Processor slot1. • F P a c t i v e--A c t i v e E m be d d e d Service Processor. • F P s t and by--S s t and by E m be d d e d Service Processor. • R0--Route Processor slot0. • R1--Route Processor slot1. • R P a c t i v e--A c t i v e Route Processor. • R P s t and by--S t and by Route Processor.

**Command Modes:** User EXEC (>) Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(28)S | This command was introduced on the Cisco7200 V X R router. |
| 12.3(9) | This command was integrated into Cisco IOS Release12.3(9) and i m p l e m e n t e d onthe Cisco7301 router. |
| 12.3(8)T | This command was integrated into Cisco IOS Release12.3(8) T. |
| 12.2SX | This command is supported in the Cisco IOS Release12.2 S X t r a in. Support in a s p e c if i c12.2 S X release of this t r a in d e p end s on your f e at u reset, platform, and platform hardware. |
| CiscoIOSXERelease 2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers and the following e n h an c e m e n t s were introduced: • This command was introduced in diagnostic mode. The command can be enter e d in both privileged EXEC and diagnostic mode on the Cisco ASR1000 Series Routers. • The slot argument was introduced. |
| 15.0(1)M | The command was modified on Cisco1800 s e r i e s routers. The output of the command was modified to l e t you k no w that the u p g r a d a b l e ROMMON version is not v is i b l e d u e to the l i c e n s e a c t i v it y and reload isr e q u i r e d. |

**Usage Guidelines:**

Use the show rom-monitor command when the router boots a Cisco IOS software iamge. In this case, the device prompt will be something like “Router>”. Use the showmon command when the device boot to Rom Monitor mode instead of booting a Cisco IOS image. In this case, the device prompt will be something like “rommon n >” where "n" is a number. Note On Cisco 1800 series routers, the show rom-monitor command does not show the version of the upgradable ROMMON. To view the version of the upgradable ROMMON, you may need to reload the router while using the upgradable ROMMON image. If you are using the read-only ROMMON, then the upgradable ROMMON disappears. You need to run the upgrade rom-monitor file command for the upgradable ROMMON. Otherwise, the upgrade rom-monitor preference upgrade command is rejected with the message “No Upgrade ROMMON present, cannot select it.” During ROMMON bootup, if you are running upgradable ROMMON, then the ROMMON first displays the read-only ROMMON message, “Running new upgrade for first time.” This message is followed by the upgradable ROMMON message.

**Example:**

The following sample output from the show rom-monitor command, applicable to both the Cisco 7200 VXR and Cisco 7301 routers, displays both the ROMMON images and verifies that the upgrade ROMMON image is running:

```text
Router> show rom-monitor
ReadOnly ROMMON version:
System Bootstrap, Version 12.2(20031011:151758)
Copyright (c) 2004 by Cisco Systems, Inc.
Upgrade ROMMON version:
System Bootstrap, Version 12.2(20031011:151758)
Copyright (c) 2004 by Cisco Systems, Inc.
Currently running ROMMON from Upgrade region
ROMMON from Upgrade region is selected for next boot
The following is sample output from the show rom-monitor command in on Cisco 1800 series
routers. To view the version of the upgradable ROMMON, you may need to reload the router
while using the upgradable ROMMON image.
Router# show rom-monitor
ReadOnly ROMMON version:
System Bootstrap, Version 12.3(8r)YH3, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2005 by cisco Systems, Inc.
Upgrade ROMMON version is not visible due to recent license activity,
such as license installation, removal, or the use of evaluation license
Reload is required to show the upgrade ROMMON version
Currently running ROMMON from Upgrade region
ROMMON from Upgrade region is selected for next boot
Router# reload
Proceed with reload? [confirm]
*Apr 13 18:44:08.583: %SYS-5-RELOAD: Reload requested by console. Reload Reason: Reload
Command.
System Bootstrap, Version 12.3(8r)YH3, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2005 by cisco Systems, Inc.
Running new upgrade for first time
System Bootstrap, Version 12.3(8r)YH13, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2008 by cisco Systems, Inc.
C1800 platform with 262144 Kbytes of main memory with parity disabled
Upgrade ROMMON initialized
```

In the following example, the ROMMON image in RP 0 of a Cisco ASR 1006 router is verified using the show rom-monitor command:

```text
Router# show rom-monitor r0
System Bootstrap, Version 12.2(33r)XN1, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2007 by cisco Systems, Inc.
```

The fields in the examples are self-explanatory.


### `show rom-monitor slot`

> **Página:** 941 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the ROM monitor (ROMMON) status, use the show rom-monitor command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show rom-monitor slot num {sp | rp}
```

**Parameters (Syntax Description):**

- `num` — D is p l a y s the slot number of the ROMMON for which the status is to be d is p l a y e d.
- `sp` — D is p l a y s the ROMMON status of the switch processor.
- `rp` — D is p l a y s the ROMMON status of the route processor.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was integrated into Release 12.2(17d)SXB. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

When you enter the show rom-monitor slot command, the output displays the following: • Region region1 and region2--Displays the status of the ROMMON image and the order of preference from which the region1 or region2 images should be booted. The ROMMON image status values are as follows: • First run--Indicates that a check of the new image is being run. • Invalid--Indicates that the new image has been checked and the upgrade process has started. • Approved--Indicates that the ROMMON field upgrade process has completed. • Currently running--This field displays the currently running image and the region. The sp or rp keyword is required only if a supervisor engine is installed in the specified slot.

**Example:**

This example shows how to display ROMMON information:

```text
Router# show rom-monitor slot 1 sp
Region F1:APPROVED
Region F2:FIRST_RUN, preferred
Currently running ROMMON from F1 region
```


### `show running identity policy`

> **Página:** 942 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display identity policy information, use the show running identity policycommand in privileged EXEC mode.

**Syntax:**

```text
show running identity policy [name]
```

**Parameters (Syntax Description):**

- `name` — ( Optional) Name of the identity policy.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SX | This command was introduced. |

**Example:**

The following is output from the show running identity policy command:

```text
Router# show running identity policy
Building configuration...
Current configuration:
identity policy p1
access-group some-acl
identity policy p2
access-group another-acl
redirect url http://www.foo.com/bar.html match redirect-acl
end
```


### `show running identity profile`

> **Página:** 942 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display identity profile information, use the show running identity profilecommand in privileged EXEC mode.

**Syntax:**

```text
show running identity profile [default | dot1x | eapoudp]
```

**Parameters (Syntax Description):**

- `default` — ( Optional) D is p l a y s default identity profile information.
- `dot1x` — ( Optional) D is p l a y s802.1 x identity profile information.
- `eapoudp` — ( Optional) D is p l a y s EAPo UDP identity profile information.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SX | This command was introduced. |

**Example:**

The following is output from the show running identity profilecommand:

```text
Router# show running identity profile
Building configuration...
Current configuration:
identity profile default
device authorize type cisco ip phone
identity profile eapoudp
device authorize ip-address 10.0.0.0 255.0.0.0 policy p1
identity profile dot1x
device authorize mac-address 0001.0203.0405 ffff.ffff.ffff policy p2
end
```


### `show running-config`

> **Página:** 943 · **Modo:** Privileged EXEC (#) · **Default:** The default syntax, show running-config, displays the contents of the running configuration file, except commands configured using the default parameters. · **Leitura (show/clear/…):** sim

**Description:** To display the contents of the current running configuration file or the configuration for a specific module, Layer 2 VLAN, class map, interface, map class, policy map, or virtual circuit (VC) class, use the show running-config command in privileged EXEC mode.

**Syntax:**

```text
show running-config [options]
```

**Parameters (Syntax Description):**

- `options` — ( Optional) Keywords used to c u s to m i z e output. You can enter more than one keyword. • all--Expand s the output to include the commands that are configure d with default parameters. If the all keyword is not used, the output does not d is p l a y commands configure d with default parameters. • b r i e f--D is p l a y s the configuration with out c e r t if i c at i on data and e n c r y p t e d f i l t e r detail s. The b r i e f keyword can be used with the line n u m keyword. • class-map[ name][ line n u m]--D is p l a y s class map information. The line n u m keyword can be used with the class-map name option. • control-plane[ c e f-e x c e p t i on| host| t r an s it]--D is p l a y s control-plane information. The c e f-e x c e p t i on, host, and t r an s it keywords can be used with the control-plane option. • f low{ e x port e r| monitor| r e c or d}--D is p l a y s global f low configuration commands. The e x port e r, monitor, and r e c or d keywords can be used with the f low option. • full--D is p l a y s the full configuration. • interface type number --D is p l a y s interface-s p e c if i c configuration information. If you use the interface keyword, you must specify the interface type and the interface number( for example, interface e the r n e t0). Keywords for c o m m on interfaces include async, e the r n e t, fast E the r n e t, group-async, l o o p b a c k, n u l l, s e r i a l, and v i r t u a l-template. Use the show r u n interface ? command to d e t e r min e the interfaces a v a i l a b l e on your system. • line n u m--D is p l a y s linenumber s in the output. The b r i e for full keyword can be used with the line n u m keyword. The line n u m keyword can be used with the class-map, interface, map-class, policy-map, and v c-class keywords. • map-class [ at m| d i a l e r| f r a m e-r e l a y][ name][ line n u m]--D is p l a y s map class information. This option is describe d s e p a r at e l y; see the show running-config map-class command p age.
- `` — • partition type s--D is p l a y s the configuration c or r e s p on d in gt o apa r t it i on. The type s keyword can be used with the partition option. • policy-map [ name][ line n u m]--D is p l a y s policy map information. The line n u m keyword can be used with the policy-map name option. • v c-class [ name][ line n u m]--D is p l a y s V C-class information( the d is p l a y is a v a i l a b l e only on c e r t a in device s such as the Cisco7500 s e r i e s device s). The line n u m keyword can be used with the v c-class name option.
- `` — • v i e w full--Enable s the d is p l a y of a full running configuration. This is for v i e w-b as e d users who t y p i c all y can only v i e w the configuration commands that they are e n title d to access for that p a r t i c u l a r v i e w. •vrf name--D is p l a y s the V i r t u a l r out in g and for w a r d in g( VRF)-a w are configuration module number. •vlan [ vlan-id]--D is p l a y s the s p e c if i c VLAN information; v a l id values are from1 to4094.

**Command Default:** The default syntax, show running-config, displays the contents of the running configuration file, except commands configured using the default parameters.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | This command was introduced. |
| 12.0 | This command was replaced by the more system: running-config command. |
| 12.0(1)T | This command was integrated into Cisco IOS Release12.0(1) T, and the output m o d if i e r(\|) was added. |
| 12.2(4)T | This command was modified. The line n u m keyword was added. |
| 12.3(8)T | This command was modified. The v i e w full option was added. |
| 12.2(14)SX | This command was integrated into Cisco IOS Release12.2(14) S X. The module number and vlan vlan-id keywords and arguments were added for the Supervisor E n g in e720. |
| 12.2(17d)SXB | This command was integrated into Release12.2(17 d) S X B and i m p l e m e n t e do n the Supervisor Engine2. |
| 12.2(33)SXH | This command was modified. The all keyword was added. |
| 12.2(31)SB2 | This command was integrated into Cisco IOS Release12.2(31) S B2. This command was e n h an c e d to d is p l a y the configuration information for traffic s h ap in g over h e a d accounting for AT M and was i m p l e m e n t e do n the Cisco10000 s e r i e s device for the PRE3. |
| 12.2(33)SRC | This command was integrated into Cisco IOS Release12.2(33) S R C. |
| 12.2(33)SB | This command was modified. Support for the Cisco7300 s e r i e s device was added. |
| 12.4(24)T | This command was modified in are l e as e e a r l i e r than Cisco IOS Release12.4(24) T. The partition and vrf keywords were added. The module and vlan keywords were removed. |
| 15.0(1)M | This command was modified. The output was modified to include e n c r y p t e d f i l t e r information. |
| 12.2(33)SXI | This command was modified. The output was modified to d is p l a y Access Control List(ACL) information. |

**Usage Guidelines:**

The show running-config command is technically a command alias (substitute or replacement syntax) of the more system:running-config command. Although the use of more commands is recommended (because of their uniform structure across platforms and their expandable syntax), the show running-config command remains enabled to accommodate its widespread use, and to allow typing shortcuts such as show run. The show running-config interface command is useful when there are multiple interfaces and you want to look at the configuration of a specific interface. The linenum keyword causes line numbers to be displayed in the output. This option is useful for identifying a particular portion of a very large configuration. You can enter additional output modifiers in the command syntax by including a pipe character (|) after the optional keyword. For example, show running-config interface serial 2/1 linenum | begin 3. To display the output modifiers that are available for a keyword, enter | ? after the keyword. Depending on the platform you are using, the keywords and the arguments for the options argument may vary. Prior to Cisco IOS Release 12.2(33)SXH, the show running-configcommand output omitted configuration commands set with default values. Effective with Cisco IOS Release 12.2(33)SXH, the show running-config all command displays complete configuration information, including the default settings and values. For example, if the Cisco Discovery Protocol (abbreviated as CDP in the output) hold-time value is set to its default of 180: • The show running-config command does not display this value. • The show running-config all displays the following output: cdp holdtime 180. If the Cisco Discovery Protocol holdtime is changed to a nondefault value (for example, 100), the output of the show running-config and show running-config allcommands is the same; that is, the configured parameter is displayed. Note In Cisco IOS Release 12.2(33)SXH, the allkeyword expands the output to include some of the commands that are configured with default values. In subsequent Cisco IOS releases, additional configuration commands that are configured with default values will be added to the output of the show running-config allcommand. Effective with Cisco IOS Release 12.2(33)SXI, the show running-config command displays ACL information. To exclude ACL information from the output, use the show running | section exclude ip access | access listcommand. Cisco 7600 Series Device In some cases, you might see a difference in the duplex mode that is displayed between the show interfaces command and the show running-config command. The duplex mode that is displayed in the show interfaces command is the actual duplex mode that the interface is running. The show interfaces command displays the operating mode of an interface, and the show running-config command displays the configured mode of the interface. The show running-config command output for an interface might display the duplex mode but no configuration for the speed. This output indicates that the interface speed is configured as auto and that the duplex mode that is displayed becomes the operational setting once the speed is configured to something other than auto. With this configuration, it is possible that the operating duplex mode for that interface does not match the duplex mode that is displayed with the show running-config command.

**Example:**

The following example shows the configuration for serial interface 1. The fields are self-explanatory.

```text
Device# show running-config interface serial 1
Building configuration...
Current configuration:
!
interface Serial1
no ip address
no ip directed-broadcast
no ip route-cache
no ip mroute-cache
shutdown
end
```

The following example shows the configuration for Ethernet interface 0/0. Line numbers are displayed in the output. The fields are self-explanatory.

```text
Device# show running-config interface ethernet 0/0 linenum
Building configuration...
Current configuration : 104 bytes
1 : !
2 : interface Ethernet0/0
3 : ip address 10.4.2.63 255.255.255.0
4 : no ip route-cache
5 : no ip mroute-cache
6 : end
```

The following example shows how to set line numbers in the command output and then use the output modifier to start the display at line 10. The fields are self-explanatory.

```text
Device# show running-config linenum | begin 10
10 : boot-start-marker
11 : boot-end-marker
12 : !
13 : no logging buffered
14 : enable password #####
15 : !
16 : spe 1/0 1/7
17 : firmware location bootflash:mica-modem-pw.172.16.0.0.bin
18 : !
19 : !
20 : resource-pool disable
21 : !
22 : no aaa new-model
23 : ip subnet-zero
24 : ip domain name cisco.com
25 : ip name-server 172.16.11.48
26 : ip name-server 172.16.2.133
27 : !
28 : !
29 : isdn switch-type primary-5ess
30 : !
126 : end
```

The following example shows how to display the module and status configuration for all modules on a Cisco 7600 series device. The fields are self-explanatory.

```text
Device#
show running-config
Building configuration...
Current configuration:
!
version 12.0
service timestamps debug datetime localtime
service timestamps log datetime localtime
no service password-encryption
!
hostname device
!
boot buffersize 126968
boot system flash slot0:7600r
boot bootldr bootflash:c6msfc-boot-mz.120-6.5T.XE1.0.83.bin
enable password lab
!
clock timezone Pacific -8
clock summer-time Daylight recurring
redundancy
main-cpu
auto-sync standard
!
ip subnet-zero
!
ip multicast-routing
ip dvmrp route-limit 20000
ip cef
mls flow ip destination
mls flow ipx destination
cns event-service server
!
spanning-tree portfast bpdu-guard
spanning-tree uplinkfast
spanning-tree vlan 200 forward-time 21
port-channel load-balance sdip
!
!
!
shutdown
!
!
```

In the following sample output from the show running-config command, the shape averagecommand indicates that the traffic shaping overhead accounting for ATM is enabled. The BRAS-DSLAM encapsulation type is qinq and the subscriber line encapsulation type is snap-rbe based on the ATM adaptation layer 5 (AAL5) service. The fields are self-explanatory

```text
Device# show running-config
subscriber policy recording rules limit 64
no mpls traffic-eng auto-bw timers frequency 0
call rsvp-sync
!
controller T1 2/0
framing sf
linecode ami
!
controller T1 2/1
framing sf
linecode ami
!
!
policy-map unit-test
class class-default
shape average percent 10 account qinq aal5 snap-rbe
!
```

The following is sample output from the show running-config class-map command. The fields in the display are self-explanatory.

```text
Device# show running-config class-map
Building configuration...
Current configuration : 2910 bytes
!
class-map type stack match-all ip_tcp_stack
match field IP protocol eq 0x6 next TCP
class-map type access-control match-all my
match field UDP dest-port eq 1111
match encrypted
filter-version 0.1, Dummy Filter 2
filter-id 123
filter-hash DE0EB7D3C4AFDD990038174A472E4789
algorithm aes256cbc
cipherkey realm-cisco.sym
ciphervalue #
oeahb4L6JK+XuC0q8k9AqXvBeQWzVfdg8WV67WEXbiWdXGQs6BEXqQeb4Pfow570zM4eDw0gxlp/Er8w
/lXsmolSgYpYuxFMYb1KX/H2iCXvA76VX7w5TElb/+6ekgbfP/d5ms6DEzKa8DlOpl+Q95lP194PsIlU
wCyfVCwLS+T8p3RDLi8dKBgQMcDW4Dha1ObBJTpV4zpwhEdMvJDu5PATtEQhFjhN/UYeyQiPRthjbkJn
LzT8hQFxwYwVW8PCjkyqEwYrr+R+mFG/C7tFRiooaW9MU9PCpFd95FARvlU=#
exit
class-map type stack match-all ip_udp_stack
match field IP protocol eq 0x11 next UDP
class-map type access-control match-all psirt1
match encrypted
filter-version 0.0_DummyVersion_20090101_1830
filter-id cisco-sa-20090101-dummy_ddts_001
filter-hash FC50BED10521002B8A170F29AF059C53
algorithm aes256cbc
cipherkey realm-cisco.sym
ciphervalue #
DkGbVq0FPAsVJKguU15lQPDfZyTcHUXWsj8+tD+dCSYW9cjkRU9jyST4vO4u69/L62QlbyQuKdyQmb10
6sAeY5vDsDfDV05k4o5eD+j8cMt78iZT0Qg7uGiBSYBbak3kKn/5w2gDd1vnivyQ7g4Ltd9+XM+GP6XL
27RrXeP5A5iGbzC7KI9t6riZXk0gmR/vFw1a5wck0D/iQHIlFa/yRPoKMSFlqfIlLTe5NM7JArSTKET2
pu7wZammTz4FF6rY#
exit
match start TCP payload-start offset 0 size 10 regex "abc.*def"
match field TCP source-port eq 1234
class-map type access-control match-all psirt2
match encrypted
filter-version 0.0_DummyVersion_20090711_1830
filter-id cisco-sa-20090711-dummy_ddts_002
filter-hash DE0EB7D3C4AFDD990038174A472E4789
algorithm aes256cbc
cipherkey realm-cisco.sym
```

The following example shows that the teletype (tty) line 2 is reserved for communicating with the 2nd core:

```text
Device# show running
Building configuration...
Current configuration:
!
version 12.0
service timestamps debug uptime
service timestamps log uptime
no service password-encryption
!
hostname device
!
enable password lab
!
no ip subnet-zero
!
!
!
interface Ethernet0
ip address 172.25.213.150 255.255.255.128
no ip directed-broadcast
no logging event link-status
!
interface Serial0
no ip address
no ip directed-broadcast
no ip mroute-cache
shutdown
no fair-queue
!
interface Serial1
no ip address
no ip directed-broadcast
shutdown
!
ip default-gateway 172.25.213.129
ip classless
ip route 0.0.0.0 0.0.0.0 172.25.213.129
!
!
line con 0
transport input none
line 1 6
no exec
transport input all
line 7
no exec
exec-timeout 300 0
transport input all
line 8 9
no exec
transport input all
line 10
no exec
transport input all
stopbits 1
line 11 12
no exec
transport input all
line 13
no exec
transport input all
speed 115200
line 14 16
no exec
transport input all
line aux 0
line vty 0 4
password cisco
login
!
end
```


### `show running-config control-plane`

> **Página:** 951 · **Modo:** Privileged EXEC (#) · **Default:** If no keyword is specified, all information about the control plane is displayed. · **Leitura (show/clear/…):** sim

**Description:** To display the control plane information for the running configuration, use the show running-config control-plane command in privileged EXEC mode.

**Syntax:**

```text
show running-config control-plane [cef-exception | host | transit]
```

**Parameters (Syntax Description):**

- `cef-exception` — ( Optional) D is p l a y s information about control plane Cisco Express For w a r d in g e x c e p t i on s.
- `host` — ( Optional) D is p l a y s information about the control plane host.
- `transit` — ( Optional) D is p l a y s information about control plane t r an s it.

**Command Default:** If no keyword is specified, all information about the control plane is displayed.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(24)T | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release12.4(24) T. |

**Example:**

The following is sample output from the show running-config control-plane command. The field descriptions are self-explanatory.

```text
show running-config control-plane
Building configuration...
Current configuration : 14 bytes
!
control-plane
!
end
```


### `show running-config map-class`

> **Página:** 952 · **Modo:** Privileged EXEC · **Default:** Displays all map-class configuration in the running configuration file. · **Leitura (show/clear/…):** sim

**Description:** To display only map-class configuration information from the running configuration file, use the show command in privileged EXEC mode. running-config map-class

**Syntax:**

```text
show running-config map-class [atm [map-class-name] | dialer [map-class-name] | frame-relay
[map-class-name]] [linenum]
```

**Parameters (Syntax Description):**

- `atm` — ( Optional) D is p l a y s only AT M map-class configuration lines.
- `dialer` — ( Optional) D is p l a y s only d i a l e r map-class configuration lines.
- `frame-relay` — ( Optional) D is p l a y s only Frame R e l a y map-class configuration lines.
- `map-class-name` — ( Optional) D is p l a y s only configuration lines for the specified map-class.
- `linenum` — ( Optional) D is p l a y s linenumber s in the output.

**Command Default:** Displays all map-class configuration in the running configuration file.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.1 | The map-class e x t e n s i onto the show running-config command was introduced to show only lines p e r t a in in gt o d i a l e r or Frame R e l a y map class e s. |
| 12.1(2)T | The at m, d i a l e r, and f r a m e-r e l a y keywords and map-class-name argument were introduced. |
| 12.2(4)T | The line n u m keyword was added. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use the show running-config map-class command to display the following information from the running configuration file: • All map classes configured on the router. • Map classes configured specifically for ATM, Frame Relay, or dialer. • A specific ATM, Frame Relay, or dialer map class. Use the linenum keyword to display line numbers in the output. This option is useful for identifying a particular portion of a very large configuration.

**Example:**

All Map Classes Configured on the Router Example The following example displays all map classes configured on the router:

```text
show running-config map-class
Building configuration...
Current configuration:
!
map-class frame-relay cir60
frame-relay bc 16000
frame-relay adaptive-shaping becn
!
map-class frame-relay cir70
no frame-relay adaptive-shaping
frame-relay priority-group 2
!
map-class atm vc100
atm aal5mux
!
map-class dialer dialer1
dialer idle-timeout 10
end
```

All Frame Relay Map Classes Example The following example displays all Frame Relay map classes on the router:

```text
Router# show running-config map-class frame-relay
Building configuration...
Current configuration:
!
map-class frame-relay cir60
frame-relay bc 16000
frame-relay adaptive-shaping becn
!
map-class frame-relay cir70
no frame-relay adaptive-shaping
frame-relay priority-group 2
end
```

A Specific Map Class and Display of Line Numbers Example The following example displays a specific map class called class1. Line numbers are displayed in the output.

```text
show running-config map-class frame-relay class1 linenum
Building configuration...
Current configuration:
1 : !
2 : map-class frame-relay boy
3 : no frame-relay adaptive-shaping
4 : frame-relay cir 1000
5 : end
```


### `show running-config partition`

> **Página:** 954 · **Modo:** Privileged EXEC (#) · **Default:** None · **Leitura (show/clear/…):** sim

**Description:** To display the list of commands that make up the current running configuration for a specific part of the system’s global running configuration, use the show running-config partition command in privileged EXEC mode.

**Syntax:**

```text
show running-config partition part
```

**Parameters (Syntax Description):**

- `part` — The p a r tar g u m e n t will c on s is to f one or more keyword options. These keywords r e p r e s e n t apa r t it i on of the system’ s running configuration state, as a m a j or-d e s c r ip to r and, in some c as e s, one or more min or-descriptors. For example, in the commands how running-config partition router e i grp1, the m a j or-d e s c r ip to r for the p a r tar g u m e n t is the router keyword, and the min or-descriptors for the p a r tar g u m e n tar e the e i grp1 keywords. The a c t u all is to f p a r t keyword options will d e p end on your system hardware, what f e at u reset you are running, and what f e at u r e s are current l y configure do n your system. Some examples of command p a r t keyword options are p r o v id e d h e r e for r e f e r e n c e. Use the show running-config partition? command on your system to v i e w the list of command options a v a i l a b l e on your system. • access-list--D is p l a y s all running configuration commands that make u p the access-list configuration partition. • boot--D is p l a y s all running configuration commands that make u p the boot configuration partition. • class-map--D is p l a y s all running configuration commands that make u p the class-map configuration partition. • global-cd p--D is p l a y s all running configuration commands that make u p the global CDP configuration partition. • interface [ type slot/ port/ number]--D is p l a y s all running configuration commands that make u p the interfaces configuration partition or the configuration commands that are ap p l i e d to the specified interface. • line--D is p l a y s all running configuration commands that make u p the line command configuration partition. • policy-map--D is p l a y s all running configuration commands that make u p the policy-map configuration partition. • route-map--D is p l a y s all running configuration commands that make u p the route-map configuration partition. •router [ p r o to c o l]--D is p l a y s all running configuration commands that make u p the router configuration partition, or the configuration commands for the specified r out in g p r o to c o l. • service--D is p l a y s all running configuration commands that make u p these r v i c e s( small server) configuration partition. • s n m p--D is p l a y s all running configuration commands that make u p the S N M P configuration partition. •|- All o w s for the a d d it i on of output m o d if i e r s.

**Command Default:** None

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRB | This command was introduced for Cisco7600 s e r i e s image s in Cisco IOS Release12.2 S R as p a r to f the“ Configuration Partition in g” f e at u r e. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |

**Usage Guidelines:**

When the Configuration Partitioning feature is enabled, the system groups the configuration state of the device into parts (called “partitions”) for the purpose of generating the virtual running configuration file (the list of configuration commands). The selective processing of the system’s configuration state for the purpose of generating a partial running configuration is called “configuration partitioning.” Note This command is not related to hard drive or flash drive partitioning. This granular access to configuration information offers important performance benefits for high-end routing platforms with very large configuration files, as the system wide generation of a complete virtual configuration file from all components on systems with large and complex configurations can become overly resource intensive and be unacceptably slow. The show running-config partition command allows you to display only the part of the running configuration that you want to examine, while also allowing the system to process only the collection of system components (such as specific interfaces) that you need to display. This is in contrast to other existing extensions to the show running-config command, which only filter the generated list after all system components have been processed. The Configuration Partitioning feature is enabled by default in Cisco IOS software images that support the feature. To disable the feature, use the no parser config partition command.

**Example:**

In the following example, the system generates a view of the running configuration by polling only the components associated with the access-list parts of the running configuration state, and then displays only those access-list-related configuration commands.

```text
Router# show running-config partition access-list
Building configuration...
Current configuration : 127 bytes
!
Configuration of Partition access-list
!
access-list 90 permit 0.0.0.0 1.2.3.5
access-list 100 permit 10 any any
!
end
```

In the following example, only the main configuration partition associated with the interface configuration is queried, and only the configuration commands associated with Fast Ethernet interface 0/1 are displayed.

```text
Router# show running-config partition interface fastethernet0/1
Building configuration...
Current configuration : 213 bytes
!
Configuration of Partition interface FastEthernet0/1
!
!
interface FastEthernet0/1
ip address 10.4.2.39 255.255.255.0
no ip route-cache cef
no ip route-cache
duplex half
ipv6 enable
no cdp enable
!
!
end
```


### `show scp`

> **Página:** 957 · **Modo:** Privileged EXEC on the Switch Processor · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display Switch-Module Configuration Protocol (SCP) information, use the show scp in privileged EXEC mode on the Switch Processor.

**Syntax:**

```text
show scp {accounting | counters | linecards [details] | mcast {group group-id | inst} | process id |
status}
```

**Parameters (Syntax Description):**

- `accounting` — D is p l a y s information about the SCP accounting.
- `counters` — D is p l a y s information about the SCP count e r.
- `line card s` — D is p l a y s information about the Optical Service s Module( O S M) w id e are an e two r k ( W AN) module s in the c has s is.
- `details` — ( Optional) D is p l a y s detailed information about the O S M W AN module.
- `mcast` — D is p l a y s information about the SCP m u l t i c as t.
- `group group-id` — ( Optional) D is p l a y s information for as p e c if i c group and group ID; v a l id values are from 1to127.
- `inst` — ( Optional) D is p l a y s information for an in s t an c e.
- `process id` — D is p l a y s all the processes that have register e d an SAPwith SCP.
- `status` — D is p l a y s information about the l o c a l SCP servers t at u s.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC on the Switch Processor

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(18)SXE | The output of the shows c p process command was changed to d is p l a y all the processes that have register e d an SAPwith SCP on the Supervisor E n g in e720 only. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 15.0(1)S | The output of the shows c p status command was changed to a d d it i on all y d is p l a y the Flow Control State( F C-State) and the Flow Control Count( F C-Count) |

**Example:**

This example displays the SCP flow control status:

```text
Router# show scp status
Rx 185, Tx 181, scp_my_addr 0x14
Id Sap Channel name current/peak/retry/dropped/totaltime(queue/process/ack) FC-state
FC-count
-------------------------------------------------------------- --------- ---- -------
0 18 SCP Unsolicited:18 801/ 0/ 0/ 0/ 0 0/ 0/ 0 off 0
1 80 SCP Unsolicited:80 0/ 0/ 0/ 0/ 0 0/ 0/ 0 off 0
2 23 SCP async: LCP#5 0/ 0/ 0/ 0/ 0 0/ 0/ 0 off 0
3 0 SCP Unsolicited:0 0/ 1/ 0/ 0/ 5 0/ 0/ 0 off 0
```

-------------------------------------------------------------------------------------------------------------------------- FC-state indicates the flow control state and FC-count indicates the number of times flow control has been turned on. This example shows how to display all the processes that have registered an SAP with SCP:

```text
show module
Mod Ports Card Type Model Serial No.
--- ----- -------------------------------------- ------------------ -----------
1 48 48-port 10/100 mb RJ45 WS-X6148-RJ-45 SAL091800RY
2 0 2 port adapter Enhanced FlexWAN WS-X6582-2PA JAE0940MH7Z
3 8 8 port 1000mb GBIC Enhanced QoS WS-X6408A-GBIC SAL09391KZH
5 2 Supervisor Engine 720 (Active) WS-SUP720-3BXL SAL09337UE6
6 2 Supervisor Engine 720 (Hot) WS-SUP720-3BXL SAL09148P59
Mod MAC addresses Hw Fw Sw Status
--- ---------------------------------- ------ ------------ ------------ -------
1 0013.c3f8.d2c4 to 0013.c3f8.d2f3 5.0 8.3(1) 8.6(0.366)TA Ok
2 0015.2bc3.5b40 to 0015.2bc3.5b7f 2.1 12.2(nightly 12.2(nightly Ok
3 0015.6324.ed48 to 0015.6324.ed4f 3.1 5.4(2) 8.6(0.366)TA Ok
5 0014.a97d.b0ac to 0014.a97d.b0af 4.3 8.4(2) 12.2(nightly Ok
6 0013.7f0d.0660 to 0013.7f0d.0663 4.3 8.4(2) 12.2(nightly Ok
Mod Sub-Module Model Serial Hw Status
---- --------------------------- ------------------ ----------- ------- -------
5 Policy Feature Card 3 WS-F6K-PFC3BXL SAL09337NVE 1.6 Ok
5 MSFC3 Daughterboard WS-SUP720 SAL09327AU6 2.3 Ok
6 Policy Feature Card 3 WS-F6K-PFC3BXL SAL1033Y0YK 1.8 Ok
6 MSFC3 Daughterboard WS-SUP720 SAL09158XB3 2.3 Ok
Mod Online Diag Status
---- -------------------
1 Pass
2 Pass
3 Pass
5 Pass
6 Pass
Router# attach 5
Trying Switch ...
Entering CONSOLE for Switch
Type "^C^C^C" to end this session
Switch-sp#
show scp process
Sap Pid Name
=== === ====
0 180 CWAN-RP SCP Input Process
18 42 itasca
20 3 Exec
21 3 Exec
22 180 CWAN-RP SCP Input Process
Total number of SAP registered = 5
```


### `show slot`

> **Página:** 959 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the PCMCIA flash memory cards file system, use the show slotcommand in user EXEC or privileged EXEC mode. [ | | | | ]

**Syntax:**

```text
show slot all chips detailed err summary
```

**Parameters (Syntax Description):**

- `all` — ( Optional) D is p l a y s all p o s s i b l e flash system information for all PCM C I A flash card s in the system.
- `chips` — ( Optional) D is p l a y s flash c h ip information.
- `detailed` — ( Optional) D is p l a y s the flash detailed directory.
- `err` — ( Optional) D is p l a y s the flash c h ip erase and write retries.
- `summary` — ( Optional) D is p l a y s the flash partition summary.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0 | This command was introduced. |

**Usage Guidelines:**

Use the show slot command to display details about the files in a particular linear PCMCIA flash memory card of less than 20 MB and some 32 MB linear PCMCIA cards. Note Use the show disk command for ATA PCMCIA cards. Other forms of this commands are show disk0: and show disk1:. For more information regarding file systems and flash cards, access the PCMCIA Filesystem Compatibility Matrix and Filesystem Information document at the following URL: http://www.cisco.com/en/US/partner/products/hw/routers/ps341/products_tech_note09186a00800a7515.shtml To see which flash cards are used in your router, use the show version command and look at the bottom portion of the output. The following display indicates an ATA PCMCIA flash disk.

```text
show version
46976K bytes of ATA PCMCIA card at slot 0 (Sector size 512 bytes).
```

The following display indicates a linear PCMCIA flash card with 20480K bytes of flash memory in card at slot 1 with a sector size of 128K.

```text
Router# show version
20480K bytes of Flash PCMCIA card at slot 1 (Sector size 128K).
```

Note In some cases the show slot command will not display the file systems, use show slot0: or show slot1:.

**Example:**

The following example displays information about slot 0. The output is self-explanatory.

```text
Router# show slot
PCMCIA Slot0 flash directory:
File Length Name/status
1 11081464 c3660-bin-mz.123-9.3.PI5b
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
```

The following example shows all possible flash system information for all PCMCIA flash cards in the system.

```text
Router# show slot all
Partition Size Used Free Bank-Size State Copy Mode
1 20223K 10821K 9402K 4096K Read/Write Direct
PCMCIA Slot0 flash directory:
File Length Name/status
addr fcksum ccksum
1 11081464 c3660-bin-mz.123-9.3.PI5b
0x40 0x5EA3 0x5EA3
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Chip Bank Code Size Name
1 1 89A0 2048KB INTEL 28F016SA
2 1 89A0 2048KB INTEL 28F016SA
1 2 89A0 2048KB INTEL 28F016SA
2 2 89A0 2048KB INTEL 28F016SA
1 3 89A0 2048KB INTEL 28F016SA
2 3 89A0 2048KB INTEL 28F016SA
1 4 89A0 2048KB INTEL 28F016SA
2 4 89A0 2048KB INTEL 28F016SA
1 5 89A0 2048KB INTEL 28F016SA
2 5 89A0 2048KB INTEL 28F016SA
The following example shows flash chip information
Router# show slot chips
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Chip Bank Code Size Name
1 1 89A0 2048KB INTEL 28F016SA
2 1 89A0 2048KB INTEL 28F016SA
1 2 89A0 2048KB INTEL 28F016SA
2 2 89A0 2048KB INTEL 28F016SA
1 3 89A0 2048KB INTEL 28F016SA
2 3 89A0 2048KB INTEL 28F016SA
1 4 89A0 2048KB INTEL 28F016SA
2 4 89A0 2048KB INTEL 28F016SA
1 5 89A0 2048KB INTEL 28F016SA
2 5 89A0 2048KB INTEL 28F016SA
```

The following example show the flash detailed directory.

```text
show slot detailed
PCMCIA Slot0 flash directory:
File Length Name/status
addr fcksum ccksum
1 11081464 c3660-bin-mz.123-9.3.PI5b
0x40 0x5EA3 0x5EA3
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
```

The following example shows the flash chip erase and write retries.

```text
Router# show slot err
PCMCIA Slot0 flash directory:
File Length Name/status
1 11081464 c3660-bin-mz.123-9.3.PI5b
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Chip Bank Code Size Name erase write
1 1 89A0 2048KB INTEL 28F016SA 0 0
2 1 89A0 2048KB INTEL 28F016SA 0 0
1 2 89A0 2048KB INTEL 28F016SA 0 0
2 2 89A0 2048KB INTEL 28F016SA 0 0
1 3 89A0 2048KB INTEL 28F016SA 0 0
2 3 89A0 2048KB INTEL 28F016SA 0 0
1 4 89A0 2048KB INTEL 28F016SA 0 0
2 4 89A0 2048KB INTEL 28F016SA 0 0
1 5 89A0 2048KB INTEL 28F016SA 0 0
2 5 89A0 2048KB INTEL 28F016SA 0 0
```

The following example shows the flash partition summary.

```text
Router# show
slot summary
Partition Size Used Free Bank-Size State Copy Mode
1 20223K 10821K 9402K 4096K Read/Write Direct
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
```


### `show slot0:`

> **Página:** 962 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the PCMCIA flash memory card’s file system located in slot 0, use the show slot0:command in user EXEC or privileged EXEC mode. show slot0:[all | chips | detailed | err | summary]

**Parameters (Syntax Description):**

- `all` — ( Optional) D is p l a y s all p o s s i b l e flash system information for all PCM C I A flash card s in the system.
- `chips` — ( Optional) D is p l a y s flash c h ip information.
- `detailed` — ( Optional) D is p l a y s the flash detailed directory.
- `err` — ( Optional) D is p l a y s the flash c h ip erase and write retries.
- `summary` — ( Optional) D is p l a y s the flash partition summary.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0 | This command was introduced. |
| 12.2SX | This command is supported in the Cisco IOS Release12.2 S X t r a in. Support in as p e c if i c12.2 S X release of this t r a in d e p end s on your f e at u reset, platform, and platform hardware. |

**Usage Guidelines:**

Use the show slot0: command to display details about the files in a particular linear PCMCIA flash memory card of less than 20 MB and some 32 MB linear PCMCIA cards. Note Use the show disk command for ATA PCMCIA cards. Other forms of this commands are show disk0: and show disk1:. For more information regarding file systems and flash cards, access the PCMCIA Filesystem Compatibility Matrix and Filesystem Information document at the following URL: http://www.cisco.com/en/US/partner/products/hw/routers/ps341/products_tech_note09186a00800a7515.shtml To see which flash cards are used in your router, use the show version command and look at the bottom portion of the output. The following display indicates an ATA PCMCIA flash disk.

```text
Router# show version
46976K bytes of ATA PCMCIA card at slot 0 (Sector size 512 bytes).
```

The following display indicates a linear PCMCIA flash card with 20480K bytes of flash memory in card at slot 1 with a sector size of 128K.

```text
Router# show version
20480K bytes of Flash PCMCIA card at slot 1 (Sector size 128K).
```

Note In some cases the show slot command will not display the file systems, use show slot0: or show slot1:.

**Example:**

The following example displays information about slot 0. The output is self-explanatory.

```text
Router# show slot0:
PCMCIA Slot0 flash directory:
File Length Name/status
1 11081464 c3660-bin-mz.123-9.3.PI5b
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Router# show slot0: all
Partition Size Used Free Bank-Size State Copy Mode
1 20223K 10821K 9402K 4096K Read/Write Direct
PCMCIA Slot0 flash directory:
File Length Name/status
addr fcksum ccksum
1 11081464 c3660-bin-mz.123-9.3.PI5b
0x40 0x5EA3 0x5EA3
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Chip Bank Code Size Name
1 1 89A0 2048KB INTEL 28F016SA
2 1 89A0 2048KB INTEL 28F016SA
1 2 89A0 2048KB INTEL 28F016SA
2 2 89A0 2048KB INTEL 28F016SA
1 3 89A0 2048KB INTEL 28F016SA
2 3 89A0 2048KB INTEL 28F016SA
1 4 89A0 2048KB INTEL 28F016SA
2 4 89A0 2048KB INTEL 28F016SA
1 5 89A0 2048KB INTEL 28F016SA
2 5 89A0 2048KB INTEL 28F016SA
The following example shows flash chip information.
Router# show slot0: chips
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Chip Bank Code Size Name
1 1 89A0 2048KB INTEL 28F016SA
2 1 89A0 2048KB INTEL 28F016SA
1 2 89A0 2048KB INTEL 28F016SA
2 2 89A0 2048KB INTEL 28F016SA
1 3 89A0 2048KB INTEL 28F016SA
2 3 89A0 2048KB INTEL 28F016SA
1 4 89A0 2048KB INTEL 28F016SA
2 4 89A0 2048KB INTEL 28F016SA
1 5 89A0 2048KB INTEL 28F016SA
2 5 89A0 2048KB INTEL 28F016SA
```

The following example show the flash detailed directory.

```text
Router# show slot0: detailed
PCMCIA Slot0 flash directory:
File Length Name/status
addr fcksum ccksum
1 11081464 c3660-bin-mz.123-9.3.PI5b
0x40 0x5EA3 0x5EA3
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
```

The following example shows the flash chip erase and write retries.

```text
Router# show slot0: err
PCMCIA Slot0 flash directory:
File Length Name/status
1 11081464 c3660-bin-mz.123-9.3.PI5b
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Chip Bank Code Size Name erase write
1 1 89A0 2048KB INTEL 28F016SA 0 0
2 1 89A0 2048KB INTEL 28F016SA 0 0
1 2 89A0 2048KB INTEL 28F016SA 0 0
2 2 89A0 2048KB INTEL 28F016SA 0 0
1 3 89A0 2048KB INTEL 28F016SA 0 0
2 3 89A0 2048KB INTEL 28F016SA 0 0
1 4 89A0 2048KB INTEL 28F016SA 0 0
2 4 89A0 2048KB INTEL 28F016SA 0 0
1 5 89A0 2048KB INTEL 28F016SA 0 0
2 5 89A0 2048KB INTEL 28F016SA 0 0
```

The following example shows the flash partition summary.

```text
Router# show
slot0: summary
Partition Size Used Free Bank-Size State Copy Mode
1 20223K 10821K 9402K 4096K Read/Write Direct
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
```


### `show slot1:`

> **Página:** 965 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the PCMCIA flash memory card’s file system located in slot 1, use the show slot1:command in user EXEC or privileged EXEC mode. show slot1:[all | chips | detailed | err | summary]

**Parameters (Syntax Description):**

- `all` — ( Optional) D is p l a y s all p o s s i b l e flash system information for all PCM C I A flash card s in the system.
- `chips` — ( Optional) D is p l a y s flash c h ip information.
- `detailed` — ( Optional) D is p l a y s the flash detailed directory.
- `err` — ( Optional) D is p l a y s the flash c h ip erase and write retries.
- `summary` — ( Optional) D is p l a y s the flash partition summary.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0 | This command was introduced. |

**Usage Guidelines:**

Use the show slot1: command to display details about the files in a particular linear PCMCIA flash memory card of less than 20 MB and some 32 MB linear PCMCIA cards located in slot 1. Note Use the show disk command for ATA PCMCIA cards. Other forms of this commands are show disk0: and show disk1:. For more information regarding file systems and flash cards, access the PCMCIA Filesystem Compatibility Matrix and Filesystem Information document at the following URL: http://www.cisco.com/en/US/partner/products/hw/routers/ps341/products_tech_note09186a00800a7515.shtml To see which flash cards are used in your router, use the show version command and look at the bottom portion of the output. The following display indicates an ATA PCMCIA flash disk.

```text
Router# show version
46976K bytes of ATA PCMCIA card at slot 0 (Sector size 512 bytes).
```

The following display indicates a linear PCMCIA flash card with 20480K bytes of flash memory in card at slot 1 with a sector size of 128K.

```text
Router# show version
20480K bytes of Flash PCMCIA card at slot 1 (Sector size 128K).
```

Note In some cases the show slot command will not display the file systems. Use show slot0: or show slot1:.

**Example:**

```text
The following example displays information about slot 0 using the slot0:
command form. The output is self-explanatory.
Router# show slot1
:
PCMCIA Slot1 flash directory:
File Length Name/status
1 10907068 c3660-bin-mz.123-7.9.PI4
[10907132 bytes used, 5739008 available, 16646140 total]
16384K bytes of processor board PCMCIA Slot1 flash (Read/Write)
show slot1: all
Partition Size Used Free Bank-Size State Copy Mode
1 20223K 10821K 9402K 4096K Read/Write Direct
PCMCIA Slot0 flash directory:
File Length Name/status
addr fcksum ccksum
1 11081464 c3660-bin-mz.123-9.3.PI5b
0x40 0x5EA3 0x5EA3
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Chip Bank Code Size Name
1 1 89A0 2048KB INTEL 28F016SA
2 1 89A0 2048KB INTEL 28F016SA
1 2 89A0 2048KB INTEL 28F016SA
2 2 89A0 2048KB INTEL 28F016SA
1 3 89A0 2048KB INTEL 28F016SA
2 3 89A0 2048KB INTEL 28F016SA
1 4 89A0 2048KB INTEL 28F016SA
2 4 89A0 2048KB INTEL 28F016SA
1 5 89A0 2048KB INTEL 28F016SA
2 5 89A0 2048KB INTEL 28F016SA
The following example shows flash chip information.
Router# show slot1: chips
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Chip Bank Code Size Name
1 1 89A0 2048KB INTEL 28F016SA
2 1 89A0 2048KB INTEL 28F016SA
1 2 89A0 2048KB INTEL 28F016SA
2 2 89A0 2048KB INTEL 28F016SA
1 3 89A0 2048KB INTEL 28F016SA
2 3 89A0 2048KB INTEL 28F016SA
1 4 89A0 2048KB INTEL 28F016SA
2 4 89A0 2048KB INTEL 28F016SA
1 5 89A0 2048KB INTEL 28F016SA
2 5 89A0 2048KB INTEL 28F016SA
```

The following example show the flash detailed directory.

```text
Router# show slot1: detailed
PCMCIA Slot0 flash directory:
File Length Name/status
addr fcksum ccksum
1 11081464 c3660-bin-mz.123-9.3.PI5b
0x40 0x5EA3 0x5EA3
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
```

The following example shows the flash chip erase and write retries.

```text
Router# show slot1: err
PCMCIA Slot0 flash directory:
File Length Name/status
1 11081464 c3660-bin-mz.123-9.3.PI5b
[11081528 bytes used, 9627844 available, 20709372 total]
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Chip Bank Code Size Name erase write
1 1 89A0 2048KB INTEL 28F016SA 0 0
2 1 89A0 2048KB INTEL 28F016SA 0 0
1 2 89A0 2048KB INTEL 28F016SA 0 0
2 2 89A0 2048KB INTEL 28F016SA 0 0
1 3 89A0 2048KB INTEL 28F016SA 0 0
2 3 89A0 2048KB INTEL 28F016SA 0 0
1 4 89A0 2048KB INTEL 28F016SA 0 0
2 4 89A0 2048KB INTEL 28F016SA 0 0
1 5 89A0 2048KB INTEL 28F016SA 0 0
2 5 89A0 2048KB INTEL 28F016SA 0 0
```

The following example shows the flash partition summary.

```text
Router# show
slot1: summary
Partition Size Used Free Bank-Size State Copy Mode
1 20223K 10821K 9402K 4096K Read/Write Direct
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
```


### `show software authenticity file`

> **Página:** 967 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information related to software authentication for a specific image file, use the show software authenticity file command in privileged EXEC mode. | usbflash0:filename | usbflash1:filename}

**Syntax:**

```text
show software authenticity file {flash0:filename | flash1:filename | flash:filename | nvram:filename
```

**Parameters (Syntax Description):**

- `flash0:` — D is p l a y s information related to software auth e n t i c at i on for flash0 resource s.
- `file name` — Name of the file name in memory.
- `flash1:` — D is p l a y s information related to software auth e n t i c at i on for flash1 resource s.
- `flash:` — D is p l a y s information related to software auth e n t i c at i on for flash resource s.
- `nvram:` — D is p l a y s information related to software auth e n t i c at i on for NVRAM resource s.
- `usb flash0:` — D is p l a y s information related to software auth e n t i c at i on for U n i v e r s a l Serial Bus( USB) flash 0 resource s.
- `usb flash1:` — D is p l a y s information related to software auth e n t i c at i on for USB flash1 resource s.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced for the Cisco1941,2900, and3900 routers. |

**Usage Guidelines:**

The show software authenticity file command allows you to display software authentication related information that includes image credential information, key type used for verification, signing information, and other attributes in the signature envelope, for a specific image file. The command handler will extract the signature envelope and its fields from the image file and dump the required information.

**Example:**

The following example displays software authentication related information for an image file named c3900-universalk9-mz.SSA:

```text
Router# show software authenticity file flash0:c3900-universalk9-mz.SSA
File Name : flash0:c3900-universalk9-mz.SSA
Image type : Development
Signer Information
Common Name : xxx
Organization Unit : xxx
Organization Name : xxx
Certificate Serial Number : xxx
Hash Algorithm : SHA512
Signature Algorithm : 2048-bit RSA
Key Version : A
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| FileName | Nameofthefilenameinthememory.Forexample, flash0:c3900-universalk9-mz.SSAreferstofilenamec3900-universalk9-mz.SSA inflashmemory(flash0:). |

| Field | Description |
| --- | --- |
| Imagetype | Displaysthetypeofimage. |
| SignerInformation | Signatureinformation. |
| CommonName | Displaysthenameofthesoftwaremanufacturer. |
| OrganizationUnit | Displaysthehardwarethesoftwareimageisdeployedon. |
| OrganizationName | Displaystheownerofthesoftwareimage. |
| CertificateSerialNumber | Displaysthecertificateserialnumberforthedigitalsignature. |
| HashAlgorithm | Displaysthetypeofhashalgorithmusedindigitalsignatureverification. |
| SignatureAlgorithm | Displaysthetypeofsignaturealgorithmusedindigitalsignatureverification. |
| KeyVersion | Displaysthekeyversionusedforverification. |


### `show software authenticity keys`

> **Página:** 969 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the software public keys that are in the storage with the key types, use the show software authenticity keyscommand in privileged EXEC mode.

**Syntax:**

```text
show software authenticity keys
```

**Parameters (Syntax Description):**

- `—` — This command has no argument or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced for the Cisco1941,2900, and3900 routers. |

**Usage Guidelines:**

The display from this command includes the public keys that are in the storage with the key types.

**Example:**

The following is sample output from the show software authenticity keys command:

```text
show software authenticity keys
Public Key #1 Information
-------------------------
Key Type : Release (Primary)
Public Key Algorithm : RSA
Modulus :
CC:CA:40:55:8C:71:E2:4A:3A:B6:9D:5C:94:1D:02:BA:
.....
26:04:6B:33:EB:70:2B:18:24:C7:D9:31:3E:77:24:85
Exponent : xxx
Key Version : A
Public Key #2 Information
-------------------------
Key Type : Development (Primary)
Public Key Algorithm : RSA
Modulus :
CC:CA:40:55:8C:71:E2:4A:3A:B6:9D:5C:94:1D:02:BA:
.....
26:04:6B:33:EB:70:2B:18:24:C7:D9:31:3E:77:24:85
Exponent : xxx
Key Version : A
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| PublicKey# | Publickeynumber. |
| KeyType | Displaysthekeytypeusedforimageverification. |
| PublicKeyAlgorithm | Displaysthenameofthealgorithmusedforpublickeycryptography. |
| Modulus | Modulusofthepublickeyalgorithm. |
| Exponent | Exponentofthepublickeyalgorithm |
| KeyVersion | Displaysthekeyversionusedforverification. |


### `show software authenticity running`

> **Página:** 970 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information related to software authentication for the current ROM monitor (ROMMON), monitor library (monlib), and Cisco IOS image used for booting, use the show software authenticity running command in privileged EXEC mode.

**Syntax:**

```text
show software authenticity running
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced for the Cisco1941,2900, and3900 routers. |

**Usage Guidelines:**

The information displayed by the show software authenticity running command about the current ROMMON, monlib and Cisco IOS image used for booting includes: • Image credential information • Key type used for verification • Signing information • Any other attributes in the signature envelope

**Example:**

The following example displays software authentication related information for the current ROM monitor (ROMMON), monitor library (monlib), and Cisco IOS image used for booting:

```text
Router(mode-prompt
)# show software authenticity running
SYSTEM IMAGE
-------------------
Image type : Development
Signer Information
Common Name : xxx
Organization Unit : xxx
Organization Name : xxx
Certificate Serial Number : xxx
Hash Algorithm : xxx
Signature Algorithm : 2048-bit RSA
Key Version : xxx
Verifier Information
Verifier Name : ROMMON 2
Verifier Version : System Bootstrap, Version 12.4(20090409:084310)
ROMMON 2
---------------
Image type : Development
Signer Information
Common Name : xxx
Organization Unit : xxx
Organization Name : xxx
Certificate Serial Number : xxx
Hash Algorithm : xxx
Signature Algorithm : 2048-bit RSA
Key Version : xxx
Verifier Information
Verifier Name : ROMMON 2
Verifier Version : System Bootstrap, Version 12.4(20090409:084310)
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| SYSTEMIMAGE | Sectionoftheoutputdisplayingthesystemimageinformation. |
| Imagetype | Displaysthetypeofimage. |
| CommonName | Displaysthenameofthesoftwaremanufacturer. |
| OrganizationUnit | Displaysthehardwarethesoftwareimageisdeployedon. |
| OrganizationName | Displaystheownerofthesoftwareimage. |
| CertificateSerialNumber | Displaysthecertificateserialnumberforthedigitalsignature. |
| HashAlgorithm | Displaysthetypeofhashalgorithmusedindigitalsignatureverification. |
| SignatureAlgorithm | Displaysthetypeofsignaturealgorithmusedindigitalsignatureverification. |
| KeyVersion | Displaysthekeyversionusedforverification. |
| VerifierName | Nameoftheprogramresponsibleforperformingthedigitalsignatureverification. |
| VerifierVersion | Versionoftheprogramresponsibleforperformingthedigitalsignature verification. |
| ROMMON2 | SectionoftheoutputdisplayingthecurrentROMmonitor(ROMMON) information. |


### `show software package`

> **Página:** 972 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To display information about a specific bundle or package file, use the show software package command in privileged EXEC mode.

**Syntax:**

```text
show software package bundle or package url [detail][verbose]
```

**Parameters (Syntax Description):**

- `bundle or package url` — Specify then a m e of the bundle or package file who s e information should be d is p l a y e d.
- `detail` — ( optional) This command option is in t end e d to p r o v id e a d d it i on a l detail s about the specified package or bundle file. Current l y, no a d d it i on a l information is d is p l a y e d.
- `verbose` — ( optional) p r o v id e s some a d d it i on a l info in the logfile s

**Command Default:** No default behavior or values.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |
| CiscoIOSXERelease3.3SE | This command was integrated. |

**Usage Guidelines:**

The 'show software package' command displays information about the specified bundle or package file. If a package file is specified, this command displays information from its package metadata. If a bundle file is specified, this command displays information from its bundle metadata, and also information from the package metadata of each package included in the bundle.

**Example:**

The following example shows the show software package output for a bundle file.

```text
infra-p2-3#show software package flash:cat3k_caa-universalk9.SSA.03.09.19.
EMP.150-9.19.EMP.bin
Package: cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin
Size: 220766688
Timestamp: 2012-11-15 11:53:50 UTC
Canonical path: /flash/cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin
Header size: 2928 bytes
Internal package information:
Name: rp_super
BuildTime: Thu Nov 15 01:55:09 PST 2012
ReleaseDate: Thu Nov 15 01:55:09 PST 2012
RouteProcessor: mips
Platform: ng3k
User: udonthi
PackageName: cat3k_caa-universalk9
Build: 03.09.19.EMP
Dependencies: PROVIDES:cat3k_caa-base,03.09.19.EMP,mips;cat3k_caa-infra,03.09.19.EMP,
mips;cat3k_caa-platform,03.09.19.EMP,mips;cat3k_caa-iosd-universalk9,150-9.19.EMP,
mips;cat3k_caa-wcm,03.09.19.EMP,mips;cat3k_caa-drivers,03.09.19.EMP,mips;
BuildType: Production
Package is bootable from media and tftp.
Package contents:
Package: cat3k_caa-base.SSA.03.09.19.EMP.pkg
Size: 74390336
Timestamp: 2012-11-15 11:55:30 UTC
Header size: 412 bytes
Internal package information:
Name: rp_base
BuildTime: Thu Nov 15 01:52:19 PST 2012
ReleaseDate: Thu Nov 15 01:52:19 PST 2012
RouteProcessor: mips
Platform: ng3k
User: udonthi
PackageName: cat3k_caa-base
Build: 03.09.19.EMP
Dependencies: PROVIDES: nova-gold,03.09.19.EMP,mips; nova-goldlib,03.09.19.EMP,mips;
nova-base,03.09.19.EMP,mips#REQUIRES:#WORKSWITH:#CONFLICTS:#
BuildType: Production
Package is not bootable.
Package: cat3k_caa-drivers.SSA.03.09.19.EMP.pkg
Size: 2734772
Timestamp: 2012-11-15 11:55:37 UTC
Header size: 252 bytes
Internal package information:
Name: drivers
BuildTime: Thu Nov 15 01:54:53 PST 2012
ReleaseDate: Thu Nov 15 01:54:53 PST 2012
RouteProcessor: mips
Platform: ng3k
User: udonthi
PackageName: cat3k_caa-drivers
Build: 03.09.19.EMP
Dependencies: PROVIDES: ng3k-drivers,03.09.19.EMP,mips#REQUIRES:#WORKSWITH:
#CONFLICTS:#
BuildType: Production
Package is not bootable.
Package: cat3k_caa-infra.SSA.03.09.19.EMP.pkg
Size: 32465772
Timestamp: 2012-11-15 11:55:32 UTC
Header size: 436 bytes
Internal package information:
Name: rp_infra
BuildTime: Thu Nov 15 01:53:08 PST 2012
ReleaseDate: Thu Nov 15 01:53:08 PST 2012
RouteProcessor: mips
Platform: ng3k
User: udonthi
PackageName: cat3k_caa-infra
Build: 03.09.19.EMP
Dependencies: PROVIDES: nova-infra,03.09.19.EMP,mips;
nova-infralibs,03.09.19.EMP,mips; nova-web,03.09.19.EMP,mips;
nova-shell,03.09.19.EMP,mips; nova-console-relay,03.09.19.EMP,mips;
nova-mgmte,03.09.19.EMP,mips; nova-ng3k-flash,03.09.19.EMP,mips#
EQUIRES:#WORKSWITH:#CONFLICTS:#
BuildType: Production
Package is not bootable.
Package: cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg
Size: 30384940
Timestamp: 2012-11-15 11:55:34 UTC
Header size: 372 bytes
Internal package information:
Name: rp_iosd
BuildTime: Thu Nov 15 01:54:09 PST 2012
ReleaseDate: Thu Nov 15 01:54:09 PST 2012
RouteProcessor: mips
Platform: ng3k
User: udonthi
PackageName: cat3k_caa-iosd-universalk9
Build: 150-9.19.EMP
Dependencies: PROVIDES: iosd-stuff,03.09.19.EMP,mips; nova-ioslibs-required,
03.09.19.EMP,mips; ioucon,150-9.19.EMP,mips;
ng3k-iosd-universalk9,150-9.19.EMP,mips#REQUIRES:#WORKSWITH:#CONFLICTS:#
BuildType: Production
Package is not bootable.
Package: cat3k_caa-platform.SSA.03.09.19.EMP.pkg
Size: 18148064
Timestamp: 2012-11-15 11:55:33 UTC
Header size: 296 bytes
Internal package information:
Name: rp_platform
BuildTime: Thu Nov 15 01:53:39 PST 2012
ReleaseDate: Thu Nov 15 01:53:39 PST 2012
RouteProcessor: mips
Platform: ng3k
User: udonthi
PackageName: cat3k_caa-platform
Build: 03.09.19.EMP
Dependencies: PROVIDES: nova-platformlibs-required,03.09.19.EMP,mips;
ng3k-platform,03.09.19.EMP,mips#REQUIRES:#WORKSWITH:#CONFLICTS:#
BuildType: Production
Package is not bootable.
Package: cat3k_caa-wcm.SSA.03.09.19.EMP.pkg
Size: 62638800
Timestamp: 2012-11-15 11:55:37 UTC
Header size: 280 bytes
Internal package information:
Name: rp_wcm
BuildTime: Thu Nov 15 01:54:34 PST 2012
ReleaseDate: Thu Nov 15 01:54:34 PST 2012
RouteProcessor: mips
Platform: ng3k
User: udonthi
PackageName: cat3k_caa-wcm
Build: 03.09.19.EMP
Dependencies: PROVIDES: wcm-ng3k,03.09.19.EMP,mips; nova-wcmlibs-required,
03.09.19.EMP,mips#REQUIRES:#WORKSWITH:#CONFLICTS:#
BuildType: Production
Package is not bootable.
infra-p2-3#
```


### `show software installer rollback-timer`

> **Página:** 976 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** There are no command options. · **Leitura (show/clear/…):** sim

**Description:** The show software installer rollback-timer command displays the current auto-rollback timer status for a standalone platform or all switches in a stacked system.

**Syntax:**

```text
show software installer rollback-timer
```

**Command Default:** There are no command options.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |
| CiscoIOSXERelease3.3SE | This command was integrated. |

**Usage Guidelines:**

There are no command options.

**Example:**

To show the auto-rollback timer status for the current switch, perform the following.

```text
infra-p2-3#show software installer rollback-timer
Switch# Status Duration
----------------------------------
1 active 00:31:28
2 active 00:31:43
infra-p2-3#
infra-p2-3#show software installer rollback-timer
Switch# Status Duration
----------------------------------
1 inactive -
2 inactive -
infra-p2-3#
```


### `show stacks`

> **Página:** 977 · **Modo:** Privilege EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To monitor the stack usage of processes and interrupt routines, use the show stacks command in EXEC mode.

**Syntax:**

```text
show stacks PID
```

**Parameters (Syntax Description):**

- `PID` — Process id e n t if i e r of the process that allocate d the stack. The value ranges from 1 to 8192.

**Command Modes:** Privilege EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOS10.0 | This command was introduced. |
| CiscoIOS12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The display from this command includes the reason for the last system reboot. If the system was reloaded because of a system failure, a saved system stack trace is displayed. This information is of use only to your technical support representative in analyzing crashes in the field. It is included here in case you need to read the displayed statistics to an engineer over the phone. Use the show stacks PID command to print the call stack of the process with ID ranging from 1 to 8192. This command displays the following information: • Stack segment: Where the process stack lies in the memory. • List of FP: <address>: The Frame Pointer (FP) for each frame in the call stack. • List of RA: <address>: The Return Address (RA) of each frame in the call stack.

**Example:**

The following is a sample output from the show stacks command following a system failure:

```text
Device# show stacks
Minimum process stacks:
Free/Size Name
652/1000 Router Init
726/1000 Init
744/1000 BGP Open
686/1200 Virtual Exec
Interrupt level stacks:
Level Called Free/Size Name
1 0 1000/1000 env-flash
3 738 900/1000 Multiport Communications Interfaces
5 178 970/1000 Console UART
System was restarted by bus error at PC 0xAD1F4, address 0xD0D0D1A
GS Software (GS3), Version 9.1(0.16), BETA TEST SOFTWARE
Compiled Tue 11-Aug-92 13:27 by jthomas
Stack trace from system failure:
FP: 0x29C158, RA: 0xACFD4
FP: 0x29C184, RA: 0xAD20C
FP: 0x29C1B0, RA: 0xACFD4
FP: 0x29C1DC, RA: 0xAD304
FP: 0x29C1F8, RA: 0xAF774
FP: 0x29C214, RA: 0xAF83E
FP: 0x29C228, RA: 0x3E0CA
FP: 0x29C244, RA: 0x3BD3C
```

The following is a sample output from the show stacks PID command:

```text
Device# show stack 10
Process 10: WATCH_AFS
Stack segment 0x21668518 - 0x216690D0
FP: 0x21669068, RA: 0x31A3D79C
Device# show stack 100
Process 100: dev_device_inserted
Stack segment 0x418D1CC8 - 0x418D2880
FP: 0x418D2830, RA: 0x30488210
Device# show stack 200
Process 200: WAAS Process
Stack segment 0x41B76DB8 - 0x41B79C98
FP: 0x41B79BE8, RA: 0x335ABEB4
Device# sh stack 311
Process 311: Virtual Exec
Stack segment 0x24625DFC - 0x2462BBBC
FP: 0x2462AEC0, RA: 0x3333372C
FP: 0x2462AF60, RA: 0x36AF9250
```


The more nvram:startup-config command has been replaced by the show startup-config command. See the description of the more command in the “Cisco IOS File System Commands” chapter for more information.

### `show subsys`

> **Página:** 979 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the subsystem information, use the show subsys command in privileged EXEC mode.

**Syntax:**

```text
show subsys [class class | name name]
```

**Parameters (Syntax Description):**

- `class` — class ( Optional) D is p l a y s the subsys t e m s of the specified class. Valid classes are driver, ehsa,
- `class class` — ( Optional) D is p l a y s the subsys t e m s of the specified class. V a l id class e s are driver, e h s a, if s, k e r n e l, l i b r a r y, l i c e n s e, management, microcode, p r e-e h s a, p r e-driver, p r o to c o l, registry, and s y s in it.
- `name name` — ( Optional) D is p l a y s the specified subsys t e m. Use the as t e r is k character(*) as a w i l d card at the end of then a m e to list all subsys t e m s, starting with the specified characters.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | This command was introduced. |
| 12.3 | This command was modified. The e h s a, if s, microcode, p r e-driver, and s y s in it class e s were added. |
| 12.3T | This command was modified The p r e-e h s a class was added. |
| 12.2(33)SRA | This command was modified. The driver, e h s a, k e r n e l, l i b r a r y, management, p r e-driver, p r e-e h s a, p r o to c o l, and registry class e s were added. |
| 12.2(35)SE2 | This command was modified. The driver, e h s a, k e r n e l, l i b r a r y, l i c e n s e, management, p r e-driver, p r e-e h s a, p r o to c o l, and registry class e s were added. |

**Usage Guidelines:**

Use the show subsys command to confirm that all required features are in the running image.

**Example:**

The following is sample output from the show subsys command:

```text
Router# show subsys
Name Class Version
static_map Kernel 1.000.001
arp Kernel 1.000.001
ether Kernel 1.000.001
compress Kernel 1.000.001
alignment Kernel 1.000.002
monvar Kernel 1.000.001
slot Kernel 1.000.001
oir Kernel 1.000.001
atm Kernel 1.000.001
ip_addrpool_sys Library 1.000.001
chat Library 1.000.001
dialer Library 1.000.001
flash_services Library 1.000.001
ip_localpool_sys Library 1.000.001
nvram_common Driver 1.000.001
ASP Driver 1.000.001
sonict Driver 1.000.001
oc3suni Driver 1.000.001
oc12suni Driver 1.000.001
ds3suni Driver 1.000.001
```

The following is sample output from the show subsys command that includes the license class:

```text
show subsys name license
Name Class Version
license_mgmt_local Management 1.000.001
license_admin_local Management 1.000.001
license_debug_core Management 1.000.001
license_test_ui Management 1.000.001
test_license_parser Management 1.000.001
license_ui Management 1.000.001
license_parser Management 1.000.001
license_registry Registry 1.000.001
license_client License 1.000.001
```

The table below describes the fields shown in the display.

| Field | Description |
| --- | --- |
| Name | Nameofthesubsystem. |
| Class | Classofthesubsystem.PossibleclassesincludeDriver,Ehsa,Ifs,Kernel,Library,License, Management,Microcode,Pre-Ehsa,Pre-driver,Protocol,Registry,andSysinit. |
| Version | Versionofthesubsystem. |


### `show sup-bootflash`

> **Página:** 980 · **Modo:** Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display information about the sup-bootflash file system, use the show sup-bootflash command in privileged EXEC mode.

**Syntax:**

```text
show sup-bootflash [all | chips | filesys]
```

**Parameters (Syntax Description):**

- `all` — ( Optional) D is p l a y s all p o s s i b l e Flash information.
- `chips` — ( Optional) D is p l a y s information about the Flash c h ip.
- `filesys` — ( Optional) D is p l a y s information about the filesystem.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.217d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to display a summary of bootflash information:

```text
show sup-bootflash
-#- ED --type-- --crc--- -seek-- nlen -length- -----date/time------ name
1 .. image EBC8FC4D A7487C 6 10700796 Nov 19 1999 07:07:37 halley
2 .. unknown C7EB077D EE2620 25 4644130 Nov 19 1999 07:50:44 cat6000-sup_
5-3-3-CSX.bin
645600 bytes available (15345184 bytes used)
```

This example shows how to display all bootflash information:

```text
show sup-bootflash all
-#- ED --type-- --crc--- -seek-- nlen -length- -----date/time------ name
1 .. image EBC8FC4D A7487C 6 10700796 Nov 19 1999 07:07:37 halley
2 .. unknown C7EB077D EE2620 25 4644130 Nov 19 1999 07:50:44 cat6000-sup_
5-3-3-CSX.bin
645600 bytes available (15345184 bytes used)
-------- F I L E S Y S T E M S T A T U S --------
Device Number = 2
DEVICE INFO BLOCK: bootflash
Magic Number = 6887635 File System Vers = 10000 (1.0)
Length = 1000000 Sector Size = 40000
Programming Algorithm = 19 Erased State = FFFFFFFF
File System Offset = 40000 Length = F40000
MONLIB Offset = 100 Length = F568
Bad Sector Map Offset = 3FFF8 Length = 8
Squeeze Log Offset = F80000 Length = 40000
Squeeze Buffer Offset = FC0000 Length = 40000
Num Spare Sectors = 0
Spares:
STATUS INFO:
Writable
NO File Open for Write
Complete Stats
No Unrecovered Errors
No Squeeze in progress
USAGE INFO:
Bytes Used = EA2620 Bytes Available = 9D9E0
Bad Sectors = 0 Spared Sectors = 0
OK Files = 2 Bytes = EA2520
Deleted Files = 0 Bytes = 0
Files w/Errors = 0 Bytes = 0
******** Intel SCS Status/Register Dump ********
COMMON MEMORY REGISTERS: Bank 0
Intelligent ID Code : 890089
Compatible Status Reg: 800080
DEVICE TYPE:
Layout : Paired x16 Mode
Write Queue Size : 64
Queued Erase Supported : No
```

This example shows how to display information about the Flash chip:

```text
Router# show sup-bootflash chips
******** Intel SCS Status/Register Dump ********
COMMON MEMORY REGISTERS: Bank 0
Intelligent ID Code : 890089
Compatible Status Reg: 800080
DEVICE TYPE:
Layout : Paired x16 Mode
Write Queue Size : 64
Queued Erase Supported : No
```

This example shows how to display information about the file system:

```text
Router# show sup-bootflash filesys
-------- F I L E S Y S T E M S T A T U S --------
Device Number = 2
DEVICE INFO BLOCK: bootflash
Magic Number = 6887635 File System Vers = 10000 (1.0)
Length = 1000000 Sector Size = 40000
Programming Algorithm = 19 Erased State = FFFFFFFF
File System Offset = 40000 Length = F40000
MONLIB Offset = 100 Length = F568
Bad Sector Map Offset = 3FFF8 Length = 8
Squeeze Log Offset = F80000 Length = 40000
Squeeze Buffer Offset = FC0000 Length = 40000
Num Spare Sectors = 0
Spares:
STATUS INFO:
Writable
NO File Open for Write
Complete Stats
No Unrecovered Errors
No Squeeze in progress
USAGE INFO:
Bytes Used = EA2620 Bytes Available = 9D9E0
Bad Sectors = 0 Spared Sectors = 0
OK Files = 2 Bytes = EA2520
Deleted Files = 0 Bytes = 0
Files w/Errors = 0 Bytes = 0
```


### `show system jumbomtu`

> **Página:** 983 · **Modo:** Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the global maximum transmission unit (MTU) setting, use the show system jumbomtu command in privileged EXEC mode.

**Syntax:**

```text
show system jumbomtu
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to display the global MTU setting:

```text
Router# show system jumbomtu
Global Ethernet MTU is 1550 bytes.
```


### `show tech-support`

> **Página:** 983 · **Modo:** Privileged EXEC (#) · **Default:** The output scrolls without page breaks. Passwords and other security information are removed from the output. · **Leitura (show/clear/…):** sim

**Description:** To display general information about the router when it reports a problem, use the command in privileged EXEC mode. Cisco 7600 Series Cisco ASR 900 Series, Cisco ASR 920 Series, Cisco NCS 4200 Series { | { } |

**Syntax:**

```text
show tech-support
show tech-support [page] [password] [cef | ipc | ipmulticast [vrf vrf-name] | isis | mpls | ipsec [peer
ipv4 address | vrf vrf-name] | ospf [process-id | detail] | rsvp | voice | wccp]
show tech-support [cef | ipmulticast [vrf vrf-name] | isis | password [page] | platform | page | rsvp]
show tech-support platform cef ipv4 address [ vrf vrf-name ] |
bfd gal GAL-BFD-tunnel-number ipv4 ip-address GigabitEthernet TenGigabitEthernet
multihop ip-address | poch-ipv4 ip-address { GigabitEthernet TenGigabitEthernet } } |
multicast ipv4 ip-address |
qos
```

**Parameters (Syntax Description):**

- `page` — ( Optional) Cause s the output to d is p l a y apa g e of information at at i m e.
- `password` — ( Optional) L e a v e s passwords and other s e c u r it y information in the output.
- `cef` — ( Optional) D is p l a y s show command output s p e c if i c to Cisco Express For w a r d in g.
- `ipc` — ( Optional) D is p l a y s show command output s p e c if i c to In t e r-Process C o m m u n i c at i on( IP C).
- `ip m u l t i c as t` — ( Optional) D is p l a y s show command output that isr e l at e d to the IP M u l t i c as t configuration, in c l u d in g P r o to c o l In d e p end e n t M u l t i c as t( P I M) information, In t e r n e t Group Management P r o to c o l( I G M P) information, and D is t an c e Vector M u l t i c as t Routing P r o to c o l( D V M R P) information.
- `vrfvrf-name` — ( Optional) Specifies a m u l t i c as t Virtual Private Network( V P N) r out in g and for w a r d in g in s t an c e( VRF).
- `ipsec` — ( Optional) D is p l a y s show command output related to the IPSec configuration.
- `p e e r ip v4 address` — ( Optional) Specifies the IP v4 address of ap e e r.
- `isis` — ( Optional) D is p l a y s show command output s p e c if i c to Connection l e s s Network Service( C L N S) and In t e r m e d i at e System-to-In t e r m e d i at e System P r o to c o l( IS-IS).
- `mpls` — ( Optional) D is p l a y s show command output s p e c if i c to M u l t ip r o to c o l Label Switch in g( M P L S) for w a r d in g and ap p l i c at i on s.
- `o s p f[ process-id| detail]` — ( Optional) D is p l a y s show command output s p e c if i c to Open S h or test Path First P r o to c o l( O S P F) network in g.
- `rsvp` — ( Optional) D is p l a y s show command output s p e c if i c to Resource R e s e r v at i on P r o to c o l( R S V P) network in g.
- `voice` — ( Optional) D is p l a y s show command output s p e c if i c to v o i c e network in g.
- `wccp` — ( Optional) D is p l a y s show command output s p e c if i c to Web Cache C o m m u n i c at i on P r o to c o l( WCCP).
- `platform` — ( Optional) D is p l a y s platform-s p e c if i c show command output.
- `bfd` — D is p l a y s debug information for B F D sessions.
- `gal` — D is p l a y s debug information for Generic As s o c i at e d Channel L a be l( G A L)( L a be l 13) B F D sessions. T u n n e l range is from1—2147483647.
- `ipv4` — D is p l a y s debug information for an IP v4 B F D session.
- `m u l t i h o p` — D is p l a y s debug information form u l t i h o p B F D sessions.
- `poch-ipv4` — D is p l a y s debug information for a m i c r o B F D session.
- `m u l t i c as t` — D is p l a y s debug information form u l t i c as t IP v4 sessions.
- `qos` — D is p l a y s debug information for q o s sessions

**Command Default:** The output scrolls without page breaks. Passwords and other security information are removed from the output.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2 | This command was introduced. |
| 11.3(7),11.2(16) | This command was modified. The output for this command was expand e d to show a d d it i on a l information for boot, bootflash, context, and traffic for all enabled protocols. |
| 12.0 | This command was modified. The output for this command was expand e d to show a d d it i on a l information for boot, bootflash, context, and traffic for all enabled protocols. The c e f, ip m u l t i c as t, is is, m l p s, and o s p f keywords were added to this command. |
| 12.2(13)T | This command was modified. Support for Apple Talk E I GRP, Ap o l l o Domain, Banyan V IN E S, No v e l l Link-State P r o to c o l, and X N S was removed from Cisco IOS software. |
| 12.2(14)SX | Support for this command was added for the Supervisor E n g in e720. |
| 12.3(4)T | This command was modified. The output of this command was expand e d to include the output from the show inventory command. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release 12.2(17d)SXB. |
| 12.2(30)S | This command was modified. The show tech-support ip m u l t i c as t command was changed as f o l low s: • Support for b id i r e c t i on a l PIMand M u l t i c as t V P N( M V P N) was added. • The vrf vrf-name keyword and argument were added. The output of the show tech-support ip m u l t i c as t command( with out the vrf vrf-name keyword and argument) was changed to include the output from these commands: • show ip p i min t d f • show ip p i m m d t • show ip p i m m d t b g p • show ip p i m r p m e t r i c |
| 12.3(16) | This command was integrated into Cisco IOS Release12.3(16). |
| 12.2(18)SXF | This command was modified. The show tech-support ip m u l t i c as t command was changed as f o l low s: • Support for b id i r e c t i on a l PIMand M V P N was added. • The vrf vrf-name keyword and argument were added. The output of the show tech-support ip m u l t i c as t vrf command was changed to include the output from these commands: • show mls ip m u l t i c as t r p-map ping g m-cache • show m mls g c process • show m mls m s c r p d f-cache The output of the show tech-support ip m u l t i c as t command( with out the vrf vrf-name keyword and argument) was changed to include the output from these commands: • show ip p i min t d f • show ip p i m m d t • show ip p i m m d t b g p • show ip p i m r p m e t r i c Support to interrupt and terminate the show tech-support output was added. |
| 12.4(7) | This command was integrated into Cisco IOS Release12.4(7). |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.4(9)T | This command was modified. The output of this command was expand e d to include p a r t i a l show d m v p n detail s command output. |
| 15.0(1)M | This command was modified. The wccp and v o i c e keywords were added. |
| 12.2(33)SRE | This command was modified. The wccp keyword was added. |
| CiscoIOSXERelease2.5 | This command was modified. The wccp keyword was added. |
| 15.3(2)T | This command was modified. The output was e x t end e d to include s e l e c to u t p u t forthe Group Domain of In t e r p r e t at i on( G DO I) configuration on keys e r v e r s and group m e m be r s. |
| CiscoIOSXERelease 3.9S | This command was modified. The output was e x t end e d to include s e l e c to u t p u t forthe G DO I configuration on keys e r v e r s and group m e m be r s. |
| 15.4(1)T | This command was modified. The output of the ipsec keyword was modified. |
| CiscoIOSXECupertino 17.9.1 | The commands how tech-support p l a f o m c e f is e n h an c e d to d is p l a y IP address information. |
| CiscoIOSXEDublin 17.10.1 | The commands how tech-support p l a f o m b f d and show tech-support p l a f o m m u l t i c as t is introduced to d is p l a y information on B F D and m u l t i c as t sessions r e s p e c t i v e l y. |
| CiscoIOSXEDublin 17.10.1 | The show tech support and show tech-support platform are e n h an c e d with a d d it i on a l commands on the Cisco AS R920 router. |
| CiscoIOSXEDublin 17.12.1 | The commands how tech-support p l a f o m b f d q o s command is introduced to d is p l a y information on Q o s sessions. |

**Usage Guidelines:**

To interrupt and terminate the show tech-support output, simultaneously press and release the CTRL, ALT, and 6 keys. Press the Return key to display the next line of output, or press the Spacebar to display the next page of information. If you do not enter the page keyword, the output scrolls (that is, it does not stop for page breaks). If you do not enter the password keyword, passwords and other security-sensitive information in the output are replaced with the label “<removed>.” The show tech-support command is useful for collecting a large amount of information about your routing device for troubleshooting purposes. The output of this command can be provided to technical support representatives when reporting a problem. Effective with CSCsg71173, password authentication protocol (PAP) and challenge handshake authentication protocol (CHAP) passwords are not displayed in the output of this command. Note This command can generate a very large amount of output. You may want to redirect the output to a file using the show inventory | redirect url command syntax extension. Redirecting the output to a file also makes sending this output to your technical support representative easier. For more information about this option, see the command documentation for show <command> | redirect. The show tech-support command displays the output of a number of show commands at once. The output from this command varies depending on your platform and configuration. For example, access servers display voice-related show command output. Additionally, the show protocol traffic commands are displayed for only the protocols enabled on your device. For a sample display of the output of the show tech-support command, see the individual show command listed. If you enter the show tech-support command without arguments, the output displays, but is not limited to, the equivalent of these show commands: • show appletalk traffic • show bootflash • show bootvar • show buffers • show cdp neighbors • show cef • show clns traffic • show context • show controllers • show crypto gdoi • show crypto gdoi gm • show crypto gdoi gm acl • show crypto gdoi gm pubkey • show crypto gdoi gm rekey detail • show crypto gdoi gm replay • show crypto gdoi ipsec sa • show crypto gdoi ks • show crypto gdoi ks acl • show crypto gdoi ks coop • show crypto gdoi ks coop version • show crypto gdoi ks identifier detail • show crypto gdoi ks member • show crypto gdoi ks policy • show crypto gdoi ks rekey • show crypto gdoi ks replay • show decnet traffic • show disk0: all • show dmvpn details • show environment • show fabric channel-counters • show file systems • show interfaces • show interfaces switchport • show interfaces trunk • show ip interface • show ip traffic • show logging • show mac-address-table • show module • show power • show processes cpu • show processes memory • show running-config • show spanning-tree • show stacks • show version • show vlan The following additional commands for show tech-support command are added on the Cisco ASR 920 router: • show cdp neighbors • show ethernet cfm errors • show ethernet cfm maintenance-points remote • show ethernet cfm maintenance-points local • show ethernet ring g8032 summary • show flow monitor • show mac address-table detail | include REMOTE • show mac address-table dynamic • show platform hardware pp active efp • show lldp neighbors • show platform hardware pp active interface all • show platform software infrastructure punt statistics • show platform software infrastructure lsmpi punt • show rep topology • show rep topology detail • request platform software sdcli "nile stats channel 0? • request platform software sdcli "nile stats channel 0 • show xconnect all The following additional commands are added to show tech-support platform command on the Cisco ASR 920 router: • show tech-support platform layer2 interface efp • show tech-support platform layer2 bridge-domain id • show tech-support platform pvppd dump vlan interface • show tech platform snmp-dyinggasp packets count Note Crypto information is not duplicated by the show dmvpn details command output. When the show tech-support command is entered on a virtual switch (VS), the output displays the output of the show module command and the show power command for both the active and standby switches. Use of the optional cef, ipc, ipmulticast, isis, mpls, ospf, or rsvp keywords provides a way to display a number of show commands specific to a particular protocol or process in addition to the show commands listed previously. For example, if your Technical Assistance Center (TAC) support representative suspects that you have a problem in your Cisco Express Forwarding (CEF) configuration, you may be asked to provide the output of the show tech-support cef command. The show tech-support [page] [password] cef command will display the output from the following commands in addition to the output for the standard show tech-support command: • show adjacency summary • show cef drop • show cef events • show cef interface • show cef not-cef-switched • show cef timers • show interfaces stats • show ip cef events summary • show ip cef inconsistency records detail • show ip cef summary If you enter the ipmulticast keyword, the output displays, but is not limited to, these show commands: • show ip dvmrp route • show ip igmp groups • show ip igmp interface • show ip mcache • show ip mroute • show ip mroute count • show ip pim interface • show ip pim interface count • show ip pim interface df • show ip pim mdt • show ip pim mdt bgp • show ip pim neighbor • show ip pim rp • show ip pim rp metric • show mls ip multicast rp-mapping gm-cache • show mmls gc process • show mmls msc rpdf-cache If you enter the wccp keyword, the output displays, but is not limited to, these show commands: • show ip wccp service-number • show ip wccp interfaces cef Use the show tech-support platform cef command to view the IPv4 address information. Note IPv6 address information is not supported. Use the show tech-support platform bfd command to view BFD debug session information. Use the show tech-support platform multicast command to view IPv4 session information.

**Example:**

```text
Router# show tech-support platform cef ipv4 10.10.10.8/32
% Warning! Execution of the platform flow scripts can
cause temporary glitch to VTY sessions. It is advised to
execute this command under the supervision of Cisco TAC
Are you sure you want to proceed? [yes/no]: yes
###### Log file at bootflash:/l3flow_log_22_44_29_562.txt ###########
Executing ASIC DUMP command
Platform CEF is programmed
KINDLY SHARE THE FILE ***l3flow_log_22_44_29_562.txt*** FROM BOOTFLASH
Router# ipv4 10.10.10.8/32 vrf vrf1
show tech-support platform cef
% Warning! Execution of the platform flow scripts can
cause temporary glitch to VTY sessions. It is advised to
execute this command under the supervision of Cisco TAC
Are you sure you want to proceed? [yes/no]: yes
###### Log file at bootflash:/l3flow_log_22_44_29_562.txt ###########
Executing ASIC DUMP command
Platform CEF is programmed
KINDLY SHARE THE FILE ***l3flow_log_22_44_29_562.txt*** FROM BOOTFLASH
show tech-support platform bfd ?
gal Dump GAL BFD
ipv4 debug an ipv4 bfd session
multihop Dump multihop BFD
poch-ipv4 debug a micro-bfd session
Router#show tech-support platform bfd ipv4 1.1.1.1 gi0/0/1 ?
| Output modifiers
<cr> <cr>
Router#show tech-support platform bfd multihop 1.1.1.1 ?
| Output modifiers
<cr> <cr>
Router#sh tech-support platform bfd gal ?
<1-2147483647> GAL BFD tunnel number
Router#show tech-support platform bfd gal 1 ?
| Output modifiers
<cr> <cr>
```


### `show template`

> **Página:** 994 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display template information, use the show template command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show template [template-name]
```

**Parameters (Syntax Description):**

- `template-name` — ( Optional) The template name.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRE | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release12.2(33) S R E. |
| 12.2(33)SXI | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release12.2(33) S X I. |
| 12.4(24)T | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release12.4(24) T. |
| CiscoIOS2.1 XE | This command was integrated into Cisco IOS X E Release2.1 on the Cisco ASR1000 Series A g g r e g at i on Service s Router. |

**Example:**

The following is sample output from the show templatecommand displaying template information. The fields are self-explanatory.

```text
Router# show template
Template class/type Component(s)
template1 owner ppp peer dialer
```


### `show usb controllers`

> **Página:** 994 · **Modo:** Privileged EXEC · **Default:** Information about all controllers on the system are displayed. · **Leitura (show/clear/…):** sim

**Description:** To display USB host controller information, use the show usb controllerscommand in privileged EXEC mode.

**Syntax:**

```text
show usb controllers [controller-number]
```

**Parameters (Syntax Description):**

- `controller-number` — ( Optional) D is p l a y s information only for the specified control l e r.

**Command Default:** Information about all controllers on the system are displayed.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(14)T | This command was introduced. |
| 12.4(11)T | This command was integrated into the Cisco7200 V X R N P E-G2 platform. |

**Usage Guidelines:**

Use the show usb controllerscommand to display content such as controller register specific information, current asynchronous buffer addresses, and period scheduling information. You can also use this command to verify that copy operations are occurring successfully onto a USB flash module.

**Example:**

The following example is sample output from the show usb controllers command:

```text
Router# show usb controllers
Name:1362HCD
Controller ID:1
Controller Specific Information:
Revision:0x11
Control:0x80
Command Status:0x0
Hardware Interrupt Status:0x24
Hardware Interrupt Enable:0x80000040
Hardware Interrupt Disable:0x80000040
Frame Interval:0x27782EDF
Frame Remaining:0x13C1
Frame Number:0xDA4C
LSThreshold:0x628
RhDescriptorA:0x19000202
RhDescriptorB:0x0
RhStatus:0x0
RhPort1Status:0x100103
RhPort2Status:0x100303
Hardware Configuration:0x3029
DMA Configuration:0x0
Transfer Counter:0x1
Interrupt:0x9
Interrupt Enable:0x196
Chip ID:0x3630
Buffer Status:0x0
Direct Address Length:0x80A00
ATL Buffer Size:0x600
ATL Buffer Port:0x0
ATL Block Size:0x100
ATL PTD Skip Map:0xFFFFFFFF
ATL PTD Last:0x20
ATL Current Active PTD:0x0
ATL Threshold Count:0x1
ATL Threshold Timeout:0xFF
Int Level:1
Transfer Completion Codes:
Success :920 CRC :0
Bit Stuff :0 Stall :0
No Response :0 Overrun :0
Underrun :0 Other :0
Buffer Overrun :0 Buffer Underrun :0
Transfer Errors:
Canceled Transfers :2 Control Timeout :0
Transfer Failures:
Interrupt Transfer :0 Bulk Transfer :0
Isochronous Transfer :0 Control Transfer:0
Transfer Successes:
Interrupt Transfer :0 Bulk Transfer :26
Isochronous Transfer :0 Control Transfer:894
USBD Failures:
Enumeration Failures :0 No Class Driver Found:0
Power Budget Exceeded:0
USB MSCD SCSI Class Driver Counters:
Good Status Failures :3 Command Fail :0
Good Status Timed out:0 Device not Found:0
Device Never Opened :0 Drive Init Fail :0
Illegal App Handle :0 Bad API Command :0
Invalid Unit Number :0 Invalid Argument:0
Application Overflow :0 Device in use :0
Control Pipe Stall :0 Malloc Error :0
Device Stalled :0 Bad Command Code:0
Device Detached :0 Unknown Error :0
Invalid Logic Unit Num:0
USB Aladdin Token Driver Counters:
Token Inserted :1 Token Removed :0
Send Insert Msg Fail :0 Response Txns :434
Dev Entry Add Fail :0 Request Txns :434
Dev Entry Remove Fail:0 Request Txn Fail:0
Response Txn Fail :0 Command Txn Fail:0
Txn Invalid Dev Handle:0
USB Flash File System Counters:
Flash Disconnected :0 Flash Connected :1
Flash Device Fail :0 Flash Ok :1
Flash startstop Fail :0 Flash FS Fail :0
USB Secure Token File System Counters:
Token Inserted :1 Token Detached :0
Token FS success :1 Token FS Fail :0
Token Max Inserted :0 Create Talker Failures:0
Token Event :0 Destroy Talker Failures:0
Watched Boolean Create Failures:0
```


### `show usb device`

> **Página:** 996 · **Modo:** Privileged EXEC · **Default:** Information for all devices attached to the system are displayed. · **Leitura (show/clear/…):** sim

**Description:** To display USB device information, use the show usb devicecommand in privileged EXEC mode.

**Syntax:**

```text
show usb device [controller-ID [device-address]]
```

**Parameters (Syntax Description):**

- `controller-ID` — ( Optional) D is p l a y s information only for the device s under the specified control l e r.
- `device-address` — ( Optional) D is p l a y s information only for the device with the specified address.

**Command Default:** Information for all devices attached to the system are displayed.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(14)T | This command was introduced. |
| 12.4(11)T | This command was integrated into the Cisco7200 V X R N P E-G2 platform. |

**Usage Guidelines:**

Use the show usb device command to display information for either a USB flash drive or a USB eToken, as appropriate.

**Example:**

The following example is sample output from the show usb device command:

```text
show usb device
Host Controller:1
Address:0x1
Device Configured:YES
Device Supported:YES
Description:DiskOnKey
Manufacturer:M-Sys
Version:2.0
Serial Number:0750D84030316868
Device Handle:0x1000000
USB Version Compliance:2.0
Class Code:0x0
Subclass Code:0x0
Protocol:0x0
Vendor ID:0x8EC
Product ID:0x15
Max. Packet Size of Endpoint Zero:64
Number of Configurations:1
Speed:Full
Selected Configuration:1
Selected Interface:0
Configuration:
Number:1
Number of Interfaces:1
Description:
Attributes:None
Max Power:140 mA
Interface:
Number:0
Description:
Class Code:8
Subclass:6
Protocol:80
Number of Endpoints:2
Endpoint:
Number:1
Transfer Type:BULK
Transfer Direction:Device to Host
Max Packet:64
Interval:0
Endpoint:
Number:2
Transfer Type:BULK
Transfer Direction:Host to Device
Max Packet:64
Interval:0
Host Controller:1
Address:0x11
Device Configured:YES
Device Supported:YES
Description:eToken Pro 4254
Manufacturer:AKS
Version:1.0
Serial Number:
Device Handle:0x1010000
USB Version Compliance:1.0
Class Code:0xFF
Subclass Code:0x0
Protocol:0x0
Vendor ID:0x529
Product ID:0x514
Max. Packet Size of Endpoint Zero:8
Number of Configurations:1
Speed:Low
Selected Configuration:1
Selected Interface:0
Configuration:
Number:1
Number of Interfaces:1
Description:
Attributes:None
Max Power:60 mA
Interface:
Number:0
Description:
Class Code:255
Subclass:0
Protocol:0
Number of Endpoints:0
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Devicehandle | Internalmemoryhandleallocatedtothedevice. |
| DeviceClasscode | Theclasscodesupportedbythedevice. ThisnumberisallocatedbytheUSB-IF.Ifthisfieldisresetto0,eachinterface withinaconfigurationspecifiesitsownclassinformation,andthevariousinterfaces operateindependently.Ifthisfieldissettoavaluebetween1andFEH,thedevice supportsdifferentclassspecificationsondifferentinterfaces,andtheinterfaces maynotoperateindependently.Thisvalueidentifiestheclassdefinitionusedfor theaggregateinterfaces.IfthisfieldissettoFFH,thedeviceclassisvendor-specific. |
| DeviceSubclasscode | Thesubclasscodesupportedbythedevice.ThisnumberisallocatedbytheUSB-IF. |
| DeviceProtocol | Theprotocolsupportedbythedevice.Ifthisfieldissetto0,thedevicedoesnot useclass-specificprotocolsonadevicebasis.Ifthisfieldissetto0xFF,thedevice usesavendor-specificprotocolonadevicebasis. |
| InterfaceClasscode | Theclasscodesupportedbytheinterface.Ifthevalueissetto0xFF,theinterface classisvendorspecific.AllothervaluesareallocatedbytheUSB-IF. |
| InterfaceSubclasscode | Thesubclasscodesupportedbytheinterface.AllvaluesareallocatedbytheUSB-IF. |
| InterfaceProtocol | Theprotocolcodesupportedbytheinterface.Ifthisfieldissetto0,thedevice doesnotuseaclass-specificprotocolonthisinterface.Ifthisfieldissetto0xFF, thedeviceusesavendor-specificprotocolforthisinterface. |
| MaxPacket | Maximumdatapacketsize,inbytes. |


### `show usb driver`

> **Página:** 999 · **Modo:** Privileged EXEC · **Default:** Information about all drivers is displayed. · **Leitura (show/clear/…):** sim

**Description:** To display information about registered USB class drivers and vendor-specific drivers, use the show usb drivercommand in privileged EXEC mode.

**Syntax:**

```text
show usb driver [index]
```

**Parameters (Syntax Description):**

- `index` — ( Optional) D is p l a y s information only for driver s on the specified in d e x.

**Command Default:** Information about all drivers is displayed.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(14)T | This command was introduced. |
| 12.4(11)T | This command was integrated into the Cisco7200 V X R N P E-G2 platform. |
| CiscoIOSXERelease3.6 | This command was integrated into Cisco IOS X E Release3.6. |

**Example:**

The following example is sample output for the show usb driver command:

```text
Router# show usb driver
Index:0
Owner Mask:0x6
Class Code:0x0
Subclass Code:0x0
Protocol:0x0
Interface Class Code:0x8
Interface Subclass Code:0x6
Interface Protocol Code:0x50
Product ID:0x655BD598
Vendor ID:0x64E90000
Attached Devices:
Controller ID:1, Device Address:1
Index:1
Owner Mask:0x1
Class Code:0x0
Subclass Code:0x0
Protocol:0x0
Interface Class Code:0x0
Interface Subclass Code:0x0
Interface Protocol Code:0x0
Product ID:0x514
Vendor ID:0x529
Attached Devices:
Controller ID:1, Device Address:17
Index:2
Owner Mask:0x5
Class Code:0x9
Subclass Code:0x6249BD58
Protocol:0x2
Interface Class Code:0x5DC0
Interface Subclass Code:0x5
Interface Protocol Code:0xFFFFFFFF
Product ID:0x2
Vendor ID:0x1
Attached Devices:
None
Index:3
Owner Mask:0x10
Class Code:0x0
Subclass Code:0x0
Protocol:0x0
Interface Class Code:0x0
Interface Subclass Code:0x0
Interface Protocol Code:0x0
Product ID:0x0
Vendor ID:0x0
Attached Devices:
None
```

The following table describes the significant field shown in the display.

| Field | Description |
| --- | --- |
| OwnerMask | Indicatesthefieldsthatareusedinenumerationcomparison.Thedrivercanowndifferent devicesonthebasisoftheirproductorvendorIDsanddeviceorinterfaceclass,subclass,and protocolcodes. |


### `show usb port`

> **Página:** 1000 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To sisplay USB root hub port information, use the show usb portcommand in privileged EXEC mode.

**Syntax:**

```text
show usb port [port-number]
```

**Parameters (Syntax Description):**

- `port-number` — ( Optional) D is p l a y s information only for as p e c if i e d. If the port-number is not is s u e d, information for all r o o t ports will be d is p l a y e d.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(14)T | This command was introduced. |

**Example:**

The following sample from the show usb port command shows the status of the port 1 on the router:

```text
Router# show usb port
Port Number:0
Status:Enabled
Connection State:Connected
Speed:Full
Power State:ON
Port Number:1
Status:Enabled
Connection State:Connected
Speed:Low
Power State:ON
```


### `show usb tree`

> **Página:** 1001 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the port state and all attached devices, use the show usb treecommand in privileged EXEC mode.

**Syntax:**

```text
show usb tree
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(14)T | This command was introduced. |

**Example:**

The following example is sample output from the show usb tree command. This output shows that both a USB flash module and a USB eToken are currently enabled.

```text
Router# show usb tree
[Host Id:1, Host Type:1362HCD, Number of RH-Port:2]
<Root Port0:Power=ON Current State=Enabled>
Port0:(DiskOnKey) Addr:0x1 VID:0x08EC PID:0x0015 Configured (0x1000000)
<Root Port1:Power=ON Current State=Enabled>
Port1:(eToken Pro 4254) Addr:0x11 VID:0x0529 PID:0x0514 Configured (0x1010000)
```


### `show usbtoken`

> **Página:** 1001 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the USB eToken (such as the eToken ID), use the show usbtokencommand in privileged EXEC mode.

**Syntax:**

```text
show usbtoken [0-9]: {allfilesystem}
```

**Parameters (Syntax Description):**

- `0-9` — ( Optional) One of the t e n a v a i l a b l e flash d r i v e s you can c h o o s e from; v a l id values:0-9. Ifyou do not specify an u m be r,0 is used by default
- `all` — ( Optional) All configuration files s to r e do n the e Token.
- `filesystem` — ( Optional) Name of a configuration file.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(14)T | This command was introduced. |
| 12.4(11)T | This command was integrated into the Cisco7200 V X R N P E-G2 platform. |
| CiscoIOSXERelease3.6 | This command was integrated into Cisco IOS X E Release3.6. |

**Usage Guidelines:**

Use the show usbtoken command to verify whether a USB eToken is inserted in the router.

**Example:**

The following example is sample output from the show usbtoken command:

```text
Router# show usbtoken0
Token ID :43353334
Token device name : token0
Vendor name : Vendor34
Product Name :Etoken Pro
Serial number : 22273a334353
Firmware version : 4.1.3.2
Total memory size : 32 KB
Free memory size : 16 KB
FIPS version : Yes/No
Token state : “Active” | “User locked” | “Admin locked” | “System Error” | “Uknown”
ATR (Answer To Reset) :"3B F2 98 0 FF C1 10 31 FE 55 C8 3"
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| TokenID | Tokenidentifier. |
| Tokendevicename | Auniquenamederivedbythetokendriver. |
| ATR(AnswertoReset) | InformationrepliedbySmartcardswhenaresetcommandisissued. |


### `show version`

> **Página:** 1002 · **Modo:** User EXEC (>) Privileged EXEC (#) Diagnostic (diag)--Cisco ASR 1000 Series Routers only · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To display information about the currently loaded software along with hardware and device information, use the show version command in user EXEC, privileged EXEC, or diagnostic mode. Cisco Catalyst 3850 Series Switches and Cisco 5760 Series Wireless Controllers Cisco ASR 1000 Series Routers Cisco Catalyst 4500e Series Switches running IOS XE software Cisco Catalyst 6500 Series Routers

**Syntax:**

```text
show version
show version[switchnode][running | committed | provisioned]
show version [rp-slot] [installed [user-interface] | provisioned | running]
show version [rp-slot] [running]
show version [epld slot]
```

**Parameters (Syntax Description):**

- `switch no d e` — ( optional) Only as in g l e switch may be specified. Default is all switch e s in as t a c k e d system.
- `running` — ( optional) Specifies information on the files current l y running. c at3850 and c t5760:( optional) D is p l a y s information about the a c t i v e package set current l y running on the switch. When boot e d in install e d mode, this is t y p i c all y these to f package s list e d in the boot e d provision in g file. When boot e d in bundle mode, this is t y p i c all y the set of package s c on t a in e d in the boot e d bundle.
- `commit t e d` — ( optional) D is p l a y s information about the commit t e d package set. If no install at i on o p e r at i on s have been perf or m e d s in c e bootup, this output will be the same as show version running. If any install at i on o p e r at i on s have been perf or m e d s in c e bootup, this output will d is p l a y these to f package s that will be activated/ running on then e x t reload. Note This command option is only ap p l i cable when running in install e d mode.
- `provision e d` — ( optional) Specifies information on the software files that are provision e d. c at3850 and c t5760:( optional) D is p l a y s information about the provision e d package set. In most c as e s, the provision e d package set is the same as the commit t e d package set. These package set s will d if f e r if an install at i on was perf or m e d with the‘ auto-rollback’ option and the install e d package s have not y e t been commit t e d using the' software commit' command. This command option is only ap p l i cable when running in install e d mode.
- `rp-slot` — Specifies the software of the R P in as p e c if i c R P slot of a Cisco AS R1000 S e r i e s Router. Options include: •r0--the RPin RPslot0. •r1--the RPin RPslot1. • r p a c t i v e--the a c t i v e RP. • r p s t and by--the s t and by RP.
- `install e d` — Specifies information on the software install e do n the RP
- `user-interface` — Specifies information on the files related to the user-interface.
- `epld slot` — ( Optional) Specifies the software of the E P L D slot of a Cisco Catalyst6500 S e r i e s Router.

**Command Default:** No default behavior or values.

**Command Modes:** User EXEC (>) Privileged EXEC (#) Diagnostic (diag)--Cisco ASR 1000 Series Routers only

**Command History:**

| Release | Modification |
| --- | --- |
| 9.0 | This command was introduced. |
| 12.1EC | This command was integrated into Cisco IOS Release12.1 E C. |
| 12.1(1a)T1 | This command was modified to include information about the clock card on C M T S routers. |
| 12.3BC | This command was integrated into Cisco IOS Release12.3 B C. |
| 12.3(4)T | The output format of this command was u p d at e d. |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to 12.2(17d)SXB. |
| 12.2(25)S | The output format of this command was u p d at e d. |
| 12.2(33)SCA | This command was integrated into Cisco IOS Release12.2(33) S C A. Support forthe Ciscou B R7225 V X R router was added. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers, and the following e n h an c e m e n t s were introduced: • the command be c a m e a v a i l a b l e in diagnostic mode. • the r p-slot, install e d, user-interface, provision e d, and running options all be c a m e a v a i l a b l e for the first time. |
| 12.2(18)SX | Added E L P D keyword and output for the Cisco Catalyst6500 S e r i e s Router. |
| CiscoIOSXERelease2.4 | The output format of this command was u p d at e d. |
| CiscoIOSXERelease3.1.0.SG | This command was introduced on the Cisco Catalyst4500 e Serfies Switch e s with support for the r p-slot parameter and running command option. |
| IOSXE3.2.0SE | Command introduced on the Cisco Catalyst3850 S e r i e s Switch e s and Cisco 5760 S e r i e s W i r e l e s s Controllers with support for the switch keyword and running, provision e d and commit t e d command options. |
| CiscoIOSXERelease3.3SE | This command was integrated. |

**Usage Guidelines:**

This command displays information about the Cisco IOS software version currently running on a routing device, the ROM Monitor and Bootflash software versions, and information about the hardware configuration, including the amount of system memory. Because this command displays both software and hardware information, the output of this command is the same as the output of the show hardware command. (The show hardware command is a command alias for the show version command.) Specifically, the show version command provides the following information: • Software information • Main Cisco IOS image version • Main Cisco IOS image capabilities (feature set) • Location and name of bootfile in ROM • Bootflash image version (depending on platform) • Device-specific information • Device name • System uptime • System reload reason • Config-register setting • Config-register settings for after the next reload (depending on platform) • Hardware information • Platform type • Processor type • Processor hardware revision • Amount of main (processor) memory installed • Amount I/O memory installed • Amount of Flash memory installed on different types (depending on platform) • Processor board ID The output of this command uses the following format:

```text
Cisco IOS Software, <platform> Software (<image-id>), Version <software-version>,
<software-type
Technical Support: http://www.cisco.com/techsupport
Copyright (c) <date-range> by Cisco Systems, Inc.
Compiled <day> <date> <time> by <compiler-id>
ROM: System Bootstrap, Version <software-version>, <software-type>
BOOTLDR: <platform> Software (image-id), Version <software-version>, <software-type>
<router-name> uptime is <w> weeks, <d> days, <h> hours,
<m> minutes
System returned to ROM by reload at <time> <day> <date>
System image file is "<filesystem-location>/<software-image-name>"
Last reload reason: <reload-reason>Cisco <platform-processor-type>
processor (revision <processor-revision-id>) with <free-DRAM-memory>
K/<packet-memory>K bytes of memory.
Processor board ID <ID-number
<CPU-type> CPU at <clock-speed>Mhz, Implementation <number>, Rev <
Revision-number>, <kilobytes-Processor-Cache-Memory>KB <cache-Level> Cache
```

See the Examples section for descriptions of the fields in this output. Cisco ASR 1000 Series Routers Entering show versionwithout any of the options on the Cisco ASR 1000 Series Router will generate output similar to show version on other Cisco routers. In order to understand the show versionoutput on Cisco ASR 1000 Series Routers, it is important to understand that the individual sub-packages run the processes on the router. Among other things, the output of this command provides information on where various individual sub-packages are stored on the router, and which processes these individual sub-packages are and are not currently running. More specifically, the command displays each individual sub-package file on the router, the hardware where the sub-package could be running, and whether the sub-package is currently being run on that hardware. The show version provisioned command displays only the individual sub-packages that can be provisioned, which are the RP-specific sub-packages (RP Access, RP Base, RP Control, and RP IOS) and the provisioning file. The output includes the individual sub-package file, the hardware where the sub-package could be running, and whether the sub-package is currently being run on that hardware. The command displays only the individual sub-packages that are currently active. The output includes the individual sub-package file and the hardware where the sub-package is running. Cisco Catalyst 4500e Series Switches Entering show version without any of the options on a Cisco Catalyst 4500e Series Switch running IOS XE software will generate output similar to show version on other Cisco platforms. One notable difference is that the output displays the IOS XE software version instead of the IOS image version. The IOS XE software bundle includes a set of individual packages that comprise the complete set of software that runs on the switch. The show version running command displays the list individual packages that are currently active, that is, the set of packages included in the IOS XE software bundle currently running on the Cisco Catalyst 4500e Series Switch. Cisco Catalyst 3850 Series Switches and Cisco 5760 Series Wireless Controllers Entering show version without any of the options on a Cisco Catalyst 3850 Series Switch or Cisco 5760 Series Wireless Controller will generate output similar to show version on other Cisco platforms. One notable difference is that the output displays the IOS XE software version instead of the IOS image version. The IOS XE software bundle includes a set of individual packages that comprise the complete set of software that runs on the switch or wireless controller. The show version running command displays the list of individual packages that are currently running on the switch. When booted in installed mode, this is typically the set of packages listed in the booted provisioning file. When booted in bundle mode, this is typically the set of packages contained in the bundle. The show version committed command displays information about the switch's or wireless controller's committed package set. If no installation operations have been performed since bootup, this output will be the same as show version running. If any installation operations have been performed since bootup, this output will display the set of packages that will be activated/running on the next reload. This command is not applicable when running in bundle mode. The show version provisioned command displays information about the provisioned package set. In most cases, the provisioned package set is the same as the committed package set. These package sets will differ if an installation was performed with the auto-rollback option and the installed packages have not yet been committed by use of the software commit command. This command is not applicable when running in bundle mode.

**Example:**

Cisco 3660 Router The following is sample output from the show version command issued on a Cisco 3660 running Cisco IOS Release 12.3(4)T:

```text
Router# show version
Cisco IOS Software, 3600 Software (C3660-I-M), Version 12.3(4)T
TAC Support: http://www.cisco.com/tac
Copyright (c) 1986-2003 by Cisco Systems, Inc.
Compiled Thu 18-Sep-03 15:37 by ccai
ROM: System Bootstrap, Version 12.0(6r)T, RELEASE SOFTWARE (fc1)
ROM:
C3660-1 uptime is 1 week, 3 days, 6 hours, 41 minutes
System returned to ROM by power-on
System image file is "slot0:tftpboot/c3660-i-mz.123-4.T"
Cisco 3660 (R527x) processor (revision 1.0) with 57344K/8192K bytes of memory.
Processor board ID JAB055180FF
R527x CPU at 225Mhz, Implementation 40, Rev 10.0, 2048KB L2 Cache
3660 Chassis type: ENTERPRISE
2 FastEthernet interfaces
4 Serial interfaces
DRAM configuration is 64 bits wide with parity disabled.
125K bytes of NVRAM.
16384K bytes of processor board System flash (Read/Write)
Flash card inserted. Reading filesystem...done.
20480K bytes of processor board PCMCIA Slot0 flash (Read/Write)
Configuration register is 0x2102
```

Cisco 7200 Router The following is sample output from the show version command issued on a Cisco 7200 router running Cisco IOS Release 12.4(4)T. This output shows the total bandwidth capacity and the bandwith capacity that is configured on the Cisco 7200. Displaying bandwidth capacity is available in Cisco IOS Release 12.2 and later releases.

```text
Router# show version
Cisco IOS Software, 7200 Software (C7200-JS-M), Version 12.4(4)T, RELEASE SOFTW)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2005 by Cisco Systems, Inc.
Compiled Thu 27-Oct-05 05:58 by ccai
ROM: System Bootstrap, Version 12.1(20000710:044039) [nlaw-121E_npeb 117], DEVEE
BOOTLDR: 7200 Software (C7200-KBOOT-M), Version 12.3(16), RELEASE SOFTWARE (fc4)
router uptime is 5 days, 18 hours, 2 minutes
System returned to ROM by reload at 02:45:12 UTC Tue Feb 14 2006
System image file is "disk0:c7200-js-mz.124-4.T"
Last reload reason: Reload Command
Cisco 7206VXR (NPE400) processor (revision A) with 491520K/32768K bytes of memo.
Processor board ID 26793934
R7000 CPU at 350MHz, Implementation 39, Rev 3.2, 256KB L2 Cache
6 slot VXR midplane, Version 2.6
Last reset from power-on
PCI bus mb0_mb1 (Slots 0, 1, 3 and 5) has a capacity of 600 bandwidth points.
Current configuration on bus mb0_mb1 has a total of 440 bandwidth points.
This configuration is within the PCI bus capacity and is supported.
PCI bus mb2 (Slots 2, 4, 6) has a capacity of 600 bandwidth points.
Current configuration on bus mb2 has a total of 390 bandwidth points
This configuration is within the PCI bus capacity and is supported.
Please refer to the following document "Cisco 7200 Series Port Adaptor
Hardware Configuration Guidelines" on Cisco.com <http://www.cisco.com>
for c7200 bandwidth points oversubscription and usage guidelines.
4 Ethernet interfaces
2 FastEthernet interfaces
2 ATM interfaces
125K bytes of NVRAM.
62976K bytes of ATA PCMCIA card at slot 0 (Sector size 512 bytes).
125952K bytes of ATA PCMCIA card at slot 1 (Sector size 512 bytes).
8192K bytes of Flash internal SIMM (Sector size 256K).
Configuration register is 0x2002
```

For information about PCI buses and bandwidth calculation, go to the "Cisco 7200 Series Port Adapter Installation Requirements" chapter, of the Cisco 7200 Series Port Adapter Hardware Configuration Guidelines guide. The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| CiscoIOSSoftware,platformSoftware (image-id),Versionsoftware-version, release-type Forexample: CiscoIOSSoftware,7200Software (C7200-G4JS-M),Version12.3(4)T | platform--Ciscohardwaredevicename. image-id--Thecodedsoftwareimageidentifier,intheformat platform-features-format(forexample,“c7200-g4js-mz”. software-version--TheCiscoIOSsoftwarereleasenumber,inthe formatx.y(z)A,wherex.yisthemainreleaseidentifier,zisthe maintenancereleasenumber,andA,whereapplicable,isthespecial releasetrainidentifier.Forexample,12.3(4)Tindicatesthefourth maintenancereleaseofthe12.3Tspecialtechnologyreleasetrain. Note Inthefullsoftwareimagefilename,12.3(4)Tappearsas123-4.T. IntheIOSUpgradePlanner,12.3(4)Tappearsas12.3.4T(ED). release-type--Thedescriptionofthereleasetype.Possiblevalues includeMAINTENANCE[forexample,12.3(3)]orINTERIM[for example,12.3(3.2)]. Tip Referto“TheABC’sofCiscoIOSNetworking”(availableon Cisco.com)formoreinformationonCiscoIOSsoftwarerelease numberingandsoftwareversions. CiscoIOSisaregisteredtrademark(R)ofCiscoSystems,Inc. |
| TechnicalSupport: http://www.cisco.com/techsupport Copyright(c)date-rangebyCisco Systems,Inc. | TheCiscoTechnicalSupport&Documentationwebsitecontains thousandsofpagesofsearchabletechnicalcontent,includinglinks toproducts,technologies,solutions,technicaltips,andtools. RegisteredCisco.comuserscanloginfromthispagetoaccesseven morecontent. CiscoIOSsoftware,includingthesourcecode,user-help,and documentation,iscopyrightedbyCiscoSystems,Inc.ItisCisco’s policytoenforceitscopyrightsagainstanythirdpartywhoinfringes onitscopyright. |
| ROM:SystemBootstrap,Version 12.0(6r)T,RELEASESOFTWARE (fc1) | Thesystem“bootstrap”software,storedinROMmemory. |
| BOOTFLASH: | Thesystem“bootflash”software,storedinFlashmemory(if applicable). |

| Field | Description |
| --- | --- |
| deviceuptimeis... Forexample: C3660-1uptimeis1week,3days,6 hours,41minutes | Theamountoftimethesystemhasbeenupandrunning. |
| SystemreturnedtoROMby reload-reasonattimedaydate Forexample: SystemreturnedtoROMbyreloadat 20:56:53UTCTueNov42003 | Showsthelastrecordedreasonforasystemreload,andtimeoflast reload. |
| Lastreloadreason:reload-reason Forexample: Lastreloadreason:Reloadcommand | Showsthelastrecordedreasonforasystemreload. |
| Lastresetfromreset-reason Forexample: Lastresetfrompower-on | Showsthelastrecordedreasonforasystemreset.Possible reset-reasonvaluesinclude: •power-on--Systemwasresetwiththeinitialpoweronorapower cyclingofthedevice. •s/wperipheral--Systemwasresetduetoasoftwareperipheral. •s/wnmi--Systemwasresetbyanonmaskableinterrupt(NMI) originatinginthesystemsoftware.Forexample,onsome systems,youcanconfigurethedevicetoresetautomaticallyif twoormorefansfail. •push-button--SystemwasresetbymanualactivationofaRESET push-button(alsocalledahardwareNMI). •watchdog--Systemwasresetduetoawatchdogprocess. •unexpectedvalue--Mayindicateabuserror,suchasforan attempttoaccessanonexistentaddress(forexample,“System restartedbybuserroratPC0xC4CA,address0x210C0C0”). (Thisfieldwasformerlylabeledasthe“Systemrestartedby”field.”) |
| Systemimagefileis“file-location/ file-name” Forexample: Systemimagefileis "slot0:tftpboot/c3660-i-mz.123-3.9.T2" | Displaysthefilelocation(localorremotefilesystem)andthesystem imagename. |

| Field | Description |
| --- | --- |
| Ciscoplatform(processor-type) processor(revision processor-revision-id)withfree -DRAM-memoryK/packet-memory Kbytesofmemory. Example--SeparateDRAMandPacket Memory: CiscoRSP4(R5000)processorwith 65536K/2072Kbytesofmemory Example--CombinedDRAMand PacketMemory: Cisco3660(R527x)processor (revision1.0)with57344K/8192K bytesofmemory. | ThislinecanbeusedtodeterminehowmuchDynamicRAM (DRAM)isinstalledonyoursystem,inordertodetermineifyou meetthe“Min.Memory”requirementforasoftwareimage.DRAM (includingSDRAM)isusedforsystemprocessingmemoryandfor packetmemory. Twovalues,separatedbyaslash,aregivenforDRAM:Thefirst valuetellsyouhowDRAMisavailableforsystemprocessing,and thesecondvaluetellsyouhowmuchDRAMisbeingusedforPacket memory. Thefirstvalue,MainProcessormemory,iseither: •TheamountofDRAMavailablefortheprocessor,or •ThetotalamountofDRAMinstalledonthesystem. Thesecondvalue,Packetmemory,iseither: •Thetotalphysicalinput/output(I/O)memory(or“Fast memory”)installedontherouter(Cisco4000,4500,4700,and 7500series),or •Theamountof“sharedmemory”usedforpacketbuffering.In thesharedmemoryscheme(Cisco2500,2600,3600,and7200 Series),apercentageofDRAMisusedforpacketbufferingby therouter'snetworkinterfaces. Note Theterms“I/Omemory”or“iomem”;“sharedmemory”;“Fast memory”and“PCImemory”allreferto“PacketMemory”.Packet memoryiseitherseparatephysicalRAMorsharedDRAM. SeparateDRAMandPacketMemory The4000,4500,4700,and7500seriesroutershaveseparateDRAM andPacketmemory,soyouonlyneedtolookatthefirstnumberto determinetotalDRAM.IntheexampletotheleftfortheCiscoRSP4, thefirstvalueshowsthattherouterhas65536K(65,536kilobytes, or64megabytes)ofDRAM.Thesecondvalue,8192K,isthePacket memory. CombinedDRAMandPacketMemory The2500,2600,3600,and7200seriesroutersrequireaminimum amountofI/Omemorytosupportcertaininterfaceprocessors. The1600,2500,2600,3600,and7200seriesroutersuseafraction ofDRAMasPacketmemory,soyouneedtoaddbothnumbersto findouttherealamountofDRAM.Intheexampletotheleftforthe Cisco3660,therouterhas57,344kilobytes(KB)offreeDRAMand 8,192KBdedicatedtoPacketmemory.Addingthetwonumbers togethergivesyou57,344K+8,192K=65,536K,or64megabytes (MB)ofDRAM. |

| Field | Description |
| --- | --- |
|  | Formoredetailsonmemeoryrequirements,seethedocument"How toChooseaCiscoIOS®SoftwareRelease"onCisco.com. |
| Configurationregisterisvalue Forexample: Configurationregisteris0x2142(will be0x2102atnextreload) | Showsthecurrentconfiguredhexvalueofthesoftwareconfiguration register.Ifthevaluehasbeenchangedwiththeconfig-register command,theregistervaluethatwillbeusedatthenextreloadis displayedinparenthesis. Thebootfield(finaldigit)ofthesoftwareconfigurationregister dictateswhatthesystemwilldoafterareset. Forexample,whenthebootfieldofthesoftwareconfiguration registerissetto00(forexample,0x0),andyoupresstheNMIbutton onaPerformanceRouteProcessor(PRP),theuser-interfaceremains attheROMmonitorprompt(rommon>)andwaitsforauser commandtobootthesystemmanually.Butifthebootfieldissetto 01(forexample,0x1),thesystemautomaticallybootsthefirstCisco IOSimagefoundintheonboardFlashmemorySIMMonthePRP. Thefactory-defaultsettingfortheconfigurationregisteris0x2102. ThisvalueindicatesthattherouterwillattempttoloadaCiscoIOS softwareimagefromFlashmemoryandloadthestartupconfiguration file. |

Catalyst 6500 Series Switches and Cisco 7600 Series Routers This example shows how to display the configuration of the system hardware, the software version, the names and sources of configuration files, and the boot images:

```text
Router# show version
Cisco Internetwork Operating System Software
IOS (tm) c6sup2_rp Software (c6sup2_rp-JSV-M), Version 12.1 (nightly.E020626) NIG
HTLY BUILD
Copyright (c) 1986-2002 by cisco Systems, Inc.
Compiled Wed 26-Jun-02 06:20 by
Image text-base: 0x40008BF0, data-base: 0x419BA000
ROM: System Bootstrap, Version 12.1(11r)E1, RELEASE SOFTWARE (fc1)
Router uptime is 2 weeks, 8 hours, 48 minutes
Time since Router switched to active is 1 minute
System returned to ROM by power-on (SP by power-on)
System image file is "sup-bootflash:c6sup22-jsv-mz"
cisco Catalyst 6000 (R7000) processor with 112640K/18432K bytes of memory.
Processor board ID SAD06210067
R7000 CPU at 300Mhz, Implementation 39, Rev 3.3, 256KB L2, 1024KB L3 Cache
Last reset from power-on
Bridging software.
X.25 software, Version 3.0.0.
SuperLAT software (copyright 1990 by Meridian Technology Corp).
TN3270 Emulation software.
3 Virtual Ethernet/IEEE 802.3 interface(s)
48 FastEthernet/IEEE 802.3 interface(s)
381K bytes of non-volatile configuration memory.
16384K bytes of Flash internal SIMM (Sector size 512K).
Configuration register is 0x2102
```

The following table describes the fields that are shown in the example.

| Field | Description |
| --- | --- |
| IOS(tm)c6sup2_rpSoftware (c6sup2_rp-JSV-M),Version 12.1(nightly.E020626)NIGHTLYBUILD | Versionnumber.Alwaysspecifythecompleteversionnumber whenreportingapossiblesoftwareproblem.Intheexample output,theversionnumberis12.1. |
| ROM:SystemBootstrap,Version 12.1(11r)E1,RELEASESOFTWARE(fc1) | Bootstrapversionstring. |
| BOOTFLASH:7200Software (C7200-BOOT-M),Version11.1(472), RELEASESOFTWARE | Bootversionstring. |
| Routeruptimeis | Amountoftimethatthesystemhasbeenupandrunning. |
| TimesinceRouterswitchedtoactive | Amountoftimesinceswitchoveroccurred. |
| Systemrestartedby | Logofhowthesystemwaslastbooted,bothasaresultof normalsystemstartupandofsystemerror.Forexample, informationcanbedisplayedtoindicateabuserrorthatis typicallytheresultofanattempttoaccessanonexistentaddress, asfollows: SystemrestartedbybuserroratPC0xC4CA,address 0x210C0C0 |
| Systemimagefileis | Ifthesoftwarewasbootedoverthenetwork,theInternetaddress oftheboothostisshown.Ifthesoftwarewasloadedfrom onboardROM,thislinereads“runningdefaultsoftware.” |
| ciscoCatalyst6000(R7000)processorwith 112640K/18432Kbytesofmemory. | Remainingoutputineachdisplaythatshowsthehardware configurationandanynonstandardsoftwareoptions. |
| Configurationregisteris | Configurationregistercontentsthataredisplayedin hexadecimalnotation. |

The output of the show version EXEC command can provide certain messages, such as bus error messages. If such error messages appear, report the complete text of this message to your technical support specialist. This example shows how to display the ELPD version information of a slot:

```text
show version epld 4
Module 4 EPLD's:
Number of EPLD's: 6
EPLD A : 0x5
EPLD B : 0x2
EPLD C : 0x1
EPLD D : 0x1
EPLD E : 0x1
```

Cisco uBR7246VXR Router The following is sample output from the show version command for a Cisco uBR7246 VXR with the cable clock card installed:

```text
Cisco Internetwork Operating System Software
IOS (tm) 7200 Software (UBR7200-P-M), Version 12.1(10)EC, RELEASE SOFTWARE
TAC Support: http://www.cisco.com/tac
Copyright (c) 1986-2000 by cisco Systems, Inc.
Compiled Wed 02-Feb-00 16:49 by ccai
Image text-base:0x60008900, data-base:0x61192000
ROM:System Bootstrap, Version 12.0(15)SC, RELEASE SOFTWARE
VXR1 uptime is 2 days, 1 hour, 24 minutes
System returned to ROM by power-on at 10:54:38 PST Sat Feb 5 2000
System restarted at 11:01:08 PST Sat Feb 5 2000
System image file is "slot1:ubr7200-p-mz.121-0.8.T"
cisco uBR7246VXR (NPE300) processor (revision B) with 122880K/40960K bytes of memory.
Processor board ID SAB0329005N
R7000 CPU at 262Mhz, Implementation 39, Rev 1.0, 256KB L2, 2048KB L3 Cache
6 slot VXR midplane, Version 2.0
Last reset from power-on
X.25 software, Version 3.0.0.
National clock card with T1 controller
1 FastEthernet/IEEE 802.3 interface(s)
2 Cable Modem network interface(s)
125K bytes of non-volatile configuration memory.
16384K bytes of Flash PCMCIA card at slot 0 (Sector size 128K).
20480K bytes of Flash PCMCIA card at slot 1 (Sector size 128K).
4096K bytes of Flash internal SIMM (Sector size 256K).
Configuration register is 0x0
```

The following table describes significant fields shown in these displays.

| Field | Description |
| --- | --- |
| IOS(tm)7200Software (UBR7200-P-M),Versionxx.x | Alwaysspecifythecompleteversionnumberwhenreportinga possiblesoftwareproblem.Intheexample,theversionnumberis CiscoIOSRelease12.1(10)EC. |
| ROM:SystemBootstrap | Bootstrapversionstring. |
| Routeruptimeis | Theamountoftimethesystemhasbeenupandrunning. |
| Systemrestartedat | Alsodisplayedisalogofhowthesystemwaslastbooted,asaresult ofnormalsystemstartuporsystemerror. |
| Systemimagefileis | Ifthesoftwarewasbootedoverthenetwork,theInternetaddressof theboothostisshown.IfthesoftwarewasloadedfromonboardROM, thislinereads“runningdefaultsoftware.” |

| Field | Description |
| --- | --- |
| ciscouBR7246VXR(NPE300) processor | Theremainingoutputineachdisplayshowsthehardware configurationandanynonstandardsoftwareoptions. |
| Configurationregisteris | Theconfigurationregistercontents,displayedinhexadecimalnotation. |

The output of the show version command can also provide certain messages, such as bus error messages. If such error messages appear, report the complete text of this message to your technical support specialist. Cisco uBR10012 Router The following example shows sample output from the show version command on a Cisco uBR10012 universal broadband router running Cisco IOS Release 12.3(17b)BC4:

```text
Router> show version
Cisco Internetwork Operating System Software
IOS (tm) 10000 Software (UBR10K2-K9P6U2-M), Version 12.3(17b)BC4, RELEASE SOFTWA
RE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Wed 22-Nov-06 11:41 by tinhuang
Image text-base: 0x60010F0C, data-base: 0x62480000
ROM: System Bootstrap, Version 12.0(20020314:211744) [REL-pulsar_sx.ios-rommon 1
12], DEVELOPMENT SOFTWARE
ubr10k uptime is 2 days, 22 hours, 13 minutes
System returned to ROM by reload at 01:34:58 UTC Sun Jun 8 2008
System image file is "disk0:ubr10k2-k9p6u2-mz.123-17b.BC4"
Last reload reason: Reload command
This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.
A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html
If you require further assistance please contact us by sending email to
export@cisco.com.
cisco uBR10000 (PRE2-RP) processor with 946175K/98304K bytes of memory.
Processor board ID TBA05380380
R7000 CPU at 500MHz, Implementation 39, Rev 4.1, 256KB L2, 8192KB L3 Cache
Backplane version 1.1, 8 slot
Last reset from register reset
PXF processor tmc0 is running.
PXF processor tmc1 is running.
PXF processor tmc2 is running.
PXF processor tmc3 is running.
1 TCCplus card(s)
1 FastEthernet/IEEE 802.3 interface(s)
3 Gigabit Ethernet/IEEE 802.3 interface(s)
24 Cable Modem network interface(s)
2045K bytes of non-volatile configuration memory.
125440K bytes of ATA PCMCIA card at slot 0 (Sector size 512 bytes).
125440K bytes of ATA PCMCIA card at slot 1 (Sector size 512 bytes).
65536K bytes of Flash internal SIMM (Sector size 512KB).
Secondary is up.
Secondary has 1044480K bytes of memory.
Configuration register is 0x2102
```

Cisco ASR 1000 Series Routers In Cisco IOS XE Release 2.4

```text
In the following example, the show version command is responsible for displaying the packages
installed, provisioned and running on the current RP.
```

In the following example, the command is entered on a Cisco ASR 1000 Series Router in diagnostic mode. Note that the output shows what every file that can be found in the consolidated package is or is not currently running (provisioning file, RP Access, RP Base, RP Control, RP IOS, ESP Base, SIP Base, SIP SPA).

```text
PE23_ASR-1006#
Package: Provisioning File, version: n/a, status: active
File: consolidated:packages.conf, on: RP0
Built: n/a, by: n/a
File SHA1 checksum: b6cb06b1ed02e041d48644340aa077833cff2076
Package: rpbase, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-rpbase.02.04.00.122-33.XND.pkg, on: RP0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 093f2c935b9dc4ed136623bc43488c6517b9a4ae
Package: rpcontrol, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-rpcontrol.02.04.00.122-33.XND.pkg, on: RP0/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: d71e05c824cb889048b3353257bd16129eb72c44
Package: rpios-advipservicesk9, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-rpios-advipservicesk9.02.04.00.122-33.XND.pkg, on: RP0/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 4167d300514153f67c3815c487c270c14449185d
Package: rpaccess, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-rpaccess.02.04.00.122-33.XND.pkg, on: RP0/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 0b0d108cd2683570778668697b7ffca2451b78b3
Package: rpcontrol, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-rpcontrol.02.04.00.122-33.XND.pkg, on: RP0/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: d71e05c824cb889048b3353257bd16129eb72c44
Package: rpios-advipservicesk9, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-rpios-advipservicesk9.02.04.00.122-33.XND.pkg, on: RP0/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 4167d300514153f67c3815c487c270c14449185d
Package: rpaccess, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-rpaccess.02.04.00.122-33.XND.pkg, on: RP0/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 0b0d108cd2683570778668697b7ffca2451b78b3
Package: rpbase, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-rpbase.02.04.00.122-33.XND.pkg, on: RP1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 093f2c935b9dc4ed136623bc43488c6517b9a4ae
Package: rpcontrol, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-rpcontrol.02.04.00.122-33.XND.pkg, on: RP1/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: d71e05c824cb889048b3353257bd16129eb72c44
Package: rpios-advipservicesk9, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-rpios-advipservicesk9.02.04.00.122-33.XND.pkg, on: RP1/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 4167d300514153f67c3815c487c270c14449185d
Package: rpaccess, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-rpaccess.02.04.00.122-33.XND.pkg, on: RP1/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 0b0d108cd2683570778668697b7ffca2451b78b3
Package: rpcontrol, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-rpcontrol.02.04.00.122-33.XND.pkg, on: RP1/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: d71e05c824cb889048b3353257bd16129eb72c44
Package: rpios-advipservicesk9, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-rpios-advipservicesk9.02.04.00.122-33.XND.pkg, on: RP1/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 4167d300514153f67c3815c487c270c14449185d
Package: rpaccess, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-rpaccess.02.04.00.122-33.XND.pkg, on: RP1/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 0b0d108cd2683570778668697b7ffca2451b78b3
Package: espbase, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-espbase.02.04.00.122-33.XND.pkg, on: ESP0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 3ae9255c7272a30f5dae319dec109acd29d9ae87
Package: espbase, version: 02.04.00.122-33.XND, status: inactive
File: consolidated:asr1000rp1-espbase.02.04.00.122-33.XND.pkg, on: ESP1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 3ae9255c7272a30f5dae319dec109acd29d9ae87
Package: sipbase, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-sipbase.02.04.00.122-33.XND.pkg, on: SIP0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: fc6e41d7de2ded3a16b6dc7e5e3a1151b788d254
Package: sipspa, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP0/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP0/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP0/2
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP0/3
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipbase, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-sipbase.02.04.00.122-33.XND.pkg, on: SIP1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: fc6e41d7de2ded3a16b6dc7e5e3a1151b788d254
Package: sipspa, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP1/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP1/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: active
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP1/2
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP1/3
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipbase, version: 02.04.00.122-33.XND, status: inactive
File: consolidated:asr1000rp1-sipbase.02.04.00.122-33.XND.pkg, on: SIP2
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: fc6e41d7de2ded3a16b6dc7e5e3a1151b788d254
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP2/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP2/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP2/2
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP2/3
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipbase, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipbase.02.04.00.122-33.XND.pkg, on: SIP3
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: fc6e41d7de2ded3a16b6dc7e5e3a1151b788d254
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP3/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP3/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP3/2
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP3/3
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipbase, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipbase.02.04.00.122-33.XND.pkg, on: SIP4
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: fc6e41d7de2ded3a16b6dc7e5e3a1151b788d254
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP4/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP4/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP4/2
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP4/3
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipbase, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipbase.02.04.00.122-33.XND.pkg, on: SIP5
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: fc6e41d7de2ded3a16b6dc7e5e3a1151b788d254
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP5/0
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP5/1
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: sipspa, version: 02.04.00.122-33.XND, status: n/a
File: consolidated:asr1000rp1-sipspa.02.04.00.122-33.XND.pkg, on: SIP5/2
Built: 2009-06-29_23.07, by: mcpre
File SHA1 checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
Package: Sipspa, Version: 02.04.00.122-33.xnd, Status: N/a
File: Consolidated:asr1000rp1-sipspa.02.04.00.122-33.xnd.pkg, On: Sip5/3
Built: 2009-06-29_23.07, By: Mcpre
File Sha1 Checksum: 24fb5b788582e062c900e2713b5c56a2704ca836
```

| Field | Description |
| --- | --- |
| Package: | Theindividualsub-packagename. |
| version: | Theconsolidatedpackageversionoftheindividualsub-package. |
| status: | Revealsifthesub-packageisactiveorinactiveforthespecifichardwarecomponent only. |
| File: | Thelocationandfilenameoftheindividualsub-packagefile. |
| on: | Thehardwarecomponent. |
| Built: | Thedatetheindividualsub-packagewasbuilt. |
| FileSHA1checksum: | TheSHA1sumforthefile.ThissumcanbecomparedagainstaSHA1sumgenerated byanySHA1sum-generatingtool. |

Cisco Catalyst 3850 Series Switches and Cisco 5760 Series Wireless Controllers The following is sample output from the show version command on a Cisco Catalyst 3850 Series Switch that is the active switch in a 2-member stack:

```text
infra-p2-3#show version
Cisco IOS Software, IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M),
Version 03.09.19.EMP EARLY DEPLOYMENT ENGINEERING NOVA_WEEKLY BUILD, synced to
DSGS_PI2_POSTPC_FLO_DSBU7_NG3K_1105
Copyright (c) 1986-2012 by Cisco Systems, Inc.
Compiled Thu 15-Nov-12 01:45 by udonthi
ROM: IOS-XE ROMMON
BOOTLDR: C3850 Boot Loader (C3850-HBOOT-M) Version 1.2, engineering software (D)
infra-p2-3 uptime is 5 minutes
Uptime for this control processor is 7 minutes
System returned to ROM by reload
System image file is "flash:packages.conf"
Last reload reason: Reload command
This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.
A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html
If you require further assistance please contact us by sending email to
export@cisco.com.
License Level: Ipservices
License Type: Permanent
Next reload license Level: Ipservices
cisco WS-C3850X-24P-PROTO2 (MIPS) processor with 2097152K bytes of physical memory.
Processor board ID FHH1515P03Y
1 Virtual Ethernet interface
56 Gigabit Ethernet interfaces
8 Ten Gigabit Ethernet interfaces
2048K bytes of non-volatile configuration memory.
2097152K bytes of physical memory.
160618K bytes of Crash Files at crashinfo:.
160618K bytes of Crash Files at crashinfo-1:.
706860K bytes of Flash at flash:.
698827K bytes of Flash at flash-1:.
3915670K bytes of USB Flash at usbflash0:.
0K bytes of Dummy USB Flash at usbflash0-1:.
0K bytes of at webui:.
Base Ethernet MAC Address : 64:00:f1:25:11:00
Motherboard Assembly Number : 73-12240-03
Motherboard Serial Number : FHH15130010
Model Revision Number : 01
Motherboard Revision Number : 02
Model Number : WS-C3850X-24P-PROTO2
System Serial Number : FHH1515P03Y
Switch Ports Model SW Version SW Image Mode
------ ----- ----- ---------- ---------- ----
1 32 WS-C3850X-24P-PROT 03.09.19.EMP cat3k_caa-universalk9 INSTALL
2 32 WS-C3850X-24P-PROT 03.09.19.EMP cat3k_caa-universalk9 INSTALL
Switch 01
---------
Switch uptime : 7 minutes
Base Ethernet MAC Address : 64:00:f1:25:1a:00
Motherboard Assembly Number : 73-12240-03
Motherboard Serial Number : FHH1513000T
Model Revision Number : 01
Motherboard Revision Number : 02
Model Number : WS-C3850X-24P-PROTO2
System Serial Number : FHH1515P047
Configuration register is 0x2 (will be 0x102 at next reload)
infra-p2-3#
```

In the following example, the show version running command is entered on a Cisco Catalyst 3850 Series Switch to view information about the packages currently running on both switches in a 2-member stack:

```text
infra-p2-3#show version running
Package: Base, version: 03.09.19.EMP, status: active
File: cat3k_caa-base.SSA.03.09.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:52:19 PST 2012, by: udonthi
Package: Drivers, version: 03.09.19.EMP, status: active
File: cat3k_caa-drivers.SSA.03.09.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:54:53 PST 2012, by: udonthi
Package: Infra, version: 03.09.19.EMP, status: active
File: cat3k_caa-infra.SSA.03.09.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:53:08 PST 2012, by: udonthi
Package: IOS, version: 150-9.19.EMP, status: active
File: cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:54:09 PST 2012, by: udonthi
Package: Platform, version: 03.09.19.EMP, status: active
File: cat3k_caa-platform.SSA.03.09.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:53:39 PST 2012, by: udonthi
Package: WCM, version: 03.09.19.EMP, status: active
File: cat3k_caa-wcm.SSA.03.09.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:54:34 PST 2012, by: udonthi
Package: Base, version: 03.09.19.EMP, status: active
File: cat3k_caa-base.SSA.03.09.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:52:19 PST 2012, by: udonthi
Package: Drivers, version: 03.09.19.EMP, status: active
File: cat3k_caa-drivers.SSA.03.09.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:54:53 PST 2012, by: udonthi
Package: Infra, version: 03.09.19.EMP, status: active
File: cat3k_caa-infra.SSA.03.09.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:53:08 PST 2012, by: udonthi
Package: IOS, version: 150-9.19.EMP, status: active
File: cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:54:09 PST 2012, by: udonthi
Package: Platform, version: 03.09.19.EMP, status: active
File: cat3k_caa-platform.SSA.03.09.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:53:39 PST 2012, by: udonthi
Package: WCM, version: 03.09.19.EMP, status: active
File: cat3k_caa-wcm.SSA.03.09.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:54:34 PST 2012, by: udonthi
```

In the following example, the show version provisioned and show version committed commands are entered on a Cisco Catalyst 3850 Series Switch that is the active switch in a 2-member stack. The show version committed commands displays information about the packages in the committed package set that will be running on the next reload. The show version provisioned command displays information about the packages in the provisioned package set. In most cases, the show version provisioned and show version committed output will display the same information, since the provisioned and committed packages sets include the same packages. The provisioned package set may differ from the committed package set in cases where a software install operation was performed with the auto-rollback command option, and the software commit command has not yet been entered. This is the case in the sample output below, where the packages from the 03.09.19.EMP were installed with the auto-rollback command option, but the 'software commit' command has not yet been entered. The show version provisioned and show version committed commands are not applicable when the switch is booted in bundle mode.

```text
infra-p2-3#show version provisioned
Package: Provisioning File, version: n/a, status: active
File: packages.conf, on: Switch1
Built: n/a, by: n/a
Package: Base, version: 03.09.19.EMP, status: active
File: cat3k_caa-base.SSA.03.09.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:52:19 PST 2012, by: udonthi
Package: Infra, version: 03.09.19.EMP, status: active
File: cat3k_caa-infra.SSA.03.09.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:53:08 PST 2012, by: udonthi
Package: Platform, version: 03.09.19.EMP, status: active
File: cat3k_caa-platform.SSA.03.09.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:53:39 PST 2012, by: udonthi
Package: IOS, version: 150-9.19.EMP, status: active
File: cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:54:09 PST 2012, by: udonthi
Package: WCM, version: 03.09.19.EMP, status: active
File: cat3k_caa-wcm.SSA.03.09.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:54:34 PST 2012, by: udonthi
Package: Drivers, version: 03.09.19.EMP, status: active
File: cat3k_caa-drivers.SSA.03.09.19.EMP.pkg, on: Switch1
Built: Thu Nov 15 01:54:53 PST 2012, by: udonthi
Package: Provisioning File, version: n/a, status: active
File: packages.conf, on: Switch2
Built: n/a, by: n/a
Package: Base, version: 03.09.19.EMP, status: active
File: cat3k_caa-base.SSA.03.09.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:52:19 PST 2012, by: udonthi
Package: Infra, version: 03.09.19.EMP, status: active
File: cat3k_caa-infra.SSA.03.09.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:53:08 PST 2012, by: udonthi
Package: Platform, version: 03.09.19.EMP, status: active
File: cat3k_caa-platform.SSA.03.09.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:53:39 PST 2012, by: udonthi
Package: IOS, version: 150-9.19.EMP, status: active
File: cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:54:09 PST 2012, by: udonthi
Package: WCM, version: 03.09.19.EMP, status: active
File: cat3k_caa-wcm.SSA.03.09.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:54:34 PST 2012, by: udonthi
Package: Drivers, version: 03.09.19.EMP, status: active
File: cat3k_caa-drivers.SSA.03.09.19.EMP.pkg, on: Switch2
Built: Thu Nov 15 01:54:53 PST 2012, by: udonthi
infra-p2-3#show version committed
Package: Provisioning File, version: n/a, status: active
File: packages.conf, on: Switch1
Built: n/a, by: n/a
Package: Base, version: 03.09.17.EMP, status: active
File: cat3k_caa-base.SSA.03.09.17.EMP.pkg, on: Switch1
Built: Mon Nov 12 20:27:51 PST 2012, by: udonthi
Package: Infra, version: 03.09.17.EMP, status: active
File: cat3k_caa-infra.SSA.03.09.17.EMP.pkg, on: Switch1
Built: Mon Nov 12 20:28:53 PST 2012, by: udonthi
Package: Platform, version: 03.09.17.EMP, status: active
File: cat3k_caa-platform.SSA.03.09.17.EMP.pkg, on: Switch1
Built: Mon Nov 12 20:29:33 PST 2012, by: udonthi
Package: IOS, version: 150-9.17.EMP, status: active
File: cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg, on: Switch1
Built: Mon Nov 12 20:29:58 PST 2012, by: udonthi
Package: WCM, version: 03.09.17.EMP, status: active
File: cat3k_caa-wcm.SSA.03.09.17.EMP.pkg, on: Switch1
Built: Mon Nov 12 20:30:29 PST 2012, by: udonthi
Package: Drivers, version: 03.09.17.EMP, status: active
File: cat3k_caa-drivers.SSA.03.09.17.EMP.pkg, on: Switch1
Built: Mon Nov 12 20:31:01 PST 2012, by: udonthi
Package: Provisioning File, version: n/a, status: active
File: packages.conf, on: Switch2
Built: n/a, by: n/a
Package: Base, version: 03.09.17.EMP, status: active
File: cat3k_caa-base.SSA.03.09.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:27:51 PST 2012, by: udonthi
Package: Infra, version: 03.09.17.EMP, status: active
File: cat3k_caa-infra.SSA.03.09.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:28:53 PST 2012, by: udonthi
Package: Platform, version: 03.09.17.EMP, status: active
File: cat3k_caa-platform.SSA.03.09.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:29:33 PST 2012, by: udonthi
Package: IOS, version: 150-9.17.EMP, status: active
File: cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:29:58 PST 2012, by: udonthi
Package: WCM, version: 03.09.17.EMP, status: active
File: cat3k_caa-wcm.SSA.03.09.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:30:29 PST 2012, by: udonthi
Package: Drivers, version: 03.09.17.EMP, status: active
File: cat3k_caa-drivers.SSA.03.09.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:31:01 PST 2012, by: udonthi
infra-p2-3#
```

| Field | Description |
| --- | --- |
| Package: | Theindividualsub-packagename. |
| version: | Theindividualsub-packageversion. |
| status: | RevealsifthepackageisactiveorinactiveforthespecificSupervisormodule. |
| File: | Thefilenameoftheindividualpackagefile. |
| on: | TheslotnumberoftheActiveorStandbySupervisorthatthispackageisrunningon. |
| Built: | Thedatetheindividualpackagewasbuilt. |

Cisco Catalyst 4500e Series Switches The following is sample output from the show version command on a Cisco Catalyst 4500e Series Switch running IOS XE software:

```text
Switch#show version
Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch Software
(cat4500e-UNIVERSALK9-M), Experimental Version 3.1.0.SG
[/nobackup/xxxx/cwab/build/arch_ppc/buildtree-ios/vob/ios/sys 100] Copyright (c)
1986-2010 by Cisco Systems, Inc.
Compiled Mon 19-Apr-10 09:19 by xxxx
Cisco IOS-XE software, Copyright (c) 2005-2010 by cisco Systems, Inc.
All rights reserved. Certain components of Cisco IOS-XE software are licensed under the
GNU General Public License ("GPL") Version 2.0. The software code licensed under GPL
Version 2.0 is free software that comes with ABSOLUTELY NO WARRANTY. You can redistribute
and/or modify such GPL code under the terms of GPL Version 2.0. For more details, see
the documentation or "License Notice" file accompanying the IOS-XE software, or the
applicable URL provided on the flyer accompanying the IOS-XE software.
Image text-base: 0x100D9954, data-base: 0x14B379D8
ROM: 12.2(54r)XO(0.246)
Jawa Revision 7, Snowtrooper Revision 0x0.0x14
gsgsw-g9-35 uptime is 4 minutes
Uptime for this control processor is 5 minutes System returned to ROM by reload System
image file is "tftp://1.2.3.4/tftpboot/xxxx/x.bin"
This product contains cryptographic features and is subject to United States and local
country laws governing import, export, transfer and use. Delivery of Cisco cryptographic
products does not imply third-party authority to import, export, distribute or use
encryption.
Importers, exporters, distributors and users are responsible for compliance with U.S. and
local country laws. By using this product you agree to comply with applicable laws and
regulations. If you are unable to comply with U.S. and local laws, return this product
immediately.
A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html
If you require further assistance please contact us by sending email to export@cisco.com.
License Information for 'iosd'
License Level: entservices Type: Evaluation
Next reboot license Level: entservices
cisco WS-C4510R-E (MPC8572) processor (revision 2) with 786516K/16384K bytes of memory.
Processor board ID SPE1046002Q
MPC8572 CPU at 1.5GHz, Supervisor 7
Last reset from Reload
1 Virtual Ethernet interface
84 Gigabit Ethernet interfaces
14 Ten Gigabit Ethernet interfaces
Configuration register is 0x920
Switch#
```

In the following example, the show version running command is entered on a Cisco Catalyst 4500e Series Switch to view the list of packages contained in the IOS XE software bundle currently loaded on the system.

```text
Switch# show version running
Package: Base, version: 3.0.0, status: active
File: cat4500e-base.SSA.3.0.0.pkg, on: Slot5
From Bundle: cat4500e-universalk9.SSA.3.1.0.SG
Built: Mon Apr 19 10:08:38 PDT 2010, by: xxxx
Package: Infra, version: 3.0.0, status: active
File: cat4500e-infra.SSA.3.0.0.pkg, on: Slot5
From Bundle: cat4500e-universalk9.SSA.3.1.0.SG
Built: Mon Apr 19 10:09:30 PDT 2010, by: xxxx
Package: IOS, version: 150-1.XO, status: active
File: cat4500e-universalk9.SSA.150-1.XO.pkg, on: Slot5
From Bundle: cat4500e-universalk9.SSA.3.1.0.SG
Built: Mon Apr 19 10:10:02 PDT 2010, by: xxxx
Package: Base, version: 3.0.0, status: active
File: cat4500e-base.SSA.3.0.0.pkg, on: Slot6
From Bundle: cat4500e-universalk9.SSA.3.1.0.SG
Built: Mon Apr 19 10:08:38 PDT 2010, by: xxxx
Package: Infra, version: 3.0.0, status: active
File: cat4500e-infra.SSA.3.0.0.pkg, on: Slot6
From Bundle: cat4500e-universalk9.SSA.3.1.0.SG
Built: Mon Apr 19 10:09:30 PDT 2010, by: xxxx
Package: IOS, version: 150-1.XO, status: active
File: cat4500e-universalk9.SSA.150-1.XO.pkg, on: Slot6
From Bundle: cat4500e-universalk9.SSA.3.1.0.SG
Built: Mon Apr 19 10:10:02 PDT 2010, by: xxxx
Switch#
```

| Field | Description |
| --- | --- |
| Package: | Theindividualsub-packagename. |
| version: | Theindividualsub-packageversion. |
| status: | RevealsifthepackageisactiveorinactiveforthespecificSupervisormodule. |
| File: | Thefilenameoftheindividualpackagefile. |
| on: | TheslotnumberoftheActiveorStandbySupervisorthatthispackageisrunningon. |
| From Bundle: | ThenameoftheIOSXEsoftwarebundlethatincludesthispackage. |
| Built: | Thedatetheindividualpackagewasbuilt. |


### `show warm-reboot`

> **Página:** 1025 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the statistics for attempted warm reboots, use the show warm-rebootcommand in privileged EXEC mode.

**Syntax:**

```text
show warm-reboot
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(2)T | This command was introduced. |
| 12.2(18)S | This command was integrated into Cisco IOS R e l as e12.2(18) S. |
| 12.2(28)SB | This command was integrated into Cisco IOS R e l as e12.2(28) S B. |

**Usage Guidelines:**

Use the show warm-reboot command to see if warm rebooting is enabled, and, if so, how many warm reloads have occurred and how much space in kilobytes (KB) is consumed by warm-reboot storage, which is the RAM area used to store the data segment that enables warm reloading to function.

**Example:**

The following example is sample output from the show warm-reboot command:

```text
show warm-reboot
Warm Reboot is enabled
Statistics:
10 warm reboots have taken place since the last cold reboot
XXX KB taken up by warm reboot storage
```


### `show wiretap`

> **Página:** 1026 · **Modo:** Privileged EXEC (#) · **Default:** If the id is not specified , information for all wiretap configurations and IDBs is displayed. · **Leitura (show/clear/…):** sim

**Description:** To display the intercept status, use the show wiretap command in privileged EXEC mode.

**Syntax:**

```text
show wiretap [id [stream-id] | idbs]
```

**Parameters (Syntax Description):**

- `id` — ( Optional) C C C ID number. The C C C ID value range is from1 to2147483647.
- `stream-id` — ( Optional) The ID value range is from1 to2147483647.
- `idbs` — (Optional)DisplaystheInterfaceDescriptiveBlock(IDB)towhichtheAccessControlList (ACL)isapplied.

**Command Default:** If the id is not specified , information for all wiretap configurations and IDBs is displayed.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |
| 12.2 (33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release12.2(33) S X I. |

**Usage Guidelines:**

Use the show wiretapcommand to display the intercept status.

**Example:**

The following is sample output from the show wiretap command. The field descriptions are self-explanatory.

```text
Router# show wiretap
Mediation Device 0x00000001
TTl = 3130
Time left = 3127 minutes
MD IP Address = 6.6.6.12
MD SNMP IF index = 0
MD HW IF index = 0
MD Source IP address = 6.6.6.14
MD UDP port = 7777
DSCP value = af41
Platform data = 0x00000000
Stream count = 1
Streams associated with MD
Generic stream 0x00000002
Status = 1
Packets intercepted = 0
Packets dropped = 0
Type = Session
Index 0x00000002
Acnt ID 0x00000001
SNMP provisioned intercept
Status 0
```


### `show whoami`

> **Página:** 1027 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the terminal line of the current user, including host name, line number, line speed, and location, use the show whoami command in EXEC mode.

**Syntax:**

```text
show whoami [text]
```

**Parameters (Syntax Description):**

- `text` — ( Optional) A d d it i on a l data to print to the screen.
- `text` — ( Optional) A d d it i on a l data to p r in t to the screen.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If text is included as an argument in the command, that text is displayed as part of the additional data about the line. To prevent the information from being lost if the menu display clears the screen, this command always displays a --More-- prompt before returning. Press the space bar to return to the prompt.

**Example:**

The following example is sample output from the show whoami command:

```text
Router> show whoami
Comm Server "Router", Line 0 at 0bps. Location "Second floor, West"
--More--
Router>
```


### `showmon`

> **Página:** 1028 · **Modo:** ROM monitor mode · **Default:** No default behavior or values · **Leitura (show/clear/…):** não

**Description:** To show both the ReadOnly and the Upgrade ROMmon image versions when you are in ROMmon mode, as well as which ROMmon image is running on the Cisco 7200 VXR or Cisco 7301 router, use the showmoncommand in ROM monitor mode.

**Syntax:**

```text
showmon
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** No default behavior or values

**Command Modes:** ROM monitor mode

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(28)S | This command was introduced on the Cisco7200 V X R router. It was introduced in ROMmon version12.3(4 r) T1 for the Cisco7200 V X R router. |
| 12.3(8)T | This command was integrated into Cisco IOS Release12.3(8) T and supported on the Cisco7200 V X R router and Cisco7301 router. It was introduced in ROMmon version12.3(4 r) T2 for the Cisco7301 router. |
| 12.3(9) | This command was integrated into Cisco IOS Release12.3(9) and supported on the Cisco7200 V X R router and Cisco7301 router. |

**Usage Guidelines:**

Use the showmon command when you are in ROM monitor mode. Use the show rom-monitor command when you are in Cisco IOS.

**Example:**

The following example, applicable to both the Cisco 7200 VXR and Cisco 7301 routers, uses the showmon command in ROMmon to display both ROMmon images and to verify that the Upgrade ROMmon image is running:

```text
rommon 1 > showmon
ReadOnly ROMMON version is:
System Bootstrap, Version 12.2(20031011:151758) [biff]
Copyright (c) 2004 by Cisco Systems, Inc.
Upgrade ROMMON version is:
System Bootstrap, Version 12.2(20031011:151758) [biff]
Copyright (c) 2004 by Cisco Systems, Inc.
Upgrade ROMMON currently running
Upgrade ROMMON is selected for next boot
rommon 2 >
```
