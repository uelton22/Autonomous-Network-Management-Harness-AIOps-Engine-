# Capítulo 13: slave auto-sync config through terminal-type

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

## show protocols through showmon

### slave auto-sync config through terminal-type

• slave auto-sync config through terminal-type, on page 1006

### slave auto-sync config through terminal-type

### `slave auto-sync config`

> **Página:** 1030 · **Modo:** Global configuration · **Default:** Enabled · **Leitura (show/clear/…):** não

**Description:** To turn on automatic synchronization of configuration files for a Cisco 7507 or Cisco 7513 router that is configured for High System Availability (HSA) using Dual RSP Cards, use the slave auto-sync config global configuration command. To turn off automatic synchronization, use the no form of the command.

**Syntax:**

```text
slave auto-sync config
no slave auto-sync config
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Enabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | The command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command for a Cisco 7507 or Cisco 7513 router that is configured for dual RSP cards. On the Cisco 7507 and Cisco 7513 router, you can install two RSP cards in a single router to improve system availability. Dual RSP Cards is a High System Availability (HSA) feature. In automatic synchronization mode, when you issue a copy EXEC command that specifies the primary devices’ startup configuration (nvram:startup-config) as the target, the primary device also copies the same file to the secondary devices' startup configuration (slavenvram:startup-config). Use this command when implementing HSA for simple hardware backup or for software error protection to ensure that the primary and secondary RSP contain the same configuration files.

**Example:**

The following example turns on automatic configuration file synchronization. When the copy system:running-config nvram:startup-config command is entered, the running configuration is saved to the startup configurations of both the primary RSP and the secondary RSP.

```text
Router(config)# slave auto-sync config
Router(config)# end
Router# copy system:running-config nvram:startup-config
```


### `slave default-slot`

> **Página:** 1031 · **Modo:** Global configuration · **Default:** The default secondary is the RSP card located in the higher number processor slot. On the Cisco 7507 router, processor slot 3 contains the default secondary RSP. On the Cisco 7513 router, processor slot 7 contains the default secondary RSP. · **Leitura (show/clear/…):** não

**Description:** To specify the default secondary Route Switch Processor (RSP) card on a Cisco 7507 or Cisco 7513 router, use the slave default-slot global configuration command.

**Syntax:**

```text
slave default-slot processor-slot-number
```

**Parameters (Syntax Description):**

- `processor-slot-number` — Number of ap r o c e s s or slot that c on t a in s the default s e c on d a r y RSP. Onthe Cisco 7507 router, v a l id values are2 or3. Onthe Cisco7513 router, v a l id values are6 or7. The default is the h i g h e r number processor slot.

**Command Default:** The default secondary is the RSP card located in the higher number processor slot. On the Cisco 7507 router, processor slot 3 contains the default secondary RSP. On the Cisco 7513 router, processor slot 7 contains the default secondary RSP.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | The command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command for a Cisco 7507 or Cisco 7513 router that is configured for Dual RSP Cards. On the Cisco 7507 and Cisco 7513 router, you can install two RSP cards in a single router to improve system availability. Dual RSP Cards is a High System Availability (HSA) feature. The router uses the default secondary information when booting as follows: • If a system boot is due to powering up the router or using the reload EXEC command, then the specified default secondary will be the secondary RSP. • If a system boot is due to a system crash or hardware failure, then the system ignores the default secondary designation, and makes the crashed or faulty RSP card the secondary RSP.

**Example:**

In the following example, the user sets the default secondary RSP to processor slot 2 on a Cisco 7507 router:

```text
c7507(config)# slave default-slot 2
```


### `slave image`

> **Página:** 1032 · **Modo:** Global configuration (config) · **Default:** The default is to load the image from the system bundle. · **Leitura (show/clear/…):** não

**Description:** To specify the image that the secondary Route Switch Processor (RSP) runs on a Cisco 7507 or Cisco 7513 router, use the slave image command in global configuration mode.

**Syntax:**

```text
slave image {systemfile-url}
```

**Parameters (Syntax Description):**

- `system` — Load s these c on d a r y image that is bundle d with the p r i m a r y system image. This is the default.
- `file-url` — The specified file in Flash filesystem from which these c on d a r y image will be load. If you do not specify a file name, the first file in the specified Flash filesystem is the default file.

**Command Default:** The default is to load the image from the system bundle.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command for a Cisco 7507 or Cisco 7513 router that is configured for Dual RSP Cards. On the Cisco 7507 and Cisco 7513 router, you can install two RSP cards in a single router to improve system availability. Dual RSP Cards is a High System Availability (HSA) feature. Use the slave image command to override the secondary image that is bundled with the primary image. When using HSA for simple hardware backup, ensure that the secondary image is in the same location on the primary and the secondary RSP card. Thus, if the secondary RSP card becomes the primary RSP card, it will be able to find the secondary image and download it to the new secondary card. Note The default length of the bootstring filename is 64 characters. Depending on the platform a longer bootstring filename can be used and supported.

**Example:**

In the following example, the secondary RSP is specified to run the rsp-dw-mz.ucode.111-3.2 image from slot 0:

```text
Router(config)# slave image slot0:rsp-dw-mz.ucode.111-3.2
```


### `slave reload`

> **Página:** 1033 · **Modo:** Global configuration · **Default:** No default behavior or values. · **Leitura (show/clear/…):** não

**Description:** To force a reload of the image that the secondary Route Switch Processor (RSP) card is running on a Cisco 7507 or Cisco 7513 router, use the slave reload global configuration command.

**Syntax:**

```text
slave reload
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** No default behavior or values.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | The command was introduced. |
| 12.2913)T | This command is no l on g e r supported in Cisco IOS M a in line or Tech no log y-b as e d releases. It may ap p e a r in12.2 S-f a m i l y releases. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command for a Cisco 7507 or Cisco 7513 router that is configured for Dual RSP Cards. On the Cisco 7507 and Cisco 7513 router, you can install two RSP cards in a single router to improve system availability. Dual RSP Cards is a High System Availability (HSA) feature. After using the slave image global configuration command to specify the image that the secondary RSP runs on a Cisco 7507 or Cisco 7513 router, use the slave reload command to reload the secondary RSP with the new image. The slave reload command can also be used to force the secondary RSP to reboot its existing image.

**Example:**

In the following example, an inactive secondary RSP card is reloaded. If the secondary RSP reloads, it will return to an active secondary RSP state. If the primary RSP fails, the secondary RSP will become the primary RSP.

```text
c7507(config)# slave reload
```


### `slave sync config`

> **Página:** 1034 · **Modo:** Privileged EXEC · **Default:** Automatic synchronization is turned on. · **Leitura (show/clear/…):** não

**Description:** To manually synchronize configuration files on the primary and secondary Route Switch Processor (RSP) cards of a Cisco 7507 or Cisco 7513 router, use the slave sync config privileged EXEC command.

**Syntax:**

```text
slave sync config
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Automatic synchronization is turned on.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | The command was introduced. |
| 12.2(13)T | This command is no l on g e r supported in Cisco IOS M a in line or Tech no log y-b as e d releases. It may ap p e a r in12.2 S-f a m i l y releases. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command for a Cisco 7507 or Cisco 7513 router that is configured for Dual RSP Cards. On the Cisco 7507 and Cisco 7513 router, you can install two RSP cards in a single router to improve system availability. Dual RSP Cards is a High System Availability (HSA) feature. This command allows you to synchronize the configuration files of the primary and secondary RSP cards on a case-by-case basis when you do not have automatic synchronization turned on. This command copies the primary’s configuration file to the secondary RSP card. Note You must use this command when you insert a new secondary RSP card into a Cisco 7507 or Cisco 7513 router for the first time to ensure that the new secondary card is configured consistently with the primary card.

**Example:**

In the following example, the configuration files on the primary and secondary RSP card are synchronized:

```text
c7507(config)# slave sync config
```


### `slave terminal`

> **Página:** 1035 · **Modo:** Global configuration · **Default:** Enabled · **Leitura (show/clear/…):** não

**Description:** To enable access to the secondary Route Switch Processor (RSP) console, use the slave terminal global configuration command. To disable access to the secondary RSP console, use the no form of this command.

**Syntax:**

```text
slave terminal
no slave terminal
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Enabled

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | The command was introduced. |
| 12.2(13)T | This command is no l on g e r supported in Cisco IOS M a in line or Tech no log y-b as e d releases. It may ap p e a r in12.2 S-f a m i l y releases. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The secondary console does not have enable password protection. Thus, an individual connected to the secondary console port can enter privileged EXEC mode and view or erase the configuration of the router. Use the no slave terminal command to disable secondary console access and prevent security problems. When the secondary console is disabled, users cannot enter commands. If secondary console access is disabled, the following message appears periodically on the secondary console:

```text
%%Slave terminal access is disabled. Use "slave terminal" command in primary RSP configuration
mode to enable it.
```

**Example:**

In the following example, the user disables console access to the secondary RSP:

```text
c7507(config)# no slave terminal
```


### `software clean`

