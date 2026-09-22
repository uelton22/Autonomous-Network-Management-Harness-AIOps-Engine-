# Capítulo 6: L through mode

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## F through K

### L through mode

• L through mode, on page 250

### L through mode

### `length`

> **Página:** 274 · **Modo:** Line configuration · **Default:** Screen length of 24 lines · **Leitura (show/clear/…):** não

**Description:** To set the terminal screen length, use the length command in line configuration mode. To restore the default value, use the no form of this command.

**Syntax:**

```text
length screen-length
no length
```

**Parameters (Syntax Description):**

- `screen-length` — Then u m be r of lines on the screen. A value of z e r o disable s p a using be t we e n screen s of output.

**Command Default:** Screen length of 24 lines

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The Cisco IOS software uses the value of this command to determine when to pause during multiple-screen output. Not all commands recognize the configured screen length. For example, the show terminal command assumes a screen length of 24 lines or more.

**Example:**

In the following example, the terminal type is specified and the screen pause function is disabled for the terminal connection on line 6:

```text
Router(config)# line 6
Router(config-line)# terminal-type VT220
Router(config-line)#
length 0
```


### `load-interval`

> **Página:** 274 · **Modo:** Interface configuration Frame Relay DLCI configuration Template configuration (config-template) · **Default:** Enabled · **Leitura (show/clear/…):** não

**Description:** To change the length of time for which data is used to compute load statistics, use the load-interval command in interface configuration, Frame Relay DLCI configuration, or template configuration modes. To revert to the default setting, use the noform of this command.

**Syntax:**

```text
load-interval seconds
no load-interval seconds
```

**Parameters (Syntax Description):**

- `seconds` — Length of time for which data is used to c o m p u t e load statistics. Value is a m u l t ip l e of30, from 30 to600(30,60,90,120, and s o on). The default is300 s e c on d s.

**Command Default:** Enabled

**Command Modes:** Interface configuration Frame Relay DLCI configuration Template configuration (config-template)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(4)T | This command was m a d e a v a i l a b l e in Frame Relay D L C I configuration mode. |
| 12.2(18)SXF | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 15.1(2)SNG | This command was i m p l e m e n t e do n the Cisco AS R901 S e r i e s A g g r e g at i on Service s Routers. |
| 15.2(2)E | This command was integrated into Cisco IOS Release15.2(2) E. This command is supported in template configuration mode. |
| CiscoIOSXERelease3.6E | This command was integrated into Cisco IOS X E Release3.6 E. This command is supported in template configuration mode. |

**Usage Guidelines:**

To make computations more reactive to short bursts of traffic, you can shorten the length of time over which load averages are computed. If the load interval is set to 30 seconds, new data is used for load calculations over a 30-second period. This data is used to compute load statistics, including the input rate in bits and packets per second, the output rate in bits and packets per second, the load, and reliability. Load data is gathered every five seconds. This data is used for a weighted-average calculation in which recent load data has more weight in the computation than older load data. If the load interval is set to 30 seconds, the average is computed for the last 30 seconds of load data. If you change the calculation interval from the default of five minutes to a shorter period of time, the input and output statistics that are displayed by the show interface command or the show frame-relay pvc command will be more current and will be based on more nearly instantaneous data, rather than reflecting the average load over a longer period of time. This command is often used for dial backup purposes to increase or decrease the likelihood of implementation of a backup interface, but it can be used on any interface.

**Example:**

Interface Example In the following example, the default average of five minutes is changed to a 30-second average. A burst in traffic that would not trigger a dial backup for an interface configured with the default five-minute interval might trigger a dial backup for this interface, which is set for the shorter 30-second interval.

```text
Router(config)# interface serial 0
Router(config-if)# load-interval 30
```

Frame Relay PVC Example In the following example, the load interval is set to 60 seconds for a Frame Relay PVC with the DLCI 100:

```text
Router(config)# interface serial 1/1
Router(config-if)# frame-relay interface-dlci 100
Router(config-fr-dlci)# load-interval 60
```

Interface Template Example In the following example, the load interval is set to 60 seconds in an interface template:

```text
Device# configure terminal
Device(config)# template user-template1
Device(config-template)# load-interval 60
Device(config-template)# end
```


### `location`

> **Página:** 276 · **Modo:** Line configuration (config-line) · **Default:** A location description is not provided. · **Leitura (show/clear/…):** não

**Description:** To provide a description of the location of a serial device, use the location command in line configuration mode. To remove the description, use the no form of this command.

**Syntax:**

```text
location text
no location
```

**Parameters (Syntax Description):**

- `text` — Location description.

**Command Default:** A location description is not provided.

**Command Modes:** Line configuration (config-line)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The location command enters information about the device location and status. Use the show users all EXEC command to display the location information.

**Example:**

In the following example, the location description for the console line is given as “Building 3, Basement”:

```text
Router(config)# line console
Router(config-line)# location Building 3, Basement
```


### `lock`

> **Página:** 277 · **Modo:** EXEC · **Default:** Not locked · **Leitura (show/clear/…):** não

**Description:** To configure a temporary password on a line, use the lockcommand in EXEC mode.

**Syntax:**

```text
lock
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Not locked

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced in are l e as e p r i or to Cisco IOS Release10.0. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You can prevent access to your session while keeping your connection open by setting up a temporary password. To lock access to the terminal, perform the following steps: 1. Enter the lock command. The system prompts you for a password. 2. Enter a password, which can be any arbitrary string. The system will prompt you to confirm the password. The screen then clears and displays the message “Locked.” 3. To regain access to your sessions, reenter the password. The Cisco IOS software honors session timeouts on a locked lines. You must clear the line to remove this feature. The system administrator must set the line up to allow use of the temporary locking feature by using the lockable line configuration command.

**Example:**

The following example shows configuring the router as lockable, saving the configuration, and then locking the current session for the user:

```text
Router(config-line)# lockable
Router(config-line)# ^Z
Router# copy system:running-config nvram:startup-config
Building configuration...
OK
Router# lock
Password: <password>
Again: <password>
Locked
Password: <password>
```


### `lockable`

> **Página:** 278 · **Modo:** Line configuration · **Default:** Sessions on the line are not lockable (the lock EXEC command has no effect). · **Leitura (show/clear/…):** não

**Description:** To enable use of the lock EXEC command, use the lockablecommand in line configuration mode. To reinstate the default (the terminal session cannot be locked), use the noform of this command.

**Syntax:**

```text
lockable
no lockable
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Sessions on the line are not lockable (the lock EXEC command has no effect).

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command enables use of temporary terminal locking, which is executed using the lock EXEC command. Terminal locking allows a user keep the current session open while preventing access by other users.

**Example:**

In the following example, the terminal connection is configured as lockable, then the current connection is locked:

```text
Router# configure terminal
Router(config)# line console 0
Router(config-line)# lockable
Router(config)# ^Z
Router# lock
Password:
<password>
Again:
<password>
Locked
Password: <password>
```


### `log config`

> **Página:** 279 · **Modo:** Archive configuration (config-archive) · **Default:** Configuration change logger configuration mode is not entered. · **Leitura (show/clear/…):** não

**Description:** To enter configuration change logger configuration mode, use the log configcommand in archive configuration mode.

**Syntax:**

```text
log config
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Configuration change logger configuration mode is not entered.

**Command Modes:** Archive configuration (config-archive)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(4)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(27)SBC | This command was integrated into Cisco IOS Release12.2(27) S B C. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Example:**

The following example shows how to place the device in configuration change logger configuration mode:

```text
Device#
configure terminal
!
Device(config)# archive
Device(config-archive)# log config
Device(config-archive-log-config)#
```


### `logging buffered`

> **Página:** 280 · **Modo:** Global configuration (config) · **Default:** Varies by platform. For most platforms, logging to the buffer is disabled by default. · **Leitura (show/clear/…):** não

**Description:** To enable system message logging to a local buffer, use the logging buffered command in global configuration mode. To cancel the use of the buffer, use the no form of this command. To return the buffer size to its default value, use the default form of this command.

**Syntax:**

```text
logging buffered [discriminator discriminator-name] [buffer-size] [severity-level]
no logging buffered
default logging buffered
```

**Parameters (Syntax Description):**

- `d is c r i min at or` — ( Optional) Specifies a user-define d f i l t e r, v i at h e logging d is c r i min at or, for syslog message s.
- `discriminator-name` — ( Optional) String of a maximum of e i g h t a l p h an u m e r i c, c as e-s e n s it i v e characters. Blank space s be t we e n characters are not all o we d.
- `buffer-size` — ( Optional) Size of the buffer, in by t e s. The range is4096 to2147483647. The default size v a r i e s by platform.
- `severity-level` — ( Optional) Then u m be r or name of the d e s i r e d s e v e r it y level at which message s should be log g e d. Message s at or n u m e r i c all y low e r than the specified level are log g e d. S e v e r it y levels are as f o l low s( enter then u m be r or the keyword): [0| e m e r g e n c i e s]— System is u n u s a b l e [1| a l e r t s]— I m m e d i at e a c t i on n e e d e d [2| critical]— Critical c on d it i on s [3| error s]— Error c on d it i on s [4| warning s— Warning c on d it i on s [[5| not if i c at i on s]— Nor m a l but s i g n if i can t c on d it i on s [[6| information a l]— Information a l message s [[7| debugging]— Debugging message s The default logging level v a r i e s by platform but isg e n e r all y7. Level7 m e an s that message s at all levels(0-7) are log g e d to the buffer. Note Every time you set the d e s i r e d buffers e v e r it y level, the buffers i z e is set to default. The r e for e, enter the value for the buffers i z e after set t in gt h e buffers e v e r it y level.

**Command Default:** Varies by platform. For most platforms, logging to the buffer is disabled by default.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 11.1(17)T | These v e r it y-level argument was added. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.4(11)T | The d is c r i min at or keyword and d is c r i min at or-name argument were added. |
| 12.2SX | This command is supported in the Cisco IOS Release12.2 S X t r a in. Support in as p e c if i c 12.2 S X release of this t r a in d e p end s on your f e at u reset, platform, and platform hardware. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B. |
| 12.2(50)SY | This command was integrated into Cisco IOS Release12.2(50 S Y. |

**Usage Guidelines:**

This command copies logging messages to an internal buffer. The buffer is circular in nature, so newer messages overwrite older messages after the buffer is filled. Specifying a severity-level causes messages at that level and numerically lower levels to be logged in an internal buffer. The optional discriminator keyword and discriminator-name argument provide another layer of filtering that you can use to control the type and number of syslog messages that you want to receive. When you resize the logging buffer, the existing buffer is freed and a new buffer is allocated. To prevent the router from running out of memory, do not make the buffer size too large. You can use the show memory EXEC command to view the free processor memory on the router; however, the memory value shown is the maximum available and should not be approached. The default logging buffered command resets the buffer size to the default for the platform. Note On Catalyst 6500 standalone switches and Catalyst 6500 virtual switches, the default logging buffered size is 8192. To display messages that are logged in the buffer, use the show logging command. The first message displayed is the oldest message in the buffer. The show logging command displays the addresses and levels associated with the current logging setup and other logging statistics. The table below shows a list of levels and corresponding syslog definitions.

| Level | LevelKeyword | SyslogDefinition |
| --- | --- | --- |
| 0 | emergencies | LOG_EMERG |
| 1 | alerts | LOG_ALERT |
| 2 | critical | LOG_CRIT |
| 3 | errors | LOG_ERR |
| 4 | warnings | LOG_WARNING |
| 5 | notifications | LOG_NOTICE |
| 6 | informational | LOG_INFO |
| 7 | debugging | LOG_DEBUG |

**Example:**

The following example shows how to enable standard system logging to the local syslog buffer:

```text
Router(config)# logging buffered
```

The following example shows how to use a message discriminator named buffer1 to filter critical messages, meaning that messages at levels 0, 1, and 2 are filtered:

```text
Router(config)# logging buffered discriminator buffer1 critical
```


### `logging buginf`

> **Página:** 283 · **Modo:** Global configuration (config) · **Default:** Debug messages are not suppressed. · **Leitura (show/clear/…):** não

**Description:** To allow debug messages to be generated for the standard system logging buffer, use the logging buginfcommand in global configuration mode. To disable the logging for debugging functionality, use the

**Syntax:**

```text
no form of this command.
logging buginf
no logging buginf
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Debug messages are not suppressed.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release 15.0(1)M. |
| 12.2(33)SRC | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRC. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1. |

