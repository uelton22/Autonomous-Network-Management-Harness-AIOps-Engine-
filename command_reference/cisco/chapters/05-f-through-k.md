# Capítulo 5: F through K

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## D through E

### F through K

• F through K, on page 198

### F through K

### `factory-reset all`

> **Página:** 222 · **Modo:** EXEC mode · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To erase all the user-configured data, use the factory-reset all command in EXEC mode:

**Syntax:**

```text
factory-reset all
```

**Parameters (Syntax Description):**

- `Syntax` — Description

**Command Modes:** EXEC mode

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXEBengaluruRelease17.6.1 | This command was introduced on ASR900,ASR920,and NCS 4200 platform s. |

**Usage Guidelines:**

The command erases the following data: • All writable file systems and personal data • OBFL logs • User data and startup configuration • ROMMON variables • User credentials • License information

**Example:**

The following example shows the configuration of the command:

```text
Router>enable
Router>factory-reset all
```


### `factory-reset keep-licensing-info`

> **Página:** 222 · **Modo:** EXEC mode · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To erase all the user-configured data except the licensing information, use the factory-reset keep-licensing-info command in EXEC mode:

**Syntax:**

```text
factory-reset keep-licensing-info
```

**Parameters (Syntax Description):**

- `Syntax` — Description

**Command Modes:** EXEC mode

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXEBengaluruRelease17.6.1 | This command was introduced on ASR900,ASR 920,and N C S4200 platform s. |

**Usage Guidelines:**

This command erases the following user-configured data: • All writable file systems and personal data • OBFL logs • User data and startup configuration • ROMMON variables • User credentials

**Example:**

The following example shows the configuration of the command:

```text
enable
factory-reset keep-licensing-info
```


### `factory-reset all secure 3-pass`

> **Página:** 223 · **Modo:** EXEC mode · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To erase all data using the the National Industrial Security Program Operating Manual (DoD 5220.22-M) Wiping Standard, use the factory-reset all secure 3-pass-DoD 5220-22-M command in EXEC mode: factory-reset all-secure 3-pass-DoD 5220-22-M

**Parameters (Syntax Description):**

- `Syntax` — Description

**Command Modes:** EXEC mode

**Command History:**

| Release | Modification |
| --- | --- |
| CiscoIOSXEBengaluruRelease17.6.1 | This command was introduced on ASR900,ASR920,and NCS 4200 platform s. |

**Usage Guidelines:**

The commands erases the following data • All writable file systems and personal data using the the National Industrial Security Program Operating Manual (DoD 5220.22-M) Wiping Standard: • OBFL logs • User data and startup configuration • ROMMON variables • User credentials • License information

**Example:**

The following example shows the configuration of the command:

```text
enable
factory-reset all-secure 3-pass
DoD 5220-22-M
```


### `file privilege`

