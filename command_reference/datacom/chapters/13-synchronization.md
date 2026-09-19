# Capítulo 13: Synchronization

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## NTP

### `clock`

> **Página:** 1592 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure settings related to the local clock.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
clock timezone timezone name timezone offset
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `timezone name` — Set a friendly name for the timezone. Any value will be accepted. — *Valores:* Length 2-30 · *Default:* None.
- `timezone offset` — Define an offset from UTC for the show system clock command. — *Valores:* From -12 to 14. · *Default:* 0

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

clock timezone is used to describe the current device location and its offset from UTC (a value of 0 defines that the device should output times in UTC); show system clock displays the current system clock, using the offset information provided by clock timezone. Usage example:

```text
DM4610# config
```

DM4610(config)# clock timezone Brazil -3 DM4610(config)# commit Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `set system clock`

> **Página:** 1595 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Set the hardware clock (RTC).

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
set system clock date time
```

**Parameters:**

- `date` — Set the clock date. — *Valores:* YYYYMMDD · *Default:* None.
- `time` — Set the clock time, in “hh:mm:ss” format. The clock must be set in a 24-hour format. — *Valores:* hh:mm:ss · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. The command syntax was modified from “set clock” to “set system 1.8 clock”. |

**Usage Guidelines:**

Usage example:

```text
DM4610# set system clock 20150815 13:30:00
```

Clock is set.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show sntp`

> **Página:** 1597 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays the current status of sntp servers.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show sntp { brief }
```

**Parameters:**

- `brief` — Shows summarized information about sntp servers. — *Valores:* N/A. · *Default:* N/A.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |

**Usage Guidelines:**

Usage example:

```text
# show sntp brief
```

Tally Codes (TC): *: syspeer, .: distance exceeded, o: PPS derived, +: candidate, #: selected, -: outlyer, x: falseticker, blank: unreachable TC Server IP Stratum When(*) Poll(*) Delay(ms) Offset(ms) Reach Auth ------------------------------------------------------------------------------------- * 1.1.1.1 2 2 32 17.891 -1.252 yes none + 1.1.1.2 3 22 32 0.287 0.777 yes ok 1.1.1.3 16 - 1024 0.000 0.000 no bad *Field in seconds if not specified, otherwise ’h’ for hours and ’m’ for minutes. Note that if SNTP authentication fail the server will be shown as unreachable like Server IP 1.1.1.3 on table above.

**Output Terms:**

Output Description Tally Codes (TC) The server clock selection process status. Server IP The remote server IP to request NTP information. Stratum The stratum level of remote server. When Time in seconds of last message replied. Poll Time selected to send next synchronization message. Output Description Delay Round-trip delay to the server (in milliseconds). Offset Relative time of the server clock to the local clock (in milliseconds). Reach Server reachability status. Auth The server authentication status.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show system clock`

> **Página:** 1600 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays the current date and time.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show system clock
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. The command syntax was modified from “show clock” to “show system clock”. Date and time display format for “show system clock” command was 1.8 changed from “[day of the week] [month] [day] HH:MM:SS (timezone name/UTC[offset])” to “YYYY-MM-DD HH:MM:SS UTC[offset] [Timezone-name]”. |

**Usage Guidelines:**

Usage example:

```text
DM4610# show system clock
1980-05-17 00:30:15 UTC+3 Brazil
```

**Output Terms:**

Output Description Current date and Displays the Current date and time in “YYYY-MM-DD HH:MM:SS time UTC[offset] [Timezone-name]” format

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `sntp`