**Usage Guidelines:**

The no logging buginfcommand is used to avoid a situation where a large amount of debug messages might overload the processor (CPU hog condition). This condition differs from the use of the undebug allcommand wherein all debugging calls are disabled in the Cisco IOS software. No debug reporting is available, even if debugging is enabled. Note that even though debugging has been completely disabled in the system, other message reporting, including error reporting, is still available.

**Example:**

The following example shows how to enable buginf logging for debugging:

```text
Router# configure terminal
Router(config)# logging buginf
```


### `logging enable`

> **Página:** 284 · **Modo:** Configuration change logger configuration (config-archive-log-config) · **Default:** Configuration change logging is disabled. · **Leitura (show/clear/…):** não

**Description:** To enable the logging of configuration changes, use the logging enable command in configuration change logger configuration mode. To disable the logging of configuration changes, use the no form of this command.

**Syntax:**

```text
logging enable
no logging enable
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Configuration change logging is disabled.

**Command Modes:** Configuration change logger configuration (config-archive-log-config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(4)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(27)SBC | This command was integrated into Cisco IOS Release12.2(27) S B C. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Use this command if you want to log configuration changes. If you disable configuration logging, all configuration log records that were collected are purged.

**Example:**

The following example shows how to enable configuration logging:

```text
Device#
configure terminal
!
Device(config)# archive
Device(config-archive)# log config
Device(config-archive-log-config)# logging enable
Device(config-archive-log-config)# end
```

The following example shows how to clear the configuration log by disabling and then reenabling the configuration log:

```text
Device# configure terminal
!
Device(config)# archive
Device(config-archive)# log config
Device(config-archive-log-config)# no logging enable
Device(config-archive-log-config)# logging enable
Device(config-archive-log-config)# end
```


### `logging esm config`

> **Página:** 285 · **Modo:** Global configuration (config) · **Default:** ESM filters are enabled. · **Leitura (show/clear/…):** não

**Description:** To permit configuration changes from Embedded Syslog Manager (ESM) filters, use the logging esm config command in global configuration mode. To disable the configuration, use the no form of this command.

**Syntax:**

```text
logging esm config
no logging esm config
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** ESM filters are enabled.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release 15.0(1)M. |
| 12.2(33)SRC | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRC. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1. |

**Usage Guidelines:**

You can use the no logging esm config command to disallow configuration changes from ESM filters.

**Example:**

The following example shows how to configure the ESM filters:

```text
Router# configure terminal
Router(config)# logging esm config
```


### `logging event bundle-status`

> **Página:** 286 · **Modo:** Global configuration · **Default:** Message bundling does not occur. · **Leitura (show/clear/…):** não

**Description:** To enable message bundling, use the logging event bundle-status command in interface configuration mode. To disable message bundling, use the no form of this command.

**Syntax:**

```text
logging event bundle-status
no logging event bundle-status
```

**Parameters (Syntax Description):**

- `default` — Enable s system logging of interfaces t at e-c h an g e events on all interfaces in the system.
- `boot` — Enable s system logging of interfaces t at e-c h an g e events on all interfaces in the system d u r in g system in it i a l i z at i on.

**Command Default:** Message bundling does not occur.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The logging event bundle-status command is not applicable on Port Channel or Ether-Channel interfaces.

**Example:**

This example shows how to enable the system logging of the interface state-change events on all interfaces in the system:

```text
Router(config)# logging event bundle-status
Router(config)# end
Router #
show logging event bundle-status
*Aug 4 17:36:48.240 UTC: %EC-SP-5-UNBUNDLE: Interface FastEthernet9/23 left the port-channel
Port-channel2
*Aug 4 17:36:48.256 UTC: %LINK-SP-5-CHANGED: Interface FastEthernet9/23, changed state to
administratively down
*Aug 4 17:36:47.865 UTC: %EC-SPSTBY-5-UNBUNDLE: Interface FastEthernet9/23 left the
port-channel Port-channel2
Router # show logging event bundle-status
*Aug 4 17:37:35.845 UTC: %EC-SP-5-BUNDLE: Interface FastEthernet9/23 joined port-channel
Port-channel2
*Aug 4 17:37:35.533 UTC: %EC-SPSTBY-5-BUNDLE: Interface FastEthernet9/23 joined port-channel
Port-channel2
```


### `logging event link-status (global configuration)`

> **Página:** 287 · **Modo:** Global configuration · **Default:** Interface state-change messages are not sent. · **Leitura (show/clear/…):** não

**Description:** To change the default or set the link-status event messaging during system initialization, use the logging event link-status command in global configuration mode. To disable the link-status event messaging, use the no form of this command. logging event link-status {default | boot}

**Syntax:**

```text
no logging event link-status {default | boot}
```

**Parameters (Syntax Description):**

- `default` — Enable s system logging of interfaces t at e-c h an g e events on all interfaces in the system.
- `boot` — Enable s system logging of interfaces t at e-c h an g e events on all interfaces in the system d u r in g system in it i a l i z at i on.

**Command Default:** Interface state-change messages are not sent.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You do not have to enter the logging event link-status boot command to enable link-status messaging during system initialization. The logging event link-status default command logs system messages even during system initialization. If you enter both the logging event link-status default and the no logging event link-status bootcommands, the interface state-change events are logged after all modules in the Cisco 7600 series router come online after system initialization. The logging event link-status default and the no logging event link-status boot commands are saved and retained in the running configuration of the system. When both the logging event link-status default and the no logging event link-status bootcommands are present in the running configuration and you want to display the interface state-change messages during system initialization, enter the logging event link-status boot command.

**Example:**

This example shows how to enable the system logging of the interface state-change events on all interfaces in the system:

```text
Router(config)# logging event link-status default
Router(config)#
```

This example shows how to enable the system logging of interface state-change events on all interfaces during system initialization:

```text
Router(config)#
logging event link-status boot
Router(config)#
```

This example shows how to disable the system logging of interface state-change events on all interfaces:

```text
Router(config)# no logging event link-status default
Router(config)#
```

This example shows how to disable the system logging of interface state-change events during system initialization:

```text
Router(config)# no logging event link-status boot
Router(config)#
```


### `logging event link-status (interface configuration)`

> **Página:** 288 · **Modo:** Interface configuration (config-if) · **Default:** Interface state-change messages are not sent. · **Leitura (show/clear/…):** não

**Description:** To enable link-status event messaging on an interface, use the logging event link-status command in interface configuration mode. To disable link-status event messaging, use the no form of this command. logging event link-status [bchan | dchan | nfas]

**Syntax:**

```text
no logging event link-status [bchan | dchan | nfas]
```

**Parameters (Syntax Description):**

- `bchan` — ( Optional) Log s B-c h an n e l status message s. This keyword is a v a i l a b l e only for integrated service s d i g it a l network( IS D N) s e r i a l interfaces.
- `dchan` — ( Optional) Log s D-c h an n e l status message s. This keyword is a v a i l a b l e only for IS D N s e r i a l interfaces.
- `nfas` — ( Optional) Log s no n-f a c i l it y as s o c i at e d s i g n a l in g( N F AS) D-c h an n e l status message s. This keyword is a v a i l a b l e only for IS D N s e r i a l interfaces.

**Command Default:** Interface state-change messages are not sent.

**Command Modes:** Interface configuration (config-if)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | This command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | This command was modified to support the Supervisor Engine2. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

To enable system logging of interface state-change events on a specific interface, enter the logging event link-status command.

**Example:**

The following example shows how to enable link-status event messaging on an interface:

```text
Router(config-if)# logging event link-status
```

This example shows how to disable link-status event messaging on an interface:

```text
Router(config-if)# no logging event link-status
```


### `logging event subif-link-status`

> **Página:** 289 · **Modo:** Interface configuration · **Default:** Subinterface state-change messages are not sent. · **Leitura (show/clear/…):** não

**Description:** To enable the link-status event messaging on a subinterface, use the logging event subif-link-status command in interface configuration mode. To disable the link-status event messaging on a subinterface, use the no form of this command.

**Syntax:**

