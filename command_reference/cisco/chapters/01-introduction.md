# Capítulo 1: Introduction

> Fonte: `cf_command_ref.pdf` · Cisco IOS · Configuration Fundamentals

### Introduction

• Introduction, on page 2

### Introduction

The Cisco IOS Configuration Fundamentals Command Reference provides command documentation associated with the following tasks: • Using the Cisco IOS Command-Line Interface (CLI) • Configuration Using Setup and AutoInstall • Configuring Operating Characteristics for Terminals • Managing Connections, Logins, Menus, and System Banners • Configure user menus and banners • Using the Cisco Web Browser User Interface (UI) • Using the HTTP server-based UI as an alternative to the CLI • Using the Cisco IOS Integrated File System (IFS) • The basics of filesystem use and Cisco IOS software’s filesystem infrastructure • Configuring Basic File Transfer Services • Copy, move, and delete files locally or across the network • Managing Configuration Files • Loading, Maintaining, and Upgrading System Images • Rebooting For further information about performing these tasks, refer to the Cisco IOS Configuration Fundamentals Configuration Guide for your release. Note Some commands previously documented in this Command Reference have been moved to other books: Commands related to system management and network monitoring can be found in the Cisco IOS Network Management Command Reference . Command reference documentation for the Cisco IOS software feature “Service Assurance Agent (SAA)” can be found in the the Cisco IOS IP SLAs Command Reference Some commands in this book use URLs (uniform resource locators) as part of the command syntax. URLs used in the Cisco IOS Integrated File System (IFS) contain two parts: a file system or network prefix, and a file identification suffix. The following tables list URL keywords that can be used in the source-url and destination-url arguments for all commands in this book. The prefixes listed below can also be used in the filesystem arguments in this document. The following table lists common URL network prefixes used to indicate a device on the network.

| Prefix | Description |
| --- | --- |
| ftp: | SpecifiesaFileTransferProtocol(FTP)networkserver. |
| rcp: | Specifiesanremotecopyprotocol(rcp)networkserver. |
| tftp: | SpecifiesaTFTPserver. |

The following table lists the available suffix options (file indentification suffixes) for the URL prefixes used in the previous table.

| Prefix | SuffixOptions |
| --- | --- |
| ftp: | [[//[username[:password]@]location]/directory]/filename Forexample: ftp://network-config(prefix://filename) ftp://user1:mypassword1@example.com/config-files |
| rcp: | rcp:[[//[username@]location]/directory]/filename |
| tftp: | tftp:[[//location]/directory]/filename |

The following table lists common URL prefixes used to indicate memory locations on the system.

| Prefix | Description |
| --- | --- |
| bootflash: | Bootflashmemory. |
| disk0: | Rotatingdiskmedia. |
| flash: partition-number | Flashmemory.Thisprefixisavailableonallplatforms.Forplatformsthatdonot haveadevicenamedflash:,theprefixflash:isaliasedtoslot0:. Therefore,youcanusetheprefixflash:torefertothemainFlashmemorystorage areaonallplatforms. |
| flh: | Flashloadhelperlogfiles. |
| null: | Nulldestinationforcopies.Youcancopyaremotefiletonulltodetermineits size. |
| nvram: | NVRAM.Thisisthedefaultlocationfortherunning-configurationfile. |
| slavebootflash: | InternalFlashmemoryonasecondaryRSPcardofarouterconfiguredwithDual RSPs. |
| slavenvram: | NVRAMonasecondaryRSPcard. |

| Prefix | Description |
| --- | --- |
| slaveslot0: | FirstPCMCIAcardonasecondaryRSPcard. |
| slaveslot1: | SecondPCMCIAcardonasecondaryRSPcard. |
| slot0: | FirstPCMCIAFlashmemorycard. |
| slot1: | SecondPCMCIAFlashmemorycard. |
| xmodem: | ObtainthefilefromanetworkmachineusingtheXmodemprotocol. |
| ymodem: | ObtainthefilefromanetworkmachineusingtheYmodemprotocol. |

For details about the Cisco IOS IFS, and for IFS configuration tasks, refer to the “Using the Cisco IOS Integrated File System (IFS)” chapter in the latest Cisco IOS Configuration Fundamentals Configuration Guide appropriate for your release version. For information on obtaining documentation, obtaining support, providing documentation feedback, security guidelines, and also recommended aliases and general Cisco documents, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at: http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html