> **Página:** 1602 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Configure the settings related to the local clock.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
sntp { authenticate | authentication-key key ID md5 MD5 key | client | min-poll poll-interval | max-poll poll-interval | [ source { ipv4 address a.b.c.d | ipv6 address X:X:X:X::X | interface interface-name } ] | server IP address [ key key ID ] | vrf vrf-name }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `authenticate` — Enables NTP authentication feature. — *Valores:* None · *Default:* Disabled
- `client` — Enables SNTP client functionality. — *Valores:* None · *Default:* Disabled
- `min-poll poll-interval` — Sets the minimum polling interval in power of two seconds. — *Valores:* 3-17 (2ˆ3 to 2ˆ17) · *Default:* 6 (2ˆ6 = 64 seconds)
- `max-poll poll-interval` — Sets the maximum polling interval in power of two seconds. — *Valores:* 3-17 (2ˆ3 to 2ˆ17) · *Default:* 10 (2ˆ10 = 1024 seconds)
- `source ipv4 address a.b.c.d` — Specifies the source IPv4 address from which NTP server connection will be established. — *Valores:* a.b.c.d · *Default:* None
- `source ipv6 address X:X:X:X::X` — Specifies the source IPv6 address from which NTP server connection will be established. — *Valores:* X:X:X:X::X · *Default:* None
- `source interface interface-name` — Specifies the interface whose IP address will be used for outgoing SNTP packets. — *Valores:* Interface name in format l3-<name> or loopback-<id>. · *Default:* None
- `vrf vrf-name` — Specifies the name of VRF in which the NTP server connection will be established. — *Valores:* VRF name. · *Default:* None
- `server IP address` — Sets the IP address of a NTP server the SNTP Client is allowed to synchronize with. Max number of servers is six. — *Valores:* a.b.c.d or X:X:X:X::X · *Default:* None
- `key key ID` — Associate the server with the given key identifier. — *Valores:* 1-4294967295. · *Default:* None
- `authentication-key key ID` — Specify the authentication key identifier. — *Valores:* 1-4294967295. · *Default:* None
- `md5 MD5 key` — Specify the key for NTP authenticated connections. — *Valores:* String value up to 20 characters. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.2 | SNTP client was introduced. Replaced parameter “poll-interval” by “min-poll” and “max-poll”. Added 3.0 IPv6 and source support. |
| 5.2 | Source interface can be selected by name. |
| 7.0 | Source interface loopback and VRF can be selected by name. |
| 8.0 | Only admin user can configure SNTP. |

**Usage Guidelines:**

Since the parameters min-poll and max-poll are defined using an exponent in power of two, in accordance to RFC 5905, the following table exemplifies the exponent converted value in different time units for a better comprehension of its impact in the configuration. Both the source ip address and source interface fields specify the source of NTP packets, and therefore cannot be configured together. To use the source interface command, the l3 interface must be configured with an IP Address. Exponent to Time Conversion Table: +-------------+-------------+ | Exponent | Time | +-------------+-------------+ | 3 | 8s | | 4 | 16s | | 5 | 32s | | 6 | 1m04s | | 7 | 2m08s | | 8 | 4m16s | | 9 | 8m32s | | 10 | 17m04s | | 11 | 34m08s | | 12 | 1h08m16s | | 13 | 2h16m32s | | 14 | 4h33m04s | | 15 | 9h06m08s | | 16 | 18h12m16s | | 17 | 36h24m32s | +-------------+-------------+ Example: Enable ntp to server 172.22.110.101 with a polling interval between 32 (2ˆ5) and 256 (2ˆ8) seconds:

```text
# config
(config)# sntp client
(config)# sntp authenticate
(config)# sntp authentication-key 1 md5 "¨?![:]21476a8*x"
(config)# sntp min-poll 5
(config)# sntp max-poll 8
(config)# sntp server 172.22.110.101 key 1
(config)# commit
```

Commit complete. Enable ntp to server 2001:DB8::1 with a polling interval between 8 (2ˆ3) and 16 (2ˆ4) seconds:

```text
# config
(config)# sntp client
(config)# sntp authenticate
(config)# sntp authentication-key 1 md5 "¨?![:]21476a8*x"
(config)# sntp min-poll 3
(config)# sntp max-poll 4
(config)# sntp server 2001:DB8::1 key 1
(config)# commit
```

Commit complete. Enable ntp to server 172.22.110.101 and source IPv4 must be 127.22.110.1:

```text
# config
(config)# sntp client
(config)# sntp server 172.22.110.101
(config)# sntp source ipv4 address 172.22.110.1
(config)# commit
```

Commit complete. Enable ntp to server 2001:DB8::100 and source IPv6 must be 2001:DB8::1:

```text
# config
(config)# sntp client
(config)# sntp server 2001:DB8::100
(config)# sntp source ipv6 address 2001:DB8::1
(config)# commit
```

