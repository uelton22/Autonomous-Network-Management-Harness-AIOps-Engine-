# Capítulo 14: test cable-diagnostics through xmodem

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## slave auto-sync config through terminal-type

### test cable-diagnostics through xmodem

• test cable-diagnostics through xmodem, on page 1084

### test cable-diagnostics through xmodem

### `test cable-diagnostics`

> **Página:** 1108 · **Modo:** Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** não

**Description:** To test the condition of 10-Gigabit Ethernet links or copper cables on 48-port 10/100/1000 BASE-T modules, use the test cable-diagnosticscommand in privileged EXEC mode.

**Syntax:**

```text
test cable-diagnostics tdr interface type number
```

**Parameters (Syntax Description):**

- `tdr` — Activate s the T D R test for c o p p e r cable s on48-port10/100/1000 B AS E-T module s.
- `interface type` — Specifies the interface type; see the“ Usage Guidelines” section for v a l id values.
- `number` — Module and port number.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(17a)SX | Support for this command was introduced on the Cisco7600 s e r i e s routers. |
| 12.2(17b)SXA | This command was changed to p r o v id e support for the4-port10 G B AS E-E s e r i a l10-G i g a b it E the r n e t module( W S-X6704-10 G E). |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release 12.2(17d)SXB. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Cable diagnostics can help you detect whether your cable has connectivity problems. The TDR test guidelines are as follows: • TDR can test cables up to a maximum length of 115 meters. • The TDR test is supported on Cisco 7600 series routers running Release 12.2(17a)SX and later releases on specific mdoules. See the Release Notes for Cisco IOS Release 12.2SX on the Catalyst 6500 and Cisco 7600 Supervisor Engine 720, Supervisor Engine 32, and Supervisor Engine 2 for the list of the modules that support TDR. • The valid values for interface typeare fastethernet and gigabitethernet. • Do not start the test at the same time on both ends of the cable. Starting the test at both ends of the cable at the same time can lead to false test results. • Do not change the port configuration during any cable diagnostics test. This action may result in incorrect test results. • The interface must be up before running the TDR test. If the port is down, the test cable-diagnostics tdr command is rejected and the following message is displayed:

```text
Router# test cable-diagnostics tdr interface gigabitethernet2/12
% Interface Gi2/12 is administratively down
% Use 'no shutdown' to enable interface before TDR test start.
```

• If the port speed is 1000 and the link is up, do not disable the auto-MDIX feature. • For fixed 10/100 ports, before running the TDR test, disable auto-MDIX on both sides of the cable. Failure to do so can lead to misleading results. • For all other conditions, you must disable the auto-MDIX feature on both ends of the cable (use the no mdix autocommand). Failure to disable auto-MDIX will interfere with the TDR test and generate false results. • If a link partner has auto-MDIX enabled, this action will interfere with the TDR-cable diagnostics test and test results will be misleading. The workaround is to disable auto-MDIX on the link partner. • If you change the port speed from 1000 to 10/100, enter the no mdix autocommand before running the TDR test. Note that entering the speed 1000 command enables auto-MDIX regardless of whether the no mdix autocommand has been run.

**Example:**

This example shows how to run the TDR-cable diagnostics:

```text
Router #
test cable-diagnostics tdr interface gigabitethernet2/1
TDR test started on interface Gi2/1
A TDR test can take a few seconds to run on an interface
Use 'show cable-diagnostics tdr' to read the TDR results.
```


### `test flash`

> **Página:** 1109 · **Modo:** EXEC · **Default:** This command has no default values. · **Leitura (show/clear/…):** não

**Description:** To test Flash memory on MCI and envm Flash EPROM interfaces, use the test flash command in EXEC mode.

**Syntax:**

```text
test flash
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default values.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

In the following example, the Flash memory is tested:

```text
test flash
```


### `test interfaces`

> **Página:** 1110 · **Modo:** EXEC · **Default:** This command has no default values. · **Leitura (show/clear/…):** não

**Description:** To test the system interfaces on the modular router, use the test interfaces command in EXEC mode.

**Syntax:**

```text
test interfaces
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default values.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The test interfaces EXEC command is intended for the factory checkout of network interfaces. It is not intended for diagnosing problems with an operational router. The test interfaces output does not report correct results if the router is attached to a “live” network. For each network interface that has an IP address that can be tested in loopback (MCI and ciscoBus Ethernet and all serial interfaces), the test interfaces command sends a series of ICMP echoes. Error counters are examined to determine the operational status of the interface.

**Example:**

In the following example, the system interfaces are tested:

```text
test interfaces
```


### `test memory`

> **Página:** 1111 · **Modo:** Privileged EXEC · **Default:** This command overwrites memory. · **Leitura (show/clear/…):** não

**Description:** To perform a test of Multibus memory (including nonvolatile memory) on the modular router, use the test memory command in privileged EXEC mode. The memory test overwrites memory.

**Syntax:**

```text
test memory
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command overwrites memory.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The memory test overwrites memory. If you use the test memory command, you will need to rewrite nonvolatile memory. For example, if you test Multibus memory, which is the memory used by the CSC-R 4-Mbps Token Ring interfaces, you will need to reload the system before the network interfaces will operate properly. The test memory command is intended primarily for use by Cisco personnel.

**Example:**

In the following example, the memory is tested:

```text
test memory
```


### `test memory destroy`

> **Página:** 1111 · **Modo:** Privileged EXEC · **Default:** This command destroys memory chunks or dangling references on a router. · **Leitura (show/clear/…):** não

**Description:** To destroy a memory chunk or dangling reference, use the test memory destroycommand in privileged EXEC mode.

**Syntax:**

```text
test memory destroy [chunk | mgd-chunk | force-chunk | dangling-reference] chunk-id
```

**Parameters (Syntax Description):**

- `chunk` — ( Optional) Or d in a r y c h u n k of memory.
- `mgd-chunk` — ( Optional) M an age d c h u n k of memory.
- `force-chunk` — ( Optional) C h u n k of memory that is destroy e d for c e full y.
- `dangling-reference` — ( Optional) D an g l in g r e f e r e n c e of memory.
- `chunk-id` — Address of the c h u n k to be destroy e d.

**Command Default:** This command destroys memory chunks or dangling references on a router.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRC | This command was introduced. |

**Usage Guidelines:**

The force-chunk keyword destroys a chunk of ordinary (not managed) memory, even if the memory has elements or siblings that are not free. Caution Use the force-chunk keyword carefully. A crash or corruption will occur if someone refers to the destroyed chunk or its elements.

**Example:**

In the following example, a chunk of ordinary memory is destroyed:

```text
test memory destroy force-chunk
```


### `test platform police get`

> **Página:** 1112 · **Modo:** Privileged EXEC (#) · **Default:** 0 (No rate has been applied.) · **Leitura (show/clear/…):** não

**Syntax:**

```text
To get the IPv6 internal police rate, use the test platform police get command in privileged EXEC mode.
test platform police get
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** 0 (No rate has been applied.)

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRD1 | The command was introduced on the Cisco7600 s e r i e s routers for the E S+ line card s, the S IP-400, and the7600-E S+ IT U-2 T G and7600-E S+ IT U-4 T G. |

**Usage Guidelines:**

Use this command under the exec command of the line card console. It is not visible from the route processor (RP) console.

**Example:**

The following example shows how to get the IPv6 internal police rate:

```text
Router> enable
Router# test platform police get
IPv6 with HBH header is policed at 100000 kbps
```


### `test platform police set`

