# Capítulo 7: monitor event-trace through Q

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## L through mode

### monitor event-trace through Q

• monitor event-trace through Q, on page 320

### monitor event-trace through Q

### `monitor event-trace (EXEC)`

> **Página:** 344 · **Modo:** Privileged EXEC (#) · **Default:** The event trace function is disabled by default. · **Leitura (show/clear/…):** não

**Description:** To monitor and control the event trace function for a specified Cisco IOS software subsystem component, use the monitor event-trace command in privileged EXEC mode. | one-shot} Cisco 10000 Series Routers Catalyst 6500 Series Switches and Cisco 7600 Series Routers

**Syntax:**

```text
monitor event-trace component {clear | continuous | destroy-buffer | disable | dump [pretty] | enable
monitor event-trace component {disable | dump | enable | size | stacktrace}
monitor event-trace all-traces {continuous [cancel] | dump [merged] [pretty]}
monitor event-trace l3 {clear | continuous [cancel] | disable | dump [pretty] | enable | interface type
mod/port | one-shot}
monitor event-trace spa {clear | continuous [cancel] | disable | dump [pretty] | enable | one-shot}
monitor event-trace subsys {clear | continuous [cancel] | disable | dump [pretty] | enable | one-shot}
```

**Parameters (Syntax Description):**

- `c o m p one n t` — Name of the Cisco IOS software subsys t e m c o m p one n t that is the s u b j e c to f the event trace. To get a list of c o m p one n t s that support event t r a c in g, use the monitor event-trace? command.
- `clear` — Clear s e x is t in gt r a c e message s for the specified c o m p one n t from memory on the network in g device.
- `c on t in u o u s` — C on t in u o u s l y d is p l a y s the l at e s t event trace e n t r i e s.
- `destroy-buffer` — Clear s the buffer( in v o l at i l e memory) of the trace data. R e l e v an to n l y for subscriber ppp event.
- `disable` — T u r n s of f event t r a c in g for the specified c o m p one n t.
- `dump` — Write s the event tracer e s u l t s to the file configure d using the monitor event-trace command in global configuration mode. The trace message s are save d in b in a r y format.
- `pretty` — ( Optional) Save s the event trace message in ASCII format.
- `enable` — T u r n s one v e n t t r a c in g for the specified c o m p one n t.
- `one-shot` — Clear s any e x is t in gt r a c e information from memory, start s event t r a c in g a g a in, and disable s the trace when the tracer each e s the size specified using the monitor event-trace command in global configuration mode.
- `size` — Set s then u m be r of message s that can be w r it t e n to memory for as in g l e in s t an c e of at r a c e. Note Some Cisco IOS software subsys t e m c o m p one n t s set the size by default. To d is p l a y the size parameter, use the showmon it or event-trace c o m p one n t parameters command. When then u m be r of event trace message s in memory e x c e e d s the size, n e w message s will begin to overwrite the o l d e r message s in the file.
- `stacktrace` — Enable s the stacktrace at trace p o in t s.
- `all-traces` — D is p l a y s the configure d m e r g e d-event traces.
- `merged` — ( Optional) Dump s the e n t r i e s in all event traces s or t e d by time.
- `l3` — D is p l a y s information about the L a y e r3 trace.
- `spa` — D is p l a y s information about the Shared Port A d ap t e r( S P A) trace.
- `interface typemod / port` — Specifies the interface to be log g e d.
- `cancel` — ( Optional) Can c e l s the c on t in u o u s d is p l a y of l at e s t trace e n t r i e s.
- `subsys` — D is p l a y s information about the subsys t e m’ s in it i a l trace.

**Command Default:** The event trace function is disabled by default.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(18)S | This command was introduced. |
| 12.2(8)T | This command was integrated into Cisco IOS Release12.2(8) T. |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. The monitor event-trace c e f ip v4 clear command replace s the clear ip c e f event-log command. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s routers. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.4(20)T | This command was integrated into Cisco IOS Release12.4(20) T. |
| IOSXEFuji 16.9.1 | The subscriber ppp c o m p one n t was added, and the destroy-buffer keyword was added for use with this c o m p one n t. |

**Usage Guidelines:**

Use the monitor event-trace command to control what, when, and how event trace data is collected. Use this command after you have configured the event trace functionality on the networking device using the monitor event-trace command in global configuration mode. Note The amount of data collected from the trace depends on the trace message size configured using the monitor event-tracecommand in global configuration mode for each instance of a trace. The Cisco IOS software allows for the subsystem components to define whether support for event tracing is enabled or disabled at boot time. You can enable or disable event tracing in two ways: using the monitor event-tracecommand in privileged EXEC mode or using the monitor event-tracecommand in global configuration mode. To disable event tracing, you would enter either of these commands with the disable keyword. To enable event tracing again, you would enter either of these commands with the enable keyword. To determine whether you can enable event tracing on a subsystem, use the monitor event-trace ?commandto get a list of software components that support event tracing. To determine whether event tracing is enabled by default for the subsystem, use the show monitor event-trace command to display trace messages. Use the show monitor event-trace command to display trace messages. Use the monitor event-trace component dump command to save trace message information for a single event. By default, trace information is saved in binary format. If you want to save trace messages in ASCII format, possibly for additional application processing, use the monitor event-trace component dump pretty command. To write the trace messages for all events currently enabled on a networking device to a file, enter the monitor event-trace dumpcommand. To configure the file where you want to save trace information, use the monitor event-trace command in global configuration mode. The trace messages are saved in a binary format.

**Example:**

The following example shows the privileged EXEC commands to stop event tracing, clear the current contents of memory, and reenable the trace function for the interprocess communication (IPC) component. This example assumes that the tracing function is configured and enabled on the networking device.

```text
Router# monitor event-trace ipc disable
Router# monitor event-trace ipc clear
Router# monitor event-trace ipc enable
```

The following example shows how the monitor event-trace one-shotcommand accomplishes the same function as the previous example except in one command. In this example, once the size of the trace message file has been exceeded, the trace is terminated.

```text
Router# monitor event-trace ipc one-shot
```

The following example shows the command for writing trace messages for an event in binary format. In this example, the trace messages for the IPC component are written to a file.

```text
Router# monitor event-trace ipc dump
```

The following example shows the command for writing trace messages for an event in ASCII format. In this example, the trace messages for the MBUS component are written to a file.

```text
Router# monitor event-trace mbus dump pretty
```

Catalyst 6500 Series Switches and Cisco 7600 Series Routers Examples Only This example shows how to stop event tracing, clear the current contents of memory, and reenable the trace function for the SPA component. This example assumes that the tracing function is configured and enabled on the networking device.

```text
Router# monitor event-trace spa disable
monitor event-trace spa clear
Router# monitor event-trace spa enable
```


### `monitor event-trace (global)`

> **Página:** 347 · **Modo:** Global configuration (config) · **Default:** Event tracing is enabled or disabled depending on the software component. · **Leitura (show/clear/…):** não

**Description:** To configure event tracing for a specified Cisco IOS software subsystem component, use the monitor event-trace command in global configuration mode. Cisco 10000 Series Routers

**Syntax:**

```text
monitor event-trace component {disable | dump-file filename | enable | size number | stacktrace
number} timestamps [datetime [localtime] [msec] [show-timezone] | uptime]
monitor event-trace component {disable | dump-file filename | enable | clear | continuous | one-shot}
```

**Parameters (Syntax Description):**

- `c o m p one n t` — Name of the Cisco IOS software subsys t e m c o m p one n t that is the object of the event
- `c o m p one n t` — Name of the Cisco IOS software subsys t e m c o m p one n t that is the o b j e c to f the event trace. To get a list of c o m p one n t s that support event t r a c in g, use the monitor event-trace? command.
- `disable` — T u r n s of f event t r a c in g for the specified c o m p one n t.
- `dump-file file name` — Specifies the file where event trace message s are w r it t e n from memory on the network in g device. The maximum length of the file name( path and file name) is100 characters, and the path can p o in t to flash memory on then e two r k in g device or to a TFTPor FTP server.
- `enable` — T u r n s one v e n t t r a c in g for the specified c o m p one n t p r o v id e d that the c o m p one n t has been configure d using the monitor event-trace command.
- `size number` — Set s then u m be r of message s that can be w r it t e n to memory for as in g l e in s t an c e of atrace. V a l id values are from1 to65536. Note Some Cisco IOS software subsys t e m c o m p one n t s set the size by default. To d is p l a y the size parameter, use the showmon it or event-trace c o m p one n t parameters command. When then u m be r of event trace message s in memory e x c e e d s the configure d size, n e w message s will begin to overwrite the o l d e r message s in the file.
- `stacktrace number` — Enable s the stacktrace at trace p o in t s and specifies the d e p t h of the stacktrace s to r e d. V a l id values are from1 to16.
- `timestamps` — ( Optional) Include s time s t a m p information with the event trace message s for the specified c o m p one n t.
- `d at e time` — ( Optional) Specifies that the time s t a m p information include d with event trace message s will c on s is to f the d at e and time of the event trace.
- `l o c a l time` — ( Optional) Specifies that the time g i v e n in the time s t a m p will be l o c a l time.
- `msec` — ( Optional) Include s m i l l is e c on d s in the time s t a m p.
- `show-timezone` — ( Optional) Include s time z one information in the time s t a m p.
- `uptime` — ( Optional) D is p l a y s time s t a m p e d information about the system u p time.
- `clear` — Clear s e x is t in gt r a c e message s for the specified c o m p one n t from memory on the network in g device.
- `c on t in u o u s` — C on t in u o u s l y d is p l a y s the l at e s t event trace e n t r i e s.
- `one-shot` — Clear s any e x is t in gt r a c e information from memory, start s event t r a c in g a g a in, and disable s the trace when the tracer each e s the size specified using the monitor event-trace command.

**Command Default:** Event tracing is enabled or disabled depending on the software component.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(18)S | This command was introduced. |
| 12.2(8)T | This command was integrated into Cisco IOS Release12.2(8) T. |
| 12.2(14)SX | This command was integrated into Cisco IOS Release12.2(14) S X and i m p l e m e n t e do n the Supervisor E n g in e720. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s routers. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.4(20)T | This command was integrated into Cisco IOS Release12.4(20) T. |

**Usage Guidelines:**

Use the monitor event-trace command to enable or disable event tracing and to configure event trace parameters for Cisco IOS software subsystem components. Note Event tracing is intended for use as a software diagnostic tool and should be configured only under the direction of a Technical Assistance Center (TAC) representative. In Cisco IOS software images that do not provide subsystem support for the event trace function, the monitor event-trace command is not available. The Cisco IOS software allows the subsystem components to define whether support for event tracing is enabled or disabled by default. The command interface for event tracing allows you to change the default two ways: using the monitor event-tracecommand in privileged EXEC mode or using the monitor event-tracecommand in global configuration mode. Additionally, default settings do not show up in the configuration file. If the subsystem software enables event tracing by default, the monitor event-tracecomponentenable command will not show up in the configuration file of the networking device; however, disabling event tracing that has been enabled by default by the subsystem will create a command entry in the configuration file. Note The amount of data collected from the trace depends on the trace message size configured using the monitor event-tracecommand for each instance of a trace. To determine whether you can enable event tracing on a subsystem, use the monitor event-trace ?commandto get a list of software components that support event tracing. To determine whether event tracing is enabled by default for the subsystem, use the show monitor event-trace command to display trace messages. To specify the trace call stack at tracepoints, you must first clear the trace buffer.

**Example:**

The following example shows how to enable event tracing for the interprocess communication (IPC) subsystem component in Cisco IOS software and configure the size to 4096 messages. The trace messages file is set to ipc-dump in slot0 (flash memory).

```text
configure terminal
!
monitor event-trace ipc enable
monitor event-trace ipc dump-file slot0:ipc-dump
monitor event-trace ipc size 4096
```

When you select Cisco Express Forwarding as the component for which to enable event tracing, you can use the following additional arguments and keywords: monitor event-trace cef [events | interface | ipv6 | ipv4][all]. The following example shows how to enable event tracing for IPv4 or IPv6 events of the Cisco Express Forwarding component in Cisco IOS software:

```text
configure terminal
!
monitor event-trace cef ipv4 enable
configure terminal
!
monitor event-trace cef ipv6 enable
exit
The following example shows what happens when you try to enable event tracing for a component
(in this case, adjacency events) when it is already enabled:
configure terminal
!
monitor event-trace adjacency enable
%EVENT_TRACE-6-ENABLE: Trace already enabled.
```


### `monitor event-trace crypto pki`

> **Página:** 350 · **Modo:** Privileged EXEC · **Default:** Starting from IOS XE 16.12.2 all event-traces are disabled by default. To enable event tracing, manually enable it using monitor event-trace crypto pki · **Leitura (show/clear/…):** não

**Description:** To monitor crypto trace information, use the, use the monitor event-trace cryptopkicommand in privileged EXEC mode.

**Syntax:**

```text
monitor event-trace crypto pki { error | event | exceptions }
no monitor event-trace crypto pki { error | event | exceptions }
```

**Parameters (Syntax Description):**

- `error` — Configure event t r a c in g for all PKI error s.
- `event` — Configure event t r a c in g for all PKI events.

**Command Default:** Starting from IOS XE 16.12.2 all event-traces are disabled by default. To enable event tracing, manually enable it using monitor event-trace crypto pki

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 16.9.1 | This command was introduced. |

**Usage Guidelines:**

Use the monitor event-trace crypto pki command to control what, when, and how event trace data is collected. Use the monitor event-trace component dump command to save trace message information for a single event. By default, trace information is saved in binary format. If you want to save trace messages in ASCII format, possibly for additional application processing, use the monitor event-trace component dump pretty command. To write the trace messages for all events currently enabled on a networking device to a file, enter the monitor event-trace dump command.

**Example:**

The following example shows how to use the monitor event-trace crypto pki command with the error keyword:

```text
Device # monitor event-trace crypto pki error
```


### `monitor event-trace crypto ipsec`

