# Capítulo 9: show through show fm summary

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## R through setup

### show through show fm summary

• show through show fm summary, on page 504

### show through show fm summary

### `show`

> **Página:** 528 · **Modo:** MST configuration (config-mst) · **Default:** This command has no default settings. · **Leitura (show/clear/…):** não

**Description:** To verify the Multiple Spanning Tree (MST) configuration, use the show command in MST configuration mode.

**Syntax:**

```text
show [current | pending]
```

**Parameters (Syntax Description):**

- `current` — ( Optional) D is p l a y s the current configuration that is used to r u n MST.
- `pending` — ( Optional) D is p l a y s the e d it e d configuration that will replace the current configuration.

**Command Default:** This command has no default settings.

**Command Modes:** MST configuration (config-mst)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The display output from the show pending command is the edited configuration that will replace the current configuration if you enter the exit command to exit MST configuration mode. Entering the show command with no arguments displays the pending configurations.

**Example:**

This example shows how to display the edited configuration:

```text
Router(config-mst)# show pending
Pending MST configuration
Name [zorglub]
Version 31415
Instance Vlans Mapped
-------- ---------------------------------------------------------------------
0 4001-4096
2 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110
3 1-1009, 1011-1019, 1021-1029, 1031-1039, 1041-1049, 1051-1059
1061-1069, 1071-1079, 1081-1089, 1091-1099, 1101-1109, 1111-1119
1121-4000
------------------------------------------------------------------------------
Router(config-mst)#
```

This example shows how to display the current configuration:

```text
Router(config-mst)# show current
Current MST configuration
Name []
Revision 0
Instance Vlans mapped
-------- ---------------------------------------------------------------------
0 1-4094
-------------------------------------------------------------------------------
```


### `show command append`

> **Página:** 529 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** command in privileged EXEC mode.

**Syntax:**

```text
To redirect and add the output of any show command to an existing file, use the show command | append
{show command | append url}
```

**Parameters (Syntax Description):**