Commit complete. Enable ntp to server 172.22.110.101 and source interface l3

```text
# config
(config)# interface l3 l3
(config-l3-l3)# ipv4 address 172.22.110.10/24
(config-l3-l3)# top
(config)# sntp client
(config)# sntp server 172.22.110.101
(config)# sntp source interface l3-l3
(config)# commit
```

Commit complete. Enable ntp to server 172.22.110.101 and source interface loopback

```text
# config
(config)# interface loopback-0
(config-loopback-0)# ipv4 address 172.22.110.10/24
(config-loopback-0)# top
(config)# sntp client
(config)# sntp server 172.22.110.101
(config)# sntp source interface loopback-0
(config)# commit
```

Commit complete. Enable ntp to server 172.22.110.101 and vrf green

```text
# config
(config)# vrf green
(config-vrf-green)# top
(config)# sntp client
(config)# sntp server 172.22.110.101
(config)# sntp vrf green
(config)# commit
```

Commit complete.

**Impacts and precautions:**

When source interface is used, the NTP transaction is in unsymmetric mode, i.e. the source and destination ports of NTP packets are different. This is described in RFC 958, inside 5. Protocol Operation, 5.1. Protocol Modes. The sntp source and sntp vrf configuration is applied to all server destinations, not being configurable per server.

**Hardware restrictions:**

N/A SYNCE This topic describes the commands related to management of the timing and synchronization aspects defined by SyncE Protocol, such as commands to configure and inspect sync source.


## SyncE

### `show synchronization synce quality-level`

> **Página:** 1608 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays the SyncE (Synchronous Ethernet) quality levels for all configured network interfaces. This command is used to monitor the quality levels of both transmission (TX QL) and reception (RX QL) for interfaces that support SyncE.

**Supported Platforms:** This command is supported only in the following platforms: DM4376.

**Syntax:**

```text
show synchronization synce quality-level
```

**Parameters:**

- `None` — Display SyncE quality level information. — *Valores:* N/A. · *Default:* N/A.

**Default:** None.

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. This command is useful for monitoring the SyncE quality levels assigned to interfaces in real-time. It helps ensure that the network synchronization is operating as expected. Examples: This example shows how to use the show synchronization synce quality-level command.

```text
# show synchronization synce quality-level
```

INTERFACE NAME TX QL RX QL ---------------------------------------------- ten-gigabit-ethernet-1/1/1 QL_EEC1 QL_DNU ten-gigabit-ethernet-1/1/2 QL_SSUA QL_PRC ten-gigabit-ethernet-1/1/3 QL_SSUB QL_INV If no interfaces are configured or there is an issue, the output will be: % No entries found.

**Output Terms:**

Output Description Name of the interface being monitored (e.g., ten-gigabit-ethernetINTERFACE NAME 1/1/1). Output Description The SyncE quality level of the interface’s transmission (TX), such as TX QL QL_EEC1, QL_SSUA. The SyncE quality level of the interface’s reception (RX), such as RX QL QL_DNU, QL_PRC.

**Impacts and precautions:**

The command does not alter the system state and is purely informational.

**Hardware restrictions:**

This command is only available on devices that support SyncE.


### `synchronization synce quality-level`

> **Página:** 1611 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures SyncE (Synchronous Ethernet) quality level to enable transmission and reception of ESMC packets on supported ethernet interfaces.

**Supported Platforms:** This command is supported only in the following platforms: DM4376.

**Syntax:**

```text
synchronization synce quality-level interface interface-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface-name` — Specifies the interface where the SyncE quality level will be applied. Supported interfaces must be in the format interface- <c/s/p>, where: c: Chassis number s: Slot number p: Port number Example: ten-gigabit-ethernet-1/1/1 — *Valores:* interface-chassis/slot/port · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Attempting to apply the quality level on unsupported interfaces (e.g., electrical ethernet interfaces, lag, service-port) will result in an error. See usage examples below: To configure SyncE quality level on ten-gigabit-ethernet-1/1/1 interface, the following command must be issued:

```text
(config)#
(config)# synchronization
(sync)# synce
(sync-synce)# quality-level interface ten-gigabit-ethernet-1/1/1
(sync-synce-ql-ten-gigabit-ethernet-1/1/1)# commit
```