```text
logging event subif-link-status
no logging event subif-link-status
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Subinterface state-change messages are not sent.

**Command Modes:** Interface configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is not supported on Cisco 7600 series routers that are configured with a Supervisor Engine 720. To enable system logging of interface state-change events on a specific subinterface, enter the logging event subif-link-status command. To enable system logging of interface state-change events on a specific interface, enter the logging event link-status command. To enable system logging of interface state-change events on all interfaces in the system, enter the logging event link-status command.

**Example:**

This example shows how to enable the system logging of the interface state-change events on a subinterface:

```text
Router(config-if)# logging event subif-link-status
Router(config-if)#
```

This example shows how to disable the system logging of the interface state-change events on a subinterface:

```text
Router(config-if)#
no logging event subif-link-status
Router(config-if)#
```


### `logging event trunk-status`

> **Página:** 290 · **Modo:** Interface configuration mode · **Default:** This command has no default settings. · **Leitura (show/clear/…):** não

**Description:** To enable trunk status messaging, use the logging event trunk-status command in interface configuration mode. To disable trunk status messaging, use the no form of this command.

**Syntax:**

```text
logging event trunk-status
no logging event trunk-status
```

**Parameters (Syntax Description):**

- `—` — This command has no keywords or variables.

**Command Default:** This command has no default settings.

**Command Modes:** Interface configuration mode

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced. |

**Usage Guidelines:**

The logging event bundle-status command is not applicable on Port Channel or Ether-Channel interfaces.

**Example:**

This example shows how to enable the trunk status messaging on physical ports:

```text
Router(config)# logging event trunk-status
Router(config)# end
Router# show logging event trunk-status
*Aug 4 17:27:01.404 UTC: %DTP-SPSTBY-5-NONTRUNKPORTON: Port Gi3/3 has become non-trunk
*Aug 4 17:27:00.773 UTC: %DTP-SP-5-NONTRUNKPORTON: Port Gi3/3 has become non-trunk
```


### `logging reload`

> **Página:** 291 · **Modo:** Global configuration (config) · **Default:** The logging reload message limit is 1000 notifications. · **Leitura (show/clear/…):** não

**Description:** To set the reload logging level, use the logging reloadcommand in global configuration mode. To disable the reload logging, use the no form of this command.

**Syntax:**

```text
logging reload [message-limit number] [severity-level | alerts | critical | debugging | emergencies |
errors | informational | notifications | warnings]
no logging reload
```

**Parameters (Syntax Description):**

- `message-limit` — ( Optional) Set s the limit on then u m be r of message s that can be log g e d d u r in g reload.
- `number` — Number of message s. The range is from1 to4294967295.
- `severity-level` — ( Optional) Logging s e v e r it y level. The range is from0 to7.
- `alerts` — ( Optional) Specifies that an i m m e d i at e a c t i on is n e e d e d.
- `critical` — ( Optional) Specifies the critical c on d it i on s.
- `debugging` — ( Optional) D is p l a y s the debugging message s
- `e m e r g e n c i e s` — ( Optional) Specifies that the system is u n u s a b l e.
- `errors` — ( Optional) Specifies error c on d it i on s
- `information a l` — ( Optional) Specifies error information a l message s
- `not if i c at i on s` — ( Optional) Specifies nor m a l but s i g n if i can t c on d it i on s.
- `warning s` — ( Optional) Specifies warning c on d it i on s.

**Command Default:** The logging reload message limit is 1000 notifications.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release 15.0(1)M. |
| 12.2(33)SRC | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRC. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1. |

**Usage Guidelines:**

The default setting is recommended. Setting the message-limit too low may result in losing important messages during reload. If the logging reload command is not enabled, logging is turned off during reload.

**Example:**

The following example shows how to set the limit on number of messages that can be logged during reload to 100:

```text
Router# configure terminal
Router(config)# logging reload message-limit 100
```


### `logging ip access-list cache (global configuration)`

> **Página:** 292 · **Modo:** Global configuration · **Default:** The defaults are as follows: • entries --8000 entries. • seconds --300 seconds (5 minutes). • rate-limit pps --0 (rate limiting is off) and all packets are logged. • threshold packets --0 (rate limiting is off) and the system log is not triggered by the number of packet matches. · **Leitura (show/clear/…):** não

**Description:** To configure the Optimized ACL Logging (OAL) parameters, use the logging ip access-list cache command in global configuration mode. To return to the default settings, use the no form of this command.

**Syntax:**

```text
logging ip access-list cache {entries entries | interval seconds | rate-limit pps | threshold packets}
no logging ip access-list cache [entries | interval | rate-limit | threshold]
```

**Parameters (Syntax Description):**

- `entries entries` — Specifies the maximum number of log e n t r i e s that are cache d in the software; v a l id values are from0 to1048576 e n t r i e s.
- `interval seconds` — Specifies the maximum time interval before an entry is s e n t to syslog; v a l id values are from5 to86400 s e c on d s.
- `rate-limit pps` — Specifies then u m be r of p a c k e t s that are log g e d p e r s e c on d in the software; v a l id values are from10 to1000000 p p s.
- `threshold packets` — Specifies then u m be r of p a c k e t m at c h e s before an entry is s e n t to syslog; v a l id values are from1 to1000000 p a c k e t s.

**Command Default:** The defaults are as follows: • entries --8000 entries. • seconds --300 seconds (5 minutes). • rate-limit pps --0 (rate limiting is off) and all packets are logged. • threshold packets --0 (rate limiting is off) and the system log is not triggered by the number of packet matches.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(17d)SXB | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is supported on Cisco 7600 series routers that are configured with a Supervisor Engine 720 only. OAL is supported on IPv4 unicast traffic only. You cannot configure OAL and VACL capture on the same chassis. OAL and VACL capture are incompatible. With OAL configured, use SPAN to capture traffic. If the entry is inactive for the duration that is specified in the update-interval seconds command, the entry is removed from the cache. If you enter the no logging ip access-list cache command without keywords, all the parameters are returned to the default values. You must set ICMP unreachable rate limiting to 0 if the OAL is configured to log denied packets. When enabling the IP "too short" check using the mls verify ip length minimum command, valid IP packets with with an IP protocol field of ICMP(1), IGMP(2), IP(4), TCP(6), UDP(17), IPv6(41), GRE(47), or SIPP-ESP(50) will be hardware switched. All other IP protocol fields are software switched. Caution Using optimized access-list logging (OAL) and the mls verify ip length minimum command together can cause routing protocol neighbor flapping as they are incompatible

**Example:**

This example shows how to specify the maximum number of log entries that are cached in the software:

```text
Router(config)#
logging ip access-list cache entries 200
```

This example shows how to specify the maximum time interval before an entry is sent to the system log:

```text
Router(config)#
logging ip access-list cache interval 350
```

This example shows how to specify the number of packets that are logged per second in the software:

```text
Router(config)#
logging ip access-list cache rate-limit 100
```

This example shows how to specify the number of packet matches before an entry is sent to the system log:

```text
Router(config)#
logging ip access-list cache threshold 125
```


### `logging ip access-list cache (interface configuration)`

> **Página:** 294 · **Modo:** Interface configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To enable an Optimized ACL Logging (OAL)-logging cache on an interface that is based on direction, use the logging ip access-list cache command in interface configuration mode. To disable OAL, use the no form of this command. logging ip access-list cache [in | out]

**Syntax:**

```text
no logging ip access-list cache
```

**Parameters (Syntax Description):**

- `in` — ( Optional) Enable s O A L on in g r e s s p a c k e t s.
- `out` — ( Optional) Enable s O A L one g r e s s p a c k e t s.

**Command Default:** Disabled

**Command Modes:** Interface configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(17d)SXB | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is supported on Cisco 7600 series routers that are configured with a Supervisor Engine 720 only. This command is supported on traffic that matches the keyword in the applied ACL. You must set ICMP log unreachable rate limiting to 0 if the OAL is configured to log denied packets. On systems that are configured with a PFC3A, support for the egress direction on tunnel interfaces is not supported. OAL is supported on IPv4 unicast traffic only. You cannot configure OAL and VACL capture on the same chassis. OAL and VACL capture are incompatible. With OAL configured, use SPAN to capture traffic. If the entry is inactive for the duration that is specified in the update-interval seconds command, the entry is removed from the cache. If you enter the no logging ip access-list cache command without keywords, all the parameters are returned to the default values. When enabling the IP "too short" check using the mls verify ip length minimum command, valid IP packets with with an IP protocol field of ICMP(1), IGMP(2), IP(4), TCP(6), UDP(17), IPv6(41), GRE(47), or SIPP-ESP(50) will be hardware switched. All other IP protocol fields are software switched. Caution Using optimized access-list logging (OAL) and the mls verify ip length minimum command together can cause routing protocol neighbor flapping as they are incompatible

**Example:**

This example shows how to enable OAL on ingress packets:

```text
Router(config-if)#
logging ip access-list cache in
```

This example shows how to enable OAL on egress packets:

```text
Router(config-if)#
logging ip access-list cache out
```


### `logging persistent (config-archive-log-cfg)`

> **Página:** 295 · **Modo:** Archive configuration mode, log config (configuration-change logger) submode (config-archive-log-cfg)# · **Default:** The configuration commands are not saved to the Cisco IOS secure file system. · **Leitura (show/clear/…):** não

**Description:** To enable the configuration logging persistent feature and to select how the configuration commands are to be saved to the Cisco IOS secure file system, use the logging persistent command in the log config submode of archive configuration mode. To disable this capability, use the no form of this command. logging persistent {auto | manual}

**Syntax:**

```text
no logging persistent {auto | manual}
```

**Parameters (Syntax Description):**

- `auto` — Specifies that each configuration command will be save d automatic all y to the Cisco IOS secure filesystem.
- `manual` — Specifies that each configuration command must be save d m an u all y to the Cisco IOS secure file system.

**Command Default:** The configuration commands are not saved to the Cisco IOS secure file system.

**Command Modes:** Archive configuration mode, log config (configuration-change logger) submode (config-archive-log-cfg)#

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(26)S | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.4(11)T | This command was integrated into Cisco IOS Release12.4(11) T. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B. |

**Usage Guidelines:**

When you use the manualkeyword, you must save each configuration command manually to the Cisco IOS secure file system. To do this, you must use the archive log config persistent save command.

**Example:**

The following example automatically saves the configuration commands to the Cisco IOS secure file system:

```text
Router(config)# archive
Router(config-archive)# log config
Router(config-archive-log-cfg)# logging enable
Router(config-archive-log-cfg)# logging persistent auto
```


### `logging persistent reload (config-archive-log-cfg)`

> **Página:** 296 · **Modo:** Archive config mode; log config (configuration change logger) submode (config-archive-log-cfg)# · **Default:** The configuration commands saved in the configuration logger database are not applied to the running-config file. · **Leitura (show/clear/…):** não

**Description:** To sequentially apply the configuration commands saved in the configuration logger database (since the last write memorycommand) to the running-config file after a reload, use the logging persistent reload command in configuration change logger configuration mode in archive configuration mode. To disable this capability, use the no form of this command. logging persistent reload

**Syntax:**

```text
no logging persistent reload
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** The configuration commands saved in the configuration logger database are not applied to the running-config file.

**Command Modes:** Archive config mode; log config (configuration change logger) submode (config-archive-log-cfg)#

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRA | This command was introduced. |
| 12.4(11)T | This command was integrated into Cisco IOS Release12.4(11) T. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B. |

**Usage Guidelines:**

Use the logging persistent reload command when you want changed configuration commands to take effect on the next reload of the router.

**Example:**

The following example applies the configuration commands in the configuration logger database to the running-config file after the next reload:

```text
Router(config-archive-log-cfg)# logging persistent reload
```


### `logging purge-log buffer days`

> **Página:** 297 · **Modo:** Global Configuration · **Default:** The volatile memory contains the entries of the logging buffer. · **Leitura (show/clear/…):** não

**Description:** To automatically delete the entries from the logging buffer after a configurable time, use the logging purge-log bufferdays command in global configuration mode. To disable this capability, use the no form of this command. [ ]

**Syntax:**

```text
logging purge-log buffer days number-of-days time deletion-start-time
no logging purge-log buffer
```

**Parameters (Syntax Description):**

- `days` — number-of-days Specifies the number of days. The values range from 1 to 120.
- `time` — ( Optional) Specifies d e l e t i on start time using a 24 hour clock (hh:mm). d e l e t i on-start-time

**Command Default:** The volatile memory contains the entries of the logging buffer.

**Command Modes:** Global Configuration

**Usage Guidelines:**

Use the logging purge-log bufferdays command to automatically purge the logging data after a given time. Example The following example shows how to enable automatic log deletion after 90 days.

```text
Router (config)# logging purge-log buffer days 90 time 15:45
*May 18 20:20:20 UTC: %DMI-5-SYNC_NEEDED: R0/0: dmiauthd: Configuration change requiring
running configuration sync detected - ' logging purge-log buffer days 90 time 15:45
'. The running configuration will be sy
nchronized to the NETCONF running data store.
◦ May 18 20:20:21 UTC: %DMI-5-SYNC_START: R0/0: dmiauthd: Synchronization of the running
configuration to the NETCONF running data store has started.
May 18 20:20:26 UTC: %DMI-5-SYNC_COMPLETE: R0/0: dmiauthd: The running configuration has
been synchronized to the NETCONF running data store.
```


### `logging size`

> **Página:** 298 · **Modo:** Configuration change logger configuration (config-archive-log-config) · **Default:** 100 entries · **Leitura (show/clear/…):** não

**Description:** To specify the maximum number of entries retained in the configuration log, use the logging size command in configuration change logger configuration mode. To reset the default value, use the no form of this command.

**Syntax:**

```text
logging size entries
no logging size
```

**Parameters (Syntax Description):**

- `entries` — The maximum number of e n t r i e s r e t a in e d in the configuration log. V a l id values range from1 to 1000. The default value is100 e n t r i e s.

**Command Default:** 100 entries