> **Página:** 224 · **Modo:** Global configuration (config#) · **Default:** By default the privilege level is set to 15. · **Leitura (show/clear/…):** não

**Description:** To configure a new file privilege level for users use the file privilege command in global configuration mode. To reset the file privilege level of the files to the default and remove the file privilege level configuration from the running configuration file, use the no form of this command.

**Syntax:**

```text
file privilege level level
no file privilege level level
```

**Parameters (Syntax Description):**

- `level` — Specifies the file privilege level for the files. The level argument must be an u m be r from0 to15. Users with privilege level e q u a l to g r e at e r than the file privilege level can access the files under the filesystem.

**Command Default:** By default the privilege level is set to 15.

**Command Modes:** Global configuration (config#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.2(2)T | This command was introduced. |

**Example:**

The following example, shows how to set the file privilege level to 3 and verify the change using the show running-config command.

```text
Device(config)#
file privilege ?
<0-15> Privilege level
Device(config)# file privilege 3
Device(config)#
end
Device# show running-config | i file priv
file privilege 3
```


### `file prompt`

> **Página:** 224 · **Modo:** Global configuration · **Default:** alert · **Leitura (show/clear/…):** não

**Description:** To specify the level of prompting, use the file promptcommand in global configuration mode.

**Syntax:**

```text
file prompt prompt [alert | noisy | quiet]
```

**Parameters (Syntax Description):**

- `alert` — ( Optional) Prompt s only for d e s t r u c t i v e file o p e r at i on s. This is the default.
- `noisy` — ( Optional) Confirm s all file o p e r at i on parameters.
- `quiet` — ( Optional) S e l do m prompt s for file o p e r at i on s.

**Command Default:** alert

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to change the amount of confirmation needed for different file operations. This command affects only prompts for confirmation of operations. The router will always prompt for missing information.

**Example:**

The following example configures confirmation prompting for all file operations:

```text
Router(config)# file prompt noisy
```


### `file verify auto`

> **Página:** 225 · **Modo:** Global configuration · **Default:** Image verification is not automatically applied to all images that are copied or reloaded onto a router. · **Leitura (show/clear/…):** não

**Description:** To enable automatic image verification, use the file verify auto command in global configuration mode. To disable automatic image verification, use the no form of this command.

**Syntax:**

```text
file verify auto
no file verify auto
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Image verification is not automatically applied to all images that are copied or reloaded onto a router.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)S | This command was introduced. |
| 12.0(26)S | This command was integrated into Cisco IOS Release12.0(26) S. |
| 12.2(14)SX | This command was integrated into Cisco IOS Release12.2(14) S X and i m p l e m e n t e do n the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support was added for the Supervisor Engine2. |
| 12.3(4)T | This command was integrated into Cisco IOS Release12.3(4) T. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Image verification is accomplished by verifying the compressed Cisco IOS image checksum. Image verification allows users to automatically verify the integrity of all Cisco IOS images. Thus, users can be sure that the image is protected from accidental corruption, which can occur at any time during transit, starting from the moment the files are generated by Cisco until they reach the user. The file verify auto command enables image verification globally; that is, all images that are to be copied (via the copy command) or reloaded (via the reload command) are automatically verified. Although both the copy and reload commands have a /verify keyword that enables image verification, you must issue the keyword each time you want to copy or reload an image. The file verify auto command enables image verification by default so you no longer have to specify image verification multiple times. If you have enabled image verification by default but prefer to disable verification for a specific image copy or reload, the /noverify keyword along with either the copy or the reload command will override the file verify auto command.

**Example:**

The following example shows how to enable automatic image verification:

```text
Router(config)# file verify auto
```


### `format`

> **Página:** 226 · **Modo:** Privileged EXEC (#) Diagnostic (diag) · **Default:** spare-number : 0monlib-filename:The monlib file bundled with the system software · **Leitura (show/clear/…):** não

**Description:** To format a Class A, Class B, or Class C flash memory file system, use the format command in privileged EXEC or diagnostic mode. Class B and Class C Flash File Systems Class A Flash File System

**Syntax:**

```text
format filesystem1:
format [spare spare-number] filesystem1: [[filesystem2:][monlib-filename]]
```

**Parameters (Syntax Description):**

- `spare` — ( Optional) Reserve s s p are s e c to r s as specified by the s p are-number argument when you format flash memory.
- `spare-number` — ( Optional) Number of the s p are s e c to r s to reserve info r m at t e d flash memory. V a l id values are from0 to16. The default value is0.
- `filesystem1 :` — Flash memory to format, f o l low e d by a c o l on. V a l id values for use with the Cisco7600 s e r i e s router are disk0: disk1:, bootflash:, slot0:, sup-slot0:, and sup-bootflash:; see the“ Usage Guidelines” section for a d d it i on a l information. V a l id values for use with the AS R1000 S e r i e s Routers are bootflash:, h a r d disk:, s t by-h a r d disk:, o b f l:, and usb[01];.
- `filesystem2 :` — ( Optional) Filesystem c on t a in in gt h e monlib file to use for format t in gt h e argument filesystem1 f o l low e d by a c o l on.
- `monlib-filename` — ( Optional) Name of the ROMmon it or l i b r a r y file( monlib file) to use for format t in gt h e filesystem1 argument. The default monlib file is the one bundle d with the systems of t w are. Dual Route Switch Processor s( R S P) H i g h System A v a i l a b i l it y( H S A) F u n c t i on a l it y When this command is used with Dual R S P s and you do not specify the monlib-file name argument, the system t a k e s the ROMmon it or l i b r a r y file from the s e c on d a r y image bundle. If you specify the monlib-file name argument, the system as s u m e s that the files r e s id e on these c on d a r y device s.

**Command Default:** spare-number : 0monlib-filename:The monlib file bundled with the system software

**Command Modes:** Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.0 | This command was introduced. |
| 12.2(14)SX | Support for this command was added for the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release 12.2(17d)SXB. |
| 12.3(14)T | Support for Class B flash( USB flash and USBe Token) filesystem s was added as p a r to f the USB S to r age f e at u r e. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers and the following e n h an c e m e n t s were introduced: • This command was introduced in diagnostic mode for the first time. The command can been t e r e d in both privileged EXEC and diagnostic mode on the Cisco AS R1000 S e r i e s Routers. • The h a r d disk:, o b f l:, s t by-h a r d disk:, s t by-usb[0-1]: and usb[0-1]: filesystem1: options were introduced. |
| 12.2YST | This command was integrated into Cisco IOS Release12.2 Y S T. |

**Usage Guidelines:**

Reserve a certain number of memory sectors as spares, so that if some sectors fail, most of the flash memory card can still be used. Otherwise, you must reformat the flash card after some of the sectors fail. Use this command to format Class A, B, or C flash memory file systems. The Cisco 7600 series router supports only Class A and Class C flash file systems. In some cases, you might need to insert a new Personal Computer Memory Card Industry Association (PCMCIA) flash memory or flash PC card and load images or backup configuration files onto it. Before you can use a new flash memory or flash PC card, you must format it. Sectors in flash memory or flash PC cards can fail. Reserve certain flash memory or flash PC sectors as “spares” by using the optional spare-number argument on the format command to specify 0 to 16 sectors as spares. If you reserve a small number of spare sectors for emergencies, you can still use most of the flash memory or flash PC card. If you specify 0 spare sectors and some sectors fail, you must reformat the flash memory or flash PC card, thereby erasing all existing data. The monlib file is the ROM monitor library. The ROM monitor uses this file to access files in the flash file system. The Cisco IOS system software contains a monlib file. Use the show disk0: allcommand to display monlib file details. When this command is used with HSA and you do not specify the monlib-filename argument, the system takes the ROM monitor library file from the secondary image bundle. If you specify the monlib-filename argument, the system assumes that the files reside on the secondary devices. In the command syntax, the filesystem1 :argumentspecifies the device to format and the filesystem2 :argumentspecifies the optional device containing the monlib file used to format the filesystem1 :argument. The device determines which monlib file to use, as follows: • If you omit the optional filesystem2 : and monlib-filename arguments, the system formats the filesystem1 : argument using the monlib file already bundled with the system software. • If you omit only theoptional filesystem2 : argument, the system formats the filesystem1 : argumentusing the monlib file from the device you specified with the cd command. • If you omit only the optional monlib-filename argument, the system formats filesystem1 : using the filesystem2 : monlib file. • When you specify both arguments--filesystem2 : and monlib-filename-- the system formats the filesystem1 : argumentusing the monlib file from the specified device. • You can specify the filesystem1 :arguments’s own monlib file in this argument. If the system cannot find a monlib file, it terminates its formatting. Note Most platforms do not support booting from images stored on flash memory cards . You should reboot your device only from integrated memory locations, such as NVRAM. Cisco 7600 Series Router Notes The bootflash:, slot0:, sup-slot0:, and sup-bootflash: keywords are supported on Cisco 7600 series routers that are configured with a Supervisor Engine 2. Use the format command to format Class A or C flash memory file systems. • The disk0: and disk1: keywords are for Class C file systems. • The bootflash:, slot0:, sup-slot0:, and sup-bootflash: keywords are for Class A file systems. The disk0: keyword is supported on Cisco 7600 series routers that are configured with a Supervisor Engine 2 only. Cisco ASR 1000 Series Routers Notes This command is available in both privileged EXEC and diagnostic mode on the Cisco ASR 1000 Series Routers.

**Example:**

The following example shows how to format a flash memory card that is inserted in slot 0:

```text
Router# format slot0:
Running config file on this device, proceed? [confirm] y
All sectors will be erased, proceed? [confirm]
y
Enter volume id (up to 31 characters): <Return>
Formatting sector 1 (erasing)
Format device slot0 completed
```

When the console returns to the privileged EXEC prompt, the new flash memory card is formatted and ready for use. This following example shows how to format a CompactFlash PC card that is inserted in slot 0:

```text
Router# format disk0:
Running config file on this device, proceed? [confirm] y
All sectors will be erased, proceed? [confirm] y
Enter volume id (up to 31 characters): <Return>
Formatting sector 1 (erasing)
Format device disk0 completed
When the console returns to the EXEC prompt, the new CompactFlash PC card is formatted and
ready for use.
```

This follwing example shows how a format operation cleans up the disk and writes the monitor library on the disk filesystem:

```text
Router# format formatdisk:
Format operation may take a while. Continue? [confirm]
Format operation will destroy all data in "bootdisk:". Continue? [confirm]
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
Format: All system sectors written. OK...
Format: Total sectors in formatted partition: 1000881
Format: Total bytes in formatted partition: 512451072
Format: Operation completed successfully.
Format of bootdisk: complete
```


### `fsck`

> **Página:** 230 · **Modo:** Privileged EXEC (#) Diagnostic (diag) · **Default:** A FAT-based disk, flash file system, or Class C file system is not checked for damage and repaired. If you do not enter the /automatic keyword, command-line interface (CLI) prompts for actions are issued. For the Cisco 7600 series router, if you do not specify the disk0: keyword, the current file system is checked. This command is available in both privileged EXEC and diagnostic mode on the Cisco ASR1000 series routers. · **Leitura (show/clear/…):** não

**Description:** To check a File Allocation Table (FAT)-based disk, a flash file system, or a Class C file system for damage and to repair any problems, use the fsckcommand in privileged EXEC or diagnostic mode. Supported Platforms Other than the Cisco 7600 Series and Cisco ASR1000 Series Routers Cisco 7600 Series Routers Cisco ASR 1000 Series Routers / /

**Syntax:**

```text
fsck [/nocrc] [/automatic] [/all] [/force] [filesystem:]
fsck [/automatic] [/all] [/force] [filesystem:]
fsck [ all] [ force] [filesystem:]
```

**Parameters (Syntax Description):**

- `/nocrc` — ( Optional) This keyword is a v a i l a b l e for Class C flash filesystem s only. O m its c y c l i c redundancy check s( C R C s).
- `/ automatic` — ( Optional) This keyword is a v a i l a b l e for A d v an c e d Tech no log y Attach m e n t( AT A) F AT-b as e d disk s only. Specifies that the check and r e p a i r a c t i on s should p r o c e e d automatic all y. This option can be used to s k ip the prompt s for each check and r e p a i r a c t i on. Note This command also specifies the automatic mode for the Cisco7600 s e r i e s router; see the “Usage Guidelines” section for a d d it i on a l information.
- `/all` — ( Optional) Specifies that all partition s on the disk be check e d for p r o b l e m s.
- `/force` — ( Optional) E n s u r e s for c e d t e r min at i on of s i m u l t an e o u s file o p e r at i on s on the same device.
- `filesystem :` — The filesystem pref i x in d i c at in gt h e disk to be check e d. The c o l on(:) isr e q u i r e d. T y p i c all y, the filesystem pref i x will be disk0: or disk1:. In c as e of d u a l processor s, the filesystem on the r e d u n d an t supervisor e n g in e can also be specified.

**Command Default:** A FAT-based disk, flash file system, or Class C file system is not checked for damage and repaired. If you do not enter the /automatic keyword, command-line interface (CLI) prompts for actions are issued. For the Cisco 7600 series router, if you do not specify the disk0: keyword, the current file system is checked. This command is available in both privileged EXEC and diagnostic mode on the Cisco ASR1000 series routers.

**Command Modes:** Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3AA | This command was introduced. |
| 12.0(22)S | This command was i m p l e m e n t e do n the Cisco7000 f a m i l y of routers and on the Cisco10000 s e r i e s router and the Gigabit Switch Router( GSR) to support ATA disks. |
| 12.2(13)T | This command was integrated into Cisco IOS Release12.2(13) T. |
| 12.2(14)SX | This command was modified. Support for this command was added for the Supervisor E n g in e720. |
| 12.2(17d)SXB | This command was modified. Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers and the following e n h an c e m e n t s were introduced: • This command was introduced in diagnostic mode for the first time. The command can been t e r e d in both privileged EXEC and diagnostic mode on the Cisco AS R1000 s e r i e s routers. • The/ all option was introduced. • The h a r d disk:, o b f l:, s t by-h a r d disk:, s t by-usb[0-1]:, and usb[0-1]: filesystem: options were introduced. |
| 15.0(1)M | This command was modified. The/ for c e keyword was added. |

**Usage Guidelines:**

Supported Platforms Other than Cisco 7600 Series Router This command performs all steps necessary to remove corrupted files and reclaim unused disk space. Changes include checking for incorrect file sizes, cluster loops, and so on. The default form of this command issues multiple prompts to confirm each of the changes. However, you can skip these prompts by using the /automatic keyword when issuing the command. When you use the /automatickeyword you are prompted to confirm that you want the automatic option. Prompts for actions will be skipped, but all actions performed are displayed to the terminal (see the example below). This command works with ATA Personal Computer Memory Card Industry Association (PCMCIA) cards formatted in Disk Operating System (DOS), or for Class C flash file systems. Note Only one partition (the active partition) is checked in the ATA disk. Cisco 7600 Series Router The disk0: or slavedisk0: file systems are the only file systems in the Cisco 7600 series routers on which you can run the File-System-Check ( fsck) utility. The slavedisk0: file system appears in redundant supervisor engine systems only. This command is valid only on Class C flash file systems and only on PCMCIA ATA flash disks and CompactFlash disks. The output for the fsck slavedisk0: command is similar to the fsck disk0: command output. If you do not enter any arguments, the current file system is used. Use the pwd command to display the current file system. If you enter the disk0: or slavedisk0: keyword, the fsck utility checks the selected file system for problems. If a problem is detected, a prompt is displayed asking if you want the problem fixed. If you enter the /automatic keyword, you are prompted to confirm that you want the automatic mode. In automatic mode, problems are fixed automatically and you are not prompted to confirm. If you do not specify the /forcekeyword, any simultaneous file operations on the same device are not terminated. Instead, an error message stating files are open for read or write access appears. If you specify the /force keyword, the fsck utility terminates files that are open for read or write access and continues to check for problems. The table below lists the checks and actions that are performed by the fsck utility.

| Checks | Actions |
| --- | --- |
| Checksthebootsectorandthepartitiontableandreportsthe errors. | Noaction. |

Checks Actions Checks the boot sector and the partition table and reports the No action. errors.

| Checks | Actions |
| --- | --- |
| Validatesthemediawiththesignatureinthelast2bytesofthe firstsector(0x55and0xaa,respectively). | Noaction. |
| Checkstheos_idtofindwhetherthisisaFAT-12orFAT-16 filesystem(validvaluesinclude0,1,4,and6). | Noaction. |
| ChecksthenumberofFAT’sfield(correctvaluesare1and2). | Noaction. |
| Checksthesevalues: •n_fat_sectorscannotbelessthan1. •n_root_entriescannotbelessthan16. •n_root_sectorscannotbelessthan2. •base_fat_sector,n_sectors_per_cluster,n_heads, n_sectors_per_trackisnot0. | Noaction. |
| ChecksthefilesandFATfortheseerrors: | Iftheclusterisapartofafilechain,theclusterischangedtoend offile(EOF).Iftheclusterisnotpartofafilechain,itisaddedto thefreelistandunusedclusterchain.Thetablebelowlistsvalid clusternumbers;numbersotherthanthoselistedinthetablebelow areinvalidnumbers. |
| CheckstheFATforinvalidclusternumbers. |  |
| Checksthefile’sclusterchainforloops. | Iftheloopisbroken,thefileistruncatedattheclusterwherethe loopingoccurred. |
| Checksthedirectoriesfornonzerosizefields. | Ifdirectoriesarefoundwithnonzerosizefields,thesizeisreset tozero. |
| Checksforinvalidstartclusterfilenumbers. | Ifthestartclusternumberofafileisinvalid,thefileisdeleted. |
| Checksfilesforbadorfreeclusters. | Ifthefilecontainsbadorfreeclusters,thefileistruncatedatthe lastgoodcluster;anexampleistheclusterthatpointstothis bad/freecluster. |
| Checkstoseeifthefile’sclusterchainislongerthanindicated bythesizefields. | Ifthefile’sclusterchainislongerthanindicatedbythesizefields, thefilesizeisrecalculatedandthedirectoryentryisupdated. |
| Checkstoseeiftwoormorefilessharethesamecluster (crosslinked). | Iftwoormorefilesarecrosslinked,youarepromptedtoaccept therepair,andoneofthefilesistruncated. |
| Checkstoseeifthefile’sclusterchainisshorterthanisindicated bythesizefields. | Ifthefile’sclusterchainisshorterthanisindicatedbythesize fields,thefilesizeisrecalculatedandthedirectoryentryisupdated. |
| Checkstoseeifthereareanyunusedclusterchains. | Ifunusedclusterchainsarefound,newfilesarecreatedandlinked tothatfilewiththenamefsck-startcluster |

Checks Actions Validates the media with the signature in the last 2 bytes of the No action. first sector (0x55 and 0xaa, respectively). Checks the os_id to find whether this is a FAT-12 or FAT-16 No action. file system (valid values include 0, 1, 4, and 6). Checks the number of FAT’s field (correct values are 1 and 2). No action. Checks these values: No action. • n_fat_sectors cannot be less than 1. • n_root_entries cannot be less than 16. • n_root_sectors cannot be less than 2. • base_fat_sector, n_sectors_per_cluster, n_heads, n_sectors_per_track is not 0. Checks the files and FAT for these errors: Checks the FAT for invalid cluster numbers. Checks the file’s cluster chain for loops. If the loop is broken, the file is truncated at the cluster where the Checks the directories for nonzero size fields. If directories are found with nonzero size fields, the size is reset Checks for invalid start cluster file numbers. If the start cluster number of a file is invalid, the file is deleted. Checks files for bad or free clusters. If the file contains bad or free clusters, the file is truncated at the Checks to see if the file’s cluster chain is longer than indicated If the file’s cluster chain is longer than indicated by the size fields, by the size fields. the file size is recalculated and the directory entry is updated. Checks to see if two or more files share the same cluster If two or more files are crosslinked, you are prompted to accept (crosslinked). the repair, and one of the files is truncated. Checks to see if the file’s cluster chain is shorter than is indicated If the file’s cluster chain is shorter than is indicated by the size by the size fields. fields, the file size is recalculated and the directory entry is updated. Checks to see if there are any unused cluster chains. If unused cluster chains are found, new files are created and linked The table below lists the valid cluster numbers. Numbers other than those listed in the table below are invalid numbers.

| Cluster | FAT-12 | FAT-16 |
| --- | --- | --- |
| Nextentryinthechain | 2-FEF | 2-FFEF |
| Lastentryinchain | FF8-FFF | FFF8-FFFF |
| Availablecluster | 0 | 0 |
| BadCluster | FF7 | FFF7 |

**Example:**

Supported Platforms Other than the Cisco 7600 Series Router The following example shows sample output from the fsck command in automatic mode:

```text
Router# fsck /automatic disk1:
Proceed with the automatic mode? [yes] y
Checking the boot sector and partition table...
Checking FAT, Files and Directories...
Start cluster of file disk1:/file1 is invalid, removing file
File disk1:/file2 has a free/bad cluster, truncating...
File disk1:/file2 truncated.
File disk1:/file3 has a free/bad cluster, truncating...
File disk1:/file3 truncated.
File disk1:/file4 has a invalid cluster, truncating...
File disk1:/file4 truncated.
File disk1:/file5 has a invalid cluster, truncating...
File disk1:/file5 truncated.
File disk1:/file6 has a invalid cluster, truncating...
File disk1:/file6 truncated.
File size of disk1:/file7 is not correct, correcting it
File disk1:/file8 cluster chain has a loop, truncating it
File disk1:/file8 truncated.
File disk1:/file9 cluster chain has a loop, truncating it
File disk1:/file9 truncated.
File disk1:/file16 has a free/bad cluster, truncating...
File disk1:/file16 truncated.
File disk1:/file20 has a free/bad cluster, truncating...
File disk1:/file20 truncated.
Reclaiming unused space...
Created file disk1:/fsck-4 for an unused cluster chain
Created file disk1:/fsck-41 for an unused cluster chain
Created file disk1:/fsck-73 for an unused cluster chain
Created file disk1:/fsck-106 for an unused cluster chain
Created file disk1:/fsck-121 for an unused cluster chain
Created file disk1:/fsck-132 for an unused cluster chain
Created file disk1:/fsck-140 for an unused cluster chain
Created file disk1:/fsck-156 for an unused cluster chain
Created file disk1:/fsck-171 for an unused cluster chain
Created file disk1:/fsck-186 for an unused cluster chain
Created file disk1:/fsck-196 for an unused cluster chain
Created file disk1:/fsck-235 for an unused cluster chain
Created file disk1:/fsck-239 for an unused cluster chain
Updating FAT...
fsck of disk1: complete
```

Cisco 7600 Series Router This example shows how to run a check of the current file system:

```text
Router# fsck
Checking the boot sector and partition table...
Checking FAT, Files and Directories...
Files
1) disk0:/FILE3 and
2) disk0:/FILE2
have a common cluster.
Press 1/2 to truncate or any other character to ignore[confirm] q
Ignoring this error and continuing with the rest of the check...
Files
1) disk0:/FILE5 and
2) disk0:/FILE4
have a common cluster.
Press 1/2 to truncate or any other character to ignore[confirm] 1
File disk0:/FILE5 truncated.
Files
1) disk0:/FILE7 and
2) disk0:/FILE6
have a common cluster.
1) disk0:/FILE15 and
2) disk0:/FILE13
have a common cluster.
Press 1/2 to truncate or any other character to ignore[confirm] i
Ignoring this error and continuing with the rest of the check...
Reclaiming unused space...
Created file disk0:/fsck-11 for an unused cluster chain
Created file disk0:/fsck-20 for an unused cluster chain
Created file disk0:/fsck-30 for an unused cluster chain
Created file disk0:/fsck-35 for an unused cluster chain
Created file disk0:/fsck-40 for an unused cluster chain
Created file disk0:/fsck-46 for an unused cluster chain
Created file disk0:/fsck-55 for an unused cluster chain
Created file disk0:/fsck-62 for an unused cluster chain
Created file disk0:/fsck-90 for an unused cluster chain
Updating FAT...
fsck of disk0: complete
```


### `full-help`

> **Página:** 235 · **Modo:** Line configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To get help for the full set of user-level commands, use the full-help command in line configuration mode.

**Syntax:**

```text
full-help
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