- `command` — Any Cisco IOS show command.
- `|append url` — The a d d it i on of this syntax redirect s the command output to the file location specified in the U n i v e r s a l Resource L o c at or( URL). The p ip e(|) isr e q u i r e d. The Cisco IOSFile System( IF S) uses URL s to specify the location of a filesystem, directory, andfile. Typical URL e l e m e n t s include: pref i x:[ directory/] file name Pref i x e scan be l o c a l file location s, such as flash: or disk0:. A l t e r n at i v e l y, you can specify network location s using the following syntax: ftp:[[//[ username[: password]@] location]/ directory]/ file name tftp:[[// location]/ directory]/ file name The rcp: pref i x is not supported.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(21)S | This command was introduced. |
| 12.2(13)T | This command was integrated into Cisco IOS Release12.2(13) T. |

**Usage Guidelines:**

To display all URL prefixes that are supported for this command, use the showcommand| append ? command. This command adds the show command output to the end of the specified file.

**Example:**

In the following example, output from the show tech-support command is redirected to an existing file on Disk 1 with the file-name of “showoutput.txt.” This output is added at the end of any existing data in the file.

```text
show tech-support | append disk1:showoutput.txt
```


### `show command begin`

> **Página:** 530 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** in EXEC mode.

**Syntax:**

```text
To begin the output of any showcommand from a specified string, use the show command | begin command
{show command | begin regular-expression}
```

**Parameters (Syntax Description):**

- `command` — Any supported show command.
- `|` — A v e r t i c a l b a r( the“ p ip e” s y m b o l) in d i c at e s that an output process in g s p e c if i c at i on follows.
- `regular-expression` — Any r e g u l are x p r e s s i on f o u n d in show command output. The show output will begin from the first in s t an c e of this string( output p r i or to this string will not be p r in t e d to the screen). The string is c as e-s e n s it i v e. Use p are n the s is to in d i c at e a lite r a l use of spaces.
- `/` — Specifies as e a r c h at a--More--prompt that begin s u n f i l t e r e do u t p u t with the first line that c on t a in s the r e g u l are x p r e s s i on.
- `-` — Specifies a f i l t e r at a--More--prompt that only d is p l a y s output lines that do not c on t a in the r e g u l are x p r e s s i on.
- `+` — Specifies a f i l t e r at a--More--prompt that only d is p l a y s output lines that c on t a in the r e g u l are x p r e s s i on.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 8.3 | The show command was introduced. |
| 12.0(1)T | This e x t e n s i on of the show command was introduced.. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The regular-expressionargument is case sensitive and allows for complex matching requirements. Use parenthesis to indicate a literal use of spaces. For example, | begin u indicates that the show output should begin with any line that contains a u; | begin ( u) indicates that the show output should begin with any line that contains a space and a u together (line has a word that begins with a lowercase u). To search the remaining output of the show command, use the following command at the --More-- prompt: / regular-expression You can specify a filtered search at any --More-- prompt. To filter the remaining output of the show command, use one of the following commands at the --More-- prompt: - regular-expression + regular-expression When output volume is large, the search can produce long lists of output. To interrupt the output, press Ctrl-^ (Ctrl-Shift-6) or Ctrl-z. Note Once you specify a filter for a show command, you cannot specify another filter at the next --More-- prompt. The first specified filter remains until the more command output finishes or until you interrupt the output. The use of the keyword begin does not constitute a filter. Because prior output is not saved, you cannot search or filter backward through prior output. Note A few show commands that have long output requirements do not require user input at the --More-- prompt to jump to the next table of output; these types of output require you to enter the same number of Ctrl-^ or Ctrl-Z combinations as there are --More-- prompts to completely terminate output.

**Example:**

The following is partial sample output of the show interface | begincommand that begins unfiltered output with the first line that contains the regular expression “Ethernet.” At the --More-- prompt, the user specifies a filter to show only the lines in the remaining output that contain the regular expression “Serial.”

```text
Router# show interface | begin Ethernet
Ethernet0 is up, line protocol is up
Hardware is Lance, address is 0060.837c.6399 (bia 0060.837c.6399)
Description: ip address is 172.1.2.14 255.255.255.0
Internet address is 172.1.2.14/24
0 lost carrier, 0 no carrier
0 output buffer failures, 0 output buffers swapped out
--More--
+Serial
filtering...
Serial1 is up, line protocol is up
Serial2 is up, line protocol is up
Serial3 is up, line protocol is down
Serial4 is down, line protocol is down
Serial5 is up, line protocol is up
Serial6 is up, line protocol is up
Serial7 is up, line protocol is up
```


### `show command exclude`

> **Página:** 532 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To filter showcommand output so that it excludes lines that contain a particular regular expression, use the

**Syntax:**

```text
show command | exclude command in EXEC mode.
{show command | exclude regular-expression}
```

**Parameters (Syntax Description):**

- `command` — Any supported show command.
- `|` — A v e r t i c a l b a r( the“ p ip e” s y m b o l) in d i c at e s that an output process in g s p e c if i c at i on follows.
- `regular-expression` — Any r e g u l are x p r e s s i on f o u n d in show command output.
- `/` — Specifies as e a r c h at a--More--prompt that begin s u n f i l t e r e do u t p u t with the first line that c on t a in s the r e g u l are x p r e s s i on.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(1)T | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The regular-expression argument is case sensitive and allows for complex matching requirements. You can specify a new search at every --More-- prompt. To search the remaining output of the show command, use the following syntax at the --More-- prompt: / regular-expression When output volume is large, the search can produce long lists of output. To interrupt the output, press Ctrl-^ (Ctrl-Shift-6) or Ctrl-Z. Because prior output is not saved, you cannot search or filter backward through prior output. Note A few show commands that have long output requirements do not require user input at the --More-- prompt to jump to the next table of output; these types of output require you to enter the same number of Ctrl-^ or Ctrl-Z combinations as there are --More-- prompts to completely terminate output.

**Example:**

The following is partial sample output of the show | excludecommand used with the show bufferscommand. It excludes lines that contain the regular expression “0 misses.” At the --More-- prompt, the user searches for the regular expression “Serial0,” which continues the filtered output with the first line that contains “Serial0.”

```text
Router# show buffers | exclude 0 misses
Buffer elements:
398 in free list (500 max allowed)
Public buffer pools:
Small buffers, 104 bytes (total 50, permanent 50):
50 in free list (20 min, 150 max allowed)
551 hits, 3 misses, 0 trims, 0 created
Big buffers, 1524 bytes (total 50, permanent 50):
49 in free list (5 min, 150 max allowed)
Very Big buffers, 4520 bytes (total 10, permanent 10):
Huge buffers, 18024 bytes (total 0 permanent 0):
0 in free list (0 min, 4 max allowed)
--More--
/Serial0
filtering...
Serial0 buffers, 1543 bytes (total 64, permanent 64):
16 in free list (0 min, 64 max allowed)
48 hits, 0 fallbacks
```


### `show command include`

> **Página:** 534 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To filter showcommand output so that it only displays lines that contain a particular regular expression, use

**Syntax:**

```text
the show command | include command in EXEC mode.
{show command | include regular-expression}
```

**Parameters (Syntax Description):**

- `command` — Any supported show command.
- `|` — A v e r t i c a l b a r( the“ p ip e” s y m b o l) in d i c at e s that an output process in g s p e c if i c at i on follows.
- `regular-expression` — Any r e g u l are x p r e s s i on f o u n d in show command output. Use p are n the s is to include space s in the e x p r e s s i on.
- `/` — Specifies as e a r c h at a--More--prompt that begin s u n f i l t e r e do u t p u t with the first line that c on t a in s the r e g u l are x p r e s s i on.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(1)T | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The regular-expression argument is case sensitive and allows for complex matching requirements. You can specify a new search at every --More-- prompt. To search the remaining output of the show command, use the following syntax at the --More-- prompt: / regular-expression When output volume is large, the search can produce long lists of output. To interrupt the output, press Ctrl-^ (Ctrl-Shift-6) or Ctrl-Z. Because prior output is not saved, you cannot search or filter backward through prior output. Note A few show commands that have long output requirements do not require user input at the --More-- prompt to jump to the next table of output; these types of output require you to enter the same number of Ctrl-^ or Ctrl-Z combinations as there are --More-- prompts to completely abort output.

**Example:**

The following is partial sample output of the show interface | includecommand. It displays only lines that contain the regular expression “( is ).” The parentheses force the inclusion of the spaces before and after “is.” Use of the parenthesis ensures that only lines containing “is” with a space both before and after it will be included in the output. Lines with words like “disconnect” will be excluded because there are not spaces around the instance of the string “is”.

```text
show interface | include ( is )
ATM0 is administratively down, line protocol is down
Hardware is ATMizer BX-50
Dialer1 is up (spoofing), line protocol is up (spoofing)
Hardware is Unknown
DTR is pulsed for 1 seconds on reset
Ethernet0 is up, line protocol is up
Hardware is Lance, address is 0060.837c.6399 (bia 0060.837c.6399)
Internet address is 172.21.53.199/24
Ethernet1 is up, line protocol is up
Hardware is Lance, address is 0060.837c.639c (bia 0060.837c.639c)
Internet address is 5.5.5.99/24
Serial0:0 is down, line protocol is down
Hardware is DSX1
--More--
```

At the --More-- prompt, the user searches for the regular expression “Serial0:13”, which continues filtered output with the first line that contains “Serial0:13.”

```text
/Serial0:13
filtering...
Serial0:13 is down, line protocol is down
Hardware is DSX1
Internet address is 11.0.0.2/8
0 output errors, 0 collisions, 2 interface resets
Timeslot(s) Used:14, Transmitter delay is 0 flags
```


### `show command redirect`

> **Página:** 536 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** EXEC mode.

**Syntax:**

```text
To redirect the output of any show command to a file, use the show command | redirectcommand in privileged
{show command | redirect url}
```

**Parameters (Syntax Description):**

- `command` — Any Cisco IOS show command.
- `|redirect url` — The a d d it i on of this syntax redirect s the command output to the file location specified in the U n i v e r s a l Resource L o c at or( URL). The p ip e(|) isr e q u i r e d. The Cisco IOSFile System( IF S) uses URL s to specify the location of a filesystem, directory, and file. Typical URL e l e m e n t s include: pref i x:[ directory/] file name Pref i x e scan be l o c a l file location s, such as flash: or disk0:. A l t e r n at i v e l y, you can specify network location s using the following syntax: ftp:[[//[ username[: password]@] location]/ directory]/ file name tftp:[[// location]/ directory]/ file name The rcp: pref i x is not supported.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(21)S | This command was introduced. |
| 12.2(13)T | This command was integrated into Cisco IOS Release12.2(13) T. |

**Usage Guidelines:**

To display all URL prefixes that are supported for this command, use the showcommand| redirect ? command. This command creates a new file at the specified location, or overwrites an existing file.

**Example:**

In the following example, output from the show tech-support command is write to the file “showtech.txt” on the host at 172.16.101.101 in the directory “//tftpboot/docs/” using FTP:

```text
show tech | redirect ftp://USER:MYPASSWORD@172.16.101.101//tftpboot/docs/showtech.txt
```


### `show command section`

> **Página:** 537 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To filter the output of a show command to match a given expression as well as any lines associated with that

**Syntax:**

```text
expression, use the showcommand sectioncommand in privileged EXEC mode.
{show command | section [include | exclude] regular-expression}
```

**Parameters (Syntax Description):**

- `command` — Any Cisco IOS show command.
- `include` — ( Optional) Include s only the lines that c on t a in apa r t i c u l a r r e g u l are x p r e s s i on. Thisis the default keyword when none is specified.
- `exclude` — ( Optional) Exclude s any lines that c on t a in apa r t i c u l a r r e g u l are x p r e s s i on.
- `regular-expression` — Any r e g u l are x p r e s s i on or p l a in text string f o u n d in show command output. The syntax of the r e g u l are x p r e s s i on c on forms to that of Bell V8 regexp(3).

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(2)T | This command was introduced. |

**Usage Guidelines:**

In many cases, it is useful to filter the output of a show command to match a specific expression. Filtering provides some control over the type and amount of information displayed by the system. The show section command provides enhanced filtering capabilities by matching lines in the show command output containing specific expressions as well as matching any entries associated with those expressions. Filtering is especially useful, for example, when displaying large configuration files using the show running-configuration command or the show interfaces command. If the include or exclude keyword is not specified, include is the default. If there are no associated entries for an expression, then only the line matching the expression is displayed.

**Example:**

The following examples compare the filtering characteristics of the show running-config | include command with the show running-config | section command. The first example gathers just the lines from the configuration file with “interface” in them.

```text
Router# show running-config | include interface
interface Ethernet0/0
interface Ethernet1/0
interface Serial2/0
interface Serial3/0
```

The next example uses the showcommand sectioncommand to gather the lines in the configuration file with “interface” in them as well as any lines associated with those entries. In this example, interface configuration information is captured.

```text
Router# show running-config | section include interface
interface Ethernet0/0
shutdown
no cdp enable
interface Ethernet1/0
shutdown
no cdp enable
interface Serial2/0
shutdown
no cdp enable
interface Serial3/0
shutdown
no cdp enable
```


### `show command tee`

> **Página:** 538 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** | teecommand in privileged EXEC mode.

**Syntax:**

```text
To copy the output of any show command to a file while displaying it on the terminal, use the show command
{show command | tee [/append] url}
```

**Parameters (Syntax Description):**

- `command` — Any Cisco IOS show command.
- `|tee url` — The a d d it i on of this syntax c o p i e s the command output to the file location specified in the U n i v e r s a l Resource L o c at or( URL). The p ip e(|) isr e q u i r e d. The Cisco IOSFile System( IF S) uses URL s to specify the location of a filesystem, directory, andfile. Typical URL e l e m e n t s include: pref i x:[ directory/] file name Pref i x e scan be l o c a l file location s, such as flash: or disk0:. A l t e r n at i v e l y, you can specify network location s using the following syntax: ftp:[[//[ username[: password]@] location]/ directory]/ file name tftp:[[// location]/ directory]/ file name The rcp: pref i x is not supported.
- `/append` — ( Optional) A d d s the show command output to the end of an e x is t in g file.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.0(21)S | This command was introduced. |
| 12.2(13)T | This command was integrated into Cisco IOS Release12.2(13) T. |

**Usage Guidelines:**

To display all URL prefixes that are supported for this command, use the showcommand| tee ? command. The tee keyword was chosen to reflect that output is redirected to two locations; the terminal and a file (as a tee plumbing junction redirects water to two different pipes).

**Example:**

In the following example, output from the show tech-support command is displayed on-screen while it is written to the file “showoutput.txt” at the host 172.16.101.101 using TFTP:

```text
Router# show tech-support | tee tftp://172.16.101.101/docs/showoutput.txt
```

The following example performs the same function as above, but in this case the output is added at the end of any existing data in the file “showoutput.txt”:

```text
Router# show tech-support | tee /append tftp://172.16.101.101/docs/showoutput.txt
```


### `show (Flash file system)`

> **Página:** 539 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** EXEC mode. Class A Flash File Systems Class B Flash File Systems Class C Flash File Systems

**Syntax:**

```text
To display the layout and contents of a Flash memory file system, use the show flash-filesystem command in
show flash-filesystem:[all | chips | filesys]
show flash-filesystem:[partition-number:] [all | chips | detailed | err | summary]
show flash-filesystem :
```

**Parameters (Syntax Description):**

- `flash-filesystem :` — Flash memory filesystem, f o l low e d by a c o l on. The a v a i l a b l it y of Flash filesystem keywords will v a r y by platform. V a l id flash filesystem keywords in l u d e: • bootflash •flash •slot0 •slot1 • slave bootflash • slave slot0 • slave slot1
- `all` — ( Optional) On Class B Flash filesystem s, all keyword d is p l a y s c o m p l e t e information about Flash memory, in c l u d in g information about the in d i v id u a l ROM device s in Flash memory and then a m e s and size s of all system image files s to r e d in Flash memory, in c l u d in gt h o set h at are in v a l id. On Class A Flash filesystem s, the all keyword d is p l a y s the following information: • The information d is p l a y e d when no keywords are used. • The information d is p l a y e d by the files y s keyword. • The information d is p l a y e d by the c h ip s keyword.
- `chips` — ( Optional) D is p l a y s information p e r partition and p e r c h ip, in c l u d in g which b an k the c h ip is in, p l u s its code, size, and name.
- `filesys` — ( Optional) D is p l a y s the Device Info B lock, the Status Info, and the Usage Info.
- `partition-number` — ( Optional) D is p l a y s output for the specified partition number. If you do not specify a partition in the command, the router d is p l a y s output for all partition s. You can use this keyword only when Flash memory has m u l t ip l e partition s.
- `detailed` — ( Optional) D is p l a y s detailed file directory information p e r partition, in c l u d in g file length, address, name, Flash memory check s u m, c o m p u t e r check s u m, by t e s used, by t e s a v a i l a b l e, to t a l by t e s, and by t e s of system Flash memory.
- `err` — ( Optional) D is p l a y s write or erase failures in the form of number of retries.
- `summary` — ( Optional) D is p l a y s summary information p e r partition, in c l u d in gt h e partition size, b an k size, state, and m e t h o d by which files can be c o p i e d into apa r t i c u l a r partition. You can use this keyword only when Flash memory has m u l t ip l e partition s.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | This command was introduced. |
| 12.3 | At i m e s t a m p that shows the of f set from C o or d in at e d U n i v e r s a l Time( U T C) was added to the show command d is p l a y. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If Flash memory is partitioned, the command displays the requested output for each partition, unless you use the partition keyword. The command also specifies the location of the current image. To display the contents of boot Flash memory on Class A or B file systems, use the show bootflash: command as follows: Class A Flash file systems show bootflash: [all | chips | filesys] Class B Flash file systems show bootflash: [partition-number] [all | chips | detailed | err To display the contents of internal Flash memory on Class A or B file systems, use the show flash: command as follows: Class A Flash file systems show flash: all | chips | filesys] Class B Flash file systems show flash: [partition-number][all | chips | detailed | err | summary] The show(Flash file system) command replaces the show flash devices command.

**Example:**

The output of the showcommand depends on the type of Flash file system you select. Types include flash:, bootflash:, slot0:, slot1:, slavebootflash:, slaveslot0:, and slaveslot1:. Examples of output from the show flashcommand are provided in the following sections: • Class A Flash File System • Class B Flash File Systems Although the examples use flash: as the Flash file system, you may also use the other Flash file systems listed. Class A Flash File System The following three examples show sample output for Class A Flash file systems. The table below describes the significant fields shown in the display. The following is sample output from the show flash: command.

```text
Router# show flash:
-#- ED --type-- --crc--- -seek-- nlen -length- -----date/time------ name
1 .. unknown 317FBA1B 4A0694 24 4720148 Dec 15 2003 17:49:36 -08:00
hampton/nitro/c7200-j-mz
2 .. unknown 9237F3FF 92C574 11 4767328 Jan 02 2004 18:42:53 -08:00 c7200-js-mz
3 .D unknown 71AB01F1 10C94E0 10 7982828 Jan 02 2004 18:48:14 -08:00 rsp-jsv-mz
4 .D unknown 96DACD45 10C97E0 8 639 Jan 03 2004 12:09:17 -08:00 the_time
5 .. unknown 96DACD45 10C9AE0 3 639 Jan 03 2004 12:09:32 -08:00 the_time
6 .D unknown 96DACD45 10C9DE0 8 639 Jan 03 2004 12:37:01 -08:00 the_time
7 .. unknown 96DACD45 10CA0E0 8 639 Jan 03 2004 12:37:13 -08:00 the_time
3104544 bytes available (17473760 bytes used)
```

| Field | Description |
| --- | --- |
| # | Indexnumberforthefile. |
| ED | Whetherthefilecontainsanerror(E)orisdeleted(D). |
| type | Filetype(1=configurationfile,2=imagefile).Thesoftwaredisplaysthesevaluesonlywhen thefiletypeiscertain.Whenthefiletypeisunknown,thesystemdisplays“unknown”inthis field. |
| crc | Cyclicredundantcheckforthefile. |
| seek | Offsetintothefilesystemofthenextfile. |
| nlen | Namelength--Lengthofthefilename. |
| length | Lengthofthefileitself. |
| date/time | Dateandtimethefilewascreated.Intheexample,-08:00indicatesthatthegivendateandtime is8hoursbehindCoordinatedUniversalTime(UTC). |
| name | Nameofthefile. |

The following is sample output from the show flash: chips command:

```text
RouterA# show flash: chips
******** Intel Series 2+ Status/Register Dump ********
ATTRIBUTE MEMORY REGISTERS:
Config Option Reg (4000): 2
Config Status Reg (4002): 0
Card Status Reg (4100): 1
Write Protect Reg (4104): 4
Voltage Cntrl Reg (410C): 0
Rdy/Busy Mode Reg (4140): 2
COMMON MEMORY REGISTERS: Bank 0
Intelligent ID Code : 8989A0A0
Compatible Status Reg: 8080
Global Status Reg: B0B0
Block Status Regs:
0 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
8 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
16 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
24 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
COMMON MEMORY REGISTERS: Bank 1
Intelligent ID Code : 8989A0A0
Compatible Status Reg: 8080
Global Status Reg: B0B0
Block Status Regs:
0 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
8 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
16 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
24 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
COMMON MEMORY REGISTERS: Bank 2
Intelligent ID Code : 8989A0A0
Compatible Status Reg: 8080
Global Status Reg: B0B0
Block Status Regs:
0 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
8 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
16 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
24 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
COMMON MEMORY REGISTERS: Bank 3
Intelligent ID Code : 8989A0A0
Compatible Status Reg: 8080
Global Status Reg: B0B0
Block Status Regs:
0 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
8 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
16 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
24 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
COMMON MEMORY REGISTERS: Bank 4
Intelligent ID Code : 8989A0A0
Compatible Status Reg: 8080
Global Status Reg: B0B0
Block Status Regs:
0 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
8 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
16 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
24 : B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0 B0B0
```

The following is sample output from the show flash: filesys command:

```text
RouterA# show flash: filesys
-------- F I L E S Y S T E M S T A T U S --------
Device Number = 0
DEVICE INFO BLOCK:
Magic Number = 6887635 File System Vers = 10000 (1.0)
Length = 1400000 Sector Size = 20000
Programming Algorithm = 4 Erased State = FFFFFFFF
File System Offset = 20000 Length = 13A0000
MONLIB Offset = 100 Length = C730
Bad Sector Map Offset = 1FFEC Length = 14
Squeeze Log Offset = 13C0000 Length = 20000
Squeeze Buffer Offset = 13E0000 Length = 20000
Num Spare Sectors = 0
Spares:
STATUS INFO:
Writable
NO File Open for Write
Complete Stats
No Unrecovered Errors
No Squeeze in progress
USAGE INFO:
Bytes Used = 10AA0E0 Bytes Available = 2F5F20
Bad Sectors = 0 Spared Sectors = 0
OK Files = 4 Bytes = 90C974
Deleted Files = 3 Bytes = 79D3EC
Files w/Errors = 0 Bytes = 0
```

The following is sample output from the show flash:command:

```text
RouterB> show flash:
System flash directory:
File Length Name/status
1 4137888 c3640-c2is-mz.Feb24
[4137952 bytes used, 12639264 available, 16777216 total]
16384K bytes of processor board System flash (Read/Write)\
```

The following example shows detailed information about the second partition in internal Flash memory:

```text
RouterB#
show flash:2
System flash directory, partition 2:
File Length Name/status
1 1711088 dirt/images/c3600-i-mz
[1711152 bytes used, 15066064 available, 16777216 total]
16384K bytes of processor board System flash (Read/Write)
```

Class B Flash File Systems The table below describes the significant fields shown in the displays.

| Field | Description |
| --- | --- |
| addr | AddressofthefileinFlashmemory. |
| available | TotalnumberofbytesavailableinFlashmemory. |
| Bank | Banknumber. |
| Bank-Size | Sizeofbankinbytes. |
| bytesused | TotalnumberofbytesusedinFlashmemory. |
| ccksum | Computedchecksum. |
| Chip | Chipnumber. |
| Code | Codenumber. |
| Copy-Mode | Methodbywhichthepartitioncanbecopiedto: •RXBOOT-MANUALindicatesausercancopymanuallybyreloadingtothe bootROMimage. •RXBOOT-FLHindicatesusercancopyviaFlashloadhelper. •DirectindicatesusercancopydirectlyintoFlashmemory. •Noneindicatesthatitisnotpossibletocopyintothatpartition. |
| fcksum | ChecksumrecordedinFlashmemory. |

| Field | Description |
| --- | --- |
| File | Numberofthesystemimagefile.Ifnofilenameisspecifiedinthebootsystem flashcommand,therouterbootsthesystemimagefilewiththelowestfilenumber. |
| Free | Numberofbytesfreeinpartition. |
| Length | Sizeofthesystemimagefile(inbytes). |
| Name | Nameofchipmanufacturerandchiptype. |
| Name/status | Filenameandstatusofasystemimagefile.Thestatus[invalidated]appearswhen afilehasbeenrewritten(recopied)intoFlashmemory.Thefirst(nowinvalidated) copyofthefileisstillpresentwithinFlashmemory,butitisrenderedunusablein favorofthenewestversion.The[invalidated]statuscanalsoindicateanincomplete filethatresultsfromtheuserabnormallyterminatingthecopyprocess,anetwork timeout,oraFlashmemoryoverflow. |
| Partition | PartitionnumberinFlashmemory. |
| Size | Sizeofpartition(inbytes)orsizeofchip. |
| State | Stateofthepartition.Itcanbeoneofthefollowingvalues: •Read-Onlyindicatesthepartitionthatisbeingexecutedfrom. •Read/Writeisapartitionthatcanbecopiedto. |
| Systemflashdirectory | Flashdirectoryanditscontents. |
| total | TotalsizeofFlashmemory(inbytes). |
| Used | Numberofbytesusedinpartition. |

The following is sample output from the show flash: all command:

```text
RouterB> show flash: all
Partition Size Used Free Bank-Size State Copy Mode
1 16384K 4040K 12343K 4096K Read/Write Direct
System flash directory:
File Length Name/status
addr fcksum ccksum
1 4137888 c3640-c2is-mz.Feb24
0x40 0xED65 0xED65
[4137952 bytes used, 12639264 available, 16777216 total]
16384K bytes of processor board System flash (Read/Write)
Chip Bank Code Size Name
1 1 01D5 1024KB AMD 29F080
2 1 01D5 1024KB AMD 29F080
3 1 01D5 1024KB AMD 29F080
4 1 01D5 1024KB AMD 29F080
1 2 01D5 1024KB AMD 29F080
2 2 01D5 1024KB AMD 29F080
3 2 01D5 1024KB AMD 29F080
4 2 01D5 1024KB AMD 29F080
1 3 01D5 1024KB AMD 29F080
2 3 01D5 1024KB AMD 29F080
3 3 01D5 1024KB AMD 29F080
4 3 01D5 1024KB AMD 29F080
1 4 01D5 1024KB AMD 29F080
2 4 01D5 1024KB AMD 29F080
3 4 01D5 1024KB AMD 29F080
4 4 01D5 1024KB AMD 29F080
```

The following is sample output from the show flash: all command on a router with Flash memory partitioned:

```text
Router# show flash: all
System flash partition information:
Partition
Size Used Free Bank-Size State Copy-Mode
4096K 3459K 637K 4096K Read Only RXBOOT-FLH
4096K 3224K 872K 4096K Read/Write Direct
System flash directory, partition 1:
File Length Name/status
addr fcksum ccksum
1 3459720 master/igs-bfpx.100-4.3
0x40 0x3DE1 0x3DE1
[3459784 bytes used, 734520 available, 4194304 total]
4096K bytes of processor board System flash (Read ONLY)
Chip Bank Code Size Name
1 1 89A2 1024KB INTEL 28F008SA
2 1 89A2 1024KB INTEL 28F008SA
3 1 89A2 1024KB INTEL 28F008SA
4 1 89A2 1024KB INTEL 28F008SA
Executing current image from System flash [partition 1]
System flash directory, partition2:
File Length Name/status
addr fcksum ccksum
1 3224008 igs-kf.100
0x40 0xEE91 0xEE91
[3224072 bytes used, 970232 available, 4194304 total]
4096K bytes of processor board System flash (Read/Write)
Chip Bank Code Size Name
1 2 89A2 1024KB INTEL 28F008SA
2 2 89A2 1024KB INTEL 28F008SA
3 2 89A2 1024KB INTEL 28F008SA
4 2 89A2 1024KB INTEL 28F008SA
```

The following is sample output from the show flash: chips command:

```text
RouterB> show flash: chips
16384K bytes of processor board System flash (Read/Write)
Chip Bank Code Size Name
1 1 01D5 1024KB AMD 29F080
2 1 01D5 1024KB AMD 29F080
3 1 01D5 1024KB AMD 29F080
4 1 01D5 1024KB AMD 29F080
1 2 01D5 1024KB AMD 29F080
2 2 01D5 1024KB AMD 29F080
3 2 01D5 1024KB AMD 29F080
4 2 01D5 1024KB AMD 29F080
1 3 01D5 1024KB AMD 29F080
2 3 01D5 1024KB AMD 29F080
3 3 01D5 1024KB AMD 29F080
4 3 01D5 1024KB AMD 29F080
1 4 01D5 1024KB AMD 29F080
2 4 01D5 1024KB AMD 29F080
3 4 01D5 1024KB AMD 29F080
4 4 01D5 1024KB AMD 29F080
```

The following is sample output from the show flash: detailed command:

```text
RouterB> show flash: detailed
System flash directory:
File Length Name/status
addr fcksum ccksum
1 4137888 c3640-c2is-mz.Feb24
0x40 0xED65 0xED65
[4137952 bytes used, 12639264 available, 16777216 total]
16384K bytes of processor board System flash (Read/Write)
```

The following is sample output from the show flash: err command:

```text
RouterB> show flash: err
System flash directory:
File Length Name/status
1 4137888 c3640-c2is-mz.Feb24
[4137952 bytes used, 12639264 available, 16777216 total]
16384K bytes of processor board System flash (Read/Write)
Chip Bank Code Size Name erase write
1 1 01D5 1024KB AMD 29F080 0 0
2 1 01D5 1024KB AMD 29F080 0 0
3 1 01D5 1024KB AMD 29F080 0 0
4 1 01D5 1024KB AMD 29F080 0 0
1 2 01D5 1024KB AMD 29F080 0 0
2 2 01D5 1024KB AMD 29F080 0 0
3 2 01D5 1024KB AMD 29F080 0 0
4 2 01D5 1024KB AMD 29F080 0 0
1 3 01D5 1024KB AMD 29F080 0 0
2 3 01D5 1024KB AMD 29F080 0 0
3 3 01D5 1024KB AMD 29F080 0 0
4 3 01D5 1024KB AMD 29F080 0 0
1 4 01D5 1024KB AMD 29F080 0 0
2 4 01D5 1024KB AMD 29F080 0 0
3 4 01D5 1024KB AMD 29F080 0 0
4 4 01D5 1024KB AMD 29F080 0 0
```

See the table above for a description of the fields. The show flash: err command also displays two extra fields: erase and write. The erase field indications the number of erase errors. The write field indicates the number of write errors. The following is sample output from the show flash summary command on a router with Flash memory partitioned. The partition in the Read Only state is the partition from which the Cisco IOS image is being executed.

```text
Router# show flash summary
System flash partition information:
Partition Size Used Free Bank-Size State Copy-Mode
1 4096K 2048K 2048K 2048K Read Only RXBOOT-FLH
2 4096K 2048K 2048K 2048K Read/Write Direct
```


### `show aliases`

> **Página:** 548 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display all alias commands, or the alias commands in a specified mode, use the show aliases command in EXEC mode.

**Syntax:**

```text
show aliases [mode]
```

**Parameters (Syntax Description):**

- `mode` — ( Optional) Name of as p e c if i c command or configuration mode. Specifies that only aliases configure d for this modes h o u l d be d is p l a y e d.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

When used without the mode argument, this command will display all aliases currently configured on the system. Use the mode argument to display only the aliases configured for the specified command mode. To display a list of the command mode keywords available for your system, use the show aliases ? command. The following is sample output from the show aliases exec commands. The aliases configured for commands in EXEC mode are displayed.

```text
Router> show aliases exec
Exec mode aliases:
h help
lo logout
p ping
r resume
s show
w where
```


### `show alignment`

> **Página:** 548 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display alignment errors and spurious memory access errors, use the show alignment command in privileged EXEC mode.

**Syntax:**

```text
show alignment
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(7)T | This command was introduced. |
| 12.2(22)S | This command was integrated into Cisco IOS Release12.2(22) S. |
| 12.2(18)SXE | This command was integrated into Cisco IOS Release12.2(18) S X E. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Alignment Errors Alignment errors are caused by misaligned reads and writes. For example, a two-byte read where the memory address is not an even multiple of two bytes is an alignment error. Alignment errors are caused by a software defect. Alignment errors are reported in the system log and recorded by the device. Output from the show alignment command provides a record of these errors along with potentially useful traceback information. The traceback information for alignment errors can generally be decoded to reveal the function causing the alignment problems. Spurious Memory Access Errors Spurious memory access errors occur when a software process attempts to access memory in a restricted location. A read operation to this region of memory is usually caused when a nonexisting value is returned to a function in the software, or in other words, when a null pointer is passed to a function. Spurious memory access errors are counted and recorded, if possible, by the software. This information is displayed with the show alignment command.

**Example:**

The following is sample output from the show alignment command when alignment detection is disabled. To enable alignment detection, use the enable command to enter privileged EXEC mode.

```text
Device#
show alignment
Unaligned handler is disabled
```

The following is sample output from the show alignment command when there are no alignment or spurious memory errors:

```text
Device# show alignment
No alignment data has been recorded.
No spurious memory references have been recorded.
Device#
```

The following is sample output from the show alignment command when there are only alignment errors. The traceback information is necessary to determine the cause and the fix of the alignment errors.

```text
Device# show alignment
Total Corrections 134, Recorded 1, Reads 134, Writes 0
Initial Initial
Address Count Access Type Traceback
1A014C5 134 32bit read 0x6012F538 0x601338F8 0x601344D8 0x6022D528
No spurious memory references have been recorded.
Device#
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| TotalCorrections | Totalnumberofalignmentcorrectionsmade. |
| Recorded | Numberofalignmententries. |
| Reads | Numberofmisalignedreads. |
| Writes | Numberofmisalignedwrites. |
| InitialAddress | Addressofwherethealignmenterroroccurred. |
| Count | Numberoftimesthealignmentoccurredatthisaddress. |
| InitialAccess | Addressofwherethealignmenterroroccurred. |
| Type | Typeofalignmenterror:readorwrite. |
| Traceback | Thetracebackaddressinformationnecessarytodeterminethecauseofthemisalignment. |

The following is sample output from the show alignmentcommand when there are only spurious memory access errors:

```text
Device# show alignment
No alignment data has been recorded.
Total Spurious Accesses 50, Recorded 3
Address Count Traceback
E 10 0x605351A0 0x603CA084 0x606C4060 0x606D6368 0x60743284 0x60743270
E 20 0x605351A0 0x6036EE7C 0x606C4060 0x606D6368 0x60743284 0x60743270
E 20 0x605351A0 0x603C998C 0x606D53EC 0x606C4060 0x606D6368 0x60743284
Device#
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| TotalSpuriousAccesses | Totalnumberofspuriousmemoryaccessesmade. |
| Recorded | Numberofrecordedspuriousmemoryaccessentries. |
| Address | Addressatwhichthespuriousmemoryaccesserroroccurred. |
| Count | Numberoftimesthespuriousmemoryaccessoccurredateachaddress.Thesum equalstheTotalSpuriousAccesses. |
| Traceback | Thetracebackaddressinformationnecessarytodeterminethecauseofthe misalignment. |

The following is sample output from the show alignmentcommand when there are alignment errors and spurious memory access errors:

```text
Device#
show alignment
Total Corrections 134, Recorded 1, Reads 134, Writes 0
Initial Initial
Address Count Access Type Traceback
1A014C5 134 32bit read 0x6012F538 0x601338F8 0x601344D8 0x6022D528
Total Spurious Accesses 50, Recorded 3
Address Count Traceback
E 10 0x605351A0 0x603CA084 0x606C4060 0x606D6368 0x60743284 0x60743270
E 20 0x605351A0 0x6036EE7C 0x606C4060 0x606D6368 0x60743284 0x60743270
E 20 0x605351A0 0x603C998C 0x606D53EC 0x606C4060 0x606D6368 0x60743284 x60743270
```


### `show archive`

> **Página:** 551 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the files saved in the Cisco configuration archive, use the show archive command in privileged EXEC mode.

**Syntax:**

```text
show archive
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
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Example:**

The following is sample output from the show archive command:

```text
Device# show archive
There are currently 1 archive configurations saved.
The next archive file will be named disk0:myconfig-2
Archive # Name
1 disk0:myconfig-1 <- Most Recent
```

The following is sample output from the show archive command after several archive files of the running configuration have been saved. In this example, the maximum number of archive files to be saved is set to three.

```text
Device# show archive
There are currently 3 archive configurations saved.
The next archive file will be named disk0:myconfig-8
Archive # Name
1 :Deleted
2 :Deleted
3 :Deleted
4 :Deleted
5 disk0:myconfig-5
6 disk0:myconfig-6
7 disk0:myconfig-7 <- Most Recent
```

The table below describes the significant fields shown in the displays.

| Field | Description |
| --- | --- |
| Archive# | IndicatesthenumberoftherunningconfigurationfilesavedtotheCiscoconfigurationarchive. Youcansetthemaximumnumberofarchivefilesoftherunningconfigurationtobesavedin theconfigurationarchive.Themostrecentarchivefileisthelastoneshowninthedisplay. |
| Name | IndicatesthenameoftherunningconfigurationfilesavedtotheCiscoconfigurationarchive. |


### `show archive config differences`

> **Página:** 553 · **Modo:** User EXEC Privileged EXEC · **Default:** If the filename1(path) and filename2(path) arguments are not specified, the first configuration file is assumed to be the running configuration file and the second to be the startup configuration file. If only the filename1(path)argument is specified, the second configuration file is assumed to be the running configuration file. · **Leitura (show/clear/…):** sim

**Description:** To perform a line-by-line comparison of any two configuration files (accessible through the Cisco IOS File System [IFS]) and generate a list of the differences between them, use the show archive config differences command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show archive config differences [filename1(path)[filename2(path)] [ignorecase]]
```

**Parameters (Syntax Description):**

- `file name1( path)` — ( Optional) The file name( path) of the first configuration file. Can be files in the following location s: bootflash:, cns:, f p d:, ftp:, h a r d disk:, http:, https:, n u l l:, nvram:, o b f l:, p r a m:, rcp:, r e v r c s f:, scp:, s t by-bootflash:, s t by-h a r d disk:, s t by-nvram:, s t by-o b f l:, s t by-r c s f:, s t by-usb0:, s t by-usb1:, system:, tar:, tftp:, t m p s y s:, usb0:
- `file name2( path)` — ( Optional) The file name of these c on d configuration file. Can be files in the following location s: bootflash:, cns:, f p d:, ftp:, h a r d disk:, http:, https:, n u l l:, nvram:, o b f l:, p r a m:, rcp:, r e v r c s f:, scp:, s t by-bootflash:, s t by-h a r d disk:, s t by-nvram:, s t by-o b f l:, s t by-r c s f:, s t by-usb0:, s t by-usb1:, system:, tar:, tftp:, t m p s y s:, usb0:
- `i g nor e c as e` — ( Optional) In d i c at e s that the c as e of the file names should be i g nor e d.

**Command Default:** If the filename1(path) and filename2(path) arguments are not specified, the first configuration file is assumed to be the running configuration file and the second to be the startup configuration file. If only the filename1(path)argument is specified, the second configuration file is assumed to be the running configuration file.

**Command Modes:** User EXEC Privileged EXEC

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

Interpreting the output of the show archive config differences command is dependent on the order in which the two files are configured. Each entry in the generated output list is prefixed with a unique text symbol to indicate the type of difference found. The text symbols and their meanings are as follows: • A minus symbol (-) indicates that the configuration line exists in filename1(path) but not in filename2(path). • A plus symbol (+) indicates that the configuration line exists in filename2(path) but not in filename1(path). • An exclamation point (!) with descriptive comments is used to identify order-sensitive configuration lines whose location is different in filename1(path) than in filename2(path).

**Example:**

In this example, a diff operation is performed on the running and startup configuration files. The table below shows the configuration files used for this example.

| RunningConfigurationFile | StartupConfigurationFile |
| --- | --- |
| no ip subnet-zero ip cef interface Ethernet1/0 ip address 10.7.7.7 255.0.0.0 no ip route-cache no ip mroute-cache duplex half no ip classless snmp-server community public RO | ip subnet-zero ip cef ip name-server 10.4.4.4 voice dnis-map 1 dnis 111 interface Ethernet1/0 no ip address no ip route-cache no ip mroute-cache shutdown duplex half ip default-gateway 10.5.5.5 ip classless access-list 110 deny ip any host 10.1.1.1 access-list 110 deny ip any host 10.1.1.2 access-list 110 deny ip any host 10.1.1.3 snmp-server community private RW |

The following is sample output from the show archive config differences command. This sample output displays the results of the diff operation performed on the configuration files in the table above.

```text
Device# show archive config differences running-config startup-config
+ip subnet-zero
+ip name-server 10.4.4.4
+voice dnis-map 1
+dnis 111
interface Ethernet1/0
+no ip address
+shutdown
+ip default-gateway 10.5.5.5
+ip classless
+access-list 110 deny ip any host 10.1.1.1
+access-list 110 deny ip any host 10.1.1.2
+access-list 110 deny ip any host 10.1.1.3
+snmp-server community private RW
-no ip subnet-zero
interface Ethernet1/0
-ip address 10.7.7.7 255.0.0.0
-no ip classless
-snmp-server community public RO
```


### `show archive config incremental-diffs`

> **Página:** 555 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To perform a line-by-line comparison of a specified configuration file to the running configuration file and generate a list of the configuration lines that do not appear in the running configuration file, use the show archive config incremental-diffs command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show archive config incremental-diffs file
```

**Parameters (Syntax Description):**

- `file` — The file name of the configuration file to be c o m p are d to the running configuration file.
- `file` — The file name of the configuration file to be c o m p are d to the running configuration file.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

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

When an incremental diff operation is performed, a list of the configuration lines that do not appear in the running configuration file (in other words, configuration lines that only appear in the specified file that is being compared to the running configuration file) is generated as output. An exclamation point (!) with descriptive comments is used to identify order-sensitive configuration lines whose location is different in the specified configuration file than in the running configuration file.

**Example:**

In this example, an incremental diff operation is performed on the startup and running configuration files. The table below shows the configuration files used for this example.

| StartupConfigurationFile | RunningConfigurationFile |
| --- | --- |
| ip subnet-zero ip cef ip name-server 10.4.4.4 voice dnis-map 1 dnis 111 interface Ethernet1/0 no ip address no ip route-cache no ip mroute-cache shutdown duplex half ip default-gateway 10.5.5.5 ip classless access-list 110 deny ip any host 10.1.1.1 access-list 110 deny ip any host 10.1.1.2 access-list 110 deny ip any host 10.1.1.3 snmp-server community private RW | no ip subnet-zero ip cef interface Ethernet1/0 ip address 10.7.7.7 255.0.0.0 no ip route-cache no ip mroute-cache duplex half no ip classless snmp-server community public RO |

The following is sample output from the show archive config incremental-diffs command. This sample output displays the results of the incremental diff operation performed on the configuration files in the above table.

```text
Device# show archive config incremental-diffs nvram:startup-config
ip subnet-zero
ip name-server 10.4.4.4
voice dnis-map 1
dnis 111
interface Ethernet1/0
no ip address
shutdown
ip default-gateway 10.5.5.5
ip classless
access-list 110 deny ip any host 10.1.1.1
access-list 110 deny ip any host 10.1.1.2
access-list 110 deny ip any host 10.1.1.3
snmp-server community private RW
```


### `show archive config rollback timer`

> **Página:** 557 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display settings of the timed rollback, use the command in privileged EXEC mode.

**Syntax:**

```text
show archive config rollback timer
show archive config rollback timer
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(15)T | This command was introduced in Cisco IOS Release12.4(15) T. |
| 12.2(33)SRC | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRC. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1. |

**Usage Guidelines:**

Use the show archive config rollback timercommand to view the timed rollback settings, such as the timer type (idle timer or absolute timer), timer value, and so on, after a timed rollback is configured on a router.

**Example:**

The following is sample output from the show archive config rollback timer command:

```text
show archive config rollback timer
Time configured(or reconfigured): 22:50:48 UTC Sat Feb 21 2009
Timer type: absolute timer
Timer value: 2 min
User: console
```

The table below describes the significant fields in the sample output.

| Field | Description |
| --- | --- |
| Timeconfigured(orreconfigured) | ThetimewithwhichthetimerrefresheseverytimetheENTERkeyis presses. |
| Timertype | Thetypeofthetimer:IdleorAbsolute. |
| Timervalue | Displaysthetime,inminutes,forwhichtowaitforconfirmation. |
| User | Displaystheusername. |


### `show archive log config`

> **Página:** 558 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display entries from the configuration log, use the show archive log config command in privileged EXEC mode.

**Syntax:**

```text
show archive log config {all | record-number [end-number] | user username[ session session-number]
record-number [end-number] | statistics} [provisioning] [contenttype {plaintext | xml}] [persistent]
```

**Parameters (Syntax Description):**

- `all` — D is p l a y s all configuration log e n t r i e s.
- `record-number [end-number]` — D is p l a y s the log entry by r e c or d number. If you specify are c or d number for the optional end-number argument, all log e n t r i e s with r e c or d numbers be t we e n the values enter e d for the r e c or d-number and end-number arguments are d is p l a y e d. V a l id values for the r e c or d-number and end-number arguments range from1 to2147483647.
- `user username` — D is p l a y s log e n t r i e s at t r i but e d to apa r t i c u l a r user.
- `session session-number` — ( Optional) D is p l a y s log e n t r i e s at t r i but e d to apa r t i c u l a r session. V a l id values for these s s i on-number argument range from1 to1000.
- `statistics` — D is p l a y s memory usage information for the configuration log.
- `provision in g` — ( Optional) D is p l a y s configuration logfile information as it would ap p e a r in a configuration file, r at h e r than in t a b u l a r format.
- `c on t e n tty p e` — ( Optional) Specifies the format for the d is p l a y of configuration c h an g e r e s u l t s.
- `p l a in text` — Specifies that the configuration c h an g e r e s u l t s will be format t e d as p l a in text. This keyword ap p e a r s only if the c on t e n tty p e keyword has been enter e d.
- `xml` — Specifies that the configuration c h an g e r e s u l t s will be in e X t e n s i b l e Markup L an g u age( XML) format. This keyword ap p e a r s only if the c on t e n tty p e keyword has been enter e d.
- `persistent` — ( Optional) D is p l a y s the persistent configuration c h an g e s in a config l e t format.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(4)T | This command was introduced. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(27)SBC | This command was integrated into Cisco IOS Release12.2(27) S B C. |
| 12.2(33)SRA | The c on t e n tty p e, p l a in text, xml, and persistent keywords were added. |
| 12.4(11)T | This command was integrated into Cisco IOS Release12.4(11) T. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.2(33)SB | This command with syntax u p d at e d in12.2(33) S R A was integrated into Cisco IOS Release12.2(33) S B. This command was i m p l e m e n t e do n the Cisco10000 series. |
| CiscoIOSXERelease3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

If you do not specify the all keyword, you must specify a record number with the record-number argument. You can optionally specify an end record number with the end-numberargument to display a range of records. If you use the end-number argument to specify a record number that does not exist, all records after the starting record number with a record number lower than that specified with the end-number argument are displayed. Specifying the provisioning keyword results in the display appearing as it would in a configuration file, rather than in tabular format. This output includes commands used to change configuration modes and logged configuration commands. This output can be used to set up another device if desired. Note Any command that is configured internally and not through the standard method such as entered by the user on the console or by copy command will not be logged in the archive logger buffer. Such commands are not shown as a part of the show archive log config all command output.

**Example:**

The following is sample output from the show archive log config command, which displays configuration log entry numbers 1 and 2:

```text
Device# show archive log config 1 2
idx sess user@line Logged command
1 1 user1@console logging enable
2 1 user1@console logging size 200
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| idx | Therecordnumberoftheconfigurationlogentry. |
| sess | Thesessionnumberassociatedwiththeconfigurationlogentry. |
| user@line | Theusernameoftheuserwhoexecutedthecommandthatgeneratedtheconfiguration logentry. |
| Loggedcommand | Thecommandthatwasexecuted. |

The following example results in the display of all configuration log files as they would appear in a configuration file rather than in tabular format. In addition to displaying logged commands, the example shows the commands used to change configuration modes that are required to correctly apply the logged commands.

```text
Device# show archive log config all provisioning
archive
log config
logging enable
logging size 200
```

The following example results in the display of memory usage statistics for the configuration log:

```text
Device# show archive log config statistics
Config Log Session Info:
Number of sessions being tracked: 1
Memory being held: 3910 bytes
Total memory allocated for session tracking: 3910 bytes
Total memory freed from session tracking: 0 bytes
Config Log log-queue Info:
Number of entries in the log-queue: 3
Memory being held in the log-queue: 671 bytes
Total memory allocated for log entries: 671 bytes
Total memory freed from log entries:: 0 bytes
```

The output is self-explanatory. The following example shows the contents of the archive log in XML format:

```text
Device# show archive log config all contenttype xml
<?xml version="1.0" encoding="UTF-8"?>
<configLoggerMsg version="1.0">
<configChanged>
<changeInfo>
<user>jdoe</user>
<async>
<port>con_0</port>
</async>
<when>
<absoluteTime>2003-04-23T20:25:19.847Z</absoluteTime>
</when>
</changeInfo>
<logComment>begin test test1</logComment>
</configChanged>
<configChanged>
<changeInfo>
<user>jdoe</user>
<async>
<port>con_0</port>
</async>
<when>
<absoluteTime>2003-04-23T20:27:19.847Z</absoluteTime>
</when>
</changeInfo>
<changeItem>
<context/>
<enteredCommand>
<cli>interface e0</cli>
</enteredCommand>
<prcResultType>
<prcSuccess>
<change>PRC_CHANGE</change>
</prcSuccess>
</prcResultType>
<oldConfigState>
<cli></cli>
</oldConfigState>
<newConfigState>
<cli>interface e0</cli>
</newConfigState>
</changeItem>
</configChanged>
<configChanged>
<changeInfo>
<user>jdoe</user>
<async>
<port>con_0</port>
</async>
<when>
<absoluteTime>2003-04-23T20:28:19.847Z</absoluteTime>
</when>
</changeInfo>
<changeItem>
<context><cli>interface e0</cli></context>
<enteredCommand>
<cli>ip address 10.1.1.1 255.255.255.0</cli>
</enteredCommand>
<prcResultType>
<prcSuccess>
<change>PRC_CHANGE</change>
</prcSuccess>
</prcResultType>
<oldConfigState/>
<newConfigState>
<cli>ip address 10.1.1.1 255.255.255.0</cli>
</newConfigState>
</changeItem>
</configChanged>
<configChanged>
<changeInfo>
<user>jdoe</user>
<async>
<port>con_0</port>
</async>
<when>
<absoluteTime>2003-04-23T20:29:19.847Z</absoluteTime>
</when>
</changeInfo>
<logComment>end test test1</logComment>
</configChanged>
</configLoggerMsg>
```


### `show as5400`

> **Página:** 562 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the hardware details of an application server, use the show as5400command in privileged EXEC mode.

**Syntax:**

```text
show as5400
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(22)T | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release12.4(22) T. |

**Usage Guidelines:**

The show as5400 command provides complex troubleshooting information that pertains to the platform's shared references rather than to a specific interface.

**Example:**

The following is sample output from the show as5400 command:

```text
Router# show as5400
Hardware Info:
System I/O Controller PLD version: 0x8
Serial Interface Controller PLD version: 0x2
Memory Info:
Memory Installed: 1024 MB
Memory Type is : DDR
Bus Watcher Counters
cor_l2cache_data_ecc_count = 0
bad_l2cache_data_ecc_count = 0
cor_l2cache_tag_ecc_count = 0
bad_l2cache_tag_ecc_count = 0
cor_memory_data_ecc_count = 0
bad_memory_data_ecc_count = 0
bus_errors = 0
System Controller Network Interrupts:
Interrupt Register is at 0xB0020040 (0x0000008000000000)
BCM interrupt mask 0xFF7C03BEFFE0FCC2
Registered Interrupts:
Level Mask Count Data Interrupt Handler
0 0x0000000100000000 0 0x00000000 0x6036C144 (GT96124 Interrupt h)
0 0x0000000000100000 26415 0xC097F6AC 0x60354064 (GigabitEthernet0/1)
0 0x0000000000080000 0 0x66712B8C 0x60354064 (GigabitEthernet0/0)
0 0x0000040000000000 22982406 0x00000000 0x608B2CBC (Low IRQ interrupt)
1 0x0000100000000000 0 0x00000000 0x60085D98 (BCM1125 GPIO12 - BI)
1 0x0000000000000020 0 0xC002880C 0x608C4ABC (SB1125 Timer 3)
1 0x0000000000000010 0 0xC0028744 0x608C4ABC (SB1125 Timer 2)
1 0x0000000000000008 0 0xC002867C 0x608C4ABC (SB1125 Timer 1)
1 0x0000000000000004 0 0xC00285B4 0x608C4ABC (SB1125 Timer 0)
1 0x0000080000000000 22963823 0x00000000 0x608B2F84 (High IRQ interrupt)
3 0x0000800000000000 0 0x00000000 0x60380F88 (OIR Interrupt)
4 0x0000400000000000 0 0x00000000 0x608BD1EC (NRBUS Parity Error)
4 0x0000200000000000 0 0x00000000 0x608BD1EC (IO Error)
4 0x0000004000000000 0 0x00000000 0x608BD1EC (IO_BUS_Parity Error)
4 0x007C00000000E0C2 0 0x00000000 0x608C2FD8 (Spurious Intr ERROR)
4 0x0000000000020000 0 0x00000000 0x608C3A14 (Corrected ECC Error)
4 0x0000000000010000 0 0x00000000 0x608C2A7C (Bad ECC Error Handl)
4 0x0003000000000000 0 0x64A985BC 0x608C2B4C (BCM1125 Host LDT Br)
4 0x0000000000040000 0 0x00000000 0x608C2E04 (BCM1125 IO-Bus Erro)
4 0x0080000000000000 0 0x00000000 0x608C2BD4 (BCM1125 Host PCI Br)
6 0x0000000000000001 0 0x00000000 0x608C2FD8 (Watchdog Timer 0 Ha)
HT 600MHz Retry Count 0
BCM1125H HT Host Bridge, handle=0
BCM bridge, config=0x0
(0x00):dev, vendor id = 0x0002166D
(0x04):status, command = 0x00100107
(0x08):class code, revid = 0x06000003
(0x0C):hdr, lat timer, cls = 0x00010000
(0x18):bus id registers = 0x001B0100
(0x1C):secondary status = 0x00000141
(0x20):mem base/limit = 0x5FF04300
(0x30):io upper limit/base = 0x00010001
(0x34):capabilities ptr = 0x00000040
(0x38):expansion rom bar = 0x00000000
(0x3C):bridge ctrl = 0x00020000
(0x40):LDT cmd, cap id, = 0x20000008
(0x44):Link config/control = 0x00000020
(0x48):Link frequency = 0x801F0423
(0x50):SRIcmd, srirxden, sritxden = 0x50211010
(0x54):SRI tx numerator = 0x0000FFFF
(0x58):SRI rx numerator = 0x0000FFFF
(0x68):Error status/control = 0x00009A49
(0x6C):Tx ctrl, databufalloc = 0x00041515
(0xC8):Tx buffer count max = 0x00FFFFFF
(0xDC):Rx CRC expected = 0xBFFFABE0
(0xF0):Rx CRC received = 0x7FF3FFFD
BCM PCI Host Bridge:
bus_no=0, device_no=0
DeviceID=0x0001, VendorID=0x166D, Cmd=0x0146, Status=0x02A0
Cls=0x06/0x00/0x00, Rev=0x03, LatencyTimer=0x2C, CacheLineSize=0x10
BaseAddr0=0x60000008, BaseAddr1=0x00000000, MaxLat=0x00, MinGnt=0x00
SubsysDeviceID=0x0000, SubsysVendorID=0xFFFF, ErrorAddr=0x00030400
Additional Status = 0x00000020
PLX HT2PCI Bridge A for PCM Tracer & DFC 2,4,6, handle=0
PLX HT7520 bridge, config=0x0
(0x00):dev, vendor id = 0x74501022
(0x04):status, command = 0x02300107
(0x08):class code, revid = 0x06040012
(0x0C):hdr, lat timer, cls = 0x00810000
(0x18):bus id registers = 0xF80E0201
(0x1C):secondary status = 0x02200141
(0x20):mem base/limit = 0x4FF04300
(0x30):io upper limit/base = 0x00010001
(0x34):capabilities ptr = 0x000000A0
(0x3C):bridge ctrl = 0x00020000
(0x40):miscellaneous = 0x00010004
(0x4C):prefetch ctrl = 0x00000446
(0xC0):ht cmd, cap id = 0x00410008
(0xC4):link cfg/ctrl side a = 0x00112020
(0xC8):link cfg/ctrl side b = 0x770020D0
(0xCC):link freq ctrl side a = 0x00350422
(0xD0):link freq ctrl side b = 0x00350402
PLX HT2PCI Bridge B, for DFC 1,3,5,7
(0x00):dev, vendor id = 0x74501022
(0x04):status, command = 0x02300107
(0x08):class code, revid = 0x06040012
(0x0C):hdr, lat timer, cls = 0x00810000
(0x18):bus id registers = 0xF81B0F01
(0x1C):secondary status = 0x022001A1
(0x20):mem base/limit = 0x5FF05000
(0x30):io upper limit/base = 0x00010001
(0x34):capabilities ptr = 0x000000A0
(0x3C):bridge ctrl = 0x00020000
(0x40):miscellaneous = 0x000B0004
(0x4C):prefetch ctrl = 0x00000446
RTC chip is DS1337
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| SystemI/OControllerPLDversion | Theversionoftheprogrammablelogicdevice(PLD)onthesystem. |
| Level | Interruptprioritylevel. |
| Mask | Maskableinterrupt. |
| Count | Interruptcount. |
| Handler | Typeofinterrupthandler. |
| RTCchip | Realtimeclockchiptype. |


### `show async bootp`

> **Página:** 564 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the extended BOOTP request parameters that have been configured for asynchronous interfaces, use the show async bootp command in privileged EXEC mode.

**Syntax:**

```text
show async bootp
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

The following is sample output from the show async bootp command:

```text
show async bootp
The following extended data will be sent in BOOTP responses:
bootfile (for address 192.168.1.1) “pcboot”
bootfile (for address 172.16.1.111) “dirtboot”
subnet-mask 255.255.0.0
time-offset -3600
time-server 192.168.1.1
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| bootfile...“pcboot” | Bootfileforaddress192.168.1.1isnamedpcboot. |
| subnet-mask255.255.0.0 | Subnetmask. |
| time-offset-3600 | Localtimeisonehour(3600seconds)earlierthanUTCtime. |
| time-server192.168.1.1 | Addressofthetimeserverforthenetwork. |


### `show autoupgrade configuration unknown`

> **Página:** 565 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display all of the unknown start-up configuration lines that the auto-upgraded Cisco software image does not understand, use the show autoupgrade configuration unknown command in privileged EXEC mode.

**Syntax:**

```text
show autoupgrade configuration unknown
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(15)T | This command was introduced. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

Use the show autoupgrade configuration unknown command to view any invalid start-up configuration. This command prints invalid start-up configuration data only when run from an image which was upgraded using the Cisco IOS Auto-Upgrade Manager (AUM). This command output is useful when you are upgrading to an image with a different feature set.

**Example:**

The following example shows how to view the invalid start-up configuration lines that the Cisco software image, upgraded on the device using AUM, does not understand:

```text
Device# show autoupgrade configuration unknown
! Config Lines not understood by the current image:
voice-card 0
no dspfarm
crypto pki trustpoint aum_cisco_ca
enrollment terminal
revocation-check none
crypto pki certificate chain aum_cisco_ca
certificate ca 40DCB71E54EE24CBE5326F8006BBA4F6 nvram:SecureServer#A4F6CA.cer
no ip http secure-server
transport output lat pad telnet rlogin lapb-ta mop udptn v120 ssh
Total 9 Invalid Config Lines
Device#
```


### `show bcm560x`

> **Página:** 566 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the BCM560x hardware table information, use the show bcm560X command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show bcm560x name {offset | all} [raw]
```

**Parameters (Syntax Description):**

- `name` — D is p l a y s the bcm50 x hardware t a b l e name. The hardware t a b l e name can be VLAN t a b l e name (VTABLE)or Port b as e d VLAN t a b l e name( P T A B L E):
- `offset` — Hardware t a b l e number. Range is from0 to65535
- `all` — D is p l a y s all the bcm560 x hardware t a b l e names.
- `raw` — ( Optional) D is p l a y s the bcm560 x hardware t a b l e names.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(15)T | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release12.4(15) T. |

**Example:**

The following is sample output from the show bcm560X allcommand:

```text
Router# show bcm560x VTABLE all
Router# VTABLE.0[0x1]: <VLAN_TAG=1,PORT_BITMAP=0xA000008,UT_PORT_BITMAP=8,MOD_BMAP=0>
*Mar 11 08:07:29.863: VTABLE.0[0x2]:
<VLAN_TAG=2,PORT_BITMAP=0xA000000,UT_PORT_BITMAP=0,MOD_BMAP=0>
*Mar 11 08:07:29.863: VTABLE.0[0x3]:
<VLAN_TAG=0x401,PORT_BITMAP=0xA000000,UT_PORT_BITMAP=0,MOD_BMAP=0>
*Mar 11 08:07:29.867: VTABLE.0[0x4]:
<VLAN_TAG=0xFFF,PORT_BITMAP=0x8000000,UT_PORT_BITMAP=0x8000000,MOD_BMAP=0>
*Mar 11 08:07:29.867:
```


### `show bootflash:`

> **Página:** 567 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display information about the bootflash: file system, use the show bootflash: command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show bootflash: [all | chips | filesys]
```

**Parameters (Syntax Description):**

- `all` — ( Optional) D is p l a y s all p o s s i b l e Flash information.
- `chips` — ( Optional) D is p l a y s information about the Flash c h ip.
- `filesys` — ( Optional) D is p l a y s information about the filesystem.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to display information about the file system status:

```text
Router>
show bootflash: filesys
-------- F I L E S Y S T E M S T A T U S --------
Device Number = 0
DEVICE INFO BLOCK: bootflash
Magic Number = 6887635 File System Vers = 10000 (1.0)
Length = 1000000 Sector Size = 40000
Programming Algorithm = 39 Erased State = FFFFFFFF
File System Offset = 40000 Length = F40000
MONLIB Offset = 100 Length = C628
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
Bytes Used = 917CE8 Bytes Available = 628318
Bad Sectors = 0 Spared Sectors = 0
OK Files = 2 Bytes = 917BE8
Deleted Files = 0 Bytes = 0
Files w/Errors = 0 Bytes = 0
Router>
```

This example shows how to display image information:

```text
Router>
show bootflash:
-#- ED --type-- --crc--- -seek-- nlen -length- -----date/time------ name
1 .. image 8C5A393A 237E3C 14 2063804 Aug 23 1999 16:18:45 c6msfc-boot-mz
2 .. image D86EE0AD 957CE8 9 7470636 Sep 20 1999 13:48:49 rp.halley
Router>
```

This example shows how to display all bootflash information:

```text
Router>
show bootflash: all
-#- ED --type-- --crc--- -seek-- nlen -length- -----date/time------ name
1 .. image 8C5A393A 237E3C 14 2063804 Aug 23 1999 16:18:45 c6msfc-boot-
mz
2 .. image D86EE0AD 957CE8 9 7470636 Sep 20 1999 13:48:49 rp.halley
6456088 bytes available (9534696 bytes used)
-------- F I L E S Y S T E M S T A T U S --------
Device Number = 0
DEVICE INFO BLOCK: bootflash
Magic Number = 6887635 File System Vers = 10000 (1.0)
Length = 1000000 Sector Size = 40000
Programming Algorithm = 39 Erased State = FFFFFFFF
File System Offset = 40000 Length = F40000
MONLIB Offset = 100 Length = C628
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
Bytes Used = 917CE8 Bytes Available = 628318
Bad Sectors = 0 Spared Sectors = 0
OK Files = 2 Bytes = 917BE8
Deleted Files = 0 Bytes = 0
Files w/Errors = 0 Bytes = 0
Router>
```


### `show bootvar`

> **Página:** 569 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the contents of the BOOT variable, the name of the configuration file pointed to by the CONFIG_FILE variable, the contents of the BOOTLDR variable, and the configuration register setting, use the show bootvar command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show bootvar
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | This command was introduced. |
| 12.2(14)SX | Support for this command was i m p l e m e n t e do n the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was integrated into Release 12.2(17d)SXB. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Supported Platforms Other than the Cisco 7600 Series Router The show bootvar command replaces the show bootcommand. The show bootvar command allows you to view the current settings for the following variables: • BOOT • CONFIG_FILE • BOOTLDR The BOOT variable specifies a list of bootable images on various devices. The CONFIG_FILE variable specifies the configuration file used during system initialization. The BOOTLDR variable specifies the flash device and filename containing the rxboot image that ROM uses for booting. You set these variables with the boot system, boot config, and boot bootldr global configuration commands, respectively. When you use this command on a device with multiple Route Switch Processor (RSP) cards (Dual RSPs), this command also shows you the variable settings for both the primary and secondary RSP card. Cisco 7600 Series Router The show bootvar command displays information about the BOOT environmental variable. The command output depends on how you configure the boot statement as follows: • If you enter the boot system flash bootflash: sup720_image command in the boot configuration, then the show bootvar command output displays the bootflash information. • If you enter the boot system flash sup-bootflash: sup720_image command in the boot configuration, then the show bootvar command output displays the sup-bootflash information. This action is the correct way of configuring the boot statement. The show bootvar command is available from the switch processor command-line interface (CLI) and the route processor CLI. From the switch processor CLI, the display is always bootflash. With either the bootflash or the sup-bootflash boot statement, the switch boots correctly. You should use sup-bootflash in the boot configuration statement because the image is stored in the switch processor bootflash; the route processor sees the image as sup-bootflash. The number displayed after the image name (for example, c6sup12-js-mz.121-13.E,12) indicates the number of times that the Cisco 7600 series router tries to reboot the file before giving up.

**Example:**

Supported Platforms Other than the Cisco 7600 Series Router The following is sample output from the show bootvar command:

```text
show bootvar
BOOT variable =
CONFIG_FILE variable = nvram:
Current CONFIG_FILE variable = slot0:router-config
BOOTLDR variable not exist
Configuration register is 0x0
```

In this example, the BOOT variable contains a null string; that is no bootable images are specified. The CONFIG_FILE variable points to the configuration file in NVRAM as the startup (initialization) configuration. The run-time value for the CONFIG_FILE variable points to the router-configuration file on the flash memory card inserted in the first slot of the RSP card. That is, during the run-time configuration, you have modified the CONFIG_FILE variable using the boot config command, but you have not saved the run-time configuration to the startup configuration. To save your run-time configuration to the startup configuration, use the copy system:running-config nvram:startup-config command. If you do not save the run-time configuration to the startup configuration, then the system reverts to the saved CONFIG_FILE variable setting for initialization information upon reload. In this sample, the system reverts to NVRAM for the startup configuration file. The BOOTLDR variable does not yet exist. That is, you have not created the BOOTLDR variable using the boot bootldr global configuration command. The following example is output from the show bootvar command for a Cisco 7513 router configured for high system availability (HSA):

```text
Router# show bootvar
BOOT variable =
CONFIG_FILE variable =
Current CONFIG_FILE variable =
BOOTLDR variable does not exist
Configuration register is 0x0
current is in slot 7
BOOT variable =
CONFIG_FILE variable =
BOOTLDR variable does not exist
Configuration register is 0x0
```

The table below describes the significant fields shown in the displays.

| Field | Description |
| --- | --- |
| BOOTvariable | Displaysalistofspecifiedbootableimages. |
| CONFIG_FILEvariable | Indicateswheretolocatethestartup(initialization)configurationfile. |
| CurrentCONFIG_FILEvariable | Identifiestherun-timeconfigurationfile. |
| BOOTLDRvariable | IdentifiesthelocationofthebootimagethatROMusesforbooting,ifit isspecified. |
| Configurationregister | Specifiesrouterbehavior,suchashowtherouterboots,optionswhile booting,andconsolespeed(baudrateforaterminalemulationsession). |
| currentisinslot7 | IndicatestheslotwheretheredundantsystemislocatedinHSA configurations. |

Cisco 7600 Series Router This example shows how to display information about the BOOT environment variable:

```text
show bootvar
BOOT variable = sup-bootflash:c6sup12-js-mz.121-13.E,12
CONFIG_FILE variable =
BOOTLDR variable = bootflash:c6msfc2-boot-mz.121-13.E.bin
Configuration register is 0x2102
Standby is up
Standby has 112640K/18432K bytes of memory.
Standby BOOT variable = bootflash:c6sup12-js-mz.121-13.E,12
Standby CONFIG_FILE variable =
Standby BOOTLDR variable = bootflash:c6msfc2-boot-mz.121-13.E.bin
Standby Configuration register is 0x2102
```

The number displayed after the image name (for example, c6sup12-js-mz.121-13.E,12) indicates the number of times that the Cisco 7600 series router tries to reboot the file before giving up.


### `show buffers`

> **Página:** 572 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** If no options are specified, all buffer pool information is displayed. · **Leitura (show/clear/…):** sim

**Description:** To display detailed information about the buffer pools on the network server when Cisco IOS, Cisco IOS Software Modularity, or Cisco IOS XE images are running, use the show buffers command in user EXEC or privileged EXEC mode. Cisco Catalyst 4500e Series Switches running IOS XE software

**Syntax:**

```text
show buffers [ {address hex-address | failures | pool pool-name | detailed | processes | {all | assigned
[process-id] | free | old | input-interface interface-type interface-number} | [pool pool-name]} [dump |
header | packet | location pool-location]]
show buffers [detailed process id {address hex-address | all | assigned | failures | free | input-interface
interface-type interface-number | old | pool pool-name} [dump | header | packet | location pool-location]]
```

**Parameters (Syntax Description):**

- `address` — ( Optional) D is p l a y s buffers at as p e c if i e d address.
- `hex-address` — ( Optional) Address in hexadecimal not at i on.
- `failures` — ( Optional) D is p l a y s buffer alloc at i on failures.
- `pool` — ( Optional) D is p l a y s buffers in as p e c if i e d buffer pool.
- `pool-name` — ( Optional) Name of buffer pool.
- `detailed process` — ( Optional) D is p l a y s detailed buffer information.
- `processes` — ( Optional) For Cisco IOS Software M o d u l a r it y image s only. D is p l a y s buffers c on n e c t e d to Packet Manager.
- `all` — ( Optional) D is p l a y s all buffers.
- `as s i g n e d` — ( Optional) D is p l a y s the buffers in use.
- `process-id` — ( Optional) For Cisco IOS Software M o d u l a r it y image s only. P O S I X process id e n t if i e r.
- `free` — ( Optional) D is p l a y s the buffers a v a i l a b l e for use.
- `old` — ( Optional) D is p l a y s buffers o l d e r than one min u t e.
- `input-interface` — ( Optional) D is p l a y s interface pool information. If an interface type is specified and this interface has its own buffer pool, information for that pool is d is p l a y e d.
- `interface-type` — ( Optional) Interface type.
- `interface-number` — ( Optional) Interface number.
- `dump` — ( Optional) D is p l a y s the buffer h e a d e r and all data.
- `header` — ( Optional) D is p l a y s the buffer h e a d e r only.
- `packet` — ( Optional) D is p l a y s the buffer h e a d e r and p a c k e t data.
- `location pool-location` — ( Optional) D is p l a y s all the buffer pool s in a g i v e n location. The global buffer pool s c o m e first, f o l low e d u p with process-level buffer pool s.

**Command Default:** If no options are specified, all buffer pool information is displayed.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.3 | The option to f i l t e r d is p l a you t p u t b as e do n s p e c if i c buffer pool s was expand e d. |
| 12.2(18)SXF4 | Two a d d it i on a l f i e l d s were added to the output to support Cisco IOS Software M o d u l a r it y. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease3.1.0.SG | This command was introduced on the Cisco Catalyst4500 e Serfies Switch e s with support for the detailed process command option. Cisco IOS Software The following is sample output from the show buffers command with no arguments, showing all buffer pool information: Router# show buffers Buffer elements: |
| 398 | in free list (500 max allowed) |
| 1266 | hits, 0 misses, 0 created Public buffer pools: Small buffers, 104 bytes (total 50, permanent 50): |
| 50 | in free list (20 min, 150 max allowed) |
| 551 | hits, 0 misses, 0 trims, 0 created Middle buffers, 600 bytes (total 25, permanent 25): |
| 25 | in free list (10 min, 150 max allowed) |
| 39 | hits, 0 misses, 0 trims, 0 created Big buffers, 1524 bytes (total 50, permanent 50): |
| 49 | in free list (5 min, 150 max allowed) |
| 27 | hits, 0 misses, 0 trims, 0 created VeryBig buffers, 4520 bytes (total 10, permanent 10): |
| 10 | in free list (0 min, 100 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created Large buffers, 5024 bytes (total 0, permanent 0): |
| 0 | in free list (0 min, 10 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created Huge buffers, 18024 bytes (total 0, permanent 0): |
| 0 | in free list (0 min, 4 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created Interface buffer pools: Ethernet0 buffers, 1524 bytes (total 64, permanent 64): |
| 16 | in free list (0 min, 64 max allowed) |
| 48 | hits, 0 fallbacks |
| 16 | max cache size, 16 in cache Ethernet1 buffers, 1524 bytes (total 64, permanent 64): |
| 16 | in free list (0 min, 64 max allowed) |
| 48 | hits, 0 fallbacks |
| 16 | max cache size, 16 in cache Serial0 buffers, 1524 bytes (total 64, permanent 64): |
| 16 | in free list (0 min, 64 max allowed) |
| 48 | hits, 0 fallbacks |
| 16 | max cache size, 16 in cache Serial1 buffers, 1524 bytes (total 64, permanent 64): |
| 16 | in free list (0 min, 64 max allowed) |
| 48 | hits, 0 fallbacks |
| 16 | max cache size, 16 in cache TokenRing0 buffers, 4516 bytes (total 48, permanent 48): |
| 0 | in free list (0 min, 48 max allowed) |
| 48 | hits, 0 fallbacks |
| 16 | max cache size, 16 in cache TokenRing1 buffers, 4516 bytes (total 32, permanent 32): |
| 32 | in free list (0 min, 48 max allowed) |
| 16 | hits, 0 fallbacks |
| 0 | failures (0 no memory) The following is sample output from the show buffers command with no arguments, showing only buffer pool information for Huge buffers. This output shows a highest total of five Huge buffers created five days and 18 hours before the command was issued. Router# show buffers Huge buffers, 18024 bytes (total 5, permanent 0, peak 5 @ 5d18h): |
| 4 | in free list (3 min, 104 max allowed) |
| 0 | hits, 1 misses, 101 trims, 106 created |
| 0 | failures (0 no memory) The following is sample output from the show buffers command with no arguments, showing only buffer pool information for Huge buffers. This output shows a highest total of 184 Huge buffers created one hour, one minute, and 15 seconds before the command was issued. Router# show buffers Huge buffers, 65280 bytes (total 4, permanent 2, peak 184 @ 01:01:15): |
| 4 | in free list (0 min, 4 max allowed) |
| 32521 | hits, 143636 misses, 14668 trims, 14670 created |
| 143554 | failures (0 no memory) The following is sample output from the show buffers command with an interface type and interface number: Router# show buffers Ethernet 0 Ethernet0 buffers, 1524 bytes (total 64, permanent 64): |
| 16 | in free list (0 min, 64 max allowed) |
| 48 | hits, 0 fallbacks |
| 16 | max cache size, 16 in cache The table below describes the significant fields shown in the display. |
| Field | Description |
| Bufferelements | Small s t r u c t u r e s used as p l a c e hold e r s for buffers in in t e r n a l o p e r at in g system queue s. Used when a buffer may n e e d to be on more than one queue. |
| freelist | To t a l number of the current l y u n allocate d buffer e l e m e n t s. |
| maxallowed | Maximum number of buffers that are a v a i l a b l e for alloc at i on. |
| hits | Count of s u c c e s s f u l at t e m p t s to allocate a buffer when n e e d e d. |
| misses | Count of buffer alloc at i on at t e m p t s that r e s u l t e d in g r o w in gt h e buffer pool to allocate abuffer. |
| created | Count of n e w buffers c r e at e d to s at is f y buffer alloc at i on at t e m p t s when the a v a i l a b l e buffers in the pool have a l r e a d y been allocate d. |
| PublicBufferPools | Buffers that are104 by t e s l on g. |
| Smallbuffers |  |
| Middlebuffers | Buffers that are600 by t e s l on g. |
| Bigbuffers | Buffers that are1524 by t e s l on g. |
| VeryBigbuffers | Buffers that are4520 by t e s l on g. |
| Largebuffers | Buffers that are5024 by t e s l on g. |
| Hugebuffers | Buffers that are18,024 by t e s l on g. |
| total | To t a l number of this type of buffer. |
| permanent | Number of these buffers that are p e r m an e n t. |
| peak | Maximum number of buffers c r e at e d( h i g h e s t to t a l) and the time when that p e a k o c c u r r e d. Format s include we e k s, days, h our s, min u t e s, and s e c on d s. Not all systems r e port ap e a k value, which m e an s this f i e l d may not d is p l a y in output. |
| freelist | Number of a v a i l a b l e or u n allocate d buffers in that pool. |
| min | Min i m u m number of free or u n allocate d buffers in the buffer pool. |
| maxallowed | Maximum number of free or u n allocate d buffers in the buffer pool. |
| hits | Count of s u c c e s s f u l at t e m p t s to allocate a buffer when n e e d e d. |
| Field | Description |
| misses | Count of buffer alloc at i on at t e m p t s that r e s u l t e d in g r o w in gt h e buffer pool in or d e r to allocate a buffer. |
| trims | Count of buffers release d to the system be cause they were not being used. This f i e l d is d is p l a y e do n l y for d y n a m i c buffer pool s, not interface buffer pool s, which are static. |
| created | Count of n e w buffers c r e at e d in response to m is s e s. This f i e l d is d is p l a y e do n l y for d y n a m i c buffer pool s, not interface buffer pool s, which are s t at i c. |
| InterfaceBufferPools | To t a l number of this type of buffer. |
| total |  |
| permanent | Number of these buffers that are p e r m an e n t. |
| freelist | Number of a v a i l a b l e or u n allocate d buffers in that pool. |
| min | Min i m u m number of free or u n allocate d buffers in the buffer pool. |
| maxallowed | Maximum number of free or u n allocate d buffers in the buffer pool. |
| hits | Count of s u c c e s s f u l at t e m p t s to allocate a buffer when n e e d e d. |
| fallbacks | Count of buffer alloc at i on at t e m p t s that r e s u l t e d in f all in g b a c k to the p u b l i c buffer pool that is the small e s t pool at l e as t as b i g as the interface buffer pool. |
| maxcachesize | Maximum number of buffers from the pool of that interface that can be in the buffer pool cache of that interface. Each interface buffer pool has its own cache. These are not a d d it i on a l to the p e r m an e n t buffers; they c o m e from the buffer pool s of the interface. Some interfaces p l a c e all of their buffers from the interface pool into the cache. In this c as e, it is nor m a l for the free list to d is p l a y0. |
| failures | To t a l number of time s a buffer c r e at i on f a i l e d. The f a i l u r e may have o c c u r r e d be cause of an u m be r of d if f e r e n t r e as on s, such as low processor memory, low IOMEM,or no buffers in the pool when c all e d from interrupt context. |
| nomemory | Number of time s the r e has been low memory d u r in g buffer c r e at i on. Loworno memory d u r in g buffer c r e at i on may not n e c e s s a r i l y m e an that buffer c r e at i on f a i l e d; memory can be o b t a in e d from an a l t e r n at e resource such as a f all b a c k pool. Cisco IOS Software Modularity The following is sample output from the show buffers command using a Cisco IOS Modularity image from Cisco IOS Release 12.2(18)SXF4 and later releases. Two new output fields were introduced--Public buffer heads and Temporary buffer heads--and are shown within comments in the following sample output. Router# show buffers Buffer elements: |
| 500 | in free list (500 max allowed) |
| 106586 | hits, 0 misses, 0 created Public buffer pools: Small buffers, 104 bytes (total 50, permanent 50, peak 54 @ 1d13h): |
| 49 | in free list (20 min, 150 max allowed) |
| 54486 | hits, 0 misses, 4 trims, 4 created |
| 0 | failures (0 no memory) Middle buffers, 600 bytes (total 25, permanent 25, peak 27 @ 1d13h): |
| 25 | in free list (10 min, 150 max allowed) |
| 20 | hits, 0 misses, 2 trims, 2 created |
| 0 | failures (0 no memory) Big buffers, 1536 bytes (total 50, permanent 50): |
| 50 | in free list (40 min, 150 max allowed) |
| 6 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) VeryBig buffers, 4520 bytes (total 10, permanent 10): |
| 10 | in free list (0 min, 100 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) Large buffers, 5024 bytes (total 0, permanent 0): |
| 0 | in free list (0 min, 10 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) Huge buffers, 18024 bytes (total 1, permanent 0, peak 1 @ 1d13h): |
| 0 | in free list (0 min, 4 max allowed) |
| 1 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) ! Start of Cisco IOS Software Modularity fields Public buffer headers: Header buffers, 880 bytes (total 1000, peak 142 @ 1d13h): |
| 864 | in permanent free list |
| 142 | hits, 0 misses Temporary buffer headers: Header buffers, 896 bytes (total 0): |
| 0 | in free list |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures ! End of Cisco IOS Software Modularity fields Interface buffer pools: Logger Pool buffers, 600 bytes (total 150, permanent 150): |
| 150 | in free list (150 min, 150 max allowed) |
| 22 | hits, 0 misses The table below describes the significant fields shown in the display that are different from the fields in the first table. |
| Field | Description |
| PublicBufferHeaders | Buffers that are880 by t e s l on g. |
| Headerbuffers |  |
| total | To t a l number of this type of buffer. |
| permanentfreelist | Number of a v a i l a b l e or u n allocate d p e r m an e n the a d e r buffers. |
| hits | Count of s u c c e s s f u l at t e m p t s to allocate a h e a d e r buffer when n e e d e d. |
| misses | Count of buffer alloc at i on at t e m p t s that r e s u l t e d in g r o w in gt h e buffer pool in or d e r to allocate a buffer. |
| Field | Description |
| TemporaryBufferHeaders | Buffers that are896 by t e s l on g. |
| Headerbuffers |  |
| total | To t a l number of this type of buffer. |
| freelist | Number of a v a i l a b l e or u n allocate d h e a d e r buffers in that pool. |
| hits | Count of s u c c e s s f u l at t e m p t s to allocate a buffer when n e e d e d. |
| misses | Count of buffer alloc at i on at t e m p t s that r e s u l t e d in g r o w in gt h e buffer pool in or d e r to allocate a buffer. |
| trims | Count of buffers release d to the system be cause they were not being used. This f i e l d is d is p l a y e do n l y for d y n a m i c buffer pool s, not interface buffer pool s, which are s t at i c. |
| created | Count of n e w buffers c r e at e d in response to m is s e s. This f i e l d is d is p l a y e do n l y for d y n a m i c buffer pool s, not interface buffer pool s, which are s t at i c. |
| failures | To t a l number of alloc at i on request s that have f a i l e d be cause no buffer was a v a i l a b l e for alloc at i on; the data g r a m was l o s t. Such failures nor m all y o c c u r at interrupt level. Cisco Catalyst 4500e Series Switches running IOS XE software The following is sample output from the show buffers command on a Cisco Catalyst 4500e switch, using a Cisco IOS image from Cisco IOS XE Release 3.1.0.SG and later releases. PDS Public buffers and Packet information was added--and are shown within comments in the following sample output. Switch#show buffers PDS public buffers Public buffer pools: Packet buffer, 2048 bytes (total 1000, permanent 1000): |
| 1000 | in free list (1000 max allowed) Header pools: Packet Header Memory, 0 bytes (total 0, permanent 0): |
| 0 | in free list (0 max allowed) Buffer Header Memory, 0 bytes (total 0, permanent 0): |
| 0 | in free list (0 max allowed) IOSd private buffers: Buffer elements: |
| 354 | in free list (500 max allowed) |
| 27134 | hits, 0 misses, 500 created Public buffer pools: Small buffers, 104 bytes (total 134, permanent 50, peak 134 @ 01:04:39): |
| 134 | in free list (20 min, 150 max allowed) |
| 2554 | hits, 28 misses, 0 trims, 84 created |
| 0 | failures (0 no memory) Middle buffers, 600 bytes (total 52, permanent 25, peak 52 @ 01:04:39): |
| 52 | in free list (10 min, 150 max allowed) |
| 61 | hits, 9 misses, 0 trims, 27 created |
| 0 | failures (0 no memory) Big buffers, 1536 bytes (total 50, permanent 50): |
| 50 | in free list (5 min, 150 max allowed) |
| 157 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) VeryBig buffers, 4520 bytes (total 10, permanent 10): |
| 10 | in free list (0 min, 100 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) Large buffers, 5024 bytes (total 0, permanent 0): |
| 0 | in free list (0 min, 10 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) Huge buffers, 18024 bytes (total 0, permanent 0): |
| 0 | in free list (0 min, 4 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) Interface buffer pools: CF Small buffers, 104 bytes (total 100, permanent 100): |
| 100 | in free list (100 min, 200 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) BIPC small buffers, 128 bytes (total 250, permanent 250): |
| 250 | in free list (250 min, 250 max allowed) |
| 92 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) BIPC middle buffers, 600 bytes (total 300, permanent 300): |
| 300 | in free list (300 min, 300 max allowed) |
| 36 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) CF Middle buffers, 600 bytes (total 100, permanent 100): |
| 100 | in free list (100 min, 200 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) Syslog ED Pool buffers, 600 bytes (total 132, permanent 132): |
| 131 | in free list (132 min, 132 max allowed) |
| 5 | hits, 0 misses CF Big buffers, 1536 bytes (total 25, permanent 25): |
| 25 | in free list (25 min, 50 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) BIPC buffers, 4096 bytes (total 2, permanent 2): |
| 2 | in free list (1 min, 8 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) IPC Emergency buffers, 4096 bytes (total 301, permanent 300, peak 302 @ 01:05:07): |
| 301 | in free list (300 min, 300 max allowed) |
| 39 | hits, 1 fallbacks, 66 trims, 67 created |
| 0 | failures (0 no memory) |
| 0 | max cache size, 0 in cache |
| 0 | hits in cache, 0 misses in cache CF VeryBig buffers, 4520 bytes (total 2, permanent 2): |
| 2 | in free list (2 min, 4 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) CF Large buffers, 5024 bytes (total 1, permanent 1): |
| 1 | in free list (1 min, 2 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) BIPC Medium buffers, 16384 bytes (total 5, permanent 5): |
| 5 | in free list (5 min, 5 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) BIPC Large buffers, 65535 bytes (total 2, permanent 2): |
| 2 | in free list (2 min, 2 max allowed) |
| 0 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) IPC small buffers, 128 bytes (total 250, permanent 250): |
| 228 | in free list (250 min, 250 max allowed) |
| 124 | hits, 0 fallbacks |
| 0 | max cache size, 0 in cache |
| 0 | hits in cache, 0 misses in cache IPC middle buffers, 600 bytes (total 200, permanent 200): |
| 200 | in free list (200 min, 200 max allowed) |
| 293 | hits, 0 fallbacks |
| 0 | max cache size, 0 in cache |
| 0 | hits in cache, 0 misses in cache IPC buffers, 4096 bytes (total 300, permanent 300): |
| 298 | in free list (300 min, 300 max allowed) |
| 72 | hits, 0 fallbacks |
| 0 | max cache size, 0 in cache |
| 0 | hits in cache, 0 misses in cache IPC Medium buffers, 16384 bytes (total 30, permanent 30): |
| 30 | in free list (30 min, 30 max allowed) |
| 100 | hits, 0 fallbacks |
| 0 | max cache size, 0 in cache |
| 0 | hits in cache, 0 misses in cache IPC Large buffers, 65535 bytes (total 13, permanent 13): |
| 11 | in free list (13 min, 13 max allowed) |
| 19 | hits, 0 misses |
| 0 | max cache size, 0 in cache |
| 0 | hits in cache, 0 misses in cache Header pools: Catalyst 4000 buffers, 0 bytes (total 14600, permanent 14600): |
| 14600 | in free list (0 min, 14601 max allowed) |
| 14600 | hits, 0 misses, 0 trims, 0 created |
| 0 | failures (0 no memory) Switch# The following is sample shows how to run the show buffers detailed command on a Cisco Catalyst 4500e switch, using a Cisco IOS image from Cisco IOS XE Release 3.1.0.SG and later releases and the various keywords and arguments (Explained in the Syntax Description Table) available. Switch# Switch#show buffers ? detailed Show detailed buffer statistics \| Output modifiers <cr> Switch#show buffers detailed ? process Show detailed process buffer info Switch#show buffers detailed process ? iosd IOSd Process Switch#show buffers detailed process iosd ? address Buffer at a given address all All buffers assigned Buffers in use failures Buffer allocation failures free Buffers available for use input-interface Buffers assigned to an input interface old Buffers older than one minute pool Buffers in a specified pool \| Output modifiers <cr> |

**Usage Guidelines:**

Note When you use the show buffers input-interface [packet | dump] command, some of the data packets are not displayed correctly because of the way packets are assembled for display on the CLI. Pointers to the memory location of the header and data for the packet are stored in local memory. By the time the pointers are de-referenced, it is possible that the memory storing the header or packet data is overwritten. For example, in the show buffers input-interface packet command output, the source and destination addresses might not match the actual source and destination address if the packet data were decoded by some secondary means such as analyzing manually or by other means. It is recommended that the users of this command must validate packets by a secondary means.


### `show c2600`

> **Página:** 581 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information for troubleshooting the Cisco 2600 series router, use the show c2600 command in EXEC mode.

**Syntax:**

```text
show c2600
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3XA | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The show c2600 command provides complex troubleshooting information that pertains to the platform’s shared references rather than to a specific interface.

**Example:**

The following is sample output from the show c2600 command:

```text
Router# show c2600
C2600 Platform Information:
Interrupts:
Assigned Handlers...
Vect Handler # of Ints Name
00 801F224C 00000000 Xilinx bridge error interrupt
01 801DE768 0D3EE155 MPC860 TIMER INTERRUPT
02 801E94E0 0000119E 16552 Con/Aux Interrupt
04 801F0D94 00000000 PA Network Management Int Handler
05 801E6C34 00000000 Timebase Reference Interrupt
06 801F0DE4 00002C1A PA Network IO Int Handler
07 801F0EA0 0000015D MPC860 CPM INTERRUPT
14 801F224C 00000000 Xilinx bridge error interrupt
IOS Priority Masks...
Level 00 = [ EF020000 ]
Level 01 = [ EC020000 ]
Level 02 = [ E8020000 ]
Level 03 = [ E0020000 ]
Level 04 = [ E0020000 ]
Level 05 = [ E0020000 ]
Level 06 = [ C0020000 ]
Level 07 = [ 00000000 ]
SIU_IRQ_MASK = FFFFFFFF SIEN = EF02xxxx Current Level = 00
Spurious IRQs = 00000000 SIPEND = 0000xxxx
Interrupt Throttling:
Throttle Count = 00000000 Timer Count = 00000000
Netint usec = 00000000 Netint Mask usec = 000003E8
Active = 0 Configured = 0
Longest IRQ = 00000000
IDMA Status:
Requests = 00000349 Drops = 00000000
Complete = 00000349 Post Coalesce Frames = 00000349
Giant = 00000000
Available Blocks = 256/256
ISP Status:
Version string burned in chip: "A986122997"
New version after next program operation: "B018020998"
ISP family type: "2096"
ISP chip ID: 0x0013
Device is programmable
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Interrupts | Denotesthatthenextsectiondescribesthestatusoftheinterruptservices. |
| AssignedHandlers | DenotesasubsectionoftheInterruptsectionthatdisplaysdataaboutthe interrupthandlers. |
| Vect | Theprocessorvectornumber. |
| Handler | Theexecutionaddressofthehandlerassignedtothisvector. |
| #ofInts | Thenumberoftimesthishandlerhasbeencalled. |
| Name | Thenameofthehandlerassignedtothisvector. |
| IOSPriorityMasks | DenotesthesubsectionoftheInterruptsectionthatdisplaysinternalCisco IOSpriorities.EachiteminthissubsectionindicatesaCiscoIOSinterrupt levelandthebitmaskusedtomaskoutinterruptsourceswhenthatCisco IOSlevelisbeingprocessed.Usedexclusivelyfordebugging. |
| SIU_IRQ_MASK | Forengineeringleveldebugonly. |
| SpuriousIRQs | Forengineeringleveldebugonly. |
| InterruptThrottling: | ThissubsectiondescribesthebehavioroftheInterruptThrottling mechanismontheplatform. |
| ThrottleCount | Numberoftimesthrottlehasbecomeactive. |
| TimerCount | Numberoftimesthrottlehasdeactivatedbecausethemaximummasked outtimefornetworkinterruptlevelhasbeenreached. |
| Netintusec | Maximumtimenetworklevelisallowedtorun(inmicroseconds). |
| NetintMaskusec | Maximumtimenetworklevelinterruptismaskedouttoallowprocess levelcodetorun(inmicroseconds). |
| Active | Indicatesthatthenetworklevelinterruptismaskedorthattherouterisin interruptthrottlestate. |
| Configured | Indicatesthatthrottlingisenabledorconfiguredwhensetto1. |

| Field | Description |
| --- | --- |
| LongestIRQ | Durationoflongestnetworklevelinterrupt(inmicroseconds). |
| IDMAStatus | MonitorstheactivityoftheInternalDirectMemoryAccess(IDMA) hardwareandsoftware.Usedtocoalescepackets(turnparticularized packetsintononparticularizedpackets)fortransfertotheprocesslevel switchingmechanism. |
| Requests | NumberoftimestheIDMAengineisaskedtocoalesceapacket. |
| Drops | Numberoftimesthecoalescingoperationwasterminate. |
| Complete | Numberoftimestheoperationwassuccessful. |
| PostCoalesceFrames | NumberofFramescompletedpostcoalesceprocessing. |
| Giant | Numberofpacketstoolargetocoalesce. |
| AvailableBlocks | Indicatesthestatusoftherequestqueue,intheformatN/MwhereNisthe numberofemptyslotsinqueueandMisthetotalnumberofslots;for example,2/256indicatesthatthequeuehas256entriesandcanaccepttwo morerequestsbeforeitisfull. |
| ISPStatus | ProvidesstatusofIn-System-Programmable(ISP)hardware. |
| Versionstringburnedinchip | CurrentversionofISPhardware. |
| Newversionafternextprogram operation | VersionofISPhardwareafternextISPprogrammingoperation. |
| ISPfamilytype | DevicefamilynumberofISPhardware. |
| ISPchipID | InternalIDofISPhardwareasdesignatedbythechipmanufacturer. |
| Deviceisprogrammable | “Yes”or“No.”IndicatesifanISPoperationispossibleonthisboard. |


### `show c7200`

> **Página:** 583 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the CPU and midplane for Cisco 7200 series routers, use the show c7200 command in EXEC mode.

**Syntax:**

```text
show c7200
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

You can use the output of this command to determine whether the hardware version level and upgrade is current. The information is generally useful for diagnostic tasks performed by technical support only.

**Example:**

The following is sample output from the show c7200 command:

```text
Router# show c7200
C7200 Network IO Interrupt Throttling:
throttle count=0, timer count=0
active=0, configured=0
netint usec=3999, netint mask usec=200
C7200 Midplane EEPROM:
Hardware revision 1.2 Board revision A0
Serial number 2863311530 Part number 170-43690-170
Test history 0xAA RMA number 170-170-170
MAC=0060.3e28.ee00, MAC Size=1024
EEPROM format version 1, Model=0x6
EEPROM contents (hex):
0x20: 01 06 01 02 AA AA AA AA AA AA AA AA 00 60 3E 28
0x30: EE 00 04 00 AA AA AA AA AA AA AA 50 AA AA AA AA
C7200 CPU EEPROM:
Hardware revision 2.0 Board revision A0
Serial number 3509953 Part number 73-1536-02
Test history 0x0 RMA number 00-00-00
EEPROM format version 1
EEPROM contents (hex):
0x20: 01 15 02 00 00 35 8E C1 49 06 00 02 00 00 00 00
0x30: 50 00 00 00 FF FF FF FF FF FF FF FF FF FF FF FF
```


### `show catalyst6000`

> **Página:** 584 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** The default is all · **Leitura (show/clear/…):** sim

**Description:** To display the information about the chassis, use the show catalyst6000 command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show catalyst6000 {all | chassis-mac-address | switching-clock | traffic-meter}
```

**Parameters (Syntax Description):**

- `all` — D is p l a y s the MAC-address range s and the current and p e a k traffic-meter r e a d in g.
- `chassis-mac-address` — D is p l a y s the MAC-address range.
- `switching-clock` — D is p l a y s the f a i l u r e recovery mode of the switch in g clock.
- `traffic-meter` — D is p l a y s the percentage of the b a c k plane( s h are d bus) u t i l i z at i on.

**Command Default:** The default is all

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SXI | The output of the show catalyst6000 traffic-meter command was changed to include traffic monitor status information. |

**Usage Guidelines:**

If you enter the switching-clock keywords, the output displays whether switching of the redundant clock sources on the backplane is allowed if the active clock source fails. There are either 64 or 1024 MAC addresses that are available to support the software features. You can enter the show catalyst6000 chassis-mac-address command to display the MAC-address range on your chassis. In Cisco IOS Release 12.2(33)SXI and later releases, the traffic monitor status information is displayed in the output. In earlier releases, only the current and peak traffic-meter readings are displayed.

**Example:**

This example shows how to display the MAC-address ranges and the current and peak traffic-meter readings:

```text
Router>
show catalyst6000 all
chassis MAC addresses: 64 addresses from 0001.6441.60c0 to 0001.6441.60ff
traffic meter = 0% Never cleared
peak = 0% reached at 08:14:38 UTC Wed Mar 19 2003
switching-clock: clock switchover and system reset is allowed
Router>
```

This example shows how to display the MAC-address ranges:

```text
show catalyst6000 chassis-mac-address
chassis MAC addresses: 1024 addresses from 00d0.004c.1800 to 00d0.004c.1c00
```

The following example shows how to display the current and peak traffic-meter readings and the traffic monitor status:

```text
Router
>
show catalyst6000 traffic-meter
traffic meter = 0% Never cleared
peak = 0% reached at 10:54:49 UTC Wed Mar 19 2008
---=== Traffic Utilization Monitor Status ===---
State Interval Threshold MsgCount LastMsgTime
-----------------------------------------------------------------------------
Backplane Off 60s 80% 0 --
Fpoe#0 In Off 60s 80% 0 --
out Off 60s 80% 0 --
Fpoe#1 In Off 60s 80% 0 --
out Off 60s 80% 0 --
Fpoe#2 In Off 60s 80% 0 --
out Off 60s 80% 0 --
Fpoe#3 In Off 60s 80% 0 --
out Off 60s 80% 0 --
Fpoe#4 In Off 60s 80% 0 --
out Off 60s 80% 0 --
Fpoe#19 In Off 60s 80% 0 --
out Off 60s 80% 0 --
Router
>
```

This example shows how to display the failure recovery mode of the switching clock:

```text
Router> show catalyst6000 switching-clock
switching-clock: clock switchover and system reset is allowed
Router>
```


### `show cls`

> **Página:** 586 · **Modo:** EXEC · **Default:** Without the brief keyword, displays complete output. · **Leitura (show/clear/…):** sim

**Description:** To display the current status of all Cisco link services (CLS) sessions on the router, use the show clscommand in EXEC mode.

**Syntax:**

```text
show cls [brief]
```

**Parameters (Syntax Description):**

- `brief` — ( Optional) D is p l a y s a b r i e f version of the output.

**Command Default:** Without the brief keyword, displays complete output.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | This command was introduced in are l e as e p r i or to Cisco IOS Release11.0. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The Cisco link service (CLS) is used as the interface between data link users (DLUs), such as DLSw, LAN Network Manager (LNM), downstream physical unit (DSPU), and SNASw, and their corresponding data link circuits (DLCs) such as Logic Link Control (LLC), VDLC, and Qualified Logic Link Control (QLLC). Each DLU registers a particular service access point (SAP) with CLS, and establishes circuits through CLS over the DLC. The show cls command displays the SAP values associated with the DLU and the circuits established through CLS. For further information about CLS, use the Release 12.2 Cisco IOS Bridging and IBM Networking Configuration Guide.

**Example:**

The following is sample output from the show cls command:

```text
IBD-4500B#
show cls
DLU user:SNASW
SSap:0x04 VDLC VDLC650
DTE:1234.4000.0001 1234.4000.0002 04 04
T1 timer:0 T2 timer:0 Inact timer:0
max out:0 max in:0 retry count:10
XID retry:10 XID timer:5000 I-Frame:0
flow:0 DataIndQ:0 DataReqQ:0
DLU user:DLSWDLUPEER
DLU user:DLSWDLU
Bridging VDLC VDLC1000
Bridging VDLC VDLC650
```

The following is sample output from the show cls brief command:

```text
IBD-4500B# show cls brief
DLU user:SNASW
SSap:0x04 VDLC VDLC650
DTE:1234.4000.0001 1234.4000.0002 04 04
DLU user:DLSWDLUPEER
DLU user:DLSWDLU
Bridging VDLC VDLC1000
```

Bridging VDLC VDLC650 The examples show two DLUs--SNASw and DLSw--active in the router. SNASw uses a SAP value of 0x04, and the associated DLC port is VDLC650. SNASw has a circuit established between MAC addresses 1234.4000.0001 and 1234.4000.0002 using source and destination SAPs 04 and 04. DLSw is a bridging protocol and uses VDLC1000 and VDLC650 ports. There are no circuits in place at this time. In the output from the show cls command (without the brief argument), the values of timers and counters applicable to this circuit are displayed.


### `show config id`

> **Página:** 588 · **Modo:** Privileged EXEC (#) · **Default:** This command is disabled by default. If this command is not entered, the management system has to query the device for the current running-config file and then compare the results to the last known configuration to determine if a change has been made. · **Leitura (show/clear/…):** sim

**Description:** The configuration change tracking identifier (CTID) assigns a version number to each saved version of the running-config file. To display output about the versions, use the show config id command in privileged EXEC mode.

**Syntax:**

```text
show config id [detail]
```

**Parameters (Syntax Description):**

- `detail` — ( Optional) Expand s the output of the command to include the ID of the last user to make a configuration c h an g e and the process in which the c h an g e s were m a d e.

**Command Default:** This command is disabled by default. If this command is not entered, the management system has to query the device for the current running-config file and then compare the results to the last known configuration to determine if a change has been made.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRC | This command was introduced. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.4(20)T | This command was integrated into Cisco IOS Release12.4(20) T. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Usage Guidelines:**

This configuration infrastructure command assigns a version number that is updated every time the running-config file is changed. This version number is called the configuration change tracking identifier or CTID. The CTID can be used to compare configuration files to track configuration changes and take appropriate actions (for example, a configuration rollback). Config Logger can also use the CTID to determine if there have been any changes to the running-config file. CTID makes the management system more efficient by presenting information that indicates a change has been made to the running-config file. Without CTID, the management system has to query the device for the current running-config file and then compare the results to the last known configuration to determine if a change has been made.

**Example:**

The following example shows that the current running-config file is version 4 and that this file was saved on June 15, 2006 at 7.572 seconds after 3:02 p.m.:

```text
Device# show config id
version:4 time:2006-06-15T15:02:07.572Z
```

The following example shows that the current running-config file is version 9 and that this file was last saved on June 18, 2006 at 34.431 seconds after 6:34 p.m. The file was saved by the system and changed from Init:

```text
Device# show config id detail
Configuration version : 9
Last change time : 2006-06-18T18:34:34.431Z
Changed by user : system
Changed from process : Init
```

Field descriptions are self-explanatory.


### `show configuration id`

> **Página:** 589 · **Modo:** Privileged EXEC (#) · **Default:** This command is disabled by default. If this command is not entered, the management system has to query the device for the current running-config file and then compare the results to the last known configuration to determine if a change has been made. · **Leitura (show/clear/…):** sim

**Description:** To display output about configuration versions, use the show configuration idcommand in privileged EXEC mode.

**Syntax:**

```text
show configuration id [detail]
```

**Parameters (Syntax Description):**

- `detail` — ( Optional) Expand s the output of the command to include the ID of the last user to make a configuration c h an g e and the process in which the c h an g e s were m a d e.

**Command Default:** This command is disabled by default. If this command is not entered, the management system has to query the device for the current running-config file and then compare the results to the last known configuration to determine if a change has been made.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SRC | This command was introduced. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.4(20)T | This command was integrated into Cisco IOS Release12.4(20) T. |
| CiscoIOSXERelease2.5 | This command was i m p l e m e n t e do n Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Usage Guidelines:**

This configuration infrastructure command assigns a version number that is updated every time the running-config file is changed. This version number is called the configuration change tracking identifier (CTID). The CTID assigns a version number to each saved version of the running-config file. The CTID can be used to compare configuration files to track configuration changes and take appropriate actions (for example, a configuration rollback). Config Logger can also use the CTID to determine if there have been any changes to the running-config file. CTID makes the management system more efficient by presenting information that indicates a change has been made to the running-config file. Without CTID, the management system has to query the device for the current running-config file and then compare the results to the last known configuration to determine if a change has been made.

**Example:**

The following example shows that the current running-config file is version 4 and that this file was saved on June 15, 2006 at 7.572 seconds after 3:02 p.m.:

```text
Router# show configuration id
version:4 time:2006-06-15T15:02:07.572Z
```

The following example shows that the current running-config file is version 9 and that this file was last saved on June 18, 2006 at 34.431 seconds after 6:34 p.m. The file was saved by the system and changed from Init. The field descriptions are self-explanatory.

```text
Router# show configuration id detail
Configuration version : 9
Last change time : 2006-06-18T18:34:34.431Z
Changed by user : system
Changed from process : Init
```


### `show configuration lock`

> **Página:** 590 · **Modo:** Privileged EXEC(#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the lock status of the running configuration file during a configuration replace operation, use the show configuration lockcommand in privileged EXEC mode.

**Syntax:**

```text
show configuration lock
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC(#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(25)S | This command was introduced. |
| 12.3(14)T | This command was integrated into Cisco IOS Release12.3(14) T. The output of this command was u p d at e d to d is p l a y the configuration lock in g class. |
| 12.0(31)S | The command output was e n h an c e d. |
| 12.2(28)SB | This command was integrated into Cisco IOS Release12.2(28) S B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(31)SB2 | This command was i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| 12.2(33)SXH | This command was integrated into Cisco IOS Release12.2(33) S X H. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B and i m p l e m e n t e do n the Cisco10000 s e r i e s. |
| CiscoIOSXERelease 3.9S | This command was integrated into Cisco IOS X E Release3.9 S. |

**Example:**

The following is sample output from the show configuration lock command when the running configuration file is locked by another user. Cisco IOS Release 12.2(25)S, Release 12.2(28)SB, Release 12.3(14)T, and Later Releases

```text
Device# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Device(config)# configuration mode exclusive ?
auto Lock configuration mode automatically
manual Lock configuration mode on-demand
Device(config)#
configuration mode exclusive auto
Device(config)# end
Device# show running-config
| include configuration
configuration mode exclusive auto
Device# configure terminal
!<----------- Acquires the lock
Enter configuration commands, one per line. End with CNTL/Z.
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
Device(config)#
Device(config)# end
! <------------ Releases the lock
```

The following is sample output from the show configuration lock command when the running configuration file is not locked by another user.

```text
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
```

Cisco IOS Release 12.0(31)S, 12.2(33)SRA, and Later Releases

```text
Device# show configuration lock
Parser Configure Lock
------------------------------------------------------
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
```

The table below describes the significant fields shown in the displays.

| Field | Description |
| --- | --- |
| OwnerPID | Processidentifier(PID)oftheprocessthatownsthelock. |
| User | Owner’susername. |
| TTY | Owner’sterminalnumber. |
| Type | Locktype(EXCLUSIVE/COUNTER/NOLOCK). |
| State | Stateofthelock(FREE/LOCKED). |

| Field | Description |
| --- | --- |
| Class | Classificationofusersofthelock(EXPOSED/ROLLBACK).Processes otherthanROLLBACKbelongtotheEXPOSEDclass. |
| Count | Inthecaseofacounterlock,totalnumberofprocessesholdingthelock. |
| PendingRequests | Totalnumberofprocessesblockedbythelock. |
| Userdebuginfo | Anystringgivenbytheprocess(usedfordebuggingonly). |
| Sessionidlestate | Indicateswhethertheuserinanaccesssessionlockingsessionisidle. DisplaysTRUEorFALSE. |
| Noofexeccmdsgettingexecuted | TotalnumberofEXECcommands(showandclear)beingexecuted simultaneouslyfromdifferentsessions. |
| Noofexeccmdsblocked | TotalnumberofEXECcommands(showandclear)waitingforthe configurationcommand(runningfromtheaccesssessionlockingsession) tocompleteitsexecution. |
| Configwaitforshowcompletion | Indicateswhetheraconfigurationcommandexecutedinanaccesssession lockingsessioniswaitingforthecompletionoftheshowcommandbeing executedsimultaneouslyfromadifferentsession.DisplaysTRUEor FALSE. |
| Remoteipaddress | IPaddressoftheterminalfromwhichtheusertelnetedtotherouter. |
| Lockactivetime(inSec) | Amountoftime,inseconds,thatelapsedsincethelockwasacquired. |
| LockExpirationtimer(inSec) | Theamountoftime,inseconds,thatexpiresbeforethelockis automaticallyreleased. |

The following example shows how to configure the configuration file for single user auto configuration mode (using the configuration mode exclusive auto command). Use the configure terminalcommand to enter global configuration mode and lock the configuration mode exclusively. Once the Cisco IOS configuration mode is locked exclusively, you can verify the lock using the show configuration lockcommand.

```text
Device# configure terminal
Device(config)# configuration mode exclusive auto
Device(config)# end
Device# configure terminal
Device(config)# show configuration lock
Parser Configure Lock
Owner PID : 10
User : User1
TTY : 3
Type : EXCLUSIVE
State : LOCKED
Class : Exposed
Count : 0
Pending Requests : 0
User debug info : 0
```


### `show context`

> **Página:** 594 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information stored in NVRAM when an unexpected system reload (system exception) occurs, use the show context command in user EXEC or priviledged EXEC mode.

**Syntax:**

```text
show context [summary | all | slot slot-number [crash-index] [all] [debug]]
```

**Parameters (Syntax Description):**

- `summary` — D is p l a y s as u m m a r y of all the c r as h e s r e c or d e d.
- `all` — D is p l a y s all c r as h e s for all the slot s. When optional l y used with the slot keyword, d is p l a y s c r as h information for the specified slot.
- `slot slot-number crash-index` — D is p l a y s information for apa r t i c u l a r line card. Slot numbers range from0 to11 for the Cisco12012 router and from0 to7 for the Cisco12008. The in d e x number all o w s you to l o o k at previous c r as h context s. Context s from the last24 line card c r as h e s are save do n the GRPcard. Ifthe GRP reload s, the last24 line card c r as h context s are l o s t. For example, show context slot32 shows these c on d most r e c e n t c r as h for line card in slot3. In d e x numbers are d is p l a y e d by the show context summary command.
- `debug` — ( Optional) D is p l a y s c r as h information as a h e x r e c or d dump in a d d it i onto one of the options list e d.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 11.2GS | Theslot slot-number[ c r as h-in d e x][ all][ debug] syntax was added for Cisco12000 s e r i e s routers. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The display from the show context command includes the following information: • Reason for the system reboot • Stack trace • Software version • The signal number, code, and router uptime information • All the register contents at the time of the crash Note This command is primarily for use by Cisco technical support representatives for analyzing unexpected system reloads. Output for this command will vary by platform. Context information is specific to processors and architectures. For example, context information for the Cisco 2600 series router differs from that for other router types because the Cisco 2600 runs with an M860 processor.

**Example:**

The following is sample output from the show context command following a system failure:

```text
Router> show context
System was restarted by error - a Software forced crash, PC 0x60189354
GS Software (RSP-PV-M), Experimental Version 11.1(2033) [ganesh 111]
Compiled Mon 31-Mar-97 13:21 by ganesh
Image text-base: 0x60010900, data-base: 0x6073E000
Stack trace from system failure:
FP: 0x60AEA798, RA: 0x60189354
FP: 0x60AEA798, RA: 0x601853CC
FP: 0x60AEA7C0, RA: 0x6015E98C
FP: 0x60AEA7F8, RA: 0x6011AB3C
FP: 0x60AEA828, RA: 0x601706CC
FP: 0x60AEA878, RA: 0x60116340
FP: 0x60AEA890, RA: 0x6011632C
Fault History Buffer:
GS Software (RSP-PV-M), Experimental Version 11.1(2033) [ganesh 111]
Compiled Mon 31-Mar-97 13:21 by ganesh
Signal = 23, Code = 0x24, Uptime 00:04:19
$0 : 00000000, AT : 60930120, v0 : 00000032, v1 : 00000120
a0 : 60170110, a1 : 6097F22C, a2 : 00000000, a3 : 00000000
t0 : 60AE02A0, t1 : 8000FD80, t2 : 34008F00, t3 : FFFF00FF
t4 : 00000083, t5 : 3E840024, t6 : 00000000, t7 : 11010132
s0 : 00000006, s1 : 607A25F8, s2 : 00000001, s3 : 00000000
s4 : 00000000, s5 : 00000000, s6 : 00000000, s7 : 6097F755
t8 : 600FABBC, t9 : 00000000, k0 : 30408401, k1 : 30410000
gp : 608B9860, sp : 60AEA798, s8 : 00000000, ra : 601853CC
EPC : 60189354, SREG : 3400EF03, Cause : 00000024
Router>
```

The following is sample output from the show context summary command on a Cisco 12012 router. The show context summary command displays a summary of all the crashes recorded for each slot (line card).

```text
Router# show context summary
CRASH INFO SUMMARY
Slot 0 : 0 crashes
Slot 1 : 0 crashes
Slot 2 : 0 crashes
Slot 3 : 0 crashes
Slot 4 : 0 crashes
Slot 5 : 0 crashes
Slot 6 : 0 crashes
Slot 7 : 2 crashes
1 - crash at 18:06:41 UTC Tue Nov 5 1996
2 - crash at 12:14:55 UTC Mon Nov 4 1996
Slot 8 : 0 crashes
Slot 9 : 0 crashes
Slot 10: 0 crashes
Slot 11: 0 crashes
```

The following is sample output from the show contextcommand following an unexpected system reload on a Cisco 2600 series router.

```text
router# show context
S/W Version: Cisco IOS Software
Cisco IOS (tm) c2600 Software (c2600-JS-M), Released Version 11.3(19980115:184921]
Copyright (c) 1986-2003 by Cisco Systems, Inc.
Compiled Thu 15-Jan-98 13:49 by mmagno
Exception occurred at: 00:02:26 UTC Mon Mar 1 1993
Exception type: Data TLB Miss (0x1200)
CPU Register Context:
PC = 0x80109964 MSR = 0x00009030 CR = 0x55FFFD35 LR = 0x80109958
CTR = 0x800154E4 XER = 0xC000BB6F DAR = 0x00000088 DSISR = 0x00000249
DEC = 0x7FFFDFCA TBU = 0x00000000 TBL = 0x15433FCF IMMR = 0x68010020
R0 = 0x80000000 R1 = 0x80E80BD0 R2 = 0x80000000 R3 = 0x00000000
R4 = 0x80E80BC0 R5 = 0x40800000 R6 = 0x00000001 R7 = 0x68010000
R8 = 0x00000000 R9 = 0x00000060 R10 = 0x00001030 R11 = 0xFFFFFFFF
R12 = 0x00007CE6 R13 = 0xFFF379E8 R14 = 0x80D50000 R15 = 0x00000000
R16 = 0x00000000 R17 = 0x00000000 R18 = 0x00000000 R19 = 0x00000000
R20 = 0x00000000 R21 = 0x00000001 R22 = 0x00000010 R23 = 0x00000000
R24 = 0x00000000 R25 = 0x80E91348 R26 = 0x01936010 R27 = 0x80E92A80
R28 = 0x00000001 R29 = 0x019BA920 R30 = 0x00000000 R31 = 0x00000018
Stack trace:
Frame 00: SP = 0x80E80BD0 PC = 0x80109958
Frame 01: SP = 0x80E80C28 PC = 0x8010A720
Frame 02: SP = 0x80E80C40 PC = 0x80271010
Frame 03: SP = 0x80E80C50 PC = 0x8025EE64
Frame 04: SP = 0x80DEE548 PC = 0x8026702C
Frame 05: SP = 0x80DEE558 PC = 0x8026702C
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| S/WVersion | StandardCiscoIOSversionstringasdisplayed. |
| Exceptionoccurredat | Routerrealtimewhenexceptionoccurred.Theroutermusthavetheclocktime properlyconfiguredforthistobeaccurate. |
| Exceptiontype | Technicalreasonforexception.Forengineeringanalysis. |
| CPURegisterContext | Technicalprocessorstateinformation.Forengineeringanalysis. |
| Stacktrace | Technicalprocessorstateinformation.Forengineeringanalysis. |


### `show controllers (GRP image)`

> **Página:** 597 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information that is specific to the hardware, use the show controllerscommand in privileged EXEC mode.

**Syntax:**

```text
show controllers [atm slot-number | clock | csar [register] | csc-fpga | dp83800 | fab-clk | fia [register]
| pos [slot-number] [details] | queues [slot-number] | sca | xbar]
```

**Parameters (Syntax Description):**

- `atm slot-number` — ( Optional) D is p l a y s the AT M controllers. Number is slot-number/ port-number( for example,4/0). Slot numbers range from0 to11 for the Cisco12012 router and from 0 to7 for the Cisco12008 router.
- `clock` — ( Optional) D is p l a y s the clock card configuration.
- `csar [register` — ( Optional) D is p l a y s the Cisco Cell S e g m e n t at i on and R e as s e m b l y( C S A R) information. C S A R is then a m e of the c h ip on the card that h and l e s traffic be t we e n the GRP and the switch f a b r i c interface ASICs.
- `csc-fpga` — ( Optional) D is p l a y s the clock and scheduler card register information in the f i e l d p r o g r a m m a b l e g at e a r r a y( F P G A).
- `dp83800` — ( Optional) D is p l a y s the E the r n e t information on the GRPcard.
- `fab-clk` — ( Optional) D is p l a y the switch f a b r i c clock register information. The switch f a b r i c clock F P G A is a c h ip that monitor s the incoming f a b r i c clock generate d by the switch fabric. This clock is n e e d e d by each card c on n e c t in gt o the switch f a b r i c to p r o p e r l y c o m m u n i c at e with it. Two switch f a b r i c clock s a r r i v e at each card; only one can be used. The F P G A monitor s both clock s and s e l e c t s which one to use if only one of the m isr u n n in g.
- `fia register` — ( Optional) D is p l a y s the f a b r i c interface AS I C information and optional l y d is p l a y s the register information.
- `pos [slot-number] [details` — ( Optional) D is p l a y s the P O S f r a m e r state and optional l y d is p l a y s all the detail s for the interface. Number is slot-number/ port-number( for example,4/0). Slot numbers range from0 to11 for the Cisco12012 router and from0 to7 for the Cisco12008 router.
- `queues [slot-number` — ( Optional) D is p l a y s the S D R A M buffer c a r v e information and optional l y d is p l a y s the information for as p e c if i c line card. The S D R A M buffer c a r v e information d is p l a y e d is s u g g e s t e d c a r v e information from the GRP card to the line card. Line card s might c h an get h e show n percentage s b as e do n S D R A M a v a i l a b l e. Slot numbers range from0 to11 for the Cisco12012 router and from0 to7 for the Cisco12008.
- `sca` — ( Optional) D is p l a y s the S C Are g is t e r information. The SCAisan AS I C that a r b it r at e s a m on gt h e line card s request s to use the switch f a b r i c.
- `xbar` — ( Optional) D is p l a y s the c r o s s b a r register information. The X B A R is an AS I C that switch e s the data as it pass e s t h r o u g h the switch f a b r i c.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2GS | This command was introduced to support the Cisco12000 s e r i e s routers. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This information provided by this command is intended for use only by technical support representatives in analyzing system failures in the field.

**Example:**

The following is sample output from the show controllers pos command for a Cisco 12012:

```text
Router# show controllers pos 7/0
POS7/0
SECTION
LOF = 2 LOS = 0 BIP(B1) = 5889
Active Alarms: None
LINE
AIS = 2 RDI = 2 FEBE = 146 BIP(B2) = 2106453
Active Alarms: None
PATH
AIS = 2 RDI = 4 FEBE = 63 BIP(B3) = 3216
LOP = 0 PSE = 8 NSE = 3 NEWPTR = 2
Active Alarms: None
APS
COAPS = 3 PSBF = 2
State: PSBF_state = False
Rx(K1/K2): F0/15 Tx(K1/K2): 00/00
S1S0 = 00, C2 = 64
PATH TRACE BUFFER : STABLE
Remote hostname : GSR-C
Remote interface: POS10/0
Remote IP addr : 10.201.101.2
Remote Rx(K1/K2): F0/15 Tx(K1/K2): 00/00
```


### `show controllers (line card image)`

> **Página:** 598 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information that is specific to the hardware on a line card, use the attach command in privileged EXEC mode to connect to the line card and then use the show controllers command in privileged EXEC mode or the execute-on command in privileged EXEC mode.

**Syntax:**

```text
show controllers atm [[port-number] [all | sar | summary]]
show controllers fia [register]
show controllers {frfab | tofab} {bma {microcode | ms-inst | register} | qelem start-queue-element
[end-queue-element] | qnum start-queue-element [end-queue-element] | queues | statistics}
show controllers io
show controllers l3
show controllers pos {framers | queues | registers | rxsram port-number queue-start-address
[queue-length] | txsram port-number queue-start-address [queue-length]}
show controllers events [clear | punt-sniff [none | word1 | word2] | punt-verbose [all]]
```

**Parameters (Syntax Description):**

- `atm` — D is p l a y s the AT M control l e r information.
- `port-number` — ( Optional) D is p l a y s request for the p h y s i c a l interface on the ATMcard. The range of c h o i c e s is from0 to3.
- `all` — ( Optional) List s all detail s.
- `sar` — ( Optional) List s S A R in t e r a c t i v e command.
- `summary` — ( Optional) List s S A R status summary.
- `fia` — D is p l a y s the f a b r i c interface AS I C information.
- `register` — ( Optional) D is p l a y s the register information.
- `frfab` — ( Optional) D is p l a y s the" from"( t r an s m it) f a b r i c information.
- `tofab` — ( Optional) D is p l a y s the" to"( r e c e i v e) f a b r i c information.
- `bma` — For the f r f a b or to f a b keywords, d is p l a y s microcode, m i c r o sequence r, or register information for the s i l i c on q u e u in g e n g in e( S Q E), also k no w n as the buffer management ASIC(BMA).
- `microcode` — D is p l a y s S Q E information for the microcode bundle d in the line card and current l y running version.
- `mis-inst` — D is p l a y s S Q E information for the m i c r o sequence r in s t r u c t i on.
- `register` — D is p l a y s s i l i c on q u e u in g e n g in e( S Q E) information for the register.
- `qelem` — For the f r f a b or to f a b keywords, d is p l a y s the S D R A M buffer pool queue e l e m e n t summary information.
- `start-queue-element` — Specifies the start queue e l e m e n t number from0 to65535.
- `end-queue-element` — ( Optional) Specifies the end queue e l e m e n t number from0 to65535).
- `qnum` — For the f r f a b or to f a b keywords, d is p l a y s the S D R A M buffer pool queue detail information.
- `start-queue-number` — Specifies the start free queue number( from0 to127).
- `end-queue-number` — ( Optional) Specifies the end free queue number( from0 to127).
- `queues` — For the f r f a b or to f a b keywords, d is p l a y s the S D R A M buffer pool information.
- `statistics` — For the f r f a b or to f a b keywords, d is p l a y s the B MAc o u n t e r s.
- `io` — D is p l a y s in p u t/ output register s.
- `l3` — D is p l a y s L a y e r3 AS I C information.
- `pos` — D is p l a y s p a c k e t-over-s on i c( P O S) information for f r a m e r register s, f r a m e r queue s, and AS I C register s.
- `framers` — D is p l a y s the P O S f r a m e r register s.
- `queues` — D is p l a y s the P O S f r a m e r queue information.
- `register s` — D is p l a y s the AS I C register s.
- `rxsram` — D is p l a y s the r e c e i v e queue SRAM.
- `port-number` — Specifies ap or t number( v a l id range is from0 to3).
- `queue-start-address` — Specifies the queue S R A M log i c a l starting address.
- `queue-length` — ( Optional) Specifies the queue S R A M length.
- `txsram` — D is p l a y s the t r an s m it queue SRAM.
- `events` — D is p l a y s the line card count e r information of events generate d from line card.
- `clear` — ( Optional) Clear s all the line card event count e r output detail s that are d is p l a y e d using the commands: show controllers events, show controllers events p u n t-v e r b o s e, and show controllers events p u n t-s n if f.
- `punt-sniff` — ( Optional) S n if f s the p a c k e t s s e n t to route processor from line card by specify in gt h e w or d and location. Note P u n t s n if f is enabled only if one of the w or d is configure d.
- `none` — ( Optional) Clear s the at t r i but e s and p a c k e t s to be s n if f e d from route processor and reset s the counters to z e r o.
- `word1` — ( Optional) S n if f s p a c k e t s s e n t to the route processor for the specified hexadecimal value of w or d1. Location of the w or d is optional.
- `word2` — ( Optional) S n if f s p a c k e t s s e n t to the route processor m at c h in gt h e specified h e x a decimal value of w or d2. Location of the w or d is optional.
- `punt-verbose` — ( Optional) D is p l a y s ap p l i c at i on-w is e p a c k e t s p u n t to route processor( R P) from line card( L C). D is p l a y s no n-z e r o p u n t counters if the command is execute d with out the all keyword.
- `all` — ( Optional) D is p l a y s z e r o and no n-z e r o p u n t counters of p a c k e t s p u n t to RPfrom LC. The all keyword is used a l on g with the commands how controllers events p u n t-v e r b o s e all.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2GS | This command was added to support the Cisco12000 s e r i e s Gigabit Switch Routers. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(31)SB | This command was integrated in Cisco IOS Release12.2(31) S B. |
| 12.2(33)SB | This command’ be h a v i or was modified on the Cisco10000 s e r i e s router for the PRE3and PRE4. |
| 12.0(33)S | The keywords p u n t-s n if f and p u n t-v e r b o s e were added in the commands how controllers events for the Cisco12000 S e r i e s Routers. |

**Usage Guidelines:**

This information displayed by this command is of use only to technical support representatives in analyzing unexpected system failures in the field. It is documented here in case you need to provide the displayed statistics to an technical support engineer. Cisco 10000 Series Router Usage Guidelines In releases prior to Cisco IOS Release 12.2(33)SB, when you configure the t1 loopback remote command on the local router, the command also displays in the running-config file of the far-end router. This is due to the route processor (RP) updating an incorrect parameter when it receives the loopback event message from the line card for loopback requests from the far end. In Cisco IOS Release 12.2(33)SB, the RP updates the correct parameter and the show controllers command correctly displays the loopback CLI commands applied on the local end and displays the loopback events and status received from the line card in response to loopback requests from the far end. This change in behavior affects the following line cards and is documented in the CSCsm84447 caveat: • 4-port channelized STM1 • 1-port channelized OC-12 • 6-port channelized T3 • 4-port half-height channelized T3 In Cisco IOS Release 12.2(33)SB, the output from the show controller command includes line code information for the 6-port channelized T3 line card and the 8-port E3/DS3 line card. However, because SONET line cards do not have a direct physical link at the T3 or E3 level, the output from the show controller t3 command does not include line code information. In Cisco IOS Release 12.2(31)SB, the output from the show controller command displays line code information. The output of the show controller t3 command for SONET-based T3 also includes line code information. Cisco 12000 Series Router Usage Guidelines The packets processed by a line card are either sent to a route processor or a line card in the form of Cisco cells. To track the packets sent to a route processor from a line card is essential for troubleshooting. The keywords punt-sniff and punt-verbose have been added for the command show controllers events to identify the packets sent to RP from LC. By default, the feature is enabled and packets punt to route processor are displayed using the command show controllers events punt-verbose. To view all the zero and non-zero punt counters use the command show controllers events punt-verbose all. To clear all the line card events and counters including resetting the packets to be sniffed to zero, executing the command show controllers events clear. Packets sent to route processor from line card can be sniffed by specifying the hexa-decimal value of the word. Packets can only be sniffed if the word along with the hexa-decimal value is specified. Specifying the location of the word, sniffs packets from the particular location. To reset the counters of packets to be sniffed to zero, execute the command show controllers events punt-sniff none. For example, use the command show controllers events punt-sniff word1 0x60000000 to sniff packets punt to RP with the hexa-decimal value 0x60000000. As the location is not specified, it searches the entire buffer for the value 0x60000000. Packets punt to RP can also be sniffed by specifying a particular location using the command show controllers events punt-sniff word1 0x60000000 34.

**Example:**

Because you are executing this command on the line card, you must use the execute-on command to use the show command, or you must connect to the card using the attach command. All examples in this section use the execute-on command The following is partial sample output from the command: show controllers atm

```text
Router# execute-on slot 4 show controllers atm 0
TX SAR (Beta 1.0.0) is Operational;
RX SAR (Beta 1.0.0) is Operational;
Interface Configuration Mode:
STS-12c
Active Maker Channels: total # 6
VCID ChnnlID Type OutputInfo InPkts InOAMs MacString
1 0888 UBR 0C010010 0 0 08882000AAAA030000000800
2 0988 VBR 04010020 0 0 09882000
3 8BC8 UBR 0C010030 0 0 8BC82000AAAA030000000800
4 0E08 UBR 0C010040 0 0 0E082000AAAA030000000800
10 1288 VBR 040100A0 0 0 12882000
11 8BE8 VBR 0C0100B0 0 0 8BE82000AAAA030000000800
SAR Total Counters:
total_tx_idle_cells 215267 total_tx_paks 0 total_tx_abort_paks 0
total_rx_paks 0 total_rx_drop_paks 0 total_rx_discard_cells 15
Switching Code Counters:
total_rx_crc_err_paks 0 total_rx_giant_paks 0
total_rx_abort_paks 0 total_rx_crc10_cells 0
total_rx_tmout_paks 0 total_rx_unknown_paks 0
total_rx_out_buf_paks 0 total_rx_unknown_vc_paks 0
BATMAN Asic Register Values:
hi_addr_reg 0x8000, lo_addr_reg 0x000C, boot_msk_addr 0x0780,
rmcell_msk_addr 0x0724, rmcnt__msk_addr 0x07C2, txbuf_msk_addr 0x070C,
CM622 SAR Boot Configuration:
txind_q_addr 0x14000 txcmd_q_addr 0x20000
SUNI-622 Framer Register Values:
Master Rst and Ident/Load Meters Reg (#0x0): 0x10
Master Configuration Reg (#0x1): 0x1F
Master Interrupt Status Reg (#0x2): 0x00
PISO Interrupt Reg (#0x3): 0x04
Master Auto Alarm Reg (#0x4): 0x03
Master Auto Alarm Reg (#0x5): 0x07
Parallel Output Port Reg (#0x6): 0x02
BERM Line BIP Threshold LSB Reg (#0x74): 0x00
BERM Line BIP Threshold MSB Reg (#0x75): 0x00
```

The following is partial sample output from the show controllers command:

```text
Router# execute-on slot 6 show controllers
Interface POS0
Hardware is BFLC POS
lcpos_instance struct 60311B40
RX POS ASIC addr space 12000000
TX POS ASIC addr space 12000100
SUNI framer addr space 12000400
SUNI rsop intr status 00
CRC32 enabled, HDLC enc, int clock
no loop
Interface POS1
Hardware is BFLC POS
lcpos_instance struct 603142E0
RX POS ASIC addr space 12000000
TX POS ASIC addr space 12000100
SUNI framer addr space 12000600
SUNI rsop intr status 00
CRC32 enabled, HDLC enc, int clock
no loop
```

The following is partial sample output from the show controllers pos framers command:

```text
Router# execute-on slot 6 show controllers pos framers
Framer 0, addr=0x12000400:
master reset C0
master config 1F rrate sts3c trate sts3c fixptr
master control 00
clock rcv cntrl D0
RACP control 84
RACP gfc control 0F
TACP control status 04 hcsadd
RACP intr enable 04
RSOP cntrl intr enable 00
RSOP intr status 00
TPOP path sig lbl (c2) 13
SPTB control 04 tnull
SPTB status 00
Framer 1, addr=0x12000600:
master reset C0
master config 1F rrate sts3c trate sts3c fixptr
master control 00
clock rcv cntrl D0
RACP control 84
RACP gfc control 0F
TACP control status 04 hcsadd
RACP intr enable 04
RSOP cntrl intr enable 00
RSOP intr status 00
TPOP path sig lbl (c2) 13
SPTB control 04 tnull
SPTB status 00
Framer 2, addr=0x12000800:
master reset C0
master config 1F rrate sts3c trate sts3c fixptr
master control 00
clock rcv cntrl D0
RACP control 84
RACP gfc control 0F
TACP control status 04 hcsadd
RACP intr enable 04
RSOP cntrl intr enable 00
RSOP intr status 00
TPOP path sig lbl (c2) 13
SPTB control 04 tnull
SPTB status 00
```

The following is partial sample output from the show controllers fia command:

```text
Router# execute-on slot 7 show controllers fia
========= Line Card (Slot 7) =======
Fabric configuration: Full bandwidth redundant
Master Scheduler: Slot 17
From Fabric FIA Errors
-----------------------
redund fifo parity 0 redund overflow 0 cell drops 0
crc32 lkup parity 0 cell parity 0 crc32 0
0 1 2 3 4
-------- -------- -------- -------- --------
los 0 0 0 0 0
crc16 0 0 0 0 0
To Fabric FIA Errors
-----------------------
sca not pres 0 req error 0 uni fifo overflow 0
grant parity 0 multi req 0 uni fifo undrflow 0
cntrl parity 0 uni req 0 crc32 lkup parity 0
multi fifo 0 empty dst req 0 handshake error 0
```

The following is a sample output from the show controllers eventscommand:

```text
execute-on slot 7 show controllers events
Switching Stats
Packets punt to RP: 935
HW engine punt: 62
HW engine reject: 38113520
RX HW Engine Reject Counters
Unrecognized Protocol ID: 19182546
IP TTL Expired: 14706652
Unrecognized L2 Frame: 4224320
IPv6 Control pkts: 2
```

The following is a sample output from the show controllers events punt-verbose command:

```text
execute-on slot 7 show controllers events punt-verbose
RP Punted L2 Statistics in Verbose
------------------------------------
HDLC Encap : 927
RP Punted L3 Statistics in Verbose
------------------------------------
ICMP : 40
UDP : 441
OSPF : 211
IPV6 : 40
RP Punted L3 Application Statistics in Verbose
-----------------------------------------------
LDP : 441
DF Bit not Set : 692
```

The following is a partial sample output from the show controllers events punt-verbose all command which displays the zero and non-zero value of packets punt to RP from LC:

```text
execute-on slot 7 show controllers events punt-verbose all
RP Punted L2 Statistics in Verbose
------------------------------------
L2 Protocol - 0 : 0
ARPA Encap : 0
L2 Protocol - 2 : 0
L2 Protocol - 3 : 0
L2 Protocol - 4 : 0
HDLC Encap : 941
L2 Protocol - 6 : 0
L2 Protocol - 7 : 0
L2 Protocol - 8 : 0
L2 Protocol - 9 : 0
L2 Protocol - 10 : 0
L2 Protocol - 11 : 0
L2 Protocol - 12 : 0
L2 Protocol - 13 : 0
L2 Protocol - 14 : 0
L2 Protocol - 15 : 0
PPP Encap : 0
L2 Protocol - 17 : 0
L2 Protocol - 18 : 0
L2 Protocol - 19 : 0
Frame Relay Encap : 0
L2 Protocol - 21 : 0
L2 Protocol - 22 : 0
L2 Protocol - 23 : 0
L2 Protocol - 24 : 0
L2 Protocol - 25 : 0
L2 Protocol - 26 : 0
L2 Protocol - 27 : 0
L2 Protocol - 28 : 0
L2 Protocol - 29 : 0
L2 Protocol - 30 : 0
L2 Protocol - 31 : 0
L2 Protocol - 32 : 0
ATM Encap : 0
L2 Protocol - 34 : 0
L2 Protocol - 35 : 0
RP Punted L3 Statistics in Verbose
------------------------------------
HOPOPT : 0
ICMP : 40
IGMP : 0
L3 Protocol - 3 : 0
IPINIP : 0
L3 Protocol - 5 : 0
RP Punted L3 Application Statistics in Verbose
-----------------------------------------------
MPLS OAM : 0
FTP : 0
FTPD : 0
TFTP : 0
.....
```

The following is a sample output from the show controllers events clear command:

```text
execute-on slot 7 show controllers events clear
Drop, switching and reject counters cleared
```

The following is a sample output from the show controllers events punt-sniff command:

```text
Router# execute-on slot 7 show controllers events punt-sniff
Punt Sniff Statistics
--------------------------------
Word Location Occurance
0x60000000 34 0
0xB6010102 37 5
Note: Location offset taken from the begining of BufferHeader(32 bytes).
```

The following is a sample output from the show controllers events punt-sniff word1 0x60000000 command. This command is used to sniff a packet with a hexa-decimal value 0x60000000from the start of the buffer header of the packet being punt to RP:

```text
Router# execute-on slot 7 show controllers events punt-sniff word1 0x60000000
```

The following is a sample output from the show controllers events punt-sniff word1 0x60000000 34command. This command is used to sniff a packet with a hexa-decimal value 0x600000000 at the location 34 from the start of the buffer header of the packet being punt to RP:

```text
Router# 0x60000000 34
execute-on slot 7 show controllers events punt-sniff word1
```

The following is a sample output from the show controllers events punt-sniff none command. This command is used to clear the counter of packets to be sniffed:

```text
Router# execute-on slot 7 show controllers events punt-sniff none
```


### `show controllers logging`

> **Página:** 606 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display logging information about a Versatile Interface Processor (VIP) card, use the show controllers logging command in privileged EXEC mode.

**Syntax:**

```text
show controllers vip slot-number logging
```

**Parameters (Syntax Description):**

- `vip slot-number` — V IP slot number.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command displays the state of syslog error and event logging, including host addresses, and whether console logging is enabled. When enabled, “trap logging” allows messages to be sent to a remote host (a syslog server).

**Example:**

The following is sample output from the show controllers logging command:

```text
Router# show controllers vip 1 logging
show logging from Slot 1:
Syslog logging:enabled (0 messages dropped, 1 messages rate-limited, 0 flushes, 0 overruns)
Console logging: disabled
Monitor logging: level debugging, 0 messages logged
Buffer logging: level debugging, 24 messages logged
Trap logging: level informational, 266 messages logged.
Logging to 209.165.202.129
Exception Logging size: 4096 bytes
Count and timestamp logging messages:disabled
Log Buffer (8192 bytes):
smallest_local_pool_entries = 256, global particles = 5149
highest_local_visible_bandwidth = 155000
00:00:05:%SYS-5-RESTART:System restarted --
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Sysloglogging | Showsgeneralstateofsystemlogging(enabledordisabled),andstatusofloggedmessages (numberofmessagesdropped,rate-limited,orflushed). |
| Consolelogging | Loggingtotheconsoleport.Shows"disabled"or,ifenabled,theseveritylevellimitand numberofmessageslogged. Enabledusingtheloggingconsolecommand. |
| Monitorlogging | Loggingtothemonitor(allTTYlines).Shows"disabled"or,ifenabled,theseveritylevel limitandnumberofmessageslogged. Enabledusingtheloggingmonitorcommand. |

| Field | Description |
| --- | --- |
| Bufferlogging | Loggingtothestandardsyslogbuffer.Shows"disabled"or,ifenabled,theseveritylevel limitandnumberofmessageslogged. Enabledusingtheloggingbufferedcommand. |
| Traplogging | Loggingtoaremotehost(sysloghost).Shows"disabled"or,ifenabled,theseveritylevel limitandnumberofmessageslogged. (Theword"trap"meansatriggerinthesystemsoftwareforsendingerrormessagestoa remotehost.) Enabledusingthelogginghostcommand.Theseveritylevellimitissetusingthelogging trapcommand. |


### `show controllers tech-support`

> **Página:** 608 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display general information about a Versatile Interface Processor (VIP) card when reporting a problem, use the show controllers tech-support command in privileged EXEC mode.

**Syntax:**

```text
show controllers vip slot-number tech-support
```

**Parameters (Syntax Description):**

- `vip slot-number` — V IP slot number.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to help collect general information about a VIP card when you are reporting a problem. This command displays the equivalent of the following show commands for the VIP card: • more system:running-config • show buffers • show controllers • show interfaces • show processes cpu • show processes memory • show stacks • show version For a sample display of the show controllers tech-support command output, refer to these show commands.


### `show coverage history`

> **Página:** 609 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the system history table, use the show coverage historycommand in privileged EXEC mode.

**Syntax:**

```text
show coverage history [all | first number-of-entries | last number-of-entries | status]
```

**Parameters (Syntax Description):**

- `all` — ( Optional) D is p l a y s the e n t i r e history t a b l e.
- `first` — ( Optional) D is p l a y s the o l d e s t e n t r i e s in the history t a b l e.
- `number-of-entries` — ( Optional) Number of e n t r i e s to be d is p l a y e d. The range is from1 to100000.
- `last` — ( Optional) D is p l a y s the l at e s t e n t r i e s in the history t a b l e.
- `status` — ( Optional) D is p l a y s the status of the history system.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(24)T | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release12.4(24) T. |

**Example:**

The following is sample output from the show coverage history command. The output is self-explanatory.

```text
Router# show coverage history status
History table size is 23 entries. 0 entries have been used.
Low-level count handler has been called 0 times.
There were 0 entries not traced due to recursion detection.
There were 0 entries not traced due to internal pauses.
```


### `show data-corruption`

> **Página:** 610 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display data inconsistency errors of the present software version, use the show data-corruptioncommand in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show data-corruption
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(22)SE | This command was introduced. |
| 12.2(33)SRB | This command was integrated into Cisco IOS Release12.2(33) SRB. |
| 12.4(20)T | This command was integrated into Cisco IOS Release12.4(20) T. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |
| CiscoIOS2.3 XE | This command was integrated into Cisco IOS X E Release2.3. |

**Usage Guidelines:**

Use this command to display all data inconsistency errors or the corrupt data. If there are no data errors, the “No data inconsistency errors have been recorded” message is displayed.

**Example:**

The following is sample output from show data-corruption command. The fields are self-explanatory.

```text
Router# show data-corruption
Data inconsistency records for:
3800 Software (C3845-ADVIPSERVICESK9-M), Version 12.4(24)T, RELEASE
SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Compiled Thu 17-Dec-09 09:02 by xyz
Count Traceback
1842 60523C58, 616E85FC 60523C58 62A9F648
1: Jun 12 18:24:33.960
2: Jun 12 18:24:33.960
3: Jun 12 18:24:33.960
1842: Jun 19 00:30:51.350
```


### `show debugging`

> **Página:** 611 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about the types of debugging that are enabled for your router, use the show debugging command in privileged EXEC mode.

**Syntax:**

```text
show debugging
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | This command was introduced. |
| 12.3(7)T | The output of this command was e n h an c e d to show TCP E x p l i c it C on g e s t i on Not if i c at i on ( E C N) configuration. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(31)SB2 | This command was integrated into Cisco IOS Release12.2(31) S B2. |
| 12.2SX | This command is supported in the Cisco IOS Release12.2 S X t r a in. Support in as p e c if i c 12.2 S X release of this t r a in d e p end s on your f e at u reset, platform, and platform hardware. |
| 12.4(20)T | The output of this command was e n h an c e d to show the user-group debugging configuration. |

**Example:**

The following is sample output from the show debugging command. In this example, the remote host is not configured or connected.

```text
Router# show debugging
!
TCP:
TCP Packet debugging is on
TCP ECN debugging is on
!
Router# telnet 10.1.25.234
!
Trying 10.1.25.234 ...
!
00:02:48: 10.1.25.31:11001 <---> 10.1.25.234:23 out ECN-setup SYN
00:02:48: tcp0: O CLOSED 10.1.25.234:11001 10.1.25.31:23 seq 1922220018
OPTS 4 ECE CWR SYN WIN 4128
00:02:50: 10.1.25.31:11001 <---> 10.1.25.234:23 congestion window changes
00:02:50: cwnd from 1460 to 1460, ssthresh from 65535 to 2920
00:02:50: tcp0: R SYNSENT 10.1.25.234:11001 10.1.25.31:23 seq 1922220018
OPTS 4 ECE CWR SYN WIN 4128
00:02:54: 10.1.25.31:11001 <---> 10.1.25.234:23 congestion window changes
00:02:54: cwnd from 1460 to 1460, ssthresh from 2920 to 2920
00:02:54: tcp0: R SYNSENT 10.1.25.234:11001 10.1.25.31:23 seq 1922220018
OPTS 4 ECE CWR SYN WIN 4128
00:03:02: 10.1.25.31:11001 <---> 10.1.25.234:23 congestion window changes
00:03:02: cwnd from 1460 to 1460, ssthresh from 2920 to 2920
00:03:02: tcp0: R SYNSENT 10.1.25.234:11001 10.1.25.31:23 seq 1922220018
OPTS 4 ECE CWR SYN WIN 4128
00:03:18: 10.1.25.31:11001 <---> 10.1.25.234:23 SYN with ECN disabled
00:03:18: 10.1.25.31:11001 <---> 10.1.25.234:23 congestion window changes
00:03:18: cwnd from 1460 to 1460, ssthresh from 2920 to 2920
00:03:18: tcp0: O SYNSENT 10.1.25.234:11001 10.1.25.31:23 seq 1922220018
OPTS 4 SYN WIN 4128
00:03:20: 10.1.25.31:11001 <---> 10.1.25.234:23 congestion window changes
00:03:20: cwnd from 1460 to 1460, ssthresh from 2920 to 2920
00:03:20: tcp0: R SYNSENT 10.1.25.234:11001 10.1.25.31:23 seq 1922220018
OPTS 4 SYN WIN 4128
00:03:24: 10.1.25.31:11001 <---> 10.1.25.234:23 congestion window changes
00:03:24: cwnd from 1460 to 1460, ssthresh from 2920 to 2920
00:03:24: tcp0: R SYNSENT 10.1.25.234:11001 10.1.25.31:23 seq 1922220018
OPTS 4 SYN WIN 4128
00:03:32: 10.1.25.31:11001 <---> 10.1.25.234:23 congestion window changes
00:03:32: cwnd from 1460 to 1460, ssthresh from 2920 to 2920
00:03:32: tcp0: R SYNSENT 10.1.25.234:11001 10.1.25.31:23 seq 1922220018
OPTS 4 SYN WIN 4128
!Connection timed out; remote host not responding
```

The following is sample output from the show debugging command when user-group debugging is configured:

```text
Router# show debugging
!
usergroup:
Usergroup Deletions debugging is on
Usergroup Additions debugging is on
Usergroup Database debugging is on
Usergroup API debugging is on
```

! The following is sample output from the show debugging command when SNAP debugging is configured:

```text
Router# show debugging
```

Persistent variable debugging is currently All SNAP Server Debugging ON SNAP Client Debugging ON The table below describes the significant fields in the output.

| Field | Description |
| --- | --- |
| OPTS4 | BytesofTCPexpressedasanumber.Inthiscase,thebytesare4. |
| ECE | Echocongestionexperience. |
| CWR | Congestionwindowreduced. |

| Field | Description |
| --- | --- |
| SYN | Synchronizeconnections--Requesttosynchronizesequencenumbers,usedwhenaTCP connectionisbeingopened. |
| WIN4128 | Advertisedwindowsize,inbytes.Inthiscase,thebytesare4128. |
| cwnd | Congestionwindow(cwnd)--Indicatesthatthewindowsizehaschanged. |
| ssthresh | Slow-startthreshold(ssthresh)--VariableusedbyTCPtodeterminewhetherornottouse slow-startorcongestionavoidance. |
| usergroup | StaticallydefinedusergrouptowhichsourceIPaddressesareassociated. |


### `show declassify`

> **Página:** 613 · **Modo:** Global configuration · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the state of the declassify function (enabled, in progress, and so forth) and the sequence of declassification steps that will be performed, use the show declassify command in global configuration mode.

**Syntax:**

```text
show declassify
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords. Note The show declassify command is supported on the Cisco 3200 series routers only.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.3(8)YD | This command was introduced. |
| 12.4(2)T | This command was integrated into Cisco IOS Release12.4(2) T. |

**Example:**

The following example is sample output for the show declassify command:

```text
Router# show declassify
Declassify facility: Enabled=Yes In Progress=No
Erase flash=Yes Erase nvram=Yes
Obtain memory size
Shutdown Interfaces
Declassify Console and Aux Ports
Erase flash
Declassify NVRAM
Declassify Communications Processor Module
Declassify RAM, D-Cache, and I-Cache
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Enabled | A“Yes”valueindicatesthatzeroizationisenabled. A“No”valueindicatesthatzeroizationisdisabled. |
| InProgress | A“Yes”valueindicatesthatzeroizationiscurrentlyinprogress. A“No”valueindicatesthatzeroizationiscurrentlynotinprogress. |
| Eraseflash | A“Yes”valueindicatesthaterasureofFlashmemoryisenabled. A“No”valueindicatesthattheerasureofFlashmemoryisdisabled. |
| Erasenvram | A“Yes”valueindicatesthattheerasureofNVRAMisenabled. A“No”valueindicatesthattheerasureofNVRAMisdisabled. |
| Obtainmemorysize | Obtainthemainmemorysizeinordertounderstandhowmuchofthe memoryistobescrubbed. |
| ShutdownInterfaces | Shutdownanyandallnetworkinterfaces. |
| DeclassifyConsoleandAUXPorts | RemovepotentiallysensitiveinformationfromconsoleandAUXport FIFOs. |
| Eraseflash | EraseFlashmemory. |
| DeclassifyNVRAM | EraseNVRAM. |
| DeclassifyCommunications ProcessorModule | ErasethememoryintheCommunicationsProcessorModule(CPM). |
| DeclassifyRAM,D-Cache,and I-Cache | Scrubthemainmemory,erasetheDataCache(D-Cache),anderase theInstructionCache(I-Cache). |


### `show derived-config`

> **Página:** 614 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the composite results of all the configuration commands that apply to an interface, including commands that come from sources such as static templates, dynamic templates, dialer interfaces, and authentication, authorization, and accounting (AAA) per-user attributes, use the show derived-config command in privileged EXEC mode.

**Syntax:**

```text
show derived-config [interface type number]
```

**Parameters (Syntax Description):**

- `interface type number` — ( Optional) D is p l a y s the derived configuration for as p e c if i c interface. If you use the interface keyword, you must specify the interface type and the interface number( for example, interface e the r n e t0).

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.1 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 15.1(2)S | This command was modified. The output was e x t end e d to include information about service in s t an c e s and x c on n e c t s that are download e d and provision e d. |

**Usage Guidelines:**

Configuration commands can be applied to an interface from sources such as static templates, dynamic templates bound by resource pooling, dialer interfaces, AAA per-user attributes and the configuration of the physical interface. The show derived-config command displays all the commands that apply to an interface. The output for the show derived-configcommand is nearly identical to that of the show running-config command. It differs when the configuration for an interface is derived from a template, a dialer interface, or some per-user configuration. In those cases, the commands derived from the template, dialer interface, and so on, will be displayed for the affected interface. If the same command is configured differently in two different sources that apply to the same interface, the command coming from the source that has the highest precedence will appear in the display. On Performance Routing Version 3 (PfRv3) configured device, this command is used to display automatically configured components.

**Example:**

The following examples show sample output for the show running-config and show derived-config commands for serial interface 0:23 and dialer interface 0. The output of the show running-config and show derived-config commands is the same for dialer interface 0 because none of the commands that apply to that interface are derived from any sources other than the configuration of the dialer interface. The output for the show running-config and show derived-config commands for serial interface 0:23 differs because some of the commands that apply to serial interface 0:23 come from dialer interface 0.

```text
Router# show running-config interface Serial0:23
Building configuration...
Current configuration :296 bytes
!
interface Serial0:23
description PRI to ADTRAN (#4444150)
ip unnumbered Loopback0
encapsulation ppp
dialer rotary-group 0
isdn switch-type primary-dms100
isdn incoming-voice modem
isdn calling-number 4444150
peer default ip address pool old_pool
end
Router# show running-config interface Dialer0
Building configuration...
Current configuration :257 bytes
!
interface Dialer0
description Dialin Users
ip unnumbered Loopback0
no ip proxy-arp
encapsulation ppp
dialer in-band
dialer idle-timeout 30
dialer-group 1
peer default ip address pool new_pool
ppp authentication pap chap callin
end
Router# show derived-config interface Serial0:23
Building configuration...
Derived configuration :332 bytes
!
interface Serial0:23
description PRI to ADTRAN (#4444150)
ip unnumbered Loopback0
encapsulation ppp
dialer rotary-group 0
isdn switch-type primary-dms100
isdn incoming-voice modem
isdn calling-number 4444150
peer default ip address pool new_pool
ppp authentication pap chap callin
end
Router# show derived-config interface Dialer0
Building configuration...
Derived configuration :257 bytes
!
interface Dialer0
description Dialin Users
ip unnumbered Loopback0
no ip proxy-arp
encapsulation ppp
dialer in-band
dialer idle-timeout 30
dialer-group 1
peer default ip address pool new_pool
ppp authentication pap chap callin
end
```

The following sample output from the show running-config and show derived-config commands show service instance and xconnect configurations.

```text
Router# show running-config interface ethernet 0/0
Building configuration...
Current configuration : 201 bytes
!
interface Ethernet0/0
no ip address
service-policy type control mypolicy
service instance dynamic 1 ethernet
encapsulation dot1q 2-99
ethernet subscriber
initiator unclassified vlan
!
end
Router# show derived-config interface ethernet 0/0
Building configuration...
Derived configuration : 306 bytes
!
interface Ethernet0/0
no ip address
service-policy type control mypolicy
service instance dynamic 1 ethernet
encapsulation dot1q 2-99
ethernet subscriber
initiator unclassified vlan
!
service instance 2 ethernet
encapsulation dot1q 22
xconnect 33.33.33.34 12346 encapsulation mpls
!
end
```

This following is a sample output of the show derived-config | section eigrp command displaying that EIGRP SAF is automatically configured. Check the following fields in the output to ensure that the hub-master controller is configured accurately: • EIGRP SAF configuration is auto enabled • EIGRP SAF peering status between hub and branch sites

```text
HubMC#
show derived-config | section eigrp
------------------------------------------------------------------------------------------------------------------
router eigrp #AUTOCFG# (API-generated auto-configuration, not user configurable)
!
service-family ipv4 autonomous-system 59501
!
sf-interface Loopback0
hello-interval 120
hold-time 600
exit-sf-interface
!
topology base
exit-sf-topology
remote-neighbors source Loopback0 unicast-listen
exit-service-family
--------------------------------------------------------------------------------
```


### `show diagnostic cns`

> **Página:** 617 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the information about the CNS subject, use the show diagnostic cns command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show diagnostic cns {publish | subscribe}
```

**Parameters (Syntax Description):**

- `publish` — D is p l a y s the s u b j e c t with which the diagnostic r e s u l t s is p u b l is h e d.
- `s u b s c r i be` — D is p l a y s the s u b s c r i be d s u b j e c t s.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is not supported on Cisco 7600 series routers that are configured with a Supervisor Engine 2. The CNS subsystem communicates with remote network applications through the CNS-event agent and follows the publish and subscribe model. An application sets itself up to receive events by subscribing to the approprate event subject name.

**Example:**

This example shows how to display the subject with which the diagnostic results is published:

```text
show diagnostic cns publish
Subject: cisco.cns.device.diag_results
```

This example shows how to display the subscribed subject:

```text
Router# show diagnostic cns subscribe
Subject: cisco.cns.device.diag_get_results
```


### `show diagnostic sanity`

> **Página:** 618 · **Modo:** Privileged EXEC · **Default:** Displays information for all the Gigabit Ethernet WAN interfaces in the Cisco 7600 series router. · **Leitura (show/clear/…):** sim

**Description:** To display sanity check results, use the show diagnostic sanity command in privileged EXEC mode.

**Syntax:**

```text
show diagnostic sanity
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Displays information for all the Gigabit Ethernet WAN interfaces in the Cisco 7600 series router.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SXE | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The sanity check runs a set of predetermined checks on the configuration with a possible combination of certain system states to compile a list of warning conditions. The checks are designed to look for anything that seems out of place and are intended to serve as an aid to maintaining the system sanity. The following is a list of the checks that are run and the action taken when the condition is found: • Checks whether the default gateways are reachable. If so, the system stops pinging. • If a port auto-negotiates to half duplex, the system flags it. Trunking Checks • If a trunk port has the mode set to “on,” the system flags it. • If a port is trunking and mode is auto, the system flags it. • If a trunk port is not trunking and the mode is desirable, the system flags it. • If a trunk port negotiates to half duplex, the system flags it. Channeling Checks • If a port has channeling mode set to on, the system flags it. • If a port is not channeling and the mode is set to desirable, the system flags it. • If a VLAN has a Spanning-Tree root of 32K (root is not set), the system flags it. Spanning-Tree VLAN Checks • If a VLAN has a max age on the Spanning-Tree root that is different than the default, the system flags it. • If a VLAN has a fwd delay on the Spanning-Tree root that is different than the default, the system flags it. • If a VLAN has a fwd delay on the bridge that is different than the default, the system flags it. • If a VLAN has a fwd delay on the bridge that is different than the default, the system flags it. • If a VLAN has a hello time on the bridge that is different than the default, the system flags it. Spanning-Tree Port Checks • If a port has a port cost that is different than the default, the system flags it. • If a port has a port priority that is different than the default, the system flags it. UDLD Checks • If a port has UDLD disabled, the system flags it. • If a port had UDLD shutdown, the system flags it. • If a port had a UDLD undetermined state, the system flags it. Assorted Port Checks • If a port had receive flow control disabled, the system flags it. • If a trunk port had PortFast enabled, the system flags it. • If a inline power port has any of the following states: • denied • faulty • other • off The system flags it. • If a port has a native VLAN mismatch, the system flags it. • If a port has a duplex mismatch, the system flags it. Bootstring and Config Register Checks • The config register on the primary supervisor engine (and on the secondary supervisor engine if present) must be one of the following values: 0x2 , 0x102, or 0x2102. • The system verifies the bootstring on the primary supervisor engine (and on the secondary supervisor engine if present). The system displays a message if the bootstring is empty. • The system verifies that every file is specified in the bootstring. The system displays a message if the file is absent or shows up with a wrong checksum. If only device : is specified as a filename, then the system verifies that the first file is on the device. Assorted Checks • The system displays a message if IGMP snooping is disabled. • The system displays a message if any of the values of the snmp community access strings {RO,RW,RW-ALL} is the same as the default. • The system displays a message if any of the modules are in states other than “Ok.” • The system displays a message that lists all the tests that failed (displayed as an “F”) in the show test all command. • The system displays a message if *fast is not configured on the switch anywhere. • The system displays a message if there is enough room for the crashinfo file on the bootflash:. • The system displays a message if multicast routing is enabled globally but is not applied to all interfaces. • The system displays a message if IGMP snooping is disabled and RGMP is enabled.

**Example:**

This example displays samples of the messages that could be displayed with the show diagnostic sanity command:

```text
Router# show diagnostic sanity
Pinging default gateway 10.6.141.1 ....
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.6.141.1, timeout is 2 seconds:
..!!.
Success rate is 0 percent (0/5)
IGMP snooping disabled please enable it for optimum config.
IGMP snooping disabled but RGMP enabled on the following interfaces,
please enable IGMP for proper config :
Vlan1, Vlan2, GigabitEthernet1/1
Multicast routing is enabled globally but not enabled on the following
interfaces:
GigabitEthernet1/1, GigabitEthernet1/2
A programming algorithm mismatch was found on the device bootflash:
Formatting the device is recommended.
The bootflash: does not have enough free space to accomodate the crashinfo file.
Please check your confreg value : 0x0.
Please check your confreg value on standby: 0x0.
The boot string is empty. Please enter a valid boot string .
Could not verify boot image "disk0:" specified in the boot string on the
slave.
Invalid boot image "bootflash:asdasd" specified in the boot string on the
slave.
Please check your boot string on the slave.
UDLD has been disabled globally - port-level UDLD sanity checks are
being bypassed.
OR
[
The following ports have UDLD disabled. Please enable UDLD for optimum
config:
Fa9/45
The following ports have an unknown UDLD link state. Please enable UDLD
on both sides of the link:
Fa9/45
]
The following ports have portfast enabled:
Fa9/35, Fa9/45
The following ports have trunk mode set to on:
Fa4/1, Fa4/13
The following trunks have mode set to auto:
Fa4/2, Fa4/3
The following ports with mode set to desirable are not trunking:
Fa4/3, Fa4/4
The following trunk ports have negotiated to half-duplex:
Fa4/3, Fa4/4
The following ports are configured for channel mode on:
Fa4/1, Fa4/2, Fa4/3, Fa4/4
The following ports, not channeling are configured for channel mode
desirable:
Fa4/14
The following vlan(s) have a spanning tree root of 32768:
The following vlan(s) have max age on the spanning tree root different from
the default:
1-2
The following vlan(s) have forward delay on the spanning tree root different
from the default:
1-2
The following vlan(s) have hello time on the spanning tree root different
from the default:
1-2
The following vlan(s) have max age on the bridge different from the
default:
1-2
The following vlan(s) have fwd delay on the bridge different from the
default:
1-2
The following vlan(s) have hello time on the bridge different from the
default:
1-2
The following vlan(s) have a different port priority than the default
on the port FastEthernet4/1
1-2
The following ports have recieve flow control disabled:
Fa9/35, Fa9/45
The following inline power ports have power-deny/faulty status:
Gi7/1, Gi7/2
The following ports have negotiated to half-duplex:
Fa9/45
The following vlans have a duplex mismatch:
Fas 9/45
The following interafaces have a native vlan mismatch:
interface (native vlan - neighbor vlan)
Fas 9/45 (1 - 64)
The value for Community-Access on read-only operations for SNMP is the same
as default. Please verify that this is the best value from a security point
of view.
The value for Community-Access on write-only operations for SNMP is the same
as default. Please verify that this is the best value from a security point
of view.
The value for Community-Access on read-write operations for SNMP is the same
as default. Please verify that this is the best value from a security point
of view.
Please check the status of the following modules:
8,9
Module 2 had a MINOR_ERROR.
The Module 2 failed the following tests:
TestIngressSpan
The following ports from Module2 failed test1:
1,2,4,48
```


### `show disk`

> **Página:** 622 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display flash or file system information for a disk, use the show diskcommand in user or privileged EXEC mode. show {disk0 | disk1} [all | filesys]

**Parameters (Syntax Description):**

- `disk0` — S e l e c t s disk0 as the disk to d is p l a y information about.
- `disk1` — S e l e c t s disk1 as the disk to d is p l a y information about.
- `all` — ( Optional) Specifies that all flash information will be d is p l a y e d for these l e c t e d disk.
- `filesys` — ( Optional) Specifies that filesystem information will be d is p l a y e d for these l e c t e d disk.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2 | This command was introduced in are l e as e p r i or to Cisco IOS Release12.2. |
| 12.3(7)T | This command was e n h an c e d to d is p l a y information about the AT A ROMmon it or l i b r a r y ( monlib) file. |
| 12.2(25)S | This command was integrated into the Cisco IOS Release12.2(25) S. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The show disk command is supported only on platforms that have a disk file system. Note The name of the ATA monlib file may contain a platform name that does not match the platform that you are using. Different platforms may have a similar or the same name for their ATA monlib file.

**Example:**

The following example displays information about disk 0. The output is self-explanatory.

```text
Router# show disk0 all
-#- --length-- -----date/time------ path
1 19539160 Jan 27 2004 23:08:40 c7200-is-mz.123-5.7.PI3a
1011679232 bytes available (19546112 bytes used)
******** ATA Flash Card Geometry/Format Info ********
ATA CARD GEOMETRY
Manufacturer Name SMART ATA Flash Card
Model Number SMART ATA FLASH DISK
Serial Number 00000155000000704162
Firmware Revision V1.01
Number of Heads: 16
Number of Cylinders 1999
Sectors per Track 63
Sector Size 512
Total Sectors 2014992
ATA CARD FORMAT
Number of FAT Sectors 246
Sectors Per Cluster 32
Number of Clusters 62941
Number of Data Sectors 2014789
Base Root Sector 632
Base FAT Sector 140
Base Data Sector 664
ATA MONLIB INFO
Image Monlib size = 67256
Disk monlib size = 71680
Name = c7200-atafslib-m
Monlib Start sector = 2
Monlib End sector = 133
Monlib updated by = C7200-IS-M12.3(5.7)PI3a
Monlib version = 1
```


### `show disk0:`

> **Página:** 624 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display flash or file system information for a disk located in slot 0, use the show disk0:command in user EXEC or privileged EXEC mode. show disk0:[all | filesys]

**Parameters (Syntax Description):**

- `all` — ( Optional) The all keyword d is p l a y s c o m p l e t e information about flash memory, in c l u d in g information about the in d i v id u a l device s in flash memory and then a m e s and size s of all system image files s to r e d in flash memory, in c l u d in gt h o set h at are in v a l id.
- `filesys` — ( Optional) D is p l a y s the device information b lock, the status information, and the usage information.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | This command was introduced. |
| 12.2 | This command was in c or p or at e d into Cisco IOS Release12.2. |
| 12.3(7)T | This command was e n h an c e d to d is p l a y information about the AT A ROMmon it or l i b r a r y ( monlib) file. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The show disk0: command is supported only on platforms that have a disk file system located in slot 0. Use the show disk0: command to display details about the files in a particular ATA PCMCIA flash disk memory card. For more information regarding file systems and flash cards, access the PCMCIA Filesystem Compatibility Matrix and Filesystem Information document at the following URL: http://www.cisco.com/en/US/partner/products/hw/routers/ps341/products_tech_note09186a00800a7515.shtml Note The name of the ATA monlib file may contain a platform name that does not match the platform that you are using. Different platforms may have a similar name or the same name for their ATA monlib file.

**Example:**

The following examples show displays of information about the flash disks or file system information for a disk. The output is self-explanatory.

```text
c7200# show disk0:
-#- --length-- -----date/time------ path
1 29505176 Feb 27 2006 17:56:52 +00:00 c7200-jk9o3s-mz.124-6.T
2 32768 Feb 24 2006 13:30:30 +00:00 file1.log
34738176 bytes available (29540352 bytes used)
c7200# show disk0: all
-#- --length-- -----date/time------ path
1 29505176 Feb 27 2006 17:56:52 +00:00 c7200-jk9o3s-mz.124-6.T
2 32768 Feb 24 2006 13:30:30 +00:00 file1.log
34738176 bytes available (29540352 bytes used)
******** ATA Flash Card Geometry/Format Info ********
ATA CARD GEOMETRY
Number of Heads: 4
Number of Cylinders 984
Sectors per Cylinder 32
Sector Size 512
Total Sectors 125952
ATA CARD FORMAT
Number of FAT Sectors 62
Sectors Per Cluster 8
Number of Clusters 15693
Number of Data Sectors 125812
Base Root Sector 232
Base FAT Sector 108
Base Data Sector 264
ATA MONLIB INFO
Image Monlib size = 73048
Disk monlib size = 55296
Name = NA
Monlib end sector = NA
Monlib Start sector = NA
Monlib updated by = NA
Monlib version = NA
c7200# show disk0: filesys
******** ATA Flash Card Geometry/Format Info ********
ATA CARD GEOMETRY
Number of Heads: 4
Number of Cylinders 984
Sectors per Cylinder 32
Sector Size 512
Total Sectors 125952
ATA CARD FORMAT
Number of FAT Sectors 62
Sectors Per Cluster 8
Number of Clusters 15693
Number of Data Sectors 125812
Base Root Sector 232
Base FAT Sector 108
Base Data Sector 264
ATA MONLIB INFO
Image Monlib size = 73048
Disk monlib size = 55296
Name = NA
Monlib end sector = NA
Monlib Start sector = NA
Monlib updated by = NA
Monlib version = NA
```

This example shows how to update and display the time settings on a device using the show disk0 command.

```text
7206-1#
7206-1#sh disk0:
-#- --length-- -----date/time------ path
1 47495056 Aug 8 2009 02:04:06 -08:00 c7200-adventerprisek9-mz.124-24.6.PI11
j
2 29211500 Sep 11 2009 23:09:24 -08:00 c7200-p-mz.CSCsz11391-eagle_cnh
3 0 Aug 24 2009 02:03:40 -08:00 dtdlog
4 16089368 Sep 8 2009 08:53:58 -08:00 c7200-p-mz.CSCsz11391-v122_18_sxf_thro
ttle-test
419250176 bytes available (92807168 bytes used)
7206-1#conf t
Enter configuration commands, one per line. End with CNTL/Z.
7206-1(config)#
clock timezone UTC 0 0
7206-1(config)#
end
7206-1#
*Sep 12 07:13:56.447: %SYS-6-CLOCKUPDATE: System clock has been updated from 23:13:56 PST
Fri S
ep 11 2009 to 07:13:56 UTC Sat Sep 12 2009, configured from console by console.
7206-1#
7206-1#
7206-1#
*Sep 12 07:13:57.239: %SYS-5-CONFIG_I: Configured from console by console
7206-1#
7206-1#
7206-1#sh disk0
:
-#- --length-- -----date/time------ path
1 47495056 Aug 8 2009 10:04:06 +00:00 c7200-adventerprisek9-mz.124-24.6.PI11j
2 29211500 Sep 12 2009 07:09:24 +00:00 c7200-p-mz.CSCsz11391-eagle_cnh
3 0 Aug 24 2009 10:03:40 +00:00 dtdlog
4 16089368 Sep 8 2009 16:53:58 +00:00 c7200-p-mz.CSCsz11391-v122_18_sxf_throttle-test
419250176 bytes available (92807168 bytes used)
```


### `show disk1:`

> **Página:** 626 · **Modo:** User EXEC Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display flash or file system information for a disk located in slot 1, use the show disk1:command in user EXEC or privileged EXEC mode. show disk1:[all | filesys]

**Parameters (Syntax Description):**

- `all` — ( Optional) The all keyword d is p l a y s c o m p l e t e information about flash memory, in c l u d in g information about the in d i v id u a l device s in flash memory and then a m e s and size s of all system image files s to r e d in flash memory, in c l u d in gt h o set h at are in v a l id.
- `filesys` — ( Optional) D is p l a y s the device information b lock, the status information, and the usage information.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | This command was introduced. |
| 12.2 | This command was in c or p or at e d into Cisco IOS Release12.2. |
| 12.3(7)T | This command was e n h an c e d to d is p l a y information about the AT A ROMmon it or l i b r a r y ( monlib) file. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The show disk1: command is supported only on platforms that have a disk file system. Use the show disk01: command to display details about the files in a particular ATA PCMCIA flash disk memory card located in slot 1. For more information regarding file systems and flash cards, access the PCMCIA Filesystem Compatibility Matrix and Filesystem Information document at the following URL: http://www.cisco.com/en/US/partner/products/hw/routers/ps341/products_tech_note09186a00800a7515.shtml Note The name of the ATA monlib file may contain a platform name that does not match the platform that you are using. Different platforms may have a similar name or the same name for their ATA monlib file.

**Example:**

The following examples show displays of information about the flash disks or file system information for a disk. The output is self-explanatory.

```text
c7200# show disk1:
-#- --length-- -----date/time------ path
1 29505176 Feb 27 2006 17:56:52 +00:00 c7200-jk9o3s-mz.124-6.T
2 32768 Feb 24 2006 13:30:30 +00:00 file1.log
34738176 bytes available (29540352 bytes used)
c7200#
show disk1: all
-#- --length-- -----date/time------ path
1 29505176 Feb 27 2006 17:56:52 +00:00 c7200-jk9o3s-mz.124-6.T
2 32768 Feb 24 2006 13:30:30 +00:00 file1.log
34738176 bytes available (29540352 bytes used)
******** ATA Flash Card Geometry/Format Info ********
ATA CARD GEOMETRY
Number of Heads: 4
Number of Cylinders 984
Sectors per Cylinder 32
Sector Size 512
Total Sectors 125952
ATA CARD FORMAT
Number of FAT Sectors 62
Sectors Per Cluster 8
Number of Clusters 15693
Number of Data Sectors 125812
Base Root Sector 232
Base FAT Sector 108
Base Data Sector 264
ATA MONLIB INFO
Image Monlib size = 73048
Disk monlib size = 55296
Name = NA
Monlib end sector = NA
Monlib Start sector = NA
Monlib updated by = NA
Monlib version = NA
c7200# show disk1: filesys
******** ATA Flash Card Geometry/Format Info ********
ATA CARD GEOMETRY
Number of Heads: 4
Number of Cylinders 984
Sectors per Cylinder 32
Sector Size 512
Total Sectors 125952
ATA CARD FORMAT
Number of FAT Sectors 62
Sectors Per Cluster 8
Number of Clusters 15693
Number of Data Sectors 125812
Base Root Sector 232
Base FAT Sector 108
Base Data Sector 264
ATA MONLIB INFO
Image Monlib size = 73048
Disk monlib size = 55296
Name = NA
Monlib end sector = NA
Monlib Start sector = NA
Monlib updated by = NA
Monlib version = NA
```


### `show drops`

> **Página:** 628 · **Modo:** Privileged EXEC mode · **Default:** No default behaviour or values. · **Leitura (show/clear/…):** sim

**Description:** To display the packet drops information, use the show drops command.

**Syntax:**

```text
show drops { bqs | crypto| firewall| interface| ip-all| nat| punt| qfp| qos|history}
```

**Parameters (Syntax Description):**

- `bqs` — Shows information about BQS related drops.
- `crypto` — Specifies IPSEC related drops.
- `f i r e w all` — D is p l a y s F i r e w all related drops.
- `interface` — D is p l a y s Interface drop statistics.
- `ip-all` — Shows information about IP related drops.
- `nat` — Specifies NAT related drops.
- `punt` — Shows information about Punt path related drops.
- `qfp` — D is p l a y s QFP drop statistics.
- `qos` — D is p l a y s Qo S related drops.
- `history` — D is p l a y s History of drops.

**Command Default:** No default behaviour or values.

**Command Modes:** Privileged EXEC mode

**Usage Guidelines:**

Use the show drops command to view the packet drop informaKon. Example The following example shows the packet drops information.

```text
Router#show drops
------------------ show platform hardware qfp active statistics drop
detail ------------------
Last clearing of QFP drops statistics : never
--------------------------------------------------------------------
------------
ID Global Drop Stats Packets
Octets
--------------------------------------------------------------------
------------
2 BadUidbIdx 15
------------------ show platform hardware qfp active interface all
statistics drop_summary ------------------
```


### `show environment`

> **Página:** 629 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** If no options are specified, the default is all. · **Leitura (show/clear/…):** sim

**Description:** To display temperature, voltage, fan, and power supply information, use the show environmentcommand in user EXEC or privileged EXEC mode. | table | temperature | voltages] Cisco 7000 Series, Cisco 7200 Series, Cisco 7304, and Cisco 7500 Series Cisco ASR 1000 Series Cisco uBR10012 Routers /

**Syntax:**

```text
show environment commandshow environment [alarms | all | fans | hardware | last | leds | power-supply
show environment commandshow environment [all | last | table]
show environment {all | counters | history sensor | location sensor | sensor sensor | table sensor}
show environment [all | last | subslot slot subslot | table]
```

**Parameters (Syntax Description):**

- `alarms` — ( Optional) D is p l a y s the alarm c on t a c t information.
- `all` — ( Optional) D is p l a y s a detailed list in g of all environment a l monitor parameters( for example, the power sup p l i e s, temperature r e a d in g s, v o l t age r e a d in g s, and b low e r speed s). This is the default.
- `fans` — ( Optional) D is p l a y s b low e r and f an information.
- `hardware` — ( Optional) D is p l a y s hardware-s p e c if i c information.
- `last` — ( Optional) D is p l a y s information on the last meas u r e m e n t m a d e.
- `leds` — ( Optional) D is p l a y s the status of the MBus L E D s on the clock and scheduler card s and switch f a b r i c card s.
- `power-supply` — ( Optional) D is p l a y s power sup p l y v o l t age and current information. If ap p l i cable, d is p l a y s the status of the r e d u n d an t power sup p l y.
- `table` — ( Optional) D is p l a y s the temperature, v o l t age, and b low e r range s and threshold s. Onthe Cisco7200 s e r i e s, in c l u d in gt h e N P E-G2 in the Cisco7200 V X R, the Cisco7304 routers, and the Cisco7500 s e r i e s routers, the t a b l e keyword d is p l a y s only the temperature and v o l t age threshold s.
- `temperature` — ( Optional) D is p l a y s temperature information.
- `v o l t age s` — ( Optional) D is p l a y s v o l t age information.
- `counters` — D is p l a y s o p e r at i on a l counters.
- `history` — D is p l a y s s e n s or state c h an g e history.
- `location` — D is p l a y s s e n s or s by location.
- `sensor` — D is p l a y s s e n s or summary.
- `summary` — D is p l a y s as u m m a r y of all the environment monitor in g s e n s or s
- `sensor` — S e n s or name.
- `subslot` — ( Optional) D is p l a y s environment a l monitor parameters for as u b slot.
- `slot` — Slot number. V a l id values range from1 to8.
- `subslot` — S u b slot number. V a l id values are0 and1.

**Command Default:** If no options are specified, the default is all.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 11.2GS | The alarm s, f an s, hardware, l e d s, power-sup p l y, t a b l e, temperature, and v o l t age s keywords were added for the Cisco12000 s e r i e s GSRs. |
| 11.3(6)AA | This command was expand e d to monitor the R P S and b o a r d temperature for the Cisco AS5300 platform, Cisco3600 s e r i e s routers, Cisco7200 s e r i e s routers, andthe Cisco12000 s e r i e s GSRs. |
| 12.2(20)S | This command was integrated into Cisco IOS Release12.2(20) S. |
| 12.2(20)S2 | This command was integrated into Cisco IOS Release12.2(20) S2 to support MSCsand S P As on the Cisco7304 router using the all, last, and t a b l e keywords. |
| 12.4(4)XD | This command was integrated into Cisco IOS Release12.4(4) X D to support the N P E-G2 on the Cisco7200 V X R using the all, last, and t a b l e keywords. Command output was modified for the NPE-G2. |
| 12.2(31)SB2 | This command was integrated into Cisco IOS Release12.2(31) S B2. |
| CiscoIOSXERelease2.1 | This command was integrated into Cisco IOS X E Release2.1 on the Cisco ASR 1000 S e r i e s Routers. |
| 12.2(33)SCD2 | This command was integrated into Cisco IOS Release12.2(33) S CD2. The s u b l s o t keyword option and slot/ s u b l o t parameters were introduced. |
| CiscoIOSXErelease 17.14.1a | You use the show environment command to d is p l a y the Power Entry Module ( P E M) s e n s or r e a d in g s in m V( m i l l i v o l t) and m A( m i l l i a m p e r e) for your device s forthe Cisco ASR1000and Cisco Catalyst8500 s e r i e s routers. |

**Usage Guidelines:**

The availability of keywords depends on your system and platform. The command does not support SPAs on the Cisco 7200 series and on the NPE-G2 in the Cisco 7200 VXR routers. A routine runs once a minute that reads environmental measurements from sensors and stores the output into a buffer. For shared port adapters (SPAs), the temperature and voltage sensors are read every few seconds to get environmental data. The environmental buffer is displayed on the console when you use the show environment command. If a measurement exceeds desired margins, but has not exceeded fatal margins, a warning message is printed to the system console. The system software queries the sensors for measurements once a minute, but warnings for a given test point are printed at most once every hour for sensor readings in the warning range and once every 5 minutes for sensor readings in the critical range. If a measurement is out of line within these time segments, an automatic warning message appears on the console. As noted, you can query the environmental status with the show environment command at any time to determine whether a measurement is at the warning or critical tolerance. A SPA is shutdown when any of the SPA environment readings exceed the shutdown threshold. If a shutdown occurs because of detection of fatal environmental margins, the last measured value from each sensor is stored in internal nonvolatile memory. For environmental specifications, refer to the hardware installation and configuration publication for your individual chassis. For network processor engines (NPEs), network services engines (NSEs), line cards, and modular services cards (MSCs), environmental information is recorded in the CISCO-ENVMON-MIB. SPAs are not supported by the CISCO-ENVMON-MIB. In Cisco IOS Release 12.2(20)S2 and later, the CISCO-ENTITY-SENSOR-MIB supports environmental information for SPAs, as well as NPEs, NSEs, line cards, and MSCs. If the Cisco 12000 series GSR exceeds environmental conditions, a message similar to the following is displayed on the console:

```text
%GSR_ENV-2-WARNING: Slot 3 Hot Sensor Temperature exceeds 40 deg C;
Check cooling systems
```

Note Blower temperatures that exceed environmental conditions do not generate a warning message. You can also enable Simple Network Management Protocol (SNMP) notifications (traps or informs) to alert a network management system (NMS) when environmental thresholds are reached using the snmp-server enable traps envmon and snmp-server host global configuration commands. Whenever Cisco IOS software detects a failure or recovery event from the DRPS unit, it sends an SNMP trap to the configured SNMP server. Unlike console messages, only one SNMP trap is sent when the failure event is first detected. Another trap is sent when the recovery is detected. Cisco AS5300 DRPS software reuses the MIB attributes and traps defined in CISCO-ENVMON-MIB and CISCO-ACCESS-ENVMON-MIB. CISCO-ENVMON-MIB is supported by all Cisco routers with RPS units, and CISCO-ACCESS-ENVMON-MIB is supported by the Cisco 3600 series routers. A power supply trap defined in CISCO-ENVMON-MIB is sent when a failure is detected and when a failure recovery occurs for the following events: input voltage fail, DC output voltage fail, thermal fail, and multiple failure events. A fan failure trap defined in CISCO-ENVMON-MIB is sent when a fan failure or recovery event is detected by Cisco IOS software. A temperature trap defined in CISCO-ACCESS-ENVMON-MIB is sent when a board over-temperature condition is detected by Cisco IOS software. CISCO-ACCESS-ENVMON-MIB also defines an over-voltage trap. A similar trap is defined in CISCO-ENVMON-MIB, but it requires the ciscoEnvMonVoltageStatusValue in varbinds. This value indicates the current value of the voltage in the RPS. With Cisco AS5300 RPS units, the current voltage value is not sent to the motherboard. CISCO-ENVMON-MIB is extended to add a new enumerated value, internalRedundant(5), for MIB attribute ciscoEnvMonSupplySource. This is used to identify a RPS unit. The temperature history of the Cisco uBR-MC20X20V line card, used in Cisco uBR10012 universal broadband router, can be viewed using the show environment subslot command. The show environment subslot command displays the thermal and power status of the Cisco uBR-MC20X20V line card. The slot/subslot option of the show environment subslot command helps to identify the location of the line card.

**Example:**

Cisco ASR 1000 Series Routers In the following example, the show environment all command displays system temperature, voltage, fan, and power supply conditions. (It does not display environmental information for SPAs.) The State column in show environment all output should show “Normal” except for fans where it indicates fan speed. A fan speed of 65% is normal.

```text
Router# show environment all
Sensor List: Environmental Monitoring
Sensor Location State Reading
V1: VMA F0 Normal 1801 mV
V1: VMB F0 Normal 1206 mV
V1: VMC F0 Normal 1206 mV
V1: VMD F0 Normal 1103 mV
V1: VME F0 Normal 1005 mV
V1: 12v F0 Normal 11967 mV
V1: VDD F0 Normal 3295 mV
V1: GP1 F0 Normal 905 mV
V2: VMA F0 Normal 3295 mV
V2: VMB F0 Normal 2495 mV
V2: VMC F0 Normal 1499 mV
V2: VMD F0 Normal 1098 mV
V2: VME F0 Normal 1000 mV
V2: VMF F0 Normal 1000 mV
V2: 12v F0 Normal 11923 mV
V2: VDD F0 Normal 3295 mV
V2: GP1 F0 Normal 751 mV
Temp: Inlet F0 Normal 27 Celsius
Temp: Asic1 F0 Normal 44 Celsius
Temp: Exhaust1 F0 Normal 36 Celsius
Temp: Exhaust2 F0 Normal 34 Celsius
Temp: Asic2 F0 Normal 40 Celsius
V1: VMA 0 Normal 1103 mV
V1: VMB 0 Normal 1201 mV
V1: VMC 0 Normal 1503 mV
V1: VMD 0 Normal 1801 mV
V1: VME 0 Normal 2495 mV
V1: VMF 0 Normal 3295 mV
V1: 12v 0 Normal 11967 mV
V1: VDD 0 Normal 3295 mV
V1: GP1 0 Normal 751 mV
V1: GP2 0 Normal 903 mV
V2: VMB 0 Normal 1201 mV
V2: 12v 0 Normal 11967 mV
V2: VDD 0 Normal 3291 mV
V2: GP2 0 Normal 903 mV
Temp: Left 0 Normal 28 Celsius
Temp: Center 0 Normal 29 Celsius
Temp: Asic1 0 Normal 42 Celsius
Temp: Right 0 Normal 27 Celsius
V1: VMA 1 Normal 1103 mV
V1: VMB 1 Normal 1201 mV
V1: VMC 1 Normal 1503 mV
V1: VMD 1 Normal 1801 mV
V1: VME 1 Normal 2495 mV
V1: VMF 1 Normal 3295 mV
V1: 12v 1 Normal 11953 mV
V1: VDD 1 Normal 3291 mV
V1: GP1 1 Normal 754 mV
V1: GP2 1 Normal 903 mV
V2: VMB 1 Normal 1206 mV
V2: 12v 1 Normal 11967 mV
V2: VDD 1 Normal 3291 mV
V2: GP2 1 Normal 905 mV
Temp: Left 1 Normal 28 Celsius
Temp: Center 1 Normal 30 Celsius
Temp: Asic1 1 Normal 44 Celsius
Temp: Right 1 Normal 28 Celsius
PEM Iout P0 Normal 37 A
PEM Vout P0 Normal 12 V AC
PEM Vin P0 Normal 116 V AC
Temp: PEM P0 Normal 28 Celsius
Temp: FC P0 Fan Speed 65% 25 Celsius
Temp: FM P1 Normal 1 Celsius
Temp: FC P1 Fan Speed 65% 25 Celsius
V1: VMA R0 Normal 1118 mV
V1: VMB R0 Normal 3315 mV
V1: VMC R0 Normal 2519 mV
V1: VMD R0 Normal 1811 mV
V1: VME R0 Normal 1513 mV
V1: VMF R0 Normal 1220 mV
V1: 12v R0 Normal 12011 mV
V1: VDD R0 Normal 3300 mV
V1: GP1 R0 Normal 913 mV
V1: GP2 R0 Normal 1247 mV
Temp: CPU R0 Normal 29 Celsius
Temp: Outlet R0 Normal 30 Celsius
Temp: Inlet R0 Normal 25 Celsius
Temp: Asic1 R0 Normal 30 Celsius
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Sensor | Sensorname. |
| Location | Chassisslot. |
| State | Statedescription.Oneofthefollowingvalues: •Critical--Criticalalarmindicatingaservice-affectingcondition. •FanSpeed--Fanspeed(65%isnormal). •Major--Majoralarmindicatingimmediateactionisneeded. •Minor--Minoralarmindicatingwarningconditions. •Normal--Sensorreadingisinacceptablerange. •Shutdown--Ifautomaticshutdownisenabled,indicatesthattherouterwillshut down. |
| Reading | Voltageortemperaturedetectedbythesensor. |

Cisco 7000 Series Routers, Cisco 7200 Series Routers In the following example, the typical show environment display is shown when no warning conditions are in the system for the Cisco 7000 series and Cisco 7200 series routers. This information may vary slightly depending on the platform you are using. The date and time of the query are displayed, along with the data refresh information and a message indicating that there are no warning conditions.

```text
Router>
show environment
Environmental Statistics
Environmental status as of 13:17:39 UTC Thu Jun 6 1996
Data is 7 second(s) old, refresh in 53 second(s)
All Environmental Measurements are within specifications
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Environmentalstatusasof... | Currentdateandtime. |
| Datais...,refreshin... | Environmentalmeasurementsareoutputintoabufferevery60seconds,unless otherhigher-priorityprocessesarerunning. |
| Statusmessage | Ifenvironmentalmeasurementsarenotwithinspecification,warningmessages aredisplayed. |

NPE-G2 in Cisco 7200 VXR Routers In the following example, additional temperature and voltage readings for the NPE-G2 in the Cisco 7200 VXR router are displayed by the show environment all command. Power supplies 1 and 2 are on, and all monitored variables are within the normal operating range.

```text
Router_npe-g2# show environment all
Power Supplies:
Power Supply 1 is Zytek AC Power Supply. Unit is on.
Power Supply 2 is Zytek AC Power Supply. Unit is on.
Temperature readings:
NPE Inlet measured at 25C/77F
NPE Outlet measured at 28C/82F
CPU Die measured at 56C/132F =======> additional temperature reading on NPE-G2
Voltage readings:
+3.30 V measured at +3.32 V =======> additional voltage reading on NPE-G2
+1.50 V measured at +1.48 V =======> additional voltage reading on NPE-G2
+2.50 V measured at +2.46 V =======> additional voltage reading on NPE-G2
+1.80 V measured at +1.75 V =======> additional voltage reading on NPE-G2
+1.20 V measured at +1.17 V =======> additional voltage reading on NPE-G2
VDD_CPU measured at +1.28 V =======> additional voltage reading on NPE-G2
VDD_MEM measured at +2.50 V =======> additional voltage reading on NPE-G2
VTT measured at +1.25 V =======> additional voltage reading on NPE-G2
+3.45 V measured at +3.39 V
-11.95 measured at -11.93 V
+5.15 V measured at +4.96 V
+12.15 V measured at +12.18 V
Envm stats saved 0 time(s) since reload
```

| Field | Description |
| --- | --- |
| PowerSupplyxispresent. | Specifieswhethertheindicated(x)powersupplyslotispopulated.Ifa powersupplyslotispopulated,themanufacturernameandwhetheritis anACorDCpowersupplyisdisplayed. |
| Unitis... | Indicateswhetherthepowersupplystatusisonoroff. |

| Field | Description |
| --- | --- |
| Temperaturereadings | IndicatesthetemperatureofaircominginandgoingoutoftheNPEInlet, NPEOutlet,andCPUDieareas. |
| NPEInletmeasuredat25C/77F | Indicatesthatthetemperaturemeasurementsattheinletareaofthechassis is25C/77F,whichiswithinnormaloperatingrange.Systemshutdownfor NPEInletis80C/176F. |
| NPEOutletmeasuredat28C/82F | Indicatesthatthetemperaturemeasurementsattheoutletareaofthechassis is28C/82F,whichiswithinnormaloperatingrange.Systemshutdownfor NPEOutletis84C/183F. |
| CPUDiemeasuredat56C/132F | IndicatesthatthetemperaturemeasurementattheCPUDie(internalsilicon oftheCPU)areaofthechassisis56C/132F,whichiswithinnormal operatingrange.SystemshutdownforCPUDieis100C/212F. |
| Voltagereadings: +3.30Vmeasuredat+3.32V +1.50Vmeasuredat+1.48V | Systemvoltagemeasurementsthatindicatetheactualmeasuredvaluefor thespecifiedpowerrail,whichisnamedaftertheexpectedtargetvalue. Forexample,the+3.30Vrail,withanexpectedvalueof+3.30V,actually measuresat+3.32V.Thisiswithinthetargetrange. Forexample,the+1.50Vrail,withanexpectedvalueof+1.50V,actually measuresat+1.48V.Thisiswithinthetargetrange. |
| VDD_CPUmeasuredat+1.28V | Indicates+1.28VisthemeasuredvoltageoftheVDD_CPUpowerrail, whichiswithinnormaloperatingrange.Theexpectedvalueis1.3V. |
| VDD_MEMmeasuredat+2.50 V | Indicates+2.50VisthemeasuredvoltageoftheVDD_MEMpowerrail, whichiswithinnormaloperatingrange.Theexpectedvalueis2.5V. |
| VTTmeasuredat+1.25V | Indicates+1.25VisthemeasuredvoltageoftheVTTpowerrail,which iswithinnormaloperatingrange.Theexpectedvalueis1.25V. |

In the following example, the show environment last command displays the previously saved measurements (readings) from the last environmental reading before the router was shutdown. The command also displays the reason why the router was shutdown, which was “power supply shutdown” in this case.

```text
Router_npe-g2# show environment last
NPE Inlet previously measured at 26C/78F
NPE Outlet previously measured at 28C/82F
CPU Die previously measured at 56C/132F
+3.30 V previously measured at +3.32
+1.50 V previously measured at +1.48
+2.50 V previously measured at +2.46
+1.80 V previously measured at +1.75
+1.20 V previously measured at +1.17
VDD_CPU previously measured at +1.28
VDD_MEM previously measured at +2.50
VTT previously measured at +1.25
+3.45 V previously measured at +3.39
-11.95 previously measured at -11.93
+5.15 V previously measured at +4.96
+12.15 V previously measured at +12.18
last shutdown reason - power supply shutdown
```

| Field | Description |
| --- | --- |
| NPEInletpreviouslymeasuredat26C/78F | Thelastmeasuredtemperatureoftheinletairoftherouter priortoshutdown. |
| NPEOutletpreviouslymeasuredat28C/82F | Thelastmeasuredtemperatureoftheoutletairoftherouter priortoshutdown. |
| CPUDiepreviouslymeasuredat56C/132F | ThelastmeasuredtemperatureoftheCPUDiepriorto shutdown. |
| +3.30Vpreviouslymeasuredat+3.32 | Thelastmeasuredvoltageofthe3.30Vpowerrailpriorto shutdown. |
| VDD_CPUpreviouslymeasuredat+1.28 | ThelastmeasuredvoltageoftheVDD_CPUpowerrailprior toshutdown. |
| VDD_MEMpreviouslymeasuredat+2.50 | ThelastmeasuredvoltageoftheVDD_MEMpowerrailprior toshutdown. |
| VTTpreviouslymeasuredat+1.25 | ThelastmeasuredvoltageoftheVTTpowerrailpriorto shutdown. |
| lastshutdownreason | Indicatesthereasonfortheshutdown. |

In the following example, the show environment table command displays threshold levels in a table format of the environmental monitor parameters. It displays the high warning, high critical, and high shutdown temperature thresholds of the NPE inlet, NPE outlet, and CPU Die. It also displays the low and high critical voltage thresholds, and low and high shutdown voltage thresholds for the power rails on the NPE-G2 in the Cisco 7200 VXR. Note The low range temperatures, such as the LowShut, LowCrit, and LowWarn temperature thresholds, are not checked and are not displayed on the NPE-G2. Also the warning voltage thresholds, such as LowWarn and HighWarn, are not checked and are not displayed on the NPE-G2.

```text
Router_npe-g2# show environment table
Sample Point LowShut LowCrit LowWarn HighWarn HighCrit HighShut
NPE Inlet 44C/111F 59C/138F
NPE Outlet 49C/120F 64C/147F
CPU Die 75C/167F 85C/185F
System shutdown for NPE Inlet is 80C/176F
System shutdown for NPE Outlet is 84C/183F
System shutdown for CPU Die is 100C/212F
+3.30 V +2.30 +3.12 +3.47 +4.29
+1.50 V +1.05 +1.40 +1.56 +1.95
+2.50 V +1.71 +2.34 +2.61 +3.28
+1.80 V +1.25 +1.67 +1.91 +2.34
+1.20 V +0.82 +1.13 +1.28 +1.56
VDD_CPU +0.89 +1.21 +1.36 +1.71
VDD_MEM +1.71 +2.34 +2.61 +3.28
VTT +0.85 +1.17 +1.32 +1.64
+3.45 V +2.38 +3.28 +3.63 +4.49
-11.95 V -8.44 -11.56 -12.84 -15.78
+5.15 V +3.59 +4.88 +5.42 +6.71
+12.15 V +8.55 +11.48 +12.77 +15.82
```

| Field | Description |
| --- | --- |
| SamplePoint | Thisistheareaforwhichtemperatureorsystemvoltagethresholdsaredisplayed. |
| LowShut | ThisistheLowShutvoltagethreshold.IfthevoltagevalueisbelowtheLowShut threshold,theroutershutsdown. Note TheLowShuttemperaturevalueisnotcheckedanditsthresholdisnotdisplayed ontheNPE-G2. |
| LowCrit | Thisisthelowcriticalvoltagethreshold.IfthevoltagevalueisbelowtheLowCrit threshold,acriticalmessageisissuedforanout-of-tolerancevoltagevalue.The systemcontinuestooperate.However,thesystemisapproachingshutdown. Note TheLowCrittemperaturevalueisnotcheckedanditsthresholdisnotdisplayedon theNPE-G2. |
| LowWarn | TheLowWarntemperaturethresholdandLowWarnvoltagethresholdarenotchecked andthethresholdinformationisnotdisplayedontheNPE-G2. |
| HighWarn | ThisistheHighWarntemperaturethreshold.IfthetemperaturereachestheHighWarn threshold,awarningmessageisissuedforanout-of-tolerancetemperaturevalue. Thesystemcontinuestooperate,butoperatoractionisrecommendedtobringthe systembacktoanormalstate. Note TheHighWarnvoltagethresholdisnotcheckedanditsthresholdisnotdisplayed ontheNPE-G2. |
| HighCrit | ThisistheHighCrittemperatureorvoltagethreshold.Ifthetemperatureorvoltage reachestheHighCritlevel,acriticalmessageisissued.Thesystemcontinuesto operate.However,thesystemisapproachingshutdown. Note BewarethatifthetemperaturereachesorexceedstheHighShutvalue,aShutdown messageisissuedandtheroutershutsdown. |
| HighShut | ThisistheHighShuttemperatureorvoltagethreshold.Ifthetemperatureorvoltage levelreachesorexceedstheHighShutvalue,aShutdownmessageisissuedandthe routershutsdown. |

| Field | Description |
| --- | --- |
| NPEInlet44C/111F 59C/138F | ThesearetheHighWarnandHighCrittemperaturethresholds,respectively,forthe NPEInlet. IftheNPEInlettemperaturevaluereachestheHighWarn(44C/111F)andHighCrit (59C/138F)levels,warningandcriticalmessages,respectively,areissued. Ifthevaluereaches44C/111Forgreater,youreceiveawarningmessageindicating HighWarn.Thesystemcontinuestooperate,butoperatoractionisrecommended tobringthesystembacktoanormalstate. Ifthevaluereaches59C/138Forgreater,youreceiveacritical(HighCrit)message instead,thatindicatesthesystemcontinuestooperate,butthesystemisapproaching shutdown. Note Bewareifthetemperaturereachesorexceeds80C/176F,whichistheHighShut value,aShutdownmessageisissued,andtheNPEInletareashutsdown. |
| NPEOutlet49C/120F 64C/147F | ThesearetheHighWarnandHighCrittemperaturethresholds,respectively,forthe NPEOutlet. IftheNPEOutlettemperaturevaluereachestheHighWarn(49C/120F)andHighCrit (64C/147F)levels,warningandcriticalmessages,respectively,areissued. Ifthevaluereaches49C/120Forgreater,youreceiveawarningmessageindicating HighWarn.Thesystemcontinuestooperate,butoperatoractionisrecommended tobringthesystembacktoanormalstate. Ifthevaluereaches64C/147Forgreater,youreceiveacritical(HighCrit)message insteadthatindicatesthesystemcontinuestooperate,butthesystemisapproaching shutdown. Note Bewareifthetemperaturereachesorexceeds84C/183F,whichistheHighShut value,aShutdownmessageisissued,andtheNPEOutletareashutsdown. |
| CPUDie75C/167F 85C/185F | ThesearetheHighWarnandHighCrittemperaturethresholds,respectively,forthe CPUDie. IftheCPUDietemperaturevaluereachestheHighWarn(75C/167F)andHighCrit (85C/185F)levels,warningandcriticalmessages,respectively,areissued. Ifthevaluereaches75C/167Forgreater,youreceiveawarningmessageindicating HighWarn.Thesystemcontinuestooperate,butoperatoractionisrecommended tobringthesystembacktoanormalstate. Ifthevaluereaches85C/185Forgreater,youreceiveacritical(HighCrit)message instead,thatindicatesthesystemcontinuestooperate,butthesystemisapproaching shutdown. Note Bewareifthetemperaturereachesorexceeds100C/212F,whichistheHighShut value,aShutdownmessageisissuedandtheCPUDieareashutsdown. |

| Field | Description |
| --- | --- |
| Systemshutdownfor NPEInletis80C/176F | ThisistheHighShuttemperaturethresholdfortheNPEInlet. Ifthetemperaturereachesorexceeds80C/176F,aShutdownmessageisissuedand theNPEInletareaisshutdown. |
| Systemshutdownfor NPEOutletis 84C/183F | ThisistheHighShuttemperaturethresholdfortheNPEOutlet. Ifthetemperaturereachesorexceeds84C/183F,aShutdownmessageisissuedand theNPEOutletareaisshutdown. |
| Systemshutdownfor CPUDieis100C/212F | ThisistheHighShuttemperaturethresholdfortheCPUDie. Ifthetemperaturereachesorexceeds100C/212F,aShutdownmessageisissued andtheCPUDieareaisshutdown. |
| +3.30V+2.30+3.12 +3.47+4.29 | Thevoltagethresholdsforthe+3.30Vpowerrailareasfollows: •+2.30istheLowShutvoltagethreshold. •+3.12istheLowCritvoltagethreshold. •+3.47istheHighCritvoltagethreshold. •+4.29istheHighShutvoltagethreshold. Note TheLowWarnandHighWarnvoltagelevelsarenotcheckedandtheirthresholds arenotdisplayedontheNPE-G2. |
| VDD_CPU+0.89 +1.21+1.36+1.71 | ThevoltagethresholdsfortheVDD_CPUpowerrailareasfollows: •+0.89istheLowShutvoltagethreshold. •+1.21istheLowCritvoltagethreshold. •+1.36istheHighCritvoltagethreshold. •+1.71istheHighShutvoltagethreshold. Note TheLowWarnandHighWarnvoltagelevelsarenotcheckedandtheirthresholds arenotdisplayedontheNPE-G2. |
| VDD_MEM+1.71 +2.34+2.61+3.28 | ThevoltagethresholdsfortheVDD_MEMpowerrailareasfollows: •+1.71istheLowShutvoltagethreshold. •+2.34istheLowCritvoltagethreshold. •+2.61istheHighCritvoltagethreshold. •+3.28istheHighShutvoltagethreshold. Note TheLowWarnandHighWarnvoltagelevelsarenotcheckedandtheirthresholds arenotdisplayedontheNPE-G2. |

| Field | Description |
| --- | --- |
| VTT+0.85+1.17 +1.32+1.64 | ThevoltagethresholdsfortheVTTpowerrailareasfollows: •+0.85istheLowShutvoltagethreshold. •+1.17istheLowCritvoltagethreshold. •+1.32istheHighCritvoltagethreshold. •+1.64istheHighShutvoltagethreshold. Note TheLowWarnandHighWarnvoltagelevelsarenotcheckedandtheirthresholds arenotdisplayedontheNPE-G2. |

Cisco 7000 Series Routers The following are examples of messages that display on the system console when a measurement has exceeded an acceptable margin:

```text
ENVIRONMENTAL WARNING: Air flow appears marginal.
ENVIRONMENTAL WARNING: Internal temperature measured 41.3(C)
ENVIRONMENTAL WARNING: +5 volt testpoint measured 5.310(V)
```

The system displays the following message if voltage or temperature exceed maximum margins:

```text
SHUTDOWN: air flow problem
```

In the following example, there have been two intermittent power failures since a router was turned on, and the lower power supply is not functioning. The last intermittent power failure occurred on Monday, June 10, 1996, at 11:07 p.m.

```text
7000# show environment all
Environmental Statistics
Environmental status as of 23:19:47 UTC Wed Jun 12 1996
Data is 6 second(s) old, refresh in 54 second(s)
WARNING: Lower Power Supply is NON-OPERATIONAL
Lower Power Supply:700W, OFF Upper Power Supply: 700W, ON
Intermittent Powerfail(s): 2 Last on 23:07:05 UTC Mon Jun 10 1996
+12 volts measured at 12.05(V)
+5 volts measured at 4.96(V)
-12 volts measured at -12.05(V)
+24 volts measured at 23.80(V)
Airflow temperature measured at 38(C)
Inlet temperature measured at 25(C)
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Environmentalstatusasof... | Dateandtimeoflastquery. |

| Field | Description |
| --- | --- |
| Datais...,refreshin... | Environmentalmeasurementsareoutputintoabufferevery60seconds, unlessotherhigher-priorityprocessesarerunning. |
| WARNING: | Ifenvironmentalmeasurementsarenotwithinspecification,warningmessages aredisplayed. |
| LowerPowerSupply | Typeofpowersupplyinstalledanditsstatus(onoroff). |
| UpperPowerSupply | Typeofpowersupplyinstalledanditsstatus(onoroff). |
| IntermittentPowerfail(s) | Numberofpowerhits(notresultinginshutdown)sincethesystemwaslast booted. |
| Voltagespecifications | Systemvoltagemeasurements. |
| Airflowandinlettemperature | Temperatureofaircominginandgoingout. |

The following example is for the Cisco 7000 series routers. The router retrieves the environmental statistics at the time of the last shutdown. In this example, the last shutdown was Friday, May 19, 1995, at 12:40 p.m., so the environmental statistics at that time are displayed.

```text
Router# show environment last
Environmental Statistics
Environmental status as of 14:47:00 UTC Sun May 21 1995
Data is 6 second(s) old, refresh in 54 second(s)
WARNING: Upper Power Supply is NON-OPERATIONAL
LAST Environmental Statistics
Environmental status as of 12:40:00 UTC Fri May 19 1995
Lower Power Supply: 700W, ON Upper Power Supply: 700W, OFF
No Intermittent Powerfails
+12 volts measured at 12.05(V)
+5 volts measured at 4.98(V)
-12 volts measured at -12.00(V)
+24 volts measured at 23.80(V)
Airflow temperature measured at 30(C)
Inlet temperature measured at 23(C)
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Environmentalstatusasof... | Dateandtimeoflastquery. |
| Datais...,refreshin... | Environmentalmeasurementsareoutputintoabufferevery60seconds, unlessotherhigher-priorityprocessesarerunning. |
| WARNING: | Ifenvironmentalmeasurementsarenotwithinspecification,warning messagesaredisplayed. |
| LASTEnvironmentalStatistics | Displaystestpointvaluesattimeofthelastenvironmentalshutdown. |

| Field | Description |
| --- | --- |
| LowerPowerSupply UpperPowerSupply | FortheCisco7000router,indicatesthestatusofthetwo700Wpower supplies. FortheCisco7010router,indicatesthestatusofthesingle600Wpower supply. |

The following example shows sample output for the current environmental status in tables that list voltage and temperature parameters. There are three warning messages: one each about the lower power supply, the airflow temperature, and the inlet temperature. In this example, voltage parameters are shown to be in the normal range, airflow temperature is at a critical level, and inlet temperature is at the warning level.

```text
Router> show environment table
Environmental Statistics
Environmental status as of Mon 11-2-1992 17:43:36
Data is 52 second(s) old, refresh in 8 second(s)
WARNING: Lower Power Supply is NON-OPERATIONAL
WARNING: Airflow temperature has reached CRITICAL level at 73(C)
WARNING: Inlet temperature has reached WARNING level at 41(C)
Voltage Parameters:
SENSE CRITICAL NORMAL CRITICAL
-------|--------------------|------------------------|--------------------
+12(V) 10.20 12.05(V) 13.80
+5(V) 4.74 4.98(V) 5.26
-12(V) -10.20 -12.05(V) -13.80
+24(V) 20.00 24.00(V) 28.00
Temperature Parameters:
SENSE WARNING NORMAL WARNING CRITICAL SHUTDOWN
-------|-------------|------------|-------------|--------------|-----------
Airflow 10 60 70 73(C) 88
Inlet 10 39 41(C) 46 64
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| SENSE(VoltageParameters) | VoltagespecificationforaDCline. |
| SENSE(TemperatureParameters) | Airbeingmeasured.Inletmeasurestheaircomingin,andAirflow measuresthetemperatureoftheairinsidethechassis. |
| WARNING | Systemisapproachinganout-of-tolerancecondition. |
| NORMAL | Allmonitoredconditionsmeetnormalrequirements. |
| CRITICAL | Out-of-toleranceconditionexists. |
| SHUTDOWN | Processorhasdetectedconditionthatcouldcausephysicaldamageto thesystem. |

Cisco 7200 Series Routers The system displays the following message if the voltage or temperature enters the “Warning” range:

```text
%ENVM-4-ENVWARN: Chassis outlet 3 measured at 55C/131F
```

The system displays the following message if the voltage or temperature enters the “Critical” range:

```text
%ENVM-2-ENVCRIT: +3.45 V measured at +3.65 V
```

The system displays the following message if the voltage or temperature exceeds the maximum margins:

```text
%ENVM-0-SHUTDOWN: Environmental Monitor initiated shutdown
```

The following message is sent to the console if a power supply has been inserted or removed from the system. This message relates only to systems that have two power supplies.

```text
%ENVM-6-PSCHANGE: Power Supply 1 changed from Zytek AC Power Supply to removed
```

The following message is sent to the console if a power supply has been powered on or off. In the case of the power supply being shut off, this message can be due to the user shutting off the power supply or to a failed power supply. This message relates only to systems that have two power supplies.

```text
%ENVM-6-PSLEV: Power Supply 1 state changed from normal to shutdown
```

The following is sample output from the show environment all command on the Cisco 7200 series routers when there is a voltage warning condition in the system:

```text
7200#
show environment all
Power Supplies:
Power supply 1 is unknown. Unit is off.
Power supply 2 is Zytek AC Power Supply. Unit is on.
Temperature readings:
chassis inlet measured at 25C/77F
chassis outlet 1 measured at 29C/84F
chassis outlet 2 measured at 36C/96F
chassis outlet 3 measured at 44C/111F
Voltage readings:
+3.45 V measured at +3.83 V:Voltage in Warning range!
+5.15 V measured at +5.09 V
+12.15 measured at +12.42 V
-11.95 measured at -12.10 V
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| PowerSupplies | Currentconditionofthepowersuppliesincludingthetypeandwhetherthepower supplyisonoroff. |
| Temperaturereadings | Currentmeasurementsofthechassistemperatureattheinletandoutletlocations. |
| Voltagereadings | Currentmeasurementofthepowersupplytestpoints. |

The following example is for the Cisco 7200 series routers. This example shows the measurements immediately before the last shutdown and the reason for the last shutdown (if appropriate).

```text
7200# show environment last
chassis inlet previously measured at 27C/80F
chassis outlet 1 previously measured at 31C/87F
chassis outlet 2 previously measured at 37C/98F
chassis outlet 3 previously measured at 45C/113F
+3.3 V previously measured at 4.02
+5.0 V previously measured at 4.92
+12.0 V previously measured at 12.65
-12.0 V previously measured at 11.71
last shutdown reason - power supply shutdown
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| chassisinlet | Temperaturemeasurementsattheinletareaofthechassis. |
| chassisoutlet | Temperaturemeasurementsattheoutletareasofthechassis. |
| voltages | Powersupplytestpointmeasurements. |
| lastshutdownreason | Possibleshutdownreasonsarepowersupplyshutdown,criticaltemperature,and criticalvoltage. |

The following example is for the Cisco 7200 series routers. This information lists the temperature and voltage shutdown thresholds for each sensor.

```text
7200# s
how environment table
Sample Point LowCritical LowWarning HighWarning HighCritical
chassis inlet 40C/104F 50C/122F
chassis outlet 1 43C/109F 53C/127F
chassis outlet 2 75C/167F 75C/167F
chassis outlet 3 55C/131F 65C/149F
+3.45 V +2.76 +3.10 +3.80 +4.14
+5.15 V +4.10 +4.61 +5.67 +6.17
+12.15 V +9.72 +10.91 +13.37 +14.60
-11.95 V -8.37 -9.57 -14.34 -15.53
Shutdown system at 70C/158F
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| SamplePoint | Areaforwhichmeasurementsaretaken. |
| LowCritical | Levelatwhichacriticalmessageisissuedforanout-of-tolerancevoltagecondition. Thesystemcontinuestooperate;however,thesystemisapproachingshutdown. |

| Field | Description |
| --- | --- |
| LowWarning | Levelatwhichawarningmessageisissuedforanout-of-tolerancevoltagecondition. Thesystemcontinuestooperate,butoperatoractionisrecommendedtobringthe systembacktoanormalstate. |
| HighWarning | Levelatwhichawarningmessageisissued.Thesystemcontinuestooperate,but operatoractionisrecommendedtobringthesystembacktoanormalstate. |
| HighCritical | Levelatwhichacriticalmessageisissued.Forthechassis,therouterisshutdown. Forthepowersupply,thepowersupplyisshutdown. |
| Shutdownsystemat | Thesystemisshutdownifthespecifiedtemperatureismet. |

Cisco 7500 Series Routers The sample output for the Cisco 7500 series routers may vary depending on the specific model (for example, the Cisco 7513 router). The following is sample output from the show environment all command on the Cisco 7500 series routers:

```text
7500# show environment all
Arbiter type 1, backplane type 7513 (id 2)
Power supply #1 is 1200W AC (id 1), power supply #2 is removed (id 7)
Active fault conditions: none
Fan transfer point: 100%
Active trip points: Restart_Inhibit
15 of 15 soft shutdowns remaining before hard shutdown
Dbus slots: X XX X
card inlet hotpoint exhaust
RSP(6) 35C/95F 47C/116F 40C/104F
RSP(7) 35C/95F 43C/109F 39C/102F
Shutdown temperature source is ‘hotpoint’ on RSP(6), requested RSP(6)
+12V measured at 12.31
+5V measured at 5.21
-12V measured at -12.07
+24V measured at 22.08
+2.5 reference is 2.49
PS1 +5V Current measured at 59.61 A (capacity 200 A)
PS1 +12V Current measured at 5.08 A (capacity 35 A)
PS1 -12V Current measured at 0.42 A (capacity 3 A)
PS1 output is 378 W
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Arbitertype1 | Numbersindicatingthearbitertypeandbackplanetype. |
| Powersupply | Numberandtypeofpowersupplyinstalledinthechassis. |
| Activefaultconditions: | Listsanyfaultconditionsthatexist(suchaspowersupplyfailure,fanfailure, andtemperaturetoohigh). |

| Field | Description |
| --- | --- |
| Fantransferpoint: | Software-controlledfanspeed.Iftherouterisoperatingbelowitsautomatic restarttemperature,thetransferpointisreducedby10percentofthefull rangeeachminute.Iftherouterisatoraboveitsautomaticrestarttemperature, thetransferpointisincreasedinthesameway. |
| Activetrippoints: | Comparestemperaturesensoragainstthevaluesdisplayedatthebottomof theshowenvironment tablecommandoutput. |
| 15of15softshutdowns remaining | Whenthetemperatureincreasesabovethe“boardshutdown”level,asoft shutdownoccurs(thatis,thecardsareshutdown,andthepowersupplies, fans,andCIcontinuetooperate).Whenthesystemcoolstotherestartlevel, thesystemrestarts.Thesystemcountsthenumberoftimesthisoccursand keepstheup/downcyclefromcontinuingforever.Whenthecounterreaches zero,thesystemperformsahardshutdown,whichrequiresapowercycleto recover.Thesoftshutdowncounterisresettoitsmaximumvalueafterthe systemhasbeenupfor6hours. |
| Dbusslots: | Indicateswhichchassisslotsareoccupied. |
| card,inlet,hotpoint,exhaust | Temperaturemeasurementsattheinlet,hotpoint,andexhaustareasofthe card.The(6)and(7)indicatetheslotnumbers.DualRouteSwitchProcessor (RSP)chassiscanshowtwoRSPs. |
| Shutdowntemperaturesource | Indicateswhichofthethreetemperaturesourcesisselectedforcomparison againstthe“shutdown”levelslistedwiththeshowenvironment table command. |
| Voltages(+12V,+5V,-12V, +24V,+2.5) | Voltagesmeasuredonthebackplane. |
| PS1 | Currentmeasuredonthepowersupply. |

The following example is for the Cisco 7500 series routers. This example shows the measurements immediately before the last shutdown.

```text
7500# show environment last
RSP(4) Inlet previously measured at 37C/98F
RSP(4) Hotpoint previously measured at 46C/114F
RSP(4) Exhaust previously measured at 52C/125F
+12 Voltage previously measured at 12.26
+5 Voltage previously measured at 5.17
-12 Voltage previously measured at -12.03
+24 Voltage previously measured at 23.78
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| RSP(4)Inlet,Hotpoint,Exhaust | Temperaturemeasurementsattheinlet,hotpoint,andexhaustareasofthe card. |

| Field | Description |
| --- | --- |
| Voltages | Voltagesmeasuredonthebackplane. |

The following example is for the Cisco 7500 series router. This information lists the temperature and voltage thresholds for each sensor. These thresholds indicate when error messages occur. There are two level of messages: warning and critical.

```text
7500# show environment table
Sample Point LowCritical LowWarning HighWarning HighCritical
RSP(4) Inlet 44C/111F 50C/122F
RSP(4) Hotpoint 54C/129F 60C/140F
RSP(4) Exhaust
+12 Voltage 10.90 11.61 12.82 13.38
+5 Voltage 4.61 4.94 5.46 5.70
-12 Voltage -10.15 -10.76 -13.25 -13.86
+24 Voltage 20.38 21.51 26.42 27.65
2.5 Reference 2.43 2.51
Shutdown boards at 70C/158F
Shutdown power supplies at 76C/168F
Restart after shutdown below 40C/104F
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| SamplePoint | Areaforwhichmeasurementsaretaken. |
| LowCritical | Levelatwhichacriticalmessageisissuedforanout-of-tolerancevoltage condition.Thesystemcontinuestooperate;however,thesystemisapproaching shutdown. |
| LowWarning | Levelatwhichawarningmessageisissuedforanout-of-tolerancevoltage condition.Thesystemcontinuestooperate,butoperatoractionisrecommended tobringthesystembacktoanormalstate. |
| HighWarning | Levelatwhichawarningmessageisissued.Thesystemcontinuestooperate, butoperatoractionisrecommendedtobringthesystembacktoanormalstate. |
| HighCritical | Levelatwhichacriticalmessageisissued.Forthechassis,therouterisshut down.Forthepowersupply,thepowersupplyisshutdown. |
| Shutdownboardsat | Thecardisshutdownifthespecifiedtemperatureismet. |
| Shutdownpowersuppliesat | Thesystemisshutdownifthespecifiedtemperatureismet. |
| Restartaftershutdown | Thesystemwillrestartwhenthespecifiedtemperatureismet. |

Cisco AS5300 Series Access Servers In the following example, keywords and options are limited according to the physical characteristics of the system is shown:

```text
as5300# show environment ?
all All environmental monitor parameters
last Last environmental monitor parameters
table Temperature and voltage ranges
| Output modifiers
<cr>
as5300# show environment table
%This option not available on this platform
```

Cisco 12000 Series GSRs The following examples are for the Cisco 12000 series GSRs. The following is sample output from the show environment command for a Cisco 12012 router. Slots 0 through 11 are the line cards, slots 16 and 17 are the clock and scheduler cards, slots 18 through 20 are the switch fabric cards, slots 24 through 26 are the power supplies, and slots 28 and 29 are the blowers. An “NA” in the table means that no values were returned. In some cases it is because the equipment is not supported for that environmental parameter (for example, the power supply and blowers in slots 24, 26, 28, and 29 do not have a 3V power supply, so an NA is displayed).

```text
show environment
Slot # 3V 5V MBUS 5V Hot Sensor Inlet Sensor
(mv) (mv) (mv) (deg C) (deg C)
0 3300 4992 5040 42.0 37.0
2 3296 4976 5136 40.0 33.0
4 3280 4992 5120 38.5 31.5
7 3280 4984 5136 42.0 32.0
9 3292 4968 5160 39.5 31.5
11 3288 4992 5152 40.0 30.5
16 3308 NA 5056 42.5 38.0
17 3292 NA 5056 40.5 36.5
18 3304 NA 5176 36.5 35.0
19 3300 NA 5184 37.5 33.5
20 3304 NA 5168 36.5 34.0
24 NA 5536 5120 NA 31.5
26 NA 5544 5128 NA 31.5
28 NA NA 5128 NA NA
29 NA NA 5104 NA NA
Slot # 48V AMP_48
(Volt) (Amp)
24 46 12
26 46 19
Slot # Fan 0 Fan 1 Fan 2
(RPM) (RPM) (RPM)
28 2160 2190 2160
29 2130 2190 2070
```

The following table describes the significant fields shown and lists the equipment supported by each environmental parameter. “NA” indicates that the reading could not be obtained, so the command should be run again.

| Field | Description |
| --- | --- |
| Slot# | Slotnumberoftheequipment.OntheCisco12012router,slots0through11 arethelinecards,slots16and17aretheclockandschedulercards,slots18 through20aretheswitchfabriccards,slots24through27arethepowersupplies, andslots28and29aretheblowers. |
| 3V(mv) | Measuresthe3Vpowersupplyonthecard.The3Vpowersupplyisontheline cards,GRPcard,clockandschedulercards,andswitchfabriccards. |
| 5V(mv) | Measuresthe5Vpowersupplyonthecard.The5Vpowersupplyisontheline cards,GRPcard,andpowersupplies. |
| MBUS5V(mv) | Measuresthe5VMBusonthecard.The5VMBusisonallequipment. |
| HotSensor(degC) | Measuresthetemperatureatthehotsensoronthecard.Thehotsensorisonthe linecards,GRPcard,clockandschedulercards,switchfabriccards,andblowers. |
| InletSensor(degC) | Measuresthecurrentinlettemperatureonthecard.Theinletsensorisonthe linecards,GRPcard,clockandschedulercards,switchfabriccards,andpower supplies. |
| 48V(Volt) | MeasurestheDCpowersupplies. |
| AMP_48(Amp) | MeasurestheACpowersupplies. |
| Fan0,Fan1,Fan2(RPM) | Measuresthefanspeedinrotationsperminute. |

The following is sample output from the show environment all command for the Cisco 12008 router. Slots 0 through 7 are the line cards, slots 16 and 17 are the clock scheduler cards (the clock scheduler cards control the fans), slots 18 through 20 are the switch fabric cards, and slots 24 and 26 are the power supplies. The Cisco 12008 router does not support slots 25, 27, 28, and 29. An “NA” in the table means that no values were returned. In some cases it is because the equipment is not supported for that environmental parameter (for example, the power supplies in slots 24 and 26 do not have a hot sensor, so an NA is displayed).

```text
Router# show environment all
Slot # Hot Sensor Inlet Sensor
(deg C) (deg C)
2 31.0 22.0
5 33.5 26.5
16 25.5 21.5
18 22.0 21.0
19 22.5 21.0
24 NA 29.5
26 NA 24.5
Slot # 3V 5V MBUS 5V
(mv) (mv) (mv)
2 3292 5008 5136
5 3292 5000 5128
16 3272 NA 5128
18 3300 NA 5128
19 3316 NA 5128
Slot # 5V MBUS 5V 48V AMP_48
(mv) (mv) (Volt) (Amp)
24 0 5096 3 0
26 5544 5144 47 3
Slot # Fan Information
16 Voltage 16V Speed slow: Main Fans Ok Power Supply fans Ok
Alarm Indicators
No alarms
Slot # Card Specific Leds
16 Mbus OK SFCs Failed
18 Mbus OK
19 Mbus OK
24 Input Failed
26 Input Ok
```

The following is sample output from the show environment table command for a Cisco 12012 router. The show environment table command lists the warning, critical, and shutdown limits on your system and includes the GRP card and line cards (slots 0 to 15), clock and scheduler cards (slots 16 and 17), switch fabric cards (slots 18 to 20), and blowers.

```text
Router# show environment table
Hot Sensor Temperature Limits (deg C):
Warning Critical Shutdown
GRP/GLC (Slots 0-15) 40 46 57
CSC (Slots 16-17) 46 51 65
SFC (Slots 18-20) 41 46 60
Inlet Sensor Temperature Limits (deg C):
Warning Critical Shutdown
GRP/GLC (Slots 0-15) 35 40 52
CSC (Slots 16-17) 40 45 59
SFC (Slots 18-20) 37 42 54
3V Ranges (mv):
Warning Critical Shutdown
Below Above Below Above Below Above
GRP/GLC (Slots 0-15) 3200 3400 3100 3500 3050 3550
CSC (Slots 16-17) 3200 3400 3100 3500 3050 3550
SFC (Slots 18-20) 3200 3400 3100 3500 3050 3550
5V Ranges (mv):
Warning Critical Shutdown
Below Above Below Above Below Above
GRP/GLC (Slots 0-15) 4850 5150 4750 5250 4680 5320
MBUS_5V Ranges (mv):
Warning Critical Shutdown
Below Above Below Above Below Above
GRP/GLC (Slots 0-15) 5000 5250 4900 5350 4750 5450
CSC (Slots 16-17) 4820 5150 4720 5250 4750 5450
SFC (Slots 17-20) 5000 5250 4900 5350 4750 5450
Blower Operational Range (RPM):
Top Blower:
Warning Critical
Below Below
Fan 0 1000 750
Fan 1 1000 750
Fan 2 1000 750
Bottom Blower:
Warning Critical
Below Below
Fan 0 1000 750
Fan 1 1000 750
Fan 2 1000 750
```

The following is sample output from the show environment leds command for a Cisco 12012 router. The show environment leds command lists the status of the MBus LEDs on the clock, scheduler, and the switch fabric cards.

```text
Router# show environment leds
16 leds Mbus OK
18 leds Mbus OK
19 leds Mbus OK
20 leds Mbus OK
```

Cisco 7304 Router The following is sample output from the show environment allcommand on a Cisco 7304 router with modular services cards (MSCs) and shared port adapters (SPAs) installed:

```text
Router# show environment all
Power Supplies:
Power supply 1 is AC power supply. Unit is on.
Power supply 2 is empty.
Fans:
Fan 1 is on.
Fan 2 is on.
Temperature readings:
Active RP (NPEG100, slot 0):
npeg100 outlet measured at 29C/84F
npeg100 inlet measured at 34C/93F
npeg100 hotspot measured at 35C/95F
Line card (7304-MSC-100, slot 4):
7304-MSC-100 measured at 32C/89F
Card in subslot 4/0:
SPA-4FE-7304 inlet measured at 31C/87F
SPA-4FE-7304 outlet measured at 32C/89F
Voltage readings:
Active RP (NPEG100, slot 0):
npe outlet 2.5 V measured at 2.496 V
npe outlet 3.3 V measured at 3.302 V
npe outlet 5.0 V measured at 4.992 V
npe outlet 12.0 V measured at 11.812 V
npe outlet 3.3c V measured at 3.199 V
npe inlet 1.5 V measured at 1.494 V
npe outlet 1.8 V measured at 1.790 V
npe outlet 1.2 V measured at 1.198 V
npe outlet 1.2c V measured at 1.198 V
Line card (7304-MSC-100, slot 4):
7304-MSC-100 0.75 V measured at 0.733 V
7304-MSC-100 1.5 V measured at 1.494 V
7304-MSC-100 2.5 V measured at 2.483 V
7304-MSC-100 3.3 V measured at 3.250 V
7304-MSC-100 12 V measured at 11.937 V
Card in subslot 4/0:
SPA-4FE-7304 1.8V measured at 1.802 V
SPA-4FE-7304 1.5V measured at 1.503 V
SPA-4FE-7304 2.5V measured at 2.474 V
SPA-4FE-7304 3.3V measured at 3.252 V
SPA-4FE-7304 1.0V measured at 1.015 V
Envm stats saved 13 time(s) since reload
```

The following is sample output from the show environment lastcommand on a Cisco 7304 router with MSCs and SPAs installed and an NSE-100:

```text
show environment last
Temperature information:
NSE board:
nse outlet is unmeasured
nse inlet is unmeasured
nse hotspot is unmeasured
nse db is unmeasured
Line card slot 4:
7304-MSC-100 is unmeasured
Card in subslot 4/1:
SPA-4FE-7304 inlet previously measured at 30C/86F
SPA-4FE-7304 outlet previously measured at 32C/89F
Voltage information:
NSE board:
nse outlet 1.8 V is unmeasured
nse outlet 2.5 V is unmeasured
nse outlet 3.3 V is unmeasured
nse outlet 5 V is unmeasured
nse outlet 12 V is unmeasured
nse inlet 1.8 V is unmeasured
nse inlet 3.3 V is unmeasured
nse inlet 1.5 V is unmeasured
nse hotspot 1.8 V is unmeasured
nse db 1.65 V is unmeasured
nse db 1.8 V is unmeasured
Line card slot 4:
7304-MSC-100 0.75 V is unmeasured
7304-MSC-100 1.5 V is unmeasured
7304-MSC-100 2.5 V is unmeasured
7304-MSC-100 3.3 V is unmeasured
7304-MSC-100 12 V is unmeasured
Card in subslot 4/1:
SPA-4FE-7304 1.8V previously measured at 1.823 V
SPA-4FE-7304 1.5V previously measured at 1.512 V
SPA-4FE-7304 2.5V previously measured at 2.504 V
SPA-4FE-7304 3.3V previously measured at 3.258 V
SPA-4FE-7304 1.0V previously measured at 1.014 V
Last shutdown reason: shutdown undefined
```

The following is sample output from the show environment tablecommand on a Cisco 7304 router with MSCs and SPAs installed:

```text
Router# show environment table
Temperature tables:
Active RP (NPEG100, slot 0):
Sample Point HighWarning HighCritical HighShutdown
npeg100 outlet 53C/127F 68C/154F 73C/163F
npeg100 inlet 53C/127F 68C/154F 73C/163F
npeg100 hotspot 53C/127F 68C/154F 73C/163F
Line card (7304-MSC-100, slot 4):
Sample Point HighWarning HighCritical HighShutdown
7304-MSC-100 48C/118F 63C/145F 68C/154F
Card in subslot 4/0:
Sample Point HighWarning HighCritical HighShutdown
SPA-4FE-7304 inlet 52C/125F 67C/152F 72C/161F
SPA-4FE-7304 outlet 52C/125F 67C/152F 72C/161F
Voltage tables:
Active RP (NPEG100, slot 0):
Sample Point LowShut LowCrit LowWarn HighWarn HighCrit HighShut
npe outlet 2.5 V 2.275 V 2.375 V 2.400 V 2.600 V 2.625 V 2.725 V
npe outlet 3.3 V 3.003 V 3.135 V 3.185 V 3.415 V 3.465 V 3.597 V
npe outlet 5.0 V 4.500 V 4.750 V 4.800 V 5.200 V 5.250 V 5.500 V
npe outlet 12.0 V 9.960 V 10.440 V 10.800 V 13.200 V 13.560 V 14.040 V
npe outlet 3.3c V 3.003 V 3.135 V 3.185 V 3.415 V 3.465 V 3.597 V
npe inlet 1.5 V 1.350 V 1.425 V 1.455 V 1.545 V 1.575 V 1.650 V
npe outlet 1.8 V 1.620 V 1.710 V 1.728 V 1.872 V 1.890 V 1.980 V
npe outlet 1.2 V 1.128 V 1.164 V 1.167 V 1.233 V 1.236 V 1.272 V
npe outlet 1.2c V 1.128 V 1.164 V 1.167 V 1.233 V 1.236 V 1.272 V
Line card (7304-MSC-100, slot 4):
Sample Point LowShut LowCrit LowWarn HighWarn HighCrit HighShut
7304-MSC-100 0.75 0.559 V 0.600 V 0.600 V 0.900 V 0.900 V 0.941 V
7304-MSC-100 1.5 V 1.350 V 1.440 V 1.455 V 1.545 V 1.560 V 1.650 V
7304-MSC-100 2.5 V 2.250 V 2.375 V 2.400 V 2.600 V 2.625 V 2.750 V
7304-MSC-100 3.3 V 2.970 V 3.135 V 3.168 V 3.432 V 3.465 V 3.630 V
7304-MSC-100 12 V 9.960 V 10.440 V 10.800 V 13.200 V 13.560 V 14.040 V
Card in subslot 4/0:
Sample Point LowShut LowCrit LowWarn HighWarn HighCrit HighShut
SPA-4FE-7304 1.8V 1.620 V 1.710 V 1.728 V 1.872 V 1.890 V 1.980 V
SPA-4FE-7304 1.5V 1.350 V 1.425 V 1.440 V 1.560 V 1.575 V 1.650 V
SPA-4FE-7304 2.5V 2.250 V 2.375 V 2.400 V 2.600 V 2.625 V 2.750 V
SPA-4FE-7304 3.3V 2.970 V 3.135 V 3.168 V 3.432 V 3.465 V 3.630 V
SPA-4FE-7304 1.0V 0.900 V 0.950 V 0.960 V 1.040 V 1.050 V 1.100 V
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| SamplePoint | Areaforwhichmeasurementsaretaken. |
| LowShut | Lowestlevelforanout-of-toleranceconditionatwhichthesystemshutsitself down.Forout-of-toleranceconditionswithSPAenvironmentvariables,onlythe SPAisshutdown. |
| LowCrit/LowCritical | Levelatwhichacriticalmessageisissuedforanout-of-tolerancevoltage condition.Thesystemcontinuestooperate;however,thesystemisapproaching shutdown. |
| LowWarn/LowWarning | Levelatwhichawarningmessageisissuedforanout-of-tolerancevoltage condition.Thesystemcontinuestooperate,butoperatoractionisrecommended tobringthesystembacktoanormalstate. |
| HighWarn/HighWarning | Levelatwhichawarningmessageisissuedforanout-of-tolerancevoltage condition.Thesystemcontinuestooperate,butoperatoractionisrecommended tobringthesystembacktoanormalstate. |
| HighCrit/HighCritical | Levelatwhichacriticalmessageisissuedforanout-of-tolerancevoltage condition.Thesystemcontinuestooperate;however,thesystemisapproaching shutdown. |
| HighShut/HighShutdown | Highestlevelforanout-of-toleranceconditionatwhichthesystemshutsitself down.Forout-of-toleranceconditionswithSPAenvironmentvariables,onlythe SPAisshutdown. |

Cisco uBR10012 Router The following is sample output from the show environment subslot slot/subslotcommand on a Cisco uBR10012 router:

```text
show environment subslot 7/0
------------------------------------------------------------------------
TEMPERATURE/POWER INFORMATION
------------------------------------------------------------------------
Number of Temperature Sensors : 11
Sampling frequency : 2 minutes
------------------------------------------------------------------------
Sensor | ID | Current | Minor | Major | Critical | Alarm |
| | Temperature | Threshold | Condition |
| | 0C | 0C | |
------------------------------------------------------------------------
Nickel 10G 1 48 82 87 92 Normal
Inlet #1 2 36 68 73 78 Normal
CPU 3 44 73 78 83 Normal
Remora 4 48 82 87 92 Normal
Coldplay 5 40 75 80 85 Normal
Waxbill 6 53 92 97 102 Normal
Fauna 7 46 82 87 92 Normal
Flora 8 47 80 85 90 Normal
Toucan FPGA A 9 45 94 97 100 Normal
Toucan FPGA B 10 36 94 97 100 Normal
Toucan FPGA C 11 47 94 97 100 Normal
------------------------------------------------------------------------
Power: 168.813 watts
------------------------------------------------------------------------
-------------------------------------------------------------------------------------------
Time Stamp | Power | Sensor Temperature 0C
MM/DD/YYYY HH:MM:SS | watts | 1 2 3 4 5 6 7 8 9 10 11
-------------------------------------------------------------------------------------------
09/30/2009 10:24:26 168.813 48 36 44 48 40 53 46 47 45 36 47
09/30/2009 10:22:26 168.813 48 36 44 48 40 53 46 47 45 36 47
09/30/2009 10:20:26 168.813 48 36 44 47 40 53 46 47 45 36 47
09/30/2009 10:18:26 168.813 48 36 44 47 40 53 46 47 45 36 47
09/30/2009 10:16:26 168.813 47 36 44 47 40 53 46 47 45 36 47
09/30/2009 10:14:26 168.813 47 36 44 47 40 53 46 47 45 36 47
09/30/2009 10:12:26 168.813 47 36 44 46 40 52 45 47 45 36 47
09/30/2009 10:10:26 168.813 47 35 44 45 39 51 45 47 45 36 47
09/30/2009 10:08:26 168.132 46 35 44 43 38 50 43 47 45 36 47
-------------------------------------------------------------------------------------------
```

The following table describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| NumberofTemperatureSensors | Thenumberoftemperaturesensorsforwhichmeasurementsaretaken. |
| Samplingfrequency | Temperaturesamplingfrequency. |
| Sensor | Sensorname. |
| ID | Temperaturesensoridentifier. |

| Field | Description |
| --- | --- |
| CurrentTemperature | Currenttemperaturelevel. |
| Minor | Minortemperaturetolerancethresholdlevel. |
| MajorThreshold | Majortemperaturetolerancethresholdlevel. |
| Critical | Criticaltemperaturetolerancethresholdlevel. |
| TimeStamp | Temperaturelevelsamplingtime. |
| AlarmCondition | Alarmstate. |
| PowerWatts | Currentpowerconsumptionoftherouter. |
| Sensor | Temperaturesensoridentifier. |
| Temperature | Temperaturelevelforeachsensoratvariousperiods. |


### `show environment alarm`

> **Página:** 656 · **Modo:** User EXEC Privileged EXEC · **Default:** If you do not enter a frutype, all the information about the environmental alarm status is displayed. · **Leitura (show/clear/…):** sim

**Description:** To display the information about the environmental alarm, use the show environment alarm command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show environment alarm [ {status | threshold} [frutype]]
```

**Parameters (Syntax Description):**

- `status` — ( Optional) D is p l a y s the o p e r at i on a l F R U status.
- `threshold` — ( Optional) D is p l a y s the p r e p r o g r a m m e d alarm threshold s.
- `frutype` — ( Optional) Alarm type; v a l id values are all, b a c k plane, clock number, e a r l slot, f an-t r a y, module slot, r p slot, power-sup p l y number, supervisor slot, and v t t number. Seethe Notefor a list of v a l id values for number and slot.

**Command Default:** If you do not enter a frutype, all the information about the environmental alarm status is displayed.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Valid values for the frutype are as follows: • clock number --1 and 2. • earl slot -- See the Note for valid values. • module slot -- See the Note for valid values. • rp slot -- See the Note for valid values. • power-supply number --1 and 2. • supervisor slot -- See the Note for valid values. • vtt number --1 to 3. Note The slotargument designates the module and port number. Valid values for slot depend on the chassis and module that are used. For example, if you have a 48-port 10/100BASE-T Ethernet module that is installed in a 13-slot chassis, valid values for the slot number are from 1 to 13 and valid values for the port number are from 1 to 48.

**Example:**

This example shows how to display all the information about the status of the environmental alarm:

```text
Router>
show environment alarm
threshold
environmental alarm thresholds:
power-supply 1 fan-fail: OK
threshold #1 for power-supply 1 fan-fail:
(sensor value != 0) is system minor alarm
power-supply 1 power-output-fail: OK
threshold #1 for power-supply 1 power-output-fail:
(sensor value != 0) is system minor alarm
fantray fan operation sensor: OK
threshold #1 for fantray fan operation sensor:
(sensor value != 0) is system minor alarm
operating clock count: 2
threshold #1 for operating clock count:
(sensor value < 2) is system minor alarm
threshold #2 for operating clock count:
(sensor value < 1) is system major alarm
operating VTT count: 3
threshold #1 for operating VTT count:
(sensor value < 3) is system minor alarm
threshold #2 for operating VTT count:
(sensor value < 2) is system major alarm
VTT 1 OK: OK
threshold #1 for VTT 1 OK:
(sensor value != 0) is system minor alarm
VTT 2 OK: OK
threshold #1 for VTT 2 OK:
(sensor value != 0) is system minor alarm
VTT 3 OK: OK
threshold #1 for VTT 3 OK:
(sensor value != 0) is system minor alarm
clock 1 OK: OK
threshold #1 for clock 1 OK:
(sensor value != 0) is system minor alarm
clock 2 OK: OK
threshold #1 for clock 2 OK:
(sensor value != 0) is system minor alarm
module 1 power-output-fail: OK
threshold #1 for module 1 power-output-fail:
(sensor value != 0) is system major alarm
module 1 outlet temperature: 21C
threshold #1 for module 1 outlet temperature:
(sensor value > 60) is system minor alarm
threshold #2 for module 1 outlet temperature:
(sensor value > 70) is system major alarm
module 1 inlet temperature: 25C
threshold #1 for module 1 inlet temperature:
(sensor value > 60) is system minor alarm
threshold #2 for module 1 inlet temperature:
(sensor value > 70) is system major alarm
module 1 device-1 temperature: 30C
threshold #1 for module 1 device-1 temperature:
(sensor value > 60) is system minor alarm
threshold #2 for module 1 device-1 temperature:
(sensor value > 70) is system major alarm
module 1 device-2 temperature: 29C
threshold #1 for module 1 device-2 temperature:
(sensor value > 60) is system minor alarm
threshold #2 for module 1 device-2 temperature:
(sensor value > 70) is system major alarm
module 5 power-output-fail: OK
threshold #1 for module 5 power-output-fail:
(sensor value != 0) is system major alarm
module 5 outlet temperature: 26C
threshold #1 for module 5 outlet temperature:
(sensor value > 60) is system minor alarm
threshold #2 for module 5 outlet temperature:
(sensor value > 75) is system major alarm
module 5 inlet temperature: 23C
threshold #1 for module 5 inlet temperature:
(sensor value > 50) is system minor alarm
threshold #2 for module 5 inlet temperature:
(sensor value > 65) is system major alarm
EARL 1 outlet temperature: N/O
threshold #1 for EARL 1 outlet temperature:
(sensor value > 60) is system minor alarm
threshold #2 for EARL 1 outlet temperature:
(sensor value > 75) is system major alarm
EARL 1 inlet temperature: N/O
threshold #1 for EARL 1 inlet temperature:
(sensor value > 50) is system minor alarm
threshold #2 for EARL 1 inlet temperature:
(sensor value > 65) is system major alarm
Router>
```


### `show environment connector`

> **Página:** 659 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the connector rating and power consumption of modules or the backplane, use the show environment connector command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show environment connector [all | backplane | module number]
```

**Parameters (Syntax Description):**

- `all` — ( Optional) D is p l a y s the connector r at in g of the b a c k plane and the connector r at in g and power c on s u m p t i on of all module s.
- `b a c k plane` — ( Optional) D is p l a y s the connector r at in g of the b a c k plane.
- `module number` — ( Optional) D is p l a y s the connector r at in g and power c on s u m p t i on of the specified module.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(33)SXI4 | This command was introduced. |

**Usage Guidelines:**

The output of the show environment connector command displays the connector rating of the backplane (chassis) power connector, the connector rating of module connectors, and the power consumption of each installed module. If your system contains the necessary components for auxiliary power, the auxiliary power connector rating is displayed. If an installed module contains a voice daughterboard (VDB), the VDB connector rating is displayed. If you enter the show environment connector command with no keywords, the information for the backplane and all modules is displayed.

**Example:**

This example shows how to display the connector rating and power consumption of the backplane and all modules:

```text
Router>
show environment connector all
chassis connector rating: 1302.00 Watts (31.00 Amps @ 42V)
chassis auxiliary connector rating: 2016.00 Watts (48.00 Amps @ 42V)
module 3
module 3 connector rating: 1260.00 Watts (30.00 Amps @ 42V)
module 3 vdb connector rating: 1050.00 Watts (25.00 Amps @ 42V)
module 3 power consumption: 140.70 Watts ( 3.35 Amps @ 42V)
module 6
module 6 connector rating: 1260.00 Watts (30.00 Amps @ 42V)
module 6 power consumption: 282.24 Watts ( 6.72 Amps @ 42V)
module 9
module 9 connector rating: 1260.00 Watts (30.00 Amps @ 42V)
module 9 auxiliary connector rating: 2016.00 Watts (48.00 Amps @ 42V)
module 9 vdb connector rating: 1060.00 Watts (25.24 Amps @ 42V)
module 9 vdb auxiliary rating: 530.00 Watts (12.62 Amps @ 42V)
module 9 power consumption: 112.56 Watts ( 2.68 Amps @ 42V)
```

This example shows how to display the connector rating of the backplane:

```text
Router>
show environment connector backplane
chassis connector rating: 1302.00 Watts (31.00 Amps @ 42V)
chassis auxiliary connector rating: 2016.00 Watts (48.00 Amps @ 42V)
```


### `show environment cooling`

> **Página:** 660 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the information about the cooling parameter, use the show environment cooling command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show environment cooling
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is not supported in Cisco 7600 series routers that are configured with a Supervisor Engine 2.

**Example:**

This example shows how to display the information about the cooling parameter:

```text
Router> show environment cooling
fan-tray 1:
fan-tray 1 fan-fail: failed
fan-tray 2:
fan 2 type: FAN-MOD-9
fan-tray 2 fan-fail: OK
chassis cooling capacity: 690 cfm
ambient temperature: 55C
chassis per slot cooling capacity: 75 cfm
module 1 cooling requirement: 70 cfm
module 2 cooling requirement: 70 cfm
module 5 cooling requirement: 30 cfm
module 6 cooling requirement: 70 cfm
module 8 cooling requirement: 70 cfm
module 9 cooling requirement: 30 cfm
Router>
```


### `show environment status`

> **Página:** 661 · **Modo:** User EXEC Privileged EXEC · **Default:** If you do not enter a frutype, all FRU status information is displayed. · **Leitura (show/clear/…):** sim

**Description:** To display the information about the operational FRU status, use the show environment status command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show environment status [frutype]
```

**Parameters (Syntax Description):**

- `frutype` — ( Optional) F R U type; see the Note for a list of v a l id values.

**Command Default:** If you do not enter a frutype, all FRU status information is displayed.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(18)SXF | The output of the show environment status power-sup p l y command was changed to include information about the h i g h-capacity power sup p l i e s. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Valid values for the frutype are as follows: • all --No arguments. • backplane --No arguments. • clock number --1 and 2. • earl slot -- See the Note for valid values. • fan-tray --No arguments. • module slot -- See the Note for valid values. • power-supply number --1 and 2. • rp slot -- See the Note for valid values. • supervisor slot -- See the Note for valid values. • vtt number --1 to 3. Note The slotargument designates the module and port number. Valid values for slot depend on the chassis and module that are used. For example, if you have a 48-port 10/100BASE-T Ethernet module that is installed in a 13-slot chassis, valid values for the slot number are from 1 to 13 and valid values for the port number are from 1 to 48.

**Example:**

This example shows how to display the information about the environmental status:

```text
Router>
show environment status
backplane:
operating clock count: 2
operating VTT count: 3
fan-tray:
fantray fan operation sensor: OK
VTT 1:
VTT 1 OK: OK
VTT 2:
VTT 2 OK: OK
VTT 3:
VTT 3 OK: OK
clock 1:
clock 1 OK: OK, clock 1 clock-inuse: not-in-use
clock 2:
clock 2 OK: OK, clock 2 clock-inuse: in-use
power-supply 1:
power-supply 1 fan-fail: OK
power-supply 1 power-output-fail: OK
module 1:
module 1 power-output-fail: OK
module 1 outlet temperature: 21C
module 1 inlet temperature: 25C
module 1 device-1 temperature: 30C
module 1 device-2 temperature: 29C
EARL 1 outlet temperature: N/O
EARL 1 inlet temperature: N/O
module 5:
module 5 power-output-fail: OK
module 5 outlet temperature: 26C
module 5 inlet temperature: 23C
module 5 device-1 temperature: 26C
module 5 device-2 temperature: 27C
Router>
```

This example shows how to display the information about the high-capacity power supplies:

```text
Route># show environment status
power-supply 2
power-supply 2:
power-supply 2 fan-fail: OK
power-supply 2 power-input 1: none
power-supply 2 power-input 2: AC low
power-supply 2 power-input 3: AC high
power-supply 2 power-input 4: AC high
power-supply 2 power-output: low (mode 1)
power-supply 2 power-output-fail: OK
```

The table below describes the fields that are shown in the example. s howenvironmentstatus

| Field | Description |
| --- | --- |
| operatingclockcount | Physicalclockcount. |
| operatingVTTcount | PhysicalVTTcount. |
| fantrayfanoperationsensor | Systemfantrayfailurestatus.Thefailureofthesystemfantrayis indicatedasaminoralarm. |
| VTT1,VTT2,andVTT3 | Statusofthechassisbackplanepowermonitorsthatarelocatedonthe rearofthechassis,undertherearcover.OperationofatleasttwoVTTs isrequiredforthesystemtofunctionproperly.Aminorsystemalarm issignaledwhenoneofthethreeVTTsfails.Amajoralarmissignaled whentwoormoreVTTsfailandthesupervisorengineisaccessible throughtheconsoleport. |
| clock#clock-inuse | Clockstatus.Failureofeitherclockisconsideredtobeaminoralarm. |
| power-supply#fan-fail | Fanfailure.Fanfailuresoneitherorboth(ifany)powersuppliesare consideredminoralarms. |
| power-input-fail | Powerinputfailurestatus(none,AChigh,AClow). |
| power-output-fail | Poweroutputfailurestatus(high,low). |
| outlettemperature | Exhausttemperaturevalue. |
| inlettemperature | Intaketemperaturevalue. |
| device-1anddevice-2temperature | Twodevicesthatmeasuretheinternaltemperatureoneachindicated module.Thetemperatureshownindicatesthetemperaturethatthedevice isrecording.Thedevicesarenotplacedataninletoranexitbutare additionalreferencepoints. |


### `show environment temperature`

> **Página:** 663 · **Modo:** User EXEC Privileged EXEC · **Default:** If you do not enter a frutype, the module and EARL temperature readings are displayed. · **Leitura (show/clear/…):** sim

**Description:** To display the current temperature readings, use the show environment temperature command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show environment temperature [frutype]
```

**Parameters (Syntax Description):**

- `frutype` — ( Optional) F i e l d replace a b l e u n it( F R U) type; see the“ Usage Guidelines” section for a list of v a l id values.

**Command Default:** If you do not enter a frutype, the module and EARL temperature readings are displayed.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17a)SX | The show environment temperature module command output was u p d at e d to include the following information: • Then a m e of the AS I C of this s e n s or. • Then a m e s of the AS I C are list e d if the r e is more than one ASIC. • The type of s e n s or is list e d if the r e is more than one s e n s or on the ASIC. • Current temperature. • M a j or/ min or threshold as r e a d in the IDPROM. • Status of whether the current temperature has e x c e e d e d any temperature threshold s. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Valid values for the frutype are as follows: • earl slot -- See the Note below for valid values. • module slot -- See the Note below for valid values. • rp slot -- See the the Note below for valid values. • vtt number --1 to 3. • clock number --1 and 2. Note The slotargument designates the module and port number. Valid values for slot depend on the chassis and module that are used. For example, if you have a 48-port 10/100BASE-T Ethernet module that is installed in a 13-slot chassis, valid values for the slot number are from 1 to 13 and valid values for the port number are from 1 to 48. The show environment temperature module command output includes the updated information after an SCP response is received. In the output display, the following applies: • N/O means not operational--The sensor is broken, returning impossible values. • N/A means not available--The sensor value is presently not available; try again later. • VTT 1, 2, and 3 refer to the power monitors that are located on the chassis backplane under the rear cover.

**Example:**

This example shows how to display the temperature information for a specific module:

```text
Router>
show environment temperature
module 5
module 5 outlet temperature: 34C
module 5 inlet temperature: 27C
module 5 device-1 temperature: 42C
module 5 device-2 temperature: 41C
module 5 asic-1 (SSO-1) temp: 29C
module 5 asic-2 (SSO-2) temp: 29C
module 5 asic-3 (SSO-3) temp: 29C
module 5 asic-4 (SSO-4) temp: 28C
module 5 asic-5 (SSA-1) temp: 29C
module 5 asic-6 (HYPERION-1) temp: 29C
Router>
```

This example shows how to display the temperature readings for all modules:

```text
Router>
show environment temperature
VTT 1 outlet temperature: 25C
VTT 2 outlet temperature: 24C
VTT 3 outlet temperature: 28C
module 1 outlet temperature: 24C
module 1 device-2 temperature: 29C
RP 1 outlet temperature: 25C
RP 1 inlet temperature: 29C
EARL 1 outlet temperature: 25C
EARL 1 inlet temperature: 22C
module 5 outlet temperature: 27C
module 5 inlet temperature: 22C
Router>
```

The following table describes the fields that are shown in the example. s howenvironmenttemperature

| Field | Description |
| --- | --- |
| outlettemperature | Exhausttemperaturevalue. |

| Field | Description |
| --- | --- |
| inlettemperature | Intaketemperaturevalue. |
| device-1anddevice-2temperature | Twodevicesthatmeasuretheinternaltemperatureontheindicated module.Thetemperatureshownindicatesthetemperaturethatthedevice isrecording.Thedevicesarenotplacedataninletoranexitbutare additionalreferencepoints. |


### `show errdisable detect`

> **Página:** 666 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the error-disable detection status, use the show errdisable detect command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show errdisable detect
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17b)SXA | This command was changed to include p a c k e t-buffer error status information. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release 12.2(17d)SXB. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to display the error-disable detection status:

```text
Router>
show errdisable detect
ErrDisable Reason Detection status
----------------- ----------------
udld Enabled
bpduguard Enabled
rootguard Enabled
packet-buffer-err Enabled
pagp-flap Enabled
dtp-flap Enabled
link-flap Enabled
```


### `show errdisable recovery`

> **Página:** 667 · **Modo:** EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the information about the error-disable recovery timer, use the show errdisable recovery command in EXEC mode.

**Syntax:**

```text
show errdisable recovery
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default settings.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to display the information about the error-disable recovery timer:

```text
show errdisable recovery
ErrDisable Reason Timer Status
----------------- --------------
udld Enabled
bpduguard Enabled
rootguard Enabled
pagp-flap Enabled
dtp-flap Enabled
link-flap Enabled
Timer interval:300 seconds
Interfaces that will be enabled at the next timeout:
Interface Errdisable reason Time left(sec)
--------- ----------------- --------------
Fa9/4 link-flap 279
```


### `show fastblk`

> **Página:** 668 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display fast block memory information, use the show fastblkcommand in privileged EXEC mode.

**Syntax:**

```text
show fastblk [detailed]
```

**Parameters (Syntax Description):**

- `detailed` — ( Optional) D is p l a y s detailed allocate d fast b lock memory pool information.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(22)T | This command was introduced. |

**Usage Guidelines:**

Use this command to display allocated fast block memory pool details. When no memory pools are allocated, the “no fastblk memory pools allocated” message is displayed.

**Example:**

The following is sample output from the show fastblk command using the detailed keyword. The fields are self-explanatory.

```text
show fastblk detailed
Pool name: SCTP ApplReq flags:DYN_POOL
total = 400 inuse = 0, free = 400, max = 0
increment = 200, threshold = 100, hist max = 400
alloc failures = 0, sub-pool creation failures = 0
subpool: blks = 0x62968A2C, total = 400, inuse= 0, free = 400
delete count = 0, flags:
Pool name: SCTP BufSegHdr flags:DYN_POOL
total = 9000 inuse = 0, free = 9000, max = 0
increment = 4500, threshold = 6750, hist max = 9000
alloc failures = 0, sub-pool creation failures = 0
subpool: blks = 0x62B8E2F4, total = 9000, inuse= 0, free = 9000
delete count = 0, flags:
Pool name: SCTP DestAddr flags:DYN_POOL
total = 80 inuse = 0, free = 80, max = 0
increment = 40, threshold = 20, hist max = 80
alloc failures = 0, sub-pool creation failures = 0
subpool: blks = 0x62972534, total = 80, inuse= 0, free = 80
delete count = 0, flags:
Pool name: SCTP Addr flags:DYN_POOL POOL_HAS_GRWN
total = 200 inuse = 100, free = 100, max = 0
increment = 50, threshold = 50, hist max = 200
alloc failures = 31, sub-pool creation failures = 0
subpool: blks = 0x6271B6D0, total = 50, inuse= 0, free = 50
delete count = 0, flags: DYN_SUBPOOL
subpool: blks = 0x6271D730, total = 50, inuse= 0, free = 50
delete count = 0, flags: DYN_SUBPOOL
subpool: blks = 0x6297680C, total = 100, inuse= 100, free = 0
delete count = 0, flags:
Pool name: SCTP ChunkDesc flags:DYN_POOL
total = 9000 inuse = 0, free = 9000, max = 0
increment = 4500, threshold = 6750, hist max = 9000
alloc failures = 0, sub-pool creation failures = 0
subpool: blks = 0x62BE6160, total = 1471, inuse= 0, free = 1471
delete count = 0, flags:
subpool: blks = 0x62D8D768, total = 7529, inuse= 0, free = 7529
delete count = 0, flags:
Pool name: SCTP DgramHdr flags:DYN_POOL
total = 9000 inuse = 0, free = 9000, max = 0
increment = 4500, threshold = 6750, hist max = 9000
alloc failures = 0, sub-pool creation failures = 0
subpool: blks = 0x62BFE848, total = 9000, inuse= 0, free = 9000
delete count = 0, flags:
Pool name: SCTP Assoc flags:DYN_POOL
total = 100 inuse = 0, free = 100, max = 0
increment = 50, threshold = 25, hist max = 100
alloc failures = 0, sub-pool creation failures = 0
subpool: blks = 0x62E0A778, total = 100, inuse= 0, free = 100
delete count = 0, flags:
Pool name: SCTP Instance flags:DYN_POOL
total = 200 inuse = 50, free = 150, max = 0
increment = 100, threshold = 50, hist max = 200
alloc failures = 0, sub-pool creation failures = 0
subpool: blks = 0x62C33434, total = 200, inuse= 50, free = 150
delete count = 0, flags:
Pool name: SCTP Assoc Stats flags:DYN_POOL
total = 100 inuse = 0, free = 100, max = 0
increment = 50, threshold = 25, hist max = 100
alloc failures = 0, sub-pool creation failures = 0
subpool: blks = 0x62C39EA0, total = 100, inus
```


### `show file descriptors`

> **Página:** 669 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display a list of open file descriptors, use the show file descriptorscommand in EXEC mode.

**Syntax:**

```text
show file descriptors
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

File descriptors are the internal representations of open files. You can use this command to learn if another user has a file open.

**Example:**

The following is sample output from the show file descriptors command:

```text
show file descriptors
File Descriptors:
FD Position Open PID Path
0 187392 0001 2 tftp://dirt/hampton/c4000-i-m.a
1 184320 030A 2 flash:c4000-i-m.a
```

The table below describes the fields shown in the display.

| Field | Description |
| --- | --- |
| FD | Filedescriptor.Thefiledescriptorisasmallintegerusedtospecifythefileonceithasbeenopened. |
| Position | Byteoffsetfromthestartofthefile. |
| Open | Flagssuppliedwhenopeningthefile. |
| PID | ProcessIDoftheprocessthatopenedthefile. |
| Path | Locationofthefile. |


### `show file information`

> **Página:** 670 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about a file, use the show file informationcommand in EXEC mode.

**Syntax:**

```text
show file information file-url
```

**Parameters (Syntax Description):**

- `file-url` — The URL of the file to d is p l a y.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

The following is sample output from the show file information command:

```text
Router# show file information tftp://dirt/hampton/c2500-j-l.a
tftp://dirt/hampton/c2500-j-l.a:
type is image (a.out) [relocatable, run from flash]
file size is 8624596 bytes, run size is 9044940 bytes [8512316+112248+420344]
Foreign image
Router# show file information slot0:c7200-js-mz
slot0:c7200-js-mz:
type is image (elf) []
file size is 4770316 bytes, run size is 4935324 bytes
Runnable image, entry point 0x80008000, run from ram
Router1#
show file information nvram:startup-config
nvram:startup-config:
type is ascii text
```

The table below describes the possible file types.

| Types | Description |
| --- | --- |
| image(a.out) | Runnableimageina.outformat. |
| image(elf) | Runnableimageinelfformat. |
| asciitext | Configurationfileorothertextfile. |
| coff | Runnableimageincoffformat. |
| ebcdic | TextgeneratedonanIBMmainframe. |
| lzwcompression | Lzwcompressedfile. |
| tar | TextarchivefileusedbytheChannelInterfaceProcessor(CIP). |


### `show file systems`

> **Página:** 671 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To list available file systems, use the show file systems command in privileged EXEC mode.

**Syntax:**

```text
show file systems
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | This command was introduced. |
| 12.3(7)T | This command was e n h an c e d to d is p l a y information about the AT A ROMmon it or l i b r a r y ( monlib) file. |
| 12.2(25)S | This command was integrated into Cisco IOS Release12.2(25) S. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I and the output was modified. |
| 12.4(24)T | This command was integrated into Cisco IOS Release12.4(24) T and the output was modified. |
| 15.0(01)XO | Note added to e x p l a in d if f e r e n t by t e and usage c a l c u l at i on s for show filesystem s and dir commands on c at4000 s e r i e s routers. |
| 15.1(2)SNG | This command was i m p l e m e n t e do n the Cisco AS R901 S e r i e s A g g r e g at i on Service s Routers. |

**Usage Guidelines:**

Use this command to learn the alias names, the Prefixes column in the output of the file systems that your router supports.

**Example:**

The following is sample output from the show file systems command:

```text
show file systems
File Systems:
Size(b) Free(b) Type Flags Prefixes
- - ram rw tmp:
- - opaque rw system:
42541056 42541056 disk rw disk1: disk1:0:#
* 512065536 30834688 disk rw disk0:#
65536000 19811932 flash rw bootflash: sup-bootflash:
- - opaque ro ivfs:
129004 102228 nvram rw const_nvram:
125802334 0 opaque ro microcode: sup-microcode:
0 609689428 opaque rw image: sup-image:
- - opaque rw null:
- - opaque ro tar:
1964024 1949453 nvram rw nvram:
- - network rw rcp:
- - network rw tftp:
- - network rw http:
- - network rw ftp:
- - disk rw disk1:1:
- - disk rw disk1:2:
512065536 30842880 disk rw slavedisk0:#
- - disk rw slavedisk1: slavedisk1:0:
65536000 19328264 flash rw slavesup-bootflash:
1964024 1919757 nvram rw slavenvram:
129004 102228 nvram rw slaveconst_nvram:
65536000 65536000 flash rw slavebootflash:
- - nvram rw slavercsf:
- - opaque rw slavesystem:
- - disk rw slavedisk1:1:
- - disk rw slavedisk1:2:
- - disk rw slavedisk1:3:
```

The table below describes the significant fields shown in the display.

| Field | Description |
| --- | --- |
| Size(b) | Amountofmemoryinthefilesystem(inbytes). The"*"referencesthedefaultdevice/directorywhenflashisusedinagenericmanner.Forexample, ifyouweretotypeshflashandthedeviceactuallyhasbootflash:,theoutputofshflashwillactually betheoutputofdirbootflash:showfilesystemsshowsthedevicesthatthisrtrcanaccess.The"*" indicatesthedefaultdevice. |
| Free(b) | Amountoffreememoryinthefilesystem(inbytes). |

| Field | Description |
| --- | --- |
| Type | Typeoffilesystem.Thefilesystemcanbeoneofthefollowingtypes: •disk--Thefilesystemisforarotatingmedium. •flash--Thefilesystemisforaflashmemorydevice. •network--Thefilesystemisanetworkfilesystem(TFTP,rcp,FTP,andsoon). •nvram--ThefilesystemisforanNVRAMdevice. •opaque--Thefilesystemisalocallygenerated“pseudo”filesystem(forexample,the“system”) oradownloadinterface,suchasbrimux. •ram--ThefilesystemisforaRAMorEPROMdevice. •tty--Thefilesystemisforacollectionofterminaldevices. •unknown--Thefilesystemisofunknowntype. |
| Flags | Permissionsforthefilesystem.Thefilesystemcanhaveoneofthefollowingpermissionstates: •ro--ThefilesystemisReadOnly. •wo--ThefilesystemisWriteOnly. •rw--ThefilesystemisRead/Write. |
| Prefixes | Aliasforthefilesystem.Prefixesmarkedwithapoundsymbol(#)indicateabootabledisk. |

Note As of release 15.0(01)XO, on cat4000 series routers, the show file systems and dirwill display slightly different byte count and usage information for the same file system. This is due to slight difference in how IOS computes these figures for this platform.


The show flh-log command has been replaced by the more flh:logfile command. See the description of the more flh:logfile command for more information.

### `show fm inspect`

> **Página:** 673 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the list and status of the access control lists (ACLs) and ports on which context based access control (CBAC) is configured, use the show fm inspect command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show fm inspect [detail | interface type mod/port]
```

**Parameters (Syntax Description):**

- `detail` — ( Optional) D is p l a y s all of the f low information.
- `interface type` — Interface type; p o s s i b l e v a l id values are e the r n e t, fast e the r n e t, g i g a b it e the r n e t, t e n g i g a b it e the r n e t, port-c h an n e l, p o s, at m, n u l l, t u n n e l, and g e-w an
- `mod / port` — Module and port number.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If you can configure a VLAN access control list (VACL) on the port before you configure CBAC, the status displayed is INACTIVE; otherwise, it is ACTIVE. If policy feature card (PFC) resources are exhausted, the command displays BRIDGE and is followed by the number of failed currently active NetFlow requests that have been sent to the MSFC2 for processing. The show fm inspect command output includes this information: • interface:--Interface on which the internet protocol (IP) inspect feature is enabled • (direction)--Direction in which the IP inspect feature is enabled (IN or OUT) • acl name:--Name that is used to identify packets being inspected • status:--(ACTIVE or INACTIVE) displays if HW-assist is provided for this interface+direction (ACTIVE=hardware assisted or INACTIVE) The optional detail keyword displays the ACEs that are part of the ACL that is used for IP inspect on the given interface direction.

**Example:**

This example shows how to display the list and status of CBAC-configured ACLs and ports:

```text
Router>
show fm inspect
interface:Vlan305(in) status :ACTIVE
acl name:deny
interfaces:
Vlan305(out):status ACTIVE
```


### `show fm interface`

> **Página:** 675 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the detailed information about the feature manager on a per-interface basis, use the show fm interface command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show fm interface {interface type mod/port | null interface-number | port-channel number | vlan
vlan-id}
```

**Parameters (Syntax Description):**

- `type` — Interface type; p o s s i b l e v a l id values are e the r n e t, fast e the r n e t, g i g a b it e the r n e t, t e n g i g a b it e the r n e t, port-c h an n e l, p o s, at m, n u l l, t u n n e l, and g e-w an
- `mod / port` — Module and port number.
- `null interface-number` — Specifies then u l l interface; the v a l id value is0.
- `port-c h an n e l number` — Specifies the c h an n e l interface; v a l id values are a maximum of64 values ranging from1 to282.
- `vlan vlan-id` — Specifies the v i r t u alloc a l are an e two r k( VLAN); v a l id values are from1 to4094.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17a)SX | The or d e r of the information that is d is p l a y e d in the show fm interface vlan command output was changed. |
| 12.2(17d)SXB | Support for this command on Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The pos, atm, and ge-wan keywords are supported on Cisco 7600 series routers that are configured with a Supervisor Engine 2 The interface-number argument designates the module and port number. Valid values for interface-number depend on the specified interface type and the chassis and module that are used. For example, if you specify a Gigabit Ethernet interface and have a 48-port 10/100BASE-T Ethernet module that is installed in a 13-slot chassis, valid values for the module number are from 1 to 13 and valid values for the port number are from 1 to 48. The port-channel numbervalues from 257 to 282 are supported on the CSM and the FWSM only.

**Example:**

This example shows how to display the detailed information about the feature manager on a specified interface:

```text
Router>
show fm interface fastethernet 2/26
Interface:FastEthernet2/26 IP is enabled
hw[EGRESS] = 1, hw[INGRESS] = 0
hw_force_default[EGRESS] = 0, hw_force_default[INGRESS] = 1
mcast = 0
priority = 2
reflexive = 0
inbound label:24
protocol:ip
feature #:1
feature id:FM_IP_ACCESS
ACL:113
vmr IP value #1:0, 0, 0, 0, 0, 0, 0, 6 - 1
vmr IP mask #1:0, 0, FFFF, FFFF, 0, 0, 0, FF
vmr IP value #2:642D4122, 0, 0, 0, 1, 0, 0, 6 - 1
vmr IP mask #2:FFFFFFFF, 0, 0, 0, 1, 0, 0, FF
vmr IP value #3:0, 64020302, 0, 0, 6, 0, 0, 6 - 1
vmr IP mask #3:0, FFFFFFFF, 0, 0, 6, 0, 0, FF
vmr IP value #4:0, 64020302, 0, 0, A, 0, 0, 6 - 1
vmr IP mask #4:0, FFFFFFFF, 0, 0, A, 0, 0, FF
vmr IP value #5:0, 64020302, 0, 0, 12, 0, 0, 6 - 1
vmr IP mask #5:0, FFFFFFFF, 0, 0, 12, 0, 0, FF
vmr IP value #6:0, 0, 0, 0, 0, 0, 0, 0 - 2
vmr IP mask #6:0, 0, 0, 0, 0, 0, 0, 0
outbound label:3
protocol:ip
feature #:1
feature id:FM_IP_WCCP
Service ID:0
Service Type:0
Router>
```

This example shows how to display the detailed information about the feature manager on a specific VLAN:

```text
Router> show fm interface vlan 21
Interface: Vlan21 IP is disabled
hw_state[INGRESS] = not reduced, hw_state[EGRESS] = not reduced
mcast = 0
priority = 0
flags = 0x0
inbound label: 8
Feature IP_VACL:
-----------------------------------------------------------------------------
FM_FEATURE_IP_VACL_INGRESS i/f: Vl21 map name: test
=============================================================================
------------------------------------------------------------
IP Seq. No: 10 Seq. Result : VACL_ACTION_FORWARD_CAPTURE
------------------------------------------------------------
DPort - Destination Port SPort - Source Port Pro - Protocol
X - XTAG TOS - TOS Value Res - VMR Result
RFM - R-Recirc. Flag MRTNP - M-Multicast Flag R - Reflexive flag
- F-Fragment flag - T-Tcp Control N - Non-cachable
- M-More Fragments - P-Mask Priority(H-High, L-Low)
Adj. - Adj. Index T - M(Mask)/V(Value) FM - Flow Mask
NULL - Null FM SAO - Source Only FM DAO - Dest. Only FM
SADA - Sour.& Dest. Only VSADA - Vlan SADA Only FF - Full Flow
VFF - Vlan Full Flow F-VFF - Either FF or VFF A-VSD - Atleast VSADA
A-FF - Atleast FF A-VFF - Atleast VFF A-SON - Atleast SAO
A-DON - Atleast DAO A-SD - Atleast SADA SHORT - Shortest
A-SFF - Any short than FF A-EFF - Any except FF A-EVFF- Any except VFF
A-LVFF- Any less than VFF ERR - Flowmask Error
+----+-+---------------+---------------+-----+-----+---+---+-+---+-----+----+------+
|Indx|T| Dest Ip Addr | Source Ip Addr|DPort|SPort|Pro|RFM|X|ToS|MRTNP|Adj.| FM |
+----+-+---------------+---------------+-----+-----+---+---+-+---+-----+----+------+
1 V 22.2.2.2 21.1.1.1 0 0 0 --- 0 0 ----L ---- SHORT
M 255.255.255.255 255.255.255.255 0 0 0 000 0 0
TM_PERMIT_RESULT
2 V 32.2.2.2 31.1.1.1 0 0 0 --- 0 0 ----L ---- SHORT
M 255.255.255.255 255.255.255.255 0 0 0 000 0 0
TM_PERMIT_RESULT
3 V 0.0.0.0 0.0.0.0 0 0 0 --- 0 0 ----L ---- SHORT
M 0.0.0.0 0.0.0.0 0 0 0 000 0 0
TM_L3_DENY_RESULT
------------------------------------------------------------
IP Seq. No: 65536 Seq. Result : VACL_ACTION_DROP
------------------------------------------------------------
+----+-+---------------+---------------+-----+-----+---+---+-+---+-----+----+------+
|Indx|T| Dest Ip Addr | Source Ip Addr|DPort|SPort|Pro|RFM|X|ToS|MRTNP|Adj.| FM |
+----+-+---------------+---------------+-----+-----+---+---+-+---+-----+----+------+
1 V 0.0.0.0 0.0.0.0 0 0 0 --- 0 0 ----L ---- SHORT
M 0.0.0.0 0.0.0.0 0 0 0 000 0 0
TM_PERMIT_RESULT
Router>
```


### `show fm reflexive`

> **Página:** 677 · **Modo:** Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the information about the reflexive entry for the dynamic feature manager, use the show fm reflexive command in privileged EXEC mode.

**Syntax:**

```text
show fm reflexive
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to display the information about the reflexive entry for the dynamic feature manager:

```text
show fm reflexive
Reflexive hash table:
Vlan613:refacl, OUT-REF, 64060E0A, 64060D0A, 0, 0, 7, 783, 6
```


### `show fm summary`

> **Página:** 678 · **Modo:** User EXEC Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display a summary of feature manager information, use the show fm summary command in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show fm summary
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** This command has no default settings.

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

This example shows how to display a summary of feature manager information:

```text
Router>
show fm summary
Current global ACL merge algorithm:BDD
Interface:FastEthernet2/10
ACL merge algorithm used:
inbound direction: ODM
outbound direction:BDD
TCAM screening for features is ACTIVE outbound
TCAM screening for features is ACTIVE inbound
Interface:FastEthernet2/26
ACL merge algorithm used:
inbound direction: ODM
outbound direction:BDD
TCAM screening for features is ACTIVE outbound
TCAM screening for features is INACTIVE inbound
Router>
```


### `show funi`

> **Página:** 679 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display the frame-based user-network interface information, use the show funicommand in user EXEC or privileged EXEC mode.

**Syntax:**

```text
show funi {arp-server [atm atm-interface-number] | class-links {vpi/vci-valuevci-valueconnection-name}
| ilmi-configuration | ilmi-status [atm atm-interface-number] | map |
pvc[vpi/vci-valuevci-valueconnection-name | dbs | ppp] | route | traffic | vp atm-vpi-number | vc
{atm-vcd-numberconnection-name | detail [prefix {interface | vc-name | vcd | vpi/vci}]} | interface atm
atm-interface-number {connection-name | detail [prefix {interface | vc-name | vcd | vpi/vci}]} | range
lower-vcd-limit upper-vcd-limit {connection-name | detail [prefix {interface | vc-name | vcd | vpi/vci}]}
| interface atm atm-interface-number {connection-name | detail [prefix {interface | vc-name | vcd |
vpi/vci}]} | summary [atm atm-interface-number]}
```

**Parameters (Syntax Description):**

- `arp-server` — D is p l a y s Async h r on o u s T r an s f e r Mode( AT M) address r e s o l u t i on p r o to c o l server t a b l e information.
- `atm atm-interface-number` — ( Optional) Specifies the AT Min t e r f a c e and the AT Min t e r f a c e number.
- `class-links` — D is p l a y s AT M V C-class link s information.
- `v p i/ v c i-value` — ( Optional) Specifies the Virtual Path Id e n t if i e r or Virtual Channel Id e n t if i e r ( V P I/ V C I) value( s l as h is m and at or y).
- `vci-value` — ( Optional) Specifies the v i r t u a l c i r c u it interface value.
- `connection-name` — ( Optional) Specifies the connection name.
- `ilmi-configuration` — D is p l a y s the to p-level Integrated Local Management Interface( I L M I) information.
- `ilmi-status` — Display AT Min t e r f a c e I L M I information.
- `map` — D is p l a y s AT M s t at i c map ping information.
- `pvc` — D is p l a y s AT M P e r m an e n t Virtual C i r c u its( P V C) information.
- `dbs` — D is p l a y s the D B S information on a v i r t u a l c i r c u it.
- `ppp` — D is p l a y s the PPPover AT Min format i on
- `route` — D is p l a y s AT M route information.
- `traffic` — D is p l a y s AT M statistics.
- `vp` — D is p l a y s AT M v i r t u a l path information.
- `atm-vpi-number` — ( Optional) Specifies the V P In u m be r.
- `vc` — D is p l a y s AT M v i r t u a l c i r c u it information.
- `atm-vcd-number` — ( Optional) Specifies the AT M V i r t u a l Circuit D e s c r ip to r( V CD) number.
- `detail` — D is p l a y s the detailed information of all VCs.
- `prefix` — ( Optional) Specifies the pref i x for the output or d e r in g.
- `interface` — Specifies the type of interface. When this keyword is used a l on g with the pref i x keyword it d is p l a y s the interface values in as c end in g or d e r.
- `vc_name` — D is p l a y s the V C names in the a l p h a be t i c a l or d e r.
- `vcd` — D is p l a y s the V CD value in the as c end in g or d e r.
- `vpi/vci` — D is p l a y s the V P I/ V C I value in the as c end in g or d e r.
- `range` — D is p l a y s the range of VCs.
- `lower-vcd-limit` — Specifies the low e r limit V CD value.
- `upper-vcd-limit` — Specifies the u p p e r limit V CD value.
- `summary` — D is p l a y summary of VCs.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.4(24)T | This command was introduced. |
| CiscoIOSXE2.3 | This command was i m p l e m e n t e do n Cisco AS R1000 s e r i e s routers. |

**Usage Guidelines:**

Use this command to display the frame-based user-network interface information with the available keywords and arguments.

**Example:**

The following is sample output from the show funi trafficcommand. The fields are self-explanatory:

```text
Router# show funi traffic
Input OAM Queue: 0/4136 (size/max)
0 Input packets
0 Output packets
0 Broadcast packets
0 Packets received on non-existent VC
0 Packets attempted to send on non-existent VC
0 OAM cells received
F5 InEndloop: 0, F5 InSegloop: 0, F5 InAIS: 0, F5 InRDI: 0
F5 InEndcc: 0, F5 InSegcc: 0,
F4 InEndloop: 0, F4 InSegloop: 0, F4 InAIS: 0, F4 InRDI: 0
0 OAM cells sent
F5 OutEndloop: 0, F5 OutSegloop: 0, F5 OutAIS: 0 F5 OutRDI: 0
F5 OutEndcc: 0, F5 OutSegcc: 0,
F4 OutEndloop: 0, F4 OutSegloop: 0, F4 OutRDI: 0 F4 OutAIS: 0
0 OAM cell drops
```

The following is sample out from the show funi vc detail prefix interface command. The fields are self-explanatory:

```text
Router# show funi vc detail prefix interface
Description: N/A
ATM2/0 ATM2/0: VCD: 1, VPI: 1, VCI: 100
ATM2/0 UBR, PeakRate: 0 (0 cps)
ATM2/0 AAL5-LLC/SNAP, etype:0x0, Flags: 0xC20, VCmode: 0x0, Encapsize: 12
ATM2/0 OAM frequency: 0 second(s)
ATM2/0 InARP frequency: 15 minutes(s)
ATM2/0 Transmit priority 6
ATM2/0 InPkts: 0, OutPkts: 0, InBytes: 0, OutBytes: 0
InCells: 0, OutCells: 0
ATM2/0 InPRoc: 0, OutPRoc: 0, Broadcasts: 0
ATM2/0 InFast: 0, OutFast: 0, InAS: 0, OutAS: 0
ATM2/0 InPktDrops: 0, OutPktDrops: 0
ATM2/0 CrcErrors: 0, SarTimeOuts: 0, OverSizedSDUs: 0, LengthViolation: 0, CPIE0
ATM2/0 Out CLP=1 Pkts: 0, Cells: 0
ATM2/0 OAM cells received: 0
ATM2/0 OAM cells sent: 0
ATM2/0 Status: INACTIVE
Description: N/A
ATM2/0 ATM2/0: VCD: 2, VPI: 1, VCI: 101
ATM2/0 UBR, PeakRate: 0 (0 cps)
ATM2/0 AAL5-LLC/SNAP, etype:0x0, Flags: 0xC20, VCmode: 0x0, Encapsize: 12
ATM2/0 OAM frequency: 0 second(s)
```

The following is sample out from the show funi vc detail prefix vc_name command. The fields are self-explanatory:

```text
Router# show funi vc detail prefix vc_name
Description: N/A
ATM2/0: VCD: 1, VPI: 1, VCI: 100
UBR, PeakRate: 0 (0 cps)
AAL5-LLC/SNAP, etype:0x0, Flags: 0xC20, VCmode: 0x0, Encapsize: 12
OAM frequency: 0 second(s)
InARP frequency: 15 minutes(s)
Transmit priority 6
InPkts: 0, OutPkts: 0, InBytes: 0, OutBytes: 0
InCells: 0, OutCells: 0
InPRoc: 0, OutPRoc: 0, Broadcasts: 0
InFast: 0, OutFast: 0, InAS: 0, OutAS: 0
InPktDrops: 0, OutPktDrops: 0
CrcErrors: 0, SarTimeOuts: 0, OverSizedSDUs: 0, LengthViolation: 0, CPIErrors: 0
Out CLP=1 Pkts: 0, Cells: 0
OAM cells received: 0
OAM cells sent: 0
Status: INACTIVE
Description: N/A
ATM2/0: VCD: 2, VPI: 1, VCI: 101
UBR, PeakRate: 0 (0 cps)
AAL5-LLC/SNAP, etype:0x0, Flags: 0xC20, VCmode: 0x0, Encapsize: 12
OAM frequency: 0 second(s)
InARP frequency: 15 minutes(s)
```

The following is sample out from the show funi vc detail prefix pvi/vci command. The fields are self-explanatory:

```text
Router# show funi vc detail prefix vpi/vci
Description: N/A
VPI/VCI: 1/100 ATM2/0: VCD: 1, VPI: 1, VCI: 100
VPI/VCI: 1/100 UBR, PeakRate: 0 (0 cps)
VPI/VCI: 1/100 AAL5-LLC/SNAP, etype:0x0, Flags: 0xC20, VCmode: 0x0, Encapsize: 2
VPI/VCI: 1/100 OAM frequency: 0 second(s)
VPI/VCI: 1/100 InARP frequency: 15 minutes(s)
VPI/VCI: 1/100 Transmit priority 6
VPI/VCI: 1/100 InPkts: 0, OutPkts: 0, InBytes: 0, OutBytes: 0
InCells: 0, OutCells: 0
VPI/VCI: 1/100 InPRoc: 0, OutPRoc: 0, Broadcasts: 0
VPI/VCI: 1/100 InFast: 0, OutFast: 0, InAS: 0, OutAS: 0
VPI/VCI: 1/100 InPktDrops: 0, OutPktDrops: 0
VPI/VCI: 1/100 CrcErrors: 0, SarTimeOuts: 0, OverSizedSDUs: 0, LengthViolation:0
VPI/VCI: 1/100 Out CLP=1 Pkts: 0, Cells: 0
VPI/VCI: 1/100 OAM cells received: 0
VPI/VCI: 1/100 OAM cells sent: 0
VPI/VCI: 1/100 Status: INACTIVE
Description: N/A
VPI/VCI: 1/101 ATM2/0: VCD: 2, VPI: 1, VCI: 101
VPI/VCI: 1/101 UBR, PeakRate: 0 (0 cps)
VPI/VCI: 1/101 AAL5-LLC/SNAP, etype:0x0, Flags: 0xC20, VCmode: 0x0, Encapsize: 2
```


### `show identity policy`

> **Página:** 682 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display identity policy information in a tabular form, use the show identity policycommand in privileged EXEC mode.

**Syntax:**

```text
show identity policy [name]
```

**Parameters (Syntax Description):**

- `name` — ( Optional) Name of the identity policy.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SX | This command was introduced. |

**Example:**

The following is output from the show identity policy command:

```text
Router# show identity policy
Policy Name ACL Redirect ACL Redirect URL
===============================================================================
p1 some-acl NONE NONE
p2 another-acl redirect-acl http://www.foo.com/bar.html
```

The following is output for the policy named p2:

```text
Router# show identity policy p2
Name: p2
Description: NONE
Access-Group: another-acl
URL-Redirect Match ACL: redirect-acl
URL-Redirect URL: http://www.foo.com/bar.html
```


### `show identity profile`

> **Página:** 683 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display identity profile information in a tabular form, use the show identity profilecommand in privileged EXEC mode.

**Syntax:**

```text
show identity profile [default | dot1x | eapoudp]
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

The following is output from the show identity profilecommand:

```text
Router# show running identity profile
Service Type: default
Default Authorized Device Policy: NONE
Default Non-Authorized Device Policy: NONE
Device / Address / Mask Allowed Policy
==============================================================
Cisco IP Phone Authorized DEFAULT
Service Type: dot1x
Default Authorized Device Policy: NONE
Default Non-Authorized Device Policy: NONE
Device / Address / Mask Allowed Policy
==============================================================
0001.0203.0405 / ffff.ffff.ffff Authorized p2
Service Type: eapoudp
Device / Address / Mask Allowed Policy
==============================================================
10.0.0.0 / 255.0.0.0 Authorized p1
```


### `show install`

> **Página:** 683 · **Modo:** Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** sim

**Description:** To display information about installed packages, use the show install command in privileged EXEC mode.

**Syntax:**

```text
show install {active | committed | inactive | log | package {bootflash: | flash: | webui:} | rollback |
summary | uncommitted}
```

**Parameters (Syntax Description):**

- `active` — D is p l a y s information about active package s.
- `commit t e d` — D is p l a y s package activation s that are persistent.
- `in a c t i v e` — D is p l a y s in a c t i v e package s.
- `log` — D is p l a y s entries stored in the logging install at i on buffer.
- `package` — D is p l a y s m e t a data information about the package,
- `in c l u d in g` — description, restart information,
- `c o m p one n t s` — in the package, and so on. { bootflash: | flash: | h a r d disk: | web u i:} Specifies the location of the install package.
- `rollback` — D is p l a y s the software set as s o c i at e d with a saved install at i on.
- `summary` — D is p l a y s information about the list of active, in a c t i v e, commit t e d, and sup e r s e d e d package s.
- `u n commit t e d` — D is p l a y s package activation s that are no n persistent.

**Command Modes:** Privileged EXEC (#)

**Usage Guidelines:**

Use the show commands to view the status of the installed package. Example The following is sample output from the show install package command:

```text
Device# show install package bootflash:isr4300-universalk9.2017-01-10_13.15.1.
CSCxxx.SSA.dmp.bin
Name: isr4300-universalk9.2017-01-10_13.15.1.CSCxxx.SS
Version: 16.5.1.0.199.1484082952..Everest
Platform: ISR4300
Package Type: dmp
Defect ID: CSCxxx
Package State: Added
Supersedes List: {}
Smu ID: 1
```

The following is sample output from the show install summary command:

```text
Device# show install summary
Active Packages:
bootflash:isr4300-universalk9.2017-01-10_13.15.1.CSCxxx.SSA.dmp.bin
Inactive Packages:
No packages
Committed Packages:
bootflash:isr4300-universalk9.2017-01-10_13.15.1.CSCxxx.SSA.dmp.bin
Uncommitted Packages:
No packages
Device#
```

The table below lists the significant fields shown in the display. The following is sample output from the show install log command:

```text
Device#
show install log
[0|install_op_boot]: START Fri Feb 24 19:20:19 Universal 2017
[0|install_op_boot]: END SUCCESS Fri Feb 24 19:20:23 Universal 2017
[3|install_add]: START Sun Feb 26 05:55:31 UTC 2017
[3|install_add( FATAL)]: File path (scp) is not yet supported for this command
[4|install_add]: START Sun Feb 26 05:57:04 UTC 2017
[4|install_add]: END SUCCESS
/bootflash/isr4300-universalk9.2017-01-10_13.15.1.CSCvb12345.SSA.dmp.bin
Sun Feb 26 05:57:22 UTC 2017
[5|install_activate]: START Sun Feb 26 05:58:41 UTC 2017
```


### `show platform software snapshot status`

> **Página:** 685 · **Modo:** Privileged EXEC (#) Diagnostic Mode (diag) · **Default:** No default behavior or values · **Leitura (show/clear/…):** sim

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


### `show power usage`

> **Página:** 686 · **Modo:** Privileged EXEC (#) Command History · **Default:** This command has no default settings. · **Leitura (show/clear/…):** sim

**Description:** To display the power consumption of each component of the device and the total power consumption of the system, use the show power usage command in privileged EXEC mode. Syntax Description This command has no arguments or keywords.

**Syntax:**

```text
show power usage
```

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC (#) Command History

**Usage Guidelines:**

The show power usage command displays input power for the power supply unit, output power for the power supply unit and power usage by individual system components that include the following: • Motherboard • Modules - Network Interface Module (NIM), Switch Module (SM), Physical Interface Module (PIM), and Power over Ethernet (PoE). • Fan Tray Example The following is a sample output from the show power usage command.

```text
Device# show power usage
Slot Type Allocation State
-------- ------------------ -------------------- ------------
P0 PWR-CC1-650WAC 139 Watts (Input) Normal
P0 PWR-CC1-650WAC 134 Watts (Output) Normal
P1 PWR-CC1-1000WAC 12 Watts (Input) Normal
P1 PWR-CC1-1000WAC 4 Watts (Output) Normal
P2 C8300-FAN-2R 8 Watts Normal
POE1 PWR-CC1-MOD-POE 102 Watts (Input) Normal
1 C-SM-NIM-ADPT 3 Watts Normal
2 C-SM-NIM-ADPT 3 Watts Normal
1/1 C-NIM-2T 6 Watts Normal
0/2 NIM-4SHDSL-EA 6 Watts Normal
0/1 NIM-8CE1T1-PRI 6 Watts Normal
R0 C8300-2N2S-4T2X 132 Watts Normal
Total input power: 151 Watts
Total output power: 138 Watts
```

| Field | Description |
| --- | --- |
| Slot | Thecomponentslotnumber. |
| Type | ThecomponentproductID(PID). |
| Allocation | Thepowerconsumptionforeachcomponent. |
| State | Thecomponentpowerconsumptionstatus. |
| TotalIntputPower | Thenumberofwattsallocatedtothepowersupply units. |
| TotalOutputPower | Thenumberofwattsprovidedbythepowersupply units. Note Inaccuraciesinthemotherboardsensorsmaycause readingsonC8300-2N2Stobeslightlyhigherthan theactualvalues. |