**Command Modes:** Configuration change logger configuration (config-archive-log-config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(4)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(27)SBC | This command was integrated into Cisco IOS Release12.2(27) S B C. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

When the configuration log is full, the oldest log entry is removed every time a new entry is added. Note If a new log size is specified that is smaller than the current log size, the oldest entries will be immediately purged until the new log size is satisfied, regardless of the age of the log entries.

**Example:**

The following example shows how to specify that the configuration log may have a maximum of 200 entries:

```text
Device(config-archive-log-config)# logging size 200
```

The following example shows how to clear the configuration log by reducing the log size to 1, then resetting the log size to the desired value. Only the most recent configuration log file will be saved.

```text
Device(config)# archive
Device(config-archive)# log config
Device(config-archive-log-config)# logging size 1
Device(config-archive-log-config)# logging size 200
```


### `logging synchronous`

> **Página:** 299 · **Modo:** Line configuration · **Default:** This command is disabled. If you do not specify a severity level, the default value of 2 is assumed. If you do not specify the maximum number of buffers to be queued, the default value of 20 is assumed. · **Leitura (show/clear/…):** não

**Description:** To synchronize unsolicited messages and debug output with solicited Cisco IOS software output and prompts for a specific console port line, auxiliary port line, or vty, use the logging synchronous command in line configuration mode. To disable synchronization of unsolicited messages and debug output, use the no form of this command.

**Syntax:**

```text
logging synchronous [level severity-level | all] [limit number-of-lines]
no logging synchronous [level severity-level | all] [limit number-of-lines]
```

**Parameters (Syntax Description):**

- `level` — s e v e r it y-level ( Optional) Specifies the message s e v e r it y level. Message s with a s e v e r it y level
- `level s e v e r it y-level` — ( Optional) Specifies the message s e v e r it y level. Message s with as e v e r it y level e q u a l to or h i g h e r than this value are p r in t e d async h r on o u s l y. Low numbers in d i c at e g r e at e r s e v e r it y and h i g h numbers in d i c at e l e s s e r s e v e r it y. The default value is2.
- `all` — ( Optional) Specifies that all message s are p r in t e d async h r on o u s l y, r e g a r d l e s s of these v e r it y level.
- `limit number-of-lines` — ( Optional) Specifies then u m be r of buffer lines to be queue d for the terminal, after which n e w message s are d r o p p e d. The default value is20.

**Command Default:** This command is disabled. If you do not specify a severity level, the default value of 2 is assumed. If you do not specify the maximum number of buffers to be queued, the default value of 20 is assumed.

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2SX | This command is supported in the Cisco IOS Release12.2 S X t r a in. Support in as p e c if i c 12.2 S X release of this t r a in d e p end s on your f e at u reset, platform, and platform hardware. |

**Usage Guidelines:**

When synchronous logging of unsolicited messages and debug output is turned on, unsolicited Cisco IOS software output is displayed on the console or printed after solicited Cisco IOS software output is displayed or printed. This keeps unsolicited messages and debug output from being interspersed with solicited software output and prompts. Tip This command is useful for keeping system messages from interrupting your typing. By default, messages will appear immediately when they are processed by the system, and the CLI cursor will appear at the end of the displayed message. For example, the line “Configured by console from console” may be printed to the screen, interrupting whatever command you are currently typing. The logging synchronous command allows you to avoid these potentially annoying interruptions without have to turn off logging to the console entirely. When this command is enabled, unsolicited messages and debug output are displayed on a separate line than user input. After the unsolicited messages are displayed, the CLI returns to the user prompt. Note This command is also useful for allowing you to continue typing when debugging is enabled. When specifying a severity level number, consider that for the logging system, low numbers indicate greater severity and high numbers indicate lesser severity. When a message queue limit of a terminal line is reached, new messages are dropped from the line, although these messages might be displayed on other lines. If messages are dropped, the notice “ %SYS-3-MSGLOST number-of-messages due to overflow” follows any messages that are displayed. This notice is displayed only on the terminal that lost the messages. It is not sent to any other lines, any logging servers, or the logging buffer. Caution By configuring abnormally large message queue limits and setting the terminal to “terminal monitor” on a terminal that is accessible to intruders, you expose yourself to “denial of service” attacks. An intruder could carry out the attack by putting the terminal in synchronous output mode, making a Telnet connection to a remote host, and leaving the connection idle. This could cause large numbers of messages to be generated and queued, and these messages could consume all available RAM. You should guard against this type of attack through proper configuration.

**Example:**

In the following example, a system message appears in the middle of typing the show running-config command:

```text
Router(config-line)# end
Router# show ru
2w1d: %SYS-5-CONFIG_I: Configured from console by consolenning-config
```

The user then enables synchronous logging for the current line (indicated by the * symbol in the show line command), after which the system displays the system message on a separate line, and returns the user to the prompt to allow the user to finish typing the command on a single line:

```text
Router# show line
Tty Typ Tx/Rx A Modem Roty AccO AccI Uses Noise Overruns Int
* 0 CTY - - - - - 0 3 0/0 -
Router# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)# line 0
Router(config-line)# logging syn
<tab>
Router(config-line)# logging synchronous
Router(config-line)# end
Router# show ru
2w1d: %SYS-5-CONFIG_I: Configured from console by console
show running-config
```

In the following example, synchronous logging for line 4 is enabled with a severity level of 6. Then synchronous logging for line 2 is enabled with a severity level of 7 and is specified with a maximum number of buffer lines of 1,000.

```text
Router(config)# line 4
Router(config-line)# logging synchronous level 6
Router(config-line)# exit
Router(config)# line 2
Router(config-line)# logging synchronous level 7 limit 1000
Router(config-line)# end
```


### `logging system`

> **Página:** 302 · **Modo:** Global configuration (config) · **Default:** By default, SEA logging feature is enabled, and the events are logged to a file on a persistent storage device (bootflash: or disk:). · **Leitura (show/clear/…):** não

**Description:** To enable System Event Archive (SEA) logging, use the logging systemcommand in global configuration mode. To disable SEA logging, use the no form of this command.

**Syntax:**

```text
logging system [disk name]
no logging system
```

**Parameters (Syntax Description):**

- `disk name` — ( Optional) S to r e s the system event archive( system event logfile) in the specified disk. The specified disk must be a l r e a d y have been configure d to all o w for the s to r age of the system event archive.

**Command Default:** By default, SEA logging feature is enabled, and the events are logged to a file on a persistent storage device (bootflash: or disk:).

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SXH | This command was introduced. |
| 12.2(33)SCC | The command was introduced for the Ciscou B R10012 router in the Cisco IOS Software Release12.2(33) S C C. |

**Usage Guidelines:**

SEA is supported on switches that have a Supervisor Engine 32 or Supervisor Engine 720 with a compact flash adapter and a Compact Flash card (WS-CF-UPG= for Supervisor Engine 720). To stop SEA logging to a specified disk, use the default logging system command. For documentation of the configuration tasks associated with this feature, see the chapter “Configuring the System Event Archive” in the Catalyst 6500 Release 12.2SX Software Configuration Guide . Cisco Universal Broadband Router 100112 The SEA feature is used to address the deficiencies of the debug trace and system console. Support for SEA feature was introduced on Cisco uBR10012 Router in the Cisco IOS Release 12.2(33)SCC. Use the logging system disk command to change the location of the disk used to store the sea_log.dat file. Note To store the system event logs, the SEA requires either PCMCIA ATA disk or Compact Flash disk in compact flash adapter for PRE2.

**Example:**

The following example shows how to specify that the SEA log file should be written to the disk “disk1:”:

```text
Router(config)# logging system disk disk1:
Router(config)# end
```


### `logout`

> **Página:** 303 · **Modo:** User EXEC · **Default:** No default behavior or values. · **Leitura (show/clear/…):** não

**Description:** To close an active terminal session by logging off the router, use the logout command in user EXEC mode.

**Syntax:**

```text
logout
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** No default behavior or values.

**Command Modes:** User EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

In the following example, the exit (global) command is used to move from global configuration mode to privileged EXEC mode, the disable command is used to move from privileged EXEC mode to user EXEC mode, and the logout command is used to log off (exit from the active session):

```text
Router(config)# exit
Router# disable
Router> logout
```


### `logout-warning`

> **Página:** 303 · **Modo:** Line configuration · **Default:** No warning is sent to the user. · **Leitura (show/clear/…):** não

**Description:** To warn users of an impending forced timeout, use the logout-warningcommand in line configuration mode. To restore the default, use the no form of this command.

**Syntax:**

```text
logout-warning [seconds]
logout-warning
```

**Parameters (Syntax Description):**

- `seconds` — ( Optional) Number of s e c on d s that are count e d do w n before session t e r min at i on. If no number is specified, the default of20 s e c on d s is used.

**Command Default:** No warning is sent to the user.

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command notifies the user of an impending forced timeout (set using the absolute-timeout command).

**Example:**

In the following example, a logout warning is configured on line 5 with a countdown value of 30 seconds:

```text
Router(config)# line 5
Router(config-line)# logout-warning 30
```


### `macro (global configuration)`

> **Página:** 304 · **Modo:** Global configuration (config) · **Default:** This command has no default setting. · **Leitura (show/clear/…):** não

**Description:** To create a global command macro, use the macrocommand in global configuration mode. To remove the macro, use the no form of this command.

**Syntax:**

```text
macro {global {apply macro-name | description text | trace macro-name [keyword-to-value]
value-first-keyword [keyword-to-value] value-second-keyword [keyword-to-value] value-third-keyword
[keyword-to-value]} | name macro-name}
no macro {global {apply macro-name | description text | trace macro-name [keyword-to-value]
value-first-keyword [keyword-to-value] value-second-keyword [keyword-to-value] value-third-keyword
[keyword-to-value]} | name macro-name}
```

**Parameters (Syntax Description):**

- `global` — Ap p l i e s the macro global l y.
- `apply macro-name` — Ap p l i e s as p e c if i e d macro.
- `description text` — P r o v id e s a description of the macro s ap p l i e d to the switch.
- `trace macro-name` — Ap p l i e s as p e c if i e d macro with trace enabled.
- `keyword-to-value` — ( Optional) Keyword to replace with a value.
- `value-first-keyword` — Value of the first keyword to replace.
- `value-second-keyword` — Value of these c on d keyword to replace.
- `value-third-keyword` — Value of the t h i r d keyword to replace.
- `name macro-name` — Specifies then a m e of a macro.

**Command Default:** This command has no default setting.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SXH | This command was introduced. |
| 15.0(1)M | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |

**Usage Guidelines:**

You can enter up to three keyword pairs using the macro global trace command. You can enter the macro global descriptioncommand on the switch stack or on a standalone switch. Use the description textkeyword and argument to associate the comment text, or the macro name with a switch. When multiple macros are applied on a switch, the description text is used from the last applied macro. You can verify the global description settings by using the show parser macro description command. To find the syntax or configuration errors, enter the macro global trace macro-name command to apply and debug the macro. To display a list of any keyword-value pairs defined in the macro, enter the macro global apply macro-name ? command. You can delete a global macro-applied configuration on a switch only by entering the no version of each command that is in the macro. Keyword matching is case sensitive. When a macro is applied on the commands, all matching occurrences of keywords are replaced with the corresponding values. The no form of the macro name command deletes only the macro definition. It does not affect the configuration of the interfaces on which the macro is already applied.

**Example:**

The following example shows how to apply the macro called snmp to set the hostname address to “test-server” and to set the IP precedence value to 7:

```text
Router(config)# macro global apply snmp ADDRESS test-server VALUE 7
```

The following example shows how to debug the macro called snmp by using the macro global trace command to find the syntax or configuration errors in the macro when it is applied to a switch:

```text
Router(config)# macro global trace snmp VALUE 7 VALUE 8 VALUE 9
Applying command...`snmp-server enable traps port-security'
Applying command...`snmp-server enable traps linkup'
Applying command...`snmp-server enable traps linkdown'
Applying command...`snmp-server host'
%Error Unknown error.
Applying command...`snmp-server ip precedence 7'
Router(config)#
```


### `macro (interface configuration)`

> **Página:** 306 · **Modo:** Interface configuration (config-if) · **Default:** This command has no default setting. · **Leitura (show/clear/…):** não

**Description:** To create an interface-specific command macro, use the macro command in interface configuration mode. To remove the macro, use the no form of this command.

**Syntax:**

```text
macro {apply macro-name | description text | trace macro-name [keyword-to-value] value-first-keyword
[keyword-to-value] value-second-keyword [keyword-to-value] value-third-keyword [keyword-to-value]}
no macro {apply macro-name | description text | trace macro-name [keyword-to-value]
value-first-keyword [keyword-to-value] value-second-keyword [keyword-to-value] value-third-keyword
[keyword-to-value]}
```

**Parameters (Syntax Description):**

- `apply macro-name` — Ap p l i e s as p e c if i e d macro.
- `description text` — Specifies a description about the macro s that are ap p l i e d to the interface.
- `trace macro-name` — Ap p l i e s as p e c if i e d macro with trace enabled.
- `keyword-to-value` — ( Optional) Keyword to replace with a value.
- `value-first-keyword` — Value of the keyword to replace.

**Command Default:** This command has no default setting.

**Command Modes:** Interface configuration (config-if)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SXH | This command was introduced. |

**Usage Guidelines:**

You can enter up to three keyword changes using the macro trace command. You can enter the macro description command on the switch stack or on a standalone switch. Use the description text keyword and argument to associate comment text, or the macro name, with a switch. When multiple macros are applied on a switch, the description text will be from the last applied macro. You can verify the description settings by entering the show parser macro description command. To find any syntax or configuration errors, enter the macro trace macro-name command to apply and debug the macro. To display a list of any keyword-value pairs defined in the macro, enter the macro apply macro-name ? command. To successfully apply the macro, you must enter any required keyword-value pairs. Keyword matching is case sensitive. In the commands that the macro applies, all matching occurrences of keywords are replaced with the corresponding values. You can delete all configuration on an interface by entering the default interface interfaceinterface configuration command.

**Example:**

The following example shows how to apply the user-created macro called desktop-config and to verify the configuration:

```text
Router(config)#
interface fastethernet1/2
Router(config-if)# macro apply desktop-config
```

The following example shows how to apply the user-created macro called desktop-config and to replace all occurrences of vlan with VLAN ID 25:

```text
Router(config-if)# macro apply desktop-config vlan 25
```


### `maximum`

> **Página:** 307 · **Modo:** Archive configuration (config-archive) · **Default:** By default, a maximum of 10 archive files of the running configuration are saved in the Cisco configuration archive. · **Leitura (show/clear/…):** não

**Description:** To set the maximum number of archive files of the running configuration to be saved in the Cisco configuration archive, use the maximum command in archive configuration mode. To reset this command to its default, use the no form of this command.

**Syntax:**

```text
maximum number
no maximum number
```

**Parameters (Syntax Description):**

- `number` — Maximum number of archive files of the running configuration to be save d in the Cisco configuration archive. You can archive from1 to14 configuration files. The default is10.

**Command Default:** By default, a maximum of 10 archive files of the running configuration are saved in the Cisco configuration archive.

**Command Modes:** Archive configuration (config-archive)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(7)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(31)SB2 | This command was i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Note Before using this command, you must configure the path command to specify the location and filename prefix for the files in the Cisco configuration archive. After the maximum number of files are saved in the Cisco configuration archive, the oldest file is automatically deleted when the next, most recent file is saved. Note This command should only be used when a local writable file system is specified in the url argument of the path command. Network file systems may not support deletion of previously saved files.

**Example:**

In the following example, a value of 5 is set as the maximum number of archive files of the running configuration to be saved in the Cisco configuration archive:

```text
configure terminal
!
archive
path disk0:myconfig
maximum 5
end
```


### `memory cache error-recovery`

> **Página:** 309 · **Modo:** Global configuration (config) · **Default:** Memory cache error recovery mechanisms are not enabled. · **Leitura (show/clear/…):** não

**Description:** To trace error recovery in memory using caches, use the memory cache error-recoverycommand in global configuration mode. To disable the memory cache error recovery mechanisms, use the no form of this command.

**Syntax:**

```text
memory cache error-recovery {L1 | L2 | L3} {data | inst}
no memory cache error-recovery {L1 | L2 | L3} {data | inst}
```

**Parameters (Syntax Description):**

- `L1` — Specifies the L1cache.
- `L2` — Specifies the L2cache.
- `L3` — Specifies the L3cache.
- `data` — Specifies if data recovery isr e q u i r e d.
- `inst` — Specifies if in s t r u c t i on recovery isr e q u i r e d.

**Command Default:** Memory cache error recovery mechanisms are not enabled.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release12.2(33) S X I. |

**Example:**

The following example shows how to enable the memory cache error-recovery command:

```text
Router> enable
Router# configure terminal
Router(config)# memory cache error-recovery
```


### `memory cache error-recovery options`

> **Página:** 310 · **Modo:** Global configuration (config) · **Default:** Memory cache error recovery mechanisms are not enabled. · **Leitura (show/clear/…):** não

**Description:** To trace error recovery in memory using caches through set options, use the memory cache error-recovery optionscommand in global configuration mode. To disable the set memory cache error recovery mechanisms, use the no form of this command.

**Syntax:**

```text
memory cache error-recovery options {abort-if-same-content | blocking-mode | max-recoveries
value | nvram-report | parity-check | window seconds}
no memory cache error-recovery options {abort-if-same-content | blocking-mode | max-recoveries
value | nvram-report | parity-check | window seconds}
```

**Parameters (Syntax Description):**

- `abort-if-same-content` — Terminate recovery if the cache c on t a in s the same c on t e n t as the memory.
- `blocking-mode` — Set s the memory b lock in g mode to special or ON.
- `max-r e c over i e s value` — The maximum number of r e c over i e s all o we d with in at i m e w in do w. Specify a value in the range0 to255.
- `nvram-report` — Save s the r e port in the NVRAM.
- `parity-check` — Set s the parity check in g mode to nor m a l or ON.
- `window seconds` — The time w in do w, in s e c on d s. Specify a value in the range1 to31536000.

**Command Default:** Memory cache error recovery mechanisms are not enabled.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release12.2(33) S X I. |

**Example:**

The following example shows how to enable the memory cache error-recovery optionscommand:

```text
Router> enable
Router# configure terminal
Router(config)# memory cache error-recovery options abort-if-same-content
```


### `memory free low-watermark`

> **Página:** 310 · **Modo:** Global configuration · **Default:** Memory threshold notifications are disabled. · **Leitura (show/clear/…):** não

**Description:** To configure a router to issue system logging message notifications when available memory falls below a specified threshold, use the memory free low-watermarkcommand in global configuration mode. To disable memory threshold notifications, use the no form of this command.

**Syntax:**

```text
memory free low-watermark {processor threshold | io threshold}
no memory free low-watermark
```

**Parameters (Syntax Description):**

- `processor threshold` — Set s the processor memory threshold in k i l o by t e s. When a v a i l a b l e processor memory f all s be low this threshold, an o t if i c at i on message is t r i g g e r e d. V a l id values are1 to 4294967295.
- `io threshold` — Set s the in p u t/ output( I/ O) memory threshold in k i l o by t e s. When a v a i l a b l e I/O memory f all s be low this threshold, an o t if i c at i on message is t r i g g e r e d. V a l id values are1to4294967295.

**Command Default:** Memory threshold notifications are disabled.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)S | This command was introduced. |
| 12.0(26)S | This command was integrated into Cisco IOS Release12.0(26) S. |
| 12.3(4)T | This command was integrated into Cisco IOS Release12.3(4) T. |
| 12.2(27)SBC | This command was integrated into Cisco IOS Release12.2(27) S B C. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Using this command, you can configure a router to issue a system logging message each time available free memory falls below a specified threshold (“low-watermark”). Once available free memory rises to 5 percent above the threshold, another notification message is generated.