> **Página:** 1113 · **Modo:** Privileged EXEC (#) · **Default:** For ES40 line cards, the default police rate is 12.8 Mbps. For the SIP-400, the default police rate is 21.36 kpps. · **Leitura (show/clear/…):** não

**Description:** To set the IPv6 internal police rate, use the test platform police set command in privileged EXEC mode. This command does not have a no form.

**Syntax:**

```text
test platform police set rate
```

**Parameters (Syntax Description):**

- `rate` — Specifies the in t e r n a l police r at e. The range is from0 to100000 k b p s. •Forthe S IP-400, you can configure a r at e u p to, and in c l u d in g25600 p a c k e t s p e r s e c on d( P P S). •Forthe E S+ line card s and the7600-E S+ IT U-2 T G and7600-E S+ IT U-4 T G line card s, you can configure r at e s of: •16 K b p s to2 M b p s; g r an u l a r it y of16 k b p s •2 M b p s to100 M b p s; g r an u l a r it y of64 k b p s

**Command Default:** For ES40 line cards, the default police rate is 12.8 Mbps. For the SIP-400, the default police rate is 21.36 kpps.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRD1 | The command was introduced on the Cisco7600 s e r i e s routers for the E S+ line card s, the S IP-400, and the7600-E S+ IT U-2 T G and7600-E S+ IT U-4 T G. |

**Usage Guidelines:**

Use this command under the EXEC command of the line card console. It is not visible from the route processor (RP) console. Note There is not a no version of this command. If you have set a rate limit and wish to cancel it, you will need to use this command to set the rate to 0. For both the ES+ line cards and the SIP-400, setting the police rate to 0 turns off the policing. For both the ES+ line cards and the SIP-400, when the policer is set from the the line card console, the setting remains effective even if the line card is moved to another chassis running the Cisco IOS Release 12.2(33)SRD1 (or later) image. For the SIP-400, IPv6 HBH packets will continue to go through the QoS policing configured on the line card. For ES+ line cards, IPv6 HBH packets will bypass any QoS configured on the line card.

**Example:**

The following examples shows how to set the IPv6 with HBH header to be policed at 100000 kbps:

```text
Router> enable
Router# test platform police set 100000
```


### `tftp-server`

> **Página:** 1114 · **Modo:** Global configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To configure a router or a Flash memory device on the router as a TFTP server, use one of the following To remove a previously defined filename, use the no form of this command with the appropriate filename. Cisco 1600 Series and Cisco 3600 Series Routers Cisco 7000 Family Routers

**Syntax:**

```text
tftp-server commands in global configuration mode. This command replaces the tftp-server system command.
tftp-server flash [partition-number :] filename1 [alias filename2] [access-list-number]
tftp-server rom alias filename1 [access-list-number]
no tftp-server {flash [partition-number :] filename1 | rom alias filename2}
tftp-server flash [device :] [partition-number :] filename
no tftp-server flash [device :] [partition-number :] filename
tftp-server flash device : filename
no tftp-server flash device : filename
```

**Parameters (Syntax Description):**

- `flash` — Specifies TFTP service of a file in Flash memory.
- `rom` — Specifies TFTP service of a file in ROM.
- `file name1` — Name of a file in Flash or in ROM that the TFTP server uses in an s we r in g TFTPRead Request s.
- `alias` — Specifies an a l t e r n at e name for the file that the TFTP server uses in an s we r in g TFTP Read Request s.
- `file name2` — A l t e r n at e name of the file that the TFTP server uses in an s we r in g TFTPRead Request s. A client of the TFTP server can use this a l t e r n at e name in its Read Request s.
- `access-list-number` — ( Optional) B as i c IP access list number. V a l id values are from0 to99.
- `partition-number :` — ( Optional) Specifies TFTP service of a file in the specified partition of Flash memory. If the partition number is not specified, the file in the first partition is used. Forthe Cisco1600 s e r i e s and Cisco3600 s e r i e s routers, you must enter a c o l on after the partition number if a file name f o l low s it.
- `device :` — ( Optional) Specifies TFTP service of a file on a Flash memory device in the Cisco 1600 s e r i e s, Cisco3600 s e r i e s, and Cisco7000 f a m i l y routers. The c o l on isr e q u i r e d. V a l id device s are as f o l low s: • flash--In t e r n a l Flash memory on the Cisco1600 s e r i e s and Cisco3600 s e r i e s routers. This is the only v a l id device for the Cisco1600 s e r i e s routers. • bootflash--In t e r n a l Flash memory in the Cisco7000 f a m i l y routers. • slot0--First PCM C I As l o to n the Cisco3600 s e r i e s and Cisco7000 f a m i l y routers . • slot1--S e c on d PCM C I As l o to n the Cisco3600 s e r i e s and Cisco7000 f a m i l y. • slave bootflash--In t e r n a l Flash memory on these c on d a r y R S P card of a Cisco 7507or Cisco7513 router configure d for HSA. • slave slot0--First PCM C I As l o to f these c on d a r y R S P card on a Cisco7507 or Cisco7513 router configure d for HSA. • slave slot1--S e c on d PCM C I As l o to f these c on d a r y R S P card on a Cisco7507 or Cisco7513 router configure d for HSA.
- `file name` — Name of the file on a Flash memory device that the TFTP server uses in an s we r in g a TFTPRead Request. Use this argument only with the Cisco1600 s e r i e s, Cisco3600 s e r i e s, Cisco7000 s e r i e s, or Cisco7500 s e r i e s routers.

**Command Default:** Disabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You can specify multiple filenames by repeating the tftp-server command. The system sends a copy of the system image contained in ROM or one of the system images contained in Flash memory to any client that issues a TFTP Read Request with this filename. If the specified filename1or filename2argument exists in Flash memory, a copy of the Flash image is sent. On systems that contain a complete image in ROM, the system sends the ROM image if the specified filename1or filename2argument is not found in Flash memory. Images that run from ROM cannot be loaded over the network. Therefore, it does not make sense to use TFTP to offer the ROMs on these images. On the Cisco 7000 family routers, the system sends a copy of the file contained on one of the Flash memory devices to any client that issues a TFTP Read Request with its filename.

**Example:**

In the following example, the system uses TFTP to send a copy of the version-10.3 file located in Flash memory in response to a TFTP Read Request for that file. The requesting host is checked against access list 22.

```text
tftp-server flash version-10.3 22
```

In the following example, the system uses TFTP to send a copy of the ROM image gs3-k.101in response to a TFTP Read Request for the gs3-k.101 file:

```text
tftp-server rom alias gs3-k.101
```

In the following example, the system uses TFTP to send a copy of the version-11.0filein response to a TFTP Read Request for that file. The file is located on the Flash memory card inserted in slot 0.

```text
tftp-server flash slot0:version-11.0
```

The following example enables a Cisco 3600 series router to operate as a TFTP server. The source file c3640-i-mz is in the second partition of internal Flash memory.

```text
configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
router(config)# tftp-server flash flash:2:dirt/gate/c3640-i-mz
```

In the following example, the source file is in the second partition of the Flash memory PC card in slot 0 on a Cisco 3600 series:

```text
configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#
tftp-server flash slot0:2:dirt/gate/c3640-j-mz
```

The following example enables a Cisco 1600 series router to operate as a TFTP server. The source file c1600-i-mz is in the second partition of Flash memory:

```text
router#
configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
router(config)# tftp-server flash flash:2:dirt/gate/c1600-i-mz
```


The tftp -server system command has been replaced by the tftp-server command. See the description of the tftp-server command in this chapter for more information.

### `time-period`

> **Página:** 1117 · **Modo:** Archive configuration (config-archive) · **Default:** No time increment is set. · **Leitura (show/clear/…):** não

**Description:** To set the time increment for automatically saving an archive file of the current running configuration in the Cisco configuration archive, use the time-period command in archive configuration mode. To disable this function, use the form of this command. no

**Syntax:**

```text
time-period minutes
no time-period minutes
```

**Parameters (Syntax Description):**

- `minutes` — Specifies how of t e n, in min u t e s, to automatic all y save an archive file of the current running configuration in the Cisco configuration archive.

**Command Default:** No time increment is set.

**Command Modes:** Archive configuration (config-archive)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(7)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(31)SB2 | This command was i m p l e m e n t e do n the Cisco10000 s e r i e s router. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Note Before using this command, you must configure the path command to specify the location and filename prefix for the files in the Cisco configuration archive. If this command is configured, an archive file of the current running configuration is automatically saved after the given time specified by the minutes argument. Archive files continue to be automatically saved at this given time increment until this function is disabled. Use the maximum command to set the maximum number of archive files of the running configuration to be saved. This command saves the current running configuration to the configuration archive whether or not the running configuration has been modified since the last archive file was saved.

**Example:**

In the following example, a value of 20 minutes is set as the time increment for which to automatically save an archive file of the current running configuration in the Cisco configuration archive:

```text
Device# configure terminal
!
Device(config)# archive
Device(config-archive)# path disk0:myconfig
Device(config-archive)# time-period 20
Device(config-archive)# end
```


### `trace (privileged)`

> **Página:** 1118 · **Modo:** Privileged EXEC · **Default:** The protocol argument is based on the Cisco IOS software examination of the format of the destination argument. For example, if the software finds a destination argument in IP format, the protocol value defaults to ip. · **Leitura (show/clear/…):** não

**Description:** To discover the routes that packets will actually take when traveling to their destination, use the trace command in privileged EXEC mode.

**Syntax:**

```text
trace [protocol] [destination]
```

**Parameters (Syntax Description):**

- `p r o to c o l` — ( Optional) Protocols that can be used are ap p l e t a l k, c l n s, ip and v in e s.
- `destination` — ( Optional) Destination address or hostname on the command line. The default parameters for the ap p r o p r i at e p r o to c o l are as s u m e d and the t r a c in g a c t i on begin s.

**Command Default:** The protocol argument is based on the Cisco IOS software examination of the format of the destination argument. For example, if the software finds a destination argument in IP format, the protocol value defaults to ip.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(13)T | This command is no l on g e r supported in Cisco IOS M a in line releases or in Tech no log y-b as e d ( T-t r a in) releases. It might continue to ap p e a r in12.2 S-f a m i l y releases. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The trace command works by taking advantage of the error messages generated by routers when a datagram exceeds its time-to-live (TTL) value. The trace command starts by sending probe datagrams with a TTL value of one. This causes the first router to discard the probe datagram and send back an error message. The trace command sends several probes at each TTL level and displays the round-trip time for each. The trace command sends out one probe at a time. Each outgoing packet may result in one or two error messages. A “time exceeded” error message indicates that an intermediate router has seen and discarded the probe. A “destination unreachable” error message indicates that the destination node has received the probe and discarded it because it could not deliver the packet. If the timer goes off before a response comes in, the tracecommand prints an asterisk (*). The trace command terminates when the destination responds, when the maximum TTL is exceeded, or when the user interrupts the trace with the escape sequence. By default, to invoke the escape sequence, type Ctrl-^ X by simultaneously pressing and releasing the Ctrl, Shift, and 6 keys, and then pressing the X key. To use nondefault parameters and invoke an extended trace test, enter the command without a destination argument. You will be stepped through a dialog to select the desired parameters. Common Trace Problems Due to bugs in the IP implementation of various hosts and routers, the IP trace command may behave in unexpected ways. Not all destinations will respond correctly to a probe message by sending back an “ICMP port unreachable” message. A long sequence of TTL levels with only asterisks, terminating only when the maximum TTL has been reached, may indicate this problem. There is a known problem with the way some hosts handle an “ICMP TTL exceeded” message. Some hosts generate an “ICMP” message but they reuse the TTL of the incoming packet. Because this is zero, the ICMP packets do not make it back. When you trace the path to such a host, you may see a set of TTL values with asterisks (*). Eventually the TTL gets high enough that the ICMP message can get back. For example, if the host is six hops away, the trace command will time out on responses 6 through 11. Trace IP Routes The following display shows sample IP trace output when a destination host name has been specified:

```text
Router# trace ABA.NYC.mil
Type escape sequence to abort.
Tracing the route to ABA.NYC.mil (26.0.0.73)
1 DEBRIS.CISCO.COM (192.180.1.6) 1000 msec 8 msec 4 msec
2 BARRNET-GW.CISCO.COM (192.180.16.2) 8 msec 8 msec 8 msec
3 EXTERNAL-A-GATEWAY.STANFORD.EDU (192.42.110.225) 8 msec 4 msec 4 msec
4 BB2.SU.BARRNET.NET (192.200.254.6) 8 msec 8 msec 8 msec
5 SU.ARC.BARRNET.NET (192.200.3.8) 12 msec 12 msec 8 msec
6 MOFFETT-FLD-MB.in.MIL (192.52.195.1) 216 msec 120 msec 132 msec
7 ABA.NYC.mil (26.0.0.73) 412 msec 628 msec 664 msec
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| 1 | Indicatesthesequencenumberoftherouterinthepathtothehost. |
| DEBRIS.CISCO.COM | Hostnameofthisrouter. |
| 192.180.1.6 | Internetaddressofthisrouter. |
| 1000msec8msec4msec | Round-triptimeforeachofthethreeprobesthataresent. |

Extended IP Trace Dialog The following display shows a sample trace session involving the extended dialog of the trace command:

```text
Router# trace
Protocol [ip]:
Target IP address: mit.edu
Source address:
Numeric display [n]:
Timeout in seconds [3]:
Probe count [3]:
Minimum Time to Live [1]:
Maximum Time to Live [30]:
Port Number [33434]:
Loose, Strict, Record, Timestamp, Verbose[none]:
Type escape sequence to abort.
Tracing the route to MIT.EDU (18.72.2.1)
1 ICM-DC-2-V1.ICP.NET (192.108.209.17) 72 msec 72 msec 88 msec
2 ICM-FIX-E-H0-T3.ICP.NET (192.157.65.122) 80 msec 128 msec 80 msec
3 192.203.229.246 540 msec 88 msec 84 msec
4 T3-2.WASHINGTON-DC-CNSS58.T3.ANS.NET (140.222.58.3) 84 msec 116 msec 88 msec
5 T3-3.WASHINGTON-DC-CNSS56.T3.ANS.NET (140.222.56.4) 80 msec 132 msec 88 msec
6 T3-0.NEW-YORK-CNSS32.T3.ANS.NET (140.222.32.1) 92 msec 132 msec 88 msec
7 T3-0.HARTFORD-CNSS48.T3.ANS.NET (140.222.48.1) 88 msec 88 msec 88 msec
8 T3-0.HARTFORD-CNSS49.T3.ANS.NET (140.222.49.1) 96 msec 104 msec 96 msec
9 T3-0.ENSS134.T3.ANS.NET (140.222.134.1) 92 msec 128 msec 92 msec
10 W91-CISCO-EXTERNAL-FDDI.MIT.EDU (192.233.33.1) 92 msec 92 msec 112 msec
11 E40-RTR-FDDI.MIT.EDU (18.168.0.2) 92 msec 120 msec 96 msec
12 MIT.EDU (18.72.2.1) 96 msec 92 msec 96 msec
```

The following table describes the fields that are unique to the extended trace sequence, as shown in the display.

| Field | Description |
| --- | --- |
| TargetIPaddress | YoumustenterahostnameoranIPaddress.Thereisnodefault. |
| Sourceaddress | Oneoftheinterfaceaddressesoftheroutertouseasasourceaddressforthe probes.Therouterwillnormallypickwhatitfeelsisthebestsourceaddress touse. |

| Field | Description |
| --- | --- |
| Numericdisplay | Thedefaultistohavebothasymbolicandnumericdisplay;however,you cansuppressthesymbolicdisplay. |
| Timeoutinseconds | Thenumberofsecondstowaitforaresponsetoaprobepacket.Thedefault is3seconds. |
| Probecount | ThenumberofprobestobesentateachTTLlevel.Thedefaultcountis3. |
| MinimumTimetoLive[1] | TheTTLvalueforthefirstprobes.Thedefaultis1,butitcanbesettoa highervaluetosuppressthedisplayofknownhops. |
| MaximumTimetoLive[30] | ThelargestTTLvaluethatcanbeused.Thedefaultis30.Thetracecommand terminateswhenthedestinationisreachedorwhenthisvalueisreached. |
| PortNumber | ThedestinationportusedbytheUserDatagramProtocol(UDP)probe messages.Thedefaultis33434. |
| Loose,Strict,Record, Timestamp,Verbose | IPheaderoptions.Youcanspecifyanycombination.Thetracecommand issuespromptsfortherequiredfields.Notethatthetracecommandwillplace therequestedoptionsineachprobe;however,thereisnoguaranteethatall routers(orendnodes)willprocesstheoptions. |
| Loose | Allowsyoutospecifyalistofnodesthatmustbetraversedwhengoingto thedestination. |
| Strict | Allowsyoutospecifyalistofnodesthatmustbetheonlynodestraversed whengoingtothedestination. |
| Record | Allowsyoutospecifythenumberofhopstoleaveroomfor. |
| Timestamp | Allowsyoutospecifythenumberoftimestampstoleaveroomfor. |
| Verbose | Ifyouselectanyoption,theverbosemodeisautomaticallyselectedandthe tracecommandprintsthecontentsoftheoptionfieldinanyincomingpackets. Youcanpreventverbosemodebyselectingitagain,togglingitscurrent setting. |

The following table describes the characters that can appear in trace command output.

| Char | Description |
| --- | --- |
| nn msec | Foreachnode,theround-triptime(inmilliseconds)forthespecifiednumberofprobes. |
| * | Theprobetimedout. |
| ? | Unknownpackettype. |
| A | Administrativelyunreachable.Usually,thisoutputindicatesthatanaccesslistisblockingtraffic. |
| H | Hostunreachable. |

| Char | Description |
| --- | --- |
| N | Networkunreachable. |
| P | Protocolunreachable. |
| Q | Sourcequench. |
| U | Portunreachable. |


### `trace (user)`

> **Página:** 1122 · **Modo:** EXEC · **Default:** The protocol argument is based on the Cisco IOS software examination of the format of the destination argument. For example, if the software finds a destination argument in IP format, the protocol defaults to ip. · **Leitura (show/clear/…):** não

**Description:** To discover the IP routes that packets will actually take when traveling to their destination, use the trace command in EXEC mode.

**Syntax:**

```text
trace [protocol] [destination]
```

**Parameters (Syntax Description):**

- `p r o to c o l` — ( Optional) Protocols that can be used are ap p l e t a l k, c l n s, ip and v in e s.
- `destination` — ( Optional) Destination address or hostname on the command line. The default parameters for the ap p r o p r i at e p r o to c o l are as s u m e d and the t r a c in g a c t i on begin s.

**Command Default:** The protocol argument is based on the Cisco IOS software examination of the format of the destination argument. For example, if the software finds a destination argument in IP format, the protocol defaults to ip.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(13)T | This command is no l on g e r supported in Cisco IOS M a in line releases or in Tech no log y-b as e d ( T-t r a in) releases. It might continue to ap p e a r in12.2 S-f a m i l y releases. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The trace command works by taking advantage of the error messages generated by routers when a datagram exceeds its time-to-live (TTL) value. The trace command starts by sending probe datagrams with a TTL value of one. This causes the first router to discard the probe datagram and send back an error message. The trace command sends several probes at each TTL level and displays the round-trip time for each. The trace command sends out one probe at a time. Each outgoing packet may result in one or two error messages. A “time exceeded” error message indicates that an intermediate router has seen and discarded the probe. A “destination unreachable” error message indicates that the destination node has received the probe and discarded it because it could not deliver the packet. If the timer goes off before a response comes in, trace prints an asterisk (*). The trace command terminates when the destination responds, when the maximum TTL is exceeded, or when the user interrupts the trace with the escape sequence. By default, to invoke the escape sequence, type Ctrl-^ X by simultaneously pressing and releasing the Ctrl, Shift, and 6 keys, and then pressing the X key. Common Trace Problems Due to bugs in the IP implementation of various hosts and routers, the IP trace command may behave in unexpected ways. Not all destinations will respond correctly to a probe message by sending back an “ICMP port unreachable” message. A long sequence of TTL levels with only asterisks, terminating only when the maximum TTL has been reached, may indicate this problem. There is a known problem with the way some hosts handle an “ICMP TTL exceeded” message. Some hosts generate an ICMP message but they reuse the TTL of the incoming packet. Since this is zero, the ICMP packets do not make it back. When you trace the path to such a host, you may see a set of TTL values with asterisks (*). Eventually the TTL gets high enough that the “ICMP” message can get back. For example, if the host is six hops away, trace will time out on responses 6 through 11. Trace IP Routes The following display shows sample IP trace output when a destination host name has been specified:

```text
trace ip ABA.NYC.mil
Type escape sequence to abort.
Tracing the route to ABA.NYC.mil (26.0.0.73)
1 DEBRIS.CISCO.COM (192.180.1.6) 1000 msec 8 msec 4 msec
2 BARRNET-GW.CISCO.COM (192.180.16.2) 8 msec 8 msec 8 msec
3 EXTERNAL-A-GATEWAY.STANFORD.EDU (192.42.110.225) 8 msec 4 msec 4 msec
4 BB2.SU.BARRNET.NET (192.200.254.6) 8 msec 8 msec 8 msec
5 SU.ARC.BARRNET.NET (192.200.3.8) 12 msec 12 msec 8 msec
6 MOFFETT-FLD-MB.in.MIL (192.52.195.1) 216 msec 120 msec 132 msec
7 ABA.NYC.mil (26.0.0.73) 412 msec 628 msec 664 msec
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| 1 | Indicatesthesequencenumberoftherouterinthepathtothehost. |
| DEBRIS.CISCO.COM | Hostnameofthisrouter. |
| 192.180.1.61 | Internetaddressofthisrouter. |
| 1000msec8msec4msec | Round-triptimeforeachofthethreeprobesthataresent. |

The following table describes the characters that can appear in trace output.

| Char | Description |
| --- | --- |
| nn msec | Foreachnode,theround-triptime(inmilliseconds)forthespecifiednumberofprobes. |

| Char | Description |
| --- | --- |
| * | Theprobetimedout. |
| ? | Unknownpackettype. |
| A | Administrativelyunreachable.Usually,thisoutputindicatesthatanaccesslistisblockingtraffic. |
| H | Hostunreachable. |
| N | Networkunreachable. |
| P | Protocolunreachable. |
| Q | Sourcequench. |
| U | Portunreachable. |


### `traceroute`

> **Página:** 1124 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** When not specified, the protocol argument is determined by the software examining the format of the destination argument. For example, if the software finds a destination argument in IP format, the protocol value defaults to IP. · **Leitura (show/clear/…):** não

**Description:** To discover the routes that packets will actually take when traveling to their destination address, use the

**Syntax:**

```text
traceroute command in user EXEC or privileged EXEC mode.
traceroute [vrf vrf-name | topology topology-name] [protocol] destination
```

**Parameters (Syntax Description):**

- `vrfvrf-name` — ( Optional) Specifies then a m e of a V P N v i r t u a l r out in g and for w a r d in g( VRF) in s t an c e t a b l e in which to f in d the destination address. The only keyword that you can s e l e c t for the p r o to c o l argument when you use the vrf vrf-name keyword-argument p a i r is the ip keyword.
- `to p o log y to p o log y-name` — ( Optional) Specifies then a m e of the to p o log y in s t an c e. The to p o log y-name argument is c as e-s e n s it i v e;“ V O I C E” and“ v o i c e” specify d if f e r e n t to p o log i e s.
- `p r o to c o l` — ( Optional) P r o to c o l keyword, e it h e r ap p l e t a l k, c l n s, ip, ip v6, ip x, o l d v in e s, or v in e s. When not specified, the p r o to c o l argument is b as e do n an e x a min at i on by the software of the format of the destination argument. The default p r o to c o l is IP.
- `destination` — ( Optional in privileged EXEC mode; r e q u i r e d in user EXEC mode) The Destination address or hostname you w an t to trace of the route. The software d e t e r min e s the default parameters for the ap p r o p r i at e p r o to c o l and the t r a c in g a c t i on begin s.

**Command Default:** When not specified, the protocol argument is determined by the software examining the format of the destination argument. For example, if the software finds a destination argument in IP format, the protocol value defaults to IP.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.0(5)T | The vrf vrf-name keyword and argument were added. |
| 12.2(2)T | This command was modified, support for IP v6 was added. |
| 12.0(21)ST | This command was modified, support for IP v6 was added. |
| 12.0(22)S | This command was modified, support for IP v6 was added. |
| 12.2(11)T | The traceroute command test characters for IP v6 were u p d at e d. An e we r r or message was added. |
| 12.2(14)S | This command was integrated into Cisco IOS Release12.2(14) S. |
| 12.3(5) | This command was modified, a line was added to the in t e r a c t i v e traceroute vrf command, s o that you can r e s o l v e the auto no m o u s system number t h r o u g h the use of the global t a b l e or a VRF t a b l e, or you can c h o o s e not to r e s o l v e the auto no m o u s system. |
| 12.0(26)S1 | This command was integrated into Cisco IOS Release12.0(26) S1. |
| 12.2(20)S | This command was integrated into Cisco IOS Release12.2(20) S. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(25)SG | This command was integrated into Cisco IOS Release12.2(25) S G. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SRB | The to p o log y to p o log y-name keyword-argument p a i r was added to support M u l t it o p o log y R out in g( M T R). |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.2(33)SRE | This command was integrated into Cisco IOS Release12.2(33) S R E. |
| CiscoIOSXERelease3.2S | This command was modified. When the vrf keyword is used, the output d is p l a y s the incoming VRF name/ t a g and the out g o in g VRF name/ t a g. |
| 15.0(1)SY | This command was modified. When the vrf keyword is used, the output d is p l a y s the incoming VRF name/ t a g and the out g o in g VRF name/ t a g. |
| 15.2(2)SNI | This command was i m p l e m e n t e do n the Cisco AS R901 S e r i e s A g g r e g at i on Service s Routers. |

**Usage Guidelines:**

The traceroute command works by taking advantage of the error messages generated by devices when a datagram exceeds its hop limit value. The traceroute command starts by sending probe datagrams with a hop limit of 1. Including a hop limit of 1 with a probe datagram causes the neighboring devices to discard the probe datagram and send back an error message. The traceroute command sends several probes with increasing hop limits and displays the round-trip time for each. The traceroute command sends out one probe at a time. Each outgoing packet might result in one or more error messages. A time-exceeded error message indicates that an intermediate device has seen and discarded the probe. A destination unreachable error message indicates that the destination node has received and discarded the probe because the hop limit of the packet reached a value of 0. If the timer goes off before a response comes in, the traceroute command prints an asterisk (*). The traceroute command terminates when the destination responds, when the hop limit is exceeded, or when the user interrupts the trace with the escape sequence. By default, to invoke the escape sequence, simultaneously press and release the Ctrl, Shift, and 6 keys, and then pressing the X key. To use nondefault parameters and invoke an extended traceroute test, enter the command without a protocol or destination argument in privileged EXEC mode then follow a series of steps to select the desired parameters. Extended traceroute tests are not supported in user EXEC mode. The user-level traceroute feature provides a basic trace facility for users who do not have system privileges. The destination argument is required in user EXEC mode. If the system cannot map an address for a hostname, it returns a “%No valid source address for destination” message. If the vrf vrf-name keyword-argument pair is used, the topology option is not displayed because only the default VRF instance is supported. The topology topology-name keyword-argument pair and the DiffServ Code Point (DSCP) option in the extended traceroute system dialog are displayed only if a topology is configured on the device. In Cisco IOS XE Release 3.2S, output of the traceroute command with the vrf keyword was enhanced to make troubleshooting easier by displaying the incoming VRF name/tag and the outgoing VRF name/tag.

**Example:**

After you enter the traceroute command in privileged EXEC mode, the system prompts you for a protocol. The default protocol is IP. If you enter a hostname or address on the same line as the traceroute command, the default action is taken as appropriate for the protocol type of that name or address. The following example is sample output from the traceroute command using default values in privileged EXEC mode. The specific output varies somewhat from protocol to protocol.

```text
Device# traceroute
Protocol [ip]:
Target IP address:
Source address:
DSCP Value [0]: ! Only displayed if a topology is configured on the device.
Numeric display [n]:
Timeout in seconds [3]:
Probe count [3]:
Minimum Time to Live [1]:
Maximum Time to Live [30]:
Port Number [33434]:
Loose, Strict, Record, Timestamp, Verbose [none]:
```

The following example displays output available in Cisco IOS XE Release 3.2S and later. Output of the traceroute command with the vrf keyword includes the incoming VRF name/tag and the outgoing VRF name/tag.

```text
Device# traceroute vrf red 10.0.10.12
Type escape sequence to abort.
Tracing the route to 10.0.10.12
VRF info: (vrf in name/id, vrf out name/id)
1 10.1.13.15 (red/13,red/13) 0 msec
10.1.16.16 (red/13,red/13) 0 msec
10.1.13.15 (red/13,red/13) 1 msec
2 10.1.8.13 (red/13,red/13) 0 msec
10.1.7.13 (red/13,red/13) 0 msec
10.1.8.13 (red/13,red/13) 0 msec
3 10.1.2.11 (red/13,blue/10) 1 msec 0 msec 0 msec
4 * * *
```


### `traceroute mac`

> **Página:** 1127 · **Modo:** Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the Layer 2 path taken by the packets from the specified source to the specified destination, use the traceroute maccommand in privileged EXEC mode.

**Syntax:**

```text
traceroute mac source-mac-address {destination-mac-address | interface type interface-number
destination-mac-address} [vlan vlan-id] [detail]
traceroute mac interface type interface-number source-mac-address {destination-mac-address |
interface type interface-number destination-mac-address} [vlan vlan-id] [detail]
traceroute mac ip {source-ip-addresssource-hostname} {destination-ip-addressdestination-hostname}
[detail]
```

**Parameters (Syntax Description):**

- `source-mac-address` — Media Access Control( MAC) address of the source switch in hexadecimal format.
- `destination-mac-address` — MAC address of the destination switch in hexadecimal format.
- `interface type` — Specifies the interface where the MAC address r e s id e s; v a l id values are Fast E the r n e t, G i g a b it E the r n e t, and Port-c h an n e l.
- `interface-number` — Module and port number or the port-c h an n e l number; v a l id values for the port c h an n e l are from1 to282.
- `vlan vlan-id` — ( Optional) Specifies the v i r t u alloc a l are an e two r k( VLAN) on which to trace the L a y e r2 path that the p a c k e t s t a k e from the source switch to the destination switch; v a l id values are from1 to4094.
- `detail` — ( Optional) D is p l a y s detailed information about the L a y e r2 trace.
- `ip` — Specifies the IP address where the MAC address r e s id e s.
- `source-ip-address` — IP address of the source switch as a32-b it q u an t it y in do t t e d-decimal format.
- `source-hostname` — IP hostname of the source switch.
- `destination-ip-address` — IP address of the destination switch as a32-b it q u an t it y in do t t e d-decimal format.
- `destination-hostname` — IP hostname of the destination switch.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SXE | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is not supported on the Cisco 7600 series router that is configured with a Supervisor Engine 2. Do not use leading zeros when entering a VLAN ID. For Layer 2 traceroute to functional properly, you must enable CDP on all of the switches in the network. Do not disable CDP. When the switch detects a device in the Layer 2 path that does not support Layer 2 traceroute, the switch continues to send Layer 2 trace queries and lets them time out. The maximum number of hops identified in the path is ten . Layer 2 traceroute supports only unicast traffic. If you specify a multicast source or destination MAC address, the physical path is not identified, and a message appears. The traceroute mac command output shows the Layer 2 path when the specified source and destination addresses belong to the same VLAN. If you specify source and destination addresses that belong to different VLANs, the Layer 2 path is not identified, and a message appears. If the source or destination MAC address belongs to multiple VLANs, you must specify the VLAN to which both the source and destination MAC addresses belong. If the VLAN is not specified, the path is not identified, and a message appears. When multiple devices are attached to one port through hubs (for example, multiple CDP neighbors are detected on a port), the Layer 2 traceroute utility terminates at that hop and displays an error message. This feature is not supported in Token Ring VLANs.

**Example:**

This example shows how to display detailed information about the Layer 2 path:

```text
Router# traceroute mac 0001.0000.0204 0001.0000.0304 detail
Source 1001.0000.0204 found on VAYU[WS-C6509] (10.1.1.10)
1 VAYU / WS-C6509 / 10.1.1.10 :
Gi6/1 [full, 1000M] => Po100 [auto, auto]
2 PANI / WS-C6509 / 10.1.1.12 :
Po100 [auto, auto] => Po110 [auto, auto]
3 BUMI / WS-C6509 / 10.1.1.13 :
Po110 [auto, auto] => Po120 [auto, auto]
4 AGNI / WS-C6509 / 10.1.1.11 :
Po120 [auto, auto] => Gi8/12 [full, 1000M]
Destination 1001.0000.0304 found on AGNI[WS-C6509] (10.1.1.11)
Layer 2 trace completed.
```

This example shows the output when the switch is not connected to the source switch:

```text
Router# traceroute mac 0000.0201.0501 0000.0201.0201 detail
Source not directly connected, tracing source .....
Source 1000.0201.0501 found on con5[WS-C6509] (10.2.5.5)
con5 / WS-C6509 / 10.2.5.5 :
Fa0/1 [auto, auto] =>Gi0/1 [auto, auto]
con1 / WS-C6509 / 10.2.1.1 :
Gi0/1 [auto, auto] =>Gi0/2 [auto, auto]
con2 / WS-C6509 / 10.2.2.2 :
Gi0/2 [auto, auto] =>Fa0/1 [auto, auto]
Destination 1000.0201.0201 found on con2[WS-C6509] (10.2.2.2)
Layer 2 trace completed.
```

This example shows the output when the switch cannot find the destination port for the source MAC address:

```text
traceroute mac 0000.0011.1111 0000.0201.0201
Error:Source Mac address not found.
Layer2 trace aborted.
```

This example shows the output when the source and destination devices are in different VLANs:

```text
Router# traceroute mac 0000.0201.0601 0000.0301.0201
Error:Source and destination macs are on different vlans.
Layer2 trace aborted.
```

This example shows the output when the destination MAC address is a multicast address:

```text
Router# traceroute mac 0000.0201.0601 0100.0201.0201
Invalid destination mac address
```

This example shows the output when the source and destination switches belong to multiple VLANs:

```text
Router# traceroute mac 0000.0201.0601 0000.0201.0201
Error:Mac found on multiple vlans.
Layer2 trace aborted.
```

This example shows how to display the Layer 2 path by specifying the interfaces on the source and destination switches:

```text
Router# traceroute mac interface fastethernet0/1 0000.0201.0601 interface fastethernet0/3
0000.0201.0201
Source 1000.0201.0601 found on con6[WS-C6509] (10.2.6.6)
con6 (10.2.6.6) :Fa0/1 =>Fa0/3
con5 (10.2.5.5 ) : Fa0/3 =>Gi0/1
con1 (10.2.1.1 ) : Gi0/1 =>Gi0/2
con2 (10.2.2.2 ) : Gi0/2 =>Fa0/1
Destination 1000.0201.0201 found on con2[WS-C6509] (10.2.2.2)
Layer 2 trace completed
```

This example shows how to display detailed traceroute information:

```text
traceroute mac ip 10.2.66.66 10.2.22.22 detail
Translating IP to mac.....
10.2.66.66 =>0000.0201.0601
10.2.22.22 =>0000.0201.0201
Source 0000.0201.0601 found on con6[WS-C6509] (10.2.6.6)
con6 / WS-C6509 / 10.2.6.6 :
Fa0/1 [auto, auto] =>Fa0/3 [auto, auto]
con5 / WS-C6509 / 10.2.5.5 :
Fa0/3 [auto, auto] =>Gi0/1 [auto, auto]
con1 / WS-C6509 / 10.2.1.1 :
Gi0/1 [auto, auto] =>Gi0/2 [auto, auto]
con2 / WS-C6509 / 10.2.2.2 :
Gi0/2 [auto, auto] =>Fa0/1 [auto, auto]
Destination 0000.0201.0201 found on con2[WS-C6509] (10.2.2.2)
Layer 2 trace completed.
```

This example shows how to display the Layer 2 path by specifying the source and destination hostnames:

```text
Router# traceroute mac ip con6 con2
Translating IP to mac .....
10.2.66.66 =>0000.0201.0601
10.2.22.22 =>0000.0201.0201
Source 0000.0201.0601 found on con6
con6 (10.2.6.6) :Fa0/1 =>Fa0/3
con5 (10.2.5.5 ) : Fa0/3 =>Gi0/1
con1 (10.2.1.1 ) : Gi0/1 =>Gi0/2
con2 (10.2.2.2 ) : Gi0/2 =>Fa0/1
Destination 0000.0201.0201 found on con2
Layer 2 trace completed
```

This example shows the output when ARP cannot associate the source IP address with the corresponding MAC address:

```text
Router# traceroute mac ip 10.2.66.66 10.2.77.77
Arp failed for destination 10.2.77.77.
Layer2 trace aborted.
```


### `undelete`

> **Página:** 1130 · **Modo:** user EXEC privileged EXEC · **Default:** The default file system is the one specified by the cd command. · **Leitura (show/clear/…):** não

**Description:** To recover a file marked “deleted” on a Class A Flash file system, use the undelete command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
undelete index [filesystem :]
```

**Parameters (Syntax Description):**

- `index` — An u m be r that in d e x e s the file in the dir command output.
- `filesystem :` — ( Optional) A filesystem c on t a in in gt h e file to undelete, f o l low e d by a c o l on.

**Command Default:** The default file system is the one specified by the cd command.

**Command Modes:** user EXEC privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | This command was introduced for Class AFlash File Systems( platform s include the Cisco 7500 s e r i e s and Cisco12000 s e r i e s). |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command was introduced on the Supervisor Engine2. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

For Class A Flash file systems, when you delete a file, the Cisco IOS software simply marks the file as deleted, but it does not erase the file. This command allows you to recover a “deleted” file on a specified Flash memory device. You must undelete a file by its index because you could have multiple deleted files with the same name. For example, the “deleted” list could contain multiple configuration files with the name router-config. You undelete by index to indicate which of the many router-config files from the list to undelete. Use the dir command to learn the index number of the file you want to undelete. You cannot undelete a file if a valid (undeleted) file with the same name exists. Instead, you first delete the existing file and then undelete the file you want. For example, if you had an undeleted version of the router-config file and you wanted to use a previous, deleted version instead, you could not simply undelete the previous version by index. You would first delete the existing router-config file and then undelete the previous router-config file by index. You can delete and undelete a file up to 15 times. On Class A Flash file systems, if you try to recover the configuration file pointed to by the CONFIG_FILE environment variable, the system prompts you to confirm recovery of the file. This prompt reminds you that the CONFIG_FILE environment variable points to an undeleted file. To permanently delete all files marked “deleted” on a Flash memory device, use the squeeze EXEC command. For further information on Flash File System types (classes), see http://www.cisco.com/en/US/products/hw/routers/ps341/products_tech_note09186a00800a7515.shtml.

**Example:**

In the following example, the deleted file at index 1 is recovered:

```text
Router# show flash
System flash directory:
File Length Name/status
1 8972116 c7000-js56i-mz.121-5.T [deleted]
2 6765916 c7000-ds-mz.CSCds70452
[15738160 bytes used, 1039056 available, 16777216 total]
16384K bytes of processor board System flash (Read/Write)
Router# undelete 1 flash:
```


### `unprofile`

> **Página:** 1132 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To free the memory either by deleting data or disabling the profiles, use the unprofilecommand in privilegedEXEC mode.

**Syntax:**

```text
unprofile {process {process-IDprocess-name}} {start-address end-address increment | all | task}
```

**Parameters (Syntax Description):**

- `process` — Set s the process s p e c if i c information.
- `process-ID` — Process ID. The range is from1 to4294967295.
- `process-name` — Name of the process.
- `start-address` — Starting address of the profile.
- `end-address` — End in g address of the profile.
- `in c r e m e n t` — In c r e m e n t in g address of the profile.
- `all` — Delete s all profile data.
- `task` — Disable s t as k p r of i l in g.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release 15.0(1)M. |
| 12.2(33)SRB | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRB. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was i m p l e m e n t e do n the Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Example:**

The following example shows how to delete all the profile data:

```text
Router# unprofile
process all
```


### `upgrade automatic abortversion`

> **Página:** 1132 · **Modo:** Privileged EXEC (#) · **Default:** The reload of the device with the Cisco software image is not scheduled. The disk-management utility is disabled. · **Leitura (show/clear/…):** não

**Description:** To cancel the scheduled reloading of the device with a new Cisco software image, use the upgrade automatic abortversion command in privileged EXEC mode.

**Syntax:**

```text
upgrade automatic abortversion
no upgrade automatic abortversion
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** The reload of the device with the Cisco software image is not scheduled. The disk-management utility is disabled.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(15)T | This command was introduced. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Use the upgrade automatic abortversion command to cancel a reload that has already been scheduled with either the upgrade automatic getversion command or the upgrade automatic runversion command.

**Example:**

The following example shows how to cancel a reload that is scheduled within one hour and 15 minutes. The reload was scheduled by using the upgrade automatic runversion command.

```text
Device#
upgrade automatic runversion in 01:15
Upgrading to "flash:c1841-adventerprisek9-mz.calvin-build-20060714". Wait..
Reload scheduled for 09:51:38 UTC Thu Aug 3 2006 (in 1 hour and 15 minutes) with image -
flash:c1841-adventerprisek9-mz.calvin-build-20060714 by console
Reload reason: Auto upgrade
Device will WARM UPGRADE in 1:15:00
To cancel the upgrade, enter the command "upgrade automatic abortversion"
Aug 3 08:36:38.072: %SYS-5-SCHEDULED_RELOAD: Reload requested for 09:51:38 UTC Thu Aug 3
2006 at 08:36:38 UTC Thu Aug 3 2006 by console. Reload Reason: Auto upgrade.
Device# upgrade automatic abortversion
Auto upgrade of image which was scheduled earlier is aborted!
***
*** --- SHUTDOWN ABORTED ---
***
Aug 3 08:37:02.292: %SYS-5-SCHEDULED_RELOAD_CANCELLED: Scheduled reload cancelled at
08:37:02 UTC Thu Aug 3 2006
```


### `upgrade automatic getversion`

> **Página:** 1133 · **Modo:** Privileged EXEC (#) · **Default:** The reload of the device with the Cisco software image is not scheduled. The disk-management utility is disabled. · **Leitura (show/clear/…):** não

**Description:** To download a Cisco software image directly from www.cisco.com or from a non-Cisco server, use the

**Syntax:**

```text
upgrade automatic getversion command in privileged EXEC mode.
upgrade automatic getversion {cisco username username password password image imageurl}
{[at hh:mm]now | [in hh:mm]} [disk-management {auto | confirm | no}]
```

**Parameters (Syntax Description):**

- `cisco` — Download s the image from w w w. cisco. com.
- `username username` — Username for logging into w w w. cisco. com.
- `password password` — Password for logging into w w w. cisco. com.
- `image` — Specifies the Cisco software image to which the device is to be upgrade d.
- `image` — Name of the Cisco software image to which the device is to be upgrade d.
- `url` — URL from where the Cisco Auto-Upgrade M an age r can download the image that has a l r e a d y been download e d to an on-Cisco server.
- `at` — ( Optional) Schedule s are load at as p e c if i e d time. Use e it h e r of the following arguments with this keyword: • h h: m m--H our and min u t e. The time enter e d must be in24-h our format. • no w--I m m e d i at e l y after the download of the Cisco software image.
- `in hh:mm` — ( Optional) Schedule s are load in as p e c if i e d length of time after download in gt h e Cisco software image.
- `disk-management` — ( Optional) Cisco Auto-Upgrade M an age r disk cleanup u t i l it y. You must configure one of the following keywords: • auto--Delete s the files with out as k in g for confirm at i on. • confirm--As k s for confirm at i on before d e l e t in g a file. • no--N e v e r delete s any file.

**Command Default:** The reload of the device with the Cisco software image is not scheduled. The disk-management utility is disabled.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(15)T | This command was introduced. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Use the upgrade automatic getversion command to download the Cisco software image to a device. You can either download the image from the Cisco website (www.cisco.com) or from a non-Cisco server to which the Cisco software image has already been downloaded from the Cisco website. You can also use this command to schedule a reload. Additionally, this command can use the disk cleanup utility to delete files if there is not enough space to download the new Cisco software image. Downloading the Cisco Image from the Cisco Website The following example shows how to download a Cisco software image from the Cisco website (www.cisco.com). Here, the reloading of the device with the downloaded Cisco software image is not scheduled. Also, the disk-cleanup utility is not enabled.

```text
Device# upgrade automatic getversion cisco username myusername password mypassword image
c3825-adventerprisek9-mz.124-2.XA.bin
```

Downloading the Cisco Image from a Non-Cisco TFTP Server The following example shows how to download the Cisco software image from a non-Cisco TFTP server and reload the device immediately after the download. It also shows how to delete the files automatically if there is not enough disk space.

```text
Device# upgrade automatic getversion tftp://abc/tom/c3825-adventerprisek9-mz.124-2.XA.bin
at now disk-management auto
```

Downloading the Cisco Image from a Non-Cisco TFTP Server Using the Interactive Mode The following example shows how to use this command in interactive mode to download a Cisco software image from a non-Cisco server. Here, the reloading of the device with the downloaded Cisco software image is not scheduled.

```text
Device# upgrade automatic
################################################################################
Welcome to the Cisco Auto Upgrade Manager. To upgrade your device, please answer the following
questions. To accept the default value for a question, simply hit <ENTER>
################################################################################
Would you like to download an image directly from Cisco Server over the Internet? A valid
Cisco login will be required.
Download from Cisco server? [yes]: no
Image location:tftp://10.1.0.1/emailid/c3825-adventerprisek9-mz_pi6_aum_review
Image Found: c3825-adventerprisek9-mz_pi6_aum_review (42245860 bytes)
Memory Available: 851Mb Main Memory (RAM) - 71335936 bytes of flash space
New image will be downloaded to flash:c3825-adventerprisek9-mz_pi6_aum_review
Reload and upgrade the device immediately after image download is complete? [yes]: no
When would you like to reload your device? Use hh:mm format or specify "Manual" to not
schedule a reload time. Use 'upgrade automatic runversion' to reload manually.
Time to reload the box [Manual]?
Proceed with device image upgrade from
[tftp://10.1.0.1/emailid/c3825-adventerprisek9-mz_pi6_aum_review] to
[c3825-adventerprisek9-mz_pi6_aum_review]? [yes]:
Downloading Image from user specified url:
Loading emailid/c3825-adventerprisek9-mz_pi6_aum_review from 172.16.0.0(via
GigabitEthernet0/0): !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[OK - 42245860 bytes]
[download complete]
Verifiying the image: .........................
Done!
Image Verification: PASS
Use 'upgrade automatic runversion' command to reload manually.
```


### `upgrade automatic runversion`

> **Página:** 1136 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To reload the device with a new Cisco software image, use the upgrade automatic runversion command in privileged EXEC mode.

**Syntax:**

```text
upgrade automatic runversion {at hh:mmnow | in hh:mm}
```

**Parameters (Syntax Description):**

- `at` — Schedule s are load at as p e c if i e d time. Use e it h e r of the following arguments with this keyword: • h h: m m--H our and min u t e. The time enter e d must be in24-h our format. • no w--I m m e d i at e l y after the download of the Cisco software image.
- `in hh:mm` — Schedule s are load in as p e c if i e d length of time after download in gt h e Cisco software image.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(15)T | This command was introduced. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Use the upgrade automatic runversion command to schedule a reload after downloading a Cisco software image using the upgrade automatic getversion command. Note You can also use the upgrade automatic getversion command to reload the device with the new Cisco software image. However, if you have already downloaded the Cisco software image using the upgrade automatic getversion command, you should use the upgrade automatic runversion command to reload the device.

**Example:**

The following example shows how to schedule a reload after downloading a Cisco software image:

```text
Device# show clock
09:01:36.124 UTC Thu Aug 3 2006
Device# upgrade automatic runversion at 10:20
Upgrading to "flash:c1841-adventerprisek9-mz.calvin-build-20060714". Wait..
Reload scheduled for 10:20:00 UTC Thu Aug 3 2006 (in 1 hour and 18 minutes) with image -
flash:c1841-adventerprisek9-mz.calvin-build-20060714 by console
Reload reason: Auto upgrade
Device will WARM UPGRADE at 10:20:00
To cancel the upgrade, enter the command "upgrade automatic abortversion"
Device#
Aug 3 09:01:58.116: %SYS-5-SCHEDULED_RELOAD: Reload requested for 10:20:00 UTC Thu Aug 3
2006 at 09:01:58 UTC Thu Aug 3 2006 by console. Reload Reason: Auto upgrade.
```


### `upgrade filesystem monlib`

> **Página:** 1137 · **Modo:** Privileged EXEC(#) · **Default:** No default behavior or values · **Leitura (show/clear/…):** não

**Description:** To upgrade the ATA ROM monitor library (monlib) file without erasing file system data, use the upgrade filesystem monlibcommand in privileged EXEC mode.

**Syntax:**

```text
upgrade filesystem monlib {disk0 | disk1}
```

**Parameters (Syntax Description):**

- `disk0` — S e l e c t s disk0 as the filesystem to be format t e d.
- `disk1` — S e l e c t s disk1 as the filesystem to be format t e d.

**Command Default:** No default behavior or values

**Command Modes:** Privileged EXEC(#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(7)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2YST | This command was integrated into Cisco IOS Release12.2 Y S T. |

**Usage Guidelines:**

If you attempt to upgrade the ATA monlib file on a disk that has not been formatted on a router running Cisco IOS software, the upgrade operation will fail. If the amount of space available on the disk for the monlib image is smaller than the monlib image you are trying to upgrade to, the upgrade operation will fail. The amount of space available for the monlib file can be determined by issuing the show disk command with the all keyword specified. The “Disk monlib size” field displays the number of bytes available for the ATA monlib file.

**Example:**

The following example shows how to upgrade the ATA monlib file on disk 0:

```text
Router# upgrade filesystem monlib disk0
Hash Computation: 100%Done!
Computed Hash SHA2: DFBA87256310DC8A7B7BF8158451F7F4
0AC333C9B396D9D0E42DDBD542C30E08
F3946DDE692AF04F0B20F29BE51C49C4
1B631790A542D81F9A7C90ABC2426960
Embedded Hash SHA2: DFBA87256310DC8A7B7BF8158451F7F4
0AC333C9B396D9D0E42DDBD542C30E08
F3946DDE692AF04F0B20F29BE51C49C4
1B631790A542D81F9A7C90ABC2426960
Digital signature successfully verified in file Monlib
Writing Monlib sectors....
Monlib write complete
```


### `upgrade rom-monitor`

> **Página:** 1138 · **Modo:** Privileged EXEC (#) Diagnostic (diag) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** não

**Description:** To set the execution preference on a read-only memory monitor (ROMMON), use the upgrade rom-monitor command in privileged EXEC or diagnostic mode. Cisco ASR 1000 Series Aggregation Services Routers

**Syntax:**

```text
upgrade rom-monitor slot num {sp | rp} file filename
upgrade rom-monitor slot num {sp | rp} {invalidate | preference} {region1 | region2}
upgrade rom-monitor filename URL slot
```

**Parameters (Syntax Description):**

- `slot num` — Specifies the slot number of the ROMMON to be upgrade d.
- `sp` — Upgrade s the ROMMON of the Switch Processor.
- `rp` — Upgrade s the ROMMON of the Route Processor.
- `file file name` — Specifies then a m e of the S-r e c or d( S R E C) file; see the“ Usage Guidelines” section for v a l id values.
- `in v a l ida t e` — In v a l ida test h e ROMMON of these l e c t e d region.
- `preference` — Set s the exec u t i on preference on a ROMMON of these l e c t e d region.
- `region1` — S e l e c t s the ROMMON in region1.
- `region2` — S e l e c t s the ROMMON in region2.
- `file name` — Specifies the ROMMON package file name.
- `URL` — The URLtoa ROMMON file. The URL a l w a y s begin s with a filesystem, such as bootflash:, h a r d disk:, o b f l:, s t by-h a r d disk:, or usb[0-1], then specifies the path to the file.
- `slot` — The slot that c on t a in s the hardware that will r e c e i v e the ROMMON upgrade. Options are: • number--then u m be r of the Session In it i at i on P r o to c o l( S IP) slot that r e q u i r e s the ROMMON upgrade • all--All hardware on the router • F0--E m be d d e d-Service-Processor slot0 • F1--E m be d d e d-Service-Processor slot1 • F P--All install e d E m be d d e d-Service-Processor s • R0--Route-Processor slot0 • R1--Route-Processor slot1 • R P--Route-Processor

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | This command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | This command was modified. Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.4(24)T | This command was integrated into Cisco IOS Release12.4(24) T. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco AS R1000 S e r i e s Routers, and introduced in diagnostic mode. |

**Usage Guidelines:**

Caution If you enter the upgrade rom-monitor command from a Telnet session instead of a console connection, service may be interrupted. The slot numkeyword and argument combination is required for this command to function properly. The sp or rpkeyword is required if you installed a supervisor engine in the specified slot. Valid values for file filename are the following: • bootflash: • disk0: • disk1: • flash: • ftp: • rcp: • sup-bootflash: • sup-slot0: • tftp: On Cisco ASR 1000 Series Routers, this command can be used to upgrade ROMMON in privileged EXEC and diagnostic mode. The hardware receiving the ROMMON upgrade must be reloaded to complete the upgrade. From Cisco IOS Release 12.4(24)T, you can use the upgrade rom-monitor command on Cisco 3200 series routers to upgrade ROMMON and the system bootstrap, if a newer version of ROMMON is available on the system.

**Example:**

This example shows how to upgrade the new ROMMON image to the flash device on a Supervisor Engine 2:

```text
Router# upgrade rom-monitor
slot 1 sp file tftp://dirt/tftpboot-users/A2_71059.srec
ROMMON image upgrade in progress
Erasing flash
Programming flash
Verifying new image
ROMMON image upgrade complete
The card must be reset for this to take effect
```

In the following example, a ROMMON upgrade is performed to upgrade to Cisco IOS Release 12.2(33r)XN1 on a Cisco ASR 1000 Series Router using an ROMMON image stored on the bootflash: file system. All hardware is upgraded on the Cisco ASR 1000 Series Router in this example, and the router is then reloaded to complete the procedure.

```text
Router# show rom-monitor 0
System Bootstrap, Version 12.2(33)XN1, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2007 by cisco Systems, Inc.
Router# show rom-monitor F0
System Bootstrap, Version 12.2(33)XN1, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2007 by cisco Systems, Inc.
Router# show rom-monitor R0
System Bootstrap, Version 12.2(33)XN1, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2007 by cisco Systems, Inc.
copy tftp bootflash:
Address or name of remote host []?
127.23.16.81
Source filename []? auto/tftp-boot/asr1000-rommon.122-33r.XN1.pkg
Destination filename [asr1000-rommon.122-33r.XN1.pkg]?
Accessing tftp://127.23.16.81/auto/tftp-boot/asr1000-rommon.122-33r.XN1.pkg...
Loading auto/tftp-boot/asr1000-rommon.122-33r.XN1.pkg from 127.23.16.81 (via
GigabitEthernet0): !!!
[OK - 553164 bytes]
553164 bytes copied in 1.048 secs (527828 bytes/sec)
dir bootflash:
Directory of bootflash:/
11 drwx 16384 Dec 2 2004 12:02:09 +00:00 lost+found
14401 drwx 4096 Dec 2 2004 12:05:05 +00:00 .ssh
86401 drwx 4096 Dec 2 2004 12:05:07 +00:00 .rollback_timer
12 -rw- 33554432 Nov 20 2007 19:53:47 +00:00 nvram_00100
13 -rw- 6401536 Dec 23 2004 19:45:11 +00:00 mcp-fpd-pkg.122-test.pkg
28801 drwx 4096 Nov 1 2007 17:00:36 +00:00 .installer 15 -rw- 553164
Nov 28 2007 15:33:49 +00:00 asr1000-rommon.122-33r.XN1.pkg
16 -rw- 51716300 Nov 14 2007 16:39:59 +00:00
asr1000rp1-espbase.v122_33_xn_asr_rls0_throttle.pkg
17 -rw- 21850316 Nov 14 2007 16:41:23 +00:00
asr1000rp1-rpaccess-k9.v122_33_xn_asr_rls0_throttle.pkg
18 -rw- 21221580 Nov 14 2007 16:42:21 +00:00
asr1000rp1-rpbase.v122_33_xn_asr_rls0_throttle.pkg
19 -rw- 27576524 Nov 14 2007 16:43:50 +00:00
asr1000rp1-rpcontrol.v122_33_xn_asr_rls0_throttle.pkg
20 -rw- 48478412 Nov 14 2007 16:45:50 +00:00
asr1000rp1-rpios-advipservicesk9.v122_33_xn_asr_rls0_throttle.pkg
21 -rw- 36942028 Nov 14 2007 16:47:17 +00:00
asr1000rp1-sipbase.v122_33_xn_asr_rls0_throttle.pkg
22 -rw- 14749900 Nov 14 2007 16:48:17 +00:00
asr1000rp1-sipspa.v122_33_xn_asr_rls0_throttle.pkg
23 -rw- 6049 Nov 14 2007 16:49:29 +00:00 packages.conf
14 -rw- 213225676 Nov 20 2007 19:53:13 +00:00
asr1000rp1-advipservicesk9.v122_33_xn_asr_rls0_throttle.bin
928833536 bytes total (451940352 bytes free)
Router# upgrade rom-monitor filename bootflash:/asr1000-rommon.122-33r.XN1.pkg all
Upgrade rom-monitor on Route-Processor 0
Target copying rom-monitor image file
Checking upgrade image...
1966080+0 records in
3840+0 records out
Upgrade image MD5 signature is 253f15daf89eea22b1db92d440d03608
Burning upgrade partition...
1966080+0 records in
3840+0 records out
Checking upgrade partition...
Upgrade flash partition MD5 signature is 253f15daf89eea22b1db92d440d03608
ROMMON upgrade complete.
To make the new ROMMON permanent, you must restart the RP.
Upgrade rom-monitor on Embedded-Service-Processor 0
Target copying rom-monitor image file
Checking upgrade image...
1966080+0 records in
3840+0 records out
Upgrade image MD5 signature is 253f15daf89eea22b1db92d440d03608
Burning upgrade partition...
1966080+0 records in
3840+0 records out
Checking upgrade partition...
Upgrade flash partition MD5 signature is 253f15daf89eea22b1db92d440d03608
ROMMON upgrade complete.
To make the new ROMMON permanent, you must restart the linecard.
Upgrade rom-monitor on SPA-Inter-Processor 0
Target copying rom-monitor image file
Checking upgrade image...
1966080+0 records in
3840+0 records out
Upgrade image MD5 signature is 253f15daf89eea22b1db92d440d03608
Burning upgrade partition...
1966080+0 records in
3840+0 records out
Checking upgrade partition...
Upgrade flash partition MD5 signature is 253f15daf89eea22b1db92d440d03608
ROMMON upgrade complete.
To make the new ROMMON permanent, you must restart the linecard.
Upgrade rom-monitor on SPA-Inter-Processor 1
Target copying rom-monitor image file
Checking upgrade image...
1966080+0 records in
3840+0 records out
Upgrade image MD5 signature is 253f15daf89eea22b1db92d440d03608
Burning upgrade partition...
1966080+0 records in
3840+0 records out
Checking upgrade partition...
Upgrade flash partition MD5 signature is 253f15daf89eea22b1db92d440d03608
ROMMON upgrade complete.
To make the new ROMMON permanent, you must restart the linecard.
Router# reload
<reload bootup output removed for brevity>
Router# show rom-monitor 0
System Bootstrap, Version 12.2(33r)XN1, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2007 by cisco Systems, Inc.
Router# show rom-monitor F0
System Bootstrap, Version 12.2(33r)XN1, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2007 by cisco Systems, Inc.
Router# show rom-monitor R0
System Bootstrap, Version 12.2(33r)XN1, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2007 by cisco Systems, Inc.
```


### `upgrade filesystem monlib`

> **Página:** 1142 · **Modo:** Privileged EXEC(#) · **Default:** No default behavior or values · **Leitura (show/clear/…):** não

**Description:** To upgrade the ATA ROM monitor library (monlib) file without erasing file system data, use the upgrade filesystem monlibcommand in privileged EXEC mode.

**Syntax:**

```text
upgrade filesystem monlib {disk0 | disk1}
```

**Parameters (Syntax Description):**

- `disk0` — S e l e c t s disk0 as the filesystem to be format t e d.
- `disk1` — S e l e c t s disk1 as the filesystem to be format t e d.

**Command Default:** No default behavior or values

**Command Modes:** Privileged EXEC(#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(7)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2YST | This command was integrated into Cisco IOS Release12.2 Y S T. |

**Usage Guidelines:**

If you attempt to upgrade the ATA monlib file on a disk that has not been formatted on a router running Cisco IOS software, the upgrade operation will fail. If the amount of space available on the disk for the monlib image is smaller than the monlib image you are trying to upgrade to, the upgrade operation will fail. The amount of space available for the monlib file can be determined by issuing the show disk command with the all keyword specified. The “Disk monlib size” field displays the number of bytes available for the ATA monlib file.

**Example:**

The following example shows how to upgrade the ATA monlib file on disk 0:

```text
Router# upgrade filesystem monlib disk0
Hash Computation: 100%Done!
Computed Hash SHA2: DFBA87256310DC8A7B7BF8158451F7F4
0AC333C9B396D9D0E42DDBD542C30E08
F3946DDE692AF04F0B20F29BE51C49C4
1B631790A542D81F9A7C90ABC2426960
Embedded Hash SHA2: DFBA87256310DC8A7B7BF8158451F7F4
0AC333C9B396D9D0E42DDBD542C30E08
F3946DDE692AF04F0B20F29BE51C49C4
1B631790A542D81F9A7C90ABC2426960
Digital signature successfully verified in file Monlib
Writing Monlib sectors....
Monlib write complete
```


### `upgrade rom-monitor preference`

> **Página:** 1143 · **Modo:** Privileged EXEC · **Default:** No default behavior or values · **Leitura (show/clear/…):** não

**Description:** To select a ReadOnly or Upgrade ROMmon image to be booted on the next reload of a Cisco 7200 VXR or Cisco 7301router, use the upgrade rom-monitor preferencecommand in privileged EXEC mode.

**Syntax:**

```text
upgrade rom-monitor preference [readonly | upgrade]
```

**Parameters (Syntax Description):**

- `r e a do n l y` — S e l e c t s the Read Only ROMmon image to be boot e do n then e x t reload.
- `upgrade` — S e l e c t s the Upgrade s e c on d ROMmon image to be boot e do n then e x t reload.

**Command Default:** No default behavior or values

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(28)S | This command was introduced on the Cisco7200 V X R router. |
| 12.3(8)T | This command was integrated into Cisco IOS Release12.3(8) T and supported on the Cisco7200 V X R router and Cisco7301 router. |
| 12.3(9) | This command was integrated into Cisco IOS Release12.3(9) and supported on the Cisco7200 V X R router and Cisco7301 router. |

**Usage Guidelines:**

After running the upgrade rom-monitor preference command, you must reload the router for the selected ROMmon image to take effect. Use the rommon-prefcommand when you are in ROMmon mode.

**Example:**

The following example applicable to both the Cisco 7200 VXR and Cisco 7301 routers selects the ReadOnly ROMmon image to be booted on the next reload of the router:

```text
Router# upgrade rom-monitor preference readonly
You are about to mark ReadOnly region of ROMMON for the highest boot preference.
Proceed? [confirm]
Done! Router must be reloaded for this to take effect.
```


### `vacant-message`

> **Página:** 1144 · **Modo:** Line configuration · **Default:** The format of the default vacant message is as follows: <blank lines> hostname tty# is now available <blank lines> Press RETURN to get started. This message is generated by the system. · **Leitura (show/clear/…):** não

**Description:** To display an idle terminal message, use the vacant-message command in line configuration mode. To remove the default vacant message or any other vacant message that may have been set, use the no form of this command.

**Syntax:**

```text
vacant-message [d message d]
no vacant-message
```

**Parameters (Syntax Description):**

- `d` — ( Optional) D e limit in g character that mark s the begin n in g and end of the vacant-message. Text d e limit e r s are characters that do not or d in a r i l y ap p e a r with in the text of at it l e, such as s l as h(/ ), do u b l e q u o t e("), or t i l d e(~).^ C isr e s e r v e d for special use and should not be used in the message.
- `message` — ( Optional) Vacant terminal message.

**Command Default:** The format of the default vacant message is as follows: <blank lines> hostname tty# is now available <blank lines> Press RETURN to get started. This message is generated by the system.

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command enables the banner to be displayed on the screen of an idle terminal. The vacant-message command without any arguments restores the default message. Follow this command with one or more blank spaces and a delimiting character of your choice. Then enter one or more lines of text, terminating the message with the second occurrence of the delimiting character. Note For a rotary group, you need to define only the message for the first line in the group.

**Example:**

The following example turns on the system banner and displays this message:

```text
Router(config)# line 0
Router(config-line)#
vacant-message %
Welcome to Cisco Systems, Inc.
Press Return to get started.
%
```


### `verify`

> **Página:** 1145 · **Modo:** Privileged EXEC · **Default:** The current working device is the default device (file system). · **Leitura (show/clear/…):** não

**Description:** To verify the checksum of a file on a flash memory file system or compute a Message Digest 5 (MD5) signature for a file, use the verify command in privileged EXEC mode. [ [ ]] [ ] Cisco 7600 Series Router

**Syntax:**

```text
verify /md5 md5-value filesystem: file-url
verify {/md5 flash-filesystem [expected-md5-signature] | /ios flash-filesystemflash-filesystem}
```

**Parameters (Syntax Description):**

- `/md5` — ( Optional) C a l c u l at e s and d is p l a y s the M D5 value for the specified software image. C o m p are this value with the value a v a i l a b l e on Cisco. c o m for this image.
- `md5-value` — ( Optional) The k no w n M D5 value for the specified image. Whenan M D5 value is specified in the command, the system c a l c u l at e s the M D5 value for the specified image and d is p l a y a message verify in gt h at the M D5 values m at c h or that the r e is a m is m at c h.
- `filesystem :` — Filesystem or directory c on t a in in gt h e files to list, f o l low e d by a c o l on. S t and a r d filesystem keywords for this command are flash: and bootflash:.
- `file-url` — ( Optional) Then a m e of the files to d is p l a y on as p e c if i e d device. The files can be of any type. You can use w i l d card s in the file name. A w i l d card character(*) m at c h e s all p at t e r n s. Strings after a w i l d card are i g nor e d.
- `Cisco7600 S e r i e s Router` — C o m p u t e s an M D5 s i g n at u r e for a file; v a l id values are bootflash:, disk0:, disk1:, flash:, or sup-bootflash:.
- `/md5 flash-filesystem`
- `expected-md5-signature` — ( Optional) M D5 s i g n at u r e.
- `/ios flash-filesystem` — V e r if i e s the compress e d Cisco IOS image check s u m; v a l id values are bootflash:, disk0:, disk1:, flash:, or sup-bootflash:.
- `flash-filesystem` — Device where the Flash memory r e s id e s; v a l id values are bootflash:, disk0:, disk1:, flash:, or sup-bootflash:.

**Command Default:** The current working device is the default device (file system).

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | This command was introduced. |
| 12.2(4)T | The/ m d5 keyword was added. |
| 12.2(18)S | The verify command was e n h an c e d to verify the has h that is c on t a in e d in the image, and the output was e n h an c e d to show the has h value in a d d it i onto the e n t i r e has h image( C C O hash). |
| 12.0(26)S | The verify command e n h an c e m e n t s were integrated into Cisco IOS Release12.0(26) S. |
| 12.2(14)SX | Support for this command was added for the Supervisor E n g in e720. |
| 12.3(4)T | The verify command e n h an c e m e n t s were integrated into Cisco IOS Release12.3(4) T. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command replaces the copy verify and copy verify flash commands. Use the verify command to verify the checksum of a file before using it. Each software image that is distributed on disk uses a single checksum for the entire image. This checksum is displayed only when the image is copied into flash memory; it is not displayed when the image file is copied from one disk to another. Supported Platforms Other than the Cisco 7600 Series Router Before loading or duplicating a new image, record the checksum and MD5 information for the image so that you can verify the checksum when you copy the image into flash memory or onto a server. A variety of image information is available on Cisco.com. For example, you can get the Release, Feature Set, Size, BSD Checksum, Router Checksum, MD5, and Publication Date information by clicking on the image file name prior to downloading it from the Software Center on Cisco.com. To display the contents of flash memory, use the show flash command. The flash contents listing does not include the checksum of individual files. To recompute and verify the image checksum after the image has been copied into flash memory, use the verify command. Note, however, that the verify command only performs a check on the integrity of the file after it has been saved in the file system. It is possible for a corrupt image to be transferred to the router and saved in the file system without detection. If a corrupt image is transferred successfully to the router, the software will be unable to tell that the image is corrupted and the file will verify successfully. To use the message-digest5 (MD5) hash algorithm to ensure file validation, use the verify command with the /md5 option. MD5 is an algorithm (defined in RFC 1321) that is used to verify data integrity through the creation of a unique 128-bit message digest. The /md5 option of the verify command allows you to check the integrity of a Cisco IOS software image by comparing its MD5 checksum value against a known MD5 checksum value for the image. MD5 values are now made available on Cisco.com for all Cisco IOS software images for comparison against local system image values. To perform the MD5 integrity check, issue the verify command using the /md5 keyword. For example, issuing the verify flash:c7200-is-mz.122-2.T.bin /md5command will calculate and display the MD5 value for the software image. Compare this value with the value available on Cisco.com for this image. Alternatively, you can get the MD5 value from Cisco.com first, then specify this value in the command syntax. For example, issuing the verify flash:c7200-is-mz.122-2.T.bin /md5 8b5f3062c4caeccae72571440e962233 command will display a message verifying that the MD5 values match or that there is a mismatch. A mismatch in MD5 values means that either the image is corrupt or the wrong MD5 value was entered. Cisco 7600 Series Router The Readme file, which is included with the image on the disk, lists the name, file size, and checksum of the image. Review the contents of the Readme file before loading or duplicating the new image so that you can verify the checksum when you copy it into the flash memory or onto a server. Use the verify /md5 command to verify the MD5 signature of a file before using it. This command validates the integrity of a copied file by comparing a precomputed MD5 signature with the signature that is computed by this command. If the two MD5 signatures match, the copied file is identical to the original file. You can find the MD5 signature that is posted on the Cisco.com page with the image. You can use the verify /md5 command in one of the following ways: • Verify the MD5 signatures manually by entering the verify /md5 filename command. Check the displayed signature against the MD5 signature that is posted on the Cisco.com page. • Allow the system to compare the MD5 signatures by entering the verify /md5 flash-filesystem:filenam expected-md5-signature command. After completing the comparison, the system returns with a verified message. If an error is detected, the output is similar to the following:

```text
Router# verify /md5 disk0:c6msfc2-jsv-mz 0f
Done
!
%Error verifying disk0:c6msfc2-jsv-mz
Computed signature = 0f369ed9e98756f179d4f29d6e7755d3
Submitted signature = 0f
```

To display the contents of the flash memory, enter the show flash command. The listing of the flash contents does not include the checksum of the individual files. To recompute and verify the image checksum after the image has been copied into the flash memory, enter the verify command. A colon (:) is required after the specified device.

**Example:**

Supported Platforms Other than Cisco 7600 Series Router The following example shows how to use the verify command to check the integrity of the file c7200-js-mz on the flash memory card inserted in slot 0:

```text
Router# dir slot0:
Directory of slot0:/
1 -rw- 4720148 Aug 29 1997 17:49:36 hampton/nitro/c7200-j-mz
2 -rw- 4767328 Oct 01 1997 18:42:53 c7200-js-mz
5 -rw- 639 Oct 02 1997 12:09:32 rally
7 -rw- 639 Oct 02 1997 12:37:13 the_time
20578304 bytes total (3104544 bytes free)
Router# verify slot0:c7200-js-mz
Verified slot0:c7200-js-mz
```

In the following example, the /md5 keyword is used to display the MD5 value for the image:

```text
Router# verify /md5 disk1:
Verify filename []? c7200-js-mz
Done
!
verify /md5 (disk1:c7200-js-mz) = 0f369ed9e98756f179d4f29d6e7755d3
```

In the following example, the known MD5 value for the image (obtained from Cisco.com) is specified in the verify command, and the system checks the value against the stored value:

```text
Router# verify /md5 disk1:c7200-js-mz ?
WORD Expected md5 signature
<cr>
router# verify /md5 disk1:c7200-js-mz 0f369ed9e98756f179d4f29d6e7755d3
Done
!
Verified (disk1:c7200-js-mz) = 0f369ed9e98756f179d4f29d6e7755d3
```

The following example shows how the output of the verify command was enhanced to show the hash value in addition to the entire hash image (CCO hash):

```text
Router# verify disk0:c7200-js-mz
%Filesystem does not support verify operations
Verifying file integrity of disk0:c7200-js-mz
Done
!
Embedded Hash MD5 :CFA258948C4ECE52085DCF428A426DCD
Computed Hash MD5 :CFA258948C4ECE52085DCF428A426DCD
CCO Hash MD5 :44A7B9BDDD9638128C35528466318183
Signature Verified
```

Cisco 7600 Series Router This example shows how to use the verify command:

```text
Router# verify cat6k_r47_1.cbi
File cat6k_r47_1.cbi verified OK.
```

This example shows how to check the MD5 signature manually:

```text
Router# verify /md5 c6msfc2-jsv-mz
Done
!
verify /md5 (disk0:c6msfc2-jsv-mz) = 0f369ed9e98756f179d4f29d6e7755d3
```

This example shows how to allow the system to compare the MD5 signatures:

```text
Router# verify /md5 disk0:c6msfc2-jsv-mz 0f369ed9e98756f179d4f29d6e7755d3
Done
!
verified /md5 (disk0:c6sup12-jsv-mz) = 0f369ed9e98756f179d4f29d6e7755d3
```

This example shows how to verify the compressed checksum of the Cisco IOS image:

```text
Router# verify /ios disk0:c6k222-jsv-mz
Verified compressed IOS image checksum for disk0:c6k222-jsv-mz
```


### `vtp`

> **Página:** 1150 · **Modo:** Global configuration (config) · **Default:** The defaults are as follows: • vtp domain and vtp interface co mmands have no default settings. • filename is const-nvram:vlan.dat . • VTP mode is mode server for VLANs and transparent for all other features. • No password is configured. • Pruning is disabled. • Administrative-domain VTP version number 1. · **Leitura (show/clear/…):** não

**Description:** To configure the global VLAN Trunking Protocol (VTP) state, use the vtp command in global configuration mode. To return to the default value, use the no form of this command.

**Syntax:**

```text
vtp {domain domain-name | file filename | interface interface-name [only] | mode {client | off | server
| transparent} {vlan | mst | unknown} | password password-value [hidden | secret] | pruning | version
{1 | 2 | 3}}
no vtp
```

**Parameters (Syntax Description):**

- `domaindomain-name` — Setsthe VTP a d min is t r at i v e domain name.
- `file file name` — Setsthe ASCII name of the IF S filesystem file where the VTP configuration is s to r e d.
- `interfaceinterface-name` — Set s then a m e of the pref e r r e d source for the VTP-u p d at e r ID for this device.
- `only` — ( Optional) Specifies to use only this interface’ s IP address as the VTP-IP u p d at e r address.
- `mode client` — Set s the type of VTP-device mode to client mode.
- `modeoff` — Set s the type of VTP-device mode to of fm o d e.
- `modes e r v e r` — Set s the type of VTP-device mode to server mode.
- `mode transparent` — Set s the type of VTP-device mode to transparent mode.
- `vlan` — Specifies VTP version3 VLAN in s t an c e s.
- `mst` — Specifies VTP version3 M S T in s t an c e s.
- `unknown` — Specifies VTP version3 for all other in s t an c e s.
- `passwordpassword-value` — Specifies the a d min is t r at i v e-domain password.
- `hidden` — ( Optional) Specifies that the VTP version3 s e c r e t k e y generate d from the password be save d in the c on s t_ nvram: vlan. datfile.
- `secret` — ( Optional) All o w s you to dir e c t l y configure the VTP version3 passwords e c r e t key.
- `pruning` — Enable s the a d min is t r at i v e domain to permit p r u n in g.
- `version {1|2|3}` — Specifies the a d min is t r at i v e-domain VTP version number.

**Command Default:** The defaults are as follows: • vtp domain and vtp interface co mmands have no default settings. • filename is const-nvram:vlan.dat . • VTP mode is mode server for VLANs and transparent for all other features. • No password is configured. • Pruning is disabled. • Administrative-domain VTP version number 1.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | This command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Cisco IOS Release 12.2(17d)SXB. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SXH | The mode of f keyword c o m b in at i on was added. |
| 12.2(33)SXI | Support for VTP version3 was added. |

**Usage Guidelines:**

Note The vtp pruning, vtp password, and vtp version commands are also available in privileged EXEC mode. We recommend that you use these commands in global configuration mode only; do not use these commands in privileged EXEC mode. Extended-range VLANs are not supported by VTP. When you define the domain-name value , the domain name is case sensitive and can be from 1 to 32 characters. The filename and interface-namevalues are ASCII strings from 1 to 255 characters. You must configure a password on each network device in the management domain when the switch is in secure mode. Caution If you configure VTP in secure mode, the management domain does not function properly if you do not assign a management domain password to each network device in the domain. A VTP version 2-capable network device can operate in the same VTP domain as a network device running VTP version 1 if VTP version 2 is disabled on the VTP version 2-capable network device (VTP version 2 is disabled by default). Do not enable VTP version 2 on a network device unless all of the network devices in the same VTP domain are version 2-capable. When you enable VTP version 2 on a network device, all of the version 2-capable network devices in the domain enable VTP version 2. In a Token Ring environment, you must enable VTP version 2 for VLAN switching to function properly. Enabling or disabling VTP pruning on a VTP server enables or disables VTP pruning for the entire management domain. Configuring VLANs as pruning eligible or pruning ineligible on a Cisco 7600 series router affects pruning eligibility for those VLANs on that switch only; it does not affect pruning eligibility on all network devices in the VTP domain. The vtp password, vtp pruning, and vtp version commands are not placed in startup memory but are included in the VTP transparent-mode startup configuration file. Extended-range VLANs are not supported by VTP. You can configure the pruning keyword in VTP-server mode; the version keyword is configurable in VTP-server mode or VTP transparent mode. The password-value argument is an ASCII string from 8 to 64 characters identifying the administrative domain for the device. VTP pruning causes information about each pruning-eligible VLAN to be removed from VTP updates if there are no stations belonging to that VLAN. All Cisco 7600 series routers in a VTP domain must run the same version of VTP. VTP version 1 and VTP version 2 do not operate on Cisco 7600 series routers in the same VTP domain. If all Cisco 7600 series routers in a domain are VTP version 2-capable, you need only to enable VTP version 2 on one Cisco 7600 series router; the version number is then propagated to the other version 2-capable Cisco 7600 series routers in the VTP domain. If you toggle the version 2 mode, certain default VLAN parameters are modified. If you enter the vtp mode off command, it sets the device to off. If you enter the no vtp mode off command, it resets the device to the VTP server mode. In VTP version 3, the VTP mode has to be specified on a per-feature basis. Use the vlan and mst keywords to configure the VTP mode on VLAN and MST instances. To configure the VTP mode for any other feature, use the unknown keyword. When you convert from either VTP version 1 or 2 to version 3, the current mode configuration will be preserved. With VTP version 3, a new method is available for hiding the VTP password from the configuration file. When you use the hidden keyword, the secret key that is generated from the password string is saved in the const_nvram:vlan.dat file. If you use the secret keyword, you can directly configure the password secret key. By using the secret keyword, you can distribute the password in the secret key format rather than in the cleartext format.

**Example:**

This example shows how to set the device’s management domain:

```text
Router(config)#
vtp domain DomainName1
```

This example shows how to specify the file in the IFS-file system where the VTP configuration is stored:

```text
Router(config)#
vtp file vtpconfig
Setting device to store VLAN database at filename vtpconfig.
```

This example shows how to set the VTP mode to client:

```text
Router(config)#
vtp mode client
Setting device to VTP CLIENT mode.
```

This example shows how to disable VTP mode globally:

```text
Router(config)# vtp mode off
Setting device to VTP OFF mode.
```

This example shows how to reset the device to the VTP server mode:

```text
Router(config)# no vtp mode off
Setting device to VTP OFF mode.
```


### `warm-reboot`

> **Página:** 1153 · **Modo:** Global configuration · **Default:** Warm rebooting is disabled. If warm rebooting is enabled, the default value for the count numberoption is 5 times, and the default value for the uptime minutes option is 5 minutes. · **Leitura (show/clear/…):** não

**Description:** To enable a router to do a warm-reboot, use the warm-rebootcommand in global configuration mode. To disable warm rebooting, use the no form of this command.

**Syntax:**

```text
warm-reboot [count number] [uptime minutes]
no warm-reboot count number uptime minutes
```

**Parameters (Syntax Description):**

- `count number` — ( Optional) Maximum number of warm reboot s all o we d be t we e n any in t e r v e n in g c o l d reboot. V a l id values range from1 to50. The default value is5 time s.
- `uptime minutes` — ( Optional) Min i m u m number of min u test h at must e l ap s e be t we e n in it i a l system configuration and an e x c e p t i on before a warm reboot is at t e m p t e d. If the system c r as h e s before the specified time e l ap s e s, a warm reboot is not at t e m p t e d. V a l id values range from0 to120. The default value is5 min u t e s.

**Command Default:** Warm rebooting is disabled. If warm rebooting is enabled, the default value for the count numberoption is 5 times, and the default value for the uptime minutes option is 5 minutes.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(2)T | This command was introduced. |
| 12.2(18)S | This command was integrated into Cisco IOS Release12.2(18) S. |
| 12.2(28)SB | This command was integrated into Cisco IOS R e l as e12.2(28) S B. |

**Usage Guidelines:**

Use the warm-rebootcommand to enable the router to reload a Cisco IOS image without ROM monitor mode (ROMMON) intervention, in which the image restores read-write data from a previously saved copy in the RAM and starts execution from that point. Unlike a cold reboot, this process does not involve a flash to RAM copy or self-decompression of the image. Note After a warm reboot is enabled, it will not become active until after the next cold reboot because a warm reboot requires a copy of the initialized memory. Note If the system crashes before the image completes the warm reboot process, a cold reboot is initiated.

**Example:**

The following example shows how to enable a warm reboot on the router:

```text
Router#(config)
warm-reboot count 10 uptime 10
```


### `where`

> **Página:** 1154 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To list the open sessions, use the wherecommand in EXEC mode.

**Syntax:**

```text
where
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced in are l e as e p r i or to Cisco IOS Release10.0. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The where command displays all open sessions associated with the current terminal line. The break (Ctrl-Shift-6, x), where, and resume commands are available with all supported connection protocols.

**Example:**

The following is sample output from the wherecommand:

```text
where
Conn Host Address Byte Idle Conn Name
1 MATHOM 192.31.7.21 0 0 MATHOM
* 2 CHAFF 131.108.12.19 0 0 CHAFF
```

The asterisk (*) indicates the current terminal session. The following table describes the fields shown in the display.

| Field | Description |
| --- | --- |
| Conn | Nameoraddressoftheremotehosttowhichtheconnectionismade. |
| Host | RemotehosttowhichtherouterisconnectedthroughaTelnetsession. |
| Address | IPaddressoftheremotehost. |
| Byte | Numberofunreadbytesfortheusertoseeontheconnection. |
| Idle | Interval(inminutes)sincedatawaslastsentontheline. |
| ConnName | Assignednameoftheconnection. |


### `width`

> **Página:** 1155 · **Modo:** Line configuration · **Default:** 80 character columns · **Leitura (show/clear/…):** não

**Description:** To set the terminal screen width, use the width command in line configuration mode. To return to the default screen width, use the no form of this command.

**Syntax:**

```text
width characters
no width
```

**Parameters (Syntax Description):**

- `characters` — Number of character columns d is p l a y e d on the terminal. The default is 80 characters.
- `characters` — Number of character c o l u m n s d is p l a y e do n the terminal. The default is80 characters.

**Command Default:** 80 character columns

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

By default, the route provides a screen display width of 80 characters. You can reset this value for the current session if it does not meet the needs of your terminal. The rlogin protocol uses the value of the characters argument to set up terminal parameters on a remote host.

**Example:**

In the following example the location for line 7 is defined as “console terminal” and the display is set to 132 columns wide:

```text
Router(config)# line 7
Router(config-line)# location console terminal
Router(config-line)# width 132
```


### `write core`

> **Página:** 1156 · **Modo:** Privileged EXEC · **Default:** If the hostname or destination arguments are not specified, the core dump file is written to the IP address or hostname specified by the exception dump command. If the LINE keyword is not specified, the name of the core dump file is assigned as the host name of the remote server followed by the word “-core.” · **Leitura (show/clear/…):** não

**Description:** To test the configuration of a core dump setup, use the write core command in privileged EXEC mode.

**Syntax:**

```text
write core [hostname [LINE] | destination-address [LINE]]
```

**Parameters (Syntax Description):**

- `hostname` — ( Optional) Hostname of the remote server where the core dump file is to be w r it t e n.
- `destination-address` — ( Optional) IP address of the remote server where the core dump file is to be w r it t e n.
- `LINE` — ( Optional) As s i g n s then a m e“ LINE” to the core dump file.

**Command Default:** If the hostname or destination arguments are not specified, the core dump file is written to the IP address or hostname specified by the exception dump command. If the LINE keyword is not specified, the name of the core dump file is assigned as the host name of the remote server followed by the word “-core.”

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(11)T | This command was introduced. |

**Usage Guidelines:**

When a router reloads, it is sometimes useful to obtain a full copy of the memory image (called a core dump) to identify the cause of the reload. Core dumps are generally useful to your technical support representative. Not all types of router reloads will produce a core dump. The write core command causes the router to generate a core dump without reloading, which may be useful if the router is malfunctioning but has not reloaded. The core dump files will be the size of the respective memory regions. It is important to remember that the entire memory region is dumped, not just the memory that is in use. Caution Use the write core command only under the direction of a technical support representative. Creating a core dump while the router is functioning in a network can disrupt network operation. When using this command, the router will not reload until the content of its memory is dumped. This event might take some time, depending on the amount of DRAM present on the router. Also, the resulting binary file, which is very large, must be transferred to a Trivial File Transfer Protocol (TFTP), File Transfer Protocol (FTP), or remote copy protocol (rcp) server and subsequently interpreted by technical personnel who have access to source code and detailed memory maps. Depending on your TFTP server, you might need to create an empty target file to which the router can write the core dump.

**Example:**

The following example shows how to test the configuration of a core dump setup. In this example, the core dump file is written to the remote server with the host name test.

```text
write core test
```


The write erase command is replaced by the erase nvram: command. See the description of the erasecommand for more information.

### `write memory`

> **Página:** 1157 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To save the running configuration to the nonvolatile random-access memory (NVRAM), use the write memory command in privileged EXEC mode.

**Syntax:**

```text
write memory
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(11)T | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release 12.2(11)T. |
| 12.2(14)SX | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(14)SX. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1. |

**Usage Guidelines:**

If you try to configure the write memory command when a router is low on memory and the backup buffer cannot be allocated, then the command will fail with the error message, “Not enough space.” When the write memory command fails to apply the new configuration, the backup configuration is used to restore the original configuration.

**Example:**

The following example shows how to save the running configuration to NVRAM:

```text
Router>
enable
write memory
```


### `write mib-data`

> **Página:** 1158 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To save MIB data to system memory (NVRAM) for MIB Data Persistence, use the write mib-datacommand in EXEC mode.

**Syntax:**

```text
write mib-data
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release 15.0(1)M. |
| 12.2(33)SRC | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRC. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was i m p l e m e n t e do n the Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Usage Guidelines:**

The MIB Data Persistence feature allows the SNMP data of a MIB to be persistent across reloads; that is, the values of certain MIB objects are retained even if your networking device reboots. To determine which MIBs support “MIB Persistence” in your release, use the snmp mib persist command in global configuration mode. Any modified MIB data must be written to NVRAM memory using the write mib-data command. If the write mib-data command is not used, modified MIB data is not saved automatically, even if MIB Persistence is enabled. Executing the write mib-data command saves only the current MIB data; if the MIB object values are changed, you should reenter the write mib-data command to ensure that those values are persistent across reboots.

**Example:**

The following example shows the enabling of event MIB persistence, circuit MIB persistence, and saving the changes to set object values for these MIBs to NVRAM:

```text
Router# configure terminal
Router(config)# snmp mib persist circuit
Router(config)# snmp mib persist event
Router(config)# end
Router# write mib-data
```


### `write network`

> **Página:** 1159 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** Note This command has been replaced by copy system:/running-config command. To upload the current configuration to the network, use the write network command in privileged EXEC mode.

**Syntax:**

```text
write network [host-file-address]
```

**Parameters (Syntax Description):**

- `host-file-address` — ( Optional) Address of the host file to be u p load e d.
- `host-file-address` — ( Optional) Address of the host file to be u p load e d.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release 15.0(1)M. |
| 12.2(33)SRC | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRC. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was i m p l e m e n t e do n the Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Usage Guidelines:**

The write network command cannot be used to upload software to the ATM module.

**Example:**

This example shows how to upload the system5.cfg file to the mercury host using the write network command:

```text
Router# write network
IP address or name of host? mercury
Name of configuration file to write? system5.cfg
Upload configuration to system5.cfg on mercury (y/n) [y]? y
/
Done. Finished Network Upload. (9003 bytes)
```


### `write terminal`

> **Página:** 1160 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** This command is deprecated. Deprecated commands are considered obsolete, and their use is discouraged. Support for this command may be removed. The write terminal command is now enabled only as a command alias for the show running-config command. The show running-config command offers additional options not available for the write terminal command; see the documentation of the show running-config command for details.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 8.0 | This command was introduced in are l e as e p r i or to8.0. |
| 11.0 | The show running-config command was introduced as are p l a c e m e n t for the write terminal command. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |


### `xmodem`

> **Página:** 1160 · **Modo:** ROM monitor · **Default:** Xmodem protocol with 8-bit CRC, file downloaded into Flash memory and executed on completion. · **Leitura (show/clear/…):** não

**Description:** To copy a Cisco IOS image to a router using the ROM monitor and the Xmodem or Ymodem protocol, use the xmodem command in ROM monitor mode.

**Syntax:**

```text
xmodem [-c] [-y] [-e] [-f] [-r] [-x] [[-s] data-rate] [filename]
```

**Parameters (Syntax Description):**

- `-c` — ( Optional) C R C-16 check s u m min g, which is more s o p h is t i c at e d and t h or o u g h than s t and a r d check s u m min g.
- `-y` — ( Optional) Uses the Ymodem p r o to c o l for h i g h e r t h r o u g h p u t.
- `-e` — ( Optional) Erase s the first partition in Flash memory before starting the download. This option is only v a l id for the Cisco1600 s e r i e s.
- `-f` — ( Optional) Erase s all of Flash memory before starting the download. This option is only v a l id forthe Cisco1600 s e r i e s.
- `-r` — ( Optional) Download s the file to DRAM. The default is Flash memory.
- `-x` — ( Optional) Do note x e c u t e Cisco IOS image on c o m p l e t i on of the download.
- `-s data-rate` — ( Optional) Set s the c on s o l e port’ s data r at e d u r in g file t r an s f e r. Values are1200,2400,4800, 9600,19200,38400,and115200bps. The default r at e is specified in the configuration register. This option is only v a l id for the Cisco1600 s e r i e s.
- `file name` — ( Optional) File name to copy. This argument is i g nor e d when the-r keyword is specified, be cause only one file can be c o p i e d to DRAM. Onthe Cisco1600 s e r i e s routers, files are load e d to the ROM for exec u t i on.

**Command Default:** Xmodem protocol with 8-bit CRC, file downloaded into Flash memory and executed on completion.

**Command Modes:** ROM monitor

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2P | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The Cisco 3600 series routers does not support XBOOT functionality. If your Cisco IOS image is erased or damaged, you cannot load a new image over the network. Use the xmodem ROM monitor command to download a new system image to your router from a local personal computer (such as a PC, Mac, or UNIX workstation), or a remote computer over a modem connection, to the router’s console port. The computer must have a terminal emulation application that supports these protocols. Cisco 3600 Series Routers Your router must have enough DRAM to hold the file being transferred, even if you are copying to Flash memory. The image is copied to the first file in internal Flash memory. Any existing files in Flash memory are erased. There is no support for partitions or copying as a second file. Cisco 1600 Series Routers If you include the option, your router must have enough DRAM to hold the file being transferred. To run -r from Flash, an image must be positioned as the first file in Flash memory. If you are copying a new image to boot from Flash, erase all existing files first. Caution A modem connection from the telephone network to your console port introduces security issues that you should consider before enabling the connection. For example, remote users can dial in to your modem and access the router’s configuration settings. Note If the file to be downloaded is not a valid router image, the copy operation is automatically terminated.

**Example:**

The following example uses the xmodem -c filename ROM monitor command to copy the file named new-ios-image from a remote or local computer:

```text
rommon > xmodem -c new-ios-image
Do not start the sending program yet...
File size Checksum File name
1738244 bytes (0x1a8604) 0xdd25 george-admin/c3600-i-mz
WARNING: All existing data in bootflash will be lost!
Invoke this application only for disaster recovery.
Do you wish to continue? y/n [n]: yes
Ready to receive file new-ios-image ...
```
