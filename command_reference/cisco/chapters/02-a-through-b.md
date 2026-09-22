# Capítulo 2: A through B

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## Introduction

### A through B

• A through B, on page 6

### A through B

### `activation-character`

> **Página:** 30 · **Modo:** Line configuration (config-line) · **Default:** Return (decimal 13) · **Leitura (show/clear/…):** não

**Description:** To define the character you enter at a vacant terminal to begin a terminal session, use the activation-character command in line configuration mode. To make any character activate a terminal, use the no form of this command.

**Syntax:**

```text
activation-character ascii-number
no activation-character
```

**Parameters (Syntax Description):**

- `ascii-number` — Decimal representation of the activation character.

**Command Default:** Return (decimal 13)

**Command Modes:** Line configuration (config-line)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. This command is supported in all Cisco IOS software Releases. |

**Usage Guidelines:**

See the “ASCII Character Set and Hexadecimal Values” document for a list of ASCII characters. Note If you are using the autoselect function, set the activation character to the default, Return, and exec-character-bits to 7. If you change these defaults, the application will not recognize the activation request.

**Example:**

The following example shows how to set the activation character for the console to Delete, which is decimal character 127:

```text
Router(config)# line console
Router(config-line)#
activation-character 127
```


### `alias`

> **Página:** 30 · **Modo:** Global configuration · **Default:** A set of six basic EXEC mode aliases are enabled by default. See the “Usage Guidelines” section of this command for a list of default aliases. · **Leitura (show/clear/…):** não

**Description:** To create a command alias, use the alias command in global configuration mode. To delete all aliases in a command mode or to delete a specific alias, and to revert to the original command syntax, use the no form of this command.

**Syntax:**

```text
alias mode command-alias original-command
no alias mode [command-alias]
```

**Parameters (Syntax Description):**

- `mode` — Command mode of the original and alias commands.
- `command-alias` — Command alias.
- `original-command` — Original commands y n t a x.

**Command Default:** A set of six basic EXEC mode aliases are enabled by default. See the “Usage Guidelines” section of this command for a list of default aliases.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 15.0M | The command alias ip-vrf has been replaced with alias vrf-a f. |

**Usage Guidelines:**

You can use simple words or abbreviations as command aliases. The table below lists the basic EXEC mode aliases that are enabled by default.

| CommandAlias | OriginalCommand |
| --- | --- |
| h | help |
| lo | logout |
| p | ping |
| r | resume |
| s | show |
| w | where |

The default aliases in the table above are predefined. These default aliases can be disabled with the no alias exec command. Common keyword aliases (which cannot be disabled) include running-config (keyword alias for system:running-config) and startup-config (keyword alias for nvram:startup-config). See the description of the copy command for more information about these keyword aliases. Note that aliases can be configured for keywords instead of entire commands. You can create, for example, an alias for the first part of any command and still enter the additional keywords and arguments as normal. To determine the value for the mode argument, enter the command mode in which you would issue the original command (and in which you will issue the alias) and enter the ? command. The name of the command mode should appear at the top of the list of commands. For example, the second line in the following sample output shows the name of the command mode as “Interface configuration”:

```text
Router# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)# interface e0
Router(config-if)# ?
Interface configuration commands:
access-expression Build a bridge boolean access expression
```

To match the name of the command mode to the acceptable mode keyword for the alias command, issue the alias ? command. As shown in the following sample output, the keyword needed to create a command alias for the access-expression command is interface:

```text
Router(config)# alias ?
accept-dialin VPDN group accept dialin configuration mode
accept-dialout VPDN group accept dialout configuration mode
address-family Address Family configuration mode
call-discriminator Call Discriminator Configuration
cascustom Cas custom configuration mode
clid-group CLID group configuration mode
configure Global configuration mode
congestion Frame Relay congestion configuration mode
controller Controller configuration mode
cptone-set custom call progress tone configuration mode
customer-profile customer profile configuration mode
dhcp DHCP pool configuration mode
dnis-group DNIS group configuration mode
exec Exec mode
flow-cache Flow aggregation cache config mode
fr-fr FR/FR connection configuration mode
interface Interface configuration mode
Router(config)# alias interface express access-expression
```

When you use online help, command aliases are indicated by an asterisk (*), and displayed in the following format: *command-alias =original-command For example, the lo command alias is shown here along with other EXEC mode commands that start with “lo”:

```text
Router# lo?
*lo=logout lock login logout
```

When you use online help, aliases that contain multiple keyword elements separated by spaces are displayed in quotes, as shown here:

```text
Router(config)#alias exec device-mail telnet device.cisco.com 25
Router(config)#end
Router#device-mail?
*device-mail=”telnet device.cisco.com 25"
```

To list only commands and omit aliases, begin your input line with a space. In the following example, the alias td is not shown, because there is a space before the t?command line.

```text
Router(config)#alias exec td telnet device
Router(config)#end
Router# t?
telnet terminal test tn3270 trace
```

To circumvent command aliases, use a space before entering the command. In the following example, the command alias express is not recognized because a space is used before the command.

```text
Router(config-if)#exp?
*express=access-expression
Router(config-if)# express ?
% Unrecognized command
```

As with commands, you can use online help to display the arguments and keywords that can follow a command alias. In the following example,the alias td is created to represent the command telnet device. The /debugand /lineswitchescan be added to telnet device to modify the command:

```text
Router(config)#alias exec td telnet device
Router(config)#end
Router#td ?
/debug Enable telnet debugging mode
/line Enable telnet line mode
...
whois Whois port
<cr>
telnet device
```

You must enter the complete syntax for the command alias. Partial syntax for aliases is not accepted. In the following example, the parser does not recognize the command t as indicating the alias td:

```text
Router# t
% Ambiguous command: “t”
```

**Example:**

In the following example, the alias fixmyrtis configured for the clear iproute 192.168.116.16 EXEC mode command:

```text
Router(config)#
alias exec fixmyrt clear ip route 192.168.116.16
```

In the following example, the alias express is configured for the first part of the access-expression interface configuration command:

```text
Router#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#
interface e0
Router(config-if)#
?
Interface configuration commands:
access-expression Build a bridge boolean access expression
Router(config-if)#exit
Router(config)#alias ?
accept-dialin VPDN group accept dialin configuration mode
accept-dialout VPDN group accept dialout configuration mode
address-family Address Family configuration mode
call-discriminator Call Discriminator Configuration
cascustom Cas custom configuration mode
clid-group CLID group configuration mode
configure Global configuration mode
congestion Frame Relay congestion configuration mode
controller Controller configuration mode
cptone-set custom call progress tone configuration mode
customer-profile customer profile configuration mode
dhcp DHCP pool configuration mode
dnis-group DNIS group configuration mode
exec Exec mode
flow-cache Flow aggregation cache config mode
fr-fr FR/FR connection configuration mode
interface Interface configuration mode
Router(config)#alias interface express access-expression
Router(config)#int e0
Router(config-if)#exp?
*express=access-expression
Router(config-if)#express ?
input Filter input packets
output Filter output packets
!Note that the true form of the command/keyword alias appears on the screen after issuing
!the express ? command.
Router(config-if)#
access-expression ?
input Filter input packets
output Filter output packets
Router(config-if)#ex?
*express=access-expression exit
!Note that in the following line, a space is used before the ex? command
!so the alias is not displayed.
Router(config-if)# ex?
exit
!Note that in the following line, the alias cannot be recognized because
!a space is used before the command.
Router#(config-if)# express ?
% Unrecognized command
Router(config-if)# end
show alias interface
Interface configuration mode aliases:
express access-expression
```


### `archive`

> **Página:** 34 · **Modo:** Global configuration (config) · **Default:** Archive configuration mode is not entered. · **Leitura (show/clear/…):** não

**Description:** To enter archive configuration mode, use the archive command in global configuration mode.

**Syntax:**

```text
archive
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Archive configuration mode is not entered.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(4)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Example:**

The following example shows how to place the device in archive configuration mode:

```text
Device# configure terminal
!
Device(config)# archive
Device(config-archive)#
```


### `archive config`

> **Página:** 35 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To save a copy of the current running configuration to the Cisco configuration archive, use the archive config command in privileged EXEC mode.

**Syntax:**

```text
archive config
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

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
| CiscoIOSXERelease3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Note Before using this command, you must configure the path command in order to specify the location and filename prefix for the files in the Cisco configuration archive. The Cisco configuration archive is intended to provide a mechanism to store, organize, and manage an archive of Cisco configuration files to enhance the configuration rollback capability provided by the configure replace command. Before this feature was introduced, you could save copies of the running configuration using the copy running-config destination-url command, storing the target file either locally or remotely. However, this method lacked any automated file management. On the other hand, the Configuration Replace and Configuration Rollback feature provides the capability to automatically save copies of the running configuration to the Cisco configuration archive. These archived files serve as checkpoint configuration references and can be used by the configure replace command to revert to previous configuration states. The archive config command allows you to save Cisco configurations in the configuration archive using a standard location and filename prefix that is automatically appended with an incremental version number (and optional time stamp) as each consecutive file is saved. This functionality provides a means for consistent identification of saved Cisco configuration files. You can specify how many versions of the running configuration are kept in the archive. After the maximum number of files has been saved in the archive, the oldest file is automatically deleted when the next, most recent file is saved. The show archive command displays information for all configuration files saved in the Cisco configuration archive.

**Example:**

The following example shows how to save the current running configuration to the Cisco configuration archive using the archive config command. Before using the archive config command, you must configure the path command to specify the location and filename prefix for the files in the Cisco IOS configuration archive. In this example, the location and filename prefix are specified as disk0:myconfig as follows:

```text
configure terminal
!
archive
path disk0:myconfig
end
```

You then save the current running configuration in the configuration archive, as follows:

```text
archive config
```

The show archive command displays information on the files saved in the configuration archive as shown in the following sample output:

```text
Device# show archive
There are currently 1 archive configurations saved.
The next archive file will be named disk0:myconfig-2
Archive # Name
1 disk0:myconfig<timestamp>-1
```


### `archive log config persistent save`