Note that same effect is achieved by following commands:

```text
(config)#
(config)# synchronization synce quality-level interface ten-gigabit-ethernet-1/1/1
(sync-synce-ql-ten-gigabit-ethernet-1/1/1)# commit
```

To check if the configuration was applied, issue the show running-config synchronization synce command:

```text
#show running-config synchronization synce
synchronization
synce
quality-level interface ten-gigabit-ethernet-1/1/1
!
!
!
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

ESMC only works on optical interfaces. IEEE 1588 This topic describes the commands related to management of IEEE 1588 Protocol such as commands to configure Ordinary Clock, Transparent Clock or Boundary Clock parameters.


## IEEE 1588

### `show synchronization ptp`

> **Página:** 1614 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Precision Time Protocol (IEEE 1588v2).

**Supported Platforms:** This command is supported only in the following platforms: DM4376.

**Syntax:**

```text
show synchronization ptp { brief | detail | interface interface-name [ statistics ] | parent | slave }
```

**Parameters:**

- `brief` — PTP brief status. — *Valores:* N/A · *Default:* N/A
- `detail` — PTP detail status. — *Valores:* N/A · *Default:* N/A
- `interface interface-name` — List of interfaces with PTP enabled. — *Valores:* N/A · *Default:* N/A
- `statistics` — List of PTP counters of a configured PTP interface. — *Valores:* N/A · *Default:* N/A
- `parent` — PTP status parent. — *Valores:* N/A · *Default:* N/A
- `slave` — PTP status slave. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |

**Usage Guidelines:**

Let’s see the brief information:

```text
# show synchronization ptp brief
Profile OffsetFromMaster MeanPathDelay
--------------- ---------------- -------------
g8275-1 +0.000000000 +0.000000000
#
```

Let’s see the detail information:

```text
# show synchronization ptp detail
Profile OffsetFromMaster MeanPathDelay
--------------- ---------------- -------------
g8275-1 +0.000000000 +0.000000000
DeviceType TwoStepFlag ClockIdentity
---------- ----------- -----------------------
Boundary false 18:81:ed:11:99:75:00:00
ClockClass ClockAccuracy ClockVariance
---------- --------------------- -------------
248 Unknown 65535
Protocol Pri1 Pri2
---------------------- ----------- -----------
Ethernet 128 128
#
```

Let’s see the interface information:

```text
# show synchronization ptp interface gigabit-ethernet-1/1/1
PTP
INTERFACE NAME STATE
--------------------------------
gigabit-ethernet-1/1/1 Master
#
```

Let’s see the parent information:

```text
# show synchronization ptp parent
ParentClockIdentity ParentStatsComputed Variance PhaseChangeRate
----------------------- ------------------- ---------- ---------------
18:81:ed:11:99:75:00:00 false 65535 2147483647
Gm-Identity Gm-pri1 Gm-pri2
------------------------------ ----------- -----------
18:81:ed:11:99:75:00:00 128 128
Gm-ClockClass Gm-ClockAccuracy Gm-ClockVariance
------------- ----------------------- ----------------
248 Unknown 65535
#
```

Let’s see the slave information:

```text
# show synchronization ptp slave
Port ClockState ClockStateReason
---------------------------------- ------------------- ----------------
ten-gigabit-ethernet-1/1/1 Locked HYBRID_PHASE
#
```

To check PTP counters on ten-gigabit-ethernet-1/1/1 interface, the following command must be issued:

```text
#show synchronization ptp ten-gigabit-ethernet-1/1/1 statistics
```

Packet Type Received Received Processed Sent Discarded ------------------------------------------------------------------------------ Sync 0 0 0 0 Delay Request 0 0 0 0 Peer Delay Request 0 0 0 0 Peer Delay Response 0 0 0 0 Follow Up 0 0 0 0 Delay Response 0 0 0 0 Peer Delay Follow Up 0 0 0 0 Announce 0 0 0 0 Signaling 0 0 0 0 Management 0 0 0 0

**Output Terms:**

Output Description Profile The selected PTP protocol profile. OffsetFromMaster The time difference between the Slave Clock and the Master Clock. The average time it takes for a message to travel between the MasMeanPathDelay ter Clock and the Slave Clock. DeviceType The role of the device in the PTP network. TwoStepFlag Indicate whether a device is operating in one-step or two-step. ClockIdentity The unique identifier assigned to each clock in a PTP network. The value that indicates the quality, stability, and accuracy of a clock ClockClass in a PTP network. Output Description ClockAccuracy The parameter that describes the estimated accuracy of a clock. ClockVariance The measure of the stability of a clock’s time signal over a period. Protocol Indicate the used protocol layer. Pri1 This value is used to prioritize clocks in the initial selection process. This value is used as a secondary criterion when two or more clocks Pri2 have the same Priority1 value. The network interface that is used to participate in PTP communicaInterface Name tions. PTP State The operational mode. ParentClockIdentity The ClockIdentity of the parent clock in a clock hierarchy. ParentStatsComputed Indicate whether certain statistics or measurements related to the parent clock have been computed. The measure of the stability of a parent clock’s time signal over a Variance period. PhaseChangeRate The rate at which the phase (or time) of a clock is changing. Gm-Identity The unique identifier for the Grandmaster Clock in the network. Used to select the most suitable Grandmaster Clock from multiple Gm-pri1 candidates. Used to provide a secondary level of priority for selecting the GrandGm-pri2 master Clock if multiple clocks have the same GM-pri1 value. Output Description The value that indicates the quality, stability, and accuracy of the Gm-ClockClass Grandmaster Clock in a PTP network. The parameter that describes the estimated accuracy of the GrandGm-ClockAccuracy master Clock. The measure of the stability of the Grandmaster Clock’s time signal Gm-ClockVariance over a period. Port The network port on the device that is operating as a Slave Port. The operational states that a clock can be in when it is acting as a ClockState Slave Clock. The parameter used to indicate the specific reason or condition that ClockStateReason led to a particular state of the Slave Clock.

**Impacts and precautions:**

None

**Hardware restrictions:**

None


### `synchronization ptp`

> **Página:** 1620 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Precision Time Protocol (IEEE 1588v2).

**Supported Platforms:** This command is supported only in the following platforms: DM4376.

**Syntax:**

```text
synchronization ptp [ domain value ] [ priority2 priority ] synchronization ptp [ interface interface-name [ announce [ rate pps ] [timeout seconds ] ] [ delay-req-rate pps ] [ sync-rate pps ] ] synchronization ptp [ mode boundary [ encapsulation ethernet ] [ profile g8275-1 ] ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `domain value` — Clock domain for PTP. — *Valores:* 24 - 43 · *Default:* None
- `priority2 priority` — Clock priority 2 for PTP BMC algorithm (0 is highest priority). — *Valores:* 0 - 255 · *Default:* None
- `interface interface-name` — List of interfaces with PTP enabled. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port } · *Default:* None
- `announce rate pps` — Configure announce rate. — *Valores:* 8pps · *Default:* None
- `announce timeout seconds` — Configure announce timeout. — *Valores:* 3 - 10 · *Default:* None
- `delay-req-rate pps` — Configure delay-request message rate. — *Valores:* 16pps · *Default:* None
- `sync-rate pps` — Configure sync message rate. — *Valores:* 16pps · *Default:* None
- `mode boundary` — Configure mode for PTP. — *Valores:* boundary · *Default:* None
- `encapsulation ethernet` — PTP messages encapsulation. — *Valores:* ethernet · *Default:* ethernet
- `profile g8275-1` — Profile associated to PTP instance. — *Valores:* g8275-1 · *Default:* g8275-1

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. See usage examples below: To configure PTP on ten-gigabit-ethernet-1/1/1 interface, the following command must be issued:

