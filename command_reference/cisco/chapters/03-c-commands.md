# Capítulo 3: C commands

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## A through B

### C commands

• C commands, on page 62

### C commands

### `cd`

> **Página:** 86 · **Modo:** User EXEC Privileged EXEC · **Default:** The initial default file system is flash:. For platforms that do not have a physical device named flash:, the keyword flash: is aliased to the default Flash device. For the Supervisor Engine, the initial default file system is disk0 : If you do not specify a directory on a file system, the default is the root directory on that file system. · **Leitura (show/clear/…):** não

**Description:** To change the default directory or file system, use the cd command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
cd [filesystem:][directory]
```

**Parameters (Syntax Description):**

- `filesystem :` — ( Optional) The URL or alias of the directory or filesystem s f o l low e d by a c o l on.
- `directory` — ( Optional) Name of the directory.

**Command Default:** The initial default file system is flash:. For platforms that do not have a physical device named flash:, the keyword flash: is aliased to the default Flash device. For the Supervisor Engine, the initial default file system is disk0 : If you do not specify a directory on a file system, the default is the root directory on that file system.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | This command was introduced. |
| 12.2(14)SX | This command was integrated into Cisco IOS Release12.2(14) S X, and support was introduced onthe Supervisor E n g in e720. |
| 12.2(17d)SXB | Support was added for the Supervisor Engine2. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The valid values for filesystem :are as follows: • For systems that are configured with a Supervisor Engine 2, valid values are bootflash:, const_nvram:, disk0:, flash:, nvram:, slot0:, sup-slot0:, and sup-bootflash: • For systems that are configured with a Supervisor Engine 720, valid values are disk0: and disk1: For all EXEC commands that have an optional filesystemargument, the system uses the file system specified by the cd command when you omit the optional filesystemargument. For example, the dircommand, which displays a list of files on a file system, contains an optional filesystemargument. When you omit this argument, the system lists the files on the file system specified by the cd command. If you do not specify a directory on a file system, the default is the root directory on that file system.

**Example:**

In the following example, the cd command is used to set the default file system to the Flash memory card inserted in slot 0:

```text
Router# pwd
bootflash:/
cd slot0:
pwd
slot0:/
```

Cisco 7600 Series This example sets the default file system to the Flash PC card that is inserted in disk 0:

```text
Router# cd disk0:
pwd
disk0:/
```


### `clear archive log config`

> **Página:** 87 · **Modo:** Privileged EXEC (#) · **Default:** If this command is not used, the database entries accumulate in the archive log. · **Leitura (show/clear/…):** sim

**Description:** To purge the configuration logging database entries, use the clear archive log configcommand in privileged EXEC mode.

**Syntax:**

```text
clear archive log config [force | persistent]
```

**Parameters (Syntax Description):**

- `force` — ( Optional) E l i min at e s the confirm s t e p before the c on t e n t s of the archive log are clear e d.
- `persistent` — ( Optional) Purge s the configuration logging persistent-command data b as e e n t r i e s.

**Command Default:** If this command is not used, the database entries accumulate in the archive log.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRA | This command was introduced. |
| 12.4(11)T | This command was integrated into Cisco IOS Release12.4(11) T. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B. |

**Usage Guidelines:**

When the clear archive log configcommand is entered, only the entries in the configuration logging database file are deleted. The file itself is not deleted; it will be used in the future to log new entries as they occur.

**Example:**

The following example clears the database entries that have been saved to the config log without asking you to confirm the action before the entries are cleared:

```text
Router# clear archive log config force
```


### `clear catalyst6000 traffic-meter`

> **Página:** 88 · **Modo:** Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To clear the traffic meter counters, use the clear catalyst6000 traffic-metercommand in privileged EXEC mode.

**Syntax:**

```text
clear catalyst6000 traffic-meter
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(17a)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to clear the traffic meter counters:

```text
Router# clear catalyst6000 traffic-meter
```


### `clear configuration lock`

> **Página:** 89 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To clear the lock on the running configuration file, use the clear configuration lockcommand in privileged EXEC mode.

**Syntax:**

```text
clear configuration lock
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(25)S | This command was introduced. |
| 12.3(14)T | This command was e n h an c e d to all o w the exclusive configuration lock to be clear e d d u r in g e r r at i c or a b nor m a l be h a v i or. |
| 12.0(31)S | This command was integrated into Cisco IOS Release12.0(31) S. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(31) S X H. |

**Example:**

The following is sample output from the clear configuration lockcommand when the running configuration file is not locked by the configure replace command:

```text
Router# clear configuration lock
Parser Config not locked.
```

The following is sample output from the clear configuration lockcommand when the running configuration file is locked by the configure replace command:

```text
Router# clear configuration lock
Process <3> is holding the EXCLUSIVE lock !
Do you want to clear the lock?[confirm] y
```

The following example shows how to use the clear configuration lock command to display the owner or process ID of the lock and prompt the user for confirmation:

```text
clear configuration lock
Process <46> is holding the EXCLUSIVE lock.
Do you want to clear the lock?[confirm] y
```

After the lock is cleared, a message will be sent to the terminal if the owner of the lock is a TTY user:

```text
Router(config)# The configuration lock was cleared by user <steve> from terminal <5>
```


### `clear diagnostic event-log`

> **Página:** 90 · **Modo:** Privileged EXEC (#) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To clear the diagnostic event logs for a specific module or event type, use the clear diagnostic event-logcommand in privileged EXEC mode.

**Syntax:**

```text
clear diagnostic event-log {event-type {error | info | warning} | module {num | slot subslot | all}}
```

**Parameters (Syntax Description):**

- `event-typeerror` — Specifies clear in g error events.
- `event-typeinfo` — Specifies clear in g info r m at i v e events.
- `event-typewarning` — Specifies clear in g warning events.
- `module num |slotsubslot` — Specifies clear in g events for as p e c if i c module.
- `module all` — Specifies clear in g all line card s.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SXH | This command was introduced on the Supervisor E n g in e720. |

**Usage Guidelines:**

The clear diagnostic event-log command clears all the events for all the modules. The clear diagnostic event-log module num command clears events only for a specific module. The clear diagnostic event-log event-typecommand clears only specific event types such as error, informative, or warning events.

**Example:**

This example shows how to clear error event logs:

```text
Router# clear diagnostic event-log event-type error
```

This example shows how to clear event logs on module 3:

```text
clear diagnostic event-log module 3
```

This example shows how to clear error event logs on all the modules:

```text
Router# clear diagnostic event-log module all
```


### `clear ip http client cache`

> **Página:** 91 · **Modo:** Privileged EXEC · **Default:** None · **Leitura (show/clear/…):** sim

**Description:** To remove information from the HTTP client cache, use the clear ip http client cache command in privileged EXEC mode.

**Syntax:**

```text
clear ip http client cache {all | session session-name | url complete-url}
```

**Parameters (Syntax Description):**

- `cache all` — R e m o v e s all HTTP client cache e n t r i e s.
- `cache session session-name` — Removes HTTP client cache e n t r i e s of the HTTP client ap p l i c at i on session specified by these s s i on-name argument.
- `cache url c o m p l e t e-url` — R e m o v e s the HTTP client cache entry who s e location is specified by the c o m p l e t e-url argument, a Cisco IOSFile System( IF S) U n if or m Resource L o c at or( URL), and that c on s is t s of HTML files used by an HTTPs e r v e r.

**Command Default:** None

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(31)SB2 | This command was introduced. |

**Usage Guidelines:**

Use this command to clear entries from the HTTP client cache pool: all the entries, all the entries owned by a specific session, or only the entry associated with a specific request from an HTTP server.

**Example:**

The following example clears all entries in the HTTP client cache:

```text
Router# clear ip http client cache all
```

The following example removes HTTP client cache entries that belong to the HTTP Client File System (CFS) application:

```text
Router# clear ip http client cache session HTTP CFS
```

The following example removes HTTP client cache entries at the location http://myrouter.cisco.com/flash:/:

```text
Router# clear ip http client cache url http://myrouter.cisco.com/flash:/
```


### `clear logging`

> **Página:** 92 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To clear messages from the logging buffer, use the clear logging command in privileged EXEC mode.

**Syntax:**

```text
clear logging [persistent [url filesystem:/directory]]
```

**Parameters (Syntax Description):**

- `persistent` — ( Optional) Delete s persistent logging files.
- `url` — ( Optional) Specifies the URL for s to r in g logging message s.
- `filesystem:` — The filesystem f o l low e d by a c o l on.
- `/ directory` — The directory on the filesystem. The s l as h isr e q u i r e d.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.4 | This command was modified. The persistent and url keywords, and the filesystem:/ directory arguments were added. |

**Usage Guidelines:**

The clear logging persistent command is used to remove stored audit records. This action can be performed by the audit administrator only. The clear logging persistentcommand clears only log files stored in the directory but does not remove the directory itself. If no log URL is not specified for logging, this command clears files from the location as specified in the logging persistent command.

**Example:**

In the following example, the logging buffer is cleared:

```text
Router# clear logging
Clear logging buffer [confirm]
```

The following example shows how to clear persistent logging files:

```text
Router# clear logging persistent
Delete persistent logging files from bootflash:/audit_log ? [confirm]
Router# dir bootflash:/audit_log
Directory of bootflash:/audit_log/
No files in directory
```

The following example shows how to clear persistent logging files from a specific directory:

```text
Router# clear logging persistent url harddisk:/log-persistant
Delete persistent logging files from harddisk:/log-persistent ? [confirm]
Router# dir harddisk:/log-persistant
Directory of harddisk:////log-persistent/
No files in directory
```


### `clear logging system`

> **Página:** 93 · **Modo:** User EXEC (>) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To clear event records stored in the System Event Archive (SEA) log file sea_log.dat, use the clear logging system command in user EXEC mode.

**Syntax:**

```text
clear logging system [disk name]
```

**Parameters (Syntax Description):**

- `disk name` — ( Optional) S to r e s the system event login the specified disk.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC (>)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SXH | This command was introduced. |
| 12.2(33)SCC | This command was introduced for the Ciscou B R10012 router in the Cisco IOS Software Release12.2(33) S C C. |

**Usage Guidelines:**

SEA is supported on switches that have a Supervisor Engine 32 or Supervisor Engine 720 with a compact flash adapter and a Compact Flash card (WS-CF-UPG= for Supervisor Engine 720). Cisco Universal Broadband Router 10012 The SEA feature is used to address debug trace and system console constraints. SEA is a logging feature that allows the modules in the system to report major and critical events to the route processor (RP). The events occurring on the line card or jacket card are also sent to the RP using Inter-Process Communication (IPC) capability. Use the clear logging system command to clear the event records stored in the SEA log file. Note To store the system event logs, the SEA requires either the PCMCIA ATA disk or Compact Flash Disk in compact flash adapter for PRE2.

**Example:**

This example shows how to clear the SEA:

```text
Router# clear logging system
Clear logging system operation will take a while.
Do you want to continue? [no]: yes
```


### `clear logging xml`

> **Página:** 94 · **Modo:** User EXEC Privileged EXEC · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To clear the contents of the XML system message logging (syslog) buffer, use the clear logging xml command in User EXEC or Priviledged EXEC mode..

**Syntax:**

```text
clear logging xml
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** No default behavior or values.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(15)T | This command was introduced. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(33)SRE | This command was integrated into Cisco IOS Release12.2(33) S R E . |

**Usage Guidelines:**

This command clears the contents of the XML-formatted logging buffer, but does not clear the contents of the standard logging buffer. The system will prompt you to confirm the action before clearing the buffer.

**Example:**

In the following example, the XML-specific buffer is cleared:

```text
Router# clear logging xml
Clear XML logging buffer [confirm]?
y
```


### `clear memory low-water-mark`

> **Página:** 95 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To clear the low-water-mark memory, use the clear memory low-water-markcommand in privilegedEXEC mode.

**Syntax:**