> **Página:** 1036 · **Modo:** Privileged EXEC (#) · **Default:** No software package(s) will be cleaned by default. · **Leitura (show/clear/…):** não

**Description:** To remove any and all packages and provisioning files that are no longer in use, use the software clean command in Privileged EXEC mode. This command does not have a no form. [ ] [ ] [ ] [ ]

**Syntax:**

```text
software clean file file url force switch nodes verbose
```

**Parameters (Syntax Description):**

- `file file url` — Full path to w i l d card e d file name( s). Optional when running in install e d mode. Whenno command options are specified, all unused package, bundle and provision in g files in the current boot directory will be clean e d.
- `force` — ( optional) P r o c e e d s to clean files with out ap rom p t
- `switch no d e s` — ( optional) Specifies which switch( e s) should perf or m the clean o p e r at i on using'1,2,4' and/ or '2-4' not at i on. Default is all switch e s in the stack.
- `verbose` — ( optional) P r o v id e s some a d d it i on a l info in the logfile s.

**Command Default:** No software package(s) will be cleaned by default.

**Command Modes:** Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |
| CiscoIOSXE3.3SE | This command was integrated. |
| CiscoIOS15.2(2)E | This command was modified. The for c e keyword was added. |

**Usage Guidelines:**

If no specific file to be deleted is indicated, the installer will search for unused packages and provisioning files on a given media device (eg., bootflash:, usb0: etc) to delete. One or more nodes may be given. With no options specified for software clean, all unused packages and provisioning files on the currently booted device will be cleaned. The currently booted device is where the committed file resides.

```text
packages.conf
```

**Example:**

This example uses the 'software clean' command with no command options to clean the current boot directory, flash:, on a standalone switch that is running in installed mode.

```text
infra-p2-3#dir flash:
Directory of flash:/
7378 -rwx 2097152 Nov 15 2012 09:45:11 +00:00 nvram_config
7379 drwx 4096 Nov 15 2012 09:19:24 +00:00 mnt
7396 -rwx 1244 Nov 14 2012 18:32:55 +00:00 packages.conf.00-
7390 -rwx 74390300 Nov 15 2012 09:18:17 +00:00 cat3k_caa-base.SSA.03.09.17.EMP.pkg
7383 -rwx 74601776 Nov 14 2012 18:31:59 +00:00 cat3k_caa-base.SSA.03.09.16.EMD.pkg
7384 -rwx 2732724 Nov 14 2012 18:32:08 +00:00 cat3k_caa-drivers.SSA.03.09.16.EMD.pkg
7385 -rwx 49886128 Nov 14 2012 18:32:02 +00:00 cat3k_caa-infra.SSA.03.09.16.EMD.pkg
7387 -rwx 30579500 Nov 14 2012 18:32:05 +00:00
cat3k_caa-iosd-universalk9.SSA.150-9.16.EMD.pkg
7386 -rwx 556 Nov 9 2012 09:58:21 +00:00 vlan.dat
7389 -rwx 62814928 Nov 14 2012 18:32:08 +00:00 cat3k_caa-wcm.SSA.03.09.16.EMD.pkg
7388 -rwx 18193120 Nov 14 2012 18:32:03 +00:00 cat3k_caa-platform.SSA.03.09.16.EMD.pkg
7397 -rwx 1243 Nov 15 2012 09:18:55 +00:00 packages.conf
7391 -rwx 2734772 Nov 15 2012 09:18:17 +00:00 cat3k_caa-drivers.SSA.03.09.17.EMP.pkg
7392 -rwx 32465772 Nov 15 2012 09:18:24 +00:00 cat3k_caa-infra.SSA.03.09.17.EMP.pkg
7393 -rwx 30384940 Nov 15 2012 09:18:35 +00:00
cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg
7394 -rwx 18143968 Nov 15 2012 09:18:39 +00:00 cat3k_caa-platform.SSA.03.09.17.EMP.pkg
7395 -rwx 62638800 Nov 15 2012 09:18:51 +00:00 cat3k_caa-wcm.SSA.03.09.17.EMP.pkg
712413184 bytes total (208535552 bytes free)
infra-p2-3#
infra-p2-3#software clean
Preparing clean operation ...
[2]: Cleaning up unnecessary package files
[2]: No path specified, will use booted path flash:packages.conf
[2]: Cleaning flash:
[2]: Preparing packages list to delete ...
cat3k_caa-base.SSA.03.09.17.EMP.pkg
File is in use, will not delete.
cat3k_caa-drivers.SSA.03.09.17.EMP.pkg
File is in use, will not delete.
cat3k_caa-infra.SSA.03.09.17.EMP.pkg
File is in use, will not delete.
cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg
File is in use, will not delete.
cat3k_caa-platform.SSA.03.09.17.EMP.pkg
File is in use, will not delete.
cat3k_caa-wcm.SSA.03.09.17.EMP.pkg
File is in use, will not delete.
packages.conf
File is in use, will not delete.
[2]: Files that will be deleted:
cat3k_caa-base.SSA.03.09.16.EMD.pkg
cat3k_caa-drivers.SSA.03.09.16.EMD.pkg
cat3k_caa-infra.SSA.03.09.16.EMD.pkg
cat3k_caa-iosd-universalk9.SSA.150-9.16.EMD.pkg
cat3k_caa-platform.SSA.03.09.16.EMD.pkg
cat3k_caa-wcm.SSA.03.09.16.EMD.pkg
packages.conf.00-
[2]: Do you want to proceed with the deletion? [yes/no]: y
[2]: Clean up completed
infra-p2-3#
infra-p2-3#dir flash:
Directory of flash:/
7378 -rwx 2097152 Nov 15 2012 09:45:11 +00:00 nvram_config
7379 drwx 4096 Nov 15 2012 09:19:24 +00:00 mnt
7390 -rwx 74390300 Nov 15 2012 09:18:17 +00:00 cat3k_caa-base.SSA.03.09.17.EMP.pkg
7386 -rwx 556 Nov 9 2012 09:58:21 +00:00 vlan.dat
7397 -rwx 1243 Nov 15 2012 09:18:55 +00:00 packages.conf
7391 -rwx 2734772 Nov 15 2012 09:18:17 +00:00 cat3k_caa-drivers.SSA.03.09.17.EMP.pkg
7392 -rwx 32465772 Nov 15 2012 09:18:24 +00:00 cat3k_caa-infra.SSA.03.09.17.EMP.pkg
7393 -rwx 30384940 Nov 15 2012 09:18:35 +00:00
cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg
7394 -rwx 18143968 Nov 15 2012 09:18:39 +00:00 cat3k_caa-platform.SSA.03.09.17.EMP.pkg
7395 -rwx 62638800 Nov 15 2012 09:18:51 +00:00 cat3k_caa-wcm.SSA.03.09.17.EMP.pkg
712413184 bytes total (447623168 bytes free)
infra-p2-3#
```


### `software commit`

> **Página:** 1038 · **Modo:** Privileged EXEC · **Default:** No software package(s) will be committed by default. · **Leitura (show/clear/…):** não

**Description:** To commit a package set that was installed using the auto-rollback command option of the software install command, use the software commit command in Privileged EXEC mode.

**Syntax:**

```text
software commit[switchnode][verbose]
```

**Parameters (Syntax Description):**

- `switch no d e s` — ( optional) specifies which switch( e s) should perf or m the commit o p e r at i on using'1,2,4' and/ or '2-4' not at i on. Default is all switch e s in the stack
- `verbose` — ( optional) p r o v id e s some a d d it i on a l info in the logfile s

**Command Default:** No software package(s) will be committed by default.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |
| CiscoIOSXERelease3.3SE | This command was integrated. |

**Usage Guidelines:**

The software commit command cancels the rollback timer, if it is running, and commits a software upgrade. A commit makes an upgrade, ie. a package set, persistent. A committed package set will run after a node is reloaded.

**Example:**

This example uses the 'software install file' command with the 'auto-rollback' command option to install the bundle onto both switches in a stack via tftp . After the switches reload with the new software, the 'software commit' command is used to stop the rollback timer and commit the candidate package set.

```text
infra-p2-3#software install file
tftp://172.19.211.47/cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin auto-rollback
Preparing install operation ...
[2]: Downloading file
tftp://172.19.211.47/cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin to active
switch 2
[2]: Finished downloading file
tftp://172.19.211.47/cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin to active
switch 2
[2]: Copying software from active switch 2 to switch 1
[2]: Finished copying software to switch 1
[1 2]: Starting install operation
[1 2]: Expanding bundle cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin
[1 2]: Copying package files
[1 2]: Package files copied
[1 2]: Finished expanding bundle cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin
[1 2]: Verifying and copying expanded package files to flash:
[1 2]: Verified and copied expanded package files to flash:
[1 2]: Starting compatibility checks
[1 2]: Finished compatibility checks
[1 2]: Starting application pre-installation processing
[1 2]: Finished application pre-installation processing
[1]: Old files list:
Removed cat3k_caa-base.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-drivers.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-infra.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg
Removed cat3k_caa-platform.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-wcm.SSA.03.09.17.EMP.pkg
[2]: Old files list:
Removed cat3k_caa-base.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-drivers.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-infra.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg
Removed cat3k_caa-platform.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-wcm.SSA.03.09.17.EMP.pkg
[1]: New files list:
Added cat3k_caa-base.SSA.03.09.19.EMP.pkg
Added cat3k_caa-drivers.SSA.03.09.19.EMP.pkg
Added cat3k_caa-infra.SSA.03.09.19.EMP.pkg
Added cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg
Added cat3k_caa-platform.SSA.03.09.19.EMP.pkg
Added cat3k_caa-wcm.SSA.03.09.19.EMP.pkg
[2]: New files list:
Added cat3k_caa-base.SSA.03.09.19.EMP.pkg
Added cat3k_caa-drivers.SSA.03.09.19.EMP.pkg
Added cat3k_caa-infra.SSA.03.09.19.EMP.pkg
Added cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg
Added cat3k_caa-platform.SSA.03.09.19.EMP.pkg
Added cat3k_caa-wcm.SSA.03.09.19.EMP.pkg
[1 2]: Creating pending provisioning file
[1 2]: Finished installing software. New software will load on reboot.
[1 2]: Setting rollback timer to 45 minutes
[1 2]: Do you want to proceed with reload? [yes/no]: y
[1]: Reloading
[2]: Pausing before reload
*Nov 15 10:24:24.891: %STACKMGR-1-RELOAD_REQUEST: 2 stack-mgr: Received reload request for
switch 1, reason User requested reload
*Nov 15 10:24:25.051: %STACKMGR-1-STACK_LINK_CHANGE: 2 stack-mgr: Stack port 2 on switch
2 is down
*Nov 15 10:24:25.051: %STACKMGR-1-SWITCH_REMOVED: 2 stack-mgr: Switch 1 has been removed
from the stack
*Nov 15 10:24:25.146: %REDUNDANCY-3-STANDBY_LOST: Standby processor fault (PEER_NOT_PRESENT)
*Nov 15 10:24:25.146: %REDUNDANCY-5-PEER_MONITOR_EVENT: Active detected a standby removal
(raw-event=PEER_NOT_PRESENT(3))
*Nov 15 10:24:25.146: %REDUNDANCY-3-STANDBY_LOST: Standby processor fault (PEER_DOWN)
*Nov 15 10:24:25.146: %REDUNDANCY-5-PEER_MONITOR_EVENT: Active detected standby down or
crashed (raw-event=PEER_DOWN(2))
*Nov 15 10:24:25.146: %REDUNDANCY-3-STANDBY_LOST: Standby processor fault
(PEER_REDUNDANCY_STATE_CHANGE)
*Nov 15 10:24:25.146: %REDUNDANCY-5-PEER_MONITOR_EVENT: Active detected a standby removal
(raw-event=PEER_REDUNDANCY_STATE_CHANGE(5))
*Nov 15 10:24:27.054: %LINK-3-UPDOWN: Interface GigabitEthernet1/0/1, changed state to down
*Nov 15 10:24:28.057: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet1/0/1,
changed state to down
[2]: Reloading
infra-p2-3#
*Nov 15 10:24:39.911: %STACKMGR-1-RELOAD_REQUEST: 2 stack-mgr: Received reload request for
switch 2, reason User requested reload
*Nov 15 10:24:39.912: %STACKMGR-1-RELOAD: 2 stack-mgr: reloading due to reason User requested
reload
*Nov 15 10:24:40.423: %IOSXE-3-PLATFORM: 2 process sysmgr: Reset/Reload requested by
[stack-manager].
< Switches were reloaded and booted with the newly installed software>
*Nov 15 10:34:21.345: %AUTHMGR_SPI-6-START: Auth Manager SPI server started (infra-p2-3-1)
*Nov 15 10:34:24.612: %HA_CONFIG_SYNC-6-BULK_CFGSYNC_SUCCEED: Bulk Sync succeeded
*Nov 15 10:34:24.624: %RF-5-RF_TERMINAL_STATE: Terminal state reached for (SSO)
*Nov 15 10:34:24.510: %SSH-5-DISABLED: SSH 1.99 has been disabled (infra-p2-3-1)
*Nov 15 10:34:24.511: %SSH-5-ENABLED: SSH 1.99 has been enabled (infra-p2-3-1)
infra-p2-3#
infra-p2-3#show software installer rollback-timer
Switch# Status Duration
----------------------------------
1 active 00:31:28
2 active 00:31:43
infra-p2-3#
infra-p2-3#software commit
Preparing commit operation ...
[1 2]: Starting commit operation
[1 2]: Finished committing software changes.
infra-p2-3#
infra-p2-3#show software installer rollback-timer
Switch# Status Duration
----------------------------------
1 inactive -
2 inactive -
infra-p2-3#
```


### `software expand`

> **Página:** 1041 · **Modo:** Privileged EXEC · **Default:** Command is used to expand an IOS XE software bundle. The contents are extracted into the same directory as the source bundle by default. · **Leitura (show/clear/…):** não

**Description:** To expand individual IOS XE Software packages and the provisioning file from a specified bundle to a specific destination directory, use the software expand command in Privileged EXEC mode. To expand the individual IOS XE Software packages and the provisioning file from the running bundle, use the software expand running command in Privileged EXEC mode.

**Syntax:**

```text
software expand {file source url | running}[todestination url][switchnodes][verbose]
```

**Parameters (Syntax Description):**

- `files our c e url` — URL of the bundle to be expand e d. If an e two r k URL is specified, the to keyword must also be used to specify the destination location. The file and running keywords are m u t u all y exclusive
- `running` — Specifies that the package s from the running bundle should be expand e d. The to keyword must also be used to specify the destination location. The file and running keywords are m u t u all y exclusive. The running command option is not all o we d when running in install e d mode.
- `to destination url` — Specifies the l o c a l or U F S directory where the expand e d bundle c on t e n t s are c o p i e d to. Note If this option is note n t e r e d, the c on t e n t s are e x t r a c t e d into the same directory as the source bundle. This keyword is m and at or y when the source URL is an e two r k URL, and also when the running keyword is used.
- `switch no d e s` — ( optional) Specifies which switch( e s) should perf or m the expand o p e r at i on using'1,2,4' and/ or'2-4' not at i on. Default is all switch e s in the stack.
- `verbose` — ( optional) p r o v id e s some a d d it i on a l info in the logfile s

**Command Default:** Command is used to expand an IOS XE software bundle. The contents are extracted into the same directory as the source bundle by default.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |
| CiscoIOSXERelease3.3SE | This command was integrated. |

**Usage Guidelines:**

If the to option is not entered, the contents will be extracted into the default installation location for the platform. The bundle file is unchanged after the operation is complete.

**Example:**

This example uses the following steps to prepare a switch for booting in installed mode, i.e., booting a package provisioning file ( packages.conf ) 1. Boot in bundle mode using 'boot flash:<bundle name>' Can also boot from usbflash0 : or via tftp

```text
switch: b tftp://172.19.211.47/cat3k_caa-universalk9.SSA.03.09.17.EMP.150-9.17.EMP.bin
Reading full image into
memory......................................................................................................................................................................................................................done
Nova Bundle Image
--------------------------------------
Kernel Address : 0x6042fef4
Kernel Size : 0x317ccc/3243212
Initramfs Address : 0x60747bc0
Initramfs Size : 0xdbf2f9/14414585
Compression Format: .mzip
Bootable image at @ ram:0x6042fef4
Bootable image segment 0 address range [0x81100000, 0x81b80000] is in range [0x80180000,
0x90000000].
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
File "tftp://172.19.211.47/cat3k_caa-universalk9.SSA.03.09.17.EMP.150-9.17.EMP.bin"
uncompressed and installed, entry point: 0x811060f0
Loading Linux kernel with entry point 0x811060f0 ...
Bootloader: Done loading app on core_mask: 0xf
### Launching Linux Kernel (flags = 0x5)
All packages are Digitally Signed
Starting System Services
:
:
*Nov 15 10:49:35.746: %LINEPROTO-5-UPDOWN: Line protocol on Interface
TenGigabitEthernet2/1/1, changed state to down
*Nov 15 10:49:35.746: %LINEPROTO-5-UPDOWN: Line protocol on Interface
TenGigabitEthernet2/1/2, changed state to down
*Nov 15 10:49:36.822: %LINK-3-UPDOWN: Interface GigabitEthernet2/0/1, changed state to up
infra-p2-3>
infra-p2-3>enable
infra-p2-3#
```

2. Use the 'software clean file flash:' command to remove any unused package, bundle and provisioning files from flash:

```text
infra-p2-3#software clean file flash:
Preparing clean operation ...
[2]: Cleaning up unnecessary package files
[2]: Preparing packages list to delete ...
[2]: Files that will be deleted:
cat3k_caa-base.SSA.03.09.19.EMP.pkg
cat3k_caa-drivers.SSA.03.09.19.EMP.pkg
cat3k_caa-infra.SSA.03.09.19.EMP.pkg
cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg
cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg
cat3k_caa-platform.SSA.03.09.19.EMP.pkg
cat3k_caa-wcm.SSA.03.09.19.EMP.pkg
packages.conf
[2]: Do you want to proceed with the deletion? [yes/no]: yes
[2]: Clean up completed
infra-p2-3#
```

3. Use the 'software expand running to flash:' command to expand the running bundle to flash:

```text
infra-p2-3#software expand running to flash:
Preparing expand operation ...
[2]: Expanding the running bundle
[2]: Copying package files
[2]: Package files copied
[2]: Finished expanding the running bundle
infra-p2-3#
infra-p2-3#dir flash:
Directory of flash:/
7378 -rwx 2097152 Nov 15 2012 10:49:37 +00:00 nvram_config
14753 drwx 4096 Nov 15 2012 10:20:27 +00:00 mnt
7381 -rw- 74390300 Nov 15 2012 10:54:24 +00:00 cat3k_caa-base.SSA.03.09.17.EMP.pkg
7382 -rw- 2734772 Nov 15 2012 10:54:24 +00:00 cat3k_caa-drivers.SSA.03.09.17.EMP.pkg
7383 -rw- 32465772 Nov 15 2012 10:54:24 +00:00 cat3k_caa-infra.SSA.03.09.17.EMP.pkg
7384 -rw- 30384940 Nov 15 2012 10:54:24 +00:00
cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg
7385 -rw- 18143968 Nov 15 2012 10:54:24 +00:00 cat3k_caa-platform.SSA.03.09.17.EMP.pkg
7380 -rw- 1243 Nov 15 2012 10:55:03 +00:00 packages.conf
7386 -rwx 556 Nov 9 2012 09:58:21 +00:00 vlan.dat
7387 -rw- 62638800 Nov 15 2012 10:54:24 +00:00 cat3k_caa-wcm.SSA.03.09.17.EMP.pkg
712413184 bytes total (447627264 bytes free)
infra-p2-3#
```

4. Reload the switch

```text
infra-p2-3#reload
Reload command is being issued on Active unit, this will reload the whole stack
Proceed with reload? [confirm]
*Nov 15 10:56:35.800: %SYS-5-RELOAD: Reload requested by console. Reload Reason: Reload
command.
*Nov 15 10:56:36.569: %STACKMGR-1-RELOAD_REQUEST: 2 stack-mgr: Received reload request for
all switches, reason Reload command
*Nov 15 10:56:36.570: %STACKMGR-1-RELOAD: 2 stack-mgr: reloading due to reason Reload
command
*Nov 15 10:56:37.071: %IOSXE-3-PLATFORM: 2 process sysmgr: Reset/Reload requested by
[stack-manager].
<Thu Nov 15 10:56:37 2012> Message from sysmgr: Reset Reason:Reset/Reload requested by
[stack-manager]. [Reload command]
```

5. Boot the installed packages using 'boot flash:packages.conf '

```text
switch: boot flash:packages.conf
Getting rest of image
Reading full image into memory....done
Reading full base package into memory...: done = 74390300
Nova Bundle Image
--------------------------------------
Kernel Address : 0x6042f354
Kernel Size : 0x317ccc/3243212
Initramfs Address : 0x60747020
Initramfs Size : 0xdbf2f9/14414585
Compression Format: .mzip
Bootable image at @ ram:0x6042f354
Bootable image segment 0 address range [0x81100000, 0x81b80000] is in range
[0x80180000, 0x90000000].
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
boot_system: 377
Loading Linux kernel with entry point 0x811060f0 ...
Bootloader: Done loading app on core_mask: 0xf
### Launching Linux Kernel (flags = 0x5)
All packages are Digitally Signed
Starting System Services
:
:
*Nov 15 11:05:23.202: %LINEPROTO-5-UPDOWN: Line protocol on Interface
TenGigabitEthernet2/1/1, changed state to down
*Nov 15 11:05:23.202: %LINEPROTO-5-UPDOWN: Line protocol on Interface
TenGigabitEthernet2/1/2, changed state to down
*Nov 15 11:05:24.286: %LINK-3-UPDOWN: Interface GigabitEthernet2/0/1, changed state to up
infra-p2-3>
```


### `software install file`

> **Página:** 1046 · **Modo:** Privileged EXEC · **Default:** Command is used to install IOS XE software. No software will be installed by default. · **Leitura (show/clear/…):** não

**Description:** To install IOS XE Software files, use the software install file command in Privileged EXEC mode.

**Syntax:**

```text
software install file bundle url
[switchnodes][auto-rollbackminutes][force][on-reboot][provisioning-fileprovisioning-file
url][force][new][verbose]
```

**Parameters (Syntax Description):**

- `file bundle url` — Specify the url of the bundle file to be install e d.
- `switch no d e s` — ( optional) Specifies which switch( e s) should perf or m the install o p e r at i on using'1,2,4' and/ or '2-4' not at i on. Default is all switch e s in the stack.
- `auto-rollbackminutes` — ( optional) Used to start the rollback timer for the specified number of min u t e s. If not used, the software is automatic all y commit t e d after install at i on. A value to z e rom e an s the rollback timer is n e v e r start e d and the software is not automatic all y commit t e d( n e e d to use' software commit'). If set to an other value, the' software commit' command must be used to commit the software before the timer e x p i r e s( e l s e it will automatic all y rollback to the original software).
- `on-reboot` — ( optional) In d i c at e s that the user should not prompt e d to reload when the install at i on o p e r at i on c o m p l e t e s. The user must then use the reload command to boot the system with then e w l y install e d package s.
- `provisioning-fileprovisioning-fileurl` — ( optional) Specifies the provision in g file to be u p d at e d by the install at i on. Default is the running provision in g file. V a l id location s are flash: or usb flash0:
- `force` — ( optional) Specifies that the o p e r at i on will be for c e d. Forced m e an s that the install at i on will p r o c e e d d e s p it e any remote package in c o m p at i b i l it i e s. For c e should not g e n e r all y be r e q u i r e d, and should be used with caution. L o c a l package c o m p at i b i l it y check s are e n for c e d r e g a r d l e s s of this command option.
- `new` — ( optional) In d i c at e s that the p o s t-install package set should c on t a in only the package s being install e d. With out this option, the p o s t-install package set is a m e r g e d set of the current l y install e d software and the n e w package s being install e d.
- `verbose` — ( optional) p r o v id e s some a d d it i on a l info in the logfile s

**Command Default:** Command is used to install IOS XE software. No software will be installed by default.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |
| CiscoIOSXERelease3.3SE | This command was integrated. |

**Usage Guidelines:**

The software install file command is used to install package files from a software bundle when the system is running in installed mode. By default, the command will install software on all nodes in the system. The following tasks are performed during the software install file operation. - For a network installation, download the specified software bundle into memory on the active node (or standalone node is a standalone system). - In a multi-node system, copy the software bundle to each node if the file does not already exist on the node. If installing a bundle that resides in local media on the active node (flash: or usbflash0:), the bundle file (.bin) is copied to the corresponding local device on each node. If installing a bundle via the network, the bundle is copied to memory on each node in the system. - Expand the package files from the specified bundle into flash: on each node after verifying each package's digital signature - Perform compatibility checks on all nodes in the system to ensure that the software running on all nodes after installation will be compatible. This task is skipped if the force command option is used. - Start the auto-rollback timer if the auto-rollback command option was used. The newly installed packages will be automatically rolled back if the auto-rollback timer expires before the 'software commit' command is issued. - Update the package provisioning file (packages.conf) and save a copy of the original provisioning file for use during auto-rollback or user-initiated rollback (software rollback command). - Commit the newly installed software packages if the auto-rollback command option was not used. - Prompt the user to reload (if the on-reboot command option was not used). Note The software install file command cannot be used if the system is running in bundle mode. In this case, the software expand command can be used to prepare the system to boot in installed mode.

**Example:**

The following example installs the cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin bundle from a tftp server. The bundle is first downloaded to RAM, then the package files included in the bundle are extracted and copied to flash:. The .bin file itself is not copied to flash:. Note You need IOSd IP connectivity to install via tftp .

```text
infra-p2-3#software install file tftp://172.19.211.47/
cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin
Preparing install operation ...
[2]: Downloading file tftp://172.19.211.47/
cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin to active switch 2
[2]: Finished downloading file tftp://172.19.211.47/
cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin to active switch 2
[2]: Starting install operation
[2]: Expanding bundle cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin
[2]: Copying package files
[2]: Package files copied
[2]: Finished expanding bundle cat3k_caa-universalk9.SSA.03.09.19.EMP.150-9.19.EMP.bin
[2]: Verifying and copying expanded package files to flash:
[2]: Verified and copied expanded package files to flash:
[2]: Starting compatibility checks
[2]: Finished compatibility checks
[2]: Starting application pre-installation processing
[2]: Finished application pre-installation processing
[2]: Old files list:
Removed cat3k_caa-base.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-drivers.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-infra.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg
Removed cat3k_caa-platform.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-wcm.SSA.03.09.17.EMP.pkg
[2]: New files list:
Added cat3k_caa-base.SSA.03.09.19.EMP.pkg
Added cat3k_caa-drivers.SSA.03.09.19.EMP.pkg
Added cat3k_caa-infra.SSA.03.09.19.EMP.pkg
Added cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg
Added cat3k_caa-platform.SSA.03.09.19.EMP.pkg
Added cat3k_caa-wcm.SSA.03.09.19.EMP.pkg
[2]: Creating pending provisioning file
[2]: Finished installing software. New software will load on reboot.
[2]: Committing provisioning file
[2]: Do you want to proceed with reload? [yes/no]: n
infra-p2-3#
```


### `software install source switch`

> **Página:** 1049 · **Modo:** Privileged EXEC · **Default:** Command is used to install IOS XE software. No software will be installed by default. · **Leitura (show/clear/…):** não

**Description:** To install the running IOS XE software packages from one stack member to one or more other stack members, use the software install source switch command in Privileged EXEC mode.

**Syntax:**

```text
software install source switchnode
[switchnode][auto-rollbackminutes][force][on-reboot][verbose][new][provisioning-fileprovisioning-file
url]
```

**Parameters (Syntax Description):**

- `Specifies` — which switch in the stack
- `switch no d e` — Specifies which switch in the stack to use as the package source. Only as in g l e switch may be specified and the r e is no default value
- `switch no d e s` — ( optional) Specifies which switch( e s) should perf or m the install o p e r at i on using'1,2,4' and/ or '2-4' not at i on. Default is all switch e s in the stack.
- `auto-rollbackminutes` — ( optional) Used to start the rollback timer for the specified number of min u t e s. If not used, the software is automatic all y commit t e d after install at i on. A value to z e rom e an s the rollback timer is n e v e r start e d and the software is not automatic all y commit t e d( n e e d to use' software commit'). If set to an other value, the' software commit' command must be used to commit the software before the timer e x p i r e s( e l s e it will automatic all y rollback to the original software).
- `force` — ( optional) Specifies that the o p e r at i on will be for c e d. Forced m e an s that the install at i on will p r o c e e d d e s p it e any remote package in c o m p at i b i l it i e s. For c e should not g e n e r all y be r e q u i r e d, and should be used with caution. L o c a l package c o m p at i b i l it y check s are e n for c e d r e g a r d l e s s of this command option.
- `on-reboot` — ( optional) In d i c at e s that the user should not prompt e d to reload when the install at i on o p e r at i on c o m p l e t e s. The user must then use the reload command to boot the system with then e w l y install e d package s.
- `verbose` — ( optional) p r o v id e s some a d d it i on a l info in the logfile s
- `new` — ( optional) In d i c at e s that the p o s t-install package set should c on t a in only the package s being install e d. With out this option, the p o s t-install package set is a m e r g e d set of the current l y install e d software and the n e w package s being install e d.
- `provisioning-fileprovisioning-fileurl` — ( optional) Specifies the provision in g file to be u p d at e d by the install at i on. Default is the running provision in g file. V a l id location s are flash: or usb flash0:

**Command Default:** Command is used to install IOS XE software. No software will be installed by default.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |

**Usage Guidelines:**

The software install source switch command is used to install the running package files from one stack member to one or more other stack members while the system is running in installed mode. The following tasks are performed during the software install source switch operation. - Copy the running software packages from flash: on the specified source switch to flash: on all other switches specified in the command. - Perform compatibility checks on all switches in the stack to ensure that the software running on all stack members after installation will be compatible. This task is skipped if the force command option is used. - Start the auto-rollback timer if the auto-rollback command option was used. The newly installed packages will be automatically rolled back if the auto-rollback timer expires before the software commit command is issued. - Update the package provisioning file (packages.conf) and save a copy of the original provisioning file for use during auto-rollback or user-initiated rollback (software rollback command). - Commit the newly installed software packages if the auto-rollback command option was not used. - Prompt the user to reload (if the command option was not used). on-reboot Note The software install source switch command cannot be used if the system is running in bundle mode. In this case, the software expand command can be used to prepare the system to boot in installed mode.

**Example:**

In the following example, the switches in a 2-member stack are running different (but compatible) software packages. The software install source switch command is used to install the currently running packages on the standby switch (switch 1) to the active switch (switch 2).

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
Package: Base, version: 03.09.17.EMP, status: active
File: cat3k_caa-base.SSA.03.09.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:27:51 PST 2012, by: udonthi
Package: Drivers, version: 03.09.17.EMP, status: active
File: cat3k_caa-drivers.SSA.03.09.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:31:01 PST 2012, by: udonthi
Package: Infra, version: 03.09.17.EMP, status: active
File: cat3k_caa-infra.SSA.03.09.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:28:53 PST 2012, by: udonthi
Package: IOS, version: 150-9.17.EMP, status: active
File: cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:29:58 PST 2012, by: udonthi
Package: Platform, version: 03.09.17.EMP, status: active
File: cat3k_caa-platform.SSA.03.09.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:29:33 PST 2012, by: udonthi
Package: WCM, version: 03.09.17.EMP, status: active
File: cat3k_caa-wcm.SSA.03.09.17.EMP.pkg, on: Switch2
Built: Mon Nov 12 20:30:29 PST 2012, by: udonthi
infra-p2-3#
infra-p2-3#software install source switch 1
Preparing install operation ...
[2]: Copying software from source switch 1 to switch 2
[2]: Finished copying software to switch 2
[2]: Starting install operation
[2]: Starting compatibility checks
[2]: Finished compatibility checks
[2]: Starting application pre-installation processing
[2]: Finished application pre-installation processing
[2]: Old files list:
Removed cat3k_caa-base.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-drivers.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-infra.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg
Removed cat3k_caa-platform.SSA.03.09.17.EMP.pkg
Removed cat3k_caa-wcm.SSA.03.09.17.EMP.pkg
[2]: New files list:
Added cat3k_caa-base.SSA.03.09.19.EMP.pkg
Added cat3k_caa-drivers.SSA.03.09.19.EMP.pkg
Added cat3k_caa-infra.SSA.03.09.19.EMP.pkg
Added cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg
Added cat3k_caa-platform.SSA.03.09.19.EMP.pkg
Added cat3k_caa-wcm.SSA.03.09.19.EMP.pkg
[2]: Creating pending provisioning file
[2]: Finished installing software. New software will load on reboot.
[2]: Committing provisioning file
[2]: Do you want to proceed with reload? [yes/no]: no
infra-p2-3#
```


### `software install source switch`

> **Página:** 1053 · **Modo:** Privileged EXEC · **Default:** Command is used to install IOS XE software. No software will be installed by default. · **Leitura (show/clear/…):** não

**Description:** To install IOS XE Software objects from various sources, use the software install source switch command in Privileged EXEC mode.

**Syntax:**

```text
software install source switch node [switch nodes][auto-rollback minutes][on-reboot][provisioning-file
provisioning-file url][force][verbose][new]
```

**Parameters (Syntax Description):**

- `source switch node` — Specifies which switch in the stack to use as the package source. Only as in g l e switch may be specified and the r e is no default value.
- `switch nodes` — ( optional) Specifies which switch( e s) should perf or m the install o p e r at i on using'1,2,4' and/ or '2-4' not at i on. Default is all switch e s in the stack.
- `auto-rollback minutes` — ( optional) Used to start the rollback timer for the specified number of min u t e s. If not used, the software is automatic all y commit t e d after install at i on. A value to z e rom e an s the rollback timer is n e v e r start e d and the software is not automatic all y commit t e d( n e e d to use' software commit'). If set to an other value, the' software commit' command must be used to commit the software before the timer e x p i r e s( e l s e it will automatic all y rollback to the original software).
- `on-reboot` — ( optional) In d i c at e s that the user should not prompt e d to reload when the install at i on o p e r at i on c o m p l e t e s. The user must then use the reload command to boot the system with then e w l y install e d package s.
- `provision in g-file provision in g-file url` — ( optional) Specifies the provision in g file to be u p d at e d by the install at i on. Default is the running provision in g file. V a l id location s are flash: or usb flash0:
- `force` — ( optional) Specifies that the o p e r at i on will be for c e d. Forced m e an s that the install at i on will p r o c e e d d e s p it e any remote package in c o m p at i b i l it i e s. For c e should not g e n e r all y be r e q u i r e d, and should be used with caution. L o c a l package c o m p at i b i l it y check s are e n for c e d r e g a r d l e s s of this command option.
- `new` — ( optional) In d i c at e s that the p o s t-install package set should c on t a in only the package s being install e d. With out this option, the p o s t-install package set is a m e r g e d set of the current l y install e d software and the n e w package s being install e d.
- `verbose` — ( optional) p r o v id e s some a d d it i on a l info in the logfile s

**Command Default:** Command is used to install IOS XE software. No software will be installed by default.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |
| CiscoIOSXERelease3.3SE | This command was integrated. |

**Usage Guidelines:**

If the package option is not specified, it means operate on (ie. upgrade) the currently provisioned packages using all of the packages from the input. If one or more package names are specified, they act as a filter on the input file set, limiting the upgrade to the given packages. If one or more switch keywords are not specified, to identify destination node(s), then 'all' nodes are assumed as the destination. If the on-reboot option is not specified, then the software install file command will do everything that the platform requires to make the specified packages "run", ie. to commit and activate them. This typically involves a system reload. A new set of packages installed together succeed or fail together. Any one failure, on any node, fails the entire installation. As an example, using the "one-button" install (one single command to perform the upgrade):

```text
software install file
<bundle-url>
```

Where the bundle contains 3 packages. The 3 packages will be expanded on to the box, on each node (in a multimode system). A new will be created with the 3 new packages added/changed

```text
candidate packages.conf
```

(on each node). The packages in the new will be checked for compatibility. Then

```text
candidate packages.conf
```

they will be activated together, on each node, in parallel. If there is a failure at any point, or if the rollback timer is let to expire, the system will be rolled back to the state before the install command was issued.

**Example:**

To take advantage of the created source list, in exec mode use this command:

```text
software install source
list <list-name> [package <package-name-or-wildcard>] [switch <node>]
[auto-rollback <minutes>] [force] [on-reboot] [verbose] [new]
```

All of the same options as for the 'software source url' command apply (as above). Using the previous example, the installation command to install all of the packages using the above named list would be:

```text
software install source list my-list-123
```

with any options, as required. This is equivalent to entering:

```text
software install source list my-list-123 package *
```

The default argument for 'package' is therefore '*' (for the software install source list command). As another example, to install all "wcm" packages from the same list:

```text
software install source list my-list-123 package *wcm*
```


### `software provision`

> **Página:** 1056 · **Modo:** Privileged EXEC · **Default:** No software will be provisioned by default. · **Leitura (show/clear/…):** não

**Description:** To organize IOS XE Software packages from an input bundle(s) or a list onto a flash device for later activation, use the software provision command in Privileged EXEC mode.

**Syntax:**

```text
software provision source {url bundle or package url | listlist-name}[packagepackage name or
wildcard][switchnode][force][verbose]
```

**Parameters (Syntax Description):**

- `listlist-name` — Specify an or d e r e d list of in p u t bundle s of dir e c to r i e stop r o v is i on.
- `package package name or w i l d card` — Specify the package file names to be provision e d.
- `bundle or package url` — Specify a bundle or package( s) to be install e d. A w i l d card may be used to specify the in p u t, but only one bundle is accept e d( as the end r e s u l to f the w i l d card o p e r at i on). By c on t r as t, more than one package file will be accept e d as the r e s u l to f a w i l d card o p e r at i on.
- `switch` — In d i c at e s apa r t i c u l a r no d e, an in d e p end e n t in s t an c e running Nova, to which the o p e r at i on will be perf or m e d.
- `force` — Specifies that the o p e r at i on will p r o c e e d d e s p it e any remote package in c o m p at i b i l it i e s, with out in t e r a c t in g with the user. Note For c e should not g e n e r all y be r e q u i r e d for upgrade s, and should be used with c a u t i on. Local package c o m p at i b i l it i e s are a l w a y s e n for c e d.
- `verbose` — D is p l a y s all output that can be d is p l a y e do n the c on s o l e d u r in gt h e o p e r at i on.

**Command Default:** No software will be provisioned by default.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |

**Usage Guidelines:**

The software provision command does not activate nor commit any copied packages. This provisioning command effectively builds up a list of packages into a file, which forms the input

```text
candidate packages.conf
```

for the software activate command. The software provision command may be run multiple times in order to "build up" a desired set of packages for upgrade. The package set is built up into an internal file, and the packages

```text
candidate packages.conf
```

become "installed pending activation".

**Example:**

To:


### `software repackage`

> **Página:** 1058 · **Modo:** Privileged EXEC · **Default:** No software will be repackaged by default. · **Leitura (show/clear/…):** não

**Description:** To take a snapshot of a committed Cisco IOS XE Software package and create a bundle from it to be copied off-box, use the software repackage command in Privileged EXEC mode.

**Syntax:**

```text
software repackage switchnode dest url and filename
```

**Parameters (Syntax Description):**

- `switch` — In d i c at e s apa r t i c u l a r no d e, an in d e p end e n t in s t an c e running No v a, from which the p a r t i c u l a r package will be repackage d.
- `destination url and file name` — Specifies the destination location for the repackage d bundle.

**Command Default:** No software will be repackaged by default.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |

**Usage Guidelines:**

The installer can repackage a set of committed packages, and copy them off-box to any arbitrary filesystem. This takes a snapshot of the committed software and creates a bundle from it.


### `software rollback`

> **Página:** 1058 · **Modo:** Privileged EXEC · **Default:** No software will be rolled-back by default. · **Leitura (show/clear/…):** não

**Description:** To rollback the committed Cisco IOS XE Software to a previous installation point, use the software rollback command in Privileged EXEC mode.

**Syntax:**

```text
software rollback [switchnode][as-booted][provisioning-fileprovisioning-file
url][on-reboot][force][verbose]
```

**Parameters (Syntax Description):**

- `switch no d e s` — ( optional) specifies which switch( e s) should perf or m the rollback o p e r at i on using'1,2,4' and/ or'2-4' not at i on. Default is all switch e s in the stack
- `as-booted` — ( optional) Used to rollback any install at i on s that have o c c u r r e d s in c e bootup and commit the boot e d package s. c on f file.
- `provisioning-fileprovisioning-fileurl` — ( optional) Specifies the provision in g file to be u p d at e d by the rollback. Default is the running provision in g file. V a l id location s are flash: or usb flash0:
- `on-reboot` — ( optional) In d i c at e s that the user should not prompt e d to reload when the rollback o p e r at i on c o m p l e t e s. The user must then use the reload command to boot the system with then e w l y install e d package s.
- `force` — ( optional) Specifies that the o p e r at i on will be for c e d. Forced m e an s that the rollback will p r o c e e d d e s p it e any remote package in c o m p at i b i l it i e s. For c e should not g e n e r all y be r e q u i r e d, and should be used with caution. L o c a l package c o m p at i b i l it y check s are e n for c e d r e g a r d l e s s of this command option.
- `verbose` — ( optional) p r o v id e s some a d d it i on a l info in the logfile s

**Command Default:** No software will be rolled-back by default.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |
| CiscoIOSXERelease3.3.SE | This command was integrated. |

**Usage Guidelines:**

The software rollback command rolls back the committed software, ie. set of packages, to a previous installation point. The software rollback functionality relies on the existence of one or more rollback provisioning files in flash:, along with all of the .pkg files listed in the rollback provisioning file(s). The rollback provisioning files are visible in flash: as packages.conf.00-, packages.conf.01-, etc. - packages.conf.00- is a snapshot of the packages.conf file as it looked prior to the last installation operation. - packages.conf.01- is a snapshot of the packages.conf file as it looked two installations ago. (This pattern continues for all provisioning files.) When the software rollback command is used, packages.conf.00- becomes packages.conf, packages.conf.01- becomes packages.conf.00-, etc. Note If the software clean command is used, future attempts to do a software rollback will fail if the rollback provisioning file and/or the packages listed in it have been cleaned.

**Example:**

This example uses the 'software rollback' command to revert to the previously installed package set ( packages.conf.00 -).

```text
infra-p2-3#software rollback
Preparing rollback operation ...
[2]: Starting rollback operation
[2]: Starting compatibility checks
[2]: Finished compatibility checks
[2]: Starting application pre-installation processing
[2]: Finished application pre-installation processing
[2]: Old files list:
Removed cat3k_caa-base.SSA.03.09.19.EMP.pkg
Removed cat3k_caa-drivers.SSA.03.09.19.EMP.pkg
Removed cat3k_caa-infra.SSA.03.09.19.EMP.pkg
Removed cat3k_caa-iosd-universalk9.SSA.150-9.19.EMP.pkg
Removed cat3k_caa-platform.SSA.03.09.19.EMP.pkg
Removed cat3k_caa-wcm.SSA.03.09.19.EMP.pkg
[2]: New files list:
Added cat3k_caa-base.SSA.03.09.17.EMP.pkg
Added cat3k_caa-drivers.SSA.03.09.17.EMP.pkg
Added cat3k_caa-infra.SSA.03.09.17.EMP.pkg
Added cat3k_caa-iosd-universalk9.SSA.150-9.17.EMP.pkg
Added cat3k_caa-platform.SSA.03.09.17.EMP.pkg
Added cat3k_caa-wcm.SSA.03.09.17.EMP.pkg
[2]: Creating pending provisioning file
[2]: Finished rolling back software changes. New software will load on reboot.
[2]: Do you want to proceed with reload? [yes/no]: n
infra-p2-3#
```


### `software source list`

> **Página:** 1061 · **Modo:** Global configuration (config) · **Default:** No source list exists. · **Leitura (show/clear/…):** não

**Description:** To create a list of input bundles or directories, use the software source list command in global configuration mode. To erase a source list, use the no form of the software source list command.

**Syntax:**

```text
software source list list-name-string
no software source list list-name-string
```

**Parameters (Syntax Description):**

- `list-name-string` — Name of the list or string.

**Command Default:** No source list exists.

**Command Modes:** Global configuration (config)

**Usage Guidelines:**

If it happens that using either the software install file command or the software install source commands result in an error due to too many characters on the command line, you can create a list of input bundles or directories using the software source list command. The available configured lists may then be verified using the show running config command, which also displays the contents of the lists. The pool of packages defined by a list can be displayed with the show software source list list-name command.

**Example:**

To creat a source list named "my-list-123" perform the following

```text
(config)software source list my-list-123
(config-source-list)tftp://my-big-bundle.bin
(config-source-list)bootflash:/packages1
(config-source-list)end
```

This effectively creates a pool of packages from which to find ("source"), a package. It creates an ordered search list for Installer to find a given package. For example, a requested package will first be looked for in the bundle file 'tftp://my-big-bundle.bin'. If not found, the requested package will then be looked for in the directory . Naturally, packages would have had to have been previously 'expanded' into the directory 'bootflash:/packages1' by the user to make them available for use in this manner.


### `software uninstall`

> **Página:** 1062 · **Modo:** Privileged EXEC · **Default:** No software will be uninstalled by default. · **Leitura (show/clear/…):** não

**Description:** To deactivate a Cisco IOS XE Software package or set of packages, use the software uninstall command in Privileged EXEC mode.

**Syntax:**

```text
software unistall bundle or package url [switchnode]
```

**Parameters (Syntax Description):**

- `bundle or package url` — Specify a bundle or package( s) to be d e activated. Note W i l d card s may be used
- `switch` — In d i c at e s apa r t i c u l a r no d e, an in d e p end e n t in s t an c e running No v a, from which the p a r t i c u l a r package will be uninstall e d.

**Command Default:** No software will be uninstalled by default.

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| IOSXE3.2.0SE | Command introduced. |

**Usage Guidelines:**

Wildcards can be used with the 'package' argument. Note There may be restrictions on what can be uninstalled. For example, the installer will refuse to uninstall a package where there is no compatible ancestor.


### `special-character-bits`

> **Página:** 1063 · **Modo:** Line configuration · **Default:** 7-bit ASCII character set · **Leitura (show/clear/…):** não

**Description:** To configure the number of data bits per character for special characters such as software flow control characters and escape characters, use the special-character-bits command in line configuration mode. To restore the default value, use the no form of this command.

**Syntax:**

```text
special-character-bits {7 | 8}
no special-character-bits
```

**Parameters (Syntax Description):**

- `7` — S e l e c t s the7-b it ASCII characters e t. This is the default.
- `8` — S e l e c t s the full8-b it characters e t for special characters.

**Command Default:** 7-bit ASCII character set

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Setting the special character bits to 8 allows you to use twice as many special characters as with the 7-bit ASCII character set. The special characters affected by this setting are the escape, hold, stop, start, disconnect, and activation characters.

**Example:**

The following example allows the full 8-bit international character set for special characters on line 5:

```text
Router(config)# line 5
Router(config-line)# special-character-bits 8
```


### `squeeze`

> **Página:** 1064 · **Modo:** Privileged EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To permanently erase files tagged as “deleted” or “error” on Class A flash file systems, use the squeeze command in privileged EXEC mode. Cisco 7600 Series Router

**Syntax:**

```text
squeeze [/nolog] [/quiet] filesystem:
squeeze filesystem:
```

**Parameters (Syntax Description):**

- `/nolog` — ( Optional) Disable s the squeeze log( recovery data) and a c c e l e r at e s the squeeze process.
- `/quiet` — ( Optional) Disable s status message s d u r in gt h e squeeze process.
- `filesystem:` — The flash filesystem, f o l low e d by a c o l on. Forthe Cisco7600 s e r i e s router, the v a l id values for the flash filesystem are bootflash: and flash:

**Command Modes:** Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | This command was introduced. |
| 12.2(1) | This command was i m p l e m e n t e do n the Cisco2600 and Cisco3600 s e r i e s routers. |
| 12.0(17)S | This command was integrated into Cisco IOS Release12.0(17) S, and the/ no log and/ q u i e t keywords were added. |
| 12.2(1a) | The/ no log and/ q u i e t keywords were added. |
| 12.0(17)ST | This command was integrated into Cisco IOS Release12.0(17) S T. |
| 12.1(9)E | This command was integrated into Cisco IOS Release12.1(9) E. |
| 12.2(2)B | This command was integrated into Cisco IOS Release12.2(2) B. |
| 12.2(4)XL | This command was i m p l e m e n t e do n the Cisco1700 s e r i e s routers. |
| 12.2(14)SX | Support for this command was i m p l e m e n t e do n the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was integrated into Release 12.2(17d)SXB. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

When flash memory is full, you might need to rearrange the files so that the space used by the files marked “deleted” can be reclaimed. (This “squeeze” process is required for linear flash memory cards to make sectors contiguous; the free memory must be in a “block” to be usable.) When you enter the squeeze command, the router copies all valid files to the beginning of flash memory and erases all files marked “deleted.” After the squeeze process is completed, you can write to the reclaimed flash memory space. Caution After performing the squeeze process, you cannot recover deleted files using the undelete EXEC mode command. In addition to removing deleted files, use the squeeze command to remove any files that the system has marked as “error”. An error file is created when a file write fails (for example, the device is full). To remove error files, you must use the squeeze command. Rewriting flash memory space during the squeeze operation may take several minutes. Using the /nolog keyword disables the log for the squeeze process. In most cases, this process will speed up the squeeze process. However, if power is lost or the flash card is removed during the squeeze process, all the data on the flash card will be lost, and the device will have to be reformatted. Note Using the /nolog keyword makes the squeeze process uninterruptible. Using the /quiet keyword disables the output of status messages to the console during the squeeze process. If the optional keywords are not used, the progress of the squeeze process will be displayed to the console, a log for the process will be maintained, and the squeeze process is interruptible. On Cisco 2600 or Cisco 3600 series routers, the entire file system has to be erased once before the squeeze command can be used. After being erased once, the command should operate properly on the flash squeeze file system for the rest of the flash file system’s history. To erase an entire flash file system on a Cisco 2600 or 3600 series router, perform the following steps: 1. If the flash file system has multiple partitions, enter the no partition command to remove the partitions. The reason for removing partitions is to ensure that the entire flash file system is erased. The squeeze command can be used in a flash file system with partitions after the flash file system is erased once. 2. Enter the erase command to erase the flash file system.

**Example:**

Supported Platforms Other tha the Cisco 7600 Series Router In the following example, the file named config1 is deleted, and then the squeeze command is used to reclaim the space used by that file. The /nolog option is used to speed up the squeeze process.

```text
Router# delete config1
Delete filename [config1]?
Delete slot0:conf? [confirm]
Router# dir slot0:
! Note that the deleted file name appears in square brackets
Directory of slot0:/
1 -rw- 4300244 Apr 02 2001 03:18:07 c7200-boot-mz.122-0.14
2 -rw- 2199 Apr 02 2001 04:45:15 [config1]
3 -rw- 4300244 Apr 02 2001 04:45:23 image
20578304 bytes total (11975232 bytes free)
!20,578,304 - 4,300,244 - 4,300,244 - 2,199 - 385 = 11975232
Router# squeeze /nolog slot0:
%Warning: Using /nolog option would render squeeze operation uninterruptible.
All deleted files will be removed. Continue? [confirm]
Squeeze operation may take a while. Continue? [confirm]
Squeeze of slot0 completed in 291.832 secs .
dir slot0:
Directory of slot0:/
1 -rw- 4300244 Apr 02 2001 03:18:07 c7200-boot-mz.122-0.14
2 -rw- 4300244 Apr 02 2001 04:45:23 image
20578304 bytes total (11977560 bytes free)
!20,578,304 - 4,300,244 - 4,300,244 - 256 = 11977560
```

Cisco 7600 Series Router This example shows how to permanently erase the files that are marked “deleted” from the flash memory:

```text
squeeze flash:
```


### `stack-mib portname`

> **Página:** 1067 · **Modo:** Interface configuration · **Default:** This command has no default settings. · **Leitura (show/clear/…):** não

**Description:** To specify a name string for a port, use the stack-mib portnamecommand in interface configuration mode.

**Syntax:**

```text
stack-mib portname portname
```

**Parameters (Syntax Description):**

- `portname` — Name for ap or t.

**Command Default:** This command has no default settings.

**Command Modes:** Interface configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2917d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release 12.2(17d)SXB. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Using the stack-mib command to set a name string to a port corresponds to the portName MIB object in the portTable of CISCO-STACK-MIB. portName is the MIB object in the portTable of CISCO-STACK-MIB. You can set this object to be descriptive text describing the function of the interface.

**Example:**

This example shows how to set a name to a port:

```text
Router(config-if)#
stack-mib portname portall
Router(config-if)#
```


### `state-machine`

> **Página:** 1067 · **Modo:** Global configuration (config) · **Default:** No transition criteria are specified. · **Leitura (show/clear/…):** não

**Description:** To specify the transition criteria for the state of a particular state machine, use the state-machine command in global configuration mode . To remove a particular state machine from the configuration, use the no form of this command.

**Syntax:**

```text
state-machine name state first-character last-character [next-state delay | transmit]
no state-machine name
```

**Parameters (Syntax Description):**

- `name` — Name for the state machine( used in the dispatch-machine line configuration command). The user can specify any number of state machine s, but each line can have only one state machine as s o c i at e d with it.
- `state` — State being modified. The r e are a maximum of e i g h t state s p e r state machine. The range is from0 to7. Lines are initialize d to state0 and return to state0 after apa c k e t is t r an s m it t e d.
- `first-character last-character` — A range of characters. Use ASCII n u m e r i c a l values. The range is from0 to255. If the state machine is in the in d i c at e d state, and then e x t character in p u t is with in this range, the process g o e s to the specified next state. Full8-b it character c o m p a r is on s are perf or m e d, s o the maximum value is255. E n s u r e that the line is configure d to s t r ip parity bits( or not generate the m), or d u p l i c at e the low characters in the u p p e r h a l f of the space.
- `next-state` — ( Optional) State to enter if the character is in the specified range. The range is from 0to7.
- `delay` — ( Optional) T r an s m its the p a c k e t if the r e is no in p u t with in50 m i l l is e c on d s.
- `t r an s m it` — ( Optional) Cause s the p a c k e t to be t r an s m it t e d and the state machine to be reset to state0. R e c u r r in g characters that have not been e x p l i c it l y define d to have apa r t i c u l a r a c t i on return the state machine to state0.

**Command Default:** No transition criteria are specified.

**Command Modes:** Global configuration (config)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| 15.0(1)M | This command was modified in are l e as e e a r l i e r than Cisco IOS Release15.0(1) M. The delay keyword was added. |

**Usage Guidelines:**

This command is paired with the dispatch-machine line configuration command, which defines the line on which the state machine is effective.

**Example:**

In the following example a dispatch machine named “function” is configured to ensure that the function key characters on an ANSI terminal are kept in one packet. Because the default in the example is to remain in state 0 without sending anything, normal key signals are sent immediately.

```text
Router(config)# line 1 20
Router(config-line)#
dispatch-machine function
Router(config-line)#
exit
Router(config)# state-machine function 0 0 255 6 transmit
```

**Related Commands:**

- Command Description
- dispatch-character Defines a character that causes a packet to be sent.
- dispatch-machine Specifies an identifier for a TCP packet dispatch state machine on a particular line.


### `stopbits`

> **Página:** 1069 · **Modo:** Line configuration · **Default:** 2 stop bits per byte · **Leitura (show/clear/…):** não

**Description:** To set the number of the stop bits transmitted per byte, use the stopbits command in line configuration mode. To restore the default value, use the no form of this command.

**Syntax:**

```text
stopbits {1 | 1.5 | 2}
no stopbits
```

**Parameters (Syntax Description):**

- `1` — One stop bit.
- `1` — One stop b it.
- `1.5` — One and one-h a l f stopbits.
- `2` — Two stopbits. This is the default.

**Command Default:** 2 stop bits per byte

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Communication protocols provided by devices such as terminals and modems often require a specific stop-bit setting.

**Example:**

In the following example, the stop bits transmitted per byte are changed from the default of two stop bits to one stop bit as a performance enhancement for line 4:

```text
Router(config)#
line 4
Router(config-line)# stopbits 1
```


### `storm-control level`

> **Página:** 1069 · **Modo:** Interface configuration · **Default:** All packets are passed. · **Leitura (show/clear/…):** não

**Description:** To set the suppression level, use the storm-control level command in interface configuration mode. To turn off the suppression mode, use the no form of this command.

**Syntax:**

```text
storm-control {broadcast | multicast | unicast} level level [. level]
no storm-control {broadcast | multicast | unicast} level
```

**Parameters (Syntax Description):**

- `b r o a d c as t` — Specifies the b r o a d c as t traffic.
- `m u l t i c as t` — Specifies the m u l t i c as t traffic.
- `unicast` — Specifies the u n i c as t traffic.
- `level` — Integer-sup p r e s s i on level; v a l id values are from0 to100 p e r c e n t.
- `. level` — ( Optional) F r a c t i on a l-sup p r e s s i on level; v a l id values are from0 to99.

**Command Default:** All packets are passed.

**Command Modes:** Interface configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You can enter this command on switch ports and router ports. Enter the storm-control level command to enable traffic storm control on the interface, configure the traffic storm-control level, and apply the traffic storm-control level to all traffic storm-control modes that are enabled on the interface. Only one suppression level is shared by all three suppression modes. For example, if you set the broadcast level to 30 and set the multicast level to 40, both levels are enabled and set to 40. The Cisco 7600 series router supports storm control for multicast and unicast traffic only on Gigabit Ethernet LAN ports. The switch supports storm control for broadcast traffic on all LAN ports. The multicast and unicast keywords are supported on Gigabit Ethernet LAN ports only. These keywords are not supported on 10 Mbps, 10/100 Mbps, 100 Mbps, or 10-Gigabit Ethernet modules. The period is required when you enter the fractional-suppression level. The suppression level is entered as a percentage of the total bandwidth. A threshold value of 100 percent means that no limit is placed on traffic. A threshold value of 0 or 0.0 (fractional) percent means that all specified traffic is blocked on a port, with the following guidelines: • A fractional level value of 0.33 or lower is the same as 0.0 on the following modules: • WS-X6704-10GE • WS-X6748-SFP • WS-X6724-SFP • WS-X6748-GE-TX • A fractional level value of 0.29 or lower is the same as 0.0 on the WS-X6716-10G-3C / 3CXL in Oversubscription Mode. • Enter 0 on all other modules to block all specified traffic on a port. Enter the show interfaces counters broadcast command to display the discard count. Enter the show running-config command to display the enabled suppression mode and level setting. To turn off suppression for the specified traffic type, you can do one of the following: • Set the level to 100 percent for the specified traffic type. • Use the no form of this command.

**Example:**

This example shows how to enable and set the suppression level:

```text
Router(config-if)#
storm-control broadcast level 30
```

This example shows how to disable the suppression mode:

```text
Router(config-if)#
no storm-control multicast level
```


### `sync-restart-delay`

> **Página:** 1071 · **Modo:** Interface configuration · **Default:** timer is 210 milliseconds. · **Leitura (show/clear/…):** não

**Description:** To set the synchronization-restart delay timer to ensure accurate status reporting, use the sync-restart-delay command in interface configuration mode. To disable the synchronization-restart delay timer, use the no form of this command.

**Syntax:**

```text
sync-restart-delay timer
no sync-restart-delay timer
```

**Parameters (Syntax Description):**

- `timer` — Interval be t we e n status-register reset s; v a l id values are from200 to60000 m i l l is e c on d s.

**Command Default:** timer is 210 milliseconds.

**Command Modes:** Interface configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is supported on Gigabit Ethernet fiber ports only. The status register records the current status of the link partner.

**Example:**

This example shows how to set the Gigabit Ethernet synchronization-restart delay timer:

```text
Router(config-if)# sync-restart-delay 2000
```


### `systat`

> **Página:** 1072 · **Modo:** User EXEC (>) Privileged EXEC (#) · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** Note This command has been replaced by the show users command. To display information about the active lines on the router, use the systatcommand in user EXEC or privilegedEXEC mode.

**Syntax:**

```text
systat all
```

**Parameters (Syntax Description):**

- `all` — D is p l a y s all lines, r e g a r d l e s s of whether the lines are used or not.

**Command Modes:** User EXEC (>) Privileged EXEC (#)

**Command History:**

| Release | Modification |
| --- | --- |
| 15.0(1)M | This command was introduced in are l e as e e a r l i e r than Cisco IOS Release 15.0(1)M. |
| 12.2(33)SRB | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SRB. |
| 12.2(33)SXI | This command was integrated into are l e as e e a r l i e r than Cisco IOS Release 12.2(33)SXI. |
| CiscoIOSXERelease2.1 | This command was i m p l e m e n t e do n the Cisco AS R1000 S e r i e s A g g r e g at i on Service s Routers. |

**Example:**

The following example shows how to display the active lines:

```text
Router# systat
Line User Host(s) Idle Location
* 0 con 0 idle 00:00:00
Interface User Mode Idle Peer Address
```


### `system flowcontrol bus`

> **Página:** 1073 · **Modo:** Global configuration · **Default:** auto · **Leitura (show/clear/…):** não

**Description:** To set the FIFO overflow error count, use the system flowcontrol bus command in global configuration mode. To return to the original FIFO threshold settings, use the no form of this command. [default] system flowcontrol bus {auto | on}

**Syntax:**

```text
no system flowcontrol bus
```

**Parameters (Syntax Description):**

- `default` — ( Optional) Specifies the default set t in g s.
- `auto` — Monitor s the F IF O over f low error count and send s a warning message if the F IF O over f low error count e x c e e d s a configure d error threshold in5-s e c on d interval s.
- `on` — Specifies the original F IF O threshold set t in g s.

**Command Default:** auto

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(18)SXF | Support for this command was introduced on the Supervisor E n g in e720 and the Supervisor E n g in e32. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Note We recommend that you leave the system flow control in auto mode and use the other modes under the advice of Cisco TAC only.

**Example:**

This example shows how to monitor the FIFO overflow error count and send a warning message if the FIFO overflow error count exceeds a configured error threshold in 5-second intervals:

```text
Router(config)# system flowcontrol bus auto
```

This example shows how to specify the original FIFO threshold settings:

```text
Router(config)# system flowcontrol bus on
```


### `system jumbomtu`

> **Página:** 1074 · **Modo:** Global configuration · **Default:** mtu-size is 9216 bytes. · **Leitura (show/clear/…):** não

**Description:** To set the maximum size of the Layer 2 and Layer 3 packets, use the system jumbomtu command in global configuration mode. To revert to the default MTU setting, use the no form of this command.

**Syntax:**

```text
system jumbomtu mtu-size
no system jumbomtu
```

**Parameters (Syntax Description):**

- `mtu-size` — Maximum size of the L a y e r2 and L a y e r3 p a c k e t s; v a l id values are from1500 to9216 by t e s.

**Command Default:** mtu-size is 9216 bytes.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 1.2(14)SX | Support for this command was introduced on the Supervisor E n g in e720. |
| 12.2(17d)SXB | Support for this command on the Supervisor E n g in e2 was e x t end e d to Release12.2(17 d) S X B. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The mtu-size parameter specifies the Ethernet packet size, not the total Ethernet frame size. The Layer 3 MTU is changed as a result of entering the system jumbomtucommand. The system jumbomtucommand enables the global MTU for port ASICs. On a port ASIC after jumbo frames are enabled, the port ASIC accepts any size packet on the ingress side and checks the outgoing packets on the egress side. The packets on the egress side that exceed the global MTU are dropped by the port ASIC. For example, if you have port A in VLAN 1 and Port B in VLAN 2, and if VLAN 1 and VLAN 2 are configured for mtu 9216 and you enter the system jumbomtu 4000 command, the packets that are larger than 4000 bytes are not transmitted out because Ports B and A drop anything larger than 4000 bytes.

**Example:**

This example shows how to set the global MTU size to 1550 bytes:

```text
Router(config)# system jumbomtu 1550
```

This example shows how to revert to the default MTU setting:

```text
Router(config)# no system jumbomtu
```


### `tdm clock priority`

> **Página:** 1075 · **Modo:** Global configuration · **Default:** If no clocks are configured, the system uses a default, primary clock. An external clock is never selected by default; it must be explicitly configured. · **Leitura (show/clear/…):** não

**Description:** To configure the clock source and priority of the clock source used by the time-division multiplexing (TDM) bus on the Cisco AS5350, AS5400, and AS5850 access servers, use the tdm clock priority command in global configuration mode. To return the clock source and priority to the default values, use the no form of this command.

**Syntax:**

```text
tdm clock priority priority-number {slot/ds1-port | slot/ds3-port:ds1-port | external | freerun}
no tdm clock priority priority-number {slot/ds1-port | slot/ds3-port:ds1-port | external | freerun}
```

**Parameters (Syntax Description):**

- `priority-number` — Priority of the clock source. The priority range is from 1 to 99. A clock set to
- `priority-number` — Priority of the clock source. The priority range is from1 to99. A clock set to priority100 will not d r i v e the TDMbus.
- `slot / ds1-port` — Trunk-card slot is a value from1 to7. D S1 port number control l e r is a value be t we e n0 and7. Specify with as l as h s e p a r at in gt h e numbers; for example,1/1.
- `slot / ds3-port : ds1-port` — Trunk-card slot is a value from1 to7. D S3 ports p e c if i e s the T3port. DS1port number control l e r is a value from1 to28. Specify with as l as h s e p a r at in gt h e slot and port numbers, and a c o l on s e p a r at in gt h e D S1 port number. An example is1/0:19.
- `e x t e r n a l` — Sync h r on i z e s the TDM bus with an e x t e r n a l clock source that can be used as an a d d it i on a l network r e f e r e n c e.
- `freerun` — S e l e c t s the free-running clock from the l o c a l o s c i l l at or when the r e is no g o o d clock in g source from at r u n k card or an e x t e r n a l clock source.

**Command Default:** If no clocks are configured, the system uses a default, primary clock. An external clock is never selected by default; it must be explicitly configured.

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 12.2(8)T | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The TDM bus can receive an input clock from one of three sources on the gateway: • CT1, CE1, and CT3 trunk cards • An external T1/E1 clock source feed directly through the Building Integrated Timing Supply (BITS) interface port on the motherboard • Free-running clock providing clock from an oscillator Note BITS is a single building primary timing supply. BITS generally supplies DS1- and DS0-level timing throughout an office. BITS is the clocks that provide and distribute timing to a wireline network’s lower levels. Trunk-Card Ports The TDM bus can be synchronized with any trunk cards. On the CT1/CE1 trunk card, each port receives the clock from the T1/E1 line. The CT3 trunk card uses an M13 multiplexer to receive the DS1 clock. Each port on each trunk-card slot has a default clock priority. Also, clock priority is configurable through the tdm clock priority command. External Clock The TDM bus can be synchronized with an external clock source that can be used as an additional network reference. If no clocks are configured, the system uses a primary clock through a software-controlled default algorithm. If you want the external T1/E1 clock (from the BITS interface) as the primary clock source, you must configure it using the external keyword with the tdm clock priority command; the external clock is never selected by default. The BITS interface requires a T1 line composite clock reference set at 1.544 MHz and an E1 line composite clock reference set at 2.048 MHz. Free-Running Clock If there is no good clocking source from a trunk card or an external clock source, then select the free-running clock from the internal oscillator using the freerun keyword with the tdm clock priority command.

**Example:**

In the following example, BITS clock is set at priority 1:

```text
AS5400(config)# tdm clock priority priority 1 external
```

In the following example, a trunk clock from a CT1 trunk card is set at priority 2 and uses slot 4 and DS1 port (controller) 6:

```text
AS5400(config)# tdm clock priority priority 2 4/6
```

In the following example, a trunk clock from a CT3 trunk card is set at priority 2 and uses slot 1, DS3 port 0, and DS1 port 19:

```text
AS5400(config)# tdm clock priority priority 2 1/0:19
```

In the following example, free-running clock is set at priority 3:

```text
AS5400(config)# tdm clock priority priority 3 freerun
```


### `terminal databits`

> **Página:** 1077 · **Modo:** EXEC · **Default:** 8 data bits per character · **Leitura (show/clear/…):** não

**Description:** To change the number of data bits per character for the current terminal line for this session, use the terminal databits command in EXEC mode.

**Syntax:**

```text
terminal databits {5 | 6 | 7 | 8}
```

**Parameters (Syntax Description):**

- `5` — F i v e databits p e r character.
- `6` — S i x databits p e r character.
- `7` — S e v end at a bits p e r character.
- `8` — E i g h t databits p e r character. This is the default.

**Command Default:** 8 data bits per character

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Communication protocols provided by devices such as terminals and modems often require a specific data bit setting. The terminal databits command can be used to mask the high bit on input from devices that generate 7 data bits with parity. If parity is being generated, specify 7 data bits per character. If no parity generation is in effect, specify 8 data bits per character. The other keywords (5 and 6) are supplied for compatibility with older devices and are generally not used.

**Example:**

In the following example, the databits per character is changed to seven for the current session:

```text
Router# terminal databits 7
```


### `terminal data-character-bits`

> **Página:** 1077 · **Modo:** EXEC · **Default:** 8 data bits per character · **Leitura (show/clear/…):** não

**Description:** To set the number of data bits per character that are interpreted and generated by the Cisco IOS software for the current line and session, use the terminal data-character-bits command in EXEC mode.

**Syntax:**

```text
terminal data-character-bits {7 | 8}
```

**Parameters (Syntax Description):**

- `7` — S e v end at a bits p e r character.
- `8` — E i g h t databits. This is the default.

**Command Default:** 8 data bits per character

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is used primarily to strip parity from X.25 connections on routers with the protocol translation software option. The terminal data-character-bits command does not work on hard-wired lines.

**Example:**

The following example sets the data bits per character to seven on the current line:

```text
terminal data-character-bits 7
```


### `terminal dispatch-character`

> **Página:** 1078 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To define a character that causes a packet to be sent for the current session, use the terminal dispatch-character command in EXEC mode.

**Syntax:**

```text
terminal dispatch-character ascii-number [ascii-number2...]
```

**Parameters (Syntax Description):**

- `ascii-number` — The ASCII decimal representation of the character, such as Return( ASCII character13) for line-at-a-time t r an s m is s i on s.
- `ascii-number2...` — ( Optional) A d d it i on a l decimal representation s of characters. This syntax in d i c at e s that you can define any number of characters as dispatch characters.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

At times, you might want to queue up a string of characters until they fill a complete packet and then transmit the packet to a remote host. This can make more efficient use of a line, because the access server or router normally dispatches each character as it is entered.

**Example:**

The following example defines the characters Ctrl-D (ASCII decimal character 4) and Ctrl-Y (ASCII decimal character 25) as the dispatch characters:

```text
Router# terminal dispatch-character 4 25
```


### `terminal dispatch-timeout`

> **Página:** 1079 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To set the character dispatch timer for the current terminal line for the current session, use the terminal dispatch-timeout command in EXEC mode.

**Syntax:**

```text
terminal dispatch-timeout milliseconds
```

**Parameters (Syntax Description):**

- `m i l l is e c on d s` — Integer that specifies then u m be r of m i l l is e c on d s that the router wait s after it p u t s the first character into apa c k e t buffer before send in gt h e p a c k e t. D u r in gt h is interval, more characters can be added to the p a c k e t, which in c r e as e s the process in g e f f i c i e n c y of the remote host.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Use this command to increase the processing efficiency of the remote host. The dispatch-timeout line configuration command causes the software to buffer characters into packets for transmission to the remote host. The Cisco IOS software sends a packet a specified amount of time after the first character is put into the buffer. You can use the terminal dispatch-timeoutand terminal dispatch-character line configuration commands together. In this case, the software dispatches a packet each time the dispatch character is entered, or after the specified dispatch timeout interval, depending on which condition is met first. Note The router response time might appear intermittent if the timeout interval is greater than 100 milliseconds and remote echoing is used.

**Example:**

In the following example, the dispatch timeout timer is set to 80 milliseconds:

```text
Router# terminal dispatch-timeout 80
```


### `terminal download`

> **Página:** 1080 · **Modo:** EXEC · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To temporarily set the ability of a line to act as a transparent pipe for file transfers for the current session, use the terminal download command in EXEC mode.

**Syntax:**

```text
terminal download
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Disabled

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You can use this feature to run a program such as KERMIT, XMODEM, or CrossTalk that downloads a file across an access server or router line. This command configures the terminal line to send data and is equivalent to entering all the following commands: • terminal telnet transparent • terminal no escape-character (see terminal escape-character ) • terminal no hold-character (see terminal hold-character ) • terminal no padding 0 (see terminal padding ) • terminal no padding 128 (seeterminal padding ) • terminal parity none • terminal databits 8

**Example:**

The following example configures a line to act as a transparent pipe:

```text
Router# terminal download
```


### `terminal editing`

> **Página:** 1081 · **Modo:** EXEC · **Default:** Enabled · **Leitura (show/clear/…):** não

**Description:** To reenable the enhanced editing mode for only the current terminal session, use the terminal editing command in EXEC mode. To disable the enhanced editing mode on the current line, use the no form of this command.

**Syntax:**

```text
terminal editing
terminal no editing
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Enabled

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command is identical to the editing EXEC mode command, except that it controls (enables or disables) enhanced editing for only the terminal session you are using. For a description of the available editing keys, see the description of the editing command in this document.

**Example:**

In the following example, enhanced editing mode is reenabled for only the current terminal session:

```text
Router> terminal editing
```


### `terminal escape-character`

> **Página:** 1081 · **Modo:** EXEC · **Default:** Ctrl-^ (Ctrl-Shift-6) · **Leitura (show/clear/…):** não

**Description:** To set the escape character for the current terminal line for the current session, use the terminal escape-character command in EXEC mode.

**Syntax:**

```text
terminal escape-character ascii-number
```

**Parameters (Syntax Description):**

- `ascii-number` — ASCII decimal representation of the escape character or control sequence( for example, Ctrl-P).

**Command Default:** Ctrl-^ (Ctrl-Shift-6)

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

See the "ASCII Character Set and Hexidecimal Values" appendix for a list of ASCII characters and their numerical representation. This command is useful, for example, if you have the default escape character defined for a different purpose in your keyboard file. Entering the escape character followed by the X key returns you to EXEC mode when you are connected to another computer. Note The Break key generally cannot be used as an escape character on the console terminal because the operating software interprets the Break command on a console line as an instruction to halt the system.

**Example:**

In the following example, the escape character to Ctrl-P (ASCII decimal character 16) for the current session:

```text
terminal escape-character 16
```


### `terminal exec-character-bits`

> **Página:** 1082 · **Modo:** EXEC · **Default:** 7-bit ASCII character set (unless set otherwise in global configuration mode) · **Leitura (show/clear/…):** não

**Description:** To locally change the ASCII character set used in EXEC and configuration command characters for the current session, use the terminal exec-character-bits command in EXEC mode.

**Syntax:**

```text
terminal exec-character-bits {7 | 8}
```

**Parameters (Syntax Description):**

- `7` — S e l e c t s the7-b it ASCII characters e t. This is the default.
- `8` — S e l e c t s the full8-b it characters e t.

**Command Default:** 7-bit ASCII character set (unless set otherwise in global configuration mode)

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This EXEC command overrides the default-value exec-character-bits global configuration command. Configuring the EXEC character width to 8 bits enables you to view special graphical and international characters in banners, prompts, and so on. When the user exits the session, the character width is reset to the default value established by the exec-character-bits global configuration command. However, setting the EXEC character width to 8 bits can also cause failures. For example, if a user on a terminal that is sending parity enters the help command, an “unrecognized command” message appears because the system is reading all 8 bits, and the eighth bit is not needed for the help command.

**Example:**

The following example temporarily configures the system to use a full 8-bit user interface for system banners and prompts, allowing the use of additional graphical and international characters:

```text
Router# terminal exec-character-bits 8
```


### `terminal flowcontrol`

> **Página:** 1083 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To set flow control for the current terminal line for the current session, use the terminal flowcontrol command in EXEC mode.

**Syntax:**

```text
terminal flowcontrol {none | software[in | out] | hardware}
```

**Parameters (Syntax Description):**

- `none` — P r events flowcontrol.
- `software` — Set s software flowcontrol.
- `in |out` — ( Optional) Specifies the dir e c t i on of flowcontrol: in cause s the router to list e n to flowcontrol from the attach e d device, and out cause s the router to send flowcontrol information to the attach e d device. If you do not specify a dir e c t i on, both dir e c t i on s are as s u m e d.
- `hardware` — Set s hardware flowcontrol. For information about set t in g u p the E I A/ T I A-232 line, see the m an u a l that was s h ip p e d with your p r o d u c t.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Flow control enables you to regulate the rate at which data can be transmitted from one point so that it is equal to the rate at which it can be received at another point. Flow control protects against loss of data because the terminal is not capable of receiving data at the rate it is being sent. You can set up data flow control for the current terminal line in one of two ways: software flow control, which you do with control key sequences, and hardware flow control, which you do at the device level. For software flow control, the default stop and start characters are Ctrl-S and Ctrl-Q (XOFF and XON). You can change them with the terminal stop-character and terminal start-character EXEC commands.

**Example:**

In the following example, incoming software flow control is set for the current session:

```text
terminal flowcontrol software in
```


### `terminal full-help`

> **Página:** 1084 · **Modo:** EXEC · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To get help for the full set of user-level commands, use the terminal full-help command in EXEC mode.

**Syntax:**

```text
terminal full-help
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Disabled

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The terminal full-help command enables a user to see all of the help messages available from the terminal. It is used with the show ? command.

**Example:**

In the following example, the difference between the output of the show ? command before and after using the terminal full-help command is shown:

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
Router> terminal full-help
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
cdp CDP information
clns CLNS network information
clock Display the system clock
cls DLC user information
cmns Connection-Mode networking services (CMNS) information
compress Show compression statistics.
x25 X.25 information
xns XNS information
xremote XRemote statistics
```


### `terminal history`

> **Página:** 1085 · **Modo:** User EXEC Privileged EXEC · **Default:** Enabled, history buffer of 10 lines · **Leitura (show/clear/…):** não

**Description:** To enable the command history function with 10 lines for the current terminal session, use the terminal history command in user EXEC or privileged EXEC mode. To disable the command history function, use the no form of this command.

**Syntax:**

```text
terminal history
terminal no history
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Enabled, history buffer of 10 lines

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The history function provides a record of commands you have entered. This function is particularly useful for recalling long or complex commands or entries for the purposes of modifying them slightly and reexecuting them. The terminal history command enables the command history function with the default buffer size or the last buffer size specified using the terminal history size command. The following table lists the keys and functions you can use to recall commands from the history buffer.

| Key(s) | Function |
| --- | --- |
| Ctrl-PorUpArrow4 | Recallscommandsinthehistorybufferinabackwardsequence,beginningwith themostrecentcommand.Repeatthekeysequencetorecallsuccessivelyolder commands. |
| Ctrl-NorDownArrow1 | Returnstomorerecentcommandsinthehistorybufferafterrecallingcommands withCtrl-PortheUpArrow.Repeatthekeysequencetorecallsuccessivelymore recentcommands. |

The arrow keys function only with ANSI-compatible terminals.

**Example:**

In the following example, the command history feature is disabled for the current terminal session:

```text
Router> terminal no history
```


### `terminal history size`

> **Página:** 1086 · **Modo:** EXEC · **Default:** 10 lines of command history · **Leitura (show/clear/…):** não

**Description:** To change the size of the command history buffer for the current terminal session, use the terminal history size command in EXEC mode. To reset the command history buffer to its default size of 10 lines, use the no form of this command.

**Syntax:**

```text
terminal history size number-of-lines
terminal no history size
```

**Parameters (Syntax Description):**

- `number-of-lines` — Number of command lines that the system will r e c or d in its history buffer. The range is from0 to256. The default is10.

**Command Default:** 10 lines of command history

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The history feature provides a record of commands you have entered. This feature is particularly useful for recalling long or complex commands or entries for the purposes of modifying them slightly and reissuing them. The terminal history size command enables the command history feature and sets the command history buffer size. The terminal no history size command resets the buffer size to the default of 10 command lines. The following table lists the keys and functions you can use to recall commands from the history buffer. When you use these keys, the commands recalled will be from EXEC mode if you are in EXEC mode, or from all configuration modes if you are in any configuration mode.

| Key | Function |
| --- | --- |
| Ctrl-PorUpArrow5 | Recallscommandsinthehistorybufferinabackwardsequence,beginningwith themostrecentcommand.Repeatthekeysequencetorecallsuccessivelyolder commands. |
| Ctrl-NorDownArrow1 | Returnstomorerecentcommandsinthehistorybufferafterrecallingcommands withCtrl-PortheUpArrow.Repeatthekeysequencetorecallsuccessivelymore recentcommands. |

The arrow keys function only with ANSI-compatible terminals. In EXEC mode, you can also use the show history command to show the contents of the command history buffer. To check the current settings for the command history feature on your line, use the show line command.

**Example:**

In the following example, the number of command lines recorded is set to 15 for the current terminal session. The user then checks to see what line he/she is connected to using the show users command. The user uses this line information to issue the show line command. (In this example, the user uses the option in the command to start the output at the “Editing is show begin show line enabled/disabled” line.)

```text
Router# terminal history size 15
Router# show users
Line User Host(s) Idle Location
* 50 vty 0 admin idle 00:00:00
! the * symbol indicates the active terminal session for the user (line 50)
show line 50 | begin Editing
Editing is enabled.
! the following line shows the history settings for the line
History is enabled, history size is 15.
DNS resolution in show commands is enabled
Full user help is disabled
Allowed transports are telnet. Preferred is none.
No output characters are padded
No special data dispatching characters
```


### `terminal hold-character`

> **Página:** 1088 · **Modo:** EXEC · **Default:** The default hold character is defined by the hold-character global configuration command. · **Leitura (show/clear/…):** não

**Description:** To define the hold character for the current session, use the terminal hold-character command in EXEC mode. To return the hold character definition to the default, use the no form of this command.

**Syntax:**

```text
terminal hold-character ascii-number
terminal no hold-character
```

**Parameters (Syntax Description):**

- `ascii-number` — ASCII decimal representation of a character or control sequence( for example, C t r l-P).

**Command Default:** The default hold character is defined by the hold-character global configuration command.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You can define a local hold character that temporarily suspends the flow of output on the terminal. When information is scrolling too quickly, you can enter the hold character to pause the screen output, then enter any other character to resume the flow of output. You cannot suspend output on the console terminal. To send the hold character to the host, precede it with the escape character.

**Example:**

In the following example, the hold character for the current (local) session is set to Ctrl-P. The show terminal output is included to show the verification of the setting (the value for the hold character is shown in the “Special Characters” listing).

```text
terminal hold-character 16
"^P" is the local hold character
Router# show terminal
Line 50, Location: "", Type: "VT220"
Length: 24 lines, Width: 80 columns
Baud rate (TX/RX) is 9600/9600
Status: PSI Enabled, Ready, Active, No Exit Banner, Automore On
Capabilities: none
Modem state: Ready
Group codes: 0
Special Chars: Escape Hold Stop Start Disconnect Activation
^^x ^P - - none
Timeouts: Idle EXEC Idle Session Modem Answer Session Dispatch
00:10:00 never none not set
Idle Session Disconnect Warning
never
Login-sequence User Response
00:00:30
Autoselect Initial Wait
not set
Modem type is unknown.
Session limit is not set.
Time since activation: 00:04:13
Editing is enabled.
History is enabled, history size is 10.
```


### `terminal international`

> **Página:** 1089 · **Modo:** User EXEC Privileged EXEC · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** If you are using Telnet to access a Cisco IOS platform and you want to display 8-bit and multibyte international characters (for example, Kanji) and print the Escape character as a single character instead of as the caret and bracket symbols (^[) for a current Telnet session, use the terminal international command in user EXEC or priviledged mode. To display characters in 7-bit format for a current Telnet session, use the no form of this command.

**Syntax:**

```text
terminal international
no terminal international
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Disabled

**Command Modes:** User EXEC Privileged EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.3 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If you are configuring a Cisco IOS platform using the Cisco web browser UI, this feature is enabled automatically when you enable the Cisco web browser UI using the ip http server global configuration command.

**Example:**

The following example enables a Cisco IOS platform to display 8-bit and multibyte characters and print the Escape character as a single character instead of as the caret and bracket symbols (^[) when you are using Telnet to access the platform for the current Telnet session:

```text
Router# terminal international
```


### `terminal keymap-type`

> **Página:** 1090 · **Modo:** EXEC · **Default:** VT100 · **Leitura (show/clear/…):** não

**Description:** To specify the current keyboard type for the current session, use the terminal keymap-type command in EXEC mode.

**Syntax:**

```text
terminal keymap-type keymap-name
```

**Parameters (Syntax Description):**

- `keymap-name` — Name d e f in in gt h e current k e y b o a r d type.

**Command Default:** VT100

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 11.2 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You must use this command when you are using a keyboard other than the default of VT100.

**Example:**

The following example specifies a VT220 keyboard as the current keyboard type:

```text
Router# terminal keymap-type vt220
```


### `terminal length`

> **Página:** 1091 · **Modo:** EXEC (>) Privileged EXEC (#) Diagnostic (diag) · **Default:** 24 lines · **Leitura (show/clear/…):** não

**Description:** To set the number of lines on the current terminal screen for the current session, use the terminal length command in EXEC, privileged EXEC, and diagnostic mode.

**Syntax:**

```text
terminal length screen-length
```

**Parameters (Syntax Description):**

- `screen-length` — Number of lines on the screen. A value of z e r o disable s p a using be t we e n screen s of output.

**Command Default:** 24 lines

**Command Modes:** EXEC (>) Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers, and be c a m e a v a i l a b l e in diagnostic mode. |

**Usage Guidelines:**

The system uses the length value to determine when to pause during multiple-screen output. A value of zero prevents the router from pausing between screens of output. Some types of terminal sessions do not require you to specify the screen length because the screen length specified can be learned by some remote hosts. For example, the rlogin protocol uses the screen length to set up terminal parameters on a remote UNIX host.

**Example:**

In the following example, the system is configured to prevent output from pausing if it exceeds the length of the screen:

```text
Router# terminal length 0
```


### `terminal monitor`

> **Página:** 1092 · **Modo:** EXEC · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To display debug command output and system error messages for the current terminal and session, use the

**Syntax:**

```text
terminal monitor command in EXEC mode.
terminal monitor
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Disabled

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Remember that all terminal parameter-setting commands are set locally and do not remain in effect after a session is ended.

**Example:**

In the following example, the system is configured to display debug command output and error messages during the current terminal session:

```text
Router# terminal monitor
```


### `terminal notify`

> **Página:** 1092 · **Modo:** EXEC · **Default:** N/A · **Leitura (show/clear/…):** não

**Description:** To enable terminal notification about pending output from other Telnet connections for the current session, use the terminal notify command in EXEC mode. To disable notifications for the current session, use the no form of this command.

**Syntax:**

```text
terminal notify
terminal no notify
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Enabling notifications may be useful if, for example, you want to know when another connection receives mail, or when a process has been completed. This command enables or disables notifications for only the current session. To globally set these notifications, use the notify line configuration command.

**Example:**

In the following example, notifications will be displayed to inform the user when output is pending on another connection:

```text
terminal notify
```


### `terminal padding`

> **Página:** 1093 · **Modo:** EXEC · **Default:** No padding · **Leitura (show/clear/…):** não

**Description:** To change the character padding on a specific output character for the current session, use the terminal padding command in EXEC mode.

**Syntax:**

```text
terminal padding ascii-number count
```

**Parameters (Syntax Description):**

- `ascii-number` — ASCII decimal representation of the character.
- `count` — Number of N U L L by t e s s e n t after the specified character, u p to255 padding characters in length.

**Command Default:** No padding

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Character padding adds a number of null bytes to the end of the string and can be used to make a string an expected length for conformity. Use this command when the attached device is an old terminal that requires padding after certain characters (such as ones that scrolled or moved the carriage). See the "ASCII Character Set and Hexidecimal Values" appendix for a list of ASCII characters.

**Example:**

The following example pads Ctrl-D (ASCII decimal character 4) with 164 NULL bytes:

```text
Router# terminal padding 4 164
```


### `terminal parity`

> **Página:** 1094 · **Modo:** EXEC · **Default:** No parity. · **Leitura (show/clear/…):** não

**Description:** To define the generation of the parity bit for the current terminal line and session, use the terminal parity command in EXEC mode.

**Syntax:**

```text
terminal parity {none | even | odd | space | mark}
```

**Parameters (Syntax Description):**

- `none` — No parity. This is the default.
- `even` — E v e n parity.
- `odd` — O d d parity.
- `space` — Space parity.
- `mark` — Mark parity.

**Command Default:** No parity.

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Communication protocols provided by devices such as terminals and modems will sometimes require a specific parity bit setting. Refer to the documentation for your device to determine required parity settings.

**Example:**

In the following example, odd parity checking is enabled for the current session:

```text
Router# terminal parity odd
```


### `terminal rxspeed`

> **Página:** 1094 · **Modo:** EXEC · **Default:** 9600 bps · **Leitura (show/clear/…):** não

**Description:** To set the terminal receive speed (how fast information is sent to the terminal) for the current line and session, use the terminal rxspeed command in EXEC mode.

**Syntax:**

```text
terminal rxspeed bps
```

**Parameters (Syntax Description):**

- `bps` — B a u d r at e in bits p e r s e c on d( b p s). The default is9600.

**Command Default:** 9600 bps

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Set the speed to match the baud rate of whatever device you have connected to the port. Some baud rates available on devices connected to the port might not be supported on the system. The system will indicate if the speed you select is not supported.

**Example:**

The following example sets the current auxiliary line receive speed to 115200 bps:

```text
Router# terminal rxspeed 115200
```


### `terminal special-character-bits`

> **Página:** 1095 · **Modo:** EXEC · **Default:** 7-bit ASCII character set · **Leitura (show/clear/…):** não

**Description:** To change the ASCII character widths to accept special characters for the current terminal line and session, use the terminal special-character-bits command in EXEC mode. 7 | 8

**Syntax:**

```text
terminal special-character-bits
```

**Parameters (Syntax Description):**

- `7` — S e l e c t s the7-b it ASCII characters e t. This is the default.
- `8` — S e l e c t s the full8-b it ASCII characters e t.

**Command Default:** 7-bit ASCII character set

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Configuring the width to 8 bits enables you to use twice as many special characters as with the 7-bit setting. This selection enables you to add special graphical and international characters in banners, prompts, and so on. This command is useful, for example, if you want the router to provide temporary support for international character sets. It overrides the default-value special-character-bits global configuration command and is used to compare character sets typed by the user with the special character available during a data connection, which includes software flow control and escape characters. When you exit the session, character width is reset to the width established by the default-value exec-character-bits global configuration command. Note that setting the EXEC character width to eight bits can cause failures. For example, if a user on a terminal that is sending parity enters the help command, an “unrecognized command” message appears because the Cisco IOS software is reading all eight bits, and the eighth bit is not needed for the help command.

**Example:**

The following example temporarily configures a router to use a full 8-bit user interface for system banners and prompts.

```text
terminal special-character-bits 8
```


### `terminal speed`

> **Página:** 1096 · **Modo:** EXEC · **Default:** 9600 bps · **Leitura (show/clear/…):** não

**Description:** To set the transmit and receive speeds of the current terminal line for the current session, use the terminal speed command in EXEC mode.

**Syntax:**

```text
terminal speed bps
```

**Parameters (Syntax Description):**

- `bps` — B a u d r at e in bits p e r s e c on d( b p s). The default is9600.

**Command Default:** 9600 bps

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Set the speed to match the transmission rate of whatever device you have connected to the port. Some baud rates available on devices connected to the port might not be supported on the router. The router indicates whether the speed you selected is not supported.

**Example:**

The following example restores the transmit and receive speed on the current line to 9600 bps:

```text
Router# terminal speed 9600
```


### `terminal start-character`

> **Página:** 1097 · **Modo:** EXEC · **Default:** Ctrl-Q (ASCII decimal character 17) · **Leitura (show/clear/…):** não

**Description:** To change the flow control start character for the current session, use the terminal start-character command in EXEC mode.

**Syntax:**

```text
terminal start-character ascii-number
```

**Parameters (Syntax Description):**

- `ascii-number` — ASCII decimal representation of the start character.
- `ascii-number` — ASCII decimal representation of the start character.

**Command Default:** Ctrl-Q (ASCII decimal character 17)

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The flow control start character signals the start of data transmission when software flow control is in effect.

**Example:**

The following example changes the start character to Ctrl-O (ASCII decimal character 15):

```text
Router# terminal start-character 15
```


### `terminal stopbits`

> **Página:** 1098 · **Modo:** EXEC · **Default:** 2 stop bits · **Leitura (show/clear/…):** não

**Description:** To change the number of stop bits sent per byte by the current terminal line during an active session, use the

**Syntax:**

```text
terminal stopbits command in EXEC mode.
terminal stopbits {1 | 1.5 | 2}
```

**Parameters (Syntax Description):**

- `1` — One stop b it.
- `1.5` — One and one-h a l f stopbits.
- `2` — Two stopbits. This is the default.

**Command Default:** 2 stop bits

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

Communication protocols provided by devices such as terminals and modems often require a specific stop-bit setting.

**Example:**

In the following example, the setting for stop bits is changed to one for the current session:

```text
Router# terminal stopbits 1
```


### `terminal stop-character`

> **Página:** 1098 · **Modo:** EXEC · **Default:** Ctrl-S (ASCII character decimal 19) · **Leitura (show/clear/…):** não

**Description:** To change the flow control stop character for the current session, use the terminal stop-character command in EXEC mode.

**Syntax:**

```text
terminal stop-character ascii-number
```

**Parameters (Syntax Description):**

- `ascii-number` — ASCII decimal representation of the stop character.

**Command Default:** Ctrl-S (ASCII character decimal 19)

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The flow control stop character signals the end of data transmission when software flow control is in effect. See the "ASCII Character Set and Hexidecimal Values" appendix for a list of ASCII characters.

**Example:**

In the following example, the stop character is configured as Ctrl-E (ASCII character decimal 5) for the current session:

```text
Router# terminal stop-character 5
```


### `terminal telnet break-on-ip`

> **Página:** 1099 · **Modo:** EXEC · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To cause an access server to generate a hardware Break signal when an interrupt-process (ip) command is received, use the terminal telnet break-on-ipcommand in EXEC mode.

**Syntax:**

```text
terminal telnet break-on-ip
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Disabled

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The hardware Break signal occurs when a Telnet interrupt-process (ip) command is received on that connection. The terminal telnet break-on-ip command can be used to control the translation of Telnet interrupt-process commands into X.25 Break indications. Note In this command, the acronym “ip” indicates “interrupt-process,” not Internet Protocol (IP). This command is also a useful workaround in the following situations: • Several user Telnet programs send an ip command, but cannot send a Telnet Break signal. • Some Telnet programs implement a Break signal that sends an ip command. Some EIA/TIA-232 hardware devices use a hardware Break signal for various purposes. A hardware Break signal is generated when a Telnet Break command is received. You can verify if this command is enabled with the show terminal EXEC command. If enabled the following line will appear in the output: Capabilities: Send BREAK on IP .

**Example:**

In the following example, a Break signal is generated for the current connection when an interrupt-process command is issued:

```text
terminal telnet break-on-ip
```


### `terminal telnet refuse-negotiations`

> **Página:** 1100 · **Modo:** EXEC · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To configure the current session to refuse to negotiate full-duplex, remote echo options on incoming connections, use the terminal telnet refuse-negotiations command in EXEC mode.

**Syntax:**

```text
terminal telnet refuse-negotiations
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Disabled

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You can set the line to allow access server to refuse full-duplex, remote echo connection requests from the other end . This command suppresses negotiation of the Telnet Remote Echo and Suppress Go Ahead options.

**Example:**

In the following example, the current session is configured to refuse full-duplex, remote echo requests:

```text
Router# terminal telnet refuse-negotiations
```


### `terminal telnet speed`

> **Página:** 1101 · **Modo:** EXEC · **Default:** 9600 bps (unless otherwise set using the speed, txspeed or rxspeed line configuration commands) · **Leitura (show/clear/…):** não

**Description:** To allow an access server to negotiate transmission speed for the current terminal line and session, use the

**Syntax:**

```text
terminal telnet speed command in EXEC mode.
terminal telnet speed default-speed maximum-speed
```

**Parameters (Syntax Description):**

- `default-speed` — Lines p e e d, in bits p e r s e c on d( b p s), that the access server will use if the device on the other end of the connection has not specified as p e e d.
- `maximum-speed` — Maximum lines p e e d in bits p e r s e c on d( b p s), that the device on the other end of the connection can use.

**Command Default:** 9600 bps (unless otherwise set using the speed, txspeed or rxspeed line configuration commands)

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You can match line speeds on remote systems in reverse Telnet, on host machines connected to an access server to access the network, or on a group of console lines connected to the access server when disparate line speeds are in use at the local and remote ends of the connections listed above. Line speed negotiation adheres to the Remote Flow Control option, defined in RFC 1080. Note This command applies only to access servers. It is not supported on standalone routers.

**Example:**

The following example enables the access server to negotiate a bit rate on the line using the Telnet option. If no speed is negotiated, the line will run at 2400 bps. If the remote host requests a speed greater than 9600 bps, then 9600 bps will be used.

```text
terminal telnet speed 2400 9600
```


### `terminal telnet sync-on-break`

> **Página:** 1101 · **Modo:** EXEC · **Default:** Disabled · **Leitura (show/clear/…):** não

**Description:** To cause the access server to send a Telnet Synchronize signal when it receives a Telnet Break signal on the current line and session, use the terminal telnet sync-on-break command in EXEC mode.

**Syntax:**

```text
terminal telnet sync-on-break
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** Disabled

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

You can configure the session to cause a reverse Telnet line to send a Telnet Synchronize signal when it receives a Telnet Break signal. The TCP Synchronize signal clears the data path, but still interprets incoming commands. Note This command applies only to access servers. It is not supported on standalone routers.

**Example:**

The following example sets an asynchronous line to cause the access server to send a Telnet Synchronize signal:

```text
terminal telnet sync-on-break
```


### `terminal telnet transparent`

> **Página:** 1102 · **Modo:** EXEC · **Default:** CR followed by an LF · **Leitura (show/clear/…):** não

**Description:** To cause the current terminal line to send a Return character (CR) as a CR followed by a NULL instead of a CR followed by a Line Feed (LF) for the current session, use the terminal telnet transparent command in EXEC mode.

**Syntax:**

```text
terminal telnet transparent
```

**Parameters (Syntax Description):**

- `—` — This command has no arguments or keywords.

**Command Default:** CR followed by an LF

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

The end of each line typed at the terminal is ended with a Return (CR). This command permits interoperability with different interpretations of end-of-line demarcation in the Telnet protocol specification. Note This command applies only to access servers. It is not supported on stand-alone routers.

**Example:**

In the following example, the session is configured to send a CR signal as a CR followed by a NULL:

```text
Router# terminal telnet transparent
```


### `terminal terminal-type`

> **Página:** 1103 · **Modo:** EXEC (>) Privileged EXEC (#) Diagnostic (diag) · **Default:** VT100 · **Leitura (show/clear/…):** não

**Description:** To specify the type of terminal connected to the current line for the current session, use the terminal terminal-type command in EXEC, privileged EXEC, and diagnostic mode.

**Syntax:**

```text
terminal terminal-type terminal-type
```

**Parameters (Syntax Description):**

- `terminal-type` — Defines the terminal name and type, and permits terminal n e g o t i at i on by hosts that provide
- `terminal-type` — Define s the terminal name and type, and permit s terminal n e g o t i at i on by hosts that p r o v id e that type of service. The default is VT100.

**Command Default:** VT100

**Command Modes:** EXEC (>) Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers, and be c a m e a v a i l a b l e in diagnostic mode. |

**Usage Guidelines:**

Indicate the terminal type if it is different from the default of VT100. The terminal type name is used by TN3270s for display management and by Telnet and rlogin to inform the remote host of the terminal type.

**Example:**

In the following example, the terminal type is defined as VT220 for the current session:

```text
Router# terminal terminal-type VT220
```


### `terminal txspeed`

> **Página:** 1103 · **Modo:** EXEC · **Default:** 9600 bps · **Leitura (show/clear/…):** não

**Description:** To set the terminal transmit speed (how fast the terminal can send information) for the current line and session, use the terminal txspeed command in EXEC mode.

**Syntax:**

```text
terminal txspeed bps
```

**Parameters (Syntax Description):**

- `bps` — B a u d r at e in bits p e r s e c on d( b p s). The default is9600 b p s.

**Command Default:** 9600 bps

**Command Modes:** EXEC

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Example:**

In the following example, the line transmit speed is set to 2400 bps for the current session:

```text
Router# terminal txspeed 2400
```


### `terminal width`

> **Página:** 1104 · **Modo:** EXEC (>) Privileged EXEC (#) Diagnostic (diag) · **Default:** 80 characters · **Leitura (show/clear/…):** não

**Description:** To set the number of character columns on the terminal screen for the current line for a session, use the

**Syntax:**

```text
terminal width command in EXEC, privileged EXEC, or diagnostic mode.
terminal width characters
```

**Parameters (Syntax Description):**

- `characters` — Number of character c o l u m n s d is p l a y e do n the terminal. The default is80 characters.

**Command Default:** 80 characters

**Command Modes:** EXEC (>) Privileged EXEC (#) Diagnostic (diag)

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |
| CiscoIOSXERelease2.1 | This command was introduced on the Cisco AS R1000 S e r i e s Routers, and be c a m e a v a i l a b l e in diagnostic mode. |

**Usage Guidelines:**

By default, the route provides a screen display width of 80 characters. You can reset this value for the current session if it does not meet the needs of your terminal. The rlogin protocol uses the value of the characters argument to set up terminal parameters on a remote host.

**Example:**

The following example sets the terminal character columns to 132:

```text
Router# terminal width 132
```


### `terminal-queue entry-retry-interval`

> **Página:** 1105 · **Modo:** Global configuration · **Default:** 60 seconds · **Leitura (show/clear/…):** não

**Description:** To change the retry interval for a terminal port queue, use the terminal-queue entry-rety-interval command in global configuration mode. To restore the default terminal port queue interval, use the no form of this command.

**Syntax:**

```text
terminal-queue entry-retry-interval seconds
no terminal-queue entry-retry-interval
```

**Parameters (Syntax Description):**

- `seconds` — Number of s e c on d s be t we enter min a l port retries. The default is60 s e c on d s.

**Command Default:** 60 seconds

**Command Modes:** Global configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 11.1 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

If a remote device (such as a printer) is busy, the connection attempt is placed in a terminal port queue. If you want to decrease the waiting period between subsequent connection attempts, decrease the default of 60 to an interval of 10 seconds. Decrease the time between subsequent connection attempts when, for example, a printer queue stalls for long periods.

**Example:**

The following example changes the terminal port queue retry interval from the default of 60 seconds to 10 seconds:

```text
Router# terminal-queue entry-retry-interval 10
```


### `terminal-type`

> **Página:** 1106 · **Modo:** Line configuration · **Default:** VT100 · **Leitura (show/clear/…):** não

**Description:** To specify the type of terminal connected to a line, use the terminal-type command in line configuration mode. To remove any information about the type of terminal and reset the line to the default terminal emulation, use the no form of this command.

**Syntax:**

```text
terminal-type {terminal-nameterminal-type}
no terminal-type
```

**Parameters (Syntax Description):**

- `terminal-name` — Terminal name.
- `terminal-type` — Terminal type.

**Command Default:** VT100

**Command Modes:** Line configuration

**Command History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release12.2(33) S R A. |

**Usage Guidelines:**

This command records the type of terminal connected to the line. The terminal-nameargument provides a record of the terminal type and allows terminal negotiation of display management by hosts that provide that type of service. For TN3270 applications, this command must follow the corresponding ttycap entry in the configuration file.

**Example:**

The following example defines the terminal on line 7 as a VT220:

```text
Router(config)# line 7
Router(config-line)# terminal-type VT220
```