**Example:**

The following example specifies a free processor memory notification threshold of 20000 KB:

```text
Router(config)#
memory free low-watermark processor 200000
```

If available free processor memory falls below this threshold, the router sends a notification message like this one:

```text
000029: *Aug 12 22:31:19.559: %SYS-4-FREEMEMLOW: Free Memory has dropped below 20000k
Pool: Processor Free: 66814056 freemem_lwm: 204800000
```

Once available free processor memory rises to a point 5 percent above the threshold, another notification message like this is sent:

```text
000032: *Aug 12 22:33:29.411: %SYS-5-FREEMEMRECOVER: Free Memory has recovered 20000k
Pool: Processor Free: 66813960 freemem_lwm: 0
```


### `memory lite`

> **Página:** 312 · **Modo:** Global configuration · **Default:** This command is enabled by default. · **Leitura (show/clear/…):** não

**Description:** To enable the memory allocation lite (malloc_lite) feature, use the memory lite command in global configuration mode. To disable this feature, use the no form of this command.

**Syntax:**

```text
memory lite
no memory lite
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command is enabled by default.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(11)T | This command was introduced. |

**Usage Guidelines:**

The malloc_lite feature was implemented to avoid excessive memory allocation overhead for situations where less than 128 bytes were required. This feature is supported for processor memory pools only. The malloc_lite feature is enabled by default. If the malloc_lite feature is disabled using the no memory litecommand, you can re-enable the feature by entering the memory lite command.

**Example:**

The following example shows how to disable the malloc_lite feature:

```text
no memory lite
```


### `memory reserve`

> **Página:** 312 · **Modo:** Global configuration (config) · **Default:** 256 KB is reserved for console memory access. 100 KB is reserved for cricial memory access. · **Leitura (show/clear/…):** não

**Description:** To reserve a specified amount of memory in kilobytes for console access and critical notifications, use the this command. Syntax for Releases 15.0(1)M and 12.2(33)SRC and Later Releases Syntax for Releases 12.2(33)SXI, Cisco IOS XE Release 2.1 and Later Releases

**Syntax:**

```text
memory reserve command in global configuration mode. To disable the configuration, use the no form of
memory reserve {console size | critical [total-size]}
no memory reserve {console | critical}
memory reserve critical [total-size]
no memory reserve critical
```

**Parameters (Syntax Description):**

- `console` — Reserve s the memory size for a c on s o l e session.
- `size` — A mount of memory to be reserve d, in k i l o by t e s. The range is from0 to4096.
- `critical` — Reserve s the memory for critical not if i c at i on s.
- `total-size` — ( Optional) To t a l a mount of memory to be reserve d, in k i l o by t e s. The range is from0 to 4294967295.

**Command Default:** 256 KB is reserved for console memory access. 100 KB is reserved for cricial memory access.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release 15.0(1)M. |
| 12.2(33)SRC | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRC. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was i m p l e m e n t e do n the Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Usage Guidelines:**

The memory reserve console command reserves enough memory to ensure console access to a Cisco IOS device for administrative and troubleshooting purposes. This feature is especially beneficial when the device runs low on memory. The memory reserve critical command reserves the specified amount of memory in kilobytes so that the router can issue critical notifications. The amount of memory reserved for critical notifications cannot exceed 25 percent of the total available memory.

**Example:**

The following example shows how to reserve a specified amount of memory in kilobytes for console access:

```text
Router# configure terminal
Router(config)# memory reserve console 2
```


### `memory reserve critical`

> **Página:** 314 · **Modo:** Global configuration (config) · **Default:** 100 kilobytes of memory is reserved for the logging process. · **Leitura (show/clear/…):** não

**Description:** Note Effective with Cisco IOS Release 12.4(15)T1, the memory reserve critical command is replaced by the memory reserve command. See the memory reserve command for more information. To configure the size of the memory region to be used for critical notifications (system logging messages), use the memory reserve criticalcommand in global configuration mode. To disable the reservation of memory for critical notifications, use the no form of this command.

**Syntax:**

```text
memory reserve critical kilobytes
no memory reserve critical
```

**Parameters (Syntax Description):**

- `k i l o by t e s` — Specifies the a mount of memory to be reserve d in k i l o by t e s. V a l id values are1 to4294967295, but the value you specify can note x c e e d25 p e r c e n to f to t a l memory. The default is100 k i l o by t e s.

**Command Default:** 100 kilobytes of memory is reserved for the logging process.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)S | This command was introduced. |
| 12.0(26)S | This command was integrated into Cisco IOS Release12.0(26) S. |
| 12.3(4)T | This command was integrated into Cisco IOS Release12.3(4) T. |
| 12.2(27)SBC | This command was integrated into Cisco IOS Release12.2(27) S B C. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.4(15)T1 | This command was replaced by the memory reserve command. |

**Usage Guidelines:**

This command reserves a region of memory on the router so that, when system resources are overloaded, the router retains enough memory to issue critical system logging messages. Note Once the size of the reserved memory region is specified, any change to the specified value takes effect only after the current configuration is saved and the system has been reloaded.

**Example:**

The following example shows how to reserve 1,000 KB of system memory for logging messages at the next system restart:

```text
Router(config)# memory reserve critical 1000
```


### `memory sanity`

> **Página:** 315 · **Modo:** Global configuration · **Default:** This command is not enabled by default. If the buffer or queue keyword is not specified, a sanity check will be performed on all buffers and queues. · **Leitura (show/clear/…):** não

**Description:** To perform a “sanity check” for corruption in buffers and queues, use the memory sanity command in global configuration mode. To disable this feature, use the no form of this command.

**Syntax:**

```text
memory sanity [buffer | queue | all]
no memory sanity
```

**Parameters (Syntax Description):**

- `buffer` — ( Optional) Specifies check in g all buffers.
- `buffer` — ( Optional) Specifies check in g all buffers.
- `queue` — ( Optional) Specifies check in g all queue s.
- `all` — ( Optional) Specifies check in g all buffers and queue s.

**Command Default:** This command is not enabled by default. If the buffer or queue keyword is not specified, a sanity check will be performed on all buffers and queues.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(15)T | This command was introduced. |

**Usage Guidelines:**

When the memory sanity buffer command is enabled, a sanity check is performed on buffers when a packet buffer is allocated or when a packet buffer is returned to the buffer pool. This command also time-stamps the buffer, which may be useful when tracking the age of a buffer. The memory sanity command can be saved in the startup configuration file and, therefore, it is not necessary to reconfigure this command each time the router is reloaded. Like the scheduler heapcheck process memory command, the memory sanity command can check for corruption in the I/O memory block. Enabling the memory sanity command may result in slight router performance degradation.

**Example:**

The following example shows how to perform a sanity check for corruption in all buffers and queues:

```text
memory sanity all
```


### `memory scan`

> **Página:** 316 · **Modo:** Global configuration · **Default:** This command is disabled by default. · **Leitura (show/clear/…):** não

**Description:** To enable the Memory Scan feature, use the memory scan command in global configuration mode. To restore the router configuration to the default, use the no form of this command.

**Syntax:**

```text
memory scan
no memory scan
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command is disabled by default.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(4)XE | This command was introduced. |
| 12.0(7)T | This command was integrated in Cisco IOS Release12.0 T for the Cisco7500 s e r i e s only. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The Memory Scan feature adds a low-priority background process that searches all installed dynamic random-access memory (DRAM) for possible parity errors. If errors are found in memory areas that are not in use, this feature attempts to scrub (remove) the errors. The time to complete one memory scan and scrub cycle can range from 10 minutes to several hours, depending on the amount of installed memory. The impact of the Memory Scan feature on the central processing unit (CPU) is minimal. To view the status of the memory scan feature on your router, use the show memory scan command in EXEC mode.