```text
clear memory low-water-mark
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced into are l e as e e a r l i e r than Cisco IOS Release 15.0(1)M. |
| 12.2(33)SRB | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRB. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was i m p l e m e n t e do n the Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Usage Guidelines:**

This command clears all processor threshold values and the input/output memory threshold values, if any.

**Example:**

The following example shows how to clear the low-water-mark memory:

```text
Router# clear memory low-water-mark
```


### `clear mls statistics`

> **Página:** 95 · **Modo:** Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To reset the Multilayer Switching (MLS) statistics counters, use the clear mls statistics command in privileged EXEC mode.

**Syntax:**

```text
clear mls statistics [module num]
```

**Parameters (Syntax Description):**

- `module num` — ( Optional) Specifies the module number.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.(17d)SXB1 | This command was introduced on the Supervisor E n g in e720 and the Supervisor Engine 2. |
| 12.2(17d)SXB5 | The module n u m keyword and argument p a i r were added. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command replaces the clear mls stats command, which was introduced on the Supervisor Engine 720 in Cisco IOS Release 12.2(17a)SX, and on the Supervisor Engine 2 in Cisco IOS Release 12.2(17d)SXB.

**Example:**

This example shows how to reset the MLS statistics counters for all modules:

```text
clear mls statistics
```

This example shows how to reset the MLS statistics counters for a specific module:

```text
clear mls statistics module 5
```


### `clear parser cache`

> **Página:** 96 · **Modo:** Privileged EXEC · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To clear the parse cache entries and hit/miss statistics stored for the Parser Cache feature, use the clear parser cachecommand in privileged EXEC mode.

**Syntax:**

```text
clear parser cache
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** No default behavior or values.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.1(5)T | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The Parser Cache feature optimizes the parsing (translation and execution) of Cisco IOS software configuration command lines by remembering how to parse recently encountered command lines, decreasing the time required to process large configuration files. The clear parser cache command will free the system memory used by the Parser Cache feature and will erase the hit/miss statistics stored for the output of the show parser statistics EXEC command. This command is only effective when the Parser Cache feature is enabled.

**Example:**

The following example shows the clearing of the parser cache:

```text
Router# show parser statistics
Last configuration file parsed:Number of Commands:1484, Time:820 ms
Parser cache:enabled, 1460 hits, 26 misses
Router# clear parser cache
Router# show parser statistics
Last configuration file parsed:Number of Commands:1484, Time:820 ms
Parser cache:enabled, 0 hits, 1 misses
```


### `clear parser statistics`

> **Página:** 97 · **Modo:** Privileged EXEC · **Default:** No default behavior or values. · **Leitura (show/clear/…):** sim

**Description:** To clear the parser performance statistics, use the clear parser statisticscommand in privileged EXEC mode.

**Syntax:**

```text
clear parser statistics
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** No default behavior or values.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0S | This command was introduced. |

**Usage Guidelines:**

The clear parser statistics command will free the system memory used for recording parser performance statistics stored for the output of the show parser statistics EXEC command..

**Example:**

The following example shows the clearing parser statistics:

```text
Router# show parser statistics
Last configuration file parsed: Number of Commands: 1, Time: 31 ms
Parser cache: enabled, 129 hits, 46 misses
Active startup time: 0
Standby startup time: 186
Copy to running-config time:0
Bulksync time:0
Top 10 slowest command:
Function Time (ms) Command
0xE71F90 7 shutdown
0x1235280 11 no ip address
0x1235280 11 no ip address
0x1235280 11 no ip address
0x1235280 11 no ip address
0x1235280 12 no ip address
0x1235280 12 no ip address
0x1235280 12 no ip address
0x1235280 12 no ip address
0xD6C940 6170 show run
Parser last bootup cache hits:
Bootup hits:125
Bootup misses:43
Bootup clear parser cache:0
clear parser statistics
func=E01730, duration=0 cmd= clear parser statistics
Router# show parser statistics
Last configuration file parsed: Number of Commands: 0, Time: 0 ms
Parser cache: enabled, 130 hits, 47 misses
Active startup time: 0
Standby startup time: 0
Copy to running-config time:0
Bulksync time:0
Top 10 slowest command:
Function Time (ms) Command
Parser last bootup cache hits:
Bootup hits:0
Bootup misses:0
Bootup clear parser cache:0
```


### `clear platform netint`

> **Página:** 99 · **Modo:** Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To clear the interrupt-throttling counters for the platform, use the clear platform netint command in privileged EXEC mode.

**Syntax:**

```text
clear platform netint
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(17b)SXA | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release 12.2(17d)SXB. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to clear the interrupt-throttling counters for the platform:

```text
clear platform netint
```


### `clear processes interrupt mask`

> **Página:** 99 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To clear interrupt mask details for all processes in the interrupt mask buffer, use the clear processes interrupt mask detailcommand in privileged EXEC mode.

**Syntax:**

```text
clear processes interrupt mask detail
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(2)T | This command was introduced as p a r to f the Process Interrupt Mask Profile r E n h an c e m e n t f e at u r e. |

**Usage Guidelines:**

See the documentation of the scheduler interrupt mask commands (listed in the Related Commands table) for further details on process interrupt mask profiling.

**Example:**

The following example demonstrates how to the clear interrupt mask statistics from system memory for all processes:

```text
clear processes interrupt mask detail
```


### `clear scp accounting`

> **Página:** 100 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To clear the Switch-Module Configuration Protocol (SCP) accounting information, use the clear scp accountingcommand in privilegedEXEC mode.

**Syntax:**

```text
clear scp accounting
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced into are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release12.2(33) S X I. |

**Example:**

The following example shows how to clear the SCP accounting information:

```text
Router# clear scp accounting
```


### `clear tcp`

> **Página:** 101 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To clear a TCP connection, use the clear tcpcommand in privileged EXEC mode.

**Syntax:**

```text
clear tcp {line line-number | local hostname port remote hostname port | tcb address}
```

**Parameters (Syntax Description):**

- `line line-number` — Linenumber of the TCP connection to clear.
- `local hostname port remote hostname port` — Hostname of the l o c a l router and port and hostname of the remote router and port of the TCP connection to clear.
- `tcb address` — T r an s m is s i on Control B lock( T C B) address of the TCP connection to clear. The T C B address is an in t e r n a l id e n t if i e r for the end p o in t.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The clear tcp command is particularly useful for clearing hung TCP connections. The clear tcp line line-numbercommand terminates the TCP connection on the specified tty line. Additionally, all TCP sessions initiated from that tty line are terminated. The clear tcp local hostname port remote hostname portcommand terminates the specific TCP connection identified by the host name and port pair of the local and remote router. The clear tcp tcb address command terminates the specific TCP connection identified by the TCB address.

**Example:**

The following example clears a TCP connection using its tty line number. The show tcp command displays the line number (tty2) that is used in the clear tcp command.

```text
Router# show tcp
tty2, virtual tty from host router20.cisco.com
Connection state is ESTAB, I/O status: 1, unread input bytes: 0
Local host: 171.69.233.7, Local port: 23
Foreign host: 171.69.61.75, Foreign port: 1058
Enqueued packets for retransmit: 0, input: 0, saved: 0
Event Timers (current time is 0x36144):
Timer Starts Wakeups Next
Retrans 4 0 0x0
TimeWait 0 0 0x0
AckHold 7 4 0x0
SendWnd 0 0 0x0
KeepAlive 0 0 0x0
GiveUp 0 0 0x0
PmtuAger 0 0 0x0
iss: 4151109680 snduna: 4151109752 sndnxt: 4151109752 sndwnd: 24576
irs: 1249472001 rcvnxt: 1249472032 rcvwnd: 4258 delrcvwnd: 30
SRTT: 710 ms, RTTO: 4442 ms, RTV: 1511 ms, KRTT: 0 ms
minRTT: 0 ms, maxRTT: 300 ms, ACK hold: 300 ms
Router# clear tcp line 2
[confirm]
[OK]
```

The following example clears a TCP connection by specifying its local router host name and port and its remote router host name and port. The show tcp brief command displays the local (Local Address) and remote (Foreign Address) host names and ports to use in the clear tcp command.

```text
Router# show tcp brief
TCB Local Address Foreign Address (state)
60A34E9C router1.cisco.com.23 router20.cisco.1055 ESTAB
Router# clear tcp local router1 23 remote router20 1055
[confirm]
[OK]
```

The following example clears a TCP connection using its TCB address. The show tcp brief command displays the TCB address to use in the clear tcp command.

```text
Router# show tcp brief
TCB Local Address Foreign Address (state)
60B75E48 router1.cisco.com.23 router20.cisco.1054 ESTAB
Router# clear tcp tcb 60B75E48
[confirm]
[OK]
```


### `clear vlan counters`