The full-help command enables (or disables) an unprivileged user to see all of the help messages available. It is used with the show ? command.

**Example:**

In the following example, the show ? command is used first with full-help disabled. Then full-help is enabled for the line, and the show ? command is used again to demonstrate the additional help output that is displayed.

```text
Router> show ?
bootflash Boot Flash information
calendar Display the hardware calendar
clock Display the system clock
context Show context information
dialer Dialer parameters and statistics
history Display the session command history
hosts IP domain-name, lookup style, nameservers, and host table
isdn ISDN information
kerberos Show Kerberos Values
modemcap Show Modem Capabilities database
ppp PPP parameters and statistics
rmon rmon statistics
sessions Information about Telnet connections
snmp snmp statistics
terminal Display terminal configuration parameters
users Display information about terminal lines
version System hardware and software status
Router>
enable
Password:
<letmein>
Router# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#
line console 0
Router(config-line)# full-help
Router(config-line)# exit
%SYS-5-CONFIG_I: Configured from console by console
Router# disable
Router> show ?
access-expression List access expression
access-lists List access lists
aliases Display alias commands
apollo Apollo network information
appletalk AppleTalk information
arp ARP table
async Information on terminal lines used as router interfaces
bootflash Boot Flash information
bridge Bridge Forwarding/Filtering Database [verbose]
bsc BSC interface information
bstun BSTUN interface information
buffers Buffer pool statistics
calendar Display the hardware calendar
translate Protocol translation information
ttycap Terminal capability tables
users Display information about terminal lines
version System hardware and software status
vines VINES information
vlans Virtual LANs Information
whoami Info on current tty line
x25 X.25 information
xns XNS information
xremote XRemote statistics
```


### `help`

> **Página:** 237 · **Modo:** User EXEC Privileged EXEC All configuration modes · **Default:** No default behavior or values. · **Leitura (show/clear/…):** não

**Description:** To display a brief description of the help system, use the help command in any command mode.

**Syntax:**

```text
help
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** No default behavior or values.

**Command Modes:** User EXEC Privileged EXEC All configuration modes

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The help command provides a brief description of the context-sensitive help system, which functions as follows: • To list all commands available for a particular command mode, enter a question mark (?) at the system prompt. • To obtain a list of commands that begin with a particular character string, enter the abbreviated command entry immediately followed by a question mark (?). This form of help is called word help , because it lists only the keywords or arguments that begin with the abbreviation you entered. • To list the keywords and arguments associated with a command, enter a question mark (?) in place of a keyword or argument on the command line. This form of help is called command syntax help , because it lists the keywords or arguments that apply based on the command, keywords, and arguments you have already entered.

**Example:**

In the following example, the help command is used to display a brief description of the help system:

```text
help
Help may be requested at any point in a command by entering
a question mark '?'. If nothing matches, the help list will
be empty and you must backup until entering a '?' shows the
available options.
Two styles of help are provided:
1. Full help is available when you are ready to enter a
command argument (e.g. 'show ?') and describes each possible
argument.
2. Partial help is provided when an abbreviated argument is entered
and you want to know what arguments match the input
(e.g. 'show pr?'.)
```

The following example shows how to use word help to display all the privileged EXEC commands that begin with the letters “co.” The letters entered before the question mark are reprinted on the next command line to allow the user to continue entering the command.

```text
Router# co?
configure connect copy
Router# co
```

The following example shows how to use command syntax help to display the next argument of a partially complete access-list command. One option is to add a wildcard mask. The <cr> symbol indicates that the other option is to press Enter to execute the command without adding any more keywords or arguments. The characters entered before the question mark are reprinted on the next command line to allow the user to continue entering the command or to execute that command as it is.

```text
Router(config)# access-list 99 deny 131.108.134.234 ?
A.B.C.D Mask of bits to ignore
<cr>
Router(config)#
access-list 99 deny 131.108.134.234
```


### `hidekeys`

> **Página:** 238 · **Modo:** Configuration change logger configuration (config-archive-log-config) · **Default:** Password information is displayed. · **Leitura (show/clear/…):** não

**Description:** To suppress the display of password information in configuration log files, use the hidekeys command in configuration change logger configuration mode. To allow the display of password information in configuration log files, use the no form of this command.

**Syntax:**

```text
hidekeys
no hidekeys
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Password information is displayed.

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