**Example:**

The following example enables the Memory Scan feature on a Cisco 7500 series router:

```text
Router(config)# memory scan
```


### `memory-size iomem`

> **Página:** 316 · **Modo:** Global configuration (config) · **Default:** The default memory allocation is 25 percent of the DRAM to I/O memory and 75 percent of the DRAM to processor memory. Note If thesmartinitprocess has been enabled, the default memory allocation of 25 percent to the I/O memory does not apply. Instead, smartinitexamines the network modules, and then calculates the memory allocation for the I/O memory. · **Leitura (show/clear/…):** não

**Description:** To reallocate the percentage of DRAM to use for I/O memory and processor memory, use the memory-size iomem command in global configuration mode. To revert to the default memory allocation, use the no form of this command.

**Syntax:**

```text
memory-size iomem i/o-memory-percentage
no memory-size iomem
```

**Parameters (Syntax Description):**

- `i/ o-memory-percentage` — The percentage of D R A M allocate d to I/ O memory, in by t e s. The values permit t e d are5,10,15,20,25,30,40,and50. A min i m u m of4 M B of memory isr e q u i r e d for I/ O memory.

**Command Default:** The default memory allocation is 25 percent of the DRAM to I/O memory and 75 percent of the DRAM to processor memory. Note If thesmartinitprocess has been enabled, the default memory allocation of 25 percent to the I/O memory does not apply. Instead, smartinitexamines the network modules, and then calculates the memory allocation for the I/O memory.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2P | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.4(15)T1 | This command was integrated into Cisco IOS Release12.4(15) T1. |

**Usage Guidelines:**

When you specify the percentage of I/O memory in the command line, the processor memory automatically acquires the remaining percentage of the DRAM memory.

**Example:**

The following example allocates 40 percent of the DRAM memory to I/O memory and the remaining 60 percent to the processor memory:

```text
configure terminal
Router(config)#
memory-size iomem 40
Smart-init will be disabled and new I/O memory size will take effect upon reload.
```


### `menu (EXEC)`