```text
(config)#
(config)# synchronization
(sync)# ptp
(sync-ptp)# domain 24
(sync-ptp)# priority2 128
(sync-ptp)# mode boundary encapsulation ethernet profile g8275-1
(sync-ptp-bc)# exit
(sync-ptp)# interface ten-gigabit-ethernet-1/1/1
(sync-ptp-ten-gigabit-ethernet-1/1/1)# commit
```

To check if the configuration was applied, issue the show running-config synchronization ptp command:

```text
#show running-config synchronization ptp
synchronization
ptp
domain 24
mode boundary
!
priority2 128
interface ten-gigabit-ethernet-1/1/1
!
!
!
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

The interface interface-name does not accept electrical interface as parameter.


### `synchronization sync-source`

> **Página:** 1624 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Synchronization Source Hierarchies status.

**Supported Platforms:** This command is supported only in the following platforms: DM4376.

**Syntax:**

```text
show synchronization sync-source { status }
```

**Parameters:**

- `status` — This parameter displays a summary information about the status detail, selected hierarchy, clock source, quality level. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |

**Usage Guidelines:**

Let’s see the status information:

```text
# show synchronization sync-source status
```

Synchronization Source Status: Status Detail: Acquiring Selected Hierarchy: 0 Clock Source: - Quality Level: QL_NONE

```text
#
```

**Output Terms:**

Output Description Status Detail Current status. Selected Hierarchy The number of selected hierarchy. Clock Source The source of clock. Quality Level Quality level used in clock source selection.

**Impacts and precautions:**

None

**Hardware restrictions:**

None


### `synchronization sync-source`

> **Página:** 1626 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Synchronization Source Hierarchies configuration.

**Supported Platforms:** This command is supported only in the following platforms: DM4376.

**Syntax:**

```text
synchronization sync-source [ hierarchy level [ freq-clock-source { synce } interface interface-name ] ] synchronization sync-source [ selector forced { freerun | hierarchy level value | holdover } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `hierarchy level` — Configures hierarchies to synchronize the system clock with an external reference. — *Valores:* 1 - 3 · *Default:* N/A
- `freq-clock-source synce interface interface-name` — Configure external source of frequency. — *Valores:* { ten-gigabit-ethernet-chassis/slot/port } · *Default:* None
- `selector forced { freerun | hierarchy level value | holdover }` — Configures the switching mode of clock hierarchy. — *Valores:* { freerun | hierarchy level 1 - 3 | holdover } · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. See usage examples below: To configure Sync-Source, the following command must be issued:

```text
(config)#
(config)# synchronization
(sync)# synce quality-level interface ten-gigabit-ethernet-1/1/1
(sync-synce-ql-ten-gigabit-ethernet-1/1/1)# top
(config)# synchronization
(sync)# sync-source
(sync-source)# selector forced hierarchy level 1
(config-hierarchy-1)# freq-clock-source synce interface ten-gigabit-ethernet-1/1/1
(config-hierarchy-1)# commit
```

To check if the configuration was applied, issue the show running-config synchronization sync-source command:

```text
#show running-config synchronization sync-source
synchronization
sync-source
selector forced hierarchy level 1
hierarchy 1
freq-clock-source synce interface ten-gigabit-ethernet-1/1/1
!
!
synce
quality-level interface ten-gigabit-ethernet-1/1/1
!
!
!
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A.


### `synchronization transparent-clock`

> **Página:** 1629 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Transparent Clock measures the residence time (the time that the packet spends passing through the switch or the router), and adds the residence time into the correction field of the PTP packet.

**Supported Platforms:** This command is supported only in the following platforms: DM4360, DM4370.

**Syntax:**

```text
synchronization transparent-clock interface interface-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Interface with Transparent Clock enabled. — *Valores:* { gigabit-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port } · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.4 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. See usage examples below: To configure Transparent Clock on gigabit-ethernet-1/1/1 interface, the following command must be issued:

```text
(config)#
(config)# synchronization
(sync)# transparent-clock
(sync-tc)# interface gigabit-ethernet-1/1/1
(sync-tc-gigabit-ethernet-1/1/1)# commit
```

Note that same effect is achieved by following commands:

```text
(config)#
(config)# synchronization transparent-clock interface gigabit-ethernet-1/1/1
(sync-tc-gigabit-ethernet-1/1/1)# commit
```

To check if the configuration was applied, issue the show running-config synchronization transparent-clock command:

```text
#show running-config synchronization transparent-clock
synchronization
transparent-clock
interface gigabit-ethernet-1/1/1
!
!
!
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A. CHAPTER 14: GPON This chapter describes the commands related to management of GPON interfaces and remote ONUs. OLT This topic describes the global commands related to GPON OLT, service-port and service-vlan.