Enabling the hidekeys command increases security by preventing password information from being displayed in configuration log files.

**Example:**

The following example shows how to prevent password information from being displayed in configuration log files:

```text
Device#
configure terminal
!
Device(config)# archive
Device(config-archive)# log config
Device(config-archive-log-config)# hidekeys
Device(config-archive-log-config)# end
```


### `history`

> **Página:** 240 · **Modo:** Line configuration · **Default:** Enabled with ten command lines in the buffer. · **Leitura (show/clear/…):** não

**Description:** To enable the command history function, use the history command in line configuration mode. To disable the command history function, use the no form of this command.

**Syntax:**

```text
history
no history
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Enabled with ten command lines in the buffer.

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The command history function provides a record of EXEC commands that you have entered. This function is particularly useful for recalling long or complex commands or entries, including access lists. To change the number of command lines that the system will record in its history buffer, use the history size line configuration command. The history command enables the history function with the last buffer size specified or, if there was not a prior setting, with the default of ten lines. The no history command disables the history function. The show history EXEC command will list the commands you have entered, but you can also use your keyboard to display individual commands. The table below lists the keys you can use to recall commands from the command history buffer.

| Key(s) | Functions |
| --- | --- |
| Ctrl-PorUpArrow2 | Recallscommandsinthehistorybufferinabackwardsequence,beginningwith themostrecentcommand.Repeatthekeysequencetorecallsuccessivelyolder commands. |
| Ctrl-NorDownArrow1 | Returnstomorerecentcommandsinthehistorybufferafterrecallingcommands withCtrl-PortheUpArrow.Repeatthekeysequencetorecallsuccessivelymore recentcommands. |

The arrow keys function only with ANSI-compatible terminals.

**Example:**

In the following example, the command history function is disabled on line 4:

```text
Router(config)#
line 4
Router(config-line)# no history
```


### `history size`

> **Página:** 241 · **Modo:** Line configuration · **Default:** 10 command lines · **Leitura (show/clear/…):** não

**Description:** To change the command history buffer size for a particular line, use the history size command in line configuration mode. To reset the command history buffer size to ten lines, use the no form of this command.

**Syntax:**

```text
history size number-of-lines
no history size
```

**Parameters (Syntax Description):**

- `Specifies` — the number of command lines that the system will record in its history buffer.
- `number-of-lines` — Specifies then u m be r of command lines that the system will r e c or d in its history buffer. The range is from0 to256. The default is10.

**Command Default:** 10 command lines

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The command should be used in conjunction with the and commands. The history size history show history history command enables or disables the command history function. The show history command lists the commands you have entered in the current EXEC session. The number of commands that the history buffer will show is set by the history size command. Note The history size command only sets the size of the buffer; it does not reenable the history function. If the no history command is used, the history command must be used to reenable this function.

**Example:**

The following example displays line 4 configured with a history buffer size of 35 lines:

```text
Router(config)# line 4
Router(config-line)# history size 35
```


### `hold-character`

> **Página:** 242 · **Modo:** Line configuration · **Default:** No hold character is defined. · **Leitura (show/clear/…):** não

**Description:** To define the local hold character used to pause output to the terminal screen, use the hold-character command in line configuration mode. To restore the default, use the no form of this command.

**Syntax:**

```text
hold-character ascii-number
no hold-character
```

**Parameters (Syntax Description):**

- `ascii-number` — ASCII decimal representation of a character or control sequence( for example, C t r l-P).

**Command Default:** No hold character is defined.

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The Break character is represented by zero; NULL cannot be represented. To continue the output, enter any character after the hold character. To use the hold character in normal communications, precede it with the escape character. See the “ASCII Character Set” appendix for a list of ASCII characters.

**Example:**

The following example sets the hold character to Ctrl-S, which is ASCII decimal character 19:

```text
Router(config)# line 8
Router(config-line)# hold-character 19
```


### `hostname`

> **Página:** 242 · **Modo:** Global configuration · **Default:** The default hostname is Router. · **Leitura (show/clear/…):** não

**Description:** To specify or modify the hostname for the network server, use the hostname command in global configuration mode.

**Syntax:**

```text
hostname name
```

**Parameters (Syntax Description):**

- `name` — N e who s t name for then e two r k server.

**Command Default:** The default hostname is Router.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(33)SB | This command was integrated into Cisco IOS Release12.2(33) S B. |
| 12.2(33)SXI | This command was integrated into Cisco IOS Release12.2(33) S X I. |
| CiscoIOSXERelease2.5 | This command was integrated into Cisco IOS X E Release2.5. |
| 15.0(1)M4 | This command was integrated into Cisco IOS Release15.0(1) M4 and support for n u m e r i c hostname s added. |

**Usage Guidelines:**

The hostname is used in prompts and default configuration filenames. Do not expect case to be preserved. Uppercase and lowercase characters look the same to many internet software applications. It may seem appropriate to capitalize a name the same way you might do in English, but conventions dictate that computer names appear all lowercase. For more information, refer to RFC 1178, Choosing a Name for Your Computer . The name must also follow the rules for ARPANET hostnames. They must start with a letter, end with a letter or digit, and have as interior characters only letters, digits, and hyphens. Names must be 63 characters or fewer. Creating an all numeric hostname is not recommended but the name will be accepted after an error is returned.

```text
Router(config)#hostname 123
% Hostname contains one or more illegal characters.
123(config)#
```

A hostname of less than 10 characters is recommended. For more information, refer to RFC 1035, Domain Names--Implementation and Specification . On most systems, a field of 30 characters is used for the hostname and the prompt in the CLI. Note that the length of your hostname may cause longer configuration mode prompts to be truncated. For example, the full prompt for service profile configuration mode is:

```text
(config-service-profile)#
```

However, if you are using the hostname of “Router,” you will only see the following prompt (on most systems):

```text
Router(config-service-profil)#
```

If the hostname is longer, you will see even less of the prompt:

```text
Basement-rtr2(config-service)#
```

Keep this behavior in mind when assigning a name to your system (using the hostname global configuration command). If you expect that users will be relying on mode prompts as a CLI navigation aid, you should assign hostnames of no more than nine characters. The use of a special character such as '\'(backslash) and a three or more digit number for the character setting like hostname, results in incorrect translation:

```text
Router(config)#
Router(config)#hostname \99
% Hostname contains one or more illegal characters.
```

**Example:**

The following example changes the hostname to “host1”:

```text
Router(config)# hostname host1
host1(config)#
```


### `hw-module reset`

> **Página:** 244 · **Modo:** Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** não

**Description:** To reset a module by turning the power off and then on, use the hw-module reset command in privileged EXEC mode.

**Syntax:**

```text
hw-module module num reset
```

**Parameters (Syntax Description):**

- `module n u m` — Ap p l i e s the command to as p e c if i c module; see the“ Usage Guidelines” section for v a l id values.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | This command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | This command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 12.2(31)SB2 | This command was integrated into Cisco IOS12.2(31)SB2. |

**Usage Guidelines:**

The num argument designates the module number. Valid values depend on the chassis that is used. For example, if you have a 13-slot chassis, valid values for the module number are from 1 to 13.

**Example:**

This example shows how to reload a specific module:

```text
hw-module module 3 reset
```


### `hw-module shutdown`

> **Página:** 245 · **Modo:** Privileged EXEC · **Default:** This command has no default settings. · **Leitura (show/clear/…):** não

**Description:** To shutdown the module, use the hw-module shutdown command in privileged EXEC mode.

**Syntax:**

```text
hw-module module num shutdown
```

**Parameters (Syntax Description):**

- `module n u m` — Ap p l i e s the command to as p e c if i c module; see the“ Usage Guidelines” section for v a l id values.

**Command Default:** This command has no default settings.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is supported on the SSL Services Module and the NAM. If you enter the hw-module command to shutdown the module, you will have to enter the no power shutdown enable module command and the power enable module command to restart (power down and then power up) the module.

**Example:**

This example shows how to shutdown and restart the module:

```text
Router# hw-module module 3 shutdown
Router# no power enable module 3
Router# power enable module 3
```


### `insecure`

> **Página:** 245 · **Modo:** Line configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To configure a line as insecure, use the insecure command in line configuration mode. To disable this function, use the no form of this command.

**Syntax:**

```text
insecure
no insecure
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

Use this command to identify a modem line as insecure for DEC local area transport (LAT) classification.

**Example:**

In the following example, line 10 is configured as an insecure dialup line:

```text
Router(config)# line 10
Router(config-line)# insecure
```


### `install`