> **Página:** 317 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To display a preconfigured user menu, use the menu command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
menu menu-name
```

**Parameters (Syntax Description):**

- `menu-name` — Then a m e of the menu.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

A user menu is a type of user interface where text descriptions of actions to be performed are displayed to the user. The user can use the menu to select services and functions without having to know the details of command-line interface (CLI) commands. Menus can be created for users in global configuration mode, using the commands listed in the “Related Commands” section. A menu can be invoked at either the user or privileged EXEC level, but if an item in the menu contains a privileged EXEC command, the user must be logged in at the privileged level for the command to succeed.

**Example:**

The following example invokes a menu named OnRamp:

```text
Router> menu OnRamp
Welcome to OnRamp Internet Services
Type a number to select an option;
Type 9 to exit the menu.
1 Read email
2 UNIX Internet access
3 Resume UNIX connection
6 Resume next connection
9 Exit menu system
```


### `menu menu-name single-space`

> **Página:** 319 · **Modo:** Global configuration · **Default:** Enabled for menus with more than nine items; disabled for menus with nine or fewer items. · **Leitura (show/clear/…):** não

**Description:** To display menu items single-spaced rather than double-spaced, use the menu <menu-name> single-space command in global configuration mode.

**Syntax:**

```text
menu menu-name single-space
```

**Parameters (Syntax Description):**

- `menu-name` — Name of the menu this commands h o u l d be ap p l i e d to.

**Command Default:** Enabled for menus with more than nine items; disabled for menus with nine or fewer items.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

When more than nine menu items are defined, the menu is displayed single-spaced. To configure the menus with nine or fewer items to display single-spaced, use this command.

**Example:**

In the following example, single-spaced menu items are displayed for the menu named Access1:

```text
menu Access1 single-space
```


### `menu clear-screen`

> **Página:** 320 · **Modo:** Global configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To clear the terminal screen before displaying a menu, use the menu clear-screen command in global configuration mode.

**Syntax:**

```text
menu clear-screen menu-name clear-screen
```

**Parameters (Syntax Description):**

- `menu-name` — Name of the menu this commands h o u l d be ap p l i e d to.

**Command Default:** Disabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command uses a terminal-independent mechanism based on termcap entries defined in the router and the configured terminal type for the user. This command allows the same menu to be used on multiple types of terminals instead of having terminal-specific strings embedded within menu titles. If the termcap entry does not contain a clear string, the menu system enters 24 new lines, causing all existing text to scroll off the top of the terminal screen.

**Example:**

In the following example, the terminal screen is cleared before displaying the menu named Access1:

```text
Router(config)# menu Access1 clear-screen
```


### `menu command`

> **Página:** 321 · **Modo:** Global configuration (config) · **Default:** This command is disabled by default. · **Leitura (show/clear/…):** não

**Description:** To specify underlying commands for user menus, use the menu command command in global configuration mode. To return to default settings, use the no form of this command.

**Syntax:**

```text
menu command menu menu-name command menu-item {command | menu-exit}
```

**Parameters (Syntax Description):**

- `menumenu-name` — Name of the menu. You can specify a maximum of20 characters.
- `commandmenu-item` — Number, character, or string used as the k e y for the it e m. The k e y is d is p l a y e d to the l e f to f the menu it e m text. You can specify a maximum of18 menu e n t r i e s. When the t e n t h it e m is added to the menu, the line-mode and single-space options are activated automatic all y.
- `command` — Command to is s u e when the users e l e c t s an it e m.
- `menu-exit` — P r o v id e s a w a y form e n u users to return to a h i g h e r-level menu or exit the menu system.

**Command Default:** This command is disabled by default.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to assign actions to items in a menu. Use the menu text global configuration command to assign text to items. These commands must use the same menu name and menu selection key. The menu command command has a special keyword for the command argument, menu-exit, that is available only within menus. It is used to exit a submenu and return to the previous menu level, or to exit the menu altogether and return to the EXEC command prompt. You can create submenus that are opened by selecting entries in another menu. Use the menu EXEC command as the command for the submenu item. Note If you nest too many levels of menus, the system prints an error message on the terminal and returns to the previous menu level. When a menu allows connections (their normal use), the command for an entry activating the connection should contain a resume command, or the line should be configured to prevent users from escaping their sessions with the escape-char none command. Otherwise, when they escape from a connection and return to the menu, there will be no way to resume the session and it will sit idle until the user logs out. Specifying the resume command as the action that is performed for a selected menu entry permits a user to resume a named connection or connect using the specified name, if there is no active connection by that name. As an option, you can also supply the connect string needed to connect initially. When you do not supply this connect string, the command uses the specified connection name. You can also use the resume or next command, which resumes the next connection in the user’s list of connections. This function allows you to create a single menu entry that steps through all of the user’s connections. Note A menu should not contain any exit paths that leave users in an unfamiliar interface environment. When a particular line should always display a menu, that line can be configured with an autocommand line configuration command. Menus can be run on a per-user basis by defining a similar autocommand command for that local username. For more information about the autocommand command, see the Cisco IOS Dial Technologies Configuration Guide. Note The maximum number of menu commands that the device supports is 66.

**Example:**

In the following example, the commands to be issued when the menu user selects option 1, 2, or 3 are specified for the menu named Access1:

```text
Device (config) #menu Access1 command 1 tn3270 vms.cisco.com
Device (config) #
menu Access1 command 2 rlogin unix.cisco.com
Device (config) #
menu Access1 command 3 menu-exit
```

The following example allows a menu user to exit a menu by entering Exit at the menu prompt:

```text
menu Access1 text Exit Exit
menu Access1 command Exit menu-exit
```


### `menu default`

> **Página:** 323 · **Modo:** Global configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To specify the menu item to use as the default, use the menu default command in global configuration mode.

**Syntax:**

```text
menu menu-name default menu-item
```

**Parameters (Syntax Description):**

- `menu-name` — Name of the menu. You can specify a maximum of20 characters.
- `menu-item` — Number, character, or string k e y of the it e m to use as the default.

**Command Default:** Disabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to specify which menu entry is used when the user presses Enter without specifying an item. The menu entries are defined by the menu command and menu text global configuration commands.

**Example:**

In the following example, the menu user exits the menu when pressing Enter without selecting an item:

```text
menu Access1 9 text Exit the menu
menu Access1 9 command menu-exit
menu Access1 default
```


### `menu line-mode`

> **Página:** 324 · **Modo:** Global configuration · **Default:** Enabled for menus with more than nine items. Disabled for menus with nine or fewer items. · **Leitura (show/clear/…):** não

**Description:** To require the user to press Enter after specifying an item, use the menu line-mode command in global configuration mode.

**Syntax:**

```text
menu menu-name line-mode
```

**Parameters (Syntax Description):**

- `menu-name` — Name of the menu this commands h o u l d be ap p l i e d to.

**Command Default:** Enabled for menus with more than nine items. Disabled for menus with nine or fewer items.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

In a menu of nine or fewer items, you ordinarily select a menu item by entering the item number. In line mode, you select a menu entry by entering the item number and pressing Enter. Line mode allows you to backspace over the selected number and enter another number before pressing Enter to issue the command. This option is activated automatically when more than nine menu items are defined but also can be configured explicitly for menus of nine or fewer items. In order to use strings as keys for items, the menu line-mode command must be configured.

**Example:**

In the following example, the line-mode option is enabled for the menu named Access1:

```text
menu Access1 line-mode
```


### `menu options`

> **Página:** 325 · **Modo:** Global configuration (config) · **Default:** The menu options are disabled. · **Leitura (show/clear/…):** não

**Description:** To set options for items in user menus, use the menu options command in global configuration mode. Cisco IOS Release 10.0, 12.2(33)SRA, 12.2(33)SXI , and Later Releases Cisco IOS XE Release 3.1S and Later Releases

**Syntax:**

```text
menu menu-name options menu-item [login] [pause]
menu menu-name options menu-item {login | pause}
```

**Parameters (Syntax Description):**

- `The name of the menu. You can specify a maximum of 20 characters.`
- `menu-name` — Then a m e of the menu. You can specify a maximum of20 characters.
- `menu-item` — Number, character, or string k e y of the it e m a f f e c t e d by the option.
- `login` — ( Optional) Configure s the router to request a login before is s u in gt h e command.
- `pause` — ( Optional) Configure s the router to p a use after is s u in gt h e command and before r e d r a w in g themenu.

**Command Default:** The menu options are disabled.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease3.1S | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 3.1S. |

**Usage Guidelines:**

Use the menu command and menu text commands to define a menu entry.

**Example:**

The following example shows how to configure the router to request a login before issuing the command specified by menu entry 3 of the menu named Access1:

```text
Router(config)#
menu Access1 options 3 login
```


### `menu prompt`

> **Página:** 326 · **Modo:** Global configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To specify the prompt for a user menu, use the menu prompt command in global configuration mode.

**Syntax:**

```text
menu menu-name prompt d prompt d
```

**Parameters (Syntax Description):**

- `menu-name` — Name of the menu. You can specify a maximum of20 characters.
- `d` — A d e limit in g character that mark s the begin n in g and end of at it l e. Text d e limit e r s are characters that do not or d in a r i l y ap p e a r with in the text of at it l e, such as s l as h(/), do u b l e q u o t e("), and t i l d e(~).^ C isr e s e r v e d for special use and should not be used in the text of the title.
- `prompt` — Prompt string for the menu.

**Command Default:** Disabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Press Enter after entering the first delimiter. The router will prompt you for the text of the prompt. Enter the text followed by the delimiter, and press Enter. Use the menu command and menu text commands to define the menu selections.

**Example:**

In the following example, the prompt for the menu named Access1 is configured as “Select an item.”:

```text
Router(config)# menu Access1 prompt /
Enter TEXT message. End with the character '/'.
Select an item. /
Router(config)#
```


### `menu status-line`

> **Página:** 327 · **Modo:** Global configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To display a line of status information about the current user at the top of a menu, use the menu status-line command in global configuration mode.

**Syntax:**

```text
menu menu-name status-line
```

**Parameters (Syntax Description):**

- `menu-name` — Name of the menu this commands h o u l d be ap p l i e d to.

**Command Default:** Disabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command displays the status information at the top of the screen before the menu title is displayed. This status line includes the router’s host name, the user’s line number, and the current terminal type and keymap type (if any).

**Example:**

In the following example, status information is enabled for the menu named Access1:

```text
menu Access1 status-line
```


### `menu text`

> **Página:** 328 · **Modo:** Global configuration · **Default:** No text appears for the menu item. · **Leitura (show/clear/…):** não

**Description:** To specify the text of a menu item in a user menu, use the menu text command in global configuration mode.

**Syntax:**

```text
menu menu-name text menu-item menu-text
```

**Parameters (Syntax Description):**

- `menu-name` — Name of the menu. You can specify a maximum of20 characters.
- `menu-item` — Number, character, or string used as the k e y for the it e m. The k e y is d is p l a y e d to the l e f to f the menu it e m text. You can specify a maximum of18 menu it e m s. When the t e n t h it e m is added to the menu, the menu line-mode and menu single-space commands are activated automatic all y.
- `menu-text` — Text of the menu it e m.

**Command Default:** No text appears for the menu item.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to assign text to items in a menu. Use the menu command command to assign actions to items. These commands must use the same menu name and menu selection key. You can specify a maximum of 18 items in a menu.

**Example:**

In the following example, the descriptive text for the three entries is specified for options 1, 2, and 3 in the menu named Access1:

```text
menu Access1 text 1 IBM Information Systems
menu Access1 text 2 UNIX Internet Access
menu Access1 text 3 Exit menu system
```


### `menu title`

> **Página:** 329 · **Modo:** Global configuration · **Default:** The menu does not have a title. · **Leitura (show/clear/…):** não

**Description:** To create a title (banner) for a user menu, use the menu title command in global configuration mode.

**Syntax:**

```text
menu menu-name title d menu-title d
```

**Parameters (Syntax Description):**

- `menu-name` — Name of the menu. You can specify a maximum of20 characters.
- `d` — A d e limit in g character that mark s the begin n in g and end of at it l e. Text d e limit e r s are characters that do not or d in a r i l y ap p e a r with in the text of at it l e, such as s l as h(/), do u b l e q u o t e("), and t i l d e(~).^ C isr e s e r v e d for special use and should not be used in the text of the title.
- `menu-title` — Lines of text to ap p e a r at the to p of the menu.

**Command Default:** The menu does not have a title.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The menu title command must use the same menu name used with the menu text and menu command commands used to create a menu. You can position the title of the menu horizontally by preceding the title text with blank characters. You can also add lines of space above and below the title by pressing Enter. Follow the title keyword with one or more blank characters and a delimiting character of your choice. Then enter one or more lines of text, ending the title with the same delimiting character. You cannot use the delimiting character within the text of the message. When you are configuring from a terminal and are attempting to include special control characters, such as a screen-clearing string, you must use Ctrl-V before the special control characters so that they are accepted as part of the title string. The string ^[[H^[[J is an escape string used by many VT100-compatible terminals to clear the screen. To use a special string, you must enter Ctrl-V before each escape character. You also can use the menu clear-screen global configuration command to clear the screen before displaying menus and submenus, instead of embedding a terminal-specific string in the menu title. The menu clear-screen command allows the same menu to be used on different types of terminals.

**Example:**

In the following example, the title that will be displayed is specified when the menu named Access1 is invoked. Press Enter after the second slash (/) to display the prompt.

```text
Router(config)# menu Access1 title /^[[H^[[J
Enter TEXT message. End with the character '/'.
Welcome to Access1 Internet Services
Type a number to select an option;
Type 9 to exit the menu.
/
Router(config)#
```


### `microcode (12000)`

> **Página:** 331 · **Modo:** Global configuration · **Default:** The default is to load the image from the GRP card (system). · **Leitura (show/clear/…):** não

**Description:** To load a Cisco IOS software image on a line card from Flash memory or the GRP card on a Cisco 12000 series Gigabit Switch Router (GSR), use the microcode command in global configuration mode. To load the microcode bundled with the GRP system image, use the no form of this command.

**Syntax:**

```text
microcode {oc12-atm | oc12-pos | oc3-pos4} {flash file-id [slot] | system [slot]}
no microcode {oc12-atm | oc12-pos | oc3-pos4} [flash file-id [slot] | system [slot]]
```

**Parameters (Syntax Description):**

- `oc12-atm` — | oc12-pos | Interface name.
- `oc12-atm|oc12-pos| oc3-pos4` — Interface name.
- `flash` — Load s the image from the Flash filesystem.
- `file-id` — Specifies the device and file name of the image file to download from Flash memory. A c o l on(:) must s e p a r at e the device and file name( for example, slot0: gsr-p-m z). V a l id device s include: • bootflash:--In t e r n a l Flash memory. • slot0:--First PCM C I As l o t. • slot1:--S e c on d PCM C I As l o t.
- `slot` — ( Optional) Slot number of the line card that you w an t to copy the software image to. Slot numbers range from0 to11 for the Cisco12012 router and0 to7 for the Cisco12008 router. If you do not specify as l o t number, the Cisco IOS software image is download e do n all line card s.
- `system` — Load s the image from the software image on the GRPcard.

**Command Default:** The default is to load the image from the GRP card (system).

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2GS | This command was introduced for Cisco12000 s e r i e s GSRs. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

In addition to the Cisco IOS image that resides on the GRP card, each line card on a Cisco 12000 series has a Cisco IOS image. When the router is reloaded, the specified image is loaded onto the GRP card and then automatically downloaded to all the line cards. Normally, you want the same Cisco IOS image on the GRP card and all line cards. However, if you want to upgrade a line card with a new version of microcode for testing or to fix a defect, you might need to load a Cisco IOS image that is different from the one on the line card. Additionally, you might need to load a new image on the line card to work around a problem that is affecting only one of the line cards. To load a Cisco IOS image on a line card, first use the copy tftp command to download the Cisco IOS image to a slot on one of the PCMCIA Flash memory cards. Then use the microcode command to download the image to the line card, followed by the microcode reload command to start the image. Immediately after you enter the microcode reload command and press Return, the system reloads all microcode. Global configuration mode remains enabled. After the reloading is complete, enter the exit command to return to the EXEC system prompt. To verify that the correct image is running on the line card, use the execute-on slot slot show version command. For additional information on GSR configuration, refer to the documentation specific to your Cisco IOS software release.

**Example:**

In the following example, the Cisco IOS software image in slot 0 is downloaded to the line card in slot 10. This software image is used when the system is booted, a line card is inserted or removed, or the microcode reloadglobal configuration command is issued.

```text
Router(config)# microcode oc3-POS-4 flash slot0:fip.v141-7 10
Router(config)# microcode reload 10
```

In this example, the user would issue the execute-on slot 10 show version command to verify that the correct version is loaded.


### `microcode (7000/7500)`

> **Página:** 332 · **Modo:** Global configuration · **Default:** The default is to load from the microcode bundled in the system image. · **Leitura (show/clear/…):** não

**Description:** To specify the location of the microcode that you want to download from Flash memory into the writable control store (WCS) on Cisco 7000 series (including RSP based routers) or Cisco 7500 series routers, use the microcode command in global configuration mode. To load the microcode bundled with the system image, use the no form of this command.

**Syntax:**

```text
microcode interface-type {flash-filesystem:filename [slot] | rom | system [slot]}
no microcode interface-type {flash-filesystem:filename [slot] | rom | system [slot]}
```

**Parameters (Syntax Description):**

- `interface-type` — One of the following interface processor names: a ip, c ip, e ip, f e ip, f ip, f s ip, h ip, m ip, s ip, s p, s s p, t r ip, v ip, or v ip2
- `flash-filesystem :` — Flash filesystem, f o l low e d by a c o l on. V a l id filesystem s are bootflash, slot0, and slot1 S e c on d a r y device s such as slave slot0 are in v a l id. These c on d a r y’ s filesystem is not a v a i l a b l e d u r in g microcode reload s.
- `file name` — Name of the microcode file.
- `slot` — ( Optional) Number of the slot. Range is from0 to15.
- `rom` — If ROM is specified, the router load s from the on b o a r d ROM microcode.
- `system` — If the system keyword is specified, the router load s the microcode from the microcode bundle d into the system image you are running for that interface type.

**Command Default:** The default is to load from the microcode bundled in the system image.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If you do not use the microcode reload command after using the microcode command, the microcode reload command will be written to the configuration file automatically. When using Dual RSPs for simple hardware backup, ensure that the primary and secondary RSP card contain the same microcode image in the same location when the router is to load the interface processor microcode from a Flash file system. Thus, if the secondary RSP becomes the primary, it will be able to find the microcode image and download it to the interface processor.

**Example:**

In the following example, all FIP cards will be loaded with the microcode found in Flash memoryfile fip.v141-7 when the system is booted, when a card is inserted or removed, or when the microcode reloadglobal configuration command is issued. The configuration is then written to the startup configuration file.

```text
Router(config)#
microcode fip slot0:fip.v141-7
Router(config)# end
Router# copy system:running-config nvram:startup-config
```


### `microcode (7200)`

> **Página:** 333 · **Modo:** Global configuration · **Default:** If the default or noform of the command is specified, the driver uses the default microcode for the current running version of the Cisco IOS software. · **Leitura (show/clear/…):** não

**Description:** To configure a default override for the microcode that is downloaded to the hardware on a Cisco 7200 series router, use the microcode command in global configuration mode. To revert to the default microcode for the current running version of the Cisco IOS software, use the no form of this command.

**Syntax:**

```text
microcode {ecpa | pcpa} location
no microcode {ecpa | pcpa}
```

**Parameters (Syntax Description):**

- `ecpa` — E S C ON C h an n e l Port A d ap t e r( C P A) interface.
- `pcpa` — P a r all e l C P A interface.
- `location` — Location of microcode, in c l u d in gt h e device and file name.

**Command Default:** If the default or noform of the command is specified, the driver uses the default microcode for the current running version of the Cisco IOS software.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3(3)T | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If there are any default overrides when the configuration is written, then the microcode reload command will be written to the configuration automatically. This action enables the configured microcode to be downloaded at system startup. The CPA microcode image is preloaded on Flash memory cards for Cisco 7200-series routers for Cisco IOS Release 11.3(3)T and later releases. You may be required to copy a new image to Flash memory when a new microcode image becomes available. For more information on the CPA configuration and maintenance, refer to the “Configuring Cisco Mainframe Channel Connection Adapters” chapter in the Release 12.2 Cisco IOS Bridging and IBM Networking Configuration Guide.

**Example:**

The following example instructs the Cisco IOS software to load the microcode from an individual microcode image that is stored as a file on the Flash card inserted in Flash card slot 0:

```text
microcode ecpa slot0:xcpa26-1
```


### `microcode reload (12000)`

> **Página:** 334 · **Modo:** Global configuration · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To reload the Cisco IOS image from a line card on Cisco 12000 series routers, use the microcode reload command in global configuration mode.

**Syntax:**

```text
microcode reload [slot-number]
```

**Parameters (Syntax Description):**

- `slot-number` — ( Optional) Slot number of the line card that you w an t to reload the Cisco IOS software image on. Slot numbers range from0 to11 for the Cisco12012 and from0 to7 for the Cisco12008 router. If you do not specify as l o t number, the Cisco IOS software image isr e load e do n all line card s.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2GS | This command was introduced for Cisco12000 s e r i e s GSRs. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

In addition to the Cisco IOS image that resides on the GRP card, each line card on Cisco 12000 series routers has a Cisco IOS image. When the router is reloaded, the specified Cisco IOS image is loaded onto the GRP card and automatically downloaded to all the line cards. Normally, you want the same Cisco IOS image on the GRP card and all line cards. However, if you want to upgrade a line card with a new version of microcode for testing or to fix a defect, you might need to load a different Cisco IOS image. Additionally, you might need to load a new image on the line card to work around a problem affecting only one of the line cards. To load a Cisco IOS image on a line card, first use the copy tftp command to download the Cisco IOS image to a slot on one of the PCMCIA Flash memory cards. Then use the microcode command to download the image to the line card, followed by the microcode reload command to start the image. To verify that the correct image is running on the line card, use the execute-on slot slot show version command. For additional information on GSR configuration, refer to the “Observing System Startup and Performing a Basic Configuration” chapter in the Cisco 12000 series installation and configuration guides. The microcode reload (12000) command allows you to issue another command immediately. Issuing a microcode reload command on any of the line cards in a Cisco 12000 GSR immediately returns the console command prompt. This allows you to issue a subsequent command immediately to the reloading line card. However, any commands entered at this time will not execute, and often no indication will be given that such a command failed to run. Verify that the microcode has reloaded before issuing new commands.

**Example:**

In the following example, the mirocode firmware is reloaded on the line card in slot 10:

```text
Router(config)# microcode reload 10
```


### `microcode reload (7000 7500)`

> **Página:** 335 · **Modo:** Global configuration · **Default:** No default behaviors or values. · **Leitura (show/clear/…):** não

**Description:** To reload the processor card on the Cisco 7000 series with RSP7000 or Cisco 7500 series routers, use the microcode reload command in global configuration mode.

**Syntax:**

```text
microcode reload [slot-number]
```

**Parameters (Syntax Description):**

- `slot-number` — ( Optional) Reload s the specified processor card slot on a Cisco7500 s e r i e s router.

**Command Default:** No default behaviors or values.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced for Cisco7500 s e r i e s routers. |
| 12.3(8)T | The slot-number argument was added for Cisco7500 s e r i e s routers. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command reloads the microcode without rebooting the router. Immediately after you enter the microcode reload command, the system reloads all microcode. Global configuration mode remains enabled. Note If you modify the system configuration to load a microcode image, the microcode reload command will be written to the configuration file automatically following the use of a microcode command. This action enables the configured microcode to be downloaded at system startup.

**Example:**

In the following example, all controllers are reset, and the microcode specified in the current configuration is loaded:

```text
Router(config)# microcode reload
```


### `microcode reload (7200)`

> **Página:** 336 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To reload the Cisco IOS microcode image on an ESCON CPA card in the Cisco 7200 series router, use the microcode reload command in privileged EXEC mode.

**Syntax:**

```text
microcode reload {all | ecpa [slot slot-number] | pcpa [slot slot-number]}
```

**Parameters (Syntax Description):**

- `all` — Reset s and reload s all hardware type s that support download a b l e microcode.
- `ecpa` — Reset s and reload s only those slot s that c on t a in hardware type e c p a.
- `pcpa` — Reset s and reload s only those slot s that c on t a in hardware type p c p a.
- `slot slot-number` — ( Optional) Reset s and reload s only the slot specified, and only if it c on t a in s the hardware specified.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3(3)T | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Hardware types that do not support downloadable microcode are unaffected by the microcode reload all command. You will be prompted for confirmation before the microcode reloadcommand is executed.

**Example:**

The following example reloads the ESCON CPA microcode in slot 5 with the currently configured microcode:

```text
Router# microcode reload ecpa slot 5
```


### `mkdir`

> **Página:** 337 · **Modo:** User EXEC (>) Privileged EXEC (#) Diagnostic (diag) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To create a new directory in a Class C flash file system, use the mkdir command in user EXEC, privileged EXEC, or diagnostic mode.

**Syntax:**

```text
mkdir directory
```

**Parameters (Syntax Description):**

- `directory` — Then a m e of the directory to c r e at e.

**Command Modes:** User EXEC (>) Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.1 | This command was modified and i m p l e m e n t e do n the Cisco ASR1000 A g g r e g at i on Service s Routers. The following e n h an c e m e n t s were m a d e: • This command was introduced in diagnostic mode. The command can be enter e d in both privileged EXEC and diagnostic mode on the Cisco ASR 1000 S e r i e s Routers. • The h a r d disk:, o b f l:, s t by-h a r d disk:, s t by-nvram:, s t by-o b f l:, s t by-usb[0-1]:, and usb[0-1]: directory options were added. |

**Usage Guidelines:**

This command is valid only on Class C flash file systems. When executing the mkdir directory command on a USB token device, you can create only two levels of subdirectories under a directory. A new directory (third level directory) cannot be created on the USB token, but you can copy files to the existing subdirectories.

**Example:**

The following example creates a directory named newdir:

```text
Router# mkdir newdir
Mkdir file name [newdir]?
Created dir flash:newdir
dir
Directory of flash:
2 drwx 0 Mar 13 1993 13:16:21 newdir
8128000 bytes total (8126976 bytes free)
```


### `mkdir disk0:`

> **Página:** 338 · **Modo:** EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** não

**Description:** To create a new directory in a Flash file system, use the mkdir disk0:command.

**Syntax:**

```text
mkdir disk0:
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default settings.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to the12.2 S X release. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is valid only on Flash file systems. After you enter the mkdir disk0: command, you are prompted to enter the new directory filename. To check your entry, enter the dir command. To remove a directory, enter the rmdir command.