> **Página:** 351 · **Modo:** Privileged EXEC (#) · **Default:** Starting from IOS XE 16.12.2 all event-traces are disabled by default. To enable event tracing, manually enable it using monitor event-trace crypto ipsec · **Leitura (show/clear/…):** não

**Description:** To monitor crypto trace information, use the, monitor event-trace cryptoipseccommand in priviledged EXEC mode. To disable the configuration, use the no form of this command.

**Syntax:**

```text
monitor event-trace crypto ipsec { error | event | exceptions }
no monitor event-trace crypto ipsec { error | event | exceptions }
```

**Parameters (Syntax Description):**

- `Configure` — event tracing for all IPsec errors.
- `error` — Configure event t r a c in g for all IPsec error s.
- `event` — Configure event t r a c in g for all IPsec events.
- `e x c e p t i on` — Configure event t r a c in g for all IPsec e x c e p t i on s.

**Command Default:** Starting from IOS XE 16.12.2 all event-traces are disabled by default. To enable event tracing, manually enable it using monitor event-trace crypto ipsec

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.3.3M | This command was introduced. |

**Usage Guidelines:**

Use the monitor event-trace crypto ipsec command to control what, when, and how event trace data is collected. Use the monitor event-trace component dump command to save trace message information for a single event. By default, trace information is saved in binary format. If you want to save trace messages in ASCII format, possibly for additional application processing, use the monitor event-trace component dump pretty command. To write the trace messages for all events currently enabled on a networking device to a file, enter the monitor event-trace dump command.

**Example:**

The following example shows how to use the monitor event-trace crypto ipsec command with the error keyword:

```text
Device #
monitor event-trace crypto ipsec error
```


### `monitor event-trace crypto ikev2`

> **Página:** 352 · **Modo:** Privileged EXEC (#) · **Default:** Starting from IOS XE 16.12.2 all event-traces are disabled by default. To enable event tracing, manually enable it using monitor event-trace crypto ikev2 · **Leitura (show/clear/…):** não

**Description:** To monitor Internet Key Exchange Version 2 (IKEv2) trace information, use the, monitor event-trace cryptoikev2command in priviledged EXEC mode. To disable the configuration, use the no form of this command.

**Syntax:**

```text
monitor event-trace crypto ikev2 { error | event | exceptions }
no monitor event-trace crypto ikev2 { error | event | exceptions }
```

**Parameters (Syntax Description):**

- `error` — Configure event t r a c in g for all IKEv2 error s.
- `event` — Configure event t r a c in g for all IKEv2 events.
- `e x c e p t i on` — Configure event t r a c in g for all IKEv2 e x c e p t i on s.

**Command Default:** Starting from IOS XE 16.12.2 all event-traces are disabled by default. To enable event tracing, manually enable it using monitor event-trace crypto ikev2

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.3.3M | This command was introduced. |

**Usage Guidelines:**

Use the monitor event-trace crypto ikev2 command to control what, when, and how event trace data is collected. Use the monitor event-trace component dump command to save trace message information for a single event. By default, trace information is saved in binary format. If you want to save trace messages in ASCII format, possibly for additional application processing, use the monitor event-trace component dump pretty command. To write the trace messages for all events currently enabled on a networking device to a file, enter the monitor event-trace dump command.

**Example:**

The following example shows how to use the monitor event-trace crypto ikev2 command with the error keyword:

```text
Device # monitor event-trace crypto ikev2 error
```


### `monitor event-trace crypto ikev2 event`

> **Página:** 352 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To save trace messages for all event traces currently enabled on the networking device, use the monitor event-trace dump-tracescommand in privileged EXEC mode. monitor event-trace dump-traces [pretty]

**Parameters (Syntax Description):**

- `pretty` — ( Optional) Save s the event trace message in ASCII format.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(18)S | This command was introduced. |
| 12.2(8)T | This command was integrated into Cisco IOS Release12.2(8) T. |

**Usage Guidelines:**

Use the monitor event-trace dump-traces command to save trace message information for all event traces currently enabled on a networking device. By default, trace information is saved in binary format. If you want to save trace messages in ASCII format, possibly for additional application processing, use the monitor event-trace dump-traces pretty command. To write the trace messages for an individual trace event to a file, enter the monitor event-trace (EXEC) command. To configure the file where you want to save messages, use the monitor event-trace (global) command.

**Example:**

The following example shows how to save the trace messages in binary format for all event traces enabled on the networking device.

```text
monitor event-trace dump-traces
```

The following example shows how to save the trace messages in ASCII format for all event traces enabled on the networking device.

```text
monitor event-trace dump-traces pretty
```


### `monitor event-trace crypto ikev2 event dump-file`

> **Página:** 353 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To save trace messages for all event traces currently enabled on the networking device, use the monitor event-trace dump-tracescommand in privileged EXEC mode. monitor event-trace dump-traces [pretty]

**Parameters (Syntax Description):**

- `pretty` — ( Optional) Save s the event trace message in ASCII format.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(18)S | This command was introduced. |
| 12.2(8)T | This command was integrated into Cisco IOS Release12.2(8) T. |

**Usage Guidelines:**

Use the monitor event-trace dump-traces command to save trace message information for all event traces currently enabled on a networking device. By default, trace information is saved in binary format. If you want to save trace messages in ASCII format, possibly for additional application processing, use the monitor event-trace dump-traces pretty command. To write the trace messages for an individual trace event to a file, enter the monitor event-trace (EXEC) command. To configure the file where you want to save messages, use the monitor event-trace (global) command.

**Example:**

The following example shows how to save the trace messages in binary format for all event traces enabled on the networking device.

```text
monitor event-trace dump-traces
```

The following example shows how to save the trace messages in ASCII format for all event traces enabled on the networking device.

```text
monitor event-trace dump-traces pretty
```


### `monitor event-trace crypto ikev2 event size`

> **Página:** 354 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To save trace messages for all event traces currently enabled on the networking device, use the monitor event-trace dump-tracescommand in privileged EXEC mode. monitor event-trace dump-traces [pretty]

**Parameters (Syntax Description):**

- `pretty` — ( Optional) Save s the event trace message in ASCII format.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(18)S | This command was introduced. |
| 12.2(8)T | This command was integrated into Cisco IOS Release12.2(8) T. |

**Usage Guidelines:**

Use the monitor event-trace dump-traces command to save trace message information for all event traces currently enabled on a networking device. By default, trace information is saved in binary format. If you want to save trace messages in ASCII format, possibly for additional application processing, use the monitor event-trace dump-traces pretty command. To write the trace messages for an individual trace event to a file, enter the monitor event-trace (EXEC) command. To configure the file where you want to save messages, use the monitor event-trace (global) command.

**Example:**

The following example shows how to save the trace messages in binary format for all event traces enabled on the networking device.

```text
monitor event-trace dump-traces
```

The following example shows how to save the trace messages in ASCII format for all event traces enabled on the networking device.

```text
monitor event-trace dump-traces pretty
```


### `monitor event-trace crypto ikev2 event stacktrace`

> **Página:** 355 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To save trace messages for all event traces currently enabled on the networking device, use the monitor event-trace dump-tracescommand in privileged EXEC mode. monitor event-trace dump-traces [pretty]

**Parameters (Syntax Description):**

- `pretty` — ( Optional) Save s the event trace message in ASCII format.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(18)S | This command was introduced. |
| 12.2(8)T | This command was integrated into Cisco IOS Release12.2(8) T. |

**Usage Guidelines:**

Use the monitor event-trace dump-traces command to save trace message information for all event traces currently enabled on a networking device. By default, trace information is saved in binary format. If you want to save trace messages in ASCII format, possibly for additional application processing, use the monitor event-trace dump-traces pretty command. To write the trace messages for an individual trace event to a file, enter the monitor event-trace (EXEC) command. To configure the file where you want to save messages, use the monitor event-trace (global) command.

**Example:**

The following example shows how to save the trace messages in binary format for all event traces enabled on the networking device.

```text
monitor event-trace dump-traces
```

The following example shows how to save the trace messages in ASCII format for all event traces enabled on the networking device.

```text
monitor event-trace dump-traces pretty
```


### `monitor event-trace crypto pki`

> **Página:** 356 · **Modo:** Privileged EXEC (#) · **Default:** Event tracing is disabled · **Leitura (show/clear/…):** não

**Description:** To monitor PKI trace information, use the, monitor event-trace cryptopkicommand in priviledged EXEC mode. To disable the configuration, use the no form of this command.

**Syntax:**

```text
monitor event-trace crypto pki { error | event }
no monitor event-trace crypto pki { error | event }
```

**Parameters (Syntax Description):**

- `error` — Configure event t r a c in g for all PKI error s.
- `event` — Configure event t r a c in g for all PKI events.

**Command Default:** Event tracing is disabled

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXE16.9.1 | This command was introduced. |

**Usage Guidelines:**

Use the monitor event-trace crypto pki command to control what, when, and how event trace data is collected. Use the monitor event-trace component dump command to save trace message information for a single event. By default, trace information is saved in binary format. If you want to save trace messages in ASCII format, possibly for additional application processing, use the monitor event-trace component dump pretty command. To write the trace messages for all events currently enabled on a networking device to a file, enter the monitor event-trace dump command.

**Example:**

The following example shows how to use the monitor event-trace crypto pki command with the error keyword:

```text
Device # monitor event-trace crypto pki error
```


### `monitor event-trace dump-traces`

> **Página:** 357 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To save trace messages for all event traces currently enabled on the networking device, use the monitor event-trace dump-tracescommand in privileged EXEC mode.

**Syntax:**

```text
monitor event-trace dump-traces [pretty]
```

**Parameters (Syntax Description):**

- `pretty` — ( Optional) Save s the event trace message in ASCII format.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(18)S | This command was introduced. |
| 12.2(8)T | This command was integrated into Cisco IOS Release12.2(8) T. |

**Usage Guidelines:**

Use the monitor event-trace dump-traces command to save trace message information for all event traces currently enabled on a networking device. By default, trace information is saved in binary format. If you want to save trace messages in ASCII format, possibly for additional application processing, use the monitor event-trace dump-traces pretty command. To write the trace messages for an individual trace event to a file, enter the monitor event-trace (EXEC) command. To configure the file where you want to save messages, use the monitor event-trace (global) command.

**Example:**

The following example shows how to save the trace messages in binary format for all event traces enabled on the networking device.

```text
monitor event-trace dump-traces
```

The following example shows how to save the trace messages in ASCII format for all event traces enabled on the networking device.

```text
monitor event-trace dump-traces pretty
```


### `monitor pcm-tracer capture-destination`

> **Página:** 358 · **Modo:** Global configuration (config) · **Default:** The PCM trace information is saved to the NVRAM. · **Leitura (show/clear/…):** não

**Description:** To configure a location to save the Pulse Code Modulation (PCM) trace information, use the monitor pcm-tracer capture-destination command in global configuration mode. To disable the configuration, use the no form of this command.

**Syntax:**

```text
monitor pcm-tracer capture-destination destination
no monitor pcm-tracer capture-destination
```

**Parameters (Syntax Description):**

- `destination` — Destination to save the PCM trace information. You can specify any of the following values: • archive:--Save s trace to archive. • flash:--Save s trace to flash memory. • ftp:--Save s trace to an FTP network server. • http:--Save s trace to an HTTPs e r v e r. • https:--Save s trace to as e c u r e HTTP( HTTPS) server. • n u l l:--Save s trace to filesystem. • nvram:--Save s trace to the NVRAM of the router. • p r a m:--Save s trace to the p e r m an e n t R A M( P R A M) of the router. • rcp:--Save s trace to are m o t e copy p r o to c o l( RCP) network server. • scp:--Save s trace to an e two r k server that support s Secure Shell (SSH). • syslog:--Save s trace to the system log. • system:--Save s trace to the system memory. • tftp:--Save s trace to a TFTP network server. • t m p s y s:--Save s trace to at e m p or a r y system location.

**Command Default:** The PCM trace information is saved to the NVRAM.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |

**Usage Guidelines:**

You can use the monitor pcm-tracer capture-destination command to specify a location to save the PCM trace information. When Cisco IOS software saves the data to network file systems, such as TFTP and FTP, it assumes the location is valid and has write access. After the PCM capture is complete, the router automatically copies the captured contents to the specified location. The filename format at the destination location is as follows:

```text
<Configured name>_tx_<DS0 slot>_<DS0 unit>_<DS0 channel>--For TX
<Configured name>_rx_<DS0 slot>_<DS0 unit>_<DS0 channel>--For RX
```

You can identify the dial feature card (DFC) channel from where the PCM is traced using the filename format. Consider the following example:

```text
Router(config)# monitor pcm-tracer capture-destination tftp:
://223.255.254.254/benzeer/cap/cap_data
```

In this example, two files are created for the data corresponding to each DS0s, one for each direction (transmitter and receiver). When the debug pcmtracer command is enabled, the trace data is copied into the following files: • cap_data_tx_6_1_22 and cap_data_rx_6_1_22--This corresponds to the traffic flowing through DS0 6/1:22. • cap_data_tx_6_1_22 and cap_data_rx_6_1_22--cap_data_tx_6_1_22 is the data in the transmit direction (from the DFC to the system backplane) and cap_data_rx_6_1_22 is the data in the receiver direction (to the DFC from the system backplane).

**Example:**

The following example shows how to configure a router to save the PCM trace information to a flash drive:

```text
Router# configure terminal
Router(config)# monitor pcm-tracer capture-destination flash:
```


### `monitor pcm-tracer delayed-start`

> **Página:** 360 · **Modo:** Global configuration (config) · **Default:** The default delay time is zero. · **Leitura (show/clear/…):** não

**Description:** To configure the delay time to start the Pulse Code Modulation (PCM) trace capture, use the monitor pcm-tracer delayed-start command in global configuration mode. To disable the configuration, use the no form of this command.

**Syntax:**

```text
monitor pcm-tracer delayed-start seconds
no monitor pcm-tracer delayed-start
```

**Parameters (Syntax Description):**

- `seconds` — Delay, in s e c on d s. The range is from1 to2147483.

**Command Default:** The default delay time is zero.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |

**Example:**

The following example shows how to configure the PCM tracer delay time to 1000 seconds:

```text
configure terminal
Router(config)#
monitor pcm-tracer delayed-start 1000
```


### `monitor pcm-tracer profile`

> **Página:** 361 · **Modo:** Global configuration (config) · **Default:** PCM capture profiles are disabled. · **Leitura (show/clear/…):** não

**Description:** To create Pulse Code Modulation (PCM) capture profiles, use the monitor pcm-tracer profile command in global configuration mode. To disable the configuration, use the no form of this command.

**Syntax:**

```text
monitor pcm-tracer profile profile-number { {no}capture-tdm {[T1 | E1] | {analog-voice-port |
bri-voice-port}port | ds0 | channel-numnumber}}
no monitor pcm-tracer profile profile-number
```

**Parameters (Syntax Description):**

- `Profile` — number. The range is from 1 to 10.
- `profile-number` — Profile number. The range is from1 to10.
- `capture-tdm` — ( Optional) Setup d s0 dump s on specified ports
- `T1` — ( Optional) Specifies a d s0 dump on a T1 v o i c e port.
- `E1` — ( Optional) Specifies a d s0 dump on a E1 v o i c e port.
- `analog-voice-port` — ( Optional) Specifies a d s0 dump on an an a log v o i c e port.
- `bri-voice-port` — ( Optional) Specifies a d s0 dump on a B R I v o i c e port.
- `port` — ( Optional) The s p e c if i c portname.
- `ds0` — ( Optional) Specifies a d s0 dump.
- `channel-num` — ( Optional) Specifies a c h an n e l number for the dump.
- `number` — ( Optional) S p e c if i c number of the c h an n e l.

**Command Default:** PCM capture profiles are disabled.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |

**Usage Guidelines:**

You must create at least one user profile under the channels that need to be traced. You can create the following profile operations: • Create a user profile identified by a profile number. • Add one or more profiles. A user profile consists of capture groups in which the channels that are to be traced are specified. • Configure one or more capture groups under a profile.

**Example:**

The following example shows how to create a PCM capture profile with profile number 1:

```text
Router# configure terminal
Router(config)# monitor pcm-tracer profile 1
```


### `monitor permit-list`

> **Página:** 362 · **Modo:** Global configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To configure a destination port permit list or add to an existing destination port permit list, use the monitor permit-list command in global configuration mode. To delete from or clear an existing destination port permit list, use the no form of this command. Activate monitoring Activate monitoring on one port Activate monitoring on one range of ports Activate monitoring on two or more ranges of ports

**Syntax:**

```text
monitor permit-list
no monitor permit-list
monitor permit-list destination interface interface-type slot/port
no monitor permit-list destination interface interface-type slot/port
monitor permit-list destination interface interface-type slot/port-last-port
no monitor permit-list destination interface interface-type slot/port-last-port
monitor permit-list destination interface interface-type slot/port-last-port , [port-last-port]
no monitor permit-list destination interface interface-type slot/port-last-port , [port-last-port]
```

**Parameters (Syntax Description):**

- `destination` — Specifies a destination port.
- `interface interface-type` — Specifies the interface type; v a l id values are e the r n e t, fast e the r n e t, g i g a b it e the r n e t, or t e n g i g a b it e the r n e t
- `slot` — The slot that the interface module is install e d in.
- `port` — Specifies as in g l e port on an interface module, or the first port on an interface module used in a range of ports.
- `last-port` — ( Optional) Specifies the port on an interface module used as the last port in a range of ports.
- `,` — ( Optional) S e p a r at e s each in s t an c e of ap or t, or range of ports, that are monitor e d. Seethe Usage Guidelines and the Examples form or e information.

**Command Default:** Disabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SXE | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

To prevent accidental configuration of ports as destinations, you can create a permit list of the ports that are valid for use as destinations. With a destination port permit list configured, you can only configure the ports in the permit list as destinations. When you enter multiple instances of interface interface-type slot/port-fastport, you must enter a space before and after the comma. For example, interface interface-type slot/port-fastport , interface-type slot/port-fastport , interface-type slot/port-fastport.

**Example:**

This example shows how to configure a destination port permit list that includes Gigabit Ethernet ports 5/1 through 5/4, and activate monitoring:

```text
Router# configure terminal
Router(config)# monitor permit-list destination interface gigabitethernet 5/1-4
Router(config)# monitor permit-list
```

This example shows how to configure a destination port permit list that includes Fast Ethernet ports 1/1-48, 2/1-48, and Gigabit Ethernet ports 3/1 through 3/4, and activate monitoring:

```text
Router# configure terminal
Router(config)# monitor permit-list destination interface fastEthernet 1/1-48 , fastEthernet
2/1-48 , gigabitEthernet 3/1-4
Router(config)# monitor permit-list
```


### `monitor session egress replication-mode`

> **Página:** 363 · **Modo:** Global configuration (config) · **Default:** Cisco IOS Releases 12.2(33)SXH2a and later releases: Centralized mode Cisco IOS Releases 12.2(33)SXH, SXH1, and SXH2: Distributed mode · **Leitura (show/clear/…):** não

**Description:** To switch the egress-span mode from the default mode (either centralized or distributed depending on your Cisco IOS software release), use the monitor session egress replication-modecommand in global configuration mode. To return to the default mode, use the no form of the command. Cisco IOS Release 12.2(33)SXH2a and Later Releases Cisco IOS Release 12.2(33)SXH, SXH1, and SXH2

**Syntax:**

```text
monitor session egress replication-mode centralized
no monitor session egress replication-mode centralized
monitor session egress replication-mode distributed
no monitor session egress replication-mode distributed
```

**Parameters (Syntax Description):**

- `c e n t r a l i z e d` — In Cisco IOS Release12.2(33) S X H2 a and l at e r releases: Specifies c e n t r a l i z e d egress span monitor in g as the default mode.
- `d is t r i but e d` — In Cisco IOS Release12.2(33) S X H, S X H1, and S X H2: Specifies d is t r i but e d egress span monitor in g as the default mode.

**Command Default:** Cisco IOS Releases 12.2(33)SXH2a and later releases: Centralized mode Cisco IOS Releases 12.2(33)SXH, SXH1, and SXH2: Distributed mode

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SXH | This command was introduced. |
| 12.2(33)SXH2a | The command was changed as f o l low s: • The default mode was changed from d is t r i but e d mode to c e n t r a l i z e d mode. • The c e n t r a l i z e d keyword was removed and the d is t r i but e d keyword was added. |

**Usage Guidelines:**

Note Prior to Cisco IOS Release 12.2(33)SXH and the introduction of this feature, the operating mode was centralized and could not be changed. Centralized egress span monitoring redirects traffic to the supervisor engine for egress monitoring. Distributed egress span monitoring is performed in the ingress module. Distributed replication for Switched Port Analyzer (SPAN), Remote SPAN (RSPAN), and Encapsulated RSPAN (ERSPAN) increases the total throughput at the span destination. Note Distributed egress span (DES) mode is applied to ASIC-based sessions only.

**Example:**

Cisco IOS Release 12.2(33)SXH, SXH1, and SXH2 The following example shows how to switch the egress-span mode from the distributed default to centralized mode:

```text
Router(config)# monitor session egress replication-mode centralized
```

The following example shows how to switch the egress-span mode from centralized back to distributed mode:

```text
Router(config)# no monitor session egress replication-mode centralized
```

Cisco IOS Release 12.2(33)SXH2a and Later Releases The following example shows how to switch the egress-span mode from the centralized default to distributed mode:

```text
Router(config)# monitor session egress replication-mode distributed
```

The following example shows how to switch the egress-span mode from distributed back to centralized mode:

```text
Router(config)# no monitor session egress replication-mode distributed
```


### `monitor session type`

> **Página:** 365 · **Modo:** Global configuration (config) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** não

**Description:** To configure a local Switched Port Analyzer (SPAN), RSPAN, or ERSPAN, use the monitor session typecommand in global configuration mode. To remove one or more source or destination interfaces from the SPAN session, use the no form of this command.

**Syntax:**

```text
monitor session span-session-number type {erspan-destination | erspan-source | local | local-tx |
rspan-destination | rspan-source}
no monitor session span-session-number type {erspan-destination | erspan-source | local | local-tx |
rspan-destination | rspan-source}
```

**Parameters (Syntax Description):**

- `span-session-number` — Number of the l o c a l SPANor E R SPAN session; v a l id values are from1 to66.
- `erspan-destination` — Specifies the E R SPAN destination-session configuration mode.
- `erspan-source` — Specifies the E R SPAN source-session configuration mode.
- `local` — Specifies the l o c a l SPAN session configuration mode.
- `local-tx` — Specifies the l o c a l egress-only SPAN session configuration mode.
- `rspan-destination` — Specifies the R SPAN destination-session configuration mode.
- `rspan-source` — Specifies the R SPAN source-session configuration mode.
- `Global Configuration Mode` — Enters ERSPANor R SPAN destination session configuration mode and c h an g e s the prompt to the following: Router( config-m on-e r span-d s t)# Router( config-m on-r span-d s t)#
- `monitor session e r span-destination-session-number | r span-destination-session-number type e r span-destination| e r span-destination`
- `Destination Session Configuration Mode` — ( Optional) Describe s the ERSPANor R SPAN destination session.
- `description session-description`
- `shutdown` — ( Optional)( Default) In activate s the E R SPAN destination session.
- `no shutdown` — Activate s the E R SPAN destination session.
- `destination {single-interface|interface-list| interface-range|mixed-interface-list}` — As s o c i at e s the E R SPAN destination session number with the destination ports.
- `source` — Enters E R SPAN destination sessions our c e configuration mode and c h an g e s the prompt to the following: Router( config-m on-e r span-d s t-s r c)#
- `Destination Session Source Configuration Mode` — Configure s the E R SPAN f low destination IP address, which must also be configure do n an interface on the destination switch and been t e r e d in the E R SPAN destination session configuration.
- `ipaddress ip-address[force]`
- `erspan-id erspan-flow-id` — Configure s the ID number used by the destination and destination sessions to id e n t if y the E R SPAN traffic.
- `vrf vrf-name` — ( Optional) Configure s the VRF name of the p a c k e t s in the E R SPAN traffic.
- `Global` — Configuration Mode
- `monitor` — session e r span-destination-session-number | rspan-destination-session-number type
- `erspan-destination` — | erspan-destination
- `Destination` — Session Configuration Mode
- `description` — session-description ( Optional) Describe s the ERSPAN or RSPAN destination session.
- `shutdown` — ( Optional) ( Default) In activate s the ERSPAN destination session.
- `no` — shutdown Activate s the ERSPAN destination session.
- `destination` — { single-interface | interface-list | As s o c i at e s the ERSPAN destination session number with the destination
- `interface-range` — | mixed-interface-list } ports.
- `source` — Enters ERSPAN destination session source configuration mode and changes
- `Destination` — Session Source Configuration Mode
- `ip` — address ip-address [force]
- `erspan-id` — e r span-f low-id Configure s the ID number used by the destination and destination sessions
- `vrf` — vrf-name ( Optional) Configure s the VRF name of the packets in the ERSPAN traffic. The table below lists the ERSPAN source session configuration mode syntax e s.
- `Global Configuration Mode` — Enters ERSPANor R SPAN source session configuration mode and c h an g e s the prompt as ap p r o p r i at e to the following: Router( config-m on-e r span-s r c)# Router( config-m on-r span-s r c)#
- `monitor session e r span-source-session-number type e r span-source| r span-source`
- `Source Session Configuration Mode` — ( Optional) Describe s the ERSPANor R SPAN source session.
- `description session-description`
- `shutdown` — ( Optional)( Default) In activate s the ERSPANor R SPAN source session.
- `no shutdown` — Activate s the ERSPANor R SPAN source session.
- `source {{single-interface|interface-list| interface-range|mixed-interface-list|single-vlan| vlan-list|vlan-range|mixed-vlan-list}[rx|tx| both]}` — As s o c i at e s the ERSPANor R SPAN source session number with the source portsor VLAN s, and s e l e c t s the traffic dir e c t i onto be monitor e d.
- `filter {single-vlan|vlan-list|vlan-range| mixed-vlan-list}` — ( Optional) Configure s source VLAN f i l t e r in g when the ERSPANor RSPAN source is at r u n k port.
- `description session-description` — ( Optional) Describe s the ERSPANor R SPAN source session.
- `Source Session Destination Configuration Mode` — Configure s the ERSPANor R SPAN f low destination IP address, which must also be configure do n an interface on the destination switch and been t e r e d inthe ERSPANor R SPAN destination session configuration.
- `ipaddress ip-address`
- `erspan-id erspan-flow-id` — Configure s the ID number used by the source and destination sessions to id e n t if y the ERSPANor R SPAN traffic.
- `or i g in ip address ip-address` — Configure s the IP address used as the source of the ERSPANor RSPAN traffic.
- `ip {{ttlttl-value}|{precipp-value}| {dscpdscp-value}}` — ( Optional) Configure s the following p a c k e t values in the ERSPANor RSPAN traffic: •ttl ttl -value--IP time-to-l i v e( T T L) value •prec ip p-value--IP-p r e c e d e n c e value •dscp d scp-value--IP-p r e c e d e n c e value
- `vrf vrf-name` — ( Optional) Configure s the VRF name of the p a c k e t s in the ERSPANor R SPAN traffic.
- `Global` — Configuration Mode
- `monitor` — session e r span-source-session-number type
- `erspan-source` — | rspan-source
- `Source` — Session Configuration Mode
- `description` — session-description ( Optional) Describe s the ERSPAN or RSPAN source session.
- `shutdown` — ( Optional) ( Default) In activate s the ERSPAN or RSPAN source session.
- `no` — shutdown Activate s the ERSPAN or RSPAN source session.
- `source` — {{ single-interface | interface-list | As s o c i at e s the ERSPAN or RSPAN source session number with the source
- `interface-range` — | m i x e d-interface-list | single-vlan | ports or VLANs, and selects the traffic dir e c t i on to be monitor e d.
- `vlan-list` — | vlan-range | mixed-vlan-list } [rx | tx | both]}
- `filter` — { single-vlan | vlan-list | vlan-range | ( Optional) Configure s source VLAN f i l t e r in g when the ERSPAN or RSPAN
- `mixed-vlan-list` — } source is a trunk port.
- `description` — session-description ( Optional) Describe s the ERSPAN or RSPAN source session.
- `Source` — Session Destination Configuration Mode
- `ip` — address ip-address
- `erspan-id` — e r span-f low-id Configure s the ID number used by the source and destination sessions to
- `origin` — ip address ip-address Configure s the IP address used as the source of the ERSPAN or RSPAN
- `ip` — {{ t t l t t l-value } | { p r e c ip p-value } | ( Optional) Configure s the following packet values in the ERSPAN or RSPAN {dscpdscp-value }} traffic:
- `vrf` — vrf-name ( Optional) Configure s the VRF name of the packets in the ERSPAN or
- `When` — you configure the monitor sessions, follow these syntax guidelines: • e r span-destination-span-session-number can range from 1 to 66. • single-interface is interface type slot /port ; type is fast e the r n e t, g i g a b it e the r n e t, or t e n g i g a b it e the r n e t. • interface-list is single-interface , single-interface , single-interface ... Note In lists, you must enter a space before and after the comma. In ranges, you must enter a space before and after the dash. • interface-range is interface type slot / first-port - last-port . • mixed-interface-list is, in any order, single-interface , interface-range , ... • e r span-f low-id can range from 1 to 1023.
- `When` — you clear the monitor sessions, follow these syntax guidelines: • The no monitor sessions e s s i on-number command entered with no other parameters clears the session
- `session-number` — . • session-range is first-session-number -last-session-number. Note When you enter the no monitor session range command, do not enter spaces before or after the dash. If you
- `enter` — m u l t ip l e ranges, do not enter spaces before or after the commas.
- `Use` — the monitor session type local command to configure ingress, egress, or both ingress and egress SPAN sessions.
- `Use` — the monitor session type l o c a l-t x command to configure egress-only SPAN sessions.
- `When` — you enter the local or the local egress-only SPAN session configuration mode, the prompt changes
- `a c c or d in g l y` — to Router( config-m on-l o c a l)# or Router( config-m on-l o c a l-t x)#, and the following commands are a v a i l a b l e: • description -- Describe s the p r o p e r t i e s for this session using this syntax:
- `description` — description The description can be up to 240 characters and cannot contain special characters or spaces. • destination -- Specifies the destination and the destination p r o p e r t i e s using this syntax:
- `destination` — an a l y s is-module num an o m a l y-detect or-module num interface type number
- `intrusion-detection-module` — num
- `analysis-module num` — Specifies the SPAN destination an a l y s is-module.
- `anomaly-detector-module num` — Specifies the SPAN destination an o m a l y-detect or-module.
- `interface type number` — Specifies the interface type and number as f o l low s: • G i g a b it E the r n e t m o d/ port • port-c h an n e l n u m--E the r n e t C h an n e l of interfaces; v a l id values are from1 to496.
- `ingress` — ( Optional) Configure s destination s to r e c e i v e traffic from attach e d devices.
- `l e a r n in g` — ( Optional) Enable s MAC address l e a r n in g from the destination s, which all o w s the switch to t r an s m it traffic that is address e d to device s attach e d to the destination s.
- `intrusion-detection-module num` — Specifies the SPAN destination in t r u s i on-detect i on-module. • exit -- Exits from configuration session mode. • filter vlan vlan-id -- Limits the SPAN source traffic to s p e c if i c VLANs; valid values are from 1 to 4096. • no -- Negates a command or sets its default s. • shutdown -- Shuts down this session • source -- Specifies the SPAN source interface or VLAN using the following syntax:
- `cpurp` — As s o c i at e s the l o c a l SPAN session number with the CPU on the route processor.
- `cpusp` — As s o c i at e s the l o c a l SPAN session number with the CPU on the switch processor.
- `interface type number` — Specifies the interface type and number as f o l low s: •Fast E the r n e t m o d/ port • G i g a b it E the r n e t m o d/ port • Port-c h an n e l n u m--E the r n e t C h an n e l of interfaces; v a l id values are from1 to496.
- `vlanvlan-id` — Specifies the VLAN; v a l id values are from1 to4094.
- `,` — ( Optional) Specifies an other range of interfaces.
- `-` — ( Optional) Specifies a range of interfaces.
- `both` — ( Optional) Monitor s the r e c e i v e d and the t r an s m it t e d traffic.
- `rx` — ( Optional) Monitor s the r e c e i v e d traffic only.
- `tx When you enter the l o c a l-t x keyword, the r x and both keywords are not a v a i l a b l e and the t x keyword isr e q u i r e d.` — ( Optional) Monitor s the t r an s m it t e d traffic only. The local SPAN session limits are as follows: • Total sessions--80 • Source sessions--2 ( in g r e s s or egress or both) • Egress only--14
- `If` — you enter the filter keyword on a monitor e d trunk interface, only traffic on the set of specified VLANs is monitor e d.
- `Only` — one destination per SPAN session is supported. If you attempt to add another destination interface to a
- `session` — that already has a destination interface configure d, you get an error. You must first remove a SPAN
- `destination` — interface before c h an g in g the SPAN destination to a d if f e r e n t interface.
- `You` — can configure up to 64 SPAN destination interfaces, but you can have one egress SPAN source interface
- `and` — up to 128 ingress source interfaces only.
- `A` — SPAN session can either monitor VLANs or monitor in d i v id u a l interfaces, but it cannot monitor both
- `s p e c if i c` — interfaces and s p e c if i c VLANs. Config u r in g a SPAN session with a source interface and then trying
- `to` — add a source VLAN to the same SPAN session causes an error. Config u r in g a SPAN session with a source
- `VLAN` — and then trying to add a source interface to that session also causes an error. You must first clear any
- `sources` — for a SPAN session before switch in g to another type of source.
- `Port` — channel interfaces display in the list of interface options if you have them configure d. VLAN interfaces
- `are` — not supported. However, you can span a p a r t i c u l a r VLAN by enter in g the monitor session session source
- `vlan` — vlan-id command.
- `When` — you configure the destination, use these guidelines: • A single-interface is as follows: • interface type slot/ port; type is fast e the r n e t, g i g a b it e the r n e t, or t e n g i g a b it e the r n e t. • interface port-c h an n e l number Note Destination port channel interfaces must be configure d with the c h an n e l-group group-n u m mode on command
- `and` — the no c h an n e l-p r o to c o l command. • An interface-list is single-interface, single-interface , single-interface ... Note In lists, you must enter a space before and after the comma. In ranges, you must enter a space before and after the dash. • An interface-range is interface type slot / first-port - last-port. • A mixed-interface-list is, in any order, single-interface , interface-range , ... • A single-vlan is the ID number of a single VLAN. • A single-list is single-vlan , single-vlan , single-vlan ... • A vlan-range is first-vlan-ID - last-vlan-ID. • A mixed-vlan-list is, in any order, single-vlan , vlan-range , ...
- `When` — you clear the monitor sessions, follow these syntax guidelines: • The no monitor sessions e s s i on-number command entered with no other parameters clears the session
- `session-number` — . • session-range is first-session-number -last-session-number. Note When you enter the no monitor session range command, do not enter spaces before or after the dash. If you
- `enter` — m u l t ip l e ranges, do not enter spaces before or after the commas.

**Command Default:** This command has no default settings.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SXE | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(18)SXF | This command was changed as f o l low s: • Support for this command was introduced on the Supervisor E n g in e32. • E R SPAN is supported in any switch f a b r i c module f u n c t i on a l it y switch in g mode. |
| 12.2(33)SXH | This command was changed to include the following keywords: •local • l o c a l-t x • r span-destination • r span-source |

**Usage Guidelines:**

Release 12.2(18)SXE and later releases support ERSPAN with the Supervisor Engine 720, hardware revision 3.2 or higher. Enter the show module version | include WS-SUP720-BASE command to display the hardware revision. ERSPAN traffic is GRE-encapsulated SPAN traffic that can only be processed by an ERSPAN destination session. This command is not supported on Catalyst 6500 series switches that are configured with a Supervisor Engine 2. All ERSPAN source sessions on a switch must use the same source IP address. You enter the origin ip address command to configure the IP address for the ERSPAN source sessions. All ERSPAN destination sessions on a switch must use the same IP address. You enter the ip address command to configure the IP address for the ERSPAN destination sessions. If the ERSPAN destination IP address is not a Supervisor Engine 720 (for example, it is a network sniffer), the traffic arrives with the GRE and RSPAN headers/encapsulation intact. The ERSPAN source session destination IP address, which must be configured on an interface on the destination switch, is the source of traffic that an ERSPAN destination session sends to the destination ports. You configure the same address in both the source and destination sessions with the ip address command. The ERSPAN ID differentiates the ERSPAN traffic arriving at the same destination IP address from different ERSPAN source sessions. The local ERSPAN session limits are as follows: • Total sessions--66 • Source sessions--2 (ingress or egress or both) • Destination sessions--23 The monitor session type command creates a new ERSPAN session or allows you to enter the ERSPAN session configuration mode. ERSPAN uses separate source and destination sessions. You configure the source and destination sessions on different switches. The ERSPAN session configuration mode prompts are as follows: • Router(config-mon-erspan-src)--Indicates the ERSPAN source session configuration mode. • Router(config-mon-erspan-src-dst)--Indicates the ERSPAN source session destination configuration mode. • Router(config-mon-erspan-dst)--Indicates the ERSPAN destination session configuration mode. • Router(config-mon-erspan-dst-src)--Indicates the ERSPAN destination session source configuration mode The table below lists the ERSPAN destination session configuration mode syntaxes.

**Example:**

This example shows how to configure an ERSPAN source session number and enter the ERSPAN source session configuration mode for the session:

```text
Router(config)#
monitor session 55 type erspan-source
Router(config-mon-erspan-src)#
```

This example shows how to configure an ERSPAN destination session number and enter the ERSPAN destination session configuration mode for the session:

```text
Router(config)# monitor session 55 type erspan-destination
Router(config-mon-erspan-dst)#
```

This example shows how to associate the ERSPAN destination session number with the destination ports:

```text
Router(config-mon-erspan-dst) destination interface fastethernet 1/2 , 2/3
```

This example shows how to enter the ERSPAN destination session source configuration:

```text
Router(config-mon-erspan-dst)#
source
Router(config-mon-erspan-dst-src)#
```

This example shows how to enter the ERSPAN destination session source configuration mode:

```text
Router(config-mon-erspan-dst)# source
Router(config-mon-erspan-dst-src)#
```

This example shows how to configure multiple sources for a session:

```text
Router(config-mon-erspan-src)# source interface fastethernet 5/15 , 7/3 rx
Router(config-mon-erspan-src)# source interface gigabitethernet 1/2 tx
Router(config-mon-erspan-src)# source interface port-channel 102
Router(config-mon-erspan-src)# source filter vlan 2 - 3
Router(config-mon-erspan-src)#
```

This example shows how to enter the ERSPAN source session destination configuration mode:

```text
Router(config-mon-erspan-src)# destination
Router(config-mon-erspan-src-dst)#
```

This example shows how to configure the ID number that is used by the source and destination sessions to identify the ERSPAN traffic:

```text
Router(config-mon-erspan-src-dst)# erspan-id 1005
Router(config-mon-erspan-src-dst)#
```

This example shows how to configure session 1 to monitor ingress traffic from Gigabit Ethernet port 1/1 and configure Gigabit Ethernet port 1/2 as the destination:

```text
Router(config)#
monitor session 1 type local
Router(config-mon-local)#
source interface gigabitethernet 1/1 rx
Router(config-mon-local)# destination interface gigabitethernet 1/2
```

This example shows how to configure session 1 to monitor egress-only traffic from Gigabit Ethernet port 5/1 and configure Gigabit Ethernet port 5/2 as the destination:

```text
Router(config)# monitor session 1 type local-tx
Router(config-mon-local)# source interface gigabitethernet 5/1 rx
Router(config-mon-local)# destination interface gigabitethernet 5/2
```

This example shows how to remove an interface from a session:

```text
Router(config)# no monitor session 1 type local-tx
```


### `mop device-code`

> **Página:** 373 · **Modo:** Global configuration · **Default:** Cisco device code · **Leitura (show/clear/…):** não

**Description:** To identify the type of device sending Maintenance Operation Protocol (MOP) System Identification (sysid) messages and request program messages, use the mop device-code command in global configuration mode. To set the identity to the default value, use the no form of this command.

**Syntax:**

```text
mop device-code commandmop device-code {cisco | ds200}
no mop device-code {cisco | ds200}
```

**Parameters (Syntax Description):**

- `cisco` — Denotes a Cisco device code. This is the default.
- `cisco` — D e note s a Cisco device code. This is the default.
- `ds200` — D e note s a D E C server200 device code.

**Command Default:** Cisco device code

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The sysid messages and request program messages use the identity information indicated by this command.

**Example:**

The following example identifies a DECserver 200 device as sending MOP sysid and request program messages:

```text
mop device-code ds200
```


### `mop retransmit-timer`

> **Página:** 374 · **Modo:** Global configuration · **Default:** 4 seconds · **Leitura (show/clear/…):** não

**Description:** To configure the length of time that the Cisco IOS software waits before resending boot requests to a Maintenance Operation Protocol (MOP) server, use the mop retransmit-timer command in global configuration mode. To reinstate the default value, use the no form of this command.

**Syntax:**

```text
mop retransmit-timer seconds
no mop retransmit-timer
```

**Parameters (Syntax Description):**

- `seconds` — Set s the length of time( in s e c on d s) that the software wait s before r e send in g a message. The value is an u m be r from1 to20.

**Command Default:** 4 seconds

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

By default, when the software sends a request that requires a response from a MOP boot server and the server does not respond, the message is re-sent after 4 seconds. If the MOP boot server and router are separated by a slow serial link, it might take longer than 4 seconds for the software to receive a response to its message. Therefore, you might want to configure the software to wait longer than 4 seconds before resending the message if you are using such a link.

**Example:**

In the following example, if the MOP boot server does not respond within 10 seconds after the router sends a message, the server will resend the message:

```text
mop retransmit-timer 10
```


### `mop retries`

> **Página:** 375 · **Modo:** Global configuration · **Default:** 8 times · **Leitura (show/clear/…):** não

**Description:** To configure the number of times the Cisco IOS software will resend boot requests to a Maintenance Operation Protocol (MOP) server, use the mop retries command in global configuration mode. To reinstate the default value, use the no form of this command.

**Syntax:**

```text
mop retries count
no mop retries
```

**Parameters (Syntax Description):**

- `count` — In d i c at e s then u m be r of time s the software will r e send a MOP boot request. The value is an u m be r from3 to24. The default is8.

**Command Default:** 8 times

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

In the following example, the software will attempt to resend a message to an unresponsive host 11 times before declaring a failure:

```text
Router(config)# mop retries 11
```


### `more`

> **Página:** 376 · **Modo:** Privileged EXEC (#) · **Default:** The command displays the content of a file in its native format. Optional formats include ascii, binary, compressed, and ebcdic. · **Leitura (show/clear/…):** não

**Description:** To display the contents of a file, use the more command in privileged EXEC mode.

**Syntax:**

```text
more [/ascii | /binary | /compressed | /ebcdic] url
```

**Parameters (Syntax Description):**

- `/ascii` — ( Optional) D is p l a y s a b in a r y file in ASCII format.
- `/binary` — ( Optional) D is p l a y s a file in h e x/ text format.
- `/ compress e d` — ( Optional) D is p l a y s a compress e d file in r e a d a b l e format.
- `/ebcdic` — ( Optional) D is p l a y s a b in a r y file in E B CD I C format.
- `url` — The URL of the file to d is p l a y. A URL in the C L I c on s is t s of a file-system pref i x( such as system: or nvram:), an optional path( such as a f o l d e r name), and then a m e of a file.

**Command Default:** The command displays the content of a file in its native format. Optional formats include ascii, binary, compressed, and ebcdic.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOS11.3AA | This command was introduced. |
| CiscoIOS12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXE2.5 | This command was integrated into Cisco IOS X E Release2.5 on AS R1000 s e r i e s devices. |
| CiscoIOSXE3.13S | This command was modified. The/ compress e d keyword was added. |

**Usage Guidelines:**

The more system:running-config command displays the same output as the show running-config command. The more nvram:startup-config command is recommended as a replacement for the show startup-config command and the show configuration command. You can use the following commands to display configuration files: • The more nvram:startup-config command displays the startup configuration file that is contained in NVRAM or specified by the CONFIG_FILE environment variable. The Cisco IOS software informs you whether the displayed configuration is a complete configuration or a distilled version. A distilled configuration is one that does not contain access lists. • The more system:running-config command displays the running configuration. These commands show the version number of the software used when you last changed the configuration file. You can also display the contents of files on remote systems using the more command. For example, you could display a saved running configuration file on an FTP server using more ftp://username:password@ftp-host1/mydirectory/7200-basic-running-config. See the description of the copy command for more information on file-system prefixes available in the Cisco IOS CLI. Options for filtering and redirecting the output of this command are available by appending a pipe character (|). See the Related Commands table for a list of more <url> command extensions.

**Example:**

The following partial sample output displays the configuration file named startup-config in NVRAM:

```text
more nvram:startup-config
!
! No configuration change since last restart
! NVRAM config last updated at 02:03:26 PDT Thu Oct 2 1997
!
version 12.1
service timestamps debug uptime
service timestamps log uptime
service password-encryption
service udp-small-servers
service tcp-small-servers
end
```

The following is partial sample output from the more nvram:startup-config command when the configuration file has been compressed:

```text
more nvram:startup-config
Using 21542 out of 65536 bytes, uncompressed size = 142085 bytes
!
version 12.1
service compress-config
!
hostname rose
!
```

The following partial sample output displays the running configuration:

```text
Router2#
more system:running-config
Building configuration...
Current configuration:
!
version 12.1
no service udp-small-servers
no service tcp-small-servers
!
hostname Router2
!
!
end
```


### `more url begin`

> **Página:** 378 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** specify.

**Syntax:**

```text
To search the output of any morecommand, use the more url | begin command in EXEC mode. This command
begins unfiltered output of the more command with the first line that contains the regular expression you
{more url | begin regular-expression}
```

**Parameters (Syntax Description):**

- `url` — The U n i v e r s a l Resource L o c at or( R L l) of the file to d is p l a y. More commands are a d v an c e d show commands; for detail s, see the command r e f e r e n c e p age in this b o o k for the more command.
- `|` — A v e r t i c a l b a r( the“ p ip e” s y m b o l) in d i c at e s that an output process in g s p e c if i c at i on follows.
- `regular-expression` — Any r e g u l are x p r e s s i on f o u n d in more command output.
- `/` — Specifies as e a r c h at a--More--prompt that begin s u n f i l t e r e do u t p u t with the first line that c on t a in s the r e g u l are x p r e s s i on.
- `-` — Specifies a f i l t e r at a--More--prompt that only d is p l a y s output lines that do not c on t a in the r e g u l are x p r e s s i on.
- `+` — Specifies a f i l t e r at a--More--prompt that only d is p l a y s output lines that c on t a in the r e g u l are x p r e s s i on.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | The more command was introduced. |
| 12.0(1)T | This e x t e n s i on of the more command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The regular-expression argument is case sensitive and allows for complex matching requirements. You can specify a new search at every --More-- prompt. To search the remaining output of the more command, use the following command at the --More-- prompt: / regular-expression To filter the remaining output of the more command, use one of the following commands at the --More-- prompt: - regular-expression + regular-expression When output volume is large, the search can produce long lists of output. To interrupt the output, press Ctrl-^ (Ctrl-Shift-6) or Ctrl-Z. Note Once you specify a filter for a more command, you cannot specify another filter at a --More-- prompt. The first specified filter remains until the more command output finishes or until you interrupt the output. The use of the keyword begin does not constitute a filter. Because prior output is not saved, you cannot search or filter backward through prior output.

**Example:**

The following is partial sample output of the more nvram:startup-config | begincommand that begins unfiltered output with the first line that contain the regular expression “ip.” At the --More-- prompt, the user specifies a filter to exclude output lines that contain the regular expression “ip.”

```text
router# more nvram:startup-config | begin ip
ip subnet-zero
ip domain-name cisco.com
ip name-server 198.92.30.32
ip name-server 171.69.2.132
!
isdn switch-type primary-5ess
interface Ethernet1
ip address 5.5.5.99 255.255.255.0
--More--
-ip
filtering...
media-type 10BaseT
!
interface Serial0:23
encapsulation frame-relay
no keepalive
dialer string 4001
dialer-group 1
isdn switch-type primary-5ess
no fair-queue
```


### `more url exclude`

> **Página:** 380 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To filter morecommand output so that it excludes lines that contain a particular regular expression, use the more exclude command in EXEC mode.

**Syntax:**

```text
{more url | exclude regular-expression}
```

**Parameters (Syntax Description):**

- `url` — The U n i v e r s a l Resource L o c at or( URL) of the file to d is p l a y. More commands are a d v an c e d show commands; for detail s, see the command r e f e r e n c e p age in this b o o k for the more command. The Cisco IOSFile System( IF S) uses URL s to specify the location of a filesystem, directory, and file. Typical URL e l e m e n t s include: pref i x:[ directory/] file name Pref i x e scan be l o c a l filesystem s or file location s, such as nvram: or system:. A l t e r n at i v e l y, you can specify network location s using the following syntax: ftp:[[//[ username[: password]@] location]/ directory]/ file name tftp:[[// location]/ directory]/ file name rcp:[[//[ username@] location]/ directory]/ file name
- `|` — A v e r t i c a l b a r( the“ p ip e” s y m b o l) in d i c at e s that an output process in g s p e c if i c at i on follows.
- `regular-expression` — Any r e g u l are x p r e s s i on f o u n d in more command output.
- `/` — Specifies as e a r c h at a--More--prompt that begin s u n f i l t e r e do u t p u t with the first line that c on t a in s the r e g u l are x p r e s s i on.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | The more command was introduced. |
| 12.0(1)T | This e x t e n s i on of the more command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The regular-expression argument is case sensitive and allows for complex matching requirements. You can specify a new search at any --More-- prompt. To search the remaining output of the more command, use the following command at the --More-- prompt: / regular-expression When output volume is large, the search can produce long lists of output. To interrupt the output, press Ctrl-^ (Ctrl-Shift-6) or Ctrl-Z. Because prior output is not saved, you cannot search or filter backward through prior output.

**Example:**

The following is partial sample output of the more nvram:startup-config | excludecommand. The use of | exclude service in the command specifies a filter that excludes lines that contain the regular expression “service.” At the --More-- prompt, the user searches for the regular expression “Dialer1,” which continues filtered output with the first line that contains “Dialer1.”

```text
router# more nvram:startup-config | exclude service
!
version 12.0
!
hostname router
!
boot system flash
no logging buffered
!
ip subnet-zero
ip domain-name cisco.com
--More--
/Dialer1
filtering...
interface Dialer1
no ip address
no ip directed-broadcast
dialer in-band
no cdp enable
```


### `more url include`

> **Página:** 382 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To filter morecommand output so that it displays only lines that contain a particular regular expression, use the more include command in EXEC mode.

**Syntax:**

```text
{more url | include regular-expression}
```

**Parameters (Syntax Description):**

- `url` — The U n i v e r s a l Resource L o c at or( URL) of the file to d is p l a y. More commands are a d v an c e d show commands; for detail s, see the command r e f e r e n c e p age in this b o o k for the more command.
- `|` — A v e r t i c a l b a r( the“ p ip e” s y m b o l) in d i c at e s that an output process in g s p e c if i c at i on follows.
- `regular-expression` — Any r e g u l are x p r e s s i on f o u n d in more command output.
- `/` — Specifies as e a r c h at a--More--prompt that begin s u n f i l t e r e do u t p u t with the first line that c on t a in s the r e g u l are x p r e s s i on.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | The more command was introduced. |
| 12.0(1)T | This e x t e n s i on of the more command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The regular-expression argument is case sensitive and allows for complex matching requirements. You can specify a new search at any --More-- prompt. To search the remaining output of the more command, use the following syntax at the --More-- prompt: / regular-expression When output volume is large, the search can produce long lists of output. To interrupt the output, press Ctrl-^ (Ctrl-Shift-6) or Ctrl-Z. Because prior output is not saved, you cannot search or filter backward through prior output.

**Example:**

The following is partial sample output of the more nvram:startup-config | includecommand. It only displays lines that contain the regular expression “ip.”

```text
router#
more nvram:startup-config | include ip
ip subnet-zero
ip domain-name cisco.com
ip name-server 198.92.30.32
ip name-server 171.69.2.132
description ip address 172.21.53.199 255.255.255.0
ip address 172.21.53.199 255.255.255.0
```


### `more flh:logfile`

> **Página:** 383 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To view the system console output generated during the Flash load helper operation, use the more flh:logfile privileged EXEC command.

**Syntax:**

```text
more flh:logfile
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If you are a remote Telnet user performing the Flash upgrade without a console connection, this command allows you to retrieve console output when your Telnet connection has terminated due to the switch to the ROM image. The output indicates what happened during the download, and is particularly useful if the download fails. This command is a form of the more command. See the more command for more information.

**Example:**

The following is sample output from the more flh:logfilecommand:

```text
more flh:logfile
%FLH: abc/igs-kf.914 from 172.16.1.111 to flash...
System flash directory:
File
Length Name/status
1 2251320
abc/igs-kf.914
[2251384 bytes used, 1942920 available, 4194304 total]
Accessing file 'abc/igs-kf.914' on 172.16.1.111...
Loading from 172.16.13.111:
Erasing device...... erased
Loading from 172.16.13.111:
- [OK -
2251320/4194304 bytes]
Verifying checksum... OK (0x97FA)
Flash copy took 79292 msecs
%FLH: Re-booting system after download
Loading abc/igs-kf.914 at 0x3000040, size = 2251320 bytes [OK]
F3: 2183364+67924+259584 at 0x3000060
Restricted Rights Legend
Use, duplication, or disclosure by the Government is
subject to restrictions as set forth in subparagraph
(c) of the Commercial Computer Software - Restricted
Rights clause at FAR sec. 52.227-19 and subparagraph
(c) (1) (ii) of the Rights in Technical Data and Computer
Software clause at DFARS sec. 252.227-7013.
cisco Systems, Inc.
170 West Tasman Drive
San Jose, California 95134
Cisco Internetwork Operating System Software
Cisco IOS (tm) GS Software (GS7), Version 11.0
Copyright (c) 1986-1995 by cisco Systems, Inc.
Compiled Tue 06-Dec-94 14:01 by smith
Image text-base: 0x00001000, data-base: 0x005A9C94
cisco 2500 (68030) processor (revision 0x00) with 4092K/2048K bytes of
memory.
Processor board serial number 00000000
DDN X.25 software, Version 2.0, NET2 and BFE compliant.
ISDN software, Version 1.0.
Bridging software.
Enterprise software set supported. (0x0)
1 Ethernet/IEEE 802.3 interface.
2 Serial network interfaces.
--More--
1 ISDN Basic Rate interface.
32K bytes of non-volatile configuration memory.
4096K bytes of processor board System flash (Read ONLY)
```


### `motd-banner`

> **Página:** 385 · **Modo:** Line configuration · **Default:** Enabled on all lines. · **Leitura (show/clear/…):** não

**Description:** To enable the display of message-of-the-day (MOTD) banners on the specified line or lines, use the

**Syntax:**

```text
motd-banner command in line configuration mode. To suppress the MOTD banners on the specified line or
lines, use the no form of this command.
motd-banner
no motd-banner
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Enabled on all lines.

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command determines whether the router will display the MOTD banner when an EXEC session is created on the specified line or lines. The MOTD banner is defined with the banner motd global configuration command. By default, the MOTD banner is enabled on all lines. Disable the MOTD banner on specific lines using the no motd-banner line configuration command. The MOTD banners can also be disabled by the no exec-banner line configuration command, which disables both MOTD banners and EXEC banners on a line. If the no exec-banner command is configured on a line, the MOTD banner will be disabled regardless of whether the motd-bannercommand is enabled or disabled. The table below summarizes the effects of the exec-banner command and the motd-banner command.

|  | exec-banner(default) | noexec-banner |
| --- | --- | --- |
| motd-banner(default) | MOTDbanner EXECbanner | None |
| nomotd-banner | EXECbanner | None |

For reverse Telnet connections, the EXEC banner is never displayed. Instead, the incoming banner is displayed. The MOTD banner is displayed by default, but it is disabled if either the no exec-banner command or no motd-banner command is configured. The table below summarizes the effects of the exec-banner command and the motd-banner command for reverse Telnet connections.

|  | exec-banner(default) | noexec-banner |
| --- | --- | --- |
| motd-banner(default) | MOTDbanner Incomingbanner | Incomingbanner |
| nomotd-banner | Incomingbanner | Incomingbanner |

**Example:**

The following example suppresses the MOTD banner on vty lines 0 through 4:

```text
line vty 0 4
no motd-banner
```


### `name-connection`

> **Página:** 386 · **Modo:** User EXEC · **Default:** No logical name is defined. · **Leitura (show/clear/…):** não

**Description:** To assign a logical name to a connection, use the name-connectioncommand in user EXEC mode.

**Syntax:**

```text
name-connection
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** No logical name is defined.

**Command Modes:** User EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command can be useful for keeping track of multiple connections. You are prompted for the connection number and name to assign. The where command displays a list of the assigned logical connection names.

**Example:**

The following example assigns the logical name blueto the connection:

```text
Router> where
Conn Host Address Byte Idle Conn Name
* 1 doc-2509 172.30.162.131 0 0 doc-2509
Router>
name-connection
Connection number:
Enter logical name:
blue
Connection 1 to doc-2509 will be named "BLUE" [confirm]
```


### `nmsp enable`

> **Página:** 387 · **Modo:** Global configuration (config) · **Default:** NMSP features are not enabled. · **Leitura (show/clear/…):** não

**Description:** To enable Network Mobility Service Protocol (NMSP) features on the device, use the nmsp enable command in global configuration mode. To disable, use the no form of this command.

**Syntax:**

```text
nmsp enable
no nmsp enable
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** NMSP features are not enabled.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.2(2)E | This command was introduced. |

**Usage Guidelines:**

Configuring the nmsp enable command enables NMSP features on the switch. However, configuring the nmsp stong-cipher command before enabling the NMSP features ensures that all NMSP connections use strong ciphers.

**Example:**

The following example shows how to enable NMSP features:

```text
Device> enable
Device> configure terminal
Device(config)# nmsp enable
```


### `nmsp strong-cipher`

> **Página:** 388 · **Modo:** Global configuration (config) · **Default:** The new ciphers are not enabled. · **Leitura (show/clear/…):** não

**Description:** To enable the new ciphers, use the nmsp strong-cipher command in global configuration mode. To disable, use the no form of this command.

**Syntax:**

```text
nmsp strong-cipher
no nmsp strong-cipher
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** The new ciphers are not enabled.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.2(2)E | This command was introduced. |

**Usage Guidelines:**

The nmsp strong-cipher command enables strong ciphers for new Network Mobility Service Protocol (NMSP) connections. Note The existing NMSP connections will use the default cipher.

**Example:**

The following example shows how to enable a strong-cipher for NMSP:

```text
Device> enable
Device> configure terminal
Device(config)# nmsp strong-cipher
```


### `no menu`

> **Página:** 388 · **Modo:** Global configuration · **Default:** No default behavior or values. · **Leitura (show/clear/…):** não

**Description:** To delete a user menu from the configuration file, use the no menu command in global configuration mode.

**Syntax:**

```text
no menu menu-name
```

**Parameters (Syntax Description):**

- `menu-name` — Name of the menu to delete from the configuration file.

**Command Default:** No default behavior or values.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to remove any menu commands for a particular menu from the configuration file. As with all global configuration commands, this command will only effect the startup configuration file when you save the running configuration using the copy running-config startup-config EXEC command.

**Example:**

The following example deletes the menu named Access1:

```text
no menu Access1
```


### `notify`

> **Página:** 389 · **Modo:** Line configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To enable terminal notification about pending output from other Telnet connections, use the notify command in line configuration mode. To disable notifications, use the noform of this command.

**Syntax:**

```text
notify
no notify
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Disabled

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command sets a line to inform a user that has multiple, concurrent Telnet connections when output is pending on a connection other than the current one.

**Example:**

In the following example, notification of pending output from connections is enabled on virtual terminal lines 0 to 4:

```text
Router(config)# line vty 0 4
Router(config-line)# notify
```


### `notify syslog`

> **Página:** 390 · **Modo:** Configuration change logger configuration (config-archive-log-config) · **Default:** Notifications are not sent to the syslog. · **Leitura (show/clear/…):** não

**Description:** To enable the sending of notifications of configuration changes to a remote system message logging (syslog), use the notify syslog command in configuration change logger configuration mode. To disable the sending of notifications of configuration changes to the syslog, use the form of this command.

**Syntax:**

```text
notify syslog [contenttype {plaintext | xml}]
no notify syslog [contenttype {plaintext | xml}]
```

**Parameters (Syntax Description):**

- `c on t e n tty p e` — ( Optional) All o w s you to c h o o s e a format for the configuration c h an g e message s that are s e n t v i as y s log.
- `p l a in text` — ( Optional) Specifies that the configuration c h an g e message s are s e n t as p l a in text.
- `xml` — ( Optional) Specifies that the configuration c h an g e message s are s e n t in XML format.

**Command Default:** Notifications are not sent to the syslog.

**Command Modes:** Configuration change logger configuration (config-archive-log-config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(4)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(27)SBC | This command was integrated into Cisco IOS Release12.2(27) S B C. |
| 12.2(33)SRA | The c on t e n tty p e p l a in text, and xml keywords were added. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Enable the notify syslog command if you use the syslog to monitor your device. Syslog monitoring prevents the need to gather configuration log information manually. When a system message contains lengthy descriptive information, the message text can sometimes exceed the syslog buffer. In releases earlier than Cisco IOS Release 12.2(33)SXF2, the overrun message is truncated to the buffer size and any additional text is lost. In Cisco IOS Release 12.2(33)SXF2 and later releases, a long message can be split into multiple messages, with truncation and continuation indicators at each section. The end of an incomplete syslog message section will be tagged with the string "**MSG XXXXX TRUNCATED**", where XXXXX is a count of overrun messages since the last system reload. The continuation of the message will begin with "**MSG XXXXX CONTINUATION #YY", where YY represents the part number. A message can be divided into a maximum of 99 parts. When truncation occurs, the following message is sent after the truncated message:

```text
%Log packet overrun, PC [hex], format: [chars]
```

**Example:**

The following example shows how to enable the device to send notifications (in XML format) to the syslog:

```text
Device#
configure terminal
!
Device(config)# archive
Device(config-archive)# log config
Device(config-archive-log-config)# notify syslog contenttype xml
Device(config-archive-log-config)# end
```


### `padding`

> **Página:** 391 · **Modo:** Line configuration · **Default:** No padding · **Leitura (show/clear/…):** não

**Description:** To set the padding on a specific output character, use the padding command in line configuration mode. To remove padding for the specified output character, use the no form of this command.

**Syntax:**

```text
padding ascii-number count
no padding ascii-number
```

**Parameters (Syntax Description):**

- `ascii-number` — A C I Id e c i m a l representation of the character.
- `count` — Number of N U L L by t e s s e n t after the specified character, u p to255 padding characters in length.

**Command Default:** No padding

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command when the attached device is an old terminal that requires padding after certain characters (such as ones that scrolled or moved the carriage). See the “ASCII Character Set and Hex Values” appendix for a list of ASCII characters.

**Example:**

In the following example, the Return (decimal character 13) is padded with 25 NULL bytes on the console line:

```text
Router(config)# line console
Router(config-line)# padding 13 25
```


### `parity`

> **Página:** 392 · **Modo:** Line configuration · **Default:** No parity. · **Leitura (show/clear/…):** não

**Description:** To define generation of a parity bit, use the parity command in line configuration mode. To specify no parity, use the no form of this command.

**Syntax:**

```text
parity {none | even | odd | space | mark}
no parity
```

**Parameters (Syntax Description):**

- `none` — No parity. This is the default.
- `even` — E v e n parity.
- `odd` — O d d parity.
- `space` — Space parity.
- `mark` — Mark parity.

**Command Default:** No parity.

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.4 | This command was modified to enable parity set t in g on Cisco AS5350and Cisco AS5400 Next Port lines. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Communication protocols provided by devices such as terminals and modems sometimes require a specific parity bit setting. Refer to the documentation for your device to determine required parity settings. If you use this command to set parity on Cisco AS5350 and Cisco AS5400 NextPort lines, do not also set parity by means of S-register settings in a modemcap. (A modemcap is a series of parameter settings that are sent to your modem to configure it to interact with a Cisco device in a specified way. Cisco IOS software defines modemcaps that have been found to properly initialize most modems so that they function properly with Cisco routers and access servers.)

**Example:**

In the following example, even parity is configured for line 34:

```text
Router(config)# line 34
Router(config-line)#
parity even
```


### `parser cache`

> **Página:** 393 · **Modo:** Global configuration (config) · **Default:** Parser cache is enabled by default. · **Leitura (show/clear/…):** não

**Description:** To reenable the Cisco software parser cache after disabling it, use the parser cache command in global configuration mode. To disable the parser cache, use the no form of this command.

**Syntax:**

```text
parser cache
no parser cache
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Parser cache is enabled by default.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.1(5)T | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

The Parser Cache feature optimizes the parsing (translation and execution) of Cisco software configuration command lines by remembering how to parse recently encountered command lines, decreasing the time required to process large configuration files. The parser cache is enabled by default. However, if you wish to disable the parser cache, you may do so using the no parser cache command in global configuration mode. To reenable the parser cache after it has been disabled, use the parser cache command. When the no parser cache is issued, the command line appears in the running configuration file. However, if the parser cache is reenabled, no command line appears in the running configuration file.

**Example:**

In the following example, the Parser Cache feature is disabled:

```text
Device(config)# no parser cache
```


### `parser command serializer`

> **Página:** 394 · **Modo:** Global configuration (config) · **Default:** Access is granted only to the user holding the lock. · **Leitura (show/clear/…):** não

**Description:** To enable configuration access only to the users holding a configuration lock and to prevent other clients from accessing the running configuration, use the parser command serializer command in global configuration mode. To disable this configuration, use the no form of this command.

**Syntax:**

```text
parser command serializer
no parser command serializer
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Access is granted only to the user holding the lock.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRE | This command was introduced. |
| 15.1(1)T | This command was include d in Cisco IOS Release15.1(1) T. |

**Usage Guidelines:**

The Parser Concurrency and Locking Improvements feature ensures that exclusive access is granted only to a requested process and prevents other users from concurrently accessing the Cisco IOS configuration. That is, it prevents simultaneous execution of two or more commands. Use the parser command serializer command to configure the Parser Concurrency and Locking Improvements feature.

**Example:**

The following example shows how to configure the Parser Concurrency and Locking Improvements feature:

```text
configure terminal
Router(config)# parser command serializer
```


### `parser config cache interface`

> **Página:** 395 · **Modo:** Global configuration (config) · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To reduce the time required for the command-line interpreter to execute commands that manage the running system configuration files, use the parser config cache interfacecommand in global configuration mode. To disable the reduced command execution time functionality, use the no form of this command.

**Syntax:**

```text
parser config cache interface
no parser config cache interface
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Disabled

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(7)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(27)SBC | This command was integrated into Cisco IOS Release12.2(27) S B C. |
| 12.2(33)SRC | This command was integrated into Cisco IOS Release12.2(33) S R C. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Enable the parser config cache interfacecommand to reduce the execution time required for running configuration management commands such as the show running-configuration, write terminal, and copy system:running-configuration commands. Information for these configuration management commands is supplied by nonvolatile generation (NVGEN) processes that query the system for configuration details. The parser config cache interfacecommand is especially useful for managing large system configurations that contain numerous interface configurations. Once enabled, the command provides faster execution of the NVGEN commands that process the running system configuration by caching interface configurations in system memory, and by retrieving only configuration information that has changed. For this reason, the device on which this command is enabled must have enough memory available to store the interface configuration. For example, if the interface configurations take up 15 KB of memory, using this command would require having an additional 15 KB of memory space available. The first time you display the configuration file, you will not see much evidence of improvement in performance because the interface cache will be filled up. However, you will notice performance improvements when you enter subsequent NVGEN-type commands such as the show running-configuration EXEC command. Each time the interface configuration is changed, the interface cache is flushed. Entering an NVGEN-type command after modifying the interface configuration will once again not show any performance improvement until the next NVGEN-type command is entered.

**Example:**

The following example shows how to enable the functionality for reducing the time required for the command-line interpreter to execute commands that manage the running system configuration files:

```text
Device(config)# parser config cache interface
```


### `parser config partition`

> **Página:** 396 · **Modo:** Global configuration (config) · **Default:** This command is enabled by default. · **Leitura (show/clear/…):** não

**Description:** To enable configuration partitioning, use the parser config partition command. To disable the partitioning of the running configuration, use the noform of thiscommand.

**Syntax:**

```text
parser config partition
no parser config partition
```

**Parameters (Syntax Description):**

- `No` — arguments or keywords.

**Command Default:** This command is enabled by default.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRB | This command was introduced as p a r to f the Configuration Partition in g f e at u r e. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

This command controls (enables or disables) the Configuration Partitioning feature. Note This command is not related to disk partitions or disk partitioning. To display the list of commands that make up the current running configuration for a specific part (“partition”) of the system’s global running configuration, use the show running-config partition command in privileged Exec mode. The Configuration Partitioning feature uses a small amount of system resources. The no parser config partition command allows you to disable this feature if the feature is not needed on your system. Note Only the no form of this command appears in configuration files. To determine if config partitioning is supported on your system and whether it is enabled, use the show running-config parser ? command.

**Example:**

The following example shows how to disable partitioning of the system running configuration:

```text
Device> enable
Device# config t
Enter configuration commands, one per line. End with CNTL/Z.
Device(config)# no parser config partition
System configured
```


### `parser maximum`

> **Página:** 398 · **Modo:** Global Configuration · **Default:** No performance maximums enabled by default. · **Leitura (show/clear/…):** não

**Description:** To specify performance maximums for CLI operations use the parser maximum command in global configuration mode. To clear any previously established maximums, us the No form of the command.

**Syntax:**

```text
parser maximum {latencylimit | utilizationlimit}
no parser maximum {latency | utilization}
```

**Parameters (Syntax Description):**

- `latency` — Specifies the maximum process l at e n c y to all o w.
- `limit` — N u m e r i c all at e n c y be t we e n20 and200.
- `u t i l i z at i on` — Specifies the maximum CPU u t i l i z at i onto all o w.
- `limit` — N u m e r i c a l CPU u t i l i z at i on be t we e n1 and100.

**Command Default:** No performance maximums enabled by default.

**Command Modes:** Global Configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 15.1(3)T | This command was introduced. |

**Usage Guidelines:**

The Parser Maximum feature provides a workaround in the event of a problem with the coding of a protocol, allowing the error to be bypassed untill it can be corrected.

**Example:**

The following example shows how to impose a latency limit of 100.

```text
Router(config)#paser maximum latency 100
```

The following example shows how to clear latency limits.

```text
Router(config)#no paser maximum latency
```


### `partition`

> **Página:** 398 · **Modo:** Global configuration · **Default:** Flash memory consists of one partition. If the partition size is not specified, partitions of equal size are created. · **Leitura (show/clear/…):** não

**Description:** To separate Flash memory into partitions on Class B file system platforms, use the command in form of this command. Cisco 1600 Series and Cisco 3600 Series Routers All Other Class B Platforms

**Syntax:**

```text
partition
global configuration mode. To undo partitioning and to restore Flash memory to one partition, use the no
partition flash-filesystem: [number-of-partitions] [partition-size]
no partition flash-filesystem:
partition flash partitions [size1 size2]
no partition flash
```

**Parameters (Syntax Description):**

- `flash-filesystem :` — One of the following Flash filesystem s, which must be f o l low e d by a c o l on(:). The Cisco1600 s e r i e scan only use the flash: keyword. • flash:--In t e r n a l Flash memory • slot0:--Flash memory card in PCM C I As l o t0 • slot1:--Flash memory card in PCM C I As l o t1
- `number-of-partitions` — ( Optional) Number of partition s in Flash memory.
- `partition-size` — ( Optional) Size of each partition. Then u m be r of partition size e n t r i esm u s t be e q u a l to then u m be r of specified partition s.
- `partition s` — Number of partition s in Flash memory. Can be1 or2.
- `size1` — ( Optional) Size of the first partition( in m e g a by t e s).
- `size2` — ( Optional) Size of these c on d partition( in m e g a by t e s).

**Command Default:** Flash memory consists of one partition. If the partition size is not specified, partitions of equal size are created.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

For the Cisco 1600 series and Cisco 3600 series routers, to undo partitioning, use the partition flash-filesystem :1 or no partition flash-filesystem : command. For other Class B platforms, use either the partition flash 1 or no partition flash command. If there are files in a partition other than the first, you must use the erase flash-filesystem:partition-numbercommand to erase the partition before reverting to a single partition. When creating two partitions, you must not truncate a file or cause a file to spill over into the second partition. Note The partition command will only create 3MB or larger partitions and may not be used if the device memory contains logging persistent files.

**Example:**

The following example creates two partitions of 4 MB each in Flash memory:

```text
Router(config)# partition flash 2 4 4
```

The following example divides the Flash memory card in slot 0 into two partitions, each 8 MB in size on a Cisco 3600 series router:

```text
Router(config)#
partition slot0: 2 8 8
```

The following example creates four partitions of equal size in the card on a Cisco 1600 series router:

```text
Router(config)# partition flash: 4
```


### `path (archive configuration)`

> **Página:** 400 · **Modo:** Archive configuration (config-archive) · **Default:** If this command is not configured, no location or filename prefix is specified for files in the Cisco configuration archive. · **Leitura (show/clear/…):** não

**Description:** To specify the location and filename prefix for the files in the Cisco configuration archive, use the path command in archive configuration mode. To disable this function, use the no form of this command.

**Syntax:**

```text
path url
no path url
```

**Parameters (Syntax Description):**

- `url` — URL( access i b l e by the Cisco filesystem) used for s a v in g archive files of the running configuration file in the Cisco configuration archive.

**Command Default:** If this command is not configured, no location or filename prefix is specified for files in the Cisco configuration archive.

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

When this command is entered, an archive file of the running configuration is saved when the archive config, write-memory, or copy running-config startup-config command is entered. URLs are commonly used to specify files or location on the World Wide Web. On Cisco devices, URLs can be used to specify the location of a file or directory on a device or a remote file server. The path command uses a URL to specify the location and filename prefix for the Cisco configuration archive. The locations or file systems that you can specify in the url argument are as follows: • If your platform has disk0--disk0:, disk1:, ftp:, pram:, rcp:, slavedisk0:, slavedisk1:, or tftp: • If your platform does not have disk0--ftp:, http:, pram:, rcp:, or tftp: The colon is required in the location format. The filename of the first archive file is the filename specified in the url argument followed by -1. The filename of the second archive file is the filename specified in the url argument followed by -2 and so on. Because some file systems are incapable of storing the date and time that a file was written, the filename of the archive file can contain the date, time, and device hostname. To include the device hostname in the archive file filename, enter the characters $h (for example, disk0:$h). To include the date and time in the archive file filename, enter the characters $t. When a configuration archive operation is attempted on a local file system, the file system is tested to determine if it is writable and if it has sufficient space to save an archive file. If the file system is read-only or if there is not enough space to save an archive file, an error message is displayed. If you specify the tftp: file server as the location with the path command, you need to create the configuration file on the TFTP file server and change the file’s privileges before the command works properly. archive config

**Example:**

The following example of the path command shows how to specify the hostname, date, and time as the filename prefix for which to save archive files of the running configuration. In this example, the time-period command is also configured to automatically save an archive file of the running configuration every 20 minutes.

```text
configure terminal
!
archive
path disk0:$h$t
time-period 20
end
```

The following is sample output from the show archive command illustrating the format of the resulting configuration archive filenames.

```text
Device# show archive
There are currently 3 archive configurations saved.
The next archive file will be named routerJan-16-01:12:23.019-4
Archive # Name
1 disk0:routerJan-16-00:12:23.019-1
2 disk0:routerJan-16-00:32:23.019-2
3 disk0:routerJan-16-00:52:23.019-3 <- Most Recent
```

Cisco Configuration Archive on the TFTP File Server The following example shows how to use the path command to specify the TFTP file server, address 10.48.71.226, as the archive configuration location and router-cfg as the configuration filename. First you create the configuration file on the TFTP server and change the file’s privileges, then you can save the configuration file to the configuration archive. The following example shows the commands to use to create the file and change the file’s privileges on the TFTP server (UNIX commands):

```text
> touch
router-cfg-1
> chmod
777 router-cfg-1
```

The following example show how to create the configuration archive, save the running configuration to the archive, and display the files in the archive:

```text
configure terminal
!
archive
path tftp://10.48.71.226/router-cfg
exit
exit
!
archive config
Device# show archive
The next archive file will be named tftp://10.48.71.226/router-cfg-2
Archive # Name
1 tftp://10.48.71.226/router-cfg-1 <- Most Recent
```

The following is sample output from the show archive command if you did not create the configuration file on the TFTP server before attempting to archive the current running configuration file:

```text
configure terminal
!
archive
path tftp://10.48.71.226/router-cfg
exit
exit
archive config
Device# show archive
The next archive file will be named tftp://10.48.71.226/router-cfg-1
Archive # Name
```


### `periodic`

> **Página:** 403 · **Modo:** Time-range configuration (config-time-range) · **Default:** No recurring time range is defined. · **Leitura (show/clear/…):** não

**Description:** To specify a recurring (weekly) time range for functions that support the time-range feature, use the periodic command in time-range configuration mode. To remove the time limitation, use the no form of this command.

**Syntax:**

```text
periodic days-of-the-week hh:mm to [days-of-the-week] hh:mm
no periodic days-of-the-week hh:mm to [days-of-the-week] hh:mm
```

**Parameters (Syntax Description):**

- `days-of-the-week` — The first o c c u r r e n c e of this argument is the starting d a y or d a y of the we e k that the as s o c i at e d timer an g e is in e f f e c t. These c on do c c u r r e n c e is the end in g d a y or d a y of the we e k the as s o c i at e d state m e n t is in e f f e c t. This argument can be any single d a y or c o m b in at i on s of days: M on d a y, T u e s d a y, We d n e s d a y, T h u r s d a y, F r ida y, S at u r d a y, and Sunday. Other p o s s i b l e values are: • d a i l y--M on d a y t h r o u g h Sunday • we e k days--M on d a y t h r o u g h Friday • we e k end--S at u r d a y and Sunday If the end in g days of the we e k are the same as the starting days of the we e k, they can be omitted.
- `hh:mm` — The first o c c u r r e n c e of this argument is the starting h our s: min u test h at the as s o c i at e d time range is in e f f e c t. These c on do c c u r r e n c e is the end in g h our s: min u test h e as s o c i at e d state m e n t is in e f f e c t. The h our s: min u t e s are e x p r e s s e d in a24-h our clock. For example,8:00 is8:00 a. m. and 20:00is8:00p. m.
- `to` — Entry of the to keyword isr e q u i r e d to c o m p l e t e the range“ from start-time to end-time.”

**Command Default:** No recurring time range is defined.

**Command Modes:** Time-range configuration (config-time-range)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(1)T | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

For Cisco IOS Release 12.2(11)T, IP and Internetwork Packet Exchange (IPX) extended access lists are the only functions that can use time ranges. For further information on using these functions, refer to the Cisco and the . IOS IP Configuration Guide Cisco IOS AppleTalk and Novell IPX Configuration Guide The periodiccommand is one way to specify when a time range is in effect. Another way is to specify an absolute time period with the absolute command. Use either of these commands after the time-range global configuration command, which specifies the name of the time range. Multiple periodicentries are allowed per time-range command. If the end days-of-the-week value is the same as the start value, they can be omitted. If a time-range command has both absolute and periodic values specified, then the periodic items are evaluated only after the absolute start time is reached, and are not further evaluated after the absolute end time is reached. Note All time specifications are taken as local time. To ensure that the time range entries take effect at the desired times, you should synchronize the system software clock using Network Time Protocol (NTP). The table below lists some typical settings for your convenience:

| Ifyouwant: | Configurethis: |
| --- | --- |
| MondaythroughFriday,8:00a.m.to6:00p.m.only | periodicweekday8:00to18:00 |
| Everydayoftheweek,from8:00a.m.to6:00p.m.only | periodicdaily8:00to18:00 |
| EveryminutefromMonday8:00a.m.toFriday8:00p.m. | periodicmonday8:00tofriday20:00 |
| Allweekend,fromSaturdaymorningthroughSundaynight | periodicweekend00:00to23:59 |
| SaturdaysandSundays,fromnoontomidnight | periodicweekend12:00to23:59 |

**Example:**

The following example configuration denies HTTP traffic on Monday through Friday from 8:00 a.m. to 6:00 p.m.:

```text
show startup-config
time-range no-http
periodic weekdays 8:00 to 18:00
!
ip access-list extended strict
deny tcp any any eq http time-range no-http
!
interface ethernet 0
ip access-group strict in
```

The following example configuration permits Telnet traffic on Mondays, Tuesdays, and Fridays from 9:00 a.m. to 5:00 p.m.:

```text
Router# show startup-config
time-range testing
periodic Monday Tuesday Friday 9:00 to 17:00
!
ip access-list extended legal
permit tcp any any eq telnet time-range testing
!
interface ethernet 0
ip access-group legal in
```


### `ping`

> **Página:** 406 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** This command has no default values. · **Leitura (show/clear/…):** não

**Description:** To diagnose basic network connectivity on AppleTalk, ATM, Connectionless Network Service (CLNS), DECnet, IP, Novell IPX, or source-route bridging (SRB) networks, use the ping command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
ping [[protocol [tag]] {host-namesystem-address}]
```

**Parameters (Syntax Description):**

- `p r o to c o l` — ( Optional) P r o to c o l keyword, e it h e r ap p l e t a l k, at m, c l n s, d e c n e t, ip x, or srb. If ap r o to c o l is not specified, a b as i c ping will be s e n t using IP(IPv4). For e x t end e do p t i on s for ping over IP, see the document at i on for the ping ip command. The ping at min t e r f a c e at m, ping ip, ping ip v6, ping s n a, and ping vrf commands are document e d s e p a r at e l y.
- `tag` — ( Optional) Specifies at age n c ap s u l at e d IP(tag IP)ping.
- `host-name` — Hostname of the system to ping. If a host-name or system-address is not specified at the command line, it will be r e q u i r e d in the ping system d i a log.
- `system-address` — Address of the system to ping. If a host-name or system-address is not specified at the command line, it will be r e q u i r e d in the ping system d i a log.

**Command Default:** This command has no default values.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.0(7)T | The ping s n a command was introduced. |
| 12.1(12c)E | The ping vrf command was introduced. |
| 12.2(2)T | Support for the IP v6 p r o to c o l was added. |
| 12.2(13)T | The at m p r o to c o l keyword was added. The following keywords were removed be cause the Apollo Domain, B any an VINES,and X N S protocols are no l on g e r supported in Cisco IOS software: •apollo •vines •xns |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(25)SG | This command was integrated into Cisco IOS Release12.2(25) S G. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| CiscoIOSXERelease2.1 | This command was introduced on Cisco AS R1000 S e r i e s Routers. |

**Usage Guidelines:**

The ping command sends an echo request packet to an address then waits for a reply. Ping output can help you evaluate path-to-host reliability, delays over the path, and whether the host can be reached or is functioning. For example, the ping clns command sends International Organization for Standardization (ISO) CLNS echo packets to test the reachability of a remote router over a connectionless Open System Interconnection (OSI) network. If you enter the ping command without any keywords or argument values, an interactive system dialog prompts you for the additional syntax appropriate to the protocol you specify. (See the “Examples” section.) To exit the interactive ping dialog before responding to all the prompts, type the escape sequence. The default escape sequence is Ctrl-^, X (Simultaneously press and release the Ctrl, Shift, and 6 keys and then press the X key). The escape sequence will vary depending on your line configuration. For example, another commonly used escape sequence is Ctrl-c. The table below describes the test characters sent by the pingfacility. ping

| Character | Description |
| --- | --- |
| ! | Eachexclamationpointindicatesreceiptofareply. |
| . | Eachperiodindicatesthatthenetworkservertimedoutwhilewaitingforareply. |
| U | Adestinationunreachableerrorprotocoldataunit(PDU)wasreceived. |
| C | Areplypacketdoesnotvalidatethereplydata,andhenceismarked"Corrupted". Note Thischaracterwillonlyappearifthe"validate"optionisselectedinthepingrequest. |
| I | Userinterruptedtest. |

| Character | Description |
| --- | --- |
| M | Adestinationunreachableerrorprotocoldataunit(PDU)wasreceived(Type3)MTUrequired butDFbitset(code4)withthe“Next-HopMTU”settoanon-zerovalue.Ifthe“Next-hopMTU“ iszerothen‘U’isprinted. |
| ? | Unknownpackettype. |
| & | Packetlifetimeexceeded. |

Note Not all protocols require hosts to support pings. For some protocols, the pings are Cisco defined and can be answered only by another Cisco router. The availability of protocol keywords depends on what protocols are enabled on your system. Issuing the ping command in user EXEC mode will generally offer fewer syntax options than issuing the ping command in privileged EXEC mode.

**Example:**

After you enter the ping command in privileged EXEC mode, the system prompts you for a protocol keyword. The default protocol is IP. If you enter a hostname or address on the same line as the ping command, the default action is taken as appropriate for the protocol type of that name or address. The following example is sample dialog from the ping command using default values. The specific dialog varies somewhat from protocol to protocol.

```text
Router# ping
Protocol [ip]:
Target IP address: 192.168.7.27
Repeat count [5]:
Datagram size [100]:
Timeout in seconds [2]:
Extended commands [n]:
Sweep range of sizes [n]:
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.7.27, timeout is 2 seconds:
!!!!!
Success rate is 100 percent, round-trip min/avg/max = 1/2/4 ms
```

The table below describes the significant fields shown in the display. ping

| Field | Description |
| --- | --- |
| Protocol[ip]: | Promptforasupportedprotocol.Default:ip. |
| TargetIPaddress: | PromptfortheIPaddressorhostnameofthedestinationnodeyouplanto ping.IfyouhavespecifiedasupportedprotocolotherthanIP,enteran appropriateaddressforthatprotocolhere.Default:none. |

| Field | Description |
| --- | --- |
| Repeatcount[5]: | Numberofpingpacketsthatwillbesenttothedestinationaddress.Default: 5. |
| Datagramsize[100]: | Sizeofthepingpacket(inbytes).Default:100bytes. |
| Timeoutinseconds[2]: | Timeoutinterval.Default:2(seconds). |
| Extendedcommands[n]: | Specifieswhetheraseriesofadditionalcommandsappears. |
| Sweeprangeofsizes[n]: | Allowsyoutovarythesizesoftheechopacketsbeingsent.Thiscapability isusefulfordeterminingtheminimumsizesofthemaximumtransmission units(MTUs)configuredonthenodesalongthepathtothedestination address.Packetfragmentationcontributingtoperformanceproblemscan thenbereduced. |
| !!!!! | Eachexclamationpoint(!)indicatesreceiptofareply.Aperiod(.)indicates thatthenetworkservertimedoutwhilewaitingforareply.Othercharacters mayappearinthepingoutputdisplay,dependingontheprotocoltype. |
| Successrateis100percent | Percentageofpacketssuccessfullyechoedbacktotherouter.Anythingless than80percentisusuallyconsideredproblematic. |
| round-tripmin/avg/max=1/2/4 ms | Round-triptraveltimeintervalsfortheprotocolechopackets,including minimum/average/maximum(inmilliseconds). |

The following example verifies connectivity to the neighboring ATM device for the ATM permanent virtual circuit (PVC) with the virtual path identifier (VPI)/virtual channel identifier (VCI) value 0/16:

```text
Router# ping
Protocol [ip]:atm
ATM Interface:atm1/0
VPI value [0]:
VCI value [1]:16
Loopback - End(0), Segment(1) [0]:1
Repeat Count [5]:
Timeout [2]:
Type escape sequence to abort.
Sending 5, 53-byte segment OAM echoes, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```

The table below describes the default ping fields shown in the display. ping

| Field | Description |
| --- | --- |
| Protocol[ip]: | Promptforasupportedprotocol.Default:ip. |

| Field | Description |
| --- | --- |
| ATMInterface: | PromptfortheATMinterface. |
| VPIvalue[0]: | Promptforthevirtualpathidentifier.Default:0. |
| VCIvalue[1]: | Promptforthevirtualchannelidentifier.Default:1. |
| Loopback-End(0),Segment(1) [0]: | Prompttospecifyendloopback,whichverifiesend-to-endPVCintegrity, orsegmentloopback,whichverifiesPVCintegritytotheneighboring ATMdevice.Default:segmentloopback. |
| RepeatCount[5]: | Numberofpingpacketsthatwillbesenttothedestinationaddress. Default:5. |
| Timeout[2]: | Timeoutinterval.Default:2(seconds). |
| !!!!! | Eachexclamationpoint(!)indicatesreceiptofareply.Aperiod(.) indicatesthatthenetworkservertimedoutwhilewaitingforareply. Othercharactersmayappearinthepingoutputdisplay,dependingon theprotocoltype. |
| Successrateis100percent | Percentageofpacketssuccessfullyechoedbacktotherouter.Anything lessthan80percentisusuallyconsideredproblematic. |
| round-tripmin/avg/max=1/1/1 ms | Round-triptraveltimeintervalsfortheprotocolechopackets,including minimum/average/maximum(inmilliseconds). |


### `ping (privileged)`

> **Página:** 410 · **Modo:** Privileged EXEC · **Default:** A ping operation is not performed. · **Leitura (show/clear/…):** sim

**Description:** To diagnose basic network connectivity on Apollo, AppleTalk, Connectionless Network Service (CLNS), DECnet, IP, Novell IPX, VINES, or XNS networks, use the pingcommand in privileged EXEC command mode. | ethernet | fastethernet | lex | loopback | multilink | null | port-channel | tunnel | vif | virtual-template |

**Syntax:**

```text
ping [hostnamesystem-address | [protocol | tag] {hostnamesystem-address}] [data [hex-data-pattern] |
df-bit | repeat [repeat-count] | size [datagram-size] | source [source-address | async | bvi | ctunnel | dialer
virtual-tokenring | xtagatm] | timeout [seconds] | validate]
```

**Parameters (Syntax Description):**

- `hostname` — ( Optional) Hostname of the system to ping.
- `system-address` — ( Optional) Address of the system to ping.
- `p r o to c o l` — ( Optional) P r o to c o l to use for the ping. V a l id values are: ap o l l o, ap p l e t a l k, c l n s, d e c n e t, e the r n e t, ip, ip v6, ip x, srb, v in e s, x n s.
- `tag` — ( Optional) Specifies at age n c ap s u l at e d IPping.
- `data` — ( Optional) Specifies the data p at t e r n.
- `hex-data-pattern` — ( Optional) H e x id e c i m a l value of the data in the range of0 to FFFF.
- `df-bit` — ( Optional) Enable s the“ do not fragment” b it in the IP h e a d e r.
- `repeat` — ( Optional) Specifies then u m be r of time s the ping should be s e n t.
- `repeat-count` — ( Optional) Integer in the range of1 to2147483647. The default is5.
- `size` — ( Optional) Size, in by t e s, of the ping data g r a m.
- `datagram-size` — ( Optional) Integer in the range of40 to18024.
- `source` — ( Optional) Device send in gt h e ping
- `source-address` — ( Optional) Address or name of the device send in gt h e ping.
- `async` — ( Optional) Async h r on o u s interface.
- `bvi` — ( Optional) Bridge-Group V i r t u a l interface.
- `ctunnel` — ( Optional) C T u n n e l interface.
- `dialer` — ( Optional) D i a l e r interface.
- `e the r n e t` — ( Optional) E the r n e t I E E E802.3 interface.
- `fast e the r n e t` — ( Optional) Fast E the r n e t I E E E802.3 interface.
- `lex` — ( Optional) L e x interface.
- `l o o p b a c k` — ( Optional) L o o p b a c k interface.
- `m u l t i link` — ( Optional) M u l t i link-group interface.
- `null` — ( Optional) N u l l interface.
- `port-channel` — ( Optional) E the r n e t c h an n e l of interfaces.
- `tunnel` — ( Optional) T u n n e l interface
- `vif` — ( Optional) P r a g m at i c General M u l t i c as t( P G M) host interface
- `virtual-template` — ( Optional) V i r t u a l Template interface.
- `virtual-tokenring` — ( Optional) V i r t u a l Token Ring.
- `xtagatm` — ( Optional) E x t end e d Tag AT Min t e r f a c e.
- `timeout` — ( Optional) Specifies the timeout interval in s e c on d s.
- `seconds` — ( Optional) Integer in the range of0 to3600. The default is2.
- `v a l ida t e` — ( Optional) V a l ida test h e r e p l y data.

**Command Default:** A ping operation is not performed.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.0 | The following keywords were added in Cisco IOS Release12.0: data, d f-b it, r e p e at, size, source, timeout, v a l ida t e. |
| 12.2(33)SRA | The e the r n e to p t i on for p r o to c o l was added in Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The ping (packet internet groper) command tests the reachability of a remote router over a connectionless Open System Interconnection (OSI) network. The command sends ISO CLNS echo packets to an address and waits for a reply. Ping output can help you evaluate path-to-host reliability, delays over the path, and whether the host can be reached or is functioning. When you type the command, you are prompted to enter options before the command executes. ping ping The characters in brackets ([]) indicate default values. When you want to use a default value, press Enter on your keyboard. If you enter a hostname or system address when you enter the ping command, the default action is taken for the protocol type of that hostname or system address. The optional data, df-bit, repeat, size, source, timeout, and validate keywords can be used to prevent extended ping command output. You can use as many of these keywords as you need, and you can use them in any order after the hostname or system-address arguments. When you enter the ethernet protocol option, you will be prompted to enter MAC address and maintenance domain in addition to the information common across protocols. To terminate a ping session before it completes, type the escape sequence (Ctrl-^ X) by simultaneously pressing and releasing the Ctrl, Shift, and 6 keys and then pressing the X key. Note Not all protocols require hosts to support pings. For some protocols, the pings are defined by Cisco and answered only by a Cisco router. The table below describes the test characters that the ping operation uses.

| Character | Description |
| --- | --- |
| ! | Receiptofareply. |
| . | Networkservertimedoutwhilewaitingforareply. |
| U | Destinationunreachableerrorprotocoldataunit(PDU)wasreceived. |
| C | Areplypacketdoesnotvalidatethereplydata,andhenceismarked"Corrupted". Note Thischaracterwillonlyappearifthe"validate"optionisselectedinthepingrequest. |
| I | Userinterruptedtest. |
| ? | Unknownpackettype. |
| & | Packetlifetimeexceeded. |

**Example:**

The following example shows a ping command and output. The precise dialog varies from protocol to protocol, but all are similar to the ping session shown here using default values.

```text
ping
Protocol [ip]:
Target IP address: 192.168.7.27
Repeat count [5]:
Datagram size [100]:
Timeout in seconds [2]:
Extended commands [n]:
Sweep range of sizes [n]:
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.7.27, timeout is 2 seconds:
!!!!
Success rate is 100 percent, round-trip min/avg/max = 1/2/4 ms
```

The following example shows how to send a ping specifying the ethernet protocol option, MAC address, and maintenance domain and using the default values for the remaining parameters:

```text
Router# ping
```

Protocol [ip]: ethernet Mac Address : aabb.cc00.0410 Maintenance Domain : DOMAIN_PROVIDER_L5_1 VLAN [0]: 2 Source MPID [1522]: Repeat Count [5]: Datagram Size [107]: Timeout in seconds [2]: Sweep range of sizes [n]: Type escape sequence to abort. Sending 5 Ethernet CFM loopback messages, timeout is 2 seconds: !!!!!

```text
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/4/8 ms.
```


### `ping ip`

> **Página:** 414 · **Modo:** Privileged Exec · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To test network connectivity on IP networks, use the ping ip command inprivileged EXEC mode.

**Syntax:**

```text
ping ip {host-nameip-address} [data [hex-data-pattern] | df-bit | repeat [repeat-count] | tos [service
value] | size [datagram-size] source {source-addresssource-interface}] [timeout seconds] [validate]
[verbose]
```

**Parameters (Syntax Description):**

- `host-name` — Hostname of the system to ping.
- `system-address` — Address of the system to ping.
- `data hex-data-pattern` — ( Optional) Specifies the data p at t e r n. Range is from0 to FFFF.
- `df-bit` — ( Optional) Enable s the“ do-not-fragment” b it in the IP h e a d e r.
- `repeat r e p e at-count` — ( Optional) Specifies then u m be r of ping s s e n t. The range is from1 to2147483647. The default is5.
- `tos service value` — ( Optional) Specifies the type of service value. The range is from1 to255.
- `size` — ( Optional) Specifies the data g r a m size. Data g r a m size is then u m be r of by t e s in each ping.
- `datagram-size` — ( Optional) Range is from40 to18024.
- `source` — ( Optional) Specifies the source address or source interface.
- `source-address` — ( Optional) IP address to use as the source in the ping p a c k e t s.
- `source-interface` — ( Optional) Name of the interface from which the ping should be s e n t, and the Interface ID( slot/ port/ number). Interface name keywords include the following: •async ( Async h r on o u s Interface) •bvi ( Bridge-Group Virtual Interface) • c t u n n e l •dialer • e the r n e t •fast E the r n e t •lex • l o o p b a c k • m u l t i link ( M u l t i link-group interface) •null • port-c h an n e l ( E the r n e t c h an n e l of interfaces) •tunnel •vif ( P G M M u l t i c as t Host interface) • v i r t u a l-template • v i r t u a l-token r in g • x t a g at m ( E x t end e d Tag AT Min t e r f a c e) The a v a i l a b i l it y of these keywords d e p end s on your system hardware.
- `timeout seconds` — ( Optional) Specifies the timeout interval in s e c on d s. The default is2 s e c on d s. Range is from0 to3600.
- `v a l ida t e` — ( Optional) V a l ida test h e r e p l y data.
- `verbose` — ( Optional) Enable s v e r b o s e output, which list s in d i v id u a l I C M P p a c k e t s, as we l l as Echo Response s.

**Command Modes:** Privileged Exec

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.0 | The data, d f-b it, r e p e at, size, source, timeout, and v a l ida t e keywords were added. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 15.2(02)S | The to s keyword was added. |

**Usage Guidelines:**

The ping command sends an echo request packet to an address, then awaits a reply. Ping output can help you evaluate path-to-host reliability, delays over the path, and whether the host can be reached or is functioning. To abnormally terminate a ping session, type the escape sequence--by default, Ctrl-^ X. You type the default by simultaneously pressing and releasing the Ctrl, Shift, and 6 keys, and then pressing the X key. The table below describes the test characters that the ping facility sends.

| Character | Description |
| --- | --- |
| ! | Eachexclamationpointindicatesreceiptofareply. |
| . | Eachperiodindicatesthatthenetworkservertimedoutwhilewaitingforareply. |
| U | Adestinationunreachableerrorprotocoldataunit(PDU)wasreceived. |
| C | Areplypacketdoesnotvalidatethereplydata,andhenceismarked"Corrupted". Note Thischaracterwillonlyappearifthe"validate"optionisselectedinthepingrequest. |
| I | Userinterruptedtest. |
| ? | Unknownpackettype. |
| & | Packetlifetimeexceeded. |

Note Not all protocols require hosts to support pings. For some protocols, the pings are Cisco-defined and are only answered by another Cisco router.

**Example:**

After you enter the ping command in privileged mode, the system prompts you for a protocol keyword.The default protocol is IP. If you enter a host name or address on the same line as the ping command, the default action is taken as appropriate for the protocol type of that name or address. The optional data, df-bit, repeat, size, source, timeout, and validate keywords can be used to avoid extended ping command output. You can use as many of these keywords as you need, and you can use them in any order after the host-name or system-address arguments. Although the precise dialog varies somewhat from protocol to protocol, all are similar to the ping session using default values shown in the following output:

```text
ping
Protocol [ip]:
Target IP address: 192.168.7.27
Repeat count [5]:
Datagram size [100]:
Timeout in seconds [2]:
Extended commands [n]:
Sweep range of sizes [n]:
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.7.27, timeout is 2 seconds:
!!!!!
Success rate is 100 percent, round-trip min/avg/max = 1/2/4 ms
```

The table below describes the default ping fields shown in the display.

| Field | Description |
| --- | --- |
| Protocol[ip]: | Promptsforasupportedprotocol.ThedefaultisIP. |
| TargetIPaddress: | PromptsfortheIPaddressorhostnameofthedestinationnodeyouplanto ping.IfyouhavespecifiedasupportedprotocolotherthanIP,enteran appropriateaddressforthatprotocolhere.Thedefaultisnone. |
| Repeatcount[5]: | Promptsforthenumberofpingpacketsthatwillbesenttothedestination address.Thedefaultis5packets. |
| Datagramsize[100]: | Promptsforthesizeofthepingpacket(inbytes).Thedefaultis100bytes. |
| Timeoutinseconds[2]: | Promptsforthetimeoutinterval.Thedefaultis2seconds. |
| Extendedcommands[n]: | Specifieswhetheraseriesofadditionalcommandsappears. |
| Sweeprangeofsizes[n]: | Allowsyoutovarythesizesoftheechopacketsbeingsent.Thiscapability isusefulfordeterminingtheminimumsizesoftheMTUsconfiguredonthe nodesalongthepathtothedestinationaddress.Packetfragmentation contributingtoperformanceproblemscanthenbereduced. |
| !!!!! | Eachexclamationpoint(!)indicatesreceiptofareply.Aperiod(.)indicates thatthenetworkservertimedoutwhilewaitingforareply.Othercharacters mayappearinthepingoutputdisplay,dependingontheprotocoltype. |
| Successrateis100percent | Indicatesthepercentageofpacketssuccessfullyechoedbacktotherouter. Anythinglessthan80percentisusuallyconsideredproblematic. |
| round-tripmin/avg/max=1/2/4 ms | Indicatestheround-triptraveltimeintervalsfortheprotocolechopackets, includingminimum/average/maximum(inmilliseconds). |


### `ping srb`

> **Página:** 417 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To test network connectivity for Source Route Bridging (SRB) networks, use the ping srb command in privileged EXEC mode.

**Syntax:**

```text
ping srb name
```

**Parameters (Syntax Description):**

- `name` — Destination IP address or hostname.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release 15.0(1)M. |
| 12.2(33)SRE | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRE. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1 and i m p l e m e n t e d onthe Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Example:**

The following example shows how to ping the target host of IP address 192.0.2.1:

```text
Router# ping srb 192.0.2.1
```


### `ping vrf`

> **Página:** 418 · **Modo:** User EXEC Privileged EXEC · **Default:** The default connection type for ping is IPv4. · **Leitura (show/clear/…):** sim

**Description:** To test a connection in the context of a specific VPN connection, use the ping vrf command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
ping vrf vrf-name [tag] [connection] target-address [connection-options]
```

**Parameters (Syntax Description):**

- `vrf-name` — Then a m e of the V P N( VRF context).
- `tag` — ( Optional) Specifies at age n c ap s u l at e d IP(tag IP)ping.
- `connection` — ( Optional) Connection options include at m, c l n s, d e c n e t, ip, ip v6, ip x, s n a, or srb. The default is ip.
- `target-address` — The destination ID for the ping o p e r at i on. U s u all y, this is the IP v4 address of the host. For example, the tar get for an IP v4 ping in a VRF context would be the IP v4 address or domain name of the tar get host. The tar get for an IP v6 ping in a VRF context would bethe IP v6 pref i x or domain name of the tar get host. • If the tar get address is not specified, the C L I will enter the in t e r a c t i v e d i a log for ping.
- `connection-options` — ( Optional) Each connection type may have its own set of connection options. For example, connection options for IP v4 are source, d f-b it, and timeout. Seethe ap p r o p r i at e ping command document at i on for detail s.

**Command Default:** The default connection type for ping is IPv4.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.1(12c)E,12.2 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |
| 12.2(33)SCF | This command was integrated into Cisco IOS Release12.2(33) S C F. |

**Usage Guidelines:**

A VPN routing and forwarding (VRF) instance is used to identify a VPN. To check if a configured VRF is working, you can use the ping vrf command. When attempting to ping from a provider edge (PE) router to a customer edge (CE) router, or from a PE router to PE router, the standard ping command will not usually work. The ping vrf command allows you to ping the IP addresses of LAN interfaces on CE routers. If you are on a PE router, be sure to indicate the specific VRF (VPN) name, as shown in the “Examples” section. If all required information is not provided at the command line, the system will enter the interactive dialog (extended mode) for ping.

**Example:**

In the following example, the target host in the domain 209.165.201.1 is pinged (using IP/ICMP) in the context of the “CustomerA” VPN connection.

```text
Router# ping vrf CustomerA 209.165.201.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 209.165.201.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 176/264/576 ms
```

Pressing the Enter key before providing all of the required options will begin the interactive dialog for ping. In the following example, the interactive dialog is started after the “ip” protocol is specified, but no address is given:

```text
ping vrf CustomerB ip
Target IP address: 209.165.200.225
Repeat count [5]:
Datagram size [100]:
Timeout in seconds [2]:
Extended commands [n]: y
Source address or interface:
Type of service [0]:
Set DF bit in IP header? [no]:
Validate reply data? [no]:
Data pattern [0xABCD]:
Loose, Strict, Record, Timestamp, Verbose[none]: Record
Number of hops [ 9 ]:
Loose, Strict, Record, Timestamp, Verbose[RV]:
Sweep range of sizes [n]:
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 209.165.200.225, timeout is 2 seconds:
Packet has IP options: Total option bytes= 39, padded length=40
Record route: <*>
(0.0.0.0)
(0.0.0.0)
(0.0.0.0)
(0.0.0.0)
(0.0.0.0)
(0.0.0.0)
(0.0.0.0)
(0.0.0.0)
(0.0.0.0)
Success rate is 100 percent (5/5), round-trip min/avg/max = 4/4/4 ms
```

The following example shows the various options for IP in the ping vrf command:

```text
show parser dump exec | include ping vrf
1 ping vrf <string>
1 ping vrf <string> ip <string>
1 ping vrf <string> ip (interactive)
1 ping vrf <string> ip <string>
1 ping vrf <string> ip <string> source <address>
1 ping vrf <string> ip <string> source <interface>
1 ping vrf <string> ip <string> repeat <1-2147483647>
1 ping vrf <string> ip <string> size Number
1 ping vrf <string> ip <string> df-bit
1 ping vrf <string> ip <string> validate
1 ping vrf <string> ip <string> data <0-65535>
1 ping vrf <string> ip <string> timeout <0-3600>
1 ping vrf <string> ip <string> verbose
1 ping vrf <string> ip <string> data <0-65535>
1 ping vrf <string> ip <string> timeout <0-3600>
1 ping vrf <string> tag
1 ping vrf <string> atm
1 ping vrf <string> ipv6
1 ping vrf <string> appletalk
1 ping vrf <string> decnet
1 ping vrf <string> clns
1 ping vrf <string> ipx
1 ping vrf <string> sna
1 ping vrf <string> srb
```

Cisco CMTS Routers: Example The following example shows how to verify the matching and marking configuration in an MPLS network:

```text
Router# ping vrf vrfa 1.3.99.98
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 1.3.99.98, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 8/10/20 ms
```


### `platform qfp drops threshold`

> **Página:** 421 · **Modo:** Global configuration (config) · **Default:** No default behaviour or values. · **Leitura (show/clear/…):** não

**Description:** To configure the warning thresholds for per drop cause and/or total QFP drop in packets per second, use the

**Syntax:**

```text
platform qfp drops threshold command.
platform qfp drops threshold { per-cause drop_id threshold_value | total threshold_value }
```

**Parameters (Syntax Description):**

- `per-cause` — Set warning threshold for p e r d r o p cause QFP drops.
- `drop-id` — QFP d r o p cause ID.
- `threshold_ value` — D r o p threshold in p a c k e t s p e r s e c on d.
- `total` — Set warning threshold for to t a l QFP drops.

**Command Default:** No default behaviour or values.

**Command Modes:** Global configuration (config)

**Usage Guidelines:**

Use the platform qfp drops threshold command to configure the warning thresholds for per drop cause and/or total QFP drop in packets per second. Example The following example shows how to configure the warning threshold of 15 pps for drop cause ID 24.

```text
Router> enable
Router# configure terminal
Router(config)#platform qfp drops threshold ?
per-cause Set warning threshold for per cause QFP drops
total Set warning threshold for total QFP drops
Router(config)#platform qfp drops threshold per-cause ?
<0-1024> QFP drop cause ID
Router(config)#platform qfp drops threshold per-cause 24 ?
<0-2147483647> Drop threshold in packets per second (pps)
Router(config)#platform qfp drops threshold per-cause 24 15
```

The following example shows how to configure the warning threshold of 100 pps for total QFP drops.

```text
Router> enable
Router# configure terminal
Router(config)#platform qfp drops threshold ?
per-cause Set warning threshold for per cause QFP drops
total Set warning threshold for total QFP drops
Router(config)#platform qfp drops threshold total ?
<0-2147483647> Drop threshold in packets per second (pps)
Router(config)#platform qfp drops threshold total 100
```


### `platform shell`

> **Página:** 422 · **Modo:** Global configuration (config) · **Default:** This command is disabled. · **Leitura (show/clear/…):** não

**Description:** To grant shell access and enter shell access grant configuration mode, use the platform shellcommand in global configuration mode. To disable this function, use the no form of this command.

**Syntax:**

```text
platform shell
no platform shell
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command is disabled.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)XNC |  |

**Usage Guidelines:**

This command should be entered before using the request platform software system shell command.

**Example:**

The following example shows how to grant shell access:

```text
Router(config)# platform shell
Router(config)#
```


### `power enable`

> **Página:** 423 · **Modo:** Global configuration · **Default:** Enabled · **Leitura (show/clear/…):** não

**Description:** To turn on power for the modules, use the power enablecommand in global configuration mode. To power down a module, use the no form of this command.

**Syntax:**

```text
power enable module slot
no power enable module slot
```

**Parameters (Syntax Description):**

- `module slot` — Specifies a module slot number; see the“ Usage Guidelines” section for v a l id values.

**Command Default:** Enabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(18)SXD | This command was changed to all o w you to disable power to e m p t y slot s. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

When you enter the no power enable module slot command to power down a module, the module’s configuration is not saved. When you enter the no power enable module slot command to power down an empty slot, the configuration is saved. The slot argument designates the module number. Valid values for slotdepend on the chassis that is used. For example, if you have a 13-slot chassis, valid values for the module number are from 1 to 13.

**Example:**

This example shows how to turn on the power for a module that was previously powered down:

```text
Router(config)#
power enable module 5
Router(config)#
```

This example shows how to power down a module:

```text
Router(config)#
no power enable module 5
Router(config)#
```


### `power redundancy-mode`

> **Página:** 424 · **Modo:** Global configuration · **Default:** redundant · **Leitura (show/clear/…):** não

**Description:** To set the power-supply redundancy mode, use the power redundancy-mode command in global configuration mode.

**Syntax:**

```text
power redundancy-mode {combined | redundant}
```

**Parameters (Syntax Description):**

- `c o m b in e d` — Specifies nor e d u n d an c y( c o m b in e power-sup p l you t p u t s).
- `r e d u n d an t` — Specifies redundancy( e it h e r power sup p l y can o p e r at e the system).

**Command Default:** redundant

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to set the power supplies to the no-redundancy mode:

```text
Router(config)#
power redundancy-mode combined
Router(config)#
```

This example shows how to set the power supplies to the redundancy mode:

```text
Router(config)#
power redundancy-mode redundant
Router(config)#
```


### `printer`

> **Página:** 425 · **Modo:** Global configuration (config) · **Default:** No printers are defined. · **Leitura (show/clear/…):** não

**Description:** To configure a printer and assign a server tty line (or lines) to it, use the printer command in global configuration mode. To disable printing on a tty line, use the no form of this command.

**Syntax:**

```text
printer printer-name {line number | rotary number} [formfeed] [jobtimeout seconds]
[newline-convert] [jobtypes type]
no printer printer-name
```

**Parameters (Syntax Description):**

- `printer-name` — Printer name.
- `printer-name` — Printer name.
- `line number` — As s i g n s at t y line to the printer. Then u m be r argument can be any one of the following parameters: • a u x--Specifies the a u x i l i a r y line. • c on s o l e--Specifies the p r i m a r y terminal line. •slot / port--First slot and port numbers for the in t e r n a l modem s. •tty number--Specifies the terminal control l e r value. • tty-number--tty number, in the range0 to491. •vty value--Specifies the v i r t u a l terminal value.
- `rotary number` — As s i g n s a r o tar y group of tty lines to the printer.
- `form f e e d` — ( Optional) Cause s the Cisco IOS software to send a form-f e e d character( ASCII 0 x0 C) to the printer tty line i m m e d i at e l y following each p r in t j o b r e c e i v e d from the network.
- `j o b timeout seconds` — ( Optional) C h an g e s the default time for line a c q u is it i on. The range is from1 to3600 seconds.
- `newline-convert` — ( Optional) C on v e r t s n e w line( line f e e d) characters to at w o-characters e q u e n c e “ c a r r i age-return, line f e e d”( C R+ L F).
- `j o b type s type` — ( Optional) Specifies all o we d j o b type s.

**Command Default:** No printers are defined.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 15.0(1)M | This command was modified in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. The j o b timeout s e c on d s and j o b type s type keywords and arguments were added. |

**Usage Guidelines:**

This command enables you to configure a printer for operations and assign either a single tty line or a group of tty lines to it. To make multiple printers available through the same printer name, specify the number of a rotary group. In addition to configuring the printer with the printer command, you must modify the file /etc/printcap on your UNIX system to include the definition of the remote printer in the Cisco IOS software. Refer to the Cisco IOS Configuration Fundamentals Configuration Guide for additional information. Use the optional newline-convert keyword in UNIX environments that cannot handle single-character line terminators. This converts newline characters to a carriage-return, linefeed sequence. Use the formfeed keyword when using the line printer daemon (lpd) protocol to print and your system is unable to separate individual output jobs with a form feed (page eject). You can enter the newline-convert and formfeed keywords together and in any order.

**Example:**

The following example shows how to configure a printer named printer1 and to assign the output to tty line 4:

```text
Router# configure terminal
Router(config)# printer printer1 line 4
```


### `private`

> **Página:** 426 · **Modo:** Line configuration · **Default:** User-set configuration options are cleared with the exit EXEC command or when the interval set with the exec-timeout line configuration command has passed. · **Leitura (show/clear/…):** não

**Description:** To save user EXEC command changes between terminal sessions, use the private command in line configuration mode. To restore the default condition, use the no form of this command.

**Syntax:**

```text
private
no private
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** User-set configuration options are cleared with the exit EXEC command or when the interval set with the exec-timeout line configuration command has passed.

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command ensures that the terminal parameters set by the user remain in effect between terminal sessions. This behavior is desirable for terminals in private offices.

**Example:**

In the following example, line 15 (in this example, vty 1) is configured to keep all user-supplied settings at system restarts:

```text
Router(config)# line 15
Router(config-line)# private
```


### `process cpu statistics limit entry-percentage`

> **Página:** 427 · **Modo:** Global configuration · **Default:** size seconds: 600 seconds · **Leitura (show/clear/…):** não

**Description:** To set the process entry limit and the size of the history table for CPU utilization statistics, use the process cpu statistics limit entry-percentage command in global configuration mode. To disable CPU utilization statistics, use the no form of this command.

**Syntax:**

```text
process cpu statistics limit entry-percentage number [size seconds]
no process cpu statistics limit entry-percentage
```

**Parameters (Syntax Description):**

- `number` — Integer from1 to100 that in d i c at e s the percentage of CPU u t i l i z at i on that ap r o c e s s must use to be c o m e p a r to f the history t a b l e.
- `size seconds` — ( Optional) C h an g e s the d u r at i on of time in s e c on d s for which CPU statistics are s to r e d in the history t a b l e. V a l id values are5 to86400. The default is600.

**Command Default:** size seconds: 600 seconds

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(26)S | This command was introduced. |
| 12.3(4)T | This command was integrated into Cisco IOS Release12.3(4) T. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |

**Usage Guidelines:**

Use the process cpu statistics limit entry-percentage command to set the entry limit and size of CPU utilization statistics.

**Example:**

The following example shows how to set an entry limit at 40 percent and a size of 300 seconds:

```text
configure terminal
!
process cpu statistics limit entry-percentage 40 size 300
end
```


### `process cpu threshold type`

> **Página:** 428 · **Modo:** Global configuration · **Default:** CPU thresholding notifications are disabled. · **Leitura (show/clear/…):** não

**Description:** To set CPU thresholding notification types and values, use the process cpu threshold type command in global configuration mode. To disable CPU thresholding notifications, use the no form of this command.

**Syntax:**

```text
process cpu threshold type {total | process | interrupt} rising percentage interval seconds [falling
fall-percentage interval seconds]
no process cpu threshold type {total | process | interrupt}
```

**Parameters (Syntax Description):**

- `total` — Setsthe CPU threshold type to to t a l CPU u t i l i z at i on.
- `process` — Setsthe CPU threshold type to CPU process u t i l i z at i on.
- `interrupt` — Setsthe CPU threshold type to CPU interrupt u t i l i z at i on.
- `rising percentage` — The percentage(1 to100) of CPU resource s that, when e x c e e d e d for the configure d interval, t r i g g e r s a CPU threshold in g not if i c at i on.
- `interval seconds` — The d u r at i on of the CPU threshold v i o l at i on, in s e c on d s(5 to86400), that must be m e t to t r i g g e r a CPU threshold in g not if i c at i on.
- `falling fall-percentage` — ( Optional) The percentage(1 to100) of CPU resource s that, when usage f all s be low this level for the configure d interval, t r i g g e r s a CPU threshold in g not if i c at i on. • This value must be e q u a l to or l e s s than the r is in g percentage value. • If not specified, the f all in g f all-percentage value is set to the same value as the r is in g percentage value.

**Command Default:** CPU thresholding notifications are disabled.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(26)S | This command was introduced. |
| 12.3(4)T | This command was integrated into Cisco IOS Release12.3(4) T. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |

**Usage Guidelines:**

This command defines CPU usage thresholds that, when crossed, cause a CPU thresholding notification. When this command is enabled, Cisco IOS software polls the system at the configured interval. Notification occurs in two situations: • When a configured CPU usage threshold is exceeded (rising percentage) • When CPU usage falls below the configured threshold (falling fall-percentage)

**Example:**

The following example shows how to set the total CPU utilization notification threshold at 80 percent for a rising threshold notification and 20 percent for a falling threshold notification, with a 5-second polling interval:

```text
configure terminal
!
process cpu threshold type total rising 80 interval 5 falling 20 interval 5
end
```


### `process-max-time`

> **Página:** 429 · **Modo:** Global configuration · **Default:** The default maximum process time is 200 milliseconds. · **Leitura (show/clear/…):** não

**Description:** To configure the amount of time after which a process should voluntarily yield to another process, use the process-max-timecommand in global configuration mode. To reset this value to the system default, use the

**Syntax:**

```text
no form of this command.
process-max-time milliseconds
no process-max-time milliseconds
```

**Parameters (Syntax Description):**

- `m i l l is e c on d s` — Maximum d u r at i on( in m i l l is e c on d s) that ap r o c e s scan r u n before s u s p e n s i on. The range is from20 to200 m i l l is e c on d s.

**Command Default:** The default maximum process time is 200 milliseconds.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.1 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Lowering the maximum time a process can run is useful in some circumstances to ensure equitable division of CPU time among different tasks. Only use this command if recommended to do so by the Cisco Technical Assistance Center (TAC).

**Example:**

The following example limits the duration that a process will run to 100 milliseconds:

```text
Router(config)# process-max-time 100
```


### `prompt`

> **Página:** 430 · **Modo:** Global configuration · **Default:** The default prompt is either Router or the name defined with the hostname global configuration command, followed by an angle bracket (>) for user EXEC mode or a pound sign (#) for privileged EXEC mode. · **Leitura (show/clear/…):** não

**Description:** To customiz e the CLI prompt, use the promptcommand in global configuration mode. To revert to the default prompt, use the noform of this command. [ ]

**Syntax:**

```text
prompt string
no prompt string
```

**Parameters (Syntax Description):**

- `string` — Text that will be d is p l a y e do n screen as the C L Ip rom p t, in c l u d in g any d e s i r e d prompt v a r i a b l e s.

**Command Default:** The default prompt is either Router or the name defined with the hostname global configuration command, followed by an angle bracket (>) for user EXEC mode or a pound sign (#) for privileged EXEC mode.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You can include customized variables when specifying the prompt. All prompt variables are preceded by a percent sign (%). The table below lists the available prompt variables.

| PromptVariable | Interpretation |
| --- | --- |
| %h | Hostname.ThisiseitherRouterorthenamedefinedwiththehostnameglobal configurationcommand. |
| %n | Physicalterminalline(tty)numberoftheEXECuser. |
| %p | Promptcharacteritself.Itiseitherananglebracket(>)foruserEXECmodeorapound sign(#)forprivilegedEXECmode. |
| %s | Space. |
| %t | Tab. |
| %% | Percentsign(%) |

Issuing the prompt %h command has the same effect as issuing the no prompt command.

**Example:**

The following example changes the EXEC prompt to include the tty number, followed by the name and a space:

```text
Router(config)# prompt TTY%n@%h%s%p
```

The following are examples of user and privileged EXEC prompts that result from the previous command:

```text
TTY17@Router1 > enable
TTY17@Router1 #
```


### `prompt config`

> **Página:** 431 · **Modo:** Global configuration (config) · **Default:** The system's prompt is not configured for configuration mode. · **Leitura (show/clear/…):** não

**Description:** To configure the system’s prompt for configuration mode, use the prompt config command in global configuration mode. To disable the configuration, use the no form of this command.

**Syntax:**

```text
prompt config hostname-length number
no prompt [config]
```

**Parameters (Syntax Description):**

- `hostname-length` — Set s the length of the hostname in the configuration prompt.
- `number` — Maximum length of the hostname. The range is from0 to80.

**Command Default:** The system's prompt is not configured for configuration mode.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. |

**Example:**

This example shows how to configure the system’s prompt for configuration mode:

```text
Router(config)#
prompt config hostname-length 4
```


### `pwd`

> **Página:** 432 · **Modo:** User EXEC Priviledged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To show the current setting of the cd command, use the pwd command in EXEC mode.

**Syntax:**

```text
pwd
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** User EXEC Priviledged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use the pwd command to show which directory or file system is specified as the default by the cd command. For all EXEC commands that have an optional filesystemargument, the system uses the file system specified by the cd command when you omit the optional filesystemargument. For example, the dir command contains an optional filesystemargument and displays a list of files on a particular file system. When you omit this filesystemargument, the system shows a list of the files on the file system specified by the cd command.

**Example:**

The following example shows that the present working file system specified by the cd command is slot 0:

```text
Router> pwd
slot0:/
```

The following example uses the cd command to change the present file system to slot 1 and then uses the pwd command to display that present working file system:

```text
Router> cd slot1:
Router> pwd
slot1:/
```