> **Página:** 37 · **Modo:** Privileged EXEC (#). · **Default:** If this command is not entered, the persisted configuration commands in the archive log are not saved to the Cisco IOS secure file system. · **Leitura (show/clear/…):** não

**Description:** To save the persisted commands in the configuration log to the Cisco IOS secure file system, use the archive log config persistent save command in privileged EXEC mode.

**Syntax:**

```text
archive log config persistent save
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** If this command is not entered, the persisted configuration commands in the archive log are not saved to the Cisco IOS secure file system.

**Command Modes:** Privileged EXEC (#).

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRA | This command was introduced. |
| 12.4(11)T | This command was integrated into Cisco IOS Release12.4(11) T. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B. |

**Usage Guidelines:**

If the router is in the persistent periodic mode, the persistent timer is restarted.

**Example:**

The following example saves the persisted commands in the archive log to the Cisco IOS secure file system:

```text
Router# archive log config persistent save
```


### `archive tar`

> **Página:** 38 · **Modo:** Privileged EXEC (#) · **Default:** The TAR archive file is not created. · **Leitura (show/clear/…):** não

**Description:** To create a TAR file, to list files in a TAR file, or to extract the files from a TAR file, use the archive tar command in privileged EXEC mode. /

**Syntax:**

```text
archive tar {/create destination-urlflash: file-url | /table source-url | /xtract source-urlflash:/file-url
[dir/file...]}
```

**Parameters (Syntax Description):**

- `/create destination-url flash:/ file-url` — C r e at e s an e w TAR file on the l o c a l or network filesystem. For destination-url, specify the destination URL alias for the l o c a l or network file system and then a m e of the TAR file to c r e at e. The following options are supported: • flash:--Syntax for the l o c a l flash filesystem. • ftp:[[// username[: password]@ location]/ directory]/ tar-file name. tar--Syntax for FTP. • rcp:[[// username@ location]/ directory]/ tar-file name. tar--Syntax for Remote Copy P r o to c o l( RCP). • tftp:[[// location]/ directory]/ tar-file name. tar--Syntax for TFTP. The tar-file name. tar is then a m e of the TAR file to be c r e at e d. For flash:/ file-url, specify the location on the l o c a l flash filesystem from which the new TAR file is c r e at e d. An optional list of files or dir e c to r i e s with in the source directory can be specified to write to then e w TARfile. If none is specified, all files and dir e c to r i e s at this level are w r it t e n to then e w l y c r e at e d TARfile.
- `/table source-url` — D is p l a y the c on t e n t s of an e x is t in g TAR file to the screen. For source-url, specify the source URL alias for the l o c a l or network filesystem. The following options are supported: • flash:--Syntax for the l o c a l flash filesystem. • ftp:[[// username[: password]@ location]/ directory]/ tar-file name. tar--Syntax for FTP. • rcp:[[// username@ location]/ directory]/ tar-file name. tar--Syntax for Remote Copy P r o to c o l( RCP). • tftp:[[// location]/ directory]/ tar-file name. tar--Syntax for TFTP. The tar-file name. tar is then a m e of the TAR file to be c r e at e d.
- `/xtract source-url flash:/ file-url [ dir/ file...]` — E x t r a c t s files from a TAR file to the l o c a l filesystem. For source-url, specify the source URL alias for the l o c a l filesystem. These options are supported: • flash:--Syntax for the l o c a l flash filesystem. • ftp:[[// username[: password]@ location]/ directory]/ tar-file name. tar--Syntax for FTP. • rcp:[[// username@ location]/ directory]/ tar-file name. tar--Syntax for Remote Copy P r o to c o l( RCP). • tftp:[[// location]/ directory]/ tar-file name. tar--Syntax for TFTP. The tar-file name. tar is then a m e of the TAR file to be c r e at e d.

**Command Default:** The TAR archive file is not created.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.1(13)AY | This command was introduced. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.4(22)YB | This command was integrated into Cisco IOS Release12.4(22) Y B. |
| 12.4(24)T | This command was integrated into Cisco IOS Release12.4(24) T. |

**Usage Guidelines:**

Filenames, directory names, and image names are case sensitive. The TAR file is an archive file from which you can extract files by using the archive tarcommand.

**Example:**

The following example shows how to create a TAR file. The command writes the contents of the new-configs directory on the local flash device to a file named saved.tar on the TFTP server at 172.20.136.9.

```text
Switch# archive tar /create tftp:172.20.136.9/saved.tar flash:/new-configs
```

The following example shows how to display the contents of the c2940-tv0-m.tar file that is in flash memory. The contents of the TAR file appear on the screen.

```text
Switch# archive tar /table flash:c2940-tv0-m.tar
info (219 bytes)
c2940-tv0-mz-121/ (directory)
c2940-tv0-mz-121/html/ (directory)
c2940-tv0-mz-121/html/foo.html (0 bytes)
c2940-tv0-mz-121/vegas-tv0-mz-121.bin (610856 bytes)
c2940-tv0-mz-121/info (219 bytes)
info.ver (219 bytes)
```

The following example shows how to extract the contents of a TAR file on the TFTP server at 172.20.10.30. This command extracts only the new-configs directory into the root directory on the local flash file system. The remaining files in the saved.tar file are ignored.

```text
Switch# archive tar /xtract tftp:/172.20.10.30/saved.tar flash:/ new-configs
```


### `async-bootp`

> **Página:** 40 · **Modo:** Global configuration · **Default:** If no extended BOOTP commands are entered, the Cisco IOS software generates a gateway and subnet mask appropriate for the local network. · **Leitura (show/clear/…):** não

**Description:** To configure extended BOOTP requests for asynchronous interfaces as defined in RFC 1084, use the

**Syntax:**

```text
async-bootp command in global configuration mode. To restore the default, use the noform of this command.
async-bootp tag [:hostname] data
no async-bootp
```

**Parameters (Syntax Description):**

- `tag` — It e m being request e d; e x p r e s s e d as file name, integer, or IP do t t e d decimal address. Seethe t a b l e be low for p o s s i b l e keywords.
- `: hostname` — ( Optional) This entry ap p l i e s only to the specified host. The: hostname argument accept s both an IP address and a log i c a l hostname.
- `data` — Listof IP address e s enter e d in do t t e d decimal not at i on or as log i c a l hostname s, an u m be r, or a q u o t e d string.
- `boot file` — Specifies use of as e r v e r boot file from which to download the bootp r o g r a m. Use the optional: hostname argument and the data argument to specify the file name.
- `subnet-mask mask` — Do t t e d decimal address specify in gt h e network and l o c a l s u b network mask( as define d by RFC950).
- `time-of f set offset` — S i g n e d32-b it integer specify in gt h e time of f set of the l o c a l s u b network in s e c on d s from C o or d in at e d U n i v e r s a l Time(UTC).
- `gateway address` — Do t t e d decimal address specify in gt h e IP address e s of g at e w a y s for this s u b network. Ap r e f e r r e d g at e w a y should be list e d first.
- `time-server address` — Do t t e d decimal address specify in gt h e IP address of time servers( as define d by RFC868).
- `I E N116-server address` — Do t t e d decimal address specify in gt h e IP address of names e r v e r s( as define d by IEN116).
- `n b n s-server address` — Do t t e d decimal address specify in gt h e IP address of Windows N T servers.
- `D N S-server address` — Do t t e d decimal address specify in gt h e IP address of domain names e r v e r s( as define d by RFC1034).
- `log-server address` — Do t t e d decimal address specify in gt h e IP address of an MIT-LCSUDPlog server.
- `q u o t e-server address` — Do t t e d decimal address specify in gt h e IP address of Q u o t e of the Days e r v e r s ( as define d in RFC865).
- `l p r-server address` — Do t t e d decimal address specify in gt h e IP address of Be r k e l e y U N I X Version4 B S D servers.
- `i m p r e s s-server address` — Do t t e d decimal address specify in gt h e IP address of I m p r e s s network image servers.
- `r l p-server address` — Do t t e d decimal address specify in gt h e IP address of Resource Location P r o to c o l ( R L P) servers( as define d in RFC887).
- `hostname name` — Then a m e of the client, which may or may not be domain q u a l if i e d, d e p end in g upon the s it e.
- `bootfile-size value` — At w o-o c t e t values p e c if y in gt h e number of512-o c t e t( by t e) b lock s in the default boot file.

**Command Default:** If no extended BOOTP commands are entered, the Cisco IOS software generates a gateway and subnet mask appropriate for the local network.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use the show async-bootp EXEC command to list the configured parameters. Use the no async-bootp command to clear the list.

**Example:**

The following example illustrates how to specify different boot files: one for a PC, and one for a Macintosh. With this configuration, a BOOTP request from the host on 172.30.1.1 results in a reply listing the boot filename as pcboot. A BOOTP request from the host named “mac” results in a reply listing the boot filename as “macboot.”

```text
async-bootp bootfile :172.30.1.1 “pcboot”
async-bootp bootfile :mac “macboot”
```

The following example specifies a subnet mask of 255.255.0.0:

```text
async-bootp subnet-mask 255.255.0.0
```

The following example specifies a negative time offset of the local subnetwork of 3600 seconds:

```text
async-bootp time-offset -3600
```

The following example specifies the IP address of a time server:

```text
async-bootp time-server 172.16.1.1
```


### `attach`

> **Página:** 42 · **Modo:** Privileged EXEC · **Default:** No default behavior or values. · **Leitura (show/clear/…):** não

**Description:** To connect to a specific line card or module from a remote location for the purpose of executing monitoring and maintenance commands on that line card or module, use the attach command in privileged EXEC mode. To exit from the Cisco IOS software image on the line card and return to the Cisco IOS image on the main (Supervisor) module, use the exit command. Cisco 12000 Series Cisco 7600 Series and Catalyst 6500 Series

**Syntax:**

```text
attach slot-number
attach module-number
```

**Parameters (Syntax Description):**

- `slot-number` — Slot number of the line card to which you w is h to c on n e c t. If you o m it the slot number, you will be prompt e d for it.
- `module-number` — Module number; see the“ Usage Guidelines” section for v a l id values.

**Command Default:** No default behavior or values.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2GS | This command was introduced on the Cisco12000 s e r i e s. |
| 12.2(14)SX | This command was i m p l e m e n t e do n the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support was added for the Supervisor Engine2. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Cisco 12000 Series You must first use the attach privileged EXEC command to access the Cisco IOS software image on a line card before using line card-specific show EXEC commands. Alternatively, you can use the execute-on privileged EXEC command to execute a show command on a specific line card. After you connect to the Cisco IOS image on the line card using the attach command, the prompt changes to LC-Slotx# , where x is the slot number of the line card. The commands executed on the line card use the Cisco IOS image on that line card. You can also use the execute-on slot privileged EXEC command to execute commands on one or all line cards. Do not execute the configEXEC command from the Cisco IOS software image on the line card. Cisco 7600 Series and Catalyst 6500 Series Caution After you enter the attach or remote login command to access another console from your switch, if you enter global or interface configuration mode commands, the switch might reset. The v alid values for the module-number argument depend on the chassis that is used. For example, if you have a 13-slot chassis, valid values for the module number are from 1 to 13. This command is supported on Distributed Forwarding Card (DFC)-equipped modules, FlexWan modules, and the supervisor engine only. When you execute the attach module-number command, the prompt changes to Router-dfcx# or Switch-sp#, depending on the type of module to which you are connecting. The behavior of the attach command is identical to that of the remote login module numcommand. There are two ways to end this session: • You can enter the exit command as follows:

```text
Router-dfc3# exit
[Connection to Switch closed by foreign host]
```

• You can press Ctrl-C three times as follows:

```text
Router-dfc3# ^C
Router-dfc3# ^C
Router-dfc3# ^C
Terminate remote login session? [confirm] y
[Connection to Switch closed by local host]
```

**Example:**

In the following example, the user connects to the Cisco IOS image running on the line card in slot 9, gets a list of valid show commands, and returns the Cisco IOS image running on the GRP:

```text
Router# attach 9
Entering Console for 4 Port Packet Over SONET OC-3c/STM-1 in Slot: 9
Type exit to end this session
Press RETURN to get started!
LC-Slot9# show ?
cef Cisco Express Forwarding
clock Display the system clock
context Show context information about recent crash(s)
history Display the session command history
hosts IP domain-name, lookup style, nameservers, and host table
ipc Interprocess communications commands
location Display the system location
sessions Information about Telnet connections
terminal Display terminal configuration parameters
users Display information about terminal lines
version System hardware and software status
LC-Slot9# exit
Disconnecting from slot 9.
Connection Duration: 00:01:04
```

Note Because not all statistics are maintained on line cards, the output from some of show commands may be inconsistent. The following example shows how to log in remotely to the DFC-equipped module:

```text
Console#
attach 3
Trying Switch ...
Entering CONSOLE for Switch
Type "^C^C^C" to end this session
Router-dfc3#
```


### `autobaud`

> **Página:** 45 · **Modo:** Line configuration · **Default:** Autobaud detection is disabled. Fixed speed of 9600 bps. · **Leitura (show/clear/…):** não

**Description:** To set the line for automatic baud rate detection (autobaud), use the autobaudcommand in line configuration mode. To disable automatic baud detection, use the noform of this command.

**Syntax:**

```text
autobaud
no autobaud
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Autobaud detection is disabled. Fixed speed of 9600 bps.

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The autobaud detection supports a range from 300 to 19200 baud. A line set for autobaud cannot be used for outgoing connections, nor can you set autobaud capability on a line using 19200 baud when the parity bit is set (because of hardware limitations). Note Automatic baud detection must be disabled by using the no autobaud command prior to setting the txspeed, rxspeed, or speed commands.

**Example:**

In the following example, the auxiliary port is configured for autobaud detection:

```text
Router(config)# line aux
Router(config-line)# autobaud
```

Related Topics auto-sync, on page 22 autoupgrade disk-cleanup, on page 24 autoupgrade ida url, on page 25 autoupgrade status email, on page 26


### `auto-sync`

> **Página:** 46 · **Modo:** Redundancy configuration (config-r) Main CPU redundancy configuration (config-r-mc) · **Default:** For the Performance Routing Engines (PREs) on the Cisco uBR10012 universal broadband router, the system defaults to synchronizing all system files on the (auto-sync standard). For the Supervisor Engines on the Cisco 7600 series routers, the system defaults to synchronizing the running configuration. (running-config). At the Cisco RF Gateway 10 chassis level, all the system files are synchronized by default. · **Leitura (show/clear/…):** não

**Description:** To enable automatic synchronization of the configuration files in NVRAM, use the auto-sync command in main-cpu redundancy configuration mode. To disable automatic synchronization, use the no form of this command.

**Syntax:**

```text
auto-sync {startup-config | config-register | bootvar | running-config | standard}
no auto-sync {startup-config | config-register | bootvar | standard}
```

**Parameters (Syntax Description):**

- `startup-config` — Specifies sync h r on i z at i on of the startup configuration files.
- `config-register` — Specifies sync h r on i z at i on of the configuration register values.
- `bootvar` — Specifies sync h r on i z at i on of the following bootvar i a b l e s: • BOOT--Set by the boot system device: file name command. • CONFIG_ FILE--Set by the boot config device: file name command. • BOOTLDR--Set by the boot bootldr device: file name command.
- `running-config` — Specifies sync h r on i z at i on of the running configuration files.
- `s t and a r d` — Specifies sync h r on i z at i on of all of the system files( startup configuration, bootvar i a b l e s, and config configuration register s).

**Command Default:** For the Performance Routing Engines (PREs) on the Cisco uBR10012 universal broadband router, the system defaults to synchronizing all system files on the (auto-sync standard). For the Supervisor Engines on the Cisco 7600 series routers, the system defaults to synchronizing the running configuration. (running-config). At the Cisco RF Gateway 10 chassis level, all the system files are synchronized by default.

**Command Modes:** Redundancy configuration (config-r) Main CPU redundancy configuration (config-r-mc)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(4)XF1 | This command was introduced on the Ciscou B R10012 u n i v e r s a l b r o a d b and router. |
| 12.2(14)SX | This command was integrated into the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support was added for the Supervisor Engine2. |
| 12.2(18)SXD | Support for this command on the Cisco7600 s e r i e s routers was removed. |
| 12.3BC | This command was integrated into Cisco IOS Release12.3 B C for the Ciscou BR10012 router. |
| 12.2(33)SCA | This command is o b s o l e t e on the Ciscou B R10012 u n i v e r s a l b r o a d b and router. |
| 12.2(44)SQ | This command was integrated into Cisco IOS Release12.2(44) S Q. Support for the Cisco R F G at e w a y10 was added. |

**Usage Guidelines:**

Cisco 7600 Series Routers If you enter the no auto-sync standard command, no automatic synchronizations occur. If you want to enable any of the keywords, you have to enter the appropriate command for each keyword. The auto-synccommand is not supported in RPR+ mode. Cisco uBR10012 Universal Broadband Router By default, the system synchronizes all system files, which is the typical setting for most applications. However, you might want exclude certain files from synchronization for specialized applications. For example, if you have configured the active and standby PRE1 (or PRE2) modules to run different versions of Cisco IOS software, you might want to use different configuration files as well. In this case, you would not synchronize the startup configuration file. Cisco RF Gateway 10 We recommend that you use the auto-sync standard command to ensure that all system files are synchronized between the two Supervisor modules. The no auto-sync command is not used in production plants.

**Example:**

Cisco 7600 Series Routers The following example shows how (from the default configuration) to enable automatic synchronization of the configuration register in the main CPU:

```text
configure terminal
Router (config)#
redundancy
Router (config-r)#
main-cpu
Router (config-r-mc)#
no auto-sync standard
Router (config-r-mc)#
auto-sync config-register
```

Cisco uBR10012 Universal Broadband Router The following example shows the system being configured to synchronize only the startup configuration file:

```text
router(config)# redundancy
router(config-r)# main-cpu
router(config-r-mc)# auto-sync startup-config
router(config-r-mc)# exit
router(config-r)# exit
```

The following example shows how to configure the system to synchronize all system files except for the startup configuration file. This typically is done when the two PRE1 (or PRE2) modules are running different software images.

```text
router(config)# redundancy
router(config-r)# main-cpu
router(config-r-mc)# no auto-sync startup-config
router(config-r-mc)# auto-sync config-register
router(config-r-mc)# auto-sync bootvar
router(config-r-mc)# exit
router(config-r)# exit
```

Cisco RF Gateway 10 The following example shows the synchronization of all system files on the Cisco RFGW-10 chassis:

```text
Router#configure terminal
Router(config)#redundancy
Router(config-red)#main-cpu
Router(config-r-mc)#auto-sync standard
Router(config-r-mc)#exit
Router(config-red)#exit
```


### `autoupgrade disk-cleanup`

> **Página:** 48 · **Modo:** Global configuration (config) · **Default:** By default, the crashinfo files, the core files, and the Cisco software images are deleted by the Cisco IOS Auto-Upgrade Manager disk cleanup utility, and the filesystems that support the undelete operation are not cleaned up. · **Leitura (show/clear/…):** não

**Description:** To configure the Cisco IOS Auto-Upgrade Manager disk cleanup utility, use the autoupgrade disk-cleanup command in global configuration mode. To disable this configuration, use the no form of this command.

**Syntax:**

```text
autoupgrade disk-cleanup [crashinfo | core | image | irrecoverable]
no autoupgrade disk-cleanup [crashinfo | core | image | irrecoverable]
```

**Parameters (Syntax Description):**

- `c r as h info` — ( Optional) Delete s c r as h info files d u r in g disk-cleanup before an image is download e d.
- `core` — ( Optional) Delete s core files d u r in g disk-cleanup before an image is download e d.
- `image` — ( Optional) Delete s the Cisco IOS image s, e x c e p t the default bootimage and the current image, d u r in g disk-cleanup before an image is download e d.
- `i r r e c over a b l e` — ( Optional) Delete s files i r r e t r i e v a b l y( in a file-system that support s the undelete o p e r at i on) d u r in g disk-cleanup before an image is download e d.

**Command Default:** By default, the crashinfo files, the core files, and the Cisco software images are deleted by the Cisco IOS Auto-Upgrade Manager disk cleanup utility, and the filesystems that support the undelete operation are not cleaned up.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(15)T | This command was introduced. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Example:**

The following example shows how to clean-up filesystems that support undelete operation:

```text
Device(config)# autoupgrade disk-cleanup irrecoverable
```

The following example shows how to avoid deleting the Cisco software images:

```text
Device(config)#
no autoupgrade disk-cleanup image
```


### `autoupgrade ida url`

> **Página:** 49 · **Modo:** Global configuration (config) · **Default:** Default URL: https://www.cisco.com/cgi-bin/ida/locator/locator.pl · **Leitura (show/clear/…):** não

**Description:** To configure the URL of the Intelligent Download Application (IDA) running on www.cisco.com, use the command.

**Syntax:**

```text
autoupgrade ida url command in global configuration mode. To disable this URL, use the no form of this
autoupgrade ida url url
no autoupgrade ida url url
```

**Parameters (Syntax Description):**

- `url` — URL of the IDA server.

**Command Default:** Default URL: https://www.cisco.com/cgi-bin/ida/locator/locator.pl

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(15)T | This command was introduced. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Use the autoupgrade ida url command to configure a new URL for the IDA server, if it is not present in the default location. The device sends the image download requests to the configured URL.

**Example:**

The following example shows how to configure the URL for the IDA server:

```text
Device(config)# autoupgrade ida url https://www.cisco.com/cgi-bin/ida/locator/locator.pl
```


### `autoupgrade status email`

> **Página:** 50 · **Modo:** Global configuration (config) · **Default:** Status email is not sent unless the address is configured. The recipient email address and SMTP server have to be configured in order to receive AUM status email. · **Leitura (show/clear/…):** não

**Description:** To configure the address to which status email is to be sent and the outgoing email server, use the autoupgrade status email command in global configuration mode. To disable status email, use the no form of this command.

**Syntax:**

```text
autoupgrade status email [recipient [email-address]] [smtp-server [smtp-server]]
no autoupgrade status email [recipient [email-address]] [smtp-server [smtp-server]]
```

**Parameters (Syntax Description):**

- `r e c ip i e n t` — The address to which the Cisco IOS Auto-Upgrade M an age r( A U M) status is to be s e n t.
- `smtp-server` — The out g o in g email server to which the A U M email is s e n t.
- `email-address` — The email address to which the A U M status is to be s e n t.

**Command Default:** Status email is not sent unless the address is configured. The recipient email address and SMTP server have to be configured in order to receive AUM status email.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(15)T | This command was introduced. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Use this command to configure the email-address where AUM status email can be sent.

**Example:**

The following example shows how to configure the address to which status email is to be sent:

```text
Device(config)# autoupgrade status email recipient tree@abc.com
Device(config)# autoupgrade status email smtp-server smtpserver.abc.com
```


### `banner exec`

> **Página:** 51 · **Modo:** Global configuration · **Default:** Disabled (no EXEC banner is displayed). · **Leitura (show/clear/…):** não

**Description:** To specify and enable a message to be displayed when an EXEC process is created (an EXEC banner), use the command in global configuration mode. To delete the existing EXEC banner, use the form of this command.

**Syntax:**

```text
banner exec no
banner exec d message d
no banner exec
```

**Parameters (Syntax Description):**

- `d` — D e limit in g character of your c h o i c e--ap o u n d s i g n(#), for example. You can not use the d e limit in g character in the banner message.
- `message` — Message text. You can include token s in the form$( token) in the message text. Token s will be replaced with the c or r e s p on d in g configuration v a r i a b l e. Token s are describe d in the t a b l e be low.

**Command Default:** Disabled (no EXEC banner is displayed).

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 11.3(7.5)AA | Token f u n c t i on a l it y was introduced. |
| 12.0(3)T | Token f u n c t i on a l it y was integrated into Cisco IOS Release12.0(3) T. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command specifies a message to be displayed when an EXEC process is created (a line is activated, or an incoming connection is made to a vty). Follow this command with one or more blank spaces and a delimiting character of your choice. Then enter one or more lines of text, terminating the message with the second occurrence of the delimiting character. When a user connects to a router, the message-of-the-day (MOTD) banner appears first, followed by the login banner and prompts. After the user logs in to the router, the EXEC banner or incoming banner will be displayed, depending on the type of connection. For a reverse Telnet login, the incoming banner will be displayed. For all other connections, the router will display the EXEC banner. To disable the EXEC banner on a particular line or lines, use the no exec-banner line configuration command. To customize the banner, use tokens in the form $(token ) in the message text. Tokens will display current Cisco IOS configuration variables, such as the router’s host name and IP address. The tokens are described in the table below.

| Token | InformationDisplayedintheBanner |
| --- | --- |
| $(hostname) | Displaysthehostnamefortherouter. |
| $(domain) | Displaysthedomainnamefortherouter. |
| $(line) | Displaysthevtyortty(asynchronous)linenumber. |
| $(line-desc) | Displaysthedescriptionattachedtotheline. |

**Example:**

The following example sets an EXEC banner that uses tokens. The percent sign (%) is used as a delimiting character. Notice that the $(token ) syntax is replaced by the corresponding configuration variable.

```text
Router(config)# banner exec %
Enter TEXT message. End with the character '%'.
Session activated on line $(line), $(line-desc). Enter commands at the prompt.
%
```

When a user logs on to the system, the following output is displayed:

```text
User Access Verification
Username:
joeuser
Password: <password>
Session activated on line 50, vty default line. Enter commands at the prompt.
Router>
```


### `banner incoming`

> **Página:** 53 · **Modo:** Global configuration · **Default:** Disabled (no incoming banner is displayed). · **Leitura (show/clear/…):** não

**Description:** To define and enable a banner to be displayed when there is an incoming connection to a terminal line from a host on the network, use the banner incoming command in global configuration mode. To delete the incoming connection banner, use the no form of this command.

**Syntax:**

```text
banner incoming d message d
no banner incoming
```

**Parameters (Syntax Description):**

- `d` — D e limit in g character of your c h o i c e--a pound sign (#), for example. You cannot use the d e limit in g
- `d` — D e limit in g character of your c h o i c e--ap o u n d s i g n(#), for example. You can not use the d e limit in g character in the banner message.
- `message` — Message text. You can include token s in the form$( token) in the message text. Token s will be replaced with the c or r e s p on d in g configuration v a r i a b l e. Token s are describe d in the t a b l e be low.

**Command Default:** Disabled (no incoming banner is displayed).

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 11.3(7.5)AA | Token f u n c t i on a l it y was introduced. |
| 12.0(3)T | Token f u n c t i on a l it y was integrated into Cisco IOS Release12.0(3) T. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Follow the banner incomingcommand with one or more blank spaces and a delimiting character of your choice. Then enter one or more lines of text, terminating the message with the second occurrence of the delimiting character. An incoming connection is one initiated from the network side of the router. Incoming connections are also called reverse Telnet sessions. These sessions can display MOTD banners and incoming banners, but they do not display EXEC banners. Use the no motd-banner line configuration command to disable the MOTD banner for reverse Telnet sessions on asynchronous lines. When a user connects to the router, the message-of-the-day (MOTD) banner (if configured) appears first, before the login prompt. After the user successfully logs in to the router, the EXEC banner or incoming banner will be displayed, depending on the type of connection. For a reverse Telnet login, the incoming banner will be displayed. For all other connections, the router will display the EXEC banner. Incoming banners cannot be suppressed. If you do not want the incoming banner to appear, you must delete it with the no banner incoming command. To customize the banner, use tokens in the form $(token ) in the message text. Tokens will display current Cisco IOS configuration variables, such as the router’s host name and IP address. The tokens are described in the table below.

| Token | InformationDisplayedintheBanner |
| --- | --- |
| $(hostname) | Displaysthehostnamefortherouter. |
| $(domain) | Displaysthedomainnamefortherouter. |
| $(line) | Displaysthevtyortty(asynchronous)linenumber. |
| $(line-desc) | Displaysthedescriptionattachedtotheline. |

**Example:**

The following example sets an incoming connection banner. The pound sign (#) is used as a delimiting character.

```text
Router(config)# banner incoming #
This is the Reuses router.
#
```

The following example sets an incoming connection banner that uses several tokens. The percent sign (%) is used as a delimiting character.

```text
darkstar(config)#
banner incoming %
Enter TEXT message. End with the character '%'.
You have entered $(hostname).$(domain) on line $(line) ($(line-desc)) %
```

When the incoming connection banner is executed, the user will see the following banner. Notice that the $(token ) syntax is replaced by the corresponding configuration variable.

```text
You have entered darkstar.ourdomain.com on line 5 (Dialin Modem)
```


### `banner login`

> **Página:** 55 · **Modo:** Global configuration · **Default:** Disabled (no login banner is displayed). · **Leitura (show/clear/…):** não

**Description:** To define and enable a customized banner to be displayed before the username and password login prompts, use the banner login command in global configuration mode. To disable the login banner, use no form of this command.

**Syntax:**

```text
banner login d message d
no banner login
```

**Parameters (Syntax Description):**

- `d` — D e limit in g character of your c h o i c e--ap o u n d s i g n(#), for example. You can not use the d e limit in g character in the banner message.
- `message` — Message text. You can include token s in the form$( token) in the message text. Token s will be replaced with the c or r e s p on d in g configuration v a r i a b l e. Token s are describe d in the t a b l e be low.

**Command Default:** Disabled (no login banner is displayed).

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 11.3(7.5)AA | Token f u n c t i on a l it y was introduced. |
| 12.0(3)T | Token f u n c t i on a l it y was integrated into Cisco IOS Release12.0(3) T. |
| 12.2(14)SX | This command was integrated into Cisco IOS Release12.2(14) S X. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Follow the banner login command with one or more blank spaces and a delimiting character of your choice. Then enter one or more lines of text, terminating the message with the second occurrence of the delimiting character. When a user connects to the router, the message-of-the-day (MOTD) banner (if configured) appears first, followed by the login banner and prompts. After the user successfully logs in to the router, the EXEC banner or incoming banner will be displayed, depending on the type of connection. For a reverse Telnet login, the incoming banner will be displayed. For all other connections, the router will display the EXEC banner. To customize the banner, use tokens in the form $(token ) in the message text. Tokens will display current Cisco IOS configuration variables, such as the router’s host name and IP address. The tokens are described in the table below.

| Token | InformationDisplayedintheBanner |
| --- | --- |
| $(hostname) | Displaysthehostnamefortherouter. |
| $(domain) | Displaysthedomainnamefortherouter. |
| $(line) | Displaysthevtyortty(asynchronous)linenumber. |
| $(line-desc) | Displaysthedescriptionattachedtotheline. |

**Example:**

The following example sets a login banner. Double quotes (") are used as the delimiting character.

```text
Router# banner login " Access for authorized users only. Please enter your username and
password. "
```

The following example sets a login banner that uses several tokens. The percent sign (%) is used as the delimiting character.

```text
darkstar(config)#
banner login %
Enter TEXT message. End with the character '%'.
You have entered $(hostname).$(domain) on line $(line) ($(line-desc)) %
```

When the login banner is executed, the user will see the following banner. Notice that the $(token) syntax is replaced by the corresponding configuration variable.

```text
You have entered darkstar.ourdomain.com on line 5 (Dialin Modem)
```


### `banner motd`

> **Página:** 56 · **Modo:** Global configuration · **Default:** Disabled (no MOTD banner is displayed). · **Leitura (show/clear/…):** não

**Description:** To define and enable a message-of-the-day (MOTD) banner, use the banner motd command in global configuration mode. To delete the MOTD banner, use the no form of this command.

**Syntax:**

```text
banner motd d message d
no banner motd
```

**Parameters (Syntax Description):**

- `d` — D e limit in g character of your c h o i c e--ap o u n d s i g n(#), for example. You can not use the d e limit in g character in the banner message.
- `message` — Message text. You can include token s in the form$( token) in the message text. Token s will be replaced with the c or r e s p on d in g configuration v a r i a b l e.

**Command Default:** Disabled (no MOTD banner is displayed).

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 11.3(7.5)AA | Token f u n c t i on a l it y was introduced. |
| 12.0(3)T | Token f u n c t i on a l it y was integrated into Cisco IOS Release12.0(3) T. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Follow this command with one or more blank spaces and a delimiting character of your choice. Then enter one or more lines of text, terminating the message with the second occurrence of the delimiting character. This MOTD banner is displayed to all terminals connected and is useful for sending messages that affect all users (such as impending system shutdowns). Use the no exec-banner or no motd-banner command to disable the MOTD banner on a line. The no exec-banner command also disables the EXEC banner on the line. When a user connects to the router, the MOTD banner appears before the login prompt. After the user logs in to the router, the EXEC banner or incoming banner will be displayed, depending on the type of connection. For a reverse Telnet login, the incoming banner will be displayed. For all other connections, the router will display the EXEC banner. To customize the banner, use tokens in the form $(token ) in the message text. Tokens will display current Cisco IOS configuration variables, such as the router’s host name and IP address. The tokens are described in the table below.

| Token | InformationDisplayedintheBanner |
| --- | --- |
| $(hostname) | Displaysthehostnamefortherouter. |
| $(domain) | Displaysthedomainnamefortherouter. |
| $(line) | Displaysthevtyortty(asynchronous)linenumber. |
| $(line-desc) | Displaysthedescriptionattachedtotheline. |

**Example:**

The following example configures an MOTD banner. The pound sign (#) is used as a delimiting character.

```text
Router# banner motd # Building power will be off from 7:00 AM until 9:00 AM this coming
Tuesday.
```

The following example configures an MOTD banner with a token. The percent sign (%) is used as a delimiting character.

```text
darkstar(config)# banner motd %
Enter TEXT message. End with the character '%'.
Notice: all routers in $(domain) will be upgraded beginning April 20
%
```

When the MOTD banner is executed, the user will see the following. Notice that the $(token ) syntax is replaced by the corresponding configuration variable.

```text
Notice: all routers in ourdomain.com will be upgraded beginning April 20
```


### `banner slip-ppp`

> **Página:** 58 · **Modo:** Global configuration · **Default:** The default SLIP or PPP banner message is: Entering encapsulation mode. Async interface address is unnumbered (Ethernet0) Your IP address is 10.000.0.0 MTU is 1500 bytes The banner message when using the service old-slip-prompt command is: Entering encapsulation mode. Your IP address is 10.100.0.0 MTU is 1500 bytes where encapsulation is SLIP or PPP. · **Leitura (show/clear/…):** não

**Description:** To customize the banner that is displayed when a Serial Line Internet Protocol (SLIP) or PPP connection is made, use the banner slip-ppp command in global configuration mode. To restore the default SLIP or PPP banner, use the no form of this command.

**Syntax:**

```text
banner slip-ppp d message d
no banner slip-ppp
```

**Parameters (Syntax Description):**

- `d` — D e limit in g character of your c h o i c e--ap o u n d s i g n(#), for example. You can not use the d e limit in g character in the banner message.
- `message` — Message text. You can include token s in the form$( token) in the message text. Token s will be replaced with the c or r e s p on d in g configuration v a r i a b l e.

**Command Default:** The default SLIP or PPP banner message is: Entering encapsulation mode. Async interface address is unnumbered (Ethernet0) Your IP address is 10.000.0.0 MTU is 1500 bytes The banner message when using the service old-slip-prompt command is: Entering encapsulation mode. Your IP address is 10.100.0.0 MTU is 1500 bytes where encapsulation is SLIP or PPP.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(3)T | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Follow this command with one or more blank spaces and a delimiting character of your choice. Then enter one or more lines of text, terminating the message with the second occurrence of the delimiting character. Use this command to define a custom SLIP or PPP connection message. This is useful when legacy client applications require a specialized connection string. To customize the banner, use tokens in the form $(token ) in the message text. Tokens will display current Cisco IOS configuration variables, such as the routers host name, IP address, encapsulation type, and Maximum Transfer Unit (MTU) size. The banner tokens are described in the table below.

| Token | InformationDisplayedintheBanner |
| --- | --- |
| $(hostname) | Displaysthehostnameoftherouter. |
| $(domain) | Displaysthedomainnameoftherouter. |
| $(peer-ip) | DisplaystheIPaddressofthepeermachine. |
| $(gate-ip) | DisplaystheIPaddressofthegatewaymachine. |
| $(encap) | Displaystheencapsulationtype(SLIP,PPP,andsoon). |
| $(encap-alt) | DisplaystheencapsulationtypeasSL/IPinsteadofSLIP. |
| $(mtu) | DisplaystheMTUsize. |

**Example:**

The following example sets the SLIP/PPP banner using several tokens and the percent sign (%) as the delimiting character:

```text
Router(config)# banner slip-ppp %
Enter TEXT message. End with the character '%'.
Starting $(encap) connection from $(gate-ip) to $(peer-ip) using a maximum packet size of
$(mtu) bytes... %
```

The new SLIP/PPP banner will now be displayed when the slip EXEC command is used. Notice that the $(token ) syntax is replaced by the corresponding configuration variable.

```text
Router# slip
Starting SLIP connection from 172.16.69.96 to 192.168.1.200 using a maximum packet size of
1500 bytes...
```


### `boot`

> **Página:** 60 · **Modo:** ROM monitor · **Default:** For most platforms, if you enter the boot command and press Enter, the router boots from ROM by default. However, for some platforms, such as the Cisco 3600 series routers, if you enter the boot command and press Enter, the router boots the first image in Flash memory. Refer to the documentation for your platform for information about the default image. · **Leitura (show/clear/…):** não

**Description:** To boot the router manually, use the bootcommand in ROM monitor mode. The syntax of this command varies according to the platform and ROM monitor version. [ ] : : Cisco 7000 Series, 7200 Series, 7500 Series Routers Cisco 1600 and Cisco 3600 Series Routers Cisco 1800 Series, 2800 Series, and 3800 Series Routers :

**Syntax:**

```text
boot
boot file-url
boot filename tftp-ip-address
boot flash [flash-fs ][partition-number ][filename]
boot flash-fs:[filename]
boot [flash-fs:][partition-number:][filename]
boot usbflash0[ filename]
```

**Parameters (Syntax Description):**

- `file-url` — URL of the image to boot( for example, boot tftp://172.16.15.112/ router test).
- `file name` — When used in c on j u n c t i on with the ip-address argument, the file name argument is the name of the system image file to boot from an e two r k server. The file name is c as e s e n s it i v e. When used in c on j u n c t i on with the flash keyword, the file name argument is then a m e of the system image file to boot from Flash memory. On all platform s e x c e p t the Cisco1600 s e r i e s, Cisco3600 s e r i e s, and Cisco7000 f a m i l y routers, the system o b t a in s the image file from in t e r n a l Flash memory. Onthe Cisco1600 s e r i e s, Cisco3600 s e r i e s and Cisco7000 f a m i l y routers, the flash-f s : arguments p e c if i e s the Flash memory device from which to o b t a in the system image. ( See the flash-f s: argument l at e r in this t a b l e for v a l id device values.) The file name is c as e s e n s it i v e. With out the file name argument, the first v a l id file in Flash memory is loaded. If the file name is not specified, the first file in the partition or filesystem is used.( A USB Flash uses the first image in( c o m p a c t) Flash as the boot load e r and load s the image from USB Flash.)
- `tftp-ip-address` — ( optional) IP address of the TFTP server on which the system image r e s id e s. If o m it t e d, this value default s to the IP b r o a d c as t address of255.255.255.255.
- `flash` — Boot s the router from Flash memory. Note that this keyword isr e q u i r e d in some boot images.
- `usb flash0` — Boot the first file in USB Flash0. If the optional file name argument is used, the router boot s the specified image from USB Flash. Note This option uses the first image in( c o m p a c t) Flash as the boot load e r and load s the image from USB Flash.
- `flash-fs :` — ( Optional) Specify in gt h e Flash filesystem is optional for all platform s e x c e p t the Cisco 7500 s e r i e s routers. P o s s i b l e filesystem s are: • flash:--In t e r n a l Flash memory. • bootflash:--In t e r n a l Flash memory on the Cisco7000 f a m i l y. • slot0:--Flash memory card in the first PCM C I As l o to n the Cisco7000 f a m i l y and Cisco3600 s e r i e s routers. • slot1:--Flash memory card in these c on d PCM C I As l o to n the Cisco7000 f a m i l y and Cisco3600 s e r i e s routers.
- `partition-number :` — ( Optional) Specifies the partition number of the filesystem the files h o u l d be load e d from. This argument is not a v a i l a b l e on all platform s. If the partition-number is not specified, the first partition is used.

**Command Default:** For most platforms, if you enter the boot command and press Enter, the router boots from ROM by default. However, for some platforms, such as the Cisco 3600 series routers, if you enter the boot command and press Enter, the router boots the first image in Flash memory. Refer to the documentation for your platform for information about the default image.

**Command Modes:** ROM monitor

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | The command was introduced. |
| 12.3(14)T | The usb flash0 keyword was added to support boot in g an image from an e x t e r n a l USB Flash drive. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

To determine which form of this command to use, refer to the documentation for your platform or use the CLI help (?) feature. Use this command only when your router cannot find the boot configuration information needed in NVRAM. To enter ROM monitor mode, use one of the following methods: • Enter the reload EXEC command, then press the Break key during the first 60 seconds of startup. • Set the configuration register bits 0 to 3 to zero (for example, set the configuration register to 0x0) and enter the reload command. The ROM Monitor prompt is either “>” or, for newer platforms, “rommon x >”. Enter only lowercase commands. These commands work only if there is a valid image to boot. Also, from the ROM monitor prompt, issuing a prior reset command is necessary for the boot to be consistently successful. In Cisco IOS Release 12.3(4)T, MONLIB was modified to search in media for a valid Cisco IOS image. This change prevents boot failures that result when the first file read in disk or flash is not a valid Cisco IOS image. Refer to your hardware documentation for information on correct jumper settings for your platform. For some platforms the flash keyword is now required. If your attempts to use the boot command are failing using the older boot flash:x:[filename ] syntax, try using the boot flash flash:x:[filename ] syntax.

**Example:**

In the following example, a router is manually booted from ROM:

```text
> boot
F3:
(ROM Monitor copyrights)
```

In the following example, a router boots the file named routertest from a network server with the IP address 172.16.15.112 using the file-url syntax:

```text
> boot tftp://172.16.15.112/routertest
F3
(ROM Monitor copyrights)
```

The following example shows the boot flash command without the filename argument. The first valid file in Flash memory is loaded.

```text
> boot flash
F3: 1858656+45204+166896 at 0x1000
Booting gs7-k from flash memory RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR [OK - 1903912/13765276 bytes]
F3: 1858676+45204+166896 at 0x1000
(ROM Monitor copyrights)
```

The following example boots from Flash memory using the file named gs7-k:

```text
> boot flash gs7-k
F3: 1858656+45204+166896 at 0x1000
Booting gs7-k from flash memory RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
RRRRRRRRRRRRRR [OK - 1903912/13765276 bytes]
F3: 1858676+45204+166896 at 0x1000
(ROM Monitor copyrights)
```

In the following example, the boot flash flash: command boots the relocatable image file named igs-bpx-l from partition 2 in Flash memory:

```text
> boot flash flash:2:igs-bpx-l
F3: 3562264+98228+303632 at 0x30000B4
(ROM Monitor copyrights)
```

In the following command, the Cisco 7000 family router accepts the flash keyword for compatibility but ignores it, and boots from slot 0:

```text
> boot flash slot0:gs7-k-mz.103-9
F3: 8468+3980384+165008 at 0x1000
```

In the following example, the command did not function because it must be entered in lowercase:

```text
rommon 10 > BOOT
command “BOOT” not found
```

The following example boots the first file in the first partition of internal Flash memory of a Cisco 3600 series router:

```text
> boot flash:
```

The following example boots the first image file in the first partition of the Flash memory card in slot 0 of a Cisco 3600 series router:

```text
> boot slot0:
```

The following example shows the ROM monitor booting the first file in the first Flash memory partition on a Cisco 1600 series router:

```text
> boot flash:
```

**Related Commands:**

- Related Topics
- boot bootldr, on page 40
- boot bootstrap, on page 41
- boot config, on page 43
- boot host, on page 45


### `boot bootldr`

> **Página:** 64 · **Modo:** Global configuration (config) · **Default:** Refer to your platform documentation for the location of the default boot image. · **Leitura (show/clear/…):** não

**Description:** To specify the location of the boot image that ROM uses for booting, use the boot bootldr command in global configuration mode. To remove this boot image specification, use the no form of this command.

**Syntax:**

```text
boot bootldr file-url boot bootldr command
no boot bootldr
```

**Parameters (Syntax Description):**

- `file-url` — URL of the bootimage on a Flash filesystem.

**Command Default:** Refer to your platform documentation for the location of the default boot image.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | The command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The command sets the BOOTLDR variable in the current running configuration. You must boot bootldr specify both the Flash file system and the filename. Note When you use this global configuration command, you affect only the running configuration. You must save the variable setting to your startup configuration to place the information under ROM monitor control and to have the variable function as expected. Use the copy system:running-config nvram:startup-config command to save the variable from your running configuration to your startup configuration. Note The default length of the bootstring filename is 64 characters. Depending on the platform a longer bootstring filename can be used and supported. The no form of the command sets the BOOTLDR variable to a null string. On the Cisco 7000 family routers , a null string causes the first image file in boot Flash memory to be used as the boot image that ROM uses for booting. Use the show boot command to display the current value for the BOOTLDR variable.

**Example:**

In the following example, the internal Flash memory contains the boot image:

```text
boot bootldr bootflash:boot-image
```

The following example specifies that the Flash memory card inserted in slot 0 contains the boot image:

```text
boot bootldr slot0:boot-image
```


### `boot bootstrap`

> **Página:** 65 · **Modo:** Global configuration (config) · **Default:** No secondary bootstrap is configured. · **Leitura (show/clear/…):** não

**Description:** To configure the filename that is used to boot a secondary bootstrap image, use the boot bootstrap command in global configuration mode. To disable booting from a secondary bootstrap image, use the no form of this command.

**Syntax:**

```text
boot bootstrap file-url
no boot bootstrap file-url
boot bootstrap flash [filename]
no boot bootstrap flash [filename]
boot bootstrap [tftp] filename [ip-address]
no boot bootstrap [tftp] filename [ip-address]
boot bootstrap mop filename [interface-type interface-number]
no boot bootstrap mop filename [interface-type interface-number]
```

**Parameters (Syntax Description):**

- `file-url` — URL of the bootstrap image.
- `flash` — Boot s the router from flash memory.
- `file name` — ( Optional with flash) Name of the system image to boot from an e two r k server or from flash memory. If you o m it the file name when boot in g from flash memory, the router uses the first system image s to r e d in flash memory.
- `tftp` — ( Optional) Boot s the router from as y s t e m image s to r e do n a TFTP server.
- `ip-address` — ( Optional) IP address of the TFTP server on which the system image r e s id e s. Ifthe ip-address argument is o m it t e d, this value default s to the IP b r o a d c as t address of 255.255.255.255.
- `mop` — Boot s the router from a DECnet M a in t e n an c e O p e r at i on P r o to c o l( MOP) server.
- `interface-type` — ( Optional) Interface type. Form or e information, use the q u e s t i on mark(?) on line help f u n c t i on.
- `interface-number` — ( Optional) Interface or s u b interface number. Form or e information about then u m be r in g syntax for your network in g device, use the q u e s t i on mark(?) on line help f u n c t i on.

**Command Default:** No secondary bootstrap is configured.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 15.0(1)M | This command was modified in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. The mop keyword and interface-type interface-number arguments were added. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was i m p l e m e n t e do n the Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Usage Guidelines:**

The boot bootstrap command causes the router to load a secondary bootstrap image from the specied URL, such as from a remote server. After the bootstrap image is loaded, the bootstrap image loads the specified system image file. See the appropriate hardware installation guide for details on setting the configuration register and secondary bootstrap filename. Use this command when you have attempted to load a system image but have run out of memory even after compressing the system image. Secondary bootstrap images allows you to load a larger system image through a smaller secondary image.

**Example:**

The following example shows how to load the system image file named sysimage-2 by using a secondary bootstrap image:

```text
Router# configure terminal
Router(config)# boot bootstrap bootflash:sysimage-2
```


### `boot config`

> **Página:** 67 · **Modo:** Global configuration (config) · **Default:** The default location for the configuration file is NVRAM (nvram:). · **Leitura (show/clear/…):** não

**Description:** To s pecify the device and filename of the configuration file from which the system configures itself during initialization (startup), use the boot config command in global configuration mode. To return to the default location for the configuration file, use the no form of this command. Platforms Other than Cisco 7600 Series Router Cisco 7600 Series Router

**Syntax:**

```text
boot config file-system-prefix:[directory/]filename [nvbypass]
no boot config
boot config device:filename [nvbypass]
no boot config
```

**Parameters (Syntax Description):**

- `file-system-prefix :` — Filesystem, f o l low e d by a c o l on( for example, nvram:, flash:, slot0:, usb flash09 :, or usbtoken09:). The default is nvram:.
- `directory/` — ( Optional) Filesystem directory where the configuration file is l o c at e d, f o l low e d by a for w a r d s l as h(/).
- `file name` — Name of the configuration file.
- `device :` — Device id e n t if i c at i on, f o l low e d by a c o l on; see the“ Usage Guidelines” section for a list of the v a l id values.
- `n v by pass` — ( Optional) Specifies that the d is t i l l e d configuration is not w r it t e n to no n v o l at i l e r and o m access memory( NVRAM).

**Command Default:** The default location for the configuration file is NVRAM (nvram:).

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(14)SX | Support for this command was added for the Cisco7600 Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the cisco7600 Supervisor E n g in e2 was e x t end e d to Release 12.2(17d)SXB. |
| 11.0 | This command was introduced. |
| 12.3(14)T | Support for Class B filesystem platform s and the following filesystem pref i x options were added: usb flash09: and usbtoken09: This command is available only on Class A and Class B file system platforms. You set the CONFIG_FILE environment variable in the current running memory when you use the boot config command. This variable specifies the configuration file used for initialization (startup). The configuration file must be an ASCII file located in either NVRAM or flash memory. The valid values for the device :argument and colonare as follows: • For systems that are configured with a Supervisor Engine 2, the valid values are bootflash:, const_nvram:, flash:, nvram:, slot0:, sup-slot0:, and sup-bootflash: • For systems that are configured with a Supervisor Engine 720, the valid values are disk0: and disk1: The configuration file must be an ASCII file that is located in the specified file system. The disk0: and disk1: keywords are for Class C file systems. The , , and keywords are for Class A file systems. bootflash: slot0: sup-bootflash: For Class A flash file systems, the CONFIG_FILE environment variable specifies the file system and filename of the configuration file to use for initialization (startup). You set the CONFIG_FILE environment variable in the current running memory when you use the boot config command. This variable specifies the configuration file used for initialization (startup). When you use the boot config command, you affect only the running configuration. You must save the environment variable setting to your startup configuration to place the information under ROM monitor control and to have the environment variable function as expected. Use the copy system:running-config nvram:startup-config command to save the environment variable from your running configuration to your startup configuration. The software displays an error message and does not update the CONFIG_FILE environment variable in the following situations: • You specify nvram: as the file system, and it contains only a distilled version of the configuration. (A distilled configuration is one that does not contain access lists.) • You specify a configuration file in the filename argument that does not exist or is not valid. The router uses the NVRAM configuration during initialization when the CONFIG_FILE environment variable does not exist or when it is null (such as at first-time startup). If the software detects a problem with NVRAM or the configuration it contains, the device enters setup mode. When you use the no form of this command, the router returns to using the default NVRAM configuration file as the startup configuration. You can display the contents of the BOOT, BOOTLDR, and the CONFIG_FILE environment variables using the show bootvar command. This command displays the settings for these variables as they exist in the startup configuration and in the running configuration if a running configuration setting differs from a startup configuration setting. When the boot config command is used, the distilled configuration is written into NVRAM and the system configuration is written into the file specified by the boot config command. If the distilled configuration exceeds the size of NVRAM, the system configuration gets truncated. Use the nvbypass keyword to prevent the system configuration from being truncated when the distilled configuration is larger than the size of NVRAM. |

**Example:**

The following example shows how to set the configuration file that is located in internal flash memory to configure itself during initialization. The third line copies the specification to the startup configuration, ensuring that this specification will take effect upon the next reload.

```text
Router(config)# boot config flash:router-config
Router(config)# end
Router# copy system:running-config nvram:startup-config
```

The following example instructs a Cisco 7500 series router to use the configuration file named router-config located on the flash memory card inserted in the second Personal Computer Memory Card Industry Association (PCMCIA) slot of the Route Switch Processor (RSP) card during initialization. The third line copies the specification to the startup configuration, ensuring that this specification will take effect upon the next reload.

```text
Router (config)# boot config slot1:router-config
Router (config)# end
Router# copy system:running-config nvram:startup-config
```


### `boot host`

> **Página:** 69 · **Modo:** Global configuration · **Default:** If you do not specify a filename using this command, the router uses its configured host name to request a configuration file from a remote server. To form the configuration filename, the router converts its name to all lowercase letters, removes all domain information, and appends -confg or -config. · **Leitura (show/clear/…):** não

**Description:** To specify the host-specific configuration file to be used at the next system startup, use the boot host command in global configuration mode. To restore the host configuration filename to the default, use the no form of this command.

**Syntax:**

```text
boot host commandboot host remote-url
no boot host remote-url
```

**Parameters (Syntax Description):**

- `remote-url` — Location of the configuration file. Use the following syntax: • ftp:[[[//[ username[: password]@] location]/ directory]/ file name] • rcp:[[[//[ username@] location]/ directory]/ file name] • tftp:[[[// location]/ directory]/ file name]

**Command Default:** If you do not specify a filename using this command, the router uses its configured host name to request a configuration file from a remote server. To form the configuration filename, the router converts its name to all lowercase letters, removes all domain information, and appends -confg or -config.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command instructs the system to “Boot using host-specific configuration file x ,” where x is the filename specified in the remote-url argument. In other words, this command specifies the remote location and filename of the host-specific configuration file to be used at the next system startup, as well as the protocol to be used to obtain the file. Before using the boot host command, use the service config global configuration command to enable the loading of the specified configuration file at reboot time. Without this command, the router ignores the boot host command and uses the configuration information in NVRAM. If the configuration information in NVRAM is invalid or missing, the service config command is enabled automatically. The network server will attempt to load two configuration files from remote hosts. The first is the network configuration file containing commands that apply to all network servers on a network. Use the boot network command to identify the network configuration file. The second is the host configuration file containing commands that apply to one network server in particular. Use the boot host command to identify the host configuration file. Note Usually, the service config command is used in conjunction with the boot host or boot network command. You must enter the service config command to enable the router to automatically configure the system from the file specified by the boot host or boot network command. With IOS software versions 12.3(2)T , 12.3(1)B, and later, you no longer have to specify the service config command for the boot host or boot network command to be active. If you specify both the no service config command and the boot host command, the router attempts to find the specified host configuration file. The service config command can also be used without the boot host or boot network command. If you do not specify host or network configuration filenames, the router uses the default configuration files. The default network configuration file is network-confg. The default host configuration file is host-confg, where host is the hostname of the router. If the Cisco IOS software cannot resolve its hostname, the default host configuration file is router-confg. Loading a Configuration File Using rcp The rcp software requires that a client send the remote username on each rcp request to the network server. If the server has a directory structure (such as UNIX systems), the rcp implementation searches for the configuration files starting in the directory associated with the remote username. When you load a configuration file from a server using rcp, the Cisco IOS software sends the first valid username in the following list: 1. The username specified in the file-URL, if a username is specified. 2. The username set by the ip rcmd remote-username command, if the command is configured. 3. The router host name. Note An account for the username must be defined on the destination server. If the network administrator of the destination server did not establish an account for the username, this command will not execute successfully. Loading a Configuration File Using FTP The FTP protocol requires a client to send a remote username and password on each FTP request to a server. The username and password must be associated with an account on the FTP server. If the server has a directory structure, the configuration file or image copied from the directory is associated with the username on the server. Refer to the documentation for your FTP server for more details. When you load a configuration file from a server using FTP, the Cisco IOS software sends the first valid username in the following list: 1. The username specified in the boot host command, if a username is specified. 2. The username set by the ip ftp username command, if the command is configured. 3. Anonymous. The router sends the first valid password in the following list: 1. The password specified in the boot host command, if a password is specified. 2. The password set by the ip ftp password command, if the command is configured. 3. The router forms a password username @routername .domain . The variable username is the username associated with the current session, routername is the configured host name, and domain is the domain of the router.

**Example:**

The following example sets the host filename to wilma-confg at address 192.168.7.19:

```text
Router(config)# boot host tftp://192.168.7.19/usr/local/tftpdir/wilma-confg
Router(config)# service config
```


### `boot network`

> **Página:** 71 · **Modo:** Global configuration · **Default:** The default filename is network-config. · **Leitura (show/clear/…):** não

**Description:** To change the default name of the network configuration file from which to load configuration commands, use the boot network command in global configuration mode. To restore the network configuration filename to the default, use the no form of this command.

**Syntax:**

```text
boot network remote-url
no boot network remote-url
```

**Parameters (Syntax Description):**

- `remote-url` — Location of the configuration file. Use the following syntax: • ftp:[[[//[ username[: password]@] location]/ directory]/ file name] • rcp:[[[//[ username@] location]/ directory]/ file name] • tftp:[[[// location]/ directory]/ file name]

**Command Default:** The default filename is network-config.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command instructs the system to “Boot using network configuration file x ,” where x is the filename specified in the remote-url argument. This command specifies the remote location and filename of the network configuration file to be used at the next system startup, as well as the protocol to be used to obtain the file. When booting from a network server, routers ignore routing information, static IP routes, and bridging information. As a result, intermediate routers are responsible for handling FTP, rcp, or TFTP requests. Before booting from a network server, verify that a server is available by using the command. ping Use the service config command to enable the loading of the specified configuration file at reboot time. Without this command, the router ignores the boot network command and uses the configuration information in NVRAM. If the configuration information in NVRAM is invalid or missing, the service config command is enabled automatically. The network server will attempt to load two configuration files from remote hosts. The first is the network configuration file containing commands that apply to all network servers on a network. Use the boot network command to identify the network configuration file. The second is the host configuration file containing commands that apply to one network server in particular. Use the boot host command to identify the host configuration file. Note Usually, the service config command is used in conjunction with the boot host or boot network command. You must enter the service config command to enable the router to automatically configure the system from the file specified by the boot host or boot network command. With IOS software versions 12.3(2)T , 12.3(1)B, and later, you no longer have to specify the service config command for the boot host or boot network command to be active. If you specify both the no service config command and the boot host command, the router attempts to find the specified host configuration file. The service config command can also be used without the boot host or boot network command. If you do not specify host or network configuration filenames, the router uses the default configuration files. The default network configuration file is network-confg. The default host configuration file is host-confg, where host is the hostname of the router. If the Cisco IOS software cannot resolve its hostname, the default host configuration file is router-confg. Loading a Configuration File Using rcp The rcp software requires that a client send the remote username on each rcp request to the network server. If the server has a directory structure (such as UNIX systems), the rcp implementation searches for the configuration files starting in the directory associated with the remote username. When you load a configuration file from a server using rcp, the Cisco IOS software sends the first valid username in the following list: 1. The username specified in the file-URL, if a username is specified. 2. The username set by the ip rcmd remote-username command, if the command is configured. 3. The router host name. An account for the username must be defined on the destination server. If the network administrator of the destination server did not establish an account for the username, this command will not execute successfully. Loading a Configuration File Using FTP The FTP protocol requires a client to send a remote username and password on each FTP request to a server. The username and password must be associated with an account on the FTP server. If the server has a directory structure, the configuration file or image copied from the directory associated with the username on the server. Refer to the documentation for your FTP server for more details. When you load a configuration file from a server using FTP, the Cisco IOS software sends the first valid username in the following list: 1. The username specified in the boot network command, if a username is specified. 2. The username set by the ip ftp username command, if the command is configured. 3. Anonymous. The router sends the first valid password in the following list: 1. The password specified in the boot network command, if a password is specified. 2. The password set by the ip ftp password command, if the command is configured. 3. The router forms a password username @routername .domain . The variable username is the username associated with the current session, routername is the configured host name, and domain is the domain of the router.

**Example:**

The following example changes the network configuration filename to bridge_9.1 and uses the default broadcast address:

```text
Router(config)# boot network tftp:bridge_9.1
Router(config)# service config
```

The following example changes the network configuration filename to bridge_9.1, specifies that rcp is to be used as the transport mechanism, and gives 172.16.1.111 as the IP address of the server on which the network configuration file resides:

```text
Router(config)# service config
Router(config)# boot network rcp://172.16.1.111/bridge_9.1
```


### `boot system`

> **Página:** 74 · **Modo:** Global configuration · **Default:** If you configure the router to boot from a network server but do not specify a system image file with the boot system command, the router uses the configuration register settings to determine the default system image filename. The router forms the default boot filename by starting with the word cisco and then appending the octal equivalent of the boot field number in the configuration register, followed by a hyphen (-) and the processor type name (cisconn-cpu). Refer to the appropriate hardware installation guide for details on the configuration register and default filename. See also the config-register or confreg command. · **Leitura (show/clear/…):** não

**Description:** To specify the system image that the router loads at startup, use one of the following boot system command in global configuration mode. To remove the startup system image specification, use the no form of this command. Loading System Image from a URL or a TFTP File Booting from a System Image in Internal Flash Booting from a MOP Server Booting from ROM Booting a System Image from a Network, TFTP, or FTP Server

**Syntax:**

```text
boot system {file-urlfilename}
no boot system {file-urlfilename}
boot system flash [flash-fs:] [partition-number:][filename]
no boot system flash [flash-fs:] [partition-number:] [filename]
boot system mop filename [mac-address] [interface]
no boot system mop filename [mac-address] [interface]
boot system rom
no boot system rom
boot system {rcp | tftp | ftp} filename [ip-address]
no boot system {rcp | tftp | ftp} filename [ip-address]
```

**Parameters (Syntax Description):**

- `file-url` — The URL of the system image to load at systems tar t u p.
- `file name` — The TFTP file name of the system image to load at systems tar t u p.
- `flash` — On all platform s e x c e p t the Cisco1600 s e r i e s, Cisco3600 s e r i e s, and Cisco7000 f a m i l y routers, this keyword boot s the router from in t e r n a l flash memory. If you o m it all arguments that f o l low this keyword, the systems e a r c h e s in t e r n a l Flash for the first boot a b l e image. Onthe Cisco1600 s e r i e s, Cisco3600 s e r i e s, and Cisco7000 f a m i l y routers, this keyword boot s the router from the flash systems p e c if i e d by the flash-f s: argument. Onthe Cisco 1600 s e r i e s and Cisco3600 s e r i e s routers, if you o m it all optional arguments, the router s e a r c h e s in t e r n a l flash memory for the first boot a b l e image. Onthe Cisco7000 f a m i l y routers, when you o m it all arguments that f o l low this keyword, the systems e a r c h e s the P e r s on a l C o m p u t e r Memory Card In d u s t r y As s o c i at i on( PCM C I A) slot0 for the first boot a b l e image.
- `flash-fs :` — ( Optional) Flash filesystem c on t a in in gt h e system image to load at startup. The c o l on is r e q u i r e d. V a l id filesystem s are as f o l low s: • flash:--In t e r n a l flash memory on the Cisco1600 s e r i e s and Cisco3600 s e r i e s routers. Forthe Cisco1600 s e r i e s and Cisco3600 s e r i e s routers, this filesystem is the default if you do not specify a filesystem. This is the only v a l id filesystem for the Cisco 1600 s e r i e s. • bootflash:--In t e r n a l flash memory in the Cisco7000 f a m i l y. • slot0:--First PCM C I As l o to n the Cisco3600 s e r i e s and Cisco7000 f a m i l y routers . Forthe Cisco7000 f a m i l y routers, this filesystem is the default if you do not specify a filesystem. • slot1:--Flash memory card in these c on d PCM C I As l o to n the Cisco3600 s e r i e s and Cisco7000 f a m i l y routers. Onthe Cisco2600 s e r i e s routers, a filesystem should be specified. Other w is e, the router may at t e m p t to load the Cisco IOS software t w i c e with u n e x p e c t e d r e s u l t s.
- `partition-number :` — ( Optional) Number of the flash memory partition that c on t a in s the system image to boot, specified by the optional file name argument. If you do not specify a file name, the router load s the first v a l id file in the specified partition of flash memory. This argument is v a l id only on routers that can be partition e d.
- `file name` — ( Optional when used with the boot system flash command) Name of the system image to load at startup. This argument is c as e s e n s it i v e. If you do not specify a value for the file name argument, the router load s the first v a l id file in the following: • The specified flash filesystem • The specified partition of flash memory • The default flash filesystem if you also o m it t e d the flash-f s: argument
- `mop` — Boot s the router from as y s t e m image s to r e do n a D E C N E T M a in t e n an c e O p e r at i on s P r o to c o l( MOP) server. Do not use this keyword with the Cisco3600 s e r i e s or Cisco7000 f a m i l y routers.
- `mac-address` — ( Optional) MAC address of the MOP server c on t a in in gt h e specified system image file. If you do not include the MAC address argument, the routers end s a b r o a d c as t message toall MOP boot servers. The first MOP server to in d i c at e that it has the specified file is these r v e r from which the router get s the bootimage.
- `interface` — ( Optional) Interface the router uses to send out MOP request s to the MOP server. The interface options are async, d i a l e r, e the r n e t, s e r i a l, and t u n n e l. If you do not specify the interface argument, the routers end s are q u e s to u to n all interfaces that have MOP enabled. The interface that r e c e i v e s the first response is the interface the router uses to load the software.
- `rom` — Boot s the router from ROM. Do not use this keyword with the Cisco3600 s e r i e s or the Cisco7000 f a m i l y routers.
- `rcp` — Boot s the router from as y s t e m image s to r e do n an e two r k server using rcp.
- `tftp` — Boot s the router from as y s t e m image s to r e do n a TFTP server.
- `ftp` — Boot s the router from as y s t e m image s to r e do n an FTP server.
- `ip-address` — ( Optional) IP address of these r v e r c on t a in in gt h e system image file. If o m it t e d, this value default s to the IP b r o a d c as t address of255.255.255.255.

**Command Default:** If you configure the router to boot from a network server but do not specify a system image file with the boot system command, the router uses the configuration register settings to determine the default system image filename. The router forms the default boot filename by starting with the word cisco and then appending the octal equivalent of the boot field number in the configuration register, followed by a hyphen (-) and the processor type name (cisconn-cpu). Refer to the appropriate hardware installation guide for details on the configuration register and default filename. See also the config-register or confreg command.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(14)SX | Support for this command was added for the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(31)SB2 | This command was integrated into Cisco IOS Release12.2(31) S B. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |

**Usage Guidelines:**

For this command to work, the config-register command must be set properly. Create a comma-delimited list of several commands to provide a fail-safe method for booting boot system your router. The router stores and executes the boot system commands in the order in which you enter them in the configuration file. If you enter multiple boot commands of the same type--for example, if you enter two commands that instruct the router to boot from different network servers--the router tries them in the order in which they appear in the configuration file. If a boot system command entry in the list specifies an invalid device, the router omits that entry. Use the boot system rom command to specify use of the ROM system image as a backup to other boot system commands in the configuration. Note After a list of several images are specified with the boot system command, running the command again results in the list being appended, not removed. For some platforms, the boot image must be loaded before the system image is loaded. However, on many platforms, the boot image is loaded only if the router is booting from a network server or if the flash file system is not specified. If the file system is specified, the router will boot faster because it need not load the boot image first. This section contains the following topics: • Changing the List of Boot System Commands • Booting Compressed Images • Understanding rcp • Understanding TFTP • Understanding FTP • Stopping Booting and Entering ROM Monitor Mode • Cisco 1600 Series, Cisco 3600 Series, Cisco 7000 Family, and Cisco 7600 Series Router Notes Changing the List of Boot System Commands To remove a single entry from the bootable image list, use the no form of the command with an argument. For example, to remove the entry that specifies a bootable image on a flash memory card inserted in the second slot, use the no boot system flash slot1: filename] command. All other entries in the list remain. To eliminate all entries in the bootable image list, use the no boot system command. At this point, you can redefine the list of bootable images using the previous boot system commands. Remember to save your changes to your startup configuration by issuing the copy system:running-config nvram:startup-config command. Each time you write a new software image to flash memory, you must delete the existing filename in the configuration file with the no boot system flash filename command. Then add a new line in the configuration file with the command. boot system flash filename Note If you want to rearrange the order of the entries in the configuration file, you must first issue the no boot system command and then redefine the list. Booting Compressed Images You can boot the router from a compressed image on a network server. When a network server boots software, both the image being booted and the running image must be able to fit into memory. Use compressed images to ensure that enough memory is available to boot the router. You can compress a software image on any UNIX platform using the compress command. Refer to your UNIX platform’s documentation for the exact usage of the compress command. (You can also uncompress data with the UNIX uncompress command.) Understanding rcp The rcp requires that a client send the remote username in an rcp request to a server. When the router executes the boot system rcp command, the Cisco IOS software sends the hostname as both the remote and local usernames by default. Before the rcp can execute properly, an account must be defined on the network server for the remote username configured on the router. If the server has a directory structure, the rcp software searches for the system image to boot from the remote server relative to the directory of the remote username. By default, the router software sends the hostname as the remote username. You can override the default remote username by using the ip rcmd remote-username command. For example, if the system image resides in the home directory of a user on the server, you can specify that user’s name as the remote username. Understanding TFTP You need a TFTP server running to retrieve the router image from the host. Understanding FTP You need an FTP server running to retrieve the router image from the host. You also need an account on the server or anonymous file access to the server. Stopping Booting and Entering ROM Monitor Mode During the first 60 seconds of startup, you can force the router to stop booting by pressing the Break key. The router will enter ROM monitor mode, where you can change the configuration register value or boot the router manually. Cisco 1600 Series, Cisco 3600 Series, Cisco 7000 Family, and Cisco 7600 Series Router Notes For the Cisco 3600 series and Cisco 7000 family, the boot system command modifies the BOOT variable in the running configuration. The BOOT variable specifies a list of bootable images on various devices. Note When you use the boot system command on the Cisco 1600 series, Cisco 3600 series, Cisco 7000 family, and Cisco 7600 series, you affect only the running configuration. You must save the BOOT variable settings to your startup configuration to place the information under ROM monitor control and to have the variable function as expected. Use the copy system:running-config nvram:startup-config privileged EXEC command to save the variable from your running configuration to your startup configuration. To display the contents of the BOOT variable, use the show bootvar EXEC command.

**Example:**

The following example illustrates a configuration that specifies two possible internetwork locations for a system image, with the ROM software being used as a backup:

```text
Router(config)# boot system tftp://192.168.7.24/cs3-rx.90-1
Router(config)# boot system tftp://192.168.7.19/cs3-rx.83-2
Router(config)# boot system rom
```

The following example boots the system boot relocatable image file named igs-bpx-l from partition 2 of the flash device:

```text
Router(config)# boot system flash:2:igs-bpx-l
```

The following example instructs the router to boot from an image located on the flash memory card inserted in slot 0:

```text
Router(config)# boot system slot0:new-config
```

The following example specifies the file named new-ios-image as the system image for a Cisco 3600 series router to load at startup. This file is located in the fourth partition of the flash memory card in slot 0.

```text
Router(config)# boot system slot0:4:dirt/images/new-ios-image
```

This example boots from the image file named c1600-y-l in partition 2 of flash memory of a Cisco 1600 series router:

```text
Router(config)# boot system flash:2:c1600-y-l
```


### `boot-end-marker`

> **Página:** 79 · **Modo:** N/A · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** The boot-start-marker and boot-end-marker flags, which can be seen in Cisco IOS software configuration files, are not CLI commands. These markers are written to configuration files automatically to flag the beginning and end of the boot commands (boot statements). By flagging boot statements, these markers allow the router to more reliably load Cisco IOS images during bootup. A boot statement is one or more lines in a configuration file that tells the router which software image to load after a powercycling (reboot). The boot-start-marker and boot-end-marker flags will appear around any boot commands, including: • boot bootstrap • boot config • boot host • boot network • boot system Note, however, that these markers will always appear in the output of the show running-configor more system:running-config commands, regardless of whether any actual boot commands have been entered. This means that no boot commands will appear between the markers if no boot commands have been entered, or if all boot commands have been removed from the configuration, as shown in the “Examples” section. The boot-start-marker and boot-end-markerflags cannot be removed or modified using the CLI. These markers are written to the startup configuration file whenever a copy running-config startup-config command is issued. These flags were also introduced to circumvent errors in the configuration file, such as a leading space before a boot command (such as those sometimes introduced by manually edited configuration files), or the use of text strings that include the word “boot” in banners or other user-specified text. If the “boot start-marker” flag is not found in the configuration file, the system will use the traditional method to identify the boot commands. However, if you are manually creating configuration files, or copying from older Cisco IOS software releases, the addition of these markers is recommended.

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(3),12.3(4)T,12.0(26)S,12.0(27)SV, 12.3(3)B, | The boot-start-marker and boot-end-marker f l a g s were introduced. |

**Example:**

In the following example, a boot command is entered, and the boot-start-marker and boot-end-marker flags are shown in the context of the startup configuration file:

```text
Router# configure terminal
Enter configuration commands, one per line. End with the end command.
Router(config)# boot system slot0:
Router(config)# end
Router# copy running-config startup-config
Router# show startup-config
Using 1398 out of 129016 bytes
!
version 12.3
service timestamps debug uptime
service timestamps log uptime
no service password-encryption
!
hostname C3660-2
!
boot-start-marker
boot system slot0:
boot-end-marker
!
logging count
```

In the following example, the boot-start-marker and boot-end-marker flags appear in the configuration file even though no boot commands have been entered:

```text
Router# show running-configuration
Current configuration :3055 bytes
!
! No configuration change since last restart
!
version 12.3
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname Router
!
boot-start-marker
boot-end-marker
!
```


### `boot-start-marker`

> **Página:** 81 · **Modo:** N/A · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** The boot-start-marker and boot-end-marker flags, which can be seen in Cisco IOS software configuration files, are not CLI commands. These markers are written to configuration files automatically to flag the beginning and end of the boot commands (boot statements). By flagging boot statements, these markers allow the router to more reliably load Cisco IOS images during bootup. A boot statement is one or more lines in a configuration file that tells the router which software image to load after a powercycling (reboot). The boot-start-marker and boot-end-marker flags will appear around any boot commands, including: • boot bootstrap • boot config • boot host • boot network • boot system Note, however, that these markers will always appear in the output of the show running-configor more commands, regardless of whether any actual boot commands have been entered. This system:running-config means that no boot commands will appear between the markers if no boot commands have been entered, or if all boot commands have been removed from the configuration, as shown in the “Examples” section. The boot-start-marker and boot-end-markerflags cannot be removed or modified using the CLI. These markers are written to the startup configuration file whenever a copy running-config startup-config command is issued. These flags were also introduced to circumvent errors in the configuration file, such as a leading space before a boot command (such as those sometimes introduced by manually edited configuration files), or the use of text strings that include the word “boot” in banners or other user-specified text. If the “boot start-marker” flag is not found in the configuration file, the system will use the traditional method to identify the boot commands. However, if you are manually creating configuration files, or copying from older Cisco IOS software releases, the addition of these markers is recommended.

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(3),12.3(4)T,12.0(26)S,12.0(27)SV, 12.3(3)B | The boot-start-marker and boot-end-marker f l a g s were introduced. |

**Example:**

In the following example, a boot command is entered, and the boot-start-marker and boot-end-marker flags are shown in the context of the startup configuration file:

```text
Router# configure terminal
Enter configuration commands, one per line. End with the end command.
Router(config)# boot system slot0:
Router(config)# end
Router# copy running-config startup-config
Router# show startup-config
Using 1398 out of 129016 bytes
!
version 12.3
service timestamps debug uptime
service timestamps log uptime
no service password-encryption
!
hostname C3660-2
!
boot-start-marker
boot system slot0:
boot-end-marker
!
logging count
```

In the following example, the boot-start-marker and boot-end-marker flags appear in the configuration file even though no boot commands have been entered:

```text
Router# show running-configuration
Current configuration :3055 bytes
!
! No configuration change since last restart
!
version 12.3
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname Router
!
boot-start-marker
boot-end-marker
!
```