> **Página:** 246 · **Modo:** Privileged EXEC (#) · **Default:** Packages are not installed. · **Leitura (show/clear/…):** não

**Description:** To install Software Maintenance Upgrade (SMU) packages, use the install command in privileged EXEC mode.

**Syntax:**

```text
install {abort | activate | file {bootflash: | flash: | harddisk: | webui:} [auto-abort-timer timer timer
prompt-level {all | none}] | add file {bootflash: | flash: | ftp: | harddisk: | http: | https: | pram: |
rcp: | scp: | tftp: | webui:} [activate [auto-abort-timer timer prompt-level {all | none}commit]] |
commit | auto-abort-timer stop | deactivate file {bootflash: | flash: | harddisk: | webui:} | label id
{description description | label-name name} | remove {file {bootflash: | flash: | harddisk: | webui:}
| inactive } | rollback to {base | committed | id {install-ID } | label {label-name}}}
```

**Parameters (Syntax Description):**

- `abort` — Aborts the current install o p e r at i on.
- `activate` — V a l ida t e s whether the SMU is added through the
- `install` — add command. This keyword runs a c o m p at i b i l it y check, updates
- `package` — status, and if the package can be restart e d,
- `it` — t r i g g e r s p o s t-install scripts to restart the n e c e s s a r y processes, or t r i g g e r s a reload for no n-restart a b l e package s.
- `file` — Specifies the package to be activated. { bootflash: | flash: | h a r d disk: | webui:} Specifies the location of the install e d package.
- `auto-abort-timer` — timer ( Optional) Install s an auto-a b or t timer. The timer is set by the activate keyword and
- `removed` — by the commit keyword. After the expiry
- `of` — the install auto-a b or t timer command, a device
- `can` — be rolled back to a stage before the install
- `commit` — command is used.
- `prompt-level` — {all | none} ( Optional) Prompts the user about install at i on a c t i v it i e s.
- `For` — example, the activate keyword, automatic all y
- `t r i g g e r s` — a reload for package s that require a reload.
- `Before` — a c t i v at in g the package, a message will
- `prompt` — users as to whether they want to continue. The all keyword allows you to enable prompts. The
- `none` — keyword disable prompts.
- `add` — Copies files from a remote location (via FTP, TFTP)
- `to` — a device and perf or m s Software M a in t e n an c e
- `Upgrade` — (SMU) c o m p at i b i l it y check for the platform
- `and` — image version s. This keyword runs base c o m p at i b i l it y checks to
- `ensure` — that a specified package is supported on a platform. It also adds an entry in the package file,
- `so` — that the status can be monitor e d and m a in t a in e d. { bootflash: | flash: |ftp: | h a r d disk: |http: |https: | Specifies the package to be added. pram: |rcp: | scp: | tftp: |webui:}
- `commit` — Makes SMU changes persistent over reloads.
- `You` — can do a commit after a c t i v at in g a package,
- `while` — the system is up, or after the first reload. If a
- `package` — is activated, but not commit t e d, it remains
- `active` — after the first reload, but not after the second reload.
- `auto-abort-timer` — stop Stops the auto-abort timer.
- `If` — the rollback timer is not stopped through the command, the device rolls back to an older software
- `version` — when rollback timer expires. Default:120 minutes.
- `d e activate` — D e activate s an install e d package.
- `D e a c t i v at in g` — a package also updates the package
- `status` — and t r i g g e r s a process restart or a reload.
- `label` — id Specifies the id of the install point to label.
- `description` — Adds a description to specified install point.
- `label-name` — name Adds a description to specified install point.
- `remove` — Remove install e d package s. The package file is removed from the file system. The remove keyword can only be used on package s
- `that` — are current l y in a c t i v e.
- `in a c t i v e` — Removes all in a c t i v e package s from the device.
- `rollback` — Rollback s the SMU package to the base version, the
- `last` — commit t e d version, or a known commit ID.
- `to` — base Returns to the base image.
- `commit t e d` — Returns to the install at i on state when the last commit
- `o p e r at i on` — was perf or m e d.
- `id` — install-ID Returns to the s p e c if i c install point ID.
- `Valid` — values are from 1 to 4294967295.

**Command Default:** Packages are not installed.

**Command Modes:** Privileged EXEC (#)

**Usage Guidelines:**

An SMU is a package that can be installed on a system to provide a patch fix or security resolution to a released image. This package contain a minimal set of files for patching the release along with some metadata that describes the contents of the package. Packages must be added prior to activating the SMU. A package must be deactivated, before it is removed from the device. Example The following example shows how to add an install package on a device:

```text
Device# install add file tftp://172.16.0.1//tftpboot/folder1/isr4300-
universalk9.2017-01-10_13.15.1.CSCxxx.SSA.dmp.bin
install_add: START Sun Feb 26 05:57:04 UTC 2017
Downloading file tftp://172.16.0.1//tftpboot/folder1/isr4300-universalk9.2017-01-10_13.15.1.
CSCvb12345.SSA.dmp.bin
Finished downloading file
tftp://172.16.0.1//tftpboot/folder1/isr4300-universalk9.2017-01-10_13.15.1.
CSCvb12345.SSA.dmp.bin to
bootflash:isr4300-universalk9.2017-01-10_13.15.1.CSCvb12345.SSA.dmp.bin
SUCCESS: install_add /bootflash/isr4300-universalk9.2017-01-10_13.15.1.CSCvb12345.SSA.dmp.bin
Sun Feb 26 05:57:22 UTC 2017
```

The following example shows how to activate an install package:

```text
Device# install activate file bootflash:isr4300-universalk9.2017-01-10_13.15.1.
CSCxxx.SSA.dmp.bin
install_activate: START Sun Feb 26 05:58:41 UTC 2017
DMP package.
Netconf processes stopped
SUCCESS: install_activate
/bootflash/isr4300-universalk9.2017-01-10_13.15.1.CSCvb12345.SSA.dmp.bin
Sun Feb 26 05:58:58 UTC 2017
*Feb 26 05:58:47.655: %DMI-4-CONTROL_SOCKET_CLOSED: SIP0: nesd:
Confd control socket closed Lost connection to ConfD (45): EOF on socket to ConfD.
*Feb 26 05:58:47.661: %DMI-4-SUB_READ_FAIL: SIP0: vtyserverutild:
Confd subscription socket read failed Lost connection to ConfD (45):
EOF on socket to ConfD.
*Feb 26 05:58:47.667: %DMI-4-CONTROL_SOCKET_CLOSED: SIP0: syncfd:
Confd control socket closed Lost connection to ConfD (45): EOF on socket to ConfD.
*Feb 26 05:59:43.269: %DMI-5-SYNC_START: SIP0: syncfd:
External change to running configuration detected.
The running configuration will be synchronized to the NETCONF running data store.
*Feb 26 05:59:44.624: %DMI-5-SYNC_COMPLETE: SIP0: syncfd:
The running configuration has been synchronized to the NETCONF running data store.
```

The following example shows how to commit an installed package:

```text
Device# install commit
install_commit: START Sun Feb 26 06:46:48 UTC 2017
SUCCESS: install_commit Sun Feb 26 06:46:52 UTC 2017
```

The following example shows how to rollback to the base SMU package:

```text
Device# install rollback to base
install_rollback: START Sun Feb 26 06:50:29 UTC 2017
7 install_rollback: Restarting impacted processes to take effect
7 install_rollback: restarting confd
*Feb 26 06:50:34.957: %DMI-4-CONTROL_SOCKET_CLOSED: SIP0: syncfd:
Confd control socket closed Lost connection to ConfD (45): EOF on socket to ConfD.
*Feb 26 06:50:34.962: %DMI-4-CONTROL_SOCKET_CLOSED: SIP0: nesd:
Confd control socket closed Lost connection to ConfD (45): EOF on socket to ConfD.
*Feb 26 06:50:34.963: %DMI-4-SUB_READ_FAIL: SIP0: vtyserverutild:
Confd subscription socket read failed Lost connection to ConfD (45):
EOF on socket to ConfD.Netconf processes stopped
7 install_rollback: DMP activate complete
SUCCESS: install_rollback Sun Feb 26 06:50:41 UTC 2017
*Feb 26 06:51:28.901: %DMI-5-SYNC_START: SIP0: syncfd:
External change to running configuration detected.
The running configuration will be synchronized to the NETCONF running data store.
*Feb 26 06:51:30.339: %DMI-5-SYNC_COMPLETE: SIP0: syncfd:
The running configuration has been synchronized to the NETCONF running data store.
```


### `international`

> **Página:** 249 · **Modo:** Line configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** If you are using Telnet to access a Cisco IOS platform and you want to display 8-bit and multibyte international characters (for example, Kanji) and print the Escape character as a single character instead of as the caret and bracket symbols (^[), use the international command in line configuration mode. To display characters in 7-bit format, use the no form of this command.

**Syntax:**

```text
international
no international
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Disabled

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If you are configuring a Cisco IOS platform using the Cisco web browser user interface (UI), this function is enabled automatically when you enable the Cisco web browser UI using the ip http server global configuration command.

**Example:**

The following example enables a Cisco IOS platform to display 8-bit and multibyte characters and print the Escape character as a single character instead of as the caret and bracket symbols (^[) when you are using Telnet to access the platform:

```text
line vty 4
international
```


### `ip bootp server`

> **Página:** 250 · **Modo:** Global configuration · **Default:** Enabled · **Leitura (show/clear/…):** não

**Description:** To enable the Bootstrap Protocol (BOOTP) service on your routing device, use the ip bootp server command in global configuration mode. To disable BOOTP services, use the no form of the command.

**Syntax:**

```text
ip bootp server
no ip bootp server
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Enabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2 | This command was introduced. |
| 12.0(1)T | The D H C P r e l a y age n t and D H C P server f e at u r e s were introduced. BOOTP for w a r d in g is no w h and l e d by the D H C P r e l a y age n t i m p l e m e n t at i on. |
| 12.2(8)T | The ip d h c p bootp i g nor e command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

By default, the BOOTP service is enabled. When disabled, the no ip bootp server command will appear in the configuration file. The integrated Dynamic Host Configuration Protocol (DHCP) server was introduced in Cisco IOS Release 12.0(1)T. Because DHCP is based on BOOTP, both of these services share the “well-known” UDP server port of 67 (per RFC 951, RFC 1534, and RFC 2131; the client port is 68). To disable DHCP services (DHCP relay and DHCP server), use the no service dhcp command. To disable BOOTP services (in releases 12.2(8)T and later), but leave DHCP services enabled, use the ip dhcp bootp ignore command. If both the BOOTP server and DHCP server are disabled, “ICMP port unreachable” messages will be sent in response to incoming requests on port 67, and the original incoming packet will be discarded. If DHCP is enabled, using the no ip bootp server command by itself will not stop the router from listening on UDP port 67. Note As with all minor services, the async line BOOTP service should be disabled on your system if you do not have a need for it in your network. Any network device that has User Data Protocol (UDP), TCP, BOOTP, DHCP, or Finger services should be protected by a firewall or have the services disabled to protect against Denial of Service attacks.

**Example:**

In the following example, BOOTP and DHCP services are disabled on the router:

```text
Router(config)# no ip bootp server
Router(config)# no service dhcp
```


### `ip finger`

> **Página:** 251 · **Modo:** Global configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To configure a system to accept Finger protocol requests (defined in RFC 742), use the ip finger command in global configuration mode. To disable this service, use the noform of this command.

**Syntax:**

```text
ip finger [rfc-compliant]
no ip finger
```

**Parameters (Syntax Description):**

- `rfc-compliant` — ( Optional) Configure s the system to wait for“ Return” or“/ W” in p u t when process in g Finger request s. This keywords h o u l d not be used for those systems.

**Command Default:** Disabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3 | This command was introduced. |
| 12.1(5), 12.1(5)T | This command was changed from being enabled by default to being disabled by default. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The Finger service allows remote users to view the output equivalent to the show users [wide] command. When ip finger is configured, the router will respond to a telnet a.b.c.d finger command from a remote host by immediately displaying the output of the show userscommand and then closing the connection. When the ip finger rfc-compliantcommandis configured, the router will wait for input before displaying anything (as required by RFC 1288). The remote user can then enter the Return key to display the output of the show users EXEC command, or enter /W to display the output of the show users wide EXEC command. After this information is displayed, the connection is closed. Note As with all minor services, the Finger service should be disabled on your system if you do not have a need for it in your network. Any network device that has UDP, TCP, BOOTP, or Finger services should be protected by a firewall or have the services disabled to protect against Denial of Service attacks. Because of the potential for hung lines, the rfc-compliantform of this command should not be configured for devices with more than 20 simultaneous users.

**Example:**

The following example disables the Finger protocol:

```text
Router(config)# no ip finger
```


### `ip ftp passive`

> **Página:** 252 · **Modo:** Global configuration · **Default:** All types of FTP connections are allowed. · **Leitura (show/clear/…):** não

**Description:** To configure the router to use only passive FTP connections, use the ip ftp passivecommand in global configuration mode . To allow all types of FTP connections, use the noform of this command.

**Syntax:**

```text
ip ftp passive
no ip ftp passive
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** All types of FTP connections are allowed.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

In the following example, the router is configured to use only passive FTP connections:

```text
Router(config)# ip ftp passive
```


### `ip ftp password`

> **Página:** 253 · **Modo:** Global configuration · **Default:** The router forms a password username@routername.domain. The variable username is the username associated with the current session, routername is the configured host name, and domain is the domain of the router. · **Leitura (show/clear/…):** não

**Description:** To specify the password to be used for File Transfer Protocol (FTP) connections, use the ip ftp passwordcommand in global configuration mode. To return the password to its default, use the no form of this command.

**Syntax:**

```text
ip ftp password [type] password
no ip ftp password
```

**Parameters (Syntax Description):**

- `type` — ( Optional) Type of e n c r y p t i on to use on the password. A value of 0 disable s e n c r y p t i on. A value
- `type` — ( Optional) Type of e n c r y p t i onto use on the password. A value of0 disable s e n c r y p t i on. Avalue of7 in d i c at e s p r o p r i e tar y e n c r y p t i on.
- `password` — Password to use for FTP connection s.

**Command Default:** The router forms a password username@routername.domain. The variable username is the username associated with the current session, routername is the configured host name, and domain is the domain of the router.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. Note Any software that supports RFC1738 does not allow user name, path, or filename with pattern %xy, where (where x and y are any two hexa values 0-f, 0-F) |

**Example:**

The following example configures the router to use the username “red” and the password “blue” for FTP connections:

```text
Router(config)# ip ftp username red
Router(config)# ip ftp password blue
```


### `ip ftp source-interface`

> **Página:** 254 · **Modo:** Global configuration (config) · **Default:** The FTP source address is the IP address of the interface that the FTP packets use to leave the router. · **Leitura (show/clear/…):** não

**Description:** To specify the source IP address for File Transfer Protocol (FTP) connections, use the ip ftp source-interfacecommand in global configuration mode. To use the address of the interface where the connection is made, use the no form of this command.

**Syntax:**

```text
ip ftp source-interface interface-type interface-number
no ip ftp source-interface
```

**Parameters (Syntax Description):**

- `interface-typeinterface-number` — The interface type and number to use to o b t a in the source address for FTP connection s.

**Command Default:** The FTP source address is the IP address of the interface that the FTP packets use to leave the router.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.3(6) | Destination address lookup in a Virtual Private Network( V P N) r out in g and for w a r d in g( VRF) t a b l e was added for the t r an s f e r of FTP p a c k e t s. |
| 12.3(8)T | This command was integrated into Cisco IOS Release12.3(8) T. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to set the same source address for all FTP connections. In Cisco IOS 12.3(6) and later releases, FTP is VRF-aware, which means that FTP transfer is supported across an interface within a VRF instance. To specify a VRF as a source for FTP connections, the VRF must be associated with the same interface that you configure with the ip ftp source-interface command. In this configuration, FTP looks for the destination IP address for file transfer in the specified VRF table. If the specified source interface is not up, Cisco IOS software selects the address of the interface closest to the destination as the source address.

**Example:**

The following example shows how to configure the router to use the IP address associated with Ethernet interface 0 as the source address on all FTP packets, regardless of which interface is actually used to send the packet:

```text
Router>
enable
Router# configure terminal
Router(config)# ip ftp source-interface ethernet 0
```

The following example shows how to configure the router to use the VRF table named vpn1 to look for the destination IP address for the transfer of FTP packets:

```text
Router# configure terminal
Router(config)# ip ftp source-interface ethernet 0
Router(config)# ip vrf vpn1
Router(config-vrf)# rd 200:1
Router(config-vrf)#
route-target both 200:1
Router(config-vrf)#
interface ethernet 0
Router(config-if)# ip vrf forwarding vpn1
Router(config-if)# end
```


### `ip ftp username`

> **Página:** 255 · **Modo:** Global configuration · **Default:** The Cisco IOS software attempts an anonymous FTP. · **Leitura (show/clear/…):** não

**Description:** To configure the username for File Transfer Protocol (FTP) connections, use the ip ftp usernamecommand in global configuration mode . To configure the router to attempt anonymous FTP, use the noform of this command.

**Syntax:**

```text
ip ftp username username
no ip ftp username
```

**Parameters (Syntax Description):**

- `username` — Username for FTP connection s.

**Command Default:** The Cisco IOS software attempts an anonymous FTP.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The remote username must be associated with an account on the destination server.

**Example:**

In the following example, the router is configured to use the username “red” and the password “blue”for FTP connections:

```text
Router(config)# ip ftp username red
Router(config)# ip ftp password blue
```


### `ip rarp-server`

> **Página:** 256 · **Modo:** Interface configuration · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To enable the router to act as a Reverse Address Resolution Protocol (RARP) server, use the ip rarp-server command in interface configuration mode. To restore the interface to the default of no RARP server support, use the noform of this command.

**Syntax:**

```text
ip rarp-server ip-address
no ip rarp-server ip-address
```

**Parameters (Syntax Description):**

- `ip-address` — IP address that is to be p r o v id e d in the source p r o to c o l address f i e l do f the RARP response packet. Nor m all y, this is set to what e v e r address you configure as the p r i m a r y address for the interface.

**Command Default:** Disabled

**Command Modes:** Interface configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This feature makes diskless booting of clients possible between network subnets where the client and server are on separate subnets. RARP server support is configurable on a per-interface basis, so that the router does not interfere with RARP traffic on subnets that need no RARP assistance. The Cisco IOS software answers incoming RARP requests only if both of the following two conditions are met: • The ip rarp-server command has been configured for the interface on which the request was received. • A static entry is found in the IP ARP table that maps the MAC address contained in the RARP request to an IP address. Use the show ip arp EXEC command to display the contents of the IP ARP cache. Sun Microsystems, Inc. makes use of RARP and UDP-based network services to facilitate network-based booting of SunOS on it’s workstations. By bridging RARP packets and using both the ip helper-address interface configuration command and the ip forward-protocol global configuration command, the Cisco IOS software shouldbe able to perform the necessary packet switching to enable booting of Sun workstations across subnets. Unfortunately, some Sun workstations assume that the sender of the RARP response, in this case the router, is the host that the client can contact to TFTP load the bootstrap image. This causes the workstations to fail to boot. By using the ip rarp-server command, the Cisco IOS software can be configured to answer these RARP requests, and the client machine should be able to reach its server by having its TFTP requests forwarded through the router that acts as the RARP server. In the case of RARP responses to Sun workstations attempting to diskless boot, the IP address specified in the ip rarp-server interface configuration command should be the IP address of the TFTP server. In addition to configuring RARP service, the Cisco IOS software must be configured to forward UDP-based Sun portmapper requests to completely support diskless booting of Sun workstations. This can be accomplished using configuration commands of the following form:

```text
ip forward-protocol udp 111
interface
interface name
ip helper-address
target-address
```

RFC 903 documents the RARP.

**Example:**

The following partial example configures a router to act as a RARP server. The router is configured to use the primary address of the specified interface in its RARP responses.

```text
arp 172.30.2.5 0800.2002.ff5b arpa
interface ethernet 0
ip address 172.30.3.100 255.255.255.0
ip rarp-server 172.30.3.100
```

In the following example, a router is configured to act as a RARP server, with TFTP and portmapper requests forwarded to the Sun server:

```text
! Allow the router to forward broadcast portmapper requests
ip forward-protocol udp 111
! Provide the router with the IP address of the diskless sun
arp 172.30.2.5 0800.2002.ff5b arpa
interface ethernet 0
! Configure the router to act as a RARP server, using the Sun Server's IP
! address in the RARP response packet.
ip rarp-server 172.30.3.100
! Portmapper broadcasts from this interface are sent to the Sun Server.
ip helper-address 172.30.3.100
```


### `ip rcmd domain-lookup`

> **Página:** 258 · **Modo:** Global configuration · **Default:** Enabled · **Leitura (show/clear/…):** não

**Description:** To reena ble the basic Domain Name Service (DNS) security check for rcp and rsh, use the ip rcmd domain-lookupcommand in global configuration mode. To disable the basic DNS security check for remote copy protocol (rcp) and remote shell protoco (rsh), use the no form of this command.

**Syntax:**

```text
ip rcmd domain-lookup
no ip rcmd domain-lookup
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Enabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The abbreviation RCMD (remote command) is used to indicate both rsh and rcp. DNS lookup for RCMD is enabled by default (provided general DNS services are enabled on the system using the ip domain-lookupcommand). The no ip rcmd domain-lookup command is used to disable the DNS lookup for RCMD. The ip rcmd domain-lookup command is used to reenable the DNS lookup for RCMD. DNS lookup for RCMD is performed as a basic security check. This check is performed using a host authentication process. When enabled, the system records the address of the requesting client. That address is mapped to a host name using DNS. Then a DNS request is made for the IP address for that host name. The IP address received is then checked against the original requesting address. If the address does not match with any of the addresses received from DNS, the RCMD request will not be serviced. This reverse lookup is intended to help protect against spoofing. However, please note that the process only confirms that the IP address is a valid “routable” address; it is still possible for a hacker to spoof the valid IP address of a known host. The DNS lookup is done after the TCP handshake but before the router (which is acting as a rsh/rcp server) sends any data to the remote client. The no ip rcmd domain-lookup will turn off DNS lookups for rsh and rcp only. The no ip domain-lookup command takes precedence over the ip rcmd domain-lookupcommand. This means that if the no ip domain-lookup command is in the current configuration, DNS will be bypassed for rcp and rsh even if the ip rcmd domain-lookup command is enabled.

**Example:**

In the following example, the DNS security check is disabled for RCMD (rsh/rcp):

```text
Router(config)# no ip rcmd domain-lookup
```


### `ip rcmd rcp-enable`

> **Página:** 259 · **Modo:** Global configuration · **Default:** To ensure security, the router is not enabled for rcp by default. · **Leitura (show/clear/…):** não

**Description:** To configure the Cisco IOS software to allow remote users to copy files to and from the router using remote copy protocol (rcp), use the ip rcmd rcp-enable command in global configuration mode. To disable rcp on the device, use the no form of this command.

**Syntax:**

```text
ip rcmd rcp-enable
no ip rcmd rcp-enable
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** To ensure security, the router is not enabled for rcp by default.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

To allow a remote user to execute rcp commands on the router, you must also create an entry for the remote user in the local authentication database using the ip rcmd remote-host command. The no ip rcmd rcp-enable command does not prohibit a local user from using rcp to copy system images and configuration files to and from the router. To protect against unauthorized users copying the system image or configuration files, the router is not enabled for rcp by default.

**Example:**

In the following example, the rcp service is enabled on the system, the IP address assigned to the Loopback0 interface is used as the source address for outbound rcp and rsh packets, and access is granted to the user “netadmin3”on the remote host 172.16.101.101:

```text
Router(config)# ip rcmd rcp-enable
Router(config)# ip rcmd source-interface Loopback0
Router(config)#
ip rcmd remote-host router1 172.16.101.101 netadmin3
```


### `ip rcmd remote-host`

> **Página:** 260 · **Modo:** Global configuration · **Default:** No entries are in the local authentication database. · **Leitura (show/clear/…):** não

**Description:** To create an entry for the remote user in a local authentication database so that remote users can execute commands on the router using remote shell protocol (rsh) or remote copy protocol (rcp), use the ip rcmd remote-host command in global configuration mode. To remove an entry for a remote user from the local authentication database, use the no form of this command.

**Syntax:**

```text
ip rcmd remote-host local-username {ip-addresshost-name} remote-username [enable [level]]
no ip rcmd remote-host local-username {ip-addresshost-name} remote-username [enable [level]]
```

**Parameters (Syntax Description):**

- `local-username` — Name of the user on the l o c a l router. You can specify the router name as the username. This name n e e d s to be c o m m u n i c at e d to then e two r k a d min is t r at or or to the user on the remote system. To be all o we d to remote l y execute commands on the router, the remote user must specify this value c or r e c t l y.
- `ip-address` — IP address of the remote host from which the l o c a l router will accept remote l y execute d commands. E it h e r the IP address or the hostname isr e q u i r e d.
- `host-name` — Name of the remote host from which the l o c a l router will accept remote l y execute d commands. E it h e r the hostname or the IP address isr e q u i r e d.
- `remote-username` — Name of the user on the remote host from which the router will accept remote l y execute d commands.
- `enable [level]` — ( Optional) Enable s the remote user to execute privileged EXEC commands using rsh or to copy files to the router using rcp. The range is from1 to15. The default is15. For information on the enable level, r e f e r to the privilege level global configuration command inthe Release12.2 Cisco IOS S e c u r it y Command R e f e r e n c e.

**Command Default:** No entries are in the local authentication database.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

A TCP connection to a router is established using an IP address. Using the host name is valid only when you are initiating an rcp or rsh command from a local router. The host name is converted to an IP address using DNS or host-name aliasing. To allow a remote user to execute rcp or rsh commands on a local router, you must create an entry for the remote user in the local authentication database. You must also enable the router to act as an rsh or rcp server. To enable the router to act as an rsh server, issue the ip rcmd rsh-enable command. To enable the router to act as an rcp server, issue the ip rcmd rcp-enable command.The router cannot act as a server for either of these protocols unless you explicitly enable the capacity. A local authentication database, which is similar to a UNIX .rhosts file, is used to enforce security on the router through access control. Each entry that you configure in the authentication database identifies the local user, the remote host, and the remote user. To permit a remote user of rsh to execute commands in privileged EXEC mode or to permit a remote user of rcp to copy files to the router, specify the enable keyword and level. For information on the enable level, refer to the privilege level global configuration command in the Release 12.2 Cisco IOS Security Command Reference. An entry that you configure in the authentication database differs from an entry in a UNIX .rhostsfile in the following aspect. Because the .rhosts file on a UNIX system resides in the home directory of a local user account, an entry in a UNIX .rhosts file need not include the local username; the local username is determined from the user account. To provide equivalent support on a router, specify the local username along with the remote host and remote username in each authentication database entry that you configure. For a remote user to be able to execute commands on the router in its capacity as a server, the local username, host address or name, and remote username sent with the remote client request must match values configured in an entry in the local authentication file. A remote client host should be registered with DNS. The Cisco IOS software uses DNS to authenticate the remote host’s name and address. Because DNS can return several valid IP addresses for a host name, the Cisco IOS software checks the address of the requesting client against all of the IP addresses for the named host returned by DNS. If the address sent by the requester is considered invalid, that is, it does not match any address listed with DNS for the host name, then the software will reject the remote-command execution request. Note that if no DNS servers are configured for the router, then that device cannot authenticate the host in this manner. In this case, the Cisco IOS software sends a broadcast request to attempt to gain access to DNS services on another server. If DNS services are not available, you must use the no ip domain-lookup command to disable the attempt to gain access to a DNS server by sending a broadcast request. If DNS services are not available and, therefore, you bypass the DNS security check, the software will accept the request to remotely execute a command only if all three values sent with the request match exactly the values configured for an entry in the local authentication file.

**Example:**

The following example allows the remote user named netadmin3 on a remote host with the IP address 172.16.101.101 to execute commands on router1 using the rsh or rcp protocol. User netadmin3 is allowed to execute commands in privileged EXEC mode.

```text
Router(config)# ip rcmd remote-host router1 172.16.101.101 netadmin3 enable
```


### `ip rcmd remote-username`

> **Página:** 262 · **Modo:** Global configuration · **Default:** If you do not issue this command, the Cisco IOS software sends the remote username associated with the current tty process, if that name is valid, for rcp copy commands. For example, if the user is connected to the router through Telnet and the user was authenticated through the usernamecommand, then the software sends that username as the remote username. Note The remote username must be associated with an account on the destination server. If the username for the current tty process is not valid, the Cisco IOS software sends the host name as the remote username. For rcp boot commands, the Cisco IOS software sends the access server host name by default. For Cisco, tty lines are commonly used for access services. The concept of tty originated with UNIX. For UNIX systems, each physical device is represented in the file system. Terminals are called tty devices (tty stands for teletype, the original UNIX terminal). · **Leitura (show/clear/…):** não

**Description:** To configure the remote username to be used when requesting a remote copy using remote copy protocol (rcp), use the ip rcmd remote-usernamecommand in global configuration mode . To remove from the configuration the remote username, use the noform of this command.

**Syntax:**

```text
ip rcmd remote-username username
no ip rcmd remote-username username
```

**Parameters (Syntax Description):**

- `username` — Name of the remote user on these r v e r. This name is used for rcp copy request s. All files and image s to be c o p i e d are s e a r c h e d for or w r it t e n r e l at i v e to the directory of the remote user’ s a c count, if these r v e r has a directory s t r u c t u r e, for example, as do U N I X systems.

**Command Default:** If you do not issue this command, the Cisco IOS software sends the remote username associated with the current tty process, if that name is valid, for rcp copy commands. For example, if the user is connected to the router through Telnet and the user was authenticated through the usernamecommand, then the software sends that username as the remote username. Note The remote username must be associated with an account on the destination server. If the username for the current tty process is not valid, the Cisco IOS software sends the host name as the remote username. For rcp boot commands, the Cisco IOS software sends the access server host name by default. For Cisco, tty lines are commonly used for access services. The concept of tty originated with UNIX. For UNIX systems, each physical device is represented in the file system. Terminals are called tty devices (tty stands for teletype, the original UNIX terminal).

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The rcp protocol requires that a client send the remote username on an rcp request to the server. Use this command to specify the remote username to be sent to the server for an rcp copy request. If the server has a directory structure, as do UNIX systems, all files and images to be copied are searched for or written relative to the directory of the remote user’s account. Note Cisco IOS Release 10.3 added the ip keyword to rcmd commands. If you are upgrading from Release 10.2 to Release 10.3 or a later release, this keyword is automatically added to any rcmd commands you have in your Release 10.2 configuration files.

**Example:**

The following example configures the remote username to netadmin1:

```text
Router(config)# ip rcmd remote-username netadmin1
```


### `ip rcmd rsh-enable`

> **Página:** 263 · **Modo:** Global configuration · **Default:** To ensure security, the router is not enabled for rsh by default. · **Leitura (show/clear/…):** não

**Description:** To configure the router to allow remote users to execute commands on it using remote shell protocol (rsh), use the ip rcmd rsh-enable command in global configuration mode. To disable a router that is enabled for rsh, use the no form of this command.

**Syntax:**

```text
ip rcmd rsh-enable
no ip rcmd rsh-enable
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** To ensure security, the router is not enabled for rsh by default.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

rsh, used as a client process, gives users the ability to remotely get router information (such as status) without the need to connect into the router and then disconnect. This is valuable when looking at many statistics on many different routers. Use this command to enable the router to receive rsh requests from remote users. In addition to issuing this command, you must create an entry for the remote user in the local authentication database to allow a remote user to execute rsh commands on the router. The no ip rcmd rsh-enable command does not prohibit a local user of the router from executing a command on other routers and UNIX hosts on the network using rsh. The no form of this command only disables remote access to rsh on the router.

**Example:**

The following example enables a router as an rsh server:

```text
Router(config)#
ip rcmd rsh-enable
```


### `ip rcmd source-interface`

> **Página:** 264 · **Modo:** Global configuration · **Default:** The address of the interface closest to the destination is used as the source interface for rcp/rsh communications. · **Leitura (show/clear/…):** não

**Description:** To force remote copy protocol (rcp) or remote shell protocol (rsh) to use the IP address of a specified interface for all outgoing rcp/rsh communication packets, use the ip rcmd source-interface command in global configuration mode. To disable a previously configured ip rcmd source-interface command, use the no form of this command.

**Syntax:**

```text
ip rcmd source-interface interface-id
no ip rcmd source-interface interface-id
```

**Parameters (Syntax Description):**

- `interface-id` — Then a m e and number used to id e n t if y the interface. For example, L o o p b a c k2.

**Command Default:** The address of the interface closest to the destination is used as the source interface for rcp/rsh communications.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If this command is not used, or if the interface specified in this command is not available (not up), the Cisco IOS software uses the address of the interface closest to the destination as the source address. Use this command to force the system to tag all outgoing rcp/rsh packets with the IP address associated with the specified interface. This address is used as the source address as long as the interface is in the up state. This command is especially useful in cases where the router has many interfaces, and you want to ensure that all rcp and/or rsh packets from this router have the same source IP address. A consistent address is preferred so that the other end of the connection (the rcp/rsh server or client) can maintain a single session. The other benefit of a consistent address is that an access list can be configured on the remote device. The specified interface must have an IP address associated with it. If the specified interface does not have an IP address or is in a down state, then rcp/rsh reverts to the default. To avoid this, add an IP address to the subinterface or bring the interface to the up state.

**Example:**

In the following example, Loopback interface 0 is assigned an IP address of 220.144.159.200, and the ip rcmd source-interface command is used to specify that the source IP address for all rcp/rsh packets will be the IP address assigned to the Loopback0 interface: interface Loopback0 description Loopback interface ip address 220.144.159.200 255.255.255.255 no ip directed-broadcast ! clock timezone GMT 0 ip subnet-zero no ip source-route no ip finger ip rcmd source-interface Loopback0 ip telnet source-interface Loopback0 ip tftp source-interface Loopback0 ip ftp source-interface Loopback0 ip ftp username cisco ip ftp password shhhhsecret no ip bootp server ip domain-name net.galaxy ip name-server 220.144.159.1 ip name-server 220.144.159.2 ip name-server 219.10.2.1 !


### `ip telnet source-interface`

> **Página:** 266 · **Modo:** Global configuration · **Default:** The address of the closest interface to the destination is the source address. · **Leitura (show/clear/…):** não

**Description:** To specify the IP address of an interface as the source address for Telnet connections, use the ip telnet source-interface command in global configuration mode. To reset the source address to the default for each connection, use the no form of this command.

**Syntax:**

```text
ip telnet source-interface interface
no ip telnet source-interface
```

**Parameters (Syntax Description):**

- `interface` — The interface who s e address is to be used as the source for Telnet connection s.

**Command Default:** The address of the closest interface to the destination is the source address.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to set the IP address of an interface as the source for all Telnet connections. If the specified interface is not up, the Cisco IOS software selects the address of the interface closest to the destination as the source address.

**Example:**

The following example forces the IP address for Ethernet interface 1 as the source address for Telnet connections :

```text
Router(config)# ip telnet source-interface Ethernet1
```


### `ip tftp blocksize`

> **Página:** 266 · **Modo:** Global configuration (config) · **Default:** The default TFTP blocksize is 512 bytes. · **Leitura (show/clear/…):** não

**Description:** To negotiate a transfer TFTP blocksize, use the ip tftp blocksize command in global configuration mode. To disable this configuration, use the no form of this command.

**Syntax:**

```text
ip tftp blocksize bytes
no ip tftp blocksize
```

**Parameters (Syntax Description):**

- `bytes` — Size of the TFTP b lock, in by t e s. The range is from512 to8192.

**Command Default:** The default TFTP blocksize is 512 bytes.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2S | This command was introduced for the12.2 S releases. |
| 15.1(1)SG | This command was integrated into the15.1(1) S G releases. |
| CiscoIOSXERelease3.3SE | This command was integrated into the Cisco IOS X E Release3.3 S E releases. |

**Example:**

The following example shows how to set a 1024 byte TFTP blocksize:

```text
Router> enable
Router# configure terminal
Router(config)#
ip tftp bblocksize 1024
```


### `ip tftp boot-interface`

> **Página:** 267 · **Modo:** Global configuration (config) · **Default:** No interface is used for TFTP booting. · **Leitura (show/clear/…):** não

**Description:** To use an interface for TFTP booting, use the ip tftp boot-interfacecommand in global configuration mode. To disable this configuration, use the no form of this command.

**Syntax:**

```text
ip tftp boot-interface type number
no ip tftp boot-interface
```

**Parameters (Syntax Description):**

- `type` — The type of the interface to be used. You can c h o o s e from a list of interfaces.
- `number` — The related interface number. Each interface has are l at e d range of numbers. For example, the Virtual M u l t ip o in t Interface has a range of interface numbers from1 to2147483647.

**Command Default:** No interface is used for TFTP booting.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS15.0(1)M. |

**Example:**

The following example shows how to ensure that an interface is used for TFTP booting:

```text
Router> enable
Router# configure terminal
Router(config)# ip tftp boot-interface
```


### `ip tftp min-timeout`

> **Página:** 268 · **Modo:** Global configuration (config) · **Default:** The default minimum timeout period for retransmission of data is 4 seconds. · **Leitura (show/clear/…):** não

**Description:** To specify the minimum timeout period for retransmission of data using TFTP, use the ip tftp min-timeoutcommand in global configuration mode. To disable, use the no form of this command.

**Syntax:**

```text
ip tftp min-timeout seconds
no ip tftp min-timeout
```

**Parameters (Syntax Description):**

- `seconds` — Specifies the timeout value, in s e c on d s. The range is from4 to20.

**Command Default:** The default minimum timeout period for retransmission of data is 4 seconds.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS15.0(1)M. |

**Example:**

The following example shows how to specify the minimum timeout period for retransmission of data as 5 seconds:

```text
Router> enable
Router# configure terminal
Router(config)# ip tftp min-timeout 5
```


### `ip tftp source-interface`

> **Página:** 268 · **Modo:** Global configuration (config) · **Default:** The address of the closest interface to the destination is selected as the source address. · **Leitura (show/clear/…):** não

**Description:** To specify the IP address of an interface as the source address for TFTP connections, use the ip tftp source-interface command in global configuration mode. To return to the default, use the no form of this command.

**Syntax:**

```text
ip tftp source-interface interface-type interface-number
no ip tftp source-interface
```

**Parameters (Syntax Description):**

- `interface-typeinterface-number` — The interface type and number who s e address is to be used as the source for TFTP connection s.

**Command Default:** The address of the closest interface to the destination is selected as the source address.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | This command was introduced. |
| 12.3(6) | Destination address lookup in a Virtual Private Network( V P N) r out in g and for w a r d in g( VRF) t a b l e was added for the t r an s f e r of TFTP p a c k e t s. |
| 12.3(8)T | This command was integrated into Cisco IOS Release12.3(8) T. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to set the IP address of an interface as the source for all TFTP connections. If the specified interface is not up, the Cisco IOS software selects the address of the interface closest to the destination as the source address. In Cisco IOS 12.3(6) and later releases, TFTP is VRF-aware, which means that TFTP transfer is supported across an interface within a Virtual Private Network (VPN) routing and forwarding (VRF) instance. To specify a VRF as a source for TFTP connections, the VRF must be associated with the same interface that you configure with the ip tftp source-interface command. In this configuration, TFTP looks for the destination IP address for file transfer in the specified VRF table.

**Example:**

The following example shows how to configure the router to use the IP address associated with loopback interface 0 as the source address for TFTP connections :

```text
Router# configure terminal
Router(config)# ip tftp source-interface loopback0
```

The following example shows how to configure the router to use the VRF table named vpn1 to look for the destination IP address for TFTP connections. In this example, file transfer using TFTP is accomplished across an interface within a VRF (VRF vpn1) link.

```text
Router# configure terminal
Router(config)# ip tftp source-interface ethernet 1/0
Router(config)#
ip vrf vpn1
Router(config-vrf)#
rd 100:1
Router(config-vrf)# route-target both 100:1
Router(config-vrf)# interface ethernet 1/0
Router(config-if)# ip vrf forwarding vpn1
Router(config-if)# end
```


### `ip wccp web-cache accelerated`

> **Página:** 270 · **Modo:** Global configuration (config) · **Default:** When this command is not configured, hardware acceleration for WCCPv1 is not enabled. · **Leitura (show/clear/…):** não

**Description:** To enable the hardware acceleration for WCCP version 1, use the ip wccp web-cache acceleratedcommand in global configuration mode. To disable hardware acceleration, use the no form of this command.

**Syntax:**

```text
ip wccp web-cache accelerated [[group-address groupaddress] | [redirect-list access-list] | [group-list
access-list] | [password password]]
no ip wccp web-cache accelerated
```

**Parameters (Syntax Description):**

- `group-address group-address` — ( Optional) Dir e c t s the router to use as p e c if i e d m u l t i c as t IP address for c o m m u n i c at i on with the WCCP service group. See the“ Usage Guidelines” section for a d d it i on a l information.
- `redirect-list access-list` — ( Optional) Dir e c t s the router to use an access list to control traffic that is redirect e d to this service group. See the“ Usage Guidelines” section for a d d it i on a l information.
- `group-list access-list` — ( Optional) Dir e c t s the router to use an access list to d e t e r min e which cache e n g in e s are all o we d to p a r t i c ip at e in these r v i c e group. See the“ Usage Guidelines” section for a d d it i on a l information.
- `password password` — ( Optional) Specifies as t r in gt h at dir e c t s the router to ap p l y M D5 auth e n t i c at i on to message s r e c e i v e d from these r v i c e group specified by these r v i c e name given. See the“ Usage Guidelines” section for a d d it i on a l information.

**Command Default:** When this command is not configured, hardware acceleration for WCCPv1 is not enabled.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Cisco IOS Release 12.2(17d)SXB. |
| 12.2(18)SXD1 | This command was changed to support the Supervisor E n g in e720. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The group-address group-address option requires a multicast address that is used by the router to determine which cache engine should receive redirected messages. This option instructs the router to use the specified multicast IP address to coalesce the “I See You” responses for the “Here I Am” messages that it has received on this group address. In addition, the response is sent to the group address. The default is for no group-address to be configured, so that all “Here I Am” messages are responded to with a unicast reply. The redirect-list access-list option instructs the router to use an access list to control the traffic that is redirected to the cache engines of the service group that is specified by the service-name given. The access-list argument specifies either a number from 1 to 99 to represent a standard or extended access list number, or a name to represent a named standard or extended access list. The access list itself specifies the traffic that is permitted to be redirected. The default is for no redirect-list to be configured (all traffic is redirected). The group-list access-list option instructs the router to use an access list to control the cache engines that are allowed to participate in the specified service group. The access-list argument specifies either a number from 1 to 99 to represent a standard access list number, or a name to represent a named standard access list. The access list specifies which cache engines are permitted to participate in the service group. The default is for no group-list to be configured, so that all cache engines may participate in the service group. The password can be up to seven characters. When you designate a password, the messages that are not accepted by the authentication are discarded. The password name is combined with the HMAC MD5 value to create security for the connection between the router and the cache engine.

**Example:**

The following example shows how to enable the hardware acceleration for WCCP version 1:

```text
Router(config)# ip wccp web-cache accelerated
```