**Example:**

This example shows how to create a directory named newdir:

```text
Router# mkdir disk0:
Create directory filename [ ]? newdir
Created dir disk0: newdir
```


### `mode`

> **Página:** 339 · **Modo:** Redundancy configuration (config-red) · **Default:** • The default is SSO mode if the system is not configured for redundancy and the active and standby supervisor engines have the same image. • The default is RPR mode if different versions are installed. • If redundancy is enabled, the default is the mode that you have configured. • The default is RPR+ mode if the system is not configured for redundancy and the active and standby supervisor engines have the same image. • The default is RPR mode if different versions are installed. • If redundancy is enabled, the default is the mode that you have configured. • The default is SSO mode if the system is not configured for redundancy and the active and standby supervisor engines have the same image. • The default is RPR mode if different versions are installed. • The default is SSO mode if the system is not configured for redundancy and the active and standby supervisor engines have the same image. • The default is RPR mode if different versions are installed. · **Leitura (show/clear/…):** não

**Description:** To set the redundancy mode, use the mode command in redundancy configuration mode. Syntax for 12.2S Release Syntax for Cisco IOS XE Release 2.5 and Later Releases Syntax for 12.2XNE Release

**Syntax:**

```text
mode {rpr | rpr-plus | sso}
mode {rpr | sso}
mode sso
```

**Parameters (Syntax Description):**

- `rpr` — Specifies Route Processor Redundancy( R P R) mode.
- `rpr-plus` — Specifies Route Processor Redundancy P l u s( R P R+) mode.
- `sso` — Specifies state f u l switch over( S S O) mode.

**Command Default:** • The default is SSO mode if the system is not configured for redundancy and the active and standby supervisor engines have the same image. • The default is RPR mode if different versions are installed. • If redundancy is enabled, the default is the mode that you have configured. • The default is RPR+ mode if the system is not configured for redundancy and the active and standby supervisor engines have the same image. • The default is RPR mode if different versions are installed. • If redundancy is enabled, the default is the mode that you have configured. • The default is SSO mode if the system is not configured for redundancy and the active and standby supervisor engines have the same image. • The default is RPR mode if different versions are installed. • The default is SSO mode if the system is not configured for redundancy and the active and standby supervisor engines have the same image. • The default is RPR mode if different versions are installed.

**Command Modes:** Redundancy configuration (config-red)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | This command was introduced on the Supervisor E n g in e720. |
| 12.2(17b)SXA | This command was modified. Support was added for S S O mode and the default mode c h an g e. |
| 12.2(17d)SXB | This command was modified. Support was added form u l t i c as t and u n i c as t traffic. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)XNE | This command was modified. This command was i m p l e m e n t e do n the Cisco 10000 router. |
| CiscoIOSXERelease2.5 | This command was modified. This command was i m p l e m e n t e do n the Cisco AS R1000 S e r i e s Routers. |

**Usage Guidelines:**

Cisco IOS Release 12.2S and 7600 Series Routers SSO is not supported on Cisco 7600 series routers that are configured with a Supervisor Engine 2. On releases prior to Release 12.2(17d)SXB, single router mode (SRM) with SSO redundancy does not support stateful switchover for multicast traffic. When a switchover occurs, all multicast hardware switching entries are removed and are then re-created and reinstalled in the hardware by the newly active multilayer switch feature card (MSFC). SRM/SSO is supported in the following releases only: • Release 12.2(17b)SXA and subsequent rebuilds. • Release 12.2(17d)SXB and subsequent rebuilds. Nonstop forwarding (NSF) with SSO redundancy mode supports IPv4. NSF with SSO redundancy mode does not support IPv6, Internetwork Packet Exchange (IPX), and Multiprotocol Label Switching (MPLS). If you have configured MPLS on the Cisco 7600 series routers with redundant supervisor engines, you must configure the Cisco 7600 series router in RPR mode. The switch should not be running in the default mode of SSO. Enter the redundancy command in global configuration mode to enter redundancy configuration mode. You can enter the mode command within redundancy configuration mode. Follow these guidelines when configuring your system for RPR+ mode: • You must install compatible images on the active and standby supervisor engines to support RPR+ mode and SSO mode. • Both supervisor engines must run the same Cisco IOS software version. • Any modules that are not online at the time of a switchover are reset and reloaded on a switchover. • The Forwarding Information Base (FIB) tables are cleared on a switchover. As a result, routed traffic is interrupted until route tables reconverge. The standby supervisor engine reloads on any change of mode and begins to work in the current mode. When you use this command to force the standby supervisor engine to run as a Distributed Forwarding Card (DFC) card, the uplink ports in the standby engine continue to be in use and are not disabled. Cisco IOS Release XE Release 2.5 and ASR 1000 Series Routers For Cisco ASR 1002 and 1004 routers, RRP and stateful switchover can be used to switch between Cisco IOS processes. RPR and SSO need to be configured by the user, however, because a second Cisco IOS process is not available by default on Cisco ASR 1002 and 1004 routers. Enter the redundancy command in global configuration mode to enter redundancy configuration mode. You can enter the mode command within redundancy configuration mode. The Cisco ASR 1006 Router supports a second Route Processor. The second Cisco IOS process can run only on the standby Route Processor. This means that hardware redundancy is available and RPR and SSO do not need to be configured by the user because a second Cisco IOS process is available by default on the Cisco ASR 1006 router. RPR+ mode is not supported on the Cisco ASR 1000 Series Routers. Cisco IOS Release 12.2XNE and 1000 Series Routers Enter the redundancy command in global configuration mode to enter redundancy configuration mode. You can enter the command within redundancy configuration mode. mode RPR mode is not supported on the Cisco 10000 router.

**Example:**

This example shows how to set the redundancy mode to RPR+:

```text
Router(config)# redundancy
Router(config-red)# mode rpr-plus
```

This example shows how to set the redundancy mode to SSO:

```text
Router(config)# redundancy
Router(config-red)# mode sso
```