> **Página:** 102 · **Modo:** Privileged EXEC (#) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To clear the software-cached counter values to start from zero again for a specified VLAN or all existing VLANs, use the clear vlan counters command in privileged EXEC mode.

**Syntax:**

```text
clear vlan [vlan-id] counters
```

**Parameters (Syntax Description):**

- `vlan-id` — ( Optional) The ID of as p e c if i c VLAN. Range:1 to4094.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If you do not specify a vlan-id; the software-cached counter values for all existing VLANs are cleared.

**Example:**

This example shows how to clear the software-cached counter values for a specific VLAN:

```text
Router# clear vlan 10 counters
Clear "show vlan" counters on this vlan [confirm]y
```


### `clock`

> **Página:** 103 · **Modo:** Interface configuration · **Default:** auto · **Leitura (show/clear/…):** não

**Description:** To configure the port clocking mode for the 1000BASE-T transceivers, use the clock command in interface configuration mode. To return to the default settings,use the no form of this command.

**Syntax:**

```text
clock {auto | active [prefer] | passive [prefer]}
no clock
```

**Parameters (Syntax Description):**

- `auto` — Enable s the automatic-clock configuration.
- `active` — Enable s the a c t i v e o p e r at i on.
- `prefer` — ( Optional) N e g o t i at e s the specified mode with the f are n do f the link.
- `passive` — Enable s the passive o p e r at i on.

**Command Default:** auto

**Command Modes:** Interface configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(17a)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is supported on the 1000BASE-T transceivers only. If the clock mode of the near end of a link does not match the clock mode of the far end, the line protocol does not come up. The active and passive clock status is determined during the auto negotiation process before the transmission link is established. The clock command supports the following configurations: • auto --Auto negotiates with the far end of the link but preference is given to the active-clock switch. • active --Uses a local clock to determine transmitter-operation timing. • passive --Recovers the clock from the received signal and uses the recovered clock to determine transmitter-operation timing. • active prefer --Auto negotiates with the far end of the link but preference is given to the active-clock switch. • passive prefer --Auto negotiates with the far end of the link but preference is given to the passive-clock switch. Enter the show running-config interface command to display the current clock mode. Enter the show interfaces command to display the clock mode that is negotiated by the firmware.

**Example:**

This example shows how to enable the active-clock operation:

```text
Router(config-if)# clock active
Router(config-if)#
```


### `clock initialize nvram`

> **Página:** 104 · **Modo:** Global configuration (config) · **Default:** By default, the system clock is set to restart from the last known system clock value for platforms that have no hardware calendar. · **Leitura (show/clear/…):** não

**Description:** To restart the system clock from the last known system clock value, use the clock initialize nvramcommand in global configuration mode. To disable the restart of the system clock from the last known system clock value, use the no form of this command.

**Syntax:**

```text
clock initialize nvram
no clock initialize nvram
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** By default, the system clock is set to restart from the last known system clock value for platforms that have no hardware calendar.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(4)T | This command was introduced. |

**Usage Guidelines:**

For platforms that have hardware calendars, the clock initialize nvram command is not available. When the no form of the command is configured, the system clock gets initialized to default standard values. The default values can be either 1MAR1993 or 1MAR2002.

**Example:**

The following example shows how to set the system clock to restart from the last known system clock value:

```text
Router(config)# clock initialize nvram
```


### `config-register`

> **Página:** 105 · **Modo:** Global configuration · **Default:** Refer to the documentation for your platform for the default configuration register value. For many newer platforms, the default is 0x2102, which causes the router to boot from Flash memory and the Break key to be ignored. · **Leitura (show/clear/…):** não

**Description:** To change the configuration register settings, use the config-register command in global configuration mode.

**Syntax:**

```text
config-register value
```

**Parameters (Syntax Description):**

- `value` — Hexadecimal or decimal value that r e p r e s e n t s the16-b it configuration register value that you w an t to use then e x t time the router isr e start e d. The value range is from0 x0 to0 x FFFF(0to65535in decimal).

**Command Default:** Refer to the documentation for your platform for the default configuration register value. For many newer platforms, the default is 0x2102, which causes the router to boot from Flash memory and the Break key to be ignored.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(31)SB2 | This command was integrated into Cisco IOS Release12.2(31) S B2. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(31) S X H. |

**Usage Guidelines:**

This command applies only to platforms that use a software configuration register. The lowest four bits of the configuration register (bits 3, 2, 1, and 0) form the boot field. The boot field determines if the router boots manually, from ROM, or from Flash or the network. To change the boot field value and leave all other bits set to their default values, follow these guidelines: • If you set the configuration register boot field value to 0x0, you must boot the operating system manually with the boot command. • If you set the configuration register boot field value to 0x1, the router boots using the default ROM software. • If you set the configuration register boot field to any value from 0x2 to 0xF, the router uses the boot field value to form a default boot filename for booting from a network server. For more information about the configuration register bit settings and default filenames, refer to the appropriate router hardware installation guide. Note In a virtual switch application, If you have configured your config-register with a value that would skip file parsing during the bootup process, your change to either a standalone or virtual switch will not take place until you reconfigure your config-register. The config-register must be allowed to parse files in order to ensure the conversion from either a standalone or virtual switch.

**Example:**

In the following example, the configuration register is set to boot the system image from Flash memory:

```text
config-register 0x2102
```


### `configure check syntax`

> **Página:** 106 · **Modo:** Privileged EXEC (#) · **Default:** The syntax configuration is not checked. · **Leitura (show/clear/…):** não

**Description:** To check the syntax configuration, use the configure check syntax commandinprivilegedEXEC mode.

**Syntax:**

```text
configure check syntax [source-location]
```

**Parameters (Syntax Description):**

- `source-location` — ( Optional) Location or the address of the source to be check e d.

**Command Default:** The syntax configuration is not checked.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |
| 12.2(33)SRB | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release12.2(33) SRB. |

**Example:**

The following example shows how to check the syntax configuration using the configure check syntax command:

```text
configure check syntax revrcsf:
```


### `configuration mode exclusive`

> **Página:** 107 · **Modo:** Global configuration (config) · **Default:** Single-user mode is disabled. · **Leitura (show/clear/…):** não

**Description:** Note Effective with Cisco IOS XE Release 3.1S, the configuration mode exclusive command is replaced by the parser command serializer command. See the parser command serializer command for more information. To enable single-user (exclusive) access functionality for the Cisco CLI, use the configuration mode exclusive command in global configuration mode. To disable the single-user access (configuration locking) feature, use the no form of this command.

**Syntax:**

```text
configuration mode exclusive {auto | manual} [expire seconds] [lock-show] [interleave] [terminate]
[config-wait seconds] [retry-wait seconds]
no configuration mode exclusive
```

**Parameters (Syntax Description):**

- `auto` — Automatic all y limit s configuration to single-user mode.
- `manual` — All o w s you to m an u all y limit the configuration file to single-user mode.
- `expire seconds` — ( Optional) Specifies then u m be r of s e c on d s in which the configuration lock isr e l e as e d after the users to p s m a k in g configuration c h an g e s.
- `lock-show` — ( Optional) G i v e s priority to configuration commands being execute d from the exclusive configuration session, and p r events the exec u t i on of show commands.
- `in t e r l e a v e` — ( Optional) All o w s show commands from sessions that are not hold in gt h e configuration lock to be execute d when the user in these s s i on hold in gt h e configuration lock is not m a k in g configuration c h an g e s. Note If you enter e d the lock-show keyword, you should enter this keyword.
- `terminate` — ( Optional) Cause s the configuration command execute d from the exclusive configuration session to terminate show and clear commands being execute d in other sessions.
- `config-wait seconds` — ( Optional) Specifies the a mount of time, in s e c on d s, that a configuration command enter e d by a user in single user mode wait s for show commands enter e d by other users to f in is h being execute d. If the show command is s t i l l being execute d when the timer e x p i r e s and if the terminate option is set, the configuration command terminate s the show command. If the configuration command c o m p l e t e s exec u t i on before the specified number of s e c on d s, the show command begin s exec u t i on.
- `retry-wait seconds` — ( Optional) Specifies the a mount of time, in s e c on d s, that show and clear EXEC commands will wait for a configuration command enter e d by a user in exclusive configuration mode to c o m p l e tee x e c u t i on. If the configuration command is s t i l l being execute d when the specified a mount of time has pass e d, the EXEC commands generate an error message and are terminate d. If exec u t i on of the configuration command is c o m p l e t e d before the specified number of s e c on d s, the EXEC commands are execute d.

**Command Default:** Single-user mode is disabled.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(14)T | This command was introduced. |
| 12.0(31)S | This command was integrated into Cisco IOS Release12.0(31) S. The following keywords were added: config-wait, e x p i r e, in t e r l e a v e, lock-show, retry-wait, and terminate. N e w f u n c t i on a l it y was added, in c l u d in g Access Session Locking. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| 15.0(1)S | This command was d e p r e c at e d for Cisco IOS Release15.0(1) S. |
| CiscoIOSXERelease3.1S | This command was replaced by the parser commands e r i a l i z e r command. |

**Usage Guidelines:**

Note As of the 15.0 release, the configuration mode exclusive command is no longer available on the S and T trains. The configuration mode exclusive command enables the exclusive configuration lock feature. The exclusive configuration lock allows single-user access to configuration modes using single-user configuration mode. While the device configuration is locked, no other users can enter configuration commands. Users accessing the device using the state-full, session-based transports (telnet, Secure Shell (SSH) are able to enter single-user configuration mode. The user enters single-user configuration mode by acquiring the exclusive configuration lock using the configure terminal lock privileged EXEC mode command. The configuration lock is released when the user exits configuration mode by using the end or exit command, or by pressing Ctrl-Z. While a user is in single-user configuration mode, no other users can configure the device. Users accessing Command Line Interface (CLI) options through stateless protocols (that is, the HTTP web-based user interface) cannot access single-user configuration mode. (However, an Application Programming Interface (API) allows the stateless transports to lock the configuration mode, complete its operations, and release the lock.)

**Example:**

The following example shows how to configure the configuration file for single-user autoconfiguration mode by using the configuration mode exclusive auto command. Use the configuration terminal command to enter global configuration mode and lock the configuration mode exclusively. After the Cisco configuration mode is locked exclusively, you can verify this configuration by entering the show configuration lock command.

```text
Device# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Device(config)# configuration mode exclusive auto
Device(config)# end
Device# show running-configuration
| include config
Building configuration...
Current configuration : 2296 bytes
configuration mode exclusive auto <========== auto policy
Device#
configure terminal ?
<======== lock option not displayed when in auto policy
Device# configure terminal
<======= acquires the lock
```

The configuration mode is locked exclusively. The lock is cleared after you exit from configuration mode by entering the end or exit command.

```text
Enter configuration commands, one per line. End with CNTL/Z.
Device(config)#
Device(config)#
show configuration lock
Parser Configure Lock
---------------------
Owner PID : 3
User : unknown
TTY : 0
Type : EXCLUSIVE
State : LOCKED
Class : EXPOSED
Count : 1
Pending Requests : 0
User debug info : configure terminal
Session idle state : TRUE
No of exec cmds getting executed : 0
No of exec cmds blocked : 0
Config wait for show completion : FALSE
Remote ip address : Unknown
Lock active time (in Sec) : 6
Lock Expiration timer (in Sec) : 593
Device(config)#
Device(config)# end
<========= releases the lock
Device#
Device# show configuration lock
Parser Configure Lock
---------------------
Owner PID : -1
User : unknown
TTY : -1
Type : NO LOCK
State : FREE
Class : unknown
Count : 0
Pending Requests : 0
User debug info :
Session idle state : TRUE
No of exec cmds getting executed : 0
No of exec cmds blocked : 0
Config wait for show completion : FALSE
Remote ip address : Unknown
Lock active time (in Sec) : 0
Lock Expiration timer (in Sec) : 0
```

The following example shows how to enable the exclusive locking feature in manual mode by using the configuration mode exclusive manual command. Once you have configured manual exclusive mode, you can lock the configuration mode by using the configure terminal lock command. In this mode, the configure terminal command does not automatically lock the parser configuration mode. The lock is cleared after you exit from configuration mode by entering the end or exit command.

```text
Device# configure terminal
Configuration mode locked exclusively. The lock will be cleared once you exit out of
configuration mode using end/exit
Enter configuration commands, one per line. End with CNTL/Z.
Device(config)# configuration mode exclusive manual
Device(config)# end
Device#
Device# show running-configuration
| include configuration
Building configuration...
Current configuration : 2298 bytes
configuration mode exclusive manual <==== 'manual' policy
Device# show configuration lock
Parser Configure Lock
---------------------
Owner PID : -1
User : unknown
TTY : -1
Type : NO LOCK
State : FREE
Class : unknown
Count : 0
Pending Requests : 0
User debug info :
Session idle state : TRUE
No of exec cmds getting executed : 0
No of exec cmds blocked : 0
Config wait for show completion : FALSE
Remote ip address : Unknown
Lock active time (in Sec) : 0
Lock Expiration timer (in Sec) : 0
Device#
Device# configure terminal ?
lock Lock configuration mode <========= 'lock' option displayed in 'manual' policy
Device# configure terminal <============ ‘configure terminal’ won't acquire lock automatically
Enter configuration commands, one per line. End with CNTL/Z.
Device(config)# show configuration lock
Parser Configure Lock
---------------------
Owner PID : -1
User : unknown
TTY : -1
Type : NO LOCK
State : FREE
Class : unknown
Count : 0
Pending Requests : 0
User debug info :
Session idle state : TRUE
No of exec cmds getting executed : 0
No of exec cmds blocked : 0
Config wait for show completion : FALSE
Remote ip address : Unknown
Lock active time (in Sec) : 0
Lock Expiration timer (in Sec) : 0
Device(config)#
end
Device# show configuration lock
Parser Configure Lock
---------------------
Owner PID : -1
User : unknown
TTY : -1
Type : NO LOCK
State : FREE
Class : unknown
Count : 0
Pending Requests : 0
User debug info :
Session idle state : TRUE
No of exec cmds getting executed : 0
No of exec cmds blocked : 0
Config wait for show completion : FALSE
Remote ip address : Unknown
Lock active time (in Sec) : 0
Lock Expiration timer (in Sec) : 0
Device#
Device# configure
Device# configure terminal
Device#
configure terminal ?
lock Lock configuration mode <======= 'lock' option displayed when in 'manual' policy
Device# configure terminal lock
Device# configure terminal lock
<============ acquires exclusive configuration lock
```

Configuration mode is locked exclusively. The lock is cleared after you exit from configuration mode by entering the end or exit command. Enter configuration commands, one per line. End with CNTL/Z.

```text
Device(config)# show configuration lock
Parser Configure Lock
---------------------
Owner PID : 3
User : unknown
TTY : 0
Type : EXCLUSIVE
State : LOCKED
Class : EXPOSED
Count : 1
Pending Requests : 0
User debug info : configure terminal lock
Session idle state : TRUE
No of exec cmds getting executed : 0
No of exec cmds blocked : 0
Config wait for show completion : FALSE
Remote ip address : Unknown
Lock active time (in Sec) : 5
Lock Expiration timer (in Sec) : 594
Device(config)# end
<================ 'end' releases exclusive configuration lock
Device# show configuration lock
Parser Configure Lock
---------------------
Owner PID : -1
User : unknown
TTY : -1
Type : NO LOCK
State : FREE
Class : unknown
Count : 0
Pending Requests : 0
User debug info :
Session idle state : TRUE
No of exec cmds getting executed : 0
No of exec cmds blocked : 0
Config wait for show completion : FALSE
Remote ip address : Unknown
Lock active time (in Sec) : 0
Lock Expiration timer (in Sec) : 0
Device#
```


### `configure confirm`

> **Página:** 113 · **Modo:** Privileged EXEC (#) · **Default:** The replacement of the current running configuration with a saved configuration file is not confirmed. · **Leitura (show/clear/…):** não

**Description:** To confirm replacement of the current running configuration with a saved Cisco configuration file, use the

**Syntax:**

```text
configure confirm command in privileged EXEC mode.
configure confirm
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** The replacement of the current running configuration with a saved configuration file is not confirmed.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(7)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2 S. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2 S B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2 S R. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2 S X. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

The configure confirm command is used only if the time seconds keyword and argument of the configure replace command are specified. If the configure confirm command is not entered within the specified time limit, the configuration replace operation is automatically reversed (in other words, the current running configuration file is restored to the configuration state that existed prior to entering the configure replace command).

**Example:**

The following example shows the use of the configure replace command with the time seconds keyword and argument. You must enter the configure confirm command within the specified time limit to confirm replacement of the current running configuration file:

```text
Device# configure replace nvram:startup-config time 120
This will apply all necessary additions and deletions
to replace the current running configuration with the
contents of the specified configuration file, which is
assumed to be a complete configuration, not a partial
configuration. Enter Y if you are sure you want to proceed. ? [no]: Y
Total number of passes: 1
Rollback Done
Device# configure confirm
```


### `configure memory`

> **Página:** 114 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To configure the system from the system memory, use the configure memory command in privileged EXEC mode.

**Syntax:**

```text
configure memory
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

On all platforms except Class A Flash file system platforms, this command executes the commands located in the configuration file in NVRAM (the “startup configuration file”). On Class A Flash file system platforms, if you specify the configure memory command, the router executes the commands pointed to by the CONFIG_FILE environment variable. The CONFIG_FILE environment variable specifies the location of the configuration file that the router uses to configure itself during initialization. The file can be located in NVRAM or any of the Flash file systems supported by the platform. When the CONFIG_FILE environment variable specifies NVRAM, the router executes the NVRAM configuration only if it is an entire configuration, not a distilled version. A distilled configuration is one that does not contain access lists. To view the contents of the CONFIG_FILE environment variable, use the show bootvar EXEC command. To modify the CONFIG_FILE environment variable, use the boot config command and then save your changes by issuing the copy system:running-config nvram:startup-config command.

**Example:**

In the following example, a router is configured from the configuration file in the memory location pointed to by the CONFIG_FILE environment variable:

```text
Router# configure memory
```


The configure network command was replaced by the copy{rcp| tftp} running-config command in Cisco IOS Release 11.0. To maintain backward compatibility, the configure network command continues to function in Cisco IOS Release 12.2(11)T for most systems, but support for this command may be removed in a future release. The copy{rcp| tftp} running-config command was replaced by the copy {ftp: | rcp: | tftp:}[filename] system: running-config command in Cisco IOS Release 12.1. The copy {ftp: | rcp: | tftp:}[filename] system: running-config command specifies that a configuration file should be copied from a FTP, rcp, or TFTP source to the running configuration. See the description of the copy command in this chapter for more information. The configure overwrite-network has been replaced by the copy {ftp-url | rcp-url | tftp-url nvram:startup-config command. See the description of the copycommand in the Cisco IOS File System Commands chapter for more information.

### `configure replace`

> **Página:** 115 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To replace the current running configuration with a saved Cisco configuration file, use the configure replace command in privileged EXEC mode.

**Syntax:**

```text
configure replace target-url [nolock] list force ignorecase [revert trigger [error] [timer minutes]
| time minutes]
```

**Parameters (Syntax Description):**

- `target-url` — URL( access i b l e by the Cisco filesystem) of the save d Cisco configuration file that is to replace the current running configuration.
- `nolock` — ( Optional) Disable s the lock in g of the running configuration file that p r events other users from c h an g in gt h e running configuration d u r in g a configuration replace o p e r at i on.
- `list` — D is p l a y s a list of the command lines ap p l i e d by the Cisco software parser d u r in g each pass of the configuration replace o p e r at i on. The to t a l number of pass e s perf or m e d is also d is p l a y e d.
- `force` — Replace s the current running configuration file with the specified save d Cisco configuration file with out prompt in g you for confirm at i on.
- `i g nor e c as e` — In s t r u c t s the configuration to i g nor e the c as e of the configuration confirm at i on.
- `revert t r i g g e r` — ( Optional) Set s the t r i g g e r s for revert in gt o the original configuration. •( Optional) error: Revert s to the original configuration upon error. •( Optional) timer min u t e s: Revert s to the original configuration if the specified time elapses.
- `time minutes` — ( Optional) Time( in min u t e s) with in which you must enter the configure confirm command to confirm replace m e n to f the current running configuration file. If the configure confirm command is note n t e r e d with in the specified time limit, the configuration replace o p e r at i on is automatic all y r e v e r s e d( in other w or d s, the current running configuration file isr e s to r e d to the configuration state that e x is t e d p r i or to enter in gt h e configure replace command).

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(7)T | This command was introduced. |
| 12.2(25)S | Then o lock keyword was added. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(31)SB2 | This command was i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |
| 12.4(20)T | The revert and t r i g g e r keywords were added. |
| 12.2(33)SRC | The i g nor e c as e keyword was added. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| CiscoIOSXERelease3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

When you are configuring more than one keyword option, the following rules apply: • The list keyword must be entered before the force and time keywords. • The force keyword must be entered before the time keyword. If the current running configuration is replaced with a saved Cisco configuration file that contains commands that are not accepted by the Cisco software parser, an error message is displayed that lists the commands that were not accepted. The total number of passes performed in the configuration replace operation is also displayed. In Cisco IOS Release 12.2(25)S, a locking feature for the configuration replace operation was introduced. When the configure replace command is enabled, the Cisco running configuration file is locked by default for the duration of the configuration replace operation. This locking mechanism prevents other users from changing the running configuration while the replace operation is taking place, which avoids the replace operation from terminating unsuccessfully. You can disable the locking of the running configuration by using the configure replace nolock command. The running configuration lock is automatically cleared at the end of the configuration replace operation. You are not expected to clear the lock manually during the replace operation, but as a protection against any unforeseen circumstances, you can manually clear the lock by using the clear configuration lock command. You can also display any locks that are currently applied to the running configuration by using the show configuration lock command. Note You cannot replace the controller configuration of the T1 E1 card by using the configure replace command. Replacing the Current Running Configuration with a Saved Cisco Configuration File The following example shows how to replace the current running configuration with a saved Cisco configuration file named disk0:myconfig. Note that the configure replace command interactively prompts you to confirm the operation.

```text
Device# configure replace disk0:myconfig
This will apply all necessary additions and deletions
to replace the current running configuration with the
contents of the specified configuration file, which is
assumed to be a complete configuration, not a partial
configuration. Enter Y if you are sure you want to proceed. ? [no]:
Y
Total number of passes: 1
Rollback Done
```

In the following example, the list keyword is specified to display the command lines that were applied during the configuration replace operation:

```text
Device# configure replace disk0:myconfig list
This will apply all necessary additions and deletions
to replace the current running configuration with the
contents of the specified configuration file, which is
assumed to be a complete configuration, not a partial
configuration. Enter Y if you are sure you want to proceed. ? [no]: Y
!Pass 1
!List of Commands:
no snmp-server community public ro
snmp-server community mystring ro
end
Total number of passes: 1
Rollback Done
```

Reverting to the Startup Configuration File The following example shows how to revert to the Cisco startup configuration file. This example also shows the use of the optional force keyword to override the interactive user prompt.

```text
Device#
configure replace nvram:startup-config force
Total number of passes: 1
Rollback Done
```

Performing a Configuration Replace Operation with the configure confirm Command The following example shows the use of the configure replace command with the time seconds keyword and argument. You must enter the configure confirm command within the specified time limit to confirm replacement of the current running configuration file. If the configure confirm command is not entered within the specified time limit, the configuration replace operation is automatically reversed (in other words, the current running configuration file is restored to the configuration state that existed prior to entering the configure replace command).

```text
Device# configure replace nvram:startup-config time 120
This will apply all necessary additions and deletions
to replace the current running configuration with the
contents of the specified configuration file, which is
assumed to be a complete configuration, not a partial
configuration. Enter Y if you are sure you want to proceed. ? [no]: Y
Total number of passes: 1
Rollback Done
Device# configure confirm
```

Performing a Configuration Rollback Operation The following example shows how to make changes to the current running configuration and then rollback the changes. As a part of the configuration rollback operation, you must save the current running configuration before making changes to the file. In this example, the archive config command is used to save the current running configuration. Note that the generated output of the configure replace command indicates that only one pass was performed to complete the rollback operation. Note The path command must be configured before using the archive config command. You first save the current running configuration in the configuration archive as follows:

```text
Device# archive config
```

You then enter configuration changes as shown in the following example:

```text
Device#
configure terminal
Device(config)#
user netops2 password rain
Device(config)# user netops3 password snow
Device(config)# exit
```

After making changes to the running configuration file, you should rollback these changes and revert to the configuration that was present prior to making changes. The show archive command is used to verify the version of the configuration that needs to be used as a target file. The configure replace command is then used to revert to the target configuration file as shown in the following example:

```text
Device#
show archive
There are currently 1 archive configurations saved.
The next archive file will be named disk0:myconfig-2
Archive # Name
1 disk0:myconfig-1 <- Most Recent
Device# configure replace disk0:myconfig-1
Total number of passes: 1
Rollback Done
```


### `configure revert`

> **Página:** 119 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To cancel the timed rollback and trigger the rollback immediately, or to reset the parameters for the timed rollback, use the configure revert command in privileged EXEC mode.

**Syntax:**

```text
configure revert {now | timer {minutes | idle minutes}}
```

**Parameters (Syntax Description):**

- `now` — Can c e l s the time d rollback and revert s i m m e d i at e l y.
- `timer` — Reset s the confirm at i on timer.
- `minutes` — Time in min u t e s(1-120).
- `idle minutes` — Id l e time in min u t e s(1-120) for which to wait before rollback.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRC | This command was introduced. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.4(20)T | This command was integrated into Cisco IOS Release12.4(20) T. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

In order to use the configure revert command to configure a timed rollback, the Configuration Archive functionality must be enable first. The Configuration Archive APIs are used to store the current configuration before applying any changes or rolling back to the previous configuration. In case of multi-user environments, only the user who enabled the timed rollback functionality will have the permission to perform the following operations: • Confirm the configuration change • Reset the timer • Cancel the timer and trigger rollback immediately

**Example:**

The following example shows how to cancel the timed rollback and revert to the saved configuration immediately:

```text
Device(config)#
archive
Device(config-archive)#
path disk0:abc
Device#
configure revert now
```


### `configure terminal`

> **Página:** 121 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To enter global configuration mode, use the configure terminal command in privileged EXEC mode. Cisco IOS Releases 12.3(14)T and Subsequent Releases: Cisco IOS Releases 12.2(33)SRC and Subsequent Releases:

**Syntax:**

```text
configure terminal
configure terminal [lock]
configure terminal [revert {timer minutes | idle minutes}]
```

**Parameters (Syntax Description):**

- `lock` — ( Optional) Lock s the running configuration into exclusive configuration mode for the d u r at i on of your configuration session. This keyword only f u n c t i on s if the configuration mode exclusive command was previous l y enabled.
- `revert` — ( Optional) Set s the parameters for revert in gt h e configuration if confirm at i on of then e w configuration is not r e c e i v e d.
- `timer min u t e s` — Time in min u t e s(1-120) for which to wait for confirm at i on.
- `id l e min u t e s` — Id l e time in min u t e s(1-120) for which to wait for confirm at i on.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.3(14)T | The lock keyword option was added. |
| 12.0(31)S | This command was integrated into Cisco IOS Release12.0(31) S. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.4(20)T | The revert keyword option was added, a l on g with the timer parameters of id l e and min u t e s. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Use this command to enter global configuration mode. Note that commands in this mode are written to the running configuration file as soon as you enter them (using the Enter key/Carriage Return). After you enter the configure terminal command, the system prompt changes from <device-name># to <device-name>(config)# , indicating that the device is in global configuration mode. To leave global configuration mode and return to privileged EXEC mode, type exit or press Ctrl-Z. To view the changes to the configuration you have made, use the more system:running-config command or show running-config command in user EXEC or privileged EXEC mode. Configuration Locking The first user to enter the configure terminal lock command acquires the configuration lock (exclusive configuration mode).

**Example:**

The following example shows how to enter global configuration mode and lock the Cisco software in exclusive mode:

```text
Device(config)# configure terminal lock
Enter configuration commands, one per line. End with CNTL/Z.
Device(config)#
```


### `confreg`

> **Página:** 122 · **Modo:** ROM monitor · **Default:** Refer to your platform documentation for the default configuration register value. · **Leitura (show/clear/…):** não

**Description:** To change the configuration register settings while in ROM monitor mode, use the confreg command in ROM monitor mode.

**Syntax:**

```text
confreg [value]
```

**Parameters (Syntax Description):**

- `value` — ( Optional) Hexadecimal value that r e p r e s e n t s the16-b it configuration register value that you w an t to use then e x t time the router isr e start e d. The value range is from0 x0 to0 x FFFF.

**Command Default:** Refer to your platform documentation for the default configuration register value.

**Command Modes:** ROM monitor

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Not all versions in the ROM monitor support this command. Refer to your platform documentation for more information on ROM monitor mode. If you use this command without specifying the configuration register value, the router prompts for each bit of the configuration register. The lowest four bits of the configuration register (bits 3, 2, 1, and 0) form the boot field. The boot field determines if the router boots manually, from ROM, or from Flash or the network. To change the boot field value and leave all other bits set to their default values, follow these guidelines: • If you set the configuration register boot field value to 0x0, you must boot the operating system manually with the boot command. • If you set the configuration register boot field value to 0x1, the router boots using the default ROM software. • If you set the configuration register boot field to any value from 0x2 to 0xF, the router uses the boot field value to form a default boot filename for booting from a network server. For more information about the configuration register bit settings and default filenames, refer to the appropriate router hardware installation guide.

**Example:**

In the following example, the configuration register is set to boot the system image from Flash memory:

```text
confreg 0x210F
```

In the following example, no configuration value is entered, so the system prompts for each bit in the register:

```text
rommon 7 > confreg
Configuration Summary
enabled are:
console baud: 9600
boot: the ROM Monitor
do you wish to change the configuration? y/n [n]: y
enable "diagnostic mode"? y/n [n]: y
enable "use net in IP bcast address"? y/n [n]:
enable "load rom after netboot fails"? y/n [n]:
enable "use all zero broadcast"? y/n [n]:
enable "break/abort has effect"? y/n [n]:
enable "ignore system config info"? y/n [n]:
change console baud rate? y/n [n]: y
enter rate: 0 = 9600, 1 = 4800, 2 = 1200, 3 = 2400 [0]: 0
change the boot characteristics? y/n [n]: y
enter to boot:
0 = ROM Monitor
1 = the boot helper image
2-15 = boot system
[0]: 0
Configuration Summary
enabled are:
diagnostic mode
console baud: 9600
boot: the ROM Monitor
do you wish to change the configuration? y/n [n]:
You must reset or power cycle for new config to take effect.
rommon 8>
```


### `continue (ROM monitor)`

> **Página:** 124 · **Modo:** ROM monitor · **Default:** No default behavior or values. · **Leitura (show/clear/…):** não

**Description:** To return to EXEC mode from ROM monitor mode, use the continue command in ROM monitor mode. continue

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** No default behavior or values.

**Command Modes:** ROM monitor

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to return to EXEC mode from ROM monitor mode, to use the system image instead of reloading. On older platforms, the angle bracket (< >) indicates that the router is in ROM monitor mode. On newer platforms, rommon number> is the default ROM monitor prompt. Typically, the router is in ROM monitor mode when you manually load a system image or perform diagnostic tests. Otherwise, the router will most likely never be in this mode. Caution While in ROM monitor mode, the Cisco IOS system software is suspended until you issue either a reset or the continue command.

**Example:**

In the following example, the continue command switches the router from ROM monitor to EXEC mode:

```text
> continue
```


### `copy`

> **Página:** 125 · **Modo:** Privileged EXEC (#) Diagnostic (diag) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To copy any file from a source to a destination, use the copy command in privileged EXEC or diagnostic mode. Please note that the copy command does not yet support the handling of wildcards in order to specify multiple files as part of source-url.

**Syntax:**

```text
copy [/erase] [/verify | /noverify] source-url destination-url
```

**Parameters (Syntax Description):**

- `/erase` — ( Optional) Erase s the destination filesystem before copy in g. Note This option is t y p i c all y p r o v id e do n platform s with limit e d memory to all o w for an e as y w a y to clear l o c a l flash memory space.
- `/verify` — ( Optional) V e r if i e s the d i g it a l s i g n at u r e of the destination file. If v e r if i c at i on f a i l s, the file is delete d from the destination filesystem. This option ap p l i e s to Cisco IOS software image files only.
- `/ noverify` — ( Optional) If the file being c o p i e d is an image file, this keyword disable s the automatic image v e r if i c at i on that o c c u r s after an image is c o p i e d. Note This keyword is of t e n is s u e d if the file verify auto command is enabled, which automatic all y v e r if i e s the d i g it a l s i g n at u r e of all image s that are c o p i e d.
- `source-url` — The location URL( or alias) of the source file or directory to be c o p i e d. The source can be e it h e r l o c a l or remote, d e p end in g upon whether the file is being download e do r u p load e d.
- `destination-url` — The destination URL( or alias) of the c o p i e d file or directory. The destination can be e it h e r l o c a l or remote, d e p end in g upon whether the file is being download e do r u p load e d. The exact format of the source and destination URLs varies a c c or d in g to the file or directory location. You
- `may` — enter either an alias keyword for a p a r t i c u l a r file or a file name that follows the s t and a r d Cisco IOS file
- `system` — syntax (filesystem :[/filepath ][/filename ]). The table below shows two keyword s h or t c u t s to URLs.
- `running-config` — ( Optional) Keyword alias for the system: running-config URL. The system: running-config keyword r e p r e s e n t s the current running configuration file. This keyword does not w or k in more and show file EXEC commands y n t a x e s.
- `startup-config` — ( Optional) Keyword alias for then v r a m: startup-config URL. Then v r a m: startup-config keyword r e p r e s e n t s the configuration file used d u r in g in it i a l i z at i on( startup). This file is c on t a in e d in NVRAM for all platform s e x c e p t the Cisco7000 f a m i l y, which uses the CONFIG_ FILE environment v a r i a b l e to specify the startup configuration. The Cisco4500 s e r i e scan not use the copy running-config startup-config command. This keyword does not w or k in more and show file EXEC commands y n t a x e s. The following tables list URL prefix keywords by file system type. The a v a i l a b l e file systems will vary by platform. If you do not specify a URL prefix keyword, the router looks for a file in the current directory. The table below lists URL prefix keywords for Special ( o p a q u e) file systems.
- `cns:` — Source URLfor Cisco Network in g Service s files.
- `flh:` — Source URL for flash load help e r logfile s.
- `logging` — Source URL which c o p i esm e s s age s from the logging buffer to a file.
- `modem:` — Destination URL for load in g modem f i r m w are onto supported network in g device s.
- `null:` — N u l l destination for c o p i e s or files. You can copy are m o t e file to n u l l to d e t e r min e its size.
- `nvram:` — Router NVRAM. You can copy the startup configuration to NVRAM or from NVRAM.
- `obfl:` — Source or destination URLfor Onboard Failure Logging files.
- `s t by-nvram:` — Router NVRAM on the s t and by hardware. You can copy the startup configuration to NVRAM orfrom NVRAM.
- `s t by-o b f l:` — Source or destination URLfor Onboard Failure Logging files on the s t and by hardware.
- `system:` — Source or destination URL for system memory, which include s the running configuration.
- `tar:` — Source URL for the archive filesystem.
- `tmpsys:` — Source or destination URL for the t e m p or a r y system files.
- `xmodem:` — Source or destination for a file from an e two r k machine that uses the Xmodem p r o to c o l.
- `ymodem:` — Source or destination for a file from an e two r k machine that uses the Ymodem p r o to c o l. The table belows lists URL prefix keywords for remote file systems.
- `ftp:` — Source or destination URLfor FTP network server. The syntax for this alias is as f o l low s: ftp:[[[// username[: password]@] location]/ directory]/ file name.
- `http://` — Source or destination URL for an HTTPs e r v e r( also c all e d a web server). The syntax for this alias is as f o l low s: http://[[ username: password]@]{ hostname| host-ip}[/ file path]/ file name
- `https://` — Source or destination URLfora Secure HTTP( HTTPS) server. HTTPS uses Secure Socket Layer ( S S L) e n c r y p t i on. The syntax for this alias is as f o l low s: https://[[ username: password]@]{ hostname | host-ip}[/ file path]/ file name
- `rcp:` — Source or destination URL for are m o t e copy p r o to c o l( rcp) network server. The syntax for this alias is as f o l low s: rcp:[[[// username@] location]/ directory]/ file name
- `scp:` — Source or destination URL for an e two r k server that support s Secure Shell( S S H) and accept s c o p i e s of files using these c u r e copy p r o to c o l( scp). The syntax for this alias is as f o l low s: scp:// username@ location[/ directory][/ file name]
- `tftp:` — Source or destination URLfora TFTP network server. The syntax for this alias is as f o l low s: tftp:[[// location]/ directory]/ file name. The table below lists URL prefix keywords for local w r it a b l e storage file systems.
- `Alias` — Source or Destination
- `bootflash:` — Source or destination URL for bootflash memory.
- `disk0: and disk1:` — Source or destination URL of disk-b as e d m e d i a.
- `flash:` — Source or destination URL for flash memory. This alias is a v a i l a b l e on all platform s. For platform s that l a c k a flash: device, note that flash: is alias e d to slot0:, all o w in g you to r e f e r to the m a in flash memory s to r age are a on all platform s.
- `h a r d disk:` — Source or destination URL of the a c t i v e h a r d disk filesystem.
- `slave bootflash:` — Source or destination URL for in t e r n a l flash memory on these c on d a r y R S P card of a router configure d for HSA.
- `slave r a m:` — NVRAM on as e c on d a r y R S P card of a router configure d for HSA.
- `slave slot0:` — Source or destination URL of the first P e r s on a l C o m p u t e r Memory Card International As s o c i at i on( PCM C I A) card on as e c on d a r y R S P card of a router configure d for HSA.
- `slave slot1:` — Source or destination URL of these c on d PCM C I As l o to n as e c on d a r y R S P card of a router configure d for HSA.
- `slot0:` — Source or destination URL of the first PCM C I A flash memory card.
- `slot1:` — Source or destination URL of these c on d PCM C I A flash memory card.
- `s t by-bootflash:` — Source or destination URL for bootflash memory in s t and by RP.
- `s t by-h a r d disk:` — Source or destination URL for the s t and by h a r d disk.
- `Alias` — Source or Destination
- `s t by-usb[0-1]:` — Source or destination URL for the U n i v e r s a l Serial Bus( USB) flash d r i v e that has been p l u g g e d into the router and is l o c at e do n the s t and by RP.
- `usb[0-1]:` — Source or destination URL for the U n i v e r s a l Serial Bus( USB) flash d r i v e that has been p l u g g e d into the router and is l o c at e do n the a c t i v e RP.
- `usbflash 0 9 :` — Source or destination URL for the U n i v e r s a l Serial Bus( USB) flash d r i v e that has been p l u g g e d into the router.
- `usbtoken[09]:` — Source or destination URL for the USBe Token that has been p l u g g e d into the router.

**Command Modes:** Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3T | This command was introduced. |
| 12.3(2)T | • The http:// and https:// keywords were added as supported remote source location s( filesystem URL pref i x e s) for files. • This command was e n h an c e d to support copy in g files to servers that support S S H and the scp. |
| 12.2(14)S | This command was integrated into Cisco IOS Release12.2(14) S. |
| 12.2(18)S | The/ verify and/ noverify keywords were added. |
| 12.0(26)S | The/ verify and/ noverify keywords were integrated into Cisco IOS Release 12.0(26)S. |
| 12.3(4)T | The/ verify and/ noverify keywords were integrated into Cisco IOS Release 12.3(4)T. |
| 12.3(7)T | The http:// and https:// keywords were e n h an c e d to support file u p load s. |
| 12.3(14)T | The usb flash09: and usbtoken09: keywords were added to support USB storage. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(25)SG | This command was integrated into Cisco IOS Release12.2(25) S G. |
| 12.4(11)T | This command was integrated into the Cisco7200 V X R N P E-G2 platform. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| CiscoIOSXERelease2.1 | The Cisco AS R1000 s e r i e s routers be c a m e a v a i l a b l e, and introduced the copy command in diagnostic mode. |
| CiscoIOSXERelease3.9S | The command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

The fundamental function of the copy command is to allow you to copy a file (such as a system image or configuration file) from one location to another location. The source and destination for the file is specified using a Cisco IOS File System URL, which allows you to specify any supported local or remote file location. The file system being used (such as a local memory source, or a remote server) dictates the syntax used in the command. The copy command copies only one file at a time. The command does not allow you to copy multiple files. You can enter on the command line all necessary source- and destination-URL information and the username and password to use, or you can enter the copy command and have the router prompt you for any missing information. For local file systems, two commonly used aliases exist for the system:running-config and nvram:startup-config files; these aliases are running-config and startup-config, respectively. Any software that supports RFC1738 does not allow user name, path, or filename with pattern %xy, where (where x and y are any two hexa values 0-f, 0-F) Timesaver Aliases are used to reduce the amount of typing you need to perform. For example, it is easier to type copy run start (the abbreviated form of the copy running-config startup-config command) than it is to type copy system:r nvram:s (the abbreviated form of the copy system:running-config nvram:startup-configcommand). These aliases also allow you to continue using some of the common commands used in previous versions of Cisco IOS software. Note When authorization is turned on for the copy (filesystem:[/filepath][/filename]) running-config command, only the copy command is authorized. The individual commands available in the copied file are not authorized. The entire copying process may take several minutes and differs from protocol to protocol and from network to network. The colon is required after the file system URL prefix keywords (such as flash). In some cases, file system prefixes that did not require colons in earlier software releases are allowed for backwards compatibility, but use of the colon is recommended. In the URL syntax for ftp:, http:, https:, rcp:, scp: and tftp:, the location is either an IP address or a host name. The filename is specified relative to the directory used for file transfers. The following sections contain usage guidelines for the following topics: Understanding Invalid Combinations of Source and Destination Some invalid combinations of source and destination exist. Specifically, you cannot copy: • From a running configuration to a running configuration • From a startup configuration to a startup configuration • From a device to the same device (for example, the copy flash: flash: command is invalid) Understanding Character Descriptions The table below describes the characters that you may see during processing of the copycommand.

| Character | Description |
| --- | --- |
| ! | Fornetworktransfers,anexclamationpointindicatesthatthecopyprocessistakingplace.Each exclamationpointindicatesthesuccessfultransferoftenpackets(512byteseach). |
| . | Fornetworktransfers,aperiodindicatesthatthecopyprocesstimedout.Manyperiodsinarow typicallymeanthatthecopyprocessmayfail. |
| O | Fornetworktransfers,anuppercaseOindicatesthatapacketwasreceivedoutoforderandthe copyprocessmayfail. |
| e | Forflasherasures,alowercaseeindicatesthatadeviceisbeingerased. |
| E | AnuppercaseEindicatesanerror.Thecopyprocessmayfail. |
| V | AseriesofuppercaseVsindicatestheprogressduringtheverificationoftheimagechecksum. |

Understanding Partitions You cannot copy an image or configuration file to a flash partition from which you are currently running. For example, if partition 1 is running the current system image, copy the configuration file or image to partition 2. Otherwise, the copy operation will fail. You can identify the available flash partitions by entering the show file system EXECcommand. Using rcp The rcp requires a client to send a remote username upon each rcp request to a server. When you copy a configuration file or image between the router and a server using rcp, the Cisco IOS software sends the first valid username it encounters in the following sequence: 1. The remote username specified in the copy command, if a username is specified. 2. The username set by the ip rcmd remote-username global configuration command, if the command is configured. 3. The remote username associated with the current tty (terminal) process. For example, if the user is connected to the router through Telnet and was authenticated through the username command, the router software sends the Telnet username as the remote username. 4. The router host name. For the rcp copy request to process, an account must be defined on the network server for the remote username. If the network administrator of the destination server did not establish an account for the remote username, this command will not run. If the server has a directory structure, the configuration file or image is written to or copied from the directory associated with the remote username on the server. For example, if the system image resides in the home directory of a user on the server, specify that username as the remote username. If you are writing to the server, the rcp server must be properly configured to accept the rcp write request from the user on the router. For UNIX systems, add an entry to the .rhosts file for the remote user on the rcp server. Suppose the router contains the following configuration lines:

```text
hostname Rtr1
ip rcmd remote-username User0
```

If the router IP address translates to Router1.company.com, then the .rhosts file for User0 on the rcp server should contain the following line:

```text
Router1.company.com Rtr1
```

Refer to the documentation for your rcp server for more details. If you are using a personal computer as a file server, the computer must support the remote shell protocol (rsh). Using FTP The FTP protocol requires a client to send a username and password with each FTP request to a remote FTP server. Use the ip ftp username and ip ftp password global configuration commands to specify a default username and password for all copy operations to or from an FTP server. Include the username in the copy command syntax if you want to specify a username for that copy operation only. When you copy a file from the router to a server using FTP, the Cisco IOS software sends the first valid username that it encounters in the following sequence: 1. The username specified in the copy command, if a username is specified. 2. The username set by the ip ftp username command, if the command is configured. 3. Anonymous. The router sends the first valid password in the following list: 1. The password specified in the copy command, if a password is specified. The password set by the command, if the command is configured. 2. ip ftp password 3. The router forms a password username@routername.domain. The variable username is the username associated with the current session, routername is the configured host name, and domain is the domain of the router. The username and password must be associated with an account on the FTP server. If you are writing to the server, the FTP server must be properly configured to accept the FTP write request from the user on the router. Note The Syslog message will display 'xxxx' in place of the password entered in the syntax of the copy {ftp:} command. If the server has a directory structure, the configuration file or image is written to or copied from the directory associated with the username on the server. For example, if the system image resides in the home directory of a user on the server, specify that username as the remote username. Refer to the documentation for your FTP server for details on setting up the server. Using HTTP or HTTPS Copying a file to or from a remote HTTP or HTTPS server, to or from a local file system, is performed using the embedded Secure HTTP client that is integrated in Cisco IOS software. The HTTP client is enabled by default. Downloading files from a remote HTTP or HTTPS server is performed using the HTTP client integrated in Cisco IOS software. If a username and password are not specified in the copy command syntax, the system uses the default HTTP client username and password, if configured. When you copy a file from a remote HTTP or HTTPS server, the Cisco IOS software sends the first valid username that it encounters in the following sequence: 1. The username specified in the copy command, if a username is specified. 2. The username set by the ip http client username command, if the command is configured. 3. Anonymous. The router sends the first valid password in the following list: 1. The password specified in the copy command, if a password is specified. 2. The password set by the ip http client password command, if the command is configured. 3. The router forms the password username@routername.domain. The variable username is the username associated with the current session, routername is the configured host name, and domain is the domain of the router. Storing Images on Servers Use the copy flash: destination-urlcommand (for example, copy flash: tftp:) to copy a system image or boot image from flash memory to a network server. You can use the copy of the image as a backup copy. Also, you can also use the image backup file to verify that the image in flash memory is the same as that in the original file. Copying from a Server to Flash Memory Use the copy destination-url flash: command (for example, copy tftp: flash:) to copy an image from a server to flash memory. On Class B file system platforms, the system provides an option to erase existing flash memory before writing onto it. Note Verify the image in flash memory before booting the image. Verifying Images When copying a new image to your router, you should confirm that the image was not corrupted during the copy process. You can verify the integrity of the image in any of the following ways: • Depending on the destination file system type, a checksum for the image file may be displayed when the copy command completes. You can verify this checksum by comparing it to the checksum value provided for your image file on Cisco.com. Caution If the checksum values do not match, do not reboot the router. Instead, reissue the copycommand and compare the checksums again. If the checksum is repeatedly wrong, copy the original image back into flash memory beforeyou reboot the router from flash memory. If you have a corrupted image in flash memory and try to boot from flash memory, the router will start the system image contained in ROM (assuming booting from a network server is not configured). If ROM does not contain a fully functional system image, the router might not function and will need to be reconfigured through a direct console port connection. • Use the /verifykeyword. • Enable automatic image verification by default by issuing the file verify auto command. This command will automatically check the integrity of each file that is copied via the copy command (without specifying the /verifyoption) to the router unless the /noverify keyword is specified. • Use the UNIX 'diff' command. This method can also be applied to file types other than Cisco IOS images. If you suspect that a file is corrupted, copy the suspect file and the original file to a UNIX server. (The file names may need to be modified if you try to save the files in the same directory.) Then run the UNIX 'diff' command on the two files. If there is no difference, then the file has not been corrupted. Copying a Configuration File from a Server to the Running Configuration Use the copy {ftp: | rcp: | scp: | tftp: running-configcommand to load a configuration file from a network server to the running configuration of the router. (Note that running-config is the alias for the system:running-config keyword.) The configuration will be added to the running configuration as if the commands were typed in the command-line interface (CLI). Thus, the resulting configuration file will be a combination of the previous running configuration and the loaded configuration file, with the loaded configuration file having precedence. You can copy either a host configuration file or a network configuration file. Accept the default value of host to copy and load a host configuration file containing commands that apply to one network server in particular. Enter network to copy and load a network configuration file containing commands that apply to all network servers on a network. Copying a Configuration File from a Server to the Startup Configuration Use the copy {ftp: | rcp: | scp: | tftp:} nvram:startup-configcommand to copy a configuration file from a network server to the router startup configuration. These commands replace the startup configuration file with the copied configuration file. Storing the Running or Startup Configuration on a Server Use the copy system:running-config {ftp: | rcp: | scp: | tftp:} command to copy the current configuration file to a network server using FTP, rcp, scp, or TFTP. Use the copy nvram:startup-config {ftp: | rcp: | scp: | tftp:} command to copy the startup configuration file to a network server. The configuration file copy can serve as a backup copy. Saving the Running Configuration to the Startup Configuration Use the copy system:running-config nvram:startup-config command to copy the running configuration to the startup configuration. Note Some specific commands might not get saved to NVRAM. You will need to enter these commands again if you reboot the machine. These commands are noted in the documentation. We recommend that you keep a listing of these settings so you can quickly reconfigure your router after rebooting. If you issue the copy system:running-config nvram:startup-configcommand from a bootstrap system image, a warning will instruct you to indicate whether you want your previous NVRAM configuration to be overwritten and configuration commands to be lost. This warning does not appear if NVRAM contains an invalid configuration or if the previous configuration in NVRAM was generated by a bootstrap system image. On all platforms except Class A file system platforms, the copy system:running-config nvram:startup-config command copies the currently running configuration to NVRAM. On the Class A flash file system platforms, the copy system:running-config nvram:startup-config command copies the currently running configuration to the location specified by the CONFIG_FILE environment variable. This variable specifies the device and configuration file used for initialization. When the CONFIG_FILE environment variable points to NVRAM or when this variable does not exist (such as at first-time startup), the software writes the current configuration to NVRAM. If the current configuration is too large for NVRAM, the software displays a message and stops executing the command. When the CONFIG_FILE environment variable specifies a valid device other than nvram: (that is, flash:, bootflash:, slot0:, or slot1:), the software writes the current configuration to the specified device and filename, and stores a distilled version of the configuration in NVRAM. A distilled version is one that does not contain access list information. If NVRAM already contains a copy of a complete configuration, the router prompts you to confirm the copy. Using CONFIG_FILE, BOOT, and BOOTLDR Environment Variables For the Class A flash file system platforms, specifications are as follows: • The CONFIG_FILE environment variable specifies the configuration file used during router initialization. • The BOOT environment variable specifies a list of bootable images on various devices. • The BOOTLDR environment variable specifies the flash device and filename containing the rxboot image that ROM uses for booting. • Cisco 3600 routers do not use a dedicated boot helper image (rxboot), which many other routers use to help with the boot process. Instead, the BOOTLDR ROM monitor environment variable identifies the flash memory device and filename that are used as the boot helper; the default is the first system image in flash memory. To view the contents of environment variables, use the show bootvar EXEC command. To modify the CONFIG_FILE environment variable, use the boot config global configuration command. To modify the BOOTLDR environment variable, use the boot bootldr global configuration command. To modify the BOOT environment variable, use the boot system global configuration command. To save your modifications, use the copy system:running-config nvram:startup-configcommand. When the destination of a copy command is specified by the CONFIG_FILE or BOOTLDR environment variable, the router prompts you for confirmation before proceeding with the copy. When the destination is the only valid image in the BOOT environment variable, the router also prompts you for confirmation before proceeding with the copy. Using the Copy Command with the Dual RSP Feature The Dual RSP feature allows you to install two Route Switch Processor (RSP) cards in a single router on the Cisco 7507 and Cisco 7513 platforms. On a Cisco 7507 or Cisco 7513 router configured for Dual RSPs, if you copy a file to nvram:startup-configuration with automatic synchronization disabled, the system prompts whether you also want to copy the file to the secondary startup configuration. The default answer is yes. If automatic synchronization is enabled, the system automatically copies the file to the secondary startup configuration each time you use a copy command with nvram:startup-configuration as the destination. Using the copy command with the ASR1000 Series Routers The copy command is available in both privileged EXEC and diagnostic mode on the Cisco ASR1000 series routers. Because the copycommand is available in diagnostic mode, it can be used to copy all types of files between directories and remote locations even in the event of an IOS failure.

**Example:**

The following examples illustrate uses of the copy command: Verifying the Integrity of the Image Before It Is Copied Example The following example shows how to specify image verification before copying an image:

```text
Router# copy /verify tftp://10.1.1.1/cisco/c7200-js-mz disk0:
Destination filename [c7200-js-mz]?
Accessing tftp://10.1.1.1/cisco/c7200-js-mz...
Loading cisco/c7200-js-mz from 10.1.1.1 (via FastEthernet0/0):!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[OK - 19879944 bytes]
19879944 bytes copied in 108.632 secs (183003 bytes/sec)
Verifying file integrity of disk0:/c7200-js-mz
...................................................
...................................................................................................
...................................................................................................
.......................................Done!
Embedded Hash MD5 :CFA258948C4ECE52085DCF428A426DCD
Computed Hash MD5 :CFA258948C4ECE52085DCF428A426DCD
CCO Hash MD5 :44A7B9BDDD9638128C35528466318183
Signature Verified
```

Copying an Image from a Server to Flash Memory Examples The following examples use a copy rcp:, copy tftp:, or copy ftp: command to copy an image file from a server to flash memory: Copying an Image from a Server to Flash Memory Example The following example copies a system image named file1 from the remote rcp server with an IP address of 172.16.101.101 to flash memory. On Class B file system platforms, the Cisco IOS software allows you to first erase the contents of flash memory to ensure that enough flash memory is available to accommodate the system image.

```text
copy rcp://netadmin@172.16.101.101/file1 flash:file1
Destination file name [file1]?
Accessing file 'file1' on 172.16.101.101...
Loading file1 from 172.16.101.101 (via Ethernet0): ! [OK]
Erase flash device before writing? [confirm]
Flash contains files. Are you sure you want to erase? [confirm]
Copy 'file1' from server
as 'file1' into Flash WITH erase? [yes/no] yes
Erasing device... eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee...erased
Loading file1 from 172.16.101.101 (via Ethernet0): !
[OK - 984/8388608 bytes]
Verifying checksum... OK (0x14B3)
Flash copy took 0:00:01 [hh:mm:ss]
```

Copying an Image from a Server to a Flash Memory Using Flash Load Helper Example The following example copies a system image into a partition of flash memory. The system will prompt for a partition number only if there are two or more read/write partitions or one read-only and one read/write partition and dual flash bank support in boot ROMs. If the partition entered is not valid, the process terminates. You can enter a partition number, a question mark (?) for a directory display of all partitions, or a question mark and a number (? number) for directory display of a particular partition. The default is the first read/write partition. In this case, the partition is read-only and has dual flash bank support in boot ROM, so the system uses flash Load Helper.

```text
Router# copy tftp: flash:
System flash partition information:
Partition Size Used Free Bank-Size State Copy-Mode
1 4096K 2048K 2048K 2048K Read Only RXBOOT-FLH
2 4096K 2048K 2048K 2048K Read/Write Direct
[Type ?<no> for partition directory; ? for full directory; q to abort]
Which partition? [default = 2]
**** NOTICE ****
Flash load helper v1.0
This process will accept the copy options and then terminate
the current system image to use the ROM based image for the copy.
Routing functionality will not be available during that time.
If you are logged in via telnet, this connection will terminate.
Users with console access can see the results of the copy operation.
---- ******** ----
Proceed? [confirm]
System flash directory, partition 1:
File Length Name/status
1 3459720 master/igs-bfpx.100-4.3
[3459784 bytes used, 734520 available, 4194304 total]
Address or name of remote host [255.255.255.255]? 172.16.1.1
Source file name?
master/igs-bfpx-100.4.3
Destination file name [default = source name]?
Loading master/igs-bfpx.100-4.3 from 172.16.1.111: !
Erase flash device before writing? [confirm]
Flash contains files. Are you sure? [confirm]
Copy 'master/igs-bfpx.100-4.3' from TFTP server
as 'master/igs-bfpx.100-4.3' into Flash WITH erase? [yes/no] yes
```

Copying an Image from a Server to a Flash Memory Card Partition Example The following example copies the file c3600-i-mz from the rcp server at IP address 172.23.1.129 to the flash memory card in slot 0 of a Cisco 3600 series router, which has only one partition. As the operation progresses, the Cisco IOS software prompts you to erase the files on the flash memory PC card to accommodate the incoming file. This entire operation takes 18 seconds to perform, as indicated at the end of the example.

```text
Router# copy rcp: slot0:
PCMCIA Slot0 flash
Partition Size Used Free Bank-Size State Copy Mode
1 4096K 3068K 1027K 4096K Read/Write Direct
2 4096K 1671K 2424K 4096K Read/Write Direct
3 4096K 0K 4095K 4096K Read/Write Direct
4 4096K 3825K 270K 4096K Read/Write Direct
[Type ?<no> for partition directory; ? for full directory; q to abort]
Which partition? [default = 1]
PCMCIA Slot0 flash directory, partition 1:
File Length Name/status
1 3142288 c3600-j-mz.test
[3142352 bytes used, 1051952 available, 4194304 total]
Address or name of remote host [172.23.1.129]?
Source file name? /tftpboot/images/c3600-i-mz
Destination file name [/tftpboot/images/c3600-i-mz]?
Accessing file '/tftpboot/images/c3600-i-mz' on 172.23.1.129...
Connected to 172.23.1.129
Loading 1711088 byte file c3600-i-mz: ! [OK]
Erase flash device before writing? [confirm]
Flash contains files. Are you sure you want to erase? [confirm]
Copy '/tftpboot/images/c3600-i-mz' from server
as '/tftpboot/images/c3600-i-mz' into Flash WITH erase? [yes/no]
yes
Erasing device... eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee ...erased
Connected to 172.23.1.129
Loading 1711088 byte file c3600-i-mz:
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Verifying checksum... OK (0xF89A)
Flash device copy took 00:00:18 [hh:mm:ss]
```

Saving a Copy of an Image on a Server Examples The following examples use copy commands to copy image files to a server for storage: Copy an Image from Flash Memory to an rcp Server Example The following example copies a system image from flash Memory to an rcp server using the default remote username. Because the rcp server address and filename are not included in the command, the router prompts for it.

```text
copy flash: rcp:
IP address of remote host [255.255.255.255]? 172.16.13.110
Name of file to copy? gsxx
writing gsxx - copy complete
```

Copy an Image from Flash Memory to an SSH Server Using scp Example The following example shows how to use scp to copy a system image from flash memory to a server that supports SSH:

```text
Router# copy flash:c4500-ik2s-mz.scp scp://user1@host1/
Address or name of remote host [host1]?
Destination username [user1]?
Destination filename [c4500-ik2s-mz.scp]?
Writing c4500-ik2s-mz.scp
Password:
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

Before you can use the server-side functionality, SSH, authentication, and authorization must be properly configured so the router can determine whether a user is at the right privilege level. The scp server-side functionality is configured with the ip scp server enable command. Copy an Image from a Partition of Flash Memory to a Server Example The following example copies an image from a particular partition of flash memory to an rcp server using a remote username of netadmin1. The system will prompt if there are two or more partitions. If the partition entered is not valid, the process terminates. You have the option to enter a partition number, a question mark (?) for a directory display of all partitions, or a question mark and a number (? number) for a directory display of a particular partition. The default is the first partition.

```text
Router# configure terminal
Router# ip rcmd remote-username netadmin1
end
copy flash: rcp:
System flash partition information:
Partition Size Used Free Bank-Size State Copy-Mode
1 4096K 2048K 2048K 2048K Read Only RXBOOT-FLH
2 4096K 2048K 2048K 2048K Read/Write Direct
[Type ?<number> for partition directory; ? for full directory; q to abort]
Which partition? [1] 2
System flash directory, partition 2:
File Length Name/status
1 3459720 master/igs-bfpx.100-4.3
[3459784 bytes used, 734520 available, 4194304 total]
Address or name of remote host [ABC.CISCO.COM]?
Source file name? master/igs-bfpx.100-4.3
Destination file name [master/igs-bfpx.100-4.3]?
Verifying checksum for 'master/igs-bfpx.100-4.3' (file # 1)... OK
Copy 'master/igs-bfpx.100-4.3' from Flash to server
as 'master/igs-bfpx.100-4.3'? [yes/no] yes
!!!!...
Upload to server done
Flash copy took 0:00:00 [hh:mm:ss]
```

Copying an Image from a Flash Memory File System to an FTP Server Example The following example copies the file c3600-i-mz from partition 1 of the flash memory card in slot 0 to an FTP server at IP address 172.23.1.129:

```text
Router# show slot0: partition 1
PCMCIA Slot0 flash directory, partition 1:
File Length Name/status
1 1711088 c3600-i-mz
[1711152 bytes used, 2483152 available, 4194304 total]
Router# copy slot0:1:c3600-i-mz ftp://myuser:mypass@172.23.1.129/c3600-i-mz
Verifying checksum for '/tftpboot/cisco_rules/c3600-i-mz' (file # 1)... OK
Copy '/tftpboot/cisco_rules/c3600-i-mz' from Flash to server
as 'c3700-i-mz'? [yes/no] yes
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Upload to server done
Flash device copy took 00:00:23 [hh:mm:ss]
```

Copying an Image from Boot Flash Memory to a TFTP Server Example The following example copies an image from boot flash memory to a TFTP server:

```text
copy bootflash:file1 tftp://192.168.117.23/file1
Verifying checksum for 'file1' (file # 1)... OK
Copy 'file1' from Flash to server
as 'file1'? [yes/no]
y
!!!!...
Upload to server done
Flash copy took 0:00:00 [hh:mm:ss]
```

Copying a Configuration File from a Server to the Running Configuration Example The following example copies and runs a configuration filename host1-confg from the netadmin1 directory on the remote server with an IP address of 172.16.101.101:

```text
copy rcp://netadmin1@172.16.101.101/host1-confg system:running-config
Configure using host1-confg from 172.16.101.101? [confirm]
Connected to 172.16.101.101
Loading 1112 byte file host1-confg:![OK]
%SYS-5-CONFIG: Configured from host1-config by rcp from 172.16.101.101
```

Copying a Configuration File from a Server to the Startup Configuration Example The following example copies a configuration file host2-confg from a remote FTP server to the startup configuration. The IP address is 172.16.101.101, the remote username is netadmin1, and the remote password is ftppass.

```text
copy ftp://netadmin1:ftppass@172.16.101.101/host2-confg nvram:startup-config
Configure using rtr2-confg from 172.16.101.101?[confirm]
Connected to 172.16.101.101
Loading 1112 byte file rtr2-confg:![OK]
[OK]
%SYS-5-CONFIG_NV:Non-volatile store configured from rtr2-config by
FTP from 172.16.101.101
```

Copying the Running Configuration to a Server Example The following example specifies a remote username of netadmin1. Then it copies the running configuration file named rtr2-confg to the netadmin1 directory on the remote host with an IP address of 172.16.101.101.

```text
configure terminal
Router(config)# ip rcmd remote-username netadmin1
Router(config)#
end
copy system:running-config rcp:
Remote host[]?
172.16.101.101
Name of configuration file to write [Rtr2-confg]?
Write file rtr2-confg on host 172.16.101.101?[confirm]
Building configuration...[OK]
Connected to 172.16.101.101
```

Copying the Startup Configuration to a Server Example The following example copies the startup configuration to a TFTP server:

```text
copy nvram:startup-config tftp:
Remote host[]? 172.16.101.101
Name of configuration file to write [rtr2-confg]? <cr>
Write file rtr2-confg on host 172.16.101.101?[confirm] <cr>
![OK]
```

Saving the Current Running Configuration Example The following example copies the running configuration to the startup configuration. On a Class A flash file system platform, this command copies the running configuration to the startup configuration specified by the CONFIG_FILE variable.

```text
copy system:running-config nvram:startup-config
```

The following example shows the warning that the system provides if you try to save configuration information from bootstrap into the system:

```text
Router(boot)# copy system:running-config nvram:startup-config
Warning: Attempting to overwrite an NVRAM configuration written
by a full system image. This bootstrap software does not support
the full configuration command set. If you perform this command now,
some configuration commands may be lost.
Overwrite the previous NVRAM configuration?[confirm]
```

Enter no to escape writing the configuration information to memory. Moving Configuration Files to Other Locations Examples On some routers, you can store copies of configuration files on a flash memory device. Five examples follow: Copying the Startup Configuration to a Flash Memory Device Example The following example copies the startup configuration file (specified by the CONFIG_FILE environment variable) to a flash memory card inserted in slot 0:

```text
Router# copy nvram:startup-config slot0:router-confg
```

Copying the Running Configuration to a Flash Memory Device Example The following example copies the running configuration from the router to the flash memory PC card in slot 0:

```text
copy system:running-config slot0:berlin-cfg
Building configuration...
5267 bytes copied in 0.720 secs
```

Copying to the Running Configuration from a Flash Memory Device Example The following example copies the file named ios-upgrade-1 from the flash memory card in slot 0 to the running configuration:

```text
Router# copy slot0:4:ios-upgrade-1 system:running-config
Copy
'ios-upgrade-1
' from flash device
as 'running-config' ? [yes/no] yes
```

Copying to the Startup Configuration from a Flash Memory Device Example The following example copies the router-image file from the flash memory to the startup configuration:

```text
Router# copy flash:router-image nvram:startup-config
```

Copying a Configuration File from one Flash Device to Another Example The following example copies the file running-config from the first partition in internal flash memory to the flash memory PC card in slot 1. The checksum of the file is verified, and its copying time of 30 seconds is displayed.

```text
Router# copy flash: slot1:
System flash
Partition Size Used Free Bank-Size State Copy Mode
1 4096K 3070K 1025K 4096K Read/Write Direct
2 16384K 1671K 14712K 8192K Read/Write Direct
[Type ?<no> for partition directory; ? for full directory; q to abort]
Which partition? [default = 1]
System flash directory, partition 1:
File Length Name/status
1 3142748 dirt/images/mars-test/c3600-j-mz.latest
2 850 running-config
[3143728 bytes used, 1050576 available, 4194304 total]
PCMCIA Slot1 flash directory:
File Length Name/status
1 1711088 dirt/images/c3600-i-mz
2 850 running-config
[1712068 bytes used, 2482236 available, 4194304 total]
Source file name? running-config
Destination file name [running-config]?
Verifying checksum for 'running-config' (file # 2)... OK
Erase flash device before writing? [confirm]
Flash contains files. Are you sure you want to erase? [confirm]
Copy 'running-config' from flash: device
as 'running-config' into slot1: device WITH erase? [yes/no] yes
Erasing device... eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee ...erased
!
[OK - 850/4194304 bytes]
Flash device copy took 00:00:30 [hh:mm:ss]
Verifying checksum... OK (0x16)
```

Copying a File from a Remote Web Server Examples In the following example, the file config1 is copied from a remote server to flash memory using HTTP:

```text
Router# copy
http://
www.example.com:8080/configs/config1 flash:config1
```

In the following example, a default username and password for HTTP Client communications is configured, and then the file sample.scr is copied from a secure HTTP server using HTTPS:

```text
Router# configure terminal
Router(config)#
ip http client username joeuser
Router(config)#
ip http client password letmein
Router(config)# end
copy https://www.example_secure.com/scripts/sample.scr flash:
```

In the following example, an HTTP proxy server is specified before using the copy http:// command:

```text
Router# configure terminal
Router(config)# ip http client proxy-server edge2 proxy-port 29
Router(config)#
end
Router# copy
http://
www.example.com/configs/config3 flash:/configs/config3
```

Copying an Image from the Primary RSP Card to the Secondary RSP Card Example The following example copies the router-image file from the flash memory card inserted in slot 1 of the primary RSP card to slot 0 of the secondary RSP card in the same router:

```text
Router# copy slot1:router-image slaveslot0:
```


The copy erase flash command has been replaced by the erase flash:command. See the description of the erase command for more information. On some platforms, use can use the copy /erase source-url flash: syntax to erase the local Flash file system before copying a new file into Flash. See the desciption of the copy command for details on this option. The copy http:// command is documented as part of the copy command. The copy https:// command is documented as part of the copy command.

### `copy logging system`

> **Página:** 144 · **Modo:** Privileged EXEC (#) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** não

**Description:** To copy archived system events to a destination file system, use the copy logging systemcommand in privileged EXEC mode. To stop copying the archived system events, use the no form of the command.

**Syntax:**

```text
copy logging system target: filename
no copy logging system
```

**Parameters (Syntax Description):**

- `target :` — Specifies the destination filesystem; V a l id values are as f o l low s: • bootflash: •disk0: •disk1: •ftp: •http: •https: •rcp: • slave bootflash: • slave disk0: • slave disk1: • slave sup-boot disk: • slave sup-bootflash: • sup-boot disk: • sup-bootflash: •tftp:
- `file name` — Name of the file.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SXH | This command was introduced. |
| 12.2(33)SCC | The command was introduced for the Ciscou B R10012 router in the Cisco IOS Software Release12.2(33) S C C. |

**Usage Guidelines:**

System Event Archive (SEA) is supported on switches that have a Supervisor Engine 32 or Supervisor Engine 720 with a compact flash adapter and a Compact Flash card (WS-CF-UPG= for Supervisor Engine 720). Cisco Universal Broadband Router 10012 The System Event Archive (SEA) feature is used to address the debug trace and system console constraints. Use the copy logging systemcommand to copy the major and critical events stored in the sea_log.dat file, to the destination file system. Note To store the system event logs, the SEA requires either the PCMCIA ATA disk or Compact Flash Disk in compact flash adapter for PRE2. The following example shows how to copy the SEA to the file system of disk0:

```text
Router# copy logging system disk0:
Destination filename [sea_log.dat]?
```

The following example shows how to copy the SEA using the remote file copy function (rcp):

```text
Router# copy logging system rcp:
Address or name of remote host []? 192.0.2.1
Destination username [Router]? username1
Destination filename [sea_log.dat]? /auto/tftpboot-users/username1/sea_log.dat
```


### `copy xmodem`

> **Página:** 146 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To copy a Cisco IOS image from a local or remote computer (such as a PC, Macintosh, or UNIX workstation) to Flash memory on a Cisco 3600 series router using the Xmodem protocol, use the copy xmodem: command in EXEC mode.

**Syntax:**

```text
copy xmodem: flashfilesystem:
```

**Parameters (Syntax Description):**

- `flash-filesystem :` — Destination of the c o p i e d file, f o l low e d by a c o l on.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2P | This command was introduced. |
| 12.2(15)T | This command is no l on g e r supported in Cisco IOS M a in line or Tech no log y-b as e d( T) releases. It may continue to ap p e a r in Cisco IOS12.2 S-f a m i l y releases. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is a form of the copy command. The copy xmodem: and copy xmodem commands are identical. See the description of the copy command for more information. Copying a file using FTP, rcp, or TFTP is much faster than copying a file using Xmodem. Use the copy xmodem: command only if you do not have access to an FTP, TFTP, or rcp server. This copy operation is performed through the console or AUX port. The AUX port, which supports hardware flow control, is recommended. No output is displayed on the port over which the transfer is occurring. You can use the logging buffered command to log all router messages sent to the console port during the file transfer.

**Example:**

The following example initiates a file transfer from a local or remote computer to the router’s internal Flash memory using the Xmodem protocol:

```text
copy xmodem: flash:
```


### `copy ymodem`

> **Página:** 147 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To copy a Cisco IOS image from a local or remote computer (such as a PC, Macintosh, or UNIX workstation) to Flash memory on a Cisco 3600 series router using the Ymodem protocol, use the copy ymodem: command in EXEC mode.

**Syntax:**

```text
copy ymodem: flashfilesystem:
```

**Parameters (Syntax Description):**

- `flash-filesystem :` — Destination of the c o p i e d file, f o l low e d by a c o l on.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2P | This command was introduced. |
| 12.2(15)T | This command is no l on g e r supported in Cisco IOS M a in line or Tech no log y-b as e d( T) releases. It may continue to ap p e a r in Cisco IOS12.2 S-f a m i l y releases. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The copy ymodem: and copy ymodem commands are identical. See the description of the copycommand for more information. Copying a file using FTP, rcp, or TFTP is much faster than copying a file using Ymodem. Use the copy ymodem: command only if you do not have access to an FTP, rcp, or TFTP server. This copy operation is performed through the console or AUX port. The AUX port, which supports hardware flow control, is recommended. No output is displayed on the port over which the transfer is occurring. You can use the logging buffered command to log all router messages sent to the console port during the file transfer.

**Example:**

The following example initiates a file transfer from a local or remote computer to the router’s internal Flash memory using the Ymodem protocol:

```text
copy ymodem: flash:
```


### `copy noverify`

> **Página:** 148 · **Modo:** Privileged EXEC · **Default:** Verification is done automatically after completion of a copy operation. · **Leitura (show/clear/…):** não

**Description:** To disable the automatic image verification for the current copy operation, use the command. copy /noverify

**Syntax:**

```text
copy /noverify source-url destination-url
```

**Parameters (Syntax Description):**

- `source-url` — Location URL or alias of the source file or directory to be c o p i e d; see the“ Usage Guidelines” section for a d d it i on a l information.
- `destination-url` — Destination URL or alias of the c o p i e d file or directory; see the“ Usage Guidelines” section for a d d it i on a l information.

**Command Default:** Verification is done automatically after completion of a copy operation.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The exact format of the source and destination URLs varies according to the file or directory location. You may enter either an alias keyword for a particular file or an alias keyword for a file system type (not a file within a type). Timesaver Aliases are used to cut down on the amount of typing that you need to perform. For example, it is easier to type copy run start (the abbreviated form of the copy running-config startup-config command) than it is to type copy system:r nvram:s (the abbreviated form of the copy system:running-config nvram:startup-configcommand). These aliases allow you to continue using some of the common commands that are used in previous versions of Cisco IOS software. The table below shows two keyword shortcuts to URLs.

| Keyword | SourceorDestination |
| --- | --- |
| running-config | (Optional)Specifiesthealiasforthesystem:running-configURL.Thiskeyworddoes notworkinthemoreandshowfilecommandsyntaxes. |
| startup-config | (Optional)Specifiesthealiasforthenvram:startup-configURL.The nvram:startup-configkeywordrepresentstheconfigurationfilethatisusedduring initialization(startup).ThisfileiscontainedinNVRAM.Thiskeyworddoesnotworkin moreandshowfileEXECcommandsyntaxes. |

The following tables list aliases by file system type. If you do not specify an alias, the system looks for a file in the current directory. The table below lists the URL prefix aliases for special (opaque) file systems.

| Alias | SourceorDestination |
| --- | --- |
| flh: | SourceURLforFlashloadhelperlogfiles. |
| nvram: | RouterNVRAM.YoucancopythestartupconfigurationintoorfromNVRAM.Youcanalso displaythesizeofaprivateconfigurationfile. |
| null: | Nulldestinationforcopiesorfiles.Youcancopyaremotefiletonulltodetermineitssize. |
| system: | SourceordestinationURLforsystemmemory,whichincludestherunningconfiguration. |
| xmodem: | SourcedestinationforthefilefromanetworkdevicethatusestheXmodemprotocol. |
| ymodem: | SourcedestinationforthefilefromanetworkdevicethatusestheYmodemprotocol. |

The table below lists the URL prefix aliases for network file systems.

| Alias | SourceorDestination |
| --- | --- |
| ftp: | SourceordestinationURLforanFTPnetworkserver.Thesyntaxforthisaliasisas follows:ftp:[[[//username[:password]@]location]/directory]/filename. |

| Alias | SourceorDestination |
| --- | --- |
| rcp: | SourceordestinationURLforanrcpnetworkserver.Thesyntaxforthisaliasisasfollows: rcp:[[[//username@]location]/directory]/filename. |
| tftp: | SourceordestinationURLforaTFTPnetworkserver.Thesyntaxforthisaliasis tftp:[[//location]/directory]/filename. |

The table below lists the URL prefix aliases for local writable storage file systems.

| Alias | SourceorDestination |
| --- | --- |
| bootflash: | SourceordestinationURLforbootflashmemory. |
| disk0:anddisk1: | SourceordestinationURLofrotatingmedia. |
| flash: | SourceordestinationURLforFlashmemory.Thisaliasisavailableonallplatforms. ForplatformsthatlackaFlash:device,notethatflash:isaliasedtoslot0:,allowingyou torefertothemainFlashmemorystorageareaonallplatforms. |
| slavebootflash: | SourceordestinationURLforinternalFlashmemoryonthesecondaryRSPcardofa devicethatisconfiguredforHSA. |
| slaveram: | NVRAMonasecondaryRSPcardofadevicethatisconfiguredforHSA. |
| slavedisk0: | SourceordestinationURLofthefirstPCMCIAcardonasecondaryRSPcardofa devicethatisconfiguredforHSA. |
| slavedisk1: | SourceordestinationURLofthesecondPCMCIAslotonasecondaryRSPcardofa devicethatisconfiguredforHSA. |
| slaveslot0: | SourceordestinationURLofthefirstPCMCIAcardonasecondaryRSPcardofa routerconfiguredforHSA--AvailableonsystemsthatareconfiguredwithaSupervisor Engine2. |
| slaveslot1: | SourceordestinationURLofthesecondPCMCIAslotonasecondaryRSPcardofa routerconfiguredforHSA--AvailableonsystemsthatareconfiguredwithaSupervisor Engine2. |
| slot0: | SourceordestinationURLofthefirstPCMCIAFlashmemorycard--Availableon systemsthatareconfiguredwithaSupervisorEngine2. |
| slot1: | SourceordestinationURLofthesecondPCMCIAFlashmemorycard--Availableon systemsthatareconfiguredwithaSupervisorEngine2. |

You can enter on the command line all necessary source- and destination-URL information and the username and password to use, or you can enter the copy command and have the switch prompt you for any missing information. If you enter information, choose one of the following three options: running-config, startup-config, or a file system alias (see the tables above). The location of a file system dictates the format of the source or destination URL. The colon is required after the alias. However, earlier commands that do not require a colon remain supported but are unavailable in context-sensitive help. The entire copying process may take several minutes and differs from protocol to protocol and from network to network. In the alias syntax for ftp:, rcp:, and tftp:, the location is either an IP address or a hostname. The filename is specified for the directory that is used for file transfers. Enter the file verify autocommand to set up verification globally.

**Example:**

This example shows how to disable the automatic image verification for the current copy operation:

```text
copy /noverify tftp: sup-bootflash:
.................................................
[OK - 24301348 bytes]
24301348 bytes copied in 157.328 secs (154463 bytes/sec)
```
