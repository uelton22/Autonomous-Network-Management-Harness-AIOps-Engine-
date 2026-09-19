# Capítulo 3: Management

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## CLI Settings

This chapter describes the commands related to management access in the DmOS CLI. CLI SETTINGS This topic describes the available settings used in a command-line interface (CLI) session. Changes on these settings are applied only to the current session.

### `debug`

> **Página:** 22 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** This command is used to enable or to disable debug messages. The debug messages are printed only on the user session that enabled the debugs and these messages are not logged. After user logout, the user session is closed and all enabled debugs of that session are automatically disabled.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
debug { enable | disable } [ link-status ]*
```

**Parameters:**

- `enable` — Enable the specified list of debug commands. — *Valores:* N/A · *Default:* N/A
- `disable` — Disable the specified list of debug commands or disable all debug commands enabled in the current user session. — *Valores:* N/A · *Default:* If none command is specified then the command “debug disable” will disable all debugs.
- `link-status` — Displays a debug message if a link status is changed. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.0 | This command was introduced. |

**Usage Guidelines:**

Use the debug enable command to see the debug messages of a command or a list of commands. And use the debug disable to see no more debug messages of all commands or of some commands.

**Impacts and precautions:**

The use of debug enable with many commands over serial interface may cause the session to become unresponsive to user intervention. Consider this before issuing the respective command.

**Hardware restrictions:**

N/A


### `display-defaults`

> **Página:** 25 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Shows default values as comments when showing the configuration. This setting is valid for the current session only.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
display-defaults {true|false}
```

**Parameters:**

- `{true|false}` — Sets display-defaults to true (enabled) or false (disabled). — *Valores:* true or false · *Default:* false

**Default:** The display of default values is disabled.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.10 | Command show-defaults was replaced by display-defaults |

**Usage Guidelines:**

If show-defaults is set to true, the default values, if available, are shown as comments after the actual parameter value: Examples:

```text
# display-defaults true
# show running-config aaa
aaa user admin
password $1$SzCHCSOa$IiVcIUUino2s12Wk1Rdwa/
group admin ! audit
!
# show running-config mac-address-table
mac-address-table
aging-time 600 ! 600
!
```

Note that even if the parameter is set to the default value, it is shown again in the comment.

**Impacts and precautions:**

This command takes effect for the current session only, if the change is to be made persistent, use command “session display-defaults” or “user <username> session display-defaults” instead.

**Hardware restrictions:**

N/A


### `screen-resize`

> **Página:** 27 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Adjust the screen size following the current size of screen being used. If the screen size is changed the command must be run again.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
screen-resize
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

Example:

```text
# screen-resize
```

In configuration mode:

```text
(config)# do screen-resize
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `session`

> **Página:** 29 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures global default CLI session parameters.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
session [complete-on-space {true|false}] [ignore-leading-space {true|false}] [idle-timeout seconds] [paginate {true|false}] [history size] [display-defaults {true|false}]
```

**Parameters:**

- `complete-on-space {true|false}` — Controls if command completion should be attempted when <space> is entered. Entering <tab> always results in command completion. — *Valores:* true or false · *Default:* false
- `ignore-leading-space {true|false}` — Controls if leading spaces should be ignored or not. This is useful to turn off when pasting commands into the CLI. — *Valores:* true or false · *Default:* true
- `idle-timeout seconds` — Maximum idle time before being logged out. Use 0 (zero) for for infinity. — *Valores:* 0-8192 · *Default:* 1800
- `paginate {true|false}` — Enables/Disables pagination of command output. — *Valores:* true or false · *Default:* true
- `history size` — Size of CLI command history. — *Valores:* 0-8192 · *Default:* 100
- `display-defaults {true|false}` — Controls if defaults values should be shown when displaying the configuration. The default values are shown as comments after the configured value. — *Valores:* true or false · *Default:* false

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 5.4 | The display-level option was removed. |

**Usage Guidelines:**

N/A

**Impacts and precautions:**

This command sets the default settings for new sessions. It can be overridden by the corresponding configuration in operational mode or “user <username> session” commands. Use “show cli” command in operational mode to check the actual values.

**Hardware restrictions:**

N/A


### `user`

> **Página:** 32 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures default CLI session parameters per user

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
user user-name [description description] [alias alias_name expansion command] [session [complete-on-space {true|false}] [ignore-leading-space {true|false}] [idle-timeout seconds] [paginate {true|false}] [history size] [display-defaults {true|false}]]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `user-name` — Name of the user for which the CLI options are being set. — *Valores:* Text · *Default:* N/A
- `description description` — Adds a description for the user. — *Valores:* Text · *Default:* N/A
- `alias alias_name` — Creates a command alias. — *Valores:* Text · *Default:* N/A
- `expansion command` — Sets the original command to be replaced by the alias. — *Valores:* Text · *Default:* N/A
- `session` — Configures session parameters to be used as default for the specified user. There settings can be overridden by the corresponding configuration in operational mode. Use “show cli” command in operational mode to check the actual values. — *Valores:* N/A · *Default:* N/A
- `complete-on-space {true|false}` — Controls if command completion should be attempted when <space> is entered. Entering <tab> always results in command completion. — *Valores:* true or false · *Default:* false
- `ignore-leading-space {true|false}` — Controls if leading spaces should be ignored or not. This is useful to turn off when pasting commands into the CLI. — *Valores:* true or false · *Default:* true
- `idle-timeout seconds` — Maximum idle time before being logged out. Use 0 (zero) for infinity. — *Valores:* 0-8192 · *Default:* 1800
- `paginate {true|false}` — Enables/Disables pagination of command output. — *Valores:* true or false · *Default:* true
- `history size` — Size of CLI command history. — *Valores:* 0-8192 · *Default:* 100
- `display-defaults {true|false}` — Controls if defaults values should be shown when displaying the configuration. The default values are shown as comments after the configured value. — *Valores:* true or false · *Default:* false

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

N/A

**Impacts and precautions:**

This command sets the default settings for a specified user. It can be overridden by the corresponding configuration in operational mode. Use “show cli” command in operational mode to check the actual values. There is no check whether the user exists or not in database. This allows remote logged users to have a customized CLI environment.

**Hardware restrictions:**

N/A INTERFACES This topic describes the commands related to management interfaces such as commands to configure console and Management-Ethernet (outband).


## Interfaces

### `interface mgmt`

> **Página:** 36 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures management interface.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
interface mgmt interface [ vrf vrf-name | description if-description | ipv4 address a.b.c.d/x | ipv6 { enable | address x:x:x:x::x/y [ eui-64 ] | nd ra { suppress | max-interval | min-interval | prefix x:x:x:x::x/y [ no-advertise | no-autoconfig | off-link ] } } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface` — Management Ethernet interface in chassis/slot/port. — *Valores:* chassis/slot/port · *Default:* N/A
- `vrf vrf-name` — Specifies the name of the VRF this interface will be associated with. Currently, it is possible to configure only the VRF ‘mgmt’. — *Valores:* string. · *Default:* N/A
- `description if-description` — Specifies the description of the interface. It may point out a more meaningful text about its purpose. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* Must be a valid string. · *Default:* N/A
- `ipv4 address a.b.c.d/x` — Specifies an IPv4 address and prefix length, in CIDR notation, to be assigned to management interface. — *Valores:* a.b.c.d/x. · *Default:* 192.168.0.25/24
- `ipv6 enable` — Enables/Disables IPv6 on management interface. When enabled, the system automatically configures an IPv6 link-local address to management interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 address x:x:x:x::x/y` — Specifies an IPv6 unicast address and prefix length to be assigned to management interface. — *Valores:* x:x:x:x::x/y. · *Default:* N/A
- `eui-64` — Sets 64-bit Extended Unique Identifier for specific IPv6 prefix on management interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 nd ra suppress` — Suppresses Router Advertisements on the management interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 nd ra prefix x:x:x:x::x/y` — Prefix Address to be advertised on the specified management interface. — *Valores:* x:x:x:x::x/y. · *Default:* N/A
- `ipv6 nd ra prefix x:x:x:x::x/y no-advertise` — Disable this prefix on Router Advertisement of management interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 nd ra prefix x:x:x:x::x/y no-autoconfig` — Disable auto configuration of hosts by management interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 nd ra prefix x:x:x:x::x/y off-link` — When disabled, indicates that this prefix can be used for on-link determination on management interface. — *Valores:* N/A · *Default:* Disabled.
- `ipv6 nd ra max-interval max-interval` — The maximum time allowed between sending unsolicited multicast router advertisements from the interface, in seconds. — *Valores:* Must be no less than 4 seconds and no greater than 1800 seconds. · *Default:* 600
- `ipv6 nd ra min-interval min-interval` — The minimum time allowed between sending unsolicited multicast router advertisements from the interface, in seconds. — *Valores:* Must be no less than 3 seconds and no greater than 0.75 * MaxRtrAdvInterval. · *Default:* 198

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 2.4 | IPv6 support. VRF support. |
| 4.8.0 | Support to IPv6 ND Router Advertisement. |

**Usage Guidelines:**

It is possible the use of only one IPv4 address and/or two IPv6 addresses on management interface. Command to configure IPv6 addresses will be available only if ipv6 enable is set for interface. Example below shows that IPv6 address configuration option appears after ipv6 enable is set.

```text
(config-mgmt-1/1/1)# ipv6 ?
```

Possible completions: enable Enable IPv6 on interface

```text
!
(config-mgmt-1/1/1)# ipv6 enable
!
(config-mgmt-1/1/1)# ipv6 ?
```

Possible completions: address IPv6 address enable Enable IPv6 on interface

```text
!
```

To find which management interface is configured with a specific IP address, it is possible to use the commands showed in the example below. Example: This example shows all management interfaces:

```text
# show running-config interface mgmt all
interface mgmt 1/1/1
ipv4 address 192.168.0.25/24
ipv6 enable
ipv6 address 2001:db8::10/32
!
```

Or in configuration mode:

```text
(config)# show interface mgmt all
interface mgmt 1/1/1
ipv4 address 192.168.0.25/24
ipv6 enable
ipv6 address 2001:db8::10/32
!
```

If no VRF is explicitly associated with the mgmt interface, it is associated with the global VRF by default. The following example shows how to associate a management interface with the ‘mgmt’ VRF:

```text
(config-mgmt-1/1/1)# ?
```

Possible completions: vrf Assign a VRF instance to the interface

```text
!
(config-mgmt-1/1/1)# vrf ?
```

Possible completions: <WORD> VPN Routing/Forwarding instance name mgmt

```text
!
(config-mgmt-1/1/1)# vrf mgmt
(config-mgmt-1/1/1)# commit
```

Commit complete.

**Impacts and precautions:**

Once the VRF associated with the mgmt interface is changed, any route in the previous VRF using it as output interface will be uninstalled. In order to keep the connectivity, you will need to configure the routes in the new VRF.

**Hardware restrictions:**

N/A


### `interface mgmt-osc`

> **Página:** 42 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures management OSC interfaces.

**Supported Platforms:** This command is supported only in the following platforms: DM4920.

**Syntax:**

```text
interface mgmt-osc id [ description { string }* ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `id` — Configure the management OSC interface. The ID is composed by chassis/slot/port. — *Valores:* chassis/slot/port · *Default:* N/A
- `description` — Specifies the description of the interface. It may point out a more meaningful text about its purpose. Valid characters are A-Z, a-z, 0-9 and @ # $ % & * ( ) - _ [ ] { } <> = + , . / " ; : ? ! |. — *Valores:* Must be a valid string. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |

**Usage Guidelines:**

This command should be used to configure the mgmt-osc interfaces. Example: This example is applied to id equal to 1/1/2. This id correspond to chassis 1, slot 1 and port 2. To set description DM4920(config)# interface mgmt-osc 1/1/2 DM4920(config-mgmt-osc-1/1/2)# description "test interface name" Special characters |(vertical bar), !(exclamation mark), ?(question mark) and ;(semicolon) can only be used inside “”(double quotes) as they are also valid commands on command line. Example: DM4920(config)# interface mgmt-osc 1/1/2 DM4920(config-mgmt-osc-1/1/2)# description "test_interface_name|!?;" DM4920(config-mgmt-osc-1/1/2)# commit Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show interface mgmt-osc`

> **Página:** 45 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display status and configuration of mgmt-osc interfaces.

**Supported Platforms:** This command is supported only in the following platforms: DM4920.

**Syntax:**

```text
show interface mgmt-osc id
```

**Parameters:**

- `id` — Interface id referencing chassis/slot/port respectively. — *Valores:* chassis/slot/port · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.0 | This command was introduced. |

**Usage Guidelines:**

Use this command to display status and configuration of mgmt-osc interfaces.

```text
DM4920# show interface mgmt-osc
CHASSIS
ID/SLOT
ID/PORT
ID Link Speed Description
-----------------------------------
1/1/2 Down - test_port_2
1/1/3 Up 100M -
```

The command also can be used specifing the id of the interface. Example:

```text
DM4920# show interface mgmt-osc 1/1/2
CHASSIS
ID/SLOT
ID/PORT
ID Link Speed Description
-----------------------------------
1/1/2 Down - test_port_2
```

**Output Terms:**

Output Description Link status The current interface link state (Up/Down). The current speed state (100M/1G if the link is up, - if the is link is Speed down). Description The configured textual description of the interface.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A CONFIGURATION This topic describes the commands related to configuration management such as commands to backup or view the running-config content.


## Configuration

### `banner login`

> **Página:** 48 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This configuration represents the banner displayed when accessing the equipment via console, SSH or Telnet. This banner will be displayed before username and password prompts.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
banner login banner-text
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `banner-text` — A text message representing the banner that will be shown before login on the equipment. The text can contain special characters including line breaks () and tabulations (). — *Valores:* Text with up to 3240 characters. · *Default:* None

**Default:** None

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. It is possible to format the message using the following special characters: • \n - New line • \t - Horizontal tab • \\ - Backslash Example: There are two ways to configure the login banner, the multiline mode and single line mode. In single line mode the banner text must be written in one line, if using spaces quotation marks will be required, to include line breaks use and to include tabs use . It is recommend to always include a line break at the end to avoid having the login prompt concatenated to the banner.

```text
# config
Entering configuration mode terminal
(config)# banner login "**************** BANNER ****************"
(config)# commit
```

Commit complete. It is possible to use the command show banner login to check how the banner will be displayed.

```text
# show banner login
```

Login banner will be displayed as shown inside <> < ************** ** BANNER ** ************** >

```text
#
```

To use multi-line mode, press Enter after banner login and use ctrl-D when finished.

```text
# config
Entering configuration mode terminal
(config)# banner login
(<Hit <cr> to enter in multi-line mode. Alternatively, enter a text between double quotes.
```

Remember to insert a line break at the end. See command reference for examples. Maximum length of 3240 characters.>): [Multiline mode, exit with ctrl-D.] > *********************************************************************************** > *** Only authorized personnel are allowed to access this piece of equipment. *** > *** Others are urged to log off IMMEDIATELY. *** > *** *** > *** Somente pessoal autorizado pode acessar este equipamento. *** > *** Outros, por favor, desconectar IMEDIATAMENTE. *** > *** *** > *********************************************************************************** > ctrl-D

```text
(config)# commit
```

Commit complete.

```text
(config)# exit
# show banner login
```

Login banner will be displayed as shown inside <> < *********************************************************************************** *** Only authorized personnel are allowed to access this piece of equipment. *** *** Others are urged to log off IMMEDIATELY. *** *** *** *** Somente pessoal autorizado pode acessar este equipamento. *** *** Outros, por favor, desconectar IMEDIATAMENTE. *** *** *** *********************************************************************************** >

```text
DM4610#
```

In multi-line mode, to use backslash, it is necessary include another backslash as escape character.

```text
(config)# banner login
(<Hit <cr> to enter in multi-line mode. Alternatively, enter a text between double quotes.
```

Remember to insert a line break at the end. See command reference for examples. Maximum length of 3240 characters.>): [Multiline mode, exit with ctrl-D.] > _____ _______ _____ ____ __ __ | __ \\ /\\|__ __|/\\ / ____/ __ \\| \\/ | | | | | / \\ | | / \\ | | | | | | \\ / | | | | |/ /\\ \\ | | / /\\ \\| | | | | | |\\/| | | |__| / ____ \\| |/ ____ \\ |___| |__| | | | | |_____/_/ \\_\\_/_/ \\_\\_____\\____/|_| |_| > ctrl-D

```text
(config)# commit
```

Commit complete.

```text
(config)# exit
# show banner login
```

Login banner will be displayed as shown inside <> < _____ _______ _____ ____ __ __ | __ \ /\|__ __|/\ / ____/ __ \| \/ | | | | | / \ | | / \ | | | | | | \ / | | | | |/ /\ \ | | / /\ \| | | | | | |\/| | | |__| / ____ \| |/ ____ \ |___| |__| | | | | |_____/_/ \_\_/_/ \_\_____\____/|_| |_| >

```text
#
```

**Impacts and precautions:**

Depending on the SSH client software and locale configuration, UTF-8 characters may not be displayed correctly in login banner text.

**Hardware restrictions:**

None.


### `clear`

> **Página:** 52 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Used to remove all configuration changes that were not committed, in other words, all uncommitted modifications made are discarded, returning the system to the state after the last commit.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
clear
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use the clear command. Modify the system configuration. In the example below, the management IP address is changed.

```text
# config
Entering configuration mode terminal
(config)# show interface
interface mgmt 1/1/1
ipv4 address 192.168.0.25/24
!
(config)# interface mgmt 1/1/1
(config-mgmt-1/1/1)# no ipv4 address
(config-mgmt-1/1/1)# ipv4 address 10.4.16.134/22
(config-mgmt-1/1/1)# exit
(config)# show interface
interface mgmt 1/1/1
ipv4 address 10.4.16.134/22
!
(config)#
```

Clear all existing modifications.

```text
(config)# clear
```

All configuration changes will be lost. Proceed? [yes, NO] yes

```text
(config)#
(config)# show interface
interface mgmt 1/1/1
ipv4 address 192.168.0.25/24
!
(config)#
```

**Impacts and precautions:**

All uncommitted changes will be lost.

**Hardware restrictions:**

N/A


### `commit`

> **Página:** 54 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Copies configurations from candidate-config to running-config or confirms a pending commit. After that, the new configurations will be applied to the equipment.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
commit [and-quit | no-confirm] [ comment text ] [ label text ] [ persist-id id ] [ save-running file-name ]
```

**Parameters:**

- `and-quit` — (Optional) Exits the configuration mode after completing the commit. — *Valores:* N/A · *Default:* N/A
- `no-confirm` — (Optional) Commits without asking the user for confirmation when required. — *Valores:* N/A · *Default:* N/A
- `comment text` — (Optional) Associates a comment with the commit. The comment can later be seen when examining rollback files. — *Valores:* Text · *Default:* N/A
- `label text` — (Optional) Associates a label with the commit. The label can later be seen when examining rollback files. — *Valores:* Text · *Default:* N/A
- `persist-id id` — (Optional) Specifies a pending commit to be confirmed. — *Valores:* Text · *Default:* N/A
- `save-running file-name` — (Optional) Saves runnig-config into a file after the command completion. — *Valores:* File name or path. · *Default:* N/A

**Default:** Copy candidate-config changes to running-config.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

N/A

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `commit`

> **Página:** 57 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Command used to confirm or abort a pending confirmed commit (see commit confirmed command for more details)

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
commit { abort | confirm } { persist-id id }
```

**Parameters:**

- `abort` — Aborts a pending confirmed commit — *Valores:* N/A · *Default:* N/A
- `confirm` — Confirms a pending confirmed commit — *Valores:* N/A · *Default:* N/A
- `persist-id id` — Specifies a commit confirmed to abort or confirm. This value is the same used in commit confirmed persist command — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced |

**Usage Guidelines:**

This command can be executed directly via CLI. Examples: The examples below shows how to use the command commit. Example 1 - Sequence of commands using commit confirm:

```text
# config exclusive
Entering configuration mode exclusive
```

Warning: uncommitted changes will be discarded on exit

```text
(config)# hostname TESTE-COMM
(config)# commit confirmed 1
```

Warning: The configuration will be reverted if you exit the CLI without performing the commit operation within 1 minutes. After applying a configuration using a specific timeout is possible to persist this configuration using the commit confirm command TESTE-COMM(config)# end

```text
TESTE-COMM# commit confirm
```

Commit complete. Configuration is now permanent Example 2 - Sequence of commands using commit abort:

```text
# config exclusive
Entering configuration mode exclusive
```

Warning: uncommitted changes will be discarded on exit TESTE-COMM(config)# hostname DTC01 TESTE-COMM(config)# commit confirmed 1 Warning: The configuration will be reverted if you exit the CLI without performing the commit operation within 1 minutes. DTC01(config)# end After applying a configuration using a specific timeout is possible to abort this configuration using the commit abort command

```text
DTC01# commit abort
```

Confirmed commit has been aborted. Old configuration will now be restored.

```text
TESTE-COMM#
```

Message from system at 1970-01-01 02:37:53... confirmed commit operation not confirmed by admin from cli configuration rolled back

**Output Terms:**

Output Description Shows a message Examples of this command are displayed in the Usage Guidelines indicating the field commit status

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `commit abort`

> **Página:** 60 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Aborts a pending confirmed commit.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
commit abort [persist-id id]
```

**Parameters:**

- `persist-id id` — (Optional) Specifies a pending commit to be aborted. — *Valores:* Text: persist id argument passed to commit confirmed command. · *Default:* N/A

**Default:** Abort pending confirmed commit.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

N/A

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `commit check`

> **Página:** 62 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Used to validate the modifications made on the candidate-config. Syntax validation, integrity restrictions, YANG model validation points and coherence callbacks are assessed.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
commit check
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Examples: This example shows how to use the commit check command. It includes a few additional steps only for better understanding. Executing the command when everything is ok.

```text
# config
(config)# hostname DmOS
(config)# commit check
Validation complete
(config)# commit
```

Commit complete. Trying to configure mgmt interface ipv4 address as loopback address it is not allowed.

```text
# config
DmOS(config)# interface mgmt 1/1/1
```

DmOS(config-mgmt-1/1/1)# show # existing configured IP interface mgmt 1/1/1 ipv4 address 10.4.16.129/22

```text
!
DmOS(config-mgmt-1/1/1)# ipv4 address 127.0.0.1/8
DmOS(config-mgmt-1/1/1)# exit
DmOS(config)# commit check
```

Failed: ’interface mgmt 1/1/1 ipv4 address’ (value "127.0.0.1/8"): IPv4 address cannot be configured as loopback address

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `commit confirmed`

> **Página:** 64 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Used to copy the current candidate-config to the running-config with a timeout. If the commit command is not executed before the timeout expires, then the configuration will be reverted to the configuration that was active before the command was issued.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
commit confirmed [ timeout [persist id] [ comment text ] [ label text ] [ save-running file-name ] [persist-id id] ]
```

**Parameters:**

- `timeout` — Sets the timeout (in minutes) to undo the commit. — *Valores:* 0-71582788 · *Default:* 10
- `persist id` — Creates a persistent confirmed commit to be used through different CLI sessions. — *Valores:* Text · *Default:* N/A
- `comment text` — Associates a comment with the commit. The comment can be later verified when, for example, displaying the stored commit list. — *Valores:* Text · *Default:* N/A
- `label text` — Associates a label with the commit. The label can be later verified when, for example, displaying the stored commit list. — *Valores:* Text · *Default:* N/A
- `save-running file-name` — Saves runnig-config into a file after the command completion. — *Valores:* File name. · *Default:* N/A
- `persist-id id` — Specifies an existing pending commit to be confirmed or updated. — *Valores:* Text · *Default:* N/A

**Default:** Undo the commited changes after the default timeout (10 minutes).

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Examples: These examples show how to use the “commit confirmed” command.

```text
# config exclusive
Entering configuration mode exclusive
```

Warning: uncommitted changes will be discarded on exit

```text
(config)# hostname DTC001
(config)# commit confirmed 30
```

Warning: The configuration will be reverted if you exit the CLI without performing the commit operation within 30 minutes. DTC001(config)# DTC001(config)# commit Commit complete. Configuration is now permanent. Commit confirmed without confirmation.

```text
# config exclusive
Entering configuration mode exclusive
```

Warning: uncommitted changes will be discarded on exit

```text
(config)# hostname DTC001
(config)# commit confirmed 2
```

Warning: The configuration will be reverted if you exit the CLI without performing the commit operation within 2 minutes. DTC001(config)# (after 2 minutes) Message from system at 1970-01-01 01:36:22... confirmed commit operation not confirmed by admin from cli configuration rolled back

```text
(config)#
```

Persisting a commit confirmed through CLI sessions.

```text
# config exclusive
Entering configuration mode exclusive
```

Warning: uncommitted changes will be discarded on exit

```text
(config)# hostname DTC001
(config)# commit confirmed 300 persist commit-confirmed-label
```

Commit complete. DTC001(config)# exit

```text
DTC001# exit
```

Connection to 10.4.16.129 closed. (open a new connection) Welcome to the DmOS CLI admin connected from 10.4.4.22 using ssh on DTC001

```text
DTC001# config exclusive
```

Aborted: confirmed commit in progress

```text
DTC001# commit persist-id commit-confirmed-label
```

Commit complete. Configuration is now permanent.

**Impacts and precautions:**

Only available in exclusive mode. To confirm the pending commit use the commit command. To abort the pending commit use the commit abort command. The pending commit will be aborted if the CLI session is terminated before confirming the commit, unless the persist argument is given. In the latter case, a future session may confirm the pending confirmed commit by supplying the persist id as an argument to the commit command using the persist-id parameter. During the period this pending commit exists, access to exclusive sessions are not allowed. Configurations from terminal sessions are allowed, but if the pending commit is aborted all changes will be lost.

**Hardware restrictions:**

N/A


### `compare file`

> **Página:** 68 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Command used to compare the running-config with a configuration previously saved into a file. The differences are marked with diff notation: • ‘+’ means config is present in the file, not in running-config; • ‘-’ means config is present in the running-config, not in the file;

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
compare file config-file-name [ pathfilter ]
```

**Parameters:**

- `config-file-name` — Specifies the file to be compared with the running-config. — *Valores:* Text · *Default:* N/A
- `pathfilter` — Filters a specific set of configuration for comparison. — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. The option ‘brief’ was removed. The command will always show only the 4.4 differences, not the whole configuration. |

**Usage Guidelines:**

This example shows how to use the compare file command. It includes a few additional steps only for better understanding. Example: Saving the current configuration and comparing it after some changes:

```text
DmOS# config
Entering configuration mode terminal
DmOS(config)# save current-cfg
```

DmOS(config)# alias alias_cmd01 expansion test1 DmOS(config-alias-alias_cmd01)# exit DmOS(config)# alias alias_cmd02 expansion test2 DmOS(config-alias-alias_cmd02)# exit DmOS(config)# alias alias_cmd03 expansion test3 DmOS(config-alias-alias_cmd03)# exit DmOS(config)# commit Commit complete. DmOS(config)# exit

```text
DmOS# compare file current-cfg
-alias alias_cmd01
- expansion test1
-!
-alias alias_cmd02
- expansion test2
-!
-alias alias_cmd03
- expansion test3
-!
```

Showing a removed config:

```text
# config
(config)# no alias alias_cmd01
(config)# exit
# compare file current-cfg
+alias alias_cmd01
+ expansion test1
+!
```

**Impacts and precautions:**

When TACACS+ authorization is enabled and the user is allowed to execute the command compare file the comparison will be performed in 2 different ways, depending on the config file format: a) If the config is stored in text format, which is the default format, the comparison will be done based on the user permission to execute each command present in the configfile. Thus, commands not allowed to be executed by the user will generate an error message in the comparison output. b) If the config is stored in XML format, no additional command authorization is needed for the user.

**Hardware restrictions:**

N/A


### `config`

> **Página:** 71 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Used to enter the equipment configuration mode and change its configurations.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
config [ terminal | exclusive ]
```

**Parameters:**

- `terminal` — Edits a private copy of the configuration without locking it. — *Valores:* N/A · *Default:* N/A
- `exclusive` — Creates a lock in candidate-config allowing only one exclusive session. The access using a different mode is allowed but attempts to change the configurations will be denied. — *Valores:* N/A · *Default:* N/A

**Default:** If no option is passed to the command terminal mode is used.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 4.0 | Removed ‘config shared’ command. |

**Usage Guidelines:**

This command can be executed directly via CLI. Examples: Accessing terminal mode.

```text
# config
Entering configuration mode terminal
(config)#
```

Accessing exclusive mode.

```text
# config exclusive
Entering configuration mode exclusive
```

Warning: uncommitted changes will be discarded on exit

```text
(config)#
```

Trying to open a second exclusive session.

```text
# config exclusive
```

Error: configuration database locked by: admin ssh (cli from 10.4.4.22) on since 1970-01-02 00:24:01 exclusive Aborted: configuration locked

**Impacts and precautions:**

Extra care must be taken with simultaneous edition (e.g. two or more opened sessions editing the same configuration) see commit command for more information.

**Hardware restrictions:**

N/A


### `file`

> **Página:** 74 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Used to perform file operations (e.g. rm/ls/cat/nano unix commands).

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
file { delete file-name | list | show file-name | edit file-name }
```

**Parameters:**

- `delete file-name` — Deletes a file. The file name must be provided. — *Valores:* File name. · *Default:* N/A
- `list` — Displays all the user-related files. — *Valores:* N/A · *Default:* N/A
- `show file-name` — Displays the content of a file. The file name must be provided. — *Valores:* File name. · *Default:* N/A
- `edit file-name` — Edits an existent file or creates a new one, if it does not already exist. The provided file name is limited to 255 characters and must not start with “.”, “-”, nor contain file paths. — *Valores:* File name. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 5.0 | The edit command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Examples: This example shows how to use the file command with each of the available parameters. It includes a few additional steps only for better understanding. List the system user files.

```text
# file list
#
```

Save a user configuration file and then, use the “file list” command to check if it was saved.

```text
# config
Entering configuration mode terminal
(config)# save users_cfg aaa user
Saving aaa user
(config)# exit
# file list
users_cfg
#
```

Display the ‘user_cfg’ file contents.

```text
# file show users_cfg
aaa user admin
password $1$QAI4eb9Y$177HyfRcnuW.jYO1DPG5M.
group admin
!
#
```

Delete the ‘user_cfg’ file.

```text
# file delete users_cfg
# file list
#
```

Edit the ‘user_cfg’ file contents.

```text
# file edit users_cfg
```

The file editor will be opened. Use CTRL+s to save the file and CTRL+x to exit the editor and return to DmOS CLI.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `hostname`

> **Página:** 77 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** This configuration represents the hostname of the equipment being configured. The configured value can be visualized in three different places. Consulting the equipment configuration through the protocols SNMP and NETCONF and looking at the CLI prompt.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
hostname name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `name` — A value representing the hostname of equipment. This value must contains letters [a-zA-Z], numbers [0-9] and any of the following special characters: [~‘@#$%ˆ&*()-_[]{}<>=+,./“\]. The host name can be up to 63 characters. Although allowed, the use of special characters is not recommended because it violates RFC 952 and RFC 1123, and therefore may cause problems in some applications. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |
| 5.4 | Underscore was introduced as a possible character for hostname. Added support for the following characters 5.6 [~‘@#$%ˆ&*()[]{}<>=+,./“\]. |
| 8.0 | Only admin user can configure Hostname. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use the hostname command. It includes a few additional steps only for better understanding.

```text
DM4610# config
Entering configuration mode terminal
DM4610(config)# hostname HOST-001
DM4610(config)# commit
```

Commit complete. HOST-001(config)# HOST-001(config)# exit

```text
HOST-001#
```

**Impacts and precautions:**

Not available.

**Hardware restrictions:**

Not available.


### `load factory-config`

> **Página:** 80 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Command used to load the factory configurations to the device.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
load factory-config
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.2 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use the load factory-config command and preserve the management configuration.

```text
# config
Entering configuration mode terminal
(config)# load factory-config
```

Loading. Done.

```text
(config)# interface mgmt 1/1/1
(config-mgmt-1/1/1)# ipv4 address 192.0.2.10/24
(config)# commit
```

Commit complete.

**Impacts and precautions:**

This command does not automatically commit the loaded configuration. The user must explicitly run the commit command in order to apply the loaded configuration on the running-config. The user must be careful to apply the factory configuration. It may cause the loss of the device management, because the IP address will be reset to the default value (192.168.0.25/24).

**Hardware restrictions:**

N/A


### `load merge`

> **Página:** 82 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Command used to merge the content of a file with the current configuration.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
load merge file
```

**Parameters:**

- `file` — Name of the file that contains the configuration to be loaded. — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Examples: This example shows how to use the ‘load merge’ command. A new user ‘datacom’ is created and stored together with ‘admin’ in the ‘users_cfg’ file. This file contains only ‘aaa user’ settings.

```text
(config)# aaa user datacom password 1234 group admin
(config-user-datacom)# exit
(config)# show
aaa user admin
password $1$uYMZohDj$gP/QPHc1kog5k6IopHNQh/
group admin
!
aaa user datacom
password $1$z9a2TqCc$23midDa3BihfOZlt86YfC1
group admin
!
...
(config)# save users_cfg aaa user
Saving aaa user
(config)#
```

A new user is created and the ‘datacom’ user is changed and the load merge command is used to restore its value. Note that the new user is not affected.

```text
(config)# aaa user newuser group audit
(config-user-newuser)# show
aaa user newuser
password $1$z9a2dtIk$23midDa3BihfOZlt86YfC1
!
(config)# aaa user datacom group config
(config-user-datacom)# show
aaa user datacom
password $1$z9a2TqCc$23midDa3BihfOZlt86YfC1
group config
!
(config-user-datacom)# exit
(config)# load merge users_cfg
```

Loading. 188 bytes parsed in 0.09 sec (1.93 KiB/sec)

```text
(config)# show
aaa user admin
password $1$uYMZohDj$gP/QPHc1kog5k6IopHNQh/
group admin
!
aaa user datacom
password $1$z9a2TqCc$23midDa3BihfOZlt86YfC1
group admin
!
aaa user newuser
password $1$z9a2dtIk$23midDa3BihfOZlt86YfC1
!
...
(config)#
```

**Impacts and precautions:**

This command does not automatically commit the loaded configuration. The user must explicitly run the commit command in order to apply the loaded configuration on the running-config. A valid file must exist in order to execute this command. It can be a XML file or a text file with CLI commands. Configuration not present in the file will not be affected by this command. When TACACS+ authorization is enabled and the user is allowed to execute the command load merge the merging will be performed based on all commands present in the file if it is stored in xml format. Otherwise, if it is stored in text format, which is the default format, the merge will be done individually for each command present in the file based on the user permission to execute it. Thus, commands not allowed to be executed by the user can affect the merge requiring the operation to be aborted.

**Hardware restrictions:**

N/A


### `load override`

> **Página:** 85 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** The current configuration is deleted and a new configuration is loaded from file.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
load override file
```

**Parameters:**

- `file` — Name of the file that contains the configuration to be loaded. — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Examples: This example shows how to use the ‘load override’. The initial configuration of equipment is stored in the ‘all_cfg’ file and then the management IP is changed.

```text
# config
Entering configuration mode terminal
(config)# show aaa
aaa user admin
password $1$uYMZohDj$gP/QPHc1kog5k6IopHNQh/
group admin
!
(config)# save all_cfg
```

A new user ‘datacom’ is created.

```text
(config)# aaa user datacom password 1234 group admin
(config-user-datacom)# exit
(config)# show aaa
aaa user admin
password $1$uYMZohDj$gP/QPHc1kog5k6IopHNQh/
group admin
!
aaa user datacom
password $1$z9a2TqCc$23midDa3BihfOZlt86YfC1
group admin
!
(config)#
```

The ‘load override’ command is used to restore the original configuration. Note that the new user is removed.

```text
(config-user-datacom)# exit
(config)# load override all_cfg
```

Loading. 188 bytes parsed in 0.09 sec (1.93 KiB/sec)

```text
(config)# show aaa
aaa user admin
password $1$uYMZohDj$gP/QPHc1kog5k6IopHNQh/
group admin
!
(config)#
```

**Impacts and precautions:**

This command does not automatically commit the loaded configuration. The user must explicitly run the commit command in order to apply the loaded configuration on the running-config. A valid file must exist in order to execute this command. It can be a XML file or a text file with CLI commands, but it MUST contain the complete configuration of the device, all missing configuration will be deleted, the equipment operation may be compromised. In some cases, the commit may fail if critical configuration is missing. When TACACS+ authorization is enabled and the user is allowed to execute the command load override the overriding will be performed based on all commands present in the file if it is stored in xml format. Otherwise, if it is stored in text format, which is the default format, the overriding will be done individually for each command present in the file based on the user permission to execute it. Thus, commands not allowed to be executed will not remain in the candidate config, resulting in a partial configuration to be committed.

**Hardware restrictions:**

N/A


### `resolved`

> **Página:** 88 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Used to resolve conflicts related to simultaneous configuration changes. For example, a conflict may occur if a user updates a configuration but another user commits an update in the same configuration before the first user can commit.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
resolved
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

Open 2 ssh sessions with the same equipment and access the configuration prompt from interface gigabit 1/1/1:

```text
(config)# interface gigabit-ethernet 1/1/1
(config-gigabit-ethernet-1/1/1)#
```

On ssh session 01, change the advertising-abilities as following:

```text
(config-gigabit-ethernet-1/1/1)# advertising-abilities 1Gfull 100Mful
```

On ssh session 02, change the advertising-abilities as following and commit:

```text
(config-gigabit-ethernet-1/1/1)# advertising-abilities 100Mfull
(config-gigabit-ethernet-1/1/1)# commit
```

Commit complete. Go back to ssh session 01 and try to commit. The system shall return the following message:

```text
(config-gigabit-ethernet-1/1/1)# commit
```

Aborted: there are conflicts. -------------------------------------------------------------------------- Resolve needed before configuration can be committed. View conflicts with the command ’show configuration’ and execute the command ’resolved’ when done, or exit configuration mode to abort. Conflicting configuration items are indicated with a leading ’!’ Conflicting users: admin It is possible to check the conflicting configuration by executing the command below:

```text
(config-gigabit-ethernet-1/1/1)# show configuration
! advertising-abilities 100Mfull 1Gfull
```

Finally, to solve this conflict an apply the configuration, execute the command sequence below:

```text
(config)# resolved
(config)# commit
```

Commit complete.

```text
(config)# interface gigabit-ethernet 1/1/1
(config-gigabit-ethernet-1/1/1)# show
interface gigabit-ethernet 1/1/1
no shutdown
negotiation
duplex full
speed 1G
advertising-abilities 100Mfull 1Gfull
mdix normal
!
```

**Output Terms:**

Output Description Displays a warning message Examples of this command are displayed in the Usage Guidelines informing about field. the configuration conflict.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `rollback configuration`

> **Página:** 91 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Used to return the current configuration to a previously committed configuration. All changes, from the selected number up to the newest, are rolled back. For example, if the rollback file number 5 is selected, the changes existing in the files 4, 3, 2, 1 and 0 are rolled back too.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
rollback configuration [ number ]
```

**Parameters:**

- `number` — Number that identifies the rollback file to be used. — *Valores:* 0-64 · *Default:* 0

**Default:** Return the current configuration to the most recently committed configuration, without activating it.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

These examples show how to use the rollback configuration command. It includes a few additional steps only for better understanding. Examples: Generating and visualizing the rollback files. First, it shows the configuration commit list to illustrate the system’s current state.

```text
# config
Entering configuration mode terminal
(config)# show configuration commit list
1970-01-01 07:28:32
```

SNo. ID User Client Time Stamp Label Comment ~~~~ ~~ ~~~~ ~~~~~~ ~~~~~~~~~~ ~~~~~ ~~~~~~~ 0 10051 admin cli 1970-01-01 07:28:12 1 10050 admin cli 1970-01-01 07:01:59 2 10049 admin cli 1970-01-01 06:29:00 3 10048 admin cli 1970-01-01 06:28:36 4 10047 admin cli 1970-01-01 05:36:01 5 10046 admin cli 1970-01-01 01:49:10 6 10045 admin cli 1970-01-01 01:45:42 7 10044 admin cli 1970-01-01 01:42:42 8 10042 admin cli 1970-01-01 01:32:03 9 10041 admin cli 1970-01-01 01:30:24 1.0.. 10040 admin cli 1970-01-01 01:24:45 Then, it configures two different alias and commit them assigning a label. Next, it creates more two alias and also commit them with another label.

```text
(config)# alias cmd-alias01 expansion test1
(config-alias-cmd-alias01)# exit
(config)# alias cmd-alias02 expansion test2
(config-alias-cmd-alias02)# exit
(config)# commit comment "add cmd-alias 1/2"
```

Commit complete.

```text
(config)# alias cmd-alias03 expansion test3
(config-alias-cmd-alias03)# exit
(config)# alias cmd-alias04 expansion test4
(config-alias-cmd-alias04)# exit
(config)# commit comment "add cmd-alias 3/4"
```

Commit complete.

```text
(config)# show configuration commit list
1970-01-01 07:30:56
```

SNo. ID User Client Time Stamp Label Comment ~~~~ ~~ ~~~~ ~~~~~~ ~~~~~~~~~~ ~~~~~ ~~~~~~~ 0 10053 admin cli 1970-01-01 07:30:49 add cmd-alias 3/4 1 10052 admin cli 1970-01-01 07:30:23 add cmd-alias 1/2 2 10051 admin cli 1970-01-01 07:28:12 3 10050 admin cli 1970-01-01 07:01:59 4 10049 admin cli 1970-01-01 06:29:00 5 10048 admin cli 1970-01-01 06:28:36 6 10047 admin cli 1970-01-01 05:36:01 7 10046 admin cli 1970-01-01 01:49:10 8 10045 admin cli 1970-01-01 01:45:42 9 10044 admin cli 1970-01-01 01:42:42 1.0.. 10042 admin cli 1970-01-01 01:32:03 The command below shows the resultant alias configuration.

```text
(config)# show configuration running alias
alias cmd-alias01
expansion test1
!
alias cmd-alias02
expansion test2
!
alias cmd-alias03
expansion test3
!
alias cmd-alias04
expansion test4
!
```

Finally, the command sequence below uses the rollback command to return the current configuration to a previously committed configuration. In this case, the last 2 commits (0 and 1) are rolled back.

```text
(config)# rollback configuration 1
(config)# commit
```

Commit complete. As a result, all alias specific configurations (previously configured in this example) were removed from the system.

```text
(config)# show configuration running alias
% No entries found.
```

**Impacts and precautions:**

The system stores a limited number of rollback files (65). If the maximum number is reached, then the oldest configuration is removed before creating a new one. The most recently committed configuration (the running configuration) is number 0, the next most recent is number 1, etc. This command does not automatically commit the rolled back configuration. The user must explicitly run the commit command in order to apply the configuration. When a firmware upgrade is performed some commands might have been modified and the use of rollback command might fail if the rollback contains commands modified between firmware versions. In this case it is recommended to execute the configuration step by step again. When TACACS+ authorization is enabled and the user is allowed to execute the command rollback configuration the operation will be done independent from the user permission to execute the commands in the rollback files.

**Hardware restrictions:**

N/A


### `rollback selective`

> **Página:** 95 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Used to return the current configuration to a previously committed configuration. Only the changes existing in selected rollback file are rolled back.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
rollback selective [ number ]
```

**Parameters:**

- `number` — Number that identifies the rollback file to be used. — *Valores:* 0-64 · *Default:* 0

**Default:** Return the current configuration to the most recently committed configuration, without activating it.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

These examples show how to use the rollback selective command. It includes a few additional steps only for better understanding. Examples: Generating and visualizing the rollback files. First, it shows the configuration commit list to illustrate the system’s current state.

```text
# config
Entering configuration mode terminal
(config)# show configuration commit list
1970-01-01 07:28:32
```

SNo. ID User Client Time Stamp Label Comment ~~~~ ~~ ~~~~ ~~~~~~ ~~~~~~~~~~ ~~~~~ ~~~~~~~ 0 10051 admin cli 1970-01-01 07:28:12 1 10050 admin cli 1970-01-01 07:01:59 2 10049 admin cli 1970-01-01 06:29:00 3 10048 admin cli 1970-01-01 06:28:36 4 10047 admin cli 1970-01-01 05:36:01 5 10046 admin cli 1970-01-01 01:49:10 6 10045 admin cli 1970-01-01 01:45:42 7 10044 admin cli 1970-01-01 01:42:42 8 10042 admin cli 1970-01-01 01:32:03 9 10041 admin cli 1970-01-01 01:30:24 1.0.. 10040 admin cli 1970-01-01 01:24:45 Then, it configures two different alias and commit them assigning a label. Next, it creates more two alias and also commit them with another label.

```text
(config)# alias cmd-alias01 expansion test1
(config-alias-cmd-alias01)# exit
(config)# alias cmd-alias02 expansion test2
(config-alias-cmd-alias02)# exit
(config)# commit comment "add cmd-alias 1/2"
```

Commit complete.

```text
(config)# alias cmd-alias03 expansion test3
(config-alias-cmd-alias03)# exit
(config)# alias cmd-alias04 expansion test4
(config-alias-cmd-alias04)# exit
(config)# commit comment "add cmd-alias 3/4"
```

Commit complete.

```text
(config)# show configuration commit list
1970-01-01 07:30:56
```

SNo. ID User Client Time Stamp Label Comment ~~~~ ~~ ~~~~ ~~~~~~ ~~~~~~~~~~ ~~~~~ ~~~~~~~ 0 10053 admin cli 1970-01-01 07:30:49 add cmd-alias 3/4 1 10052 admin cli 1970-01-01 07:30:23 add cmd-alias 1/2 2 10051 admin cli 1970-01-01 07:28:12 3 10050 admin cli 1970-01-01 07:01:59 4 10049 admin cli 1970-01-01 06:29:00 5 10048 admin cli 1970-01-01 06:28:36 6 10047 admin cli 1970-01-01 05:36:01 7 10046 admin cli 1970-01-01 01:49:10 8 10045 admin cli 1970-01-01 01:45:42 9 10044 admin cli 1970-01-01 01:42:42 1.0.. 10042 admin cli 1970-01-01 01:32:03 The command below shows the resultant alias configuration.

```text
(config)# show configuration running alias
alias cmd-alias01
expansion test1
!
alias cmd-alias02
expansion test2
!
alias cmd-alias03
expansion test3
!
alias cmd-alias04
expansion test4
!
```

Finally, the command sequence below uses the rollback selective command to return the current configuration to a previously committed configuration. In this case, the “commit 1” is rolled back.

```text
(config)# rollback selective 1
(config)# commit
```

Commit complete. As a result, all configurations applied by “commit 1” (previously configured in this example) were removed from the system.

```text
(config)# show configuration running alias
alias cmd-alias03
expansion test3
!
alias cmd-alias04
expansion test4
!
```

**Impacts and precautions:**

The system stores a limited number of rollback files (65). If the maximum number is reached, then the oldest configuration is removed before creating a new one. The most recently committed configuration (the running configuration) is number 0, the next most recent is number 1, etc. This command does not automatically commit the rolled back configuration. The user must explicitly run the commit command in order to apply the configuration. When a firmware upgrade is performed some commands might have been modified and the use of rollback command might fail if the rollback contains commands modified between firmware versions. In this case it is recommended to execute the configuration step by step again. When TACACS+ authorization is enabled and the user is allowed to execute the command rollback selective the operation will be done independent from the user permission to execute the commands present in the selected commit.

**Hardware restrictions:**

N/A


### `save`

> **Página:** 99 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Used to save all or parts of the current configuration to a file.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
save file [xml] [pathfilter]
```

**Parameters:**

- `file` — Name of the file where the configurations will be saved. — *Valores:* Text · *Default:* N/A
- `xml` — Save the configuration in XML format. If this parameter is not used the configuration will be saved in text format as visualized in show command. — *Valores:* N/A · *Default:* N/A
- `pathfilter` — Specify a filter to save only parts of the current configuration. — *Valores:* Text · *Default:* N/A

**Default:** Save the whole configuration using the same format as visualized in show command.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

The following examples show how to use the save command with each parameter. Examples: The command sequence below, shows how to save the current configuration into a file named cfg001.

```text
# config
(config)# save cfg001
(config)# exit
# file show cfg001
aaa user admin
password $1$BuQV.kcR$JkYGm./9vB8LJ5bjCjEpk1
group admin
!
router static 0.0.0.0/0 next-hop 10.4.16.1
!
...
interface gpon 1/1/7
upstream-fec
downstream-fec
no shutdown
!
interface gpon 1/1/8
upstream-fec
downstream-fec
no shutdown
!
```

The command sequence below, shows how to save the current configuration into a file named cfg002, using xml format.

```text
# config
(config)# save cfg002 xml
(config)# exit
# file show cfg002
<config xmlns="http://tail-f.com/ns/config/1.0">
<bfd xmlns="http://tail-f.com/ns/bfd-stub">
<stub>
</stub>
</bfd>
<config xmlns="urn:dmos">
<interface>
<gigabit-ethernet xmlns="urn:dmos:dmos-interface-ethernet">
<id>1/1/1</id>
<shutdown>false</shutdown>
<negotiation>true</negotiation>
<duplex>full</duplex>
<speed>1G</speed>
<advertising-abilities>1Gfull</advertising-abilities>
<mdix>normal</mdix>
</gigabit-ethernet>
...
<dot1q xmlns="http://tail-f.com/ns/example/vlan-manager">
<vlan>
<vlan-id>1</vlan-id>
<interface>
<interface-name>gigabit-ethernet 1/1/9</interface-name>
</interface>
</vlan>
</dot1q>
```

The command sequence below, shows how to save a partial configuration into a file named cfg003.

```text
# config
(config)# save cfg003 dot1q
Saving dot1q
(config)# exit
# file show cfg003
dot1q
vlan 1
interface gigabit-ethernet 1/1/9
!
!
!
```

The command sequence below, shows how to save a partial configuration into a file named cfg004, using xml format.

```text
# config
(config)# save cfg004 xml dot1q
```

Saving parts of the configuration.

```text
(config)# exit
# file show cfg004
<config xmlns="http://tail-f.com/ns/config/1.0">
<dot1q xmlns="http://tail-f.com/ns/example/vlan-manager">
<vlan>
<vlan-id>1</vlan-id>
<interface>
<interface-name>gigabit-ethernet 1/1/9</interface-name>
</interface>
</vlan>
</dot1q>
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show`

> **Página:** 103 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Used to display all running configuration (applied by commits) without the default values. It can be used to display all fields when editing a subgroup configuration (e.g. a specific user in users configuration).

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show { pathfilter }
```

**Parameters:**

- `pathfilter` — Specifies a filter to display only a specific configuration — *Valores:* Text · *Default:* N/A

**Default:** All running configuration are displayed

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

The examples below shows how to use the command show. Examples: Example 1:

```text
(config)# show
aaa user admin
password $1$UoyZaDJS$aUxgMRkWXhhKCRmzqwasd/
group admin
!
alias bla
expansion bla7
!
bfd
!
interface mgmt 1/1/1
ipv4 address 10.4.16.132/22
!
router static 0.0.0.0/0 next-hop 10.4.16.1
!
snmp agent enabled
snmp agent version v2c
snmp agent version v3
snmp agent max-message-size 50000
snmp community public
sec-name public
!
snmp notify std_v1_trap
tag std_v1_trap
!
snmp notify std_v2_inform
tag std_v2_inform
type inform
!
snmp notify std_v2_trap
tag std_v2_trap
!
```

Example 2:

```text
(config)# show aaa
aaa user admin
password $1$UoyZaDJS$aUxgMRkWXhhKCRmzqwasd/
group admin
!
```

**Output Terms:**

Output Description Displays information Examples of this command are displayed in the Usage Guidelines about the system field configuration

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show banner login`

> **Página:** 106 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display login banner.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show banner login
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `login` — Display login banner. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.6 | This command was introduced. |

**Usage Guidelines:**

```text
DM4610# show banner login
```

Login banner will be displayed as shown inside <> < *********************************************************************************** *** Only authorized personnel are allowed to access this piece of equipment. *** *** Others are urged to log off IMMEDIATELY. *** *** *** *** Somente pessoal autorizado pode acessar este equipamento. *** *** Outros, por favor, desconectar IMEDIATAMENTE. *** *** *** *********************************************************************************** >

```text
DM4610#
```

**Output Terms:**

Output Description Displays the login banner formatted as it will be shown on login via Login banner console, SSH or Telnet.

**Impacts and precautions:**

None.

**Hardware restrictions:**

None.


### `show configuration`

> **Página:** 108 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to list all uncommitted configuration changes.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show configuration { this | diff | merge } [ pathfilter ]
```

**Parameters:**

- `this` — Shows the configuration changes in CLI format. — *Valores:* N/A · *Default:* N/A
- `diff` — Shows the changes using diff notation. — *Valores:* N/A · *Default:* N/A
- `merge` — Shows the complete configuration merging the running configuration to the uncommitted changes. — *Valores:* N/A · *Default:* N/A
- `pathfilter` — Specifies a filter to display only a specific configuration change. — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

In order to check the “show configuration” command functionality, it is necessary to change the system default configuration and then execute: show configuration <path>. The example below, shows how to use the command show configuration. Example: If the candidate configuration is empty, the equipment shall return the message stated below:

```text
(config)# show configuration diff
% No configuration changes found.
```

The same idea applies when a module is specified:

```text
(config)# show configuration diff aaa
% No configuration changes found.
```

Now, to clarify the purpose and operation of this command, the example below will perform a change in the configuration. In this case, the gigabit-ethernet 1/1/1 interface was activated.

```text
(config)# interface gigabit-ethernet 1/1/1
(config-gigabit-ethernet-1/1/1)# no shutdown
(config-gigabit-ethernet-1/1/1)# exit
```

Then, it is possible to verify the diference between the candidate and commited configuration.

```text
(config)# show configuration this interface gigabit-ethernet 1/1/1
interface gigabit-ethernet 1/1/1
no shutdown
!
```

And if the user wants to check this difference using diff notation:

```text
(config)# show configuration diff interface gigabit-ethernet 1/1/1
interface gigabit-ethernet 1/1/1
- shutdown
+ no shutdown
!
```

**Output Terms:**

Output Description Displays the difference between the candidate Examples of this command are displayed in the Usage Guidelines and commited field configurations for the specified module.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show configuration commit changes`

> **Página:** 112 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to display the content of a commit file. A commit file is saved with new configurations any time a commit command is performed. These files can also be used in a rollback command.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show configuration commit changes [ diff ] [ id [ pathfilter ] ]
```

**Parameters:**

- `diff` — Marks the changes between running-config and rollback file using the diff notation. — *Valores:* N/A · *Default:* N/A
- `id` — For a valid value of id number, read the explanation example in the Usage Guidelines field. — *Valores:* Number · *Default:* N/A
- `pathfilter` — Specifies a filter to display only a specific configuration. — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

These examples show how to use the show configuration commit changes command. It includes a few additional steps only for better understanding. Examples: In the first boot of system the commit list is empty: Welcome to the DmOS CLI admin connected from 127.0.0.1 using console on

```text
# config
Entering configuration mode terminal
(config)# show configuration commit list
% no rollback files found
(config)#
```

If an invalid id is used the following message is displayed:

```text
(config)# show configuration commit changes 10
Error: invalid rollback number
```

Now, just to illustrate a pratical and valid command use, the command sequences below shall perform three configuration changes. First, the management IP address is changed and committed:

```text
(config)# interface mgmt 1/1/1
(config-mgmt-1/1/1)# no ipv4 address
(config-mgmt-1/1/1)# ipv4 address 10.4.16.132/22
(config-mgmt-1/1/1)# exit
(config)# commit
```

Commit complete.

```text
(config)#
```

Secondly, a static router is added and committed:

```text
(config)# router static 0.0.0.0/0 next-hop 10.4.16.1
(config-static-0.0.0.0/0/10.4.16.1)# exit
(config)# commit
```

Commit complete.

```text
(config)#
```

Finally, two new users are added and committed:

```text
(config)# aaa user datacom_1 password 1234 group admin
(config-user-datacom_1)# exit
(config)# aaa user datacom_2 password 1234 group admin
(config-user-datacom_2)# exit
(config)# commit
```

Commit complete.

```text
(config)#
```

Now the commit list has three items:

```text
(config)# show configuration commit list
1970-01-01 00:09:02
```

SNo. ID User Client Time Stamp Label Comment ~~~~ ~~ ~~~~ ~~~~~~ ~~~~~~~~~~ ~~~~~ ~~~~~~~ 0 10002 admin cli 1970-01-01 00:04:55 1 10001 admin cli 1970-01-01 00:04:44 2 10000 admin cli 1970-01-01 00:04:33

```text
(config)#
```

Summary descriptions of the command:

```text
(config)# show configuration commit ?
```

Possible completions: changes Changes for a given rollback id list Show commit history

```text
(config)# show configuration commit changes ?
```

Possible completions: 0 1970-01-01 00:04:55 by admin via cli 1 1970-01-01 00:04:44 by admin via cli 2 1970-01-01 00:04:33 by admin via cli --- diff Changes for a given rollback id <cr> latest

```text
(config)#
```

Using the command with its parameters:

```text
(config)# show configuration commit changes
!
! Created by: admin
! Date: 1970-01-01 00:04:55
! Client: cli
!
aaa user datacom_1
password $1$VmUU06GU$Cf36xMHMikZBXDxgwYsXW0
group admin
!
aaa user datacom_2
password $1$5dZ1FwQD$2SF8Q6K7pHMGnd7xGLWhS1
group admin
!
```

Showing changes that were committed for a given commit id (id = 0):

```text
(config)#
(config)# show configuration commit changes 0
!
! Created by: admin
! Date: 1970-01-01 00:04:55
! Client: cli
!
aaa user datacom_1
password $1$VmUU06GU$Cf36xMHMikZBXDxgwYsXW0
group admin
!
aaa user datacom_2
password $1$5dZ1FwQD$2SF8Q6K7pHMGnd7xGLWhS1
group admin
!
```

Showing changes that were committed for a given commit id (id = 1):

```text
(config)#
(config)# show configuration commit changes 1
!
! Created by: admin
! Date: 1970-01-01 00:04:44
! Client: cli
!
router static 0.0.0.0/0 next-hop 10.4.16.1
!
```

Showing changes that were committed for a given commit id (id = 2):

```text
(config)#
(config)# show configuration commit changes 2
!
! Created by: admin
! Date: 1970-01-01 00:04:33
! Client: cli
!
interface mgmt 1/1/1
no ipv4 address
ipv4 address 10.4.16.132/22
!
```

Showing the changes between running-config and rollback file (id = 0) using the diff notation:

```text
(config)#
(config)# show configuration commit changes diff 0
!
! Created by: admin
! Date: 1970-01-01 00:04:55
! Client: cli
!
+aaa user datacom_1
+ password $1$VmUU06GU$Cf36xMHMikZBXDxgwYsXW0
+ group admin
+!
+aaa user datacom_2
+ password $1$5dZ1FwQD$2SF8Q6K7pHMGnd7xGLWhS1
+ group admin
+!
```

Showing the changes between running-config and rollback file (id = 0) to a specific configuration (aaa) using the diff notation:

```text
(config)#
(config)# show configuration commit changes diff 0 aaa user datacom_2
!
! Created by: admin
! Date: 1970-01-01 00:04:55
! Client: cli
!
+aaa user datacom_2
+ password $1$5dZ1FwQD$2SF8Q6K7pHMGnd7xGLWhS1
+ group admin
+!
(config)#
```

**Output Terms:**

Output Description Displays the Examples of this command are displayed in the Usage Guidelines content of a field. commit file.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show configuration commit list.`

> **Página:** 117 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows a list including all configuration commits stored in the commit database.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show configuration commit list { num | pathfilter }
```

**Parameters:**

- `num` — Number of commit IDs (beginning with the most recent commit) that will be displayed — *Valores:* Positive number · *Default:* 100
- `pathfilter` — Specifies a filter to display only commit IDs that contain a specific configuration — *Valores:* Text · *Default:* N/A

**Default:** Show all existing files

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced |

**Usage Guidelines:**

Use the show configuration commit list command to list the commit IDs (up to 65) that are available for rollback. The newest 65 commits are stored by the system. As new commit IDs are added, the oldest commit IDs are discarded. Examples:

```text
(config)# show configuration commit list
2016-01-01 09:02:07
```

SNo. ID User Client Time Stamp Label Comment ~~~~ ~~ ~~~~ ~~~~~~ ~~~~~~~~~~ ~~~~~ ~~~~~~~ 0 10068 admin cli 2015-03-26 16:17:40 1 10067 admin cli 2015-03-26 16:15:03 2 10066 oper cli 2015-03-26 16:13:35 3 10065 admin cli 2015-03-26 14:43:03 4 10059 oper cli 2015-03-26 14:09:34 5 10058 oper cli 2015-03-26 13:55:31 6 10056 oper cli 2015-03-26 13:54:25 7 10054 admin cli 2015-03-26 13:45:39 8 10053 admin cli 2015-03-26 13:45:00 9 10051 admin cli 2015-03-26 13:43:26 10 10044 admin cli 2015-03-25 14:33:31 11 10043 admin cli 2015-03-25 14:32:47 12 10042 admin cli 2015-03-25 11:30:25 It is also possible to limit the number of commits displayed in the command output, by using the num parameter. The example below, shows the last 3 configuration commits executed by the user.

```text
(config)# show configuration commit list 3
2016-01-01 09:03:44
```

SNo. ID User Client Time Stamp Label Comment ~~~~ ~~ ~~~~ ~~~~~~ ~~~~~~~~~~ ~~~~~ ~~~~~~~ 0 10068 admin cli 2015-03-26 16:17:40 1 10067 admin cli 2015-03-26 16:15:03 2 10066 oper cli 2015-03-26 16:13:35 An example showing when a specific configuration filter is used:

```text
(config)# show configuration commit list aaa
2016-01-01 09:04:14
```

SNo. ID User Client Time Stamp Label Comment ~~~~ ~~ ~~~~ ~~~~~~ ~~~~~~~~~~ ~~~~~ ~~~~~~~ 0 10068 admin cli 2015-03-26 16:17:40 1 10067 admin cli 2015-03-26 16:15:03 12 10042 admin cli 2015-03-25 11:30:25

**Output Terms:**

Output Description The output displays the Examples of this command are displayed in the Usage Guidelines commit IDs that field are available for rollback

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show configuration rollback changes`

> **Página:** 120 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to display the changes applied after a specific commit file is used in a rollback command.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show configuration rollback changes [ diff ] [ id ]
```

**Parameters:**

- `diff` — Marks the changes using diff notation. — *Valores:* N/A · *Default:* N/A
- `id` — For a valid value of id number, read the explanation example in the Usage Guidelines field. — *Valores:* Number · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

These examples show how to use the show configuration rollback changes command. It includes a few additional steps only for better understanding. Examples: In the first boot of system the commit list is empty. Welcome to the DmOS CLI admin connected from 127.0.0.1 using console on

```text
# config
Entering configuration mode terminal
(config)# show configuration commit list
% no rollback files found
(config)#
```

If an invalid id is used the following message is displayed.

```text
(config)# show configuration rollback changes 10
Error: invalid rollback number
```

Now, just to illustrate a pratical and valid command use, the command sequences below shall perform three configuration changes. First, the management IP address is changed and committed.

```text
(config)# interface mgmt 1/1/1
(config-mgmt-1/1/1)# no ipv4 address
(config-mgmt-1/1/1)# ipv4 address 10.4.16.132/22
(config-mgmt-1/1/1)# exit
(config)# commit
```

Commit complete.

```text
(config)#
```

Secondly, a static router is added and committed.

```text
(config)# router static 0.0.0.0/0 next-hop 10.4.16.1
(config-static-0.0.0.0/0/10.4.16.1)# exit
(config)# commit
```

Commit complete.

```text
(config)#
```

Now the commit list has two items.

```text
(config)# show configuration commit list
1970-01-01 00:09:02
```

SNo. ID User Client Time Stamp Label Comment ~~~~ ~~ ~~~~ ~~~~~~ ~~~~~~~~~~ ~~~~~ ~~~~~~~ 0 10001 admin cli 1970-01-01 00:04:44 1 10000 admin cli 1970-01-01 00:04:33

```text
(config)#
```

Summary descriptions of the command.

```text
(config)# show configuration rollback ?
```

Possible completions: changes Changes for rolling back last n commits

```text
(config)# show configuration rollback changes ?
```

Possible completions: 0 1970-01-01 00:04:44 by admin via cli 1 1970-01-01 00:04:33 by admin via cli --- diff Changes for rolling back last n commits <cr> latest

```text
(config)#
```

Using the command with its parameters.

```text
(config)# show configuration rollback changes
no router static 0.0.0.0/0 next-hop 10.4.16.1
(config)#
(config)# show configuration rollback changes 0
no router static 0.0.0.0/0 next-hop 10.4.16.1
(config)#
(config)# show configuration rollback changes 1
interface mgmt 1/1/1
no ipv4 address
ipv4 address 192.168.0.25/24
!
no router static 0.0.0.0/0 next-hop 10.4.16.1
(config)#
(config)# show configuration rollback changes diff 1
interface mgmt 1/1/1
- ipv4 address 10.4.16.132/22
+ ipv4 address 192.168.0.25/24
!
-router static 0.0.0.0/0 next-hop 10.4.16.1
-!
(config)#
```

**Output Terms:**

Output Description Displays the changes applied after a specific Examples of this command are displayed in the Usage Guidelines commit file is field. used in a rollback command.

**Impacts and precautions:**

When a firmware upgrade is performed some commands might have been modified and the use of rollback command might fail if the rollback contains commands modified between firmware versions. In this case it is recommended to execute the configuration step by step again.

**Hardware restrictions:**

N/A


### `show configuration running`

> **Página:** 124 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to display all running configurations without the default values.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show configuration running [ pathfilter ]
```

**Parameters:**

- `pathfilter` — Specifies a filter to display only a specific configuration. — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples shows how to use the show configuration running command.

```text
# config
Entering configuration mode terminal
(config)# show configuration running
aaa user admin
password $1$DMOzVTxJ$pczOpWZo2hIU1Or0VUfce.
group admin
!
interface mgmt 1/1/1
ipv4 address 192.168.0.25/24
!
snmp agent enabled
snmp agent version v2c
snmp agent version v3
snmp agent max-message-size 50000
snmp community public
sec-name public
!
snmp vacm group public
member public
sec-model [ v2c ]
!
access v2c no-auth-no-priv
read-view root
write-view root
notify-view root
!
...
(config)#
# config
Entering configuration mode terminal
(config)# show configuration running interface
interface mgmt 1/1/1
ipv4 address 192.168.0.25/24
!
(config)#
```

**Output Terms:**

Output Description Displays the running configuration Examples of this command are displayed in the Usage Guidelines without its field. default values.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show running-config`

> **Página:** 127 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to display all the current configurations (applied by commits). The configurations with default values will not be displayed.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show running-config [ pathfilter ]
```

**Parameters:**

- `pathfilter` — Specifies a filter to display only a specific configuration. — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples shows how to use the show running-config command.

```text
# show running-config
aaa user admin
password $1$UoyZaDJS$aUxgMRkWXhhKCRmzLko1x/
group admin
!
bfd
!
interface mgmt 1/1/1
ipv4 address 10.4.16.132/22
!
router static 0.0.0.0/0 next-hop 10.4.16.1
!
snmp agent enabled
snmp agent version v2c
snmp agent version v3
snmp agent max-message-size 50000
snmp community public
sec-name public
!
snmp notify std_v1_trap
tag std_v1_trap
!
snmp notify std_v2_inform
tag std_v2_inform
...
```

If a filter is specified, the command returns only the respective configuration. For instance, the command below shows all management interface configuration

```text
# show running-config interface mgmt
interface mgmt 1/1/1
ipv4 address 10.4.16.132/22
!
#
```

**Output Terms:**

Output Description Displays the running configuration Examples of this command are displayed in the Usage Guidelines without its field. default values.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `top`

> **Página:** 130 · **Modo:** Configuration mode · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Used to exit to the top level of configuration mode or execute a command at the top level of the configuration.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
top [ command ]
```

**Parameters:**

- `command` — It is an optional parameter that specifies a command to be executed at the top level of configuration. — *Valores:* Text · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This examples shows how to use the top command. Exit to the top level of configuration mode.

```text
# config
Entering configuration mode terminal
(config)# aaa user config
(config-user-config)# top
(config)#
```

Execute a command at the top level of the configuration. In this example the command “interface l3 L3-name” is executed at the top of configuration creating a new interface but keep the actual configuration level.

```text
# config
Entering configuration mode terminal
(config)#aaa user config
(config-user-config)# top interface l3 L3-name
(config-user-config)#
(config-user-config)# show interface l3
interface l3 L3-name
!
(config-user-config)#
```

Execute the command top and enter in other configuration level. In this example using “;” is possible to execute top command and enter at interface l3 configuration level.

```text
# config
Entering configuration mode terminal
(config)#aaa user config
(config-user-config)# top ; interface l3 L3-name
(config-l3-L3-name)#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A FIRMWARE This topic describes the commands related to firmware management such as commands to identify current version or to execute an upgrade.


## Firmware

### `request firmware onu add`

> **Página:** 132 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** This command is used to download a remotely stored ONU firmware file and store it localy.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
request firmware onu add protocol://A.B.C.D/path/fw_name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `protocol://A.B.C.D/path/fw_name` — Download and store an ONU firmware file in the local device to be used in a remote device ONU update. This parameter specifies the ‘protocol’ (available protocol is TFTP); the remote server address ‘A.B.C.D’ (IPv4 address); and the path and name ‘path/fw_name’ of the firmware stored in the remote server. — *Valores:* Max. Length 765 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |
| 2.0 | The command was modified to remove remote option Added text to Impacts and precautions about ONU FW available flash 4.9 memory. |

**Usage Guidelines:**

Use the request firmware onu add command to download and store a new ONU firmware file in the local device.

**Impacts and precautions:**

There is up to 106 MB available for ONU firmware files in the equipment flash memory.

**Hardware restrictions:**

N/A


### `request firmware onu remove`

> **Página:** 134 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** This command is used to remove a ONU firmware file stored in the local device.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618.

**Syntax:**

```text
request firmware onu remove filename
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `filename` — Delete an ONU firmware file stored in the local device. This parameter specifies the name of the ONU firmware file to be removed. — *Valores:* Max. Length 255 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |

**Usage Guidelines:**

Use the request firmware onu remove command to delete a downloaded ONU firmware file from the local device.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A DIAGNOSTICS This topic describes the commands related to management diagnostic such as commands to verify some interface connection, to check CPU usage or to execute a traffic mirror.


## Diagnostics

### `clear core-dump`

> **Página:** 136 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Deletes a core-dump file of the list. Uses the file name.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
clear core-dump filename
```

**Parameters:**

- `filename` — Name of core dump file to be deleted — *Valores:* File name or ‘all’ to delete all core dumps · *Default:* No default value.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

To clear existing core-dump file, as in the example below.

```text
DM4610# clear core-dump core-file.5407.111222333.core.gz
Success!
DM4610#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `clear counters`

> **Página:** 138 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Clear statistics counters for User-Defined Counter instances. If no parameters are given all user-defined counters will be cleared.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
clear counters [ { ingress | egress } [ id counter-id ] ]
```

**Parameters:**

- `ingress` — Clear counters of ingress stage. If no IDs are given all counters of ingress stage will be cleared. — *Valores:* N/A · *Default:* N/A
- `egress` — Clear counters of egress stage. If no IDs are given all counters of egress stage will be cleared. — *Valores:* N/A · *Default:* N/A
- `id counter-id` — Counter ID to be cleared. It supports multiple IDs by using range/list syntax (e.g. 1-3,5). — *Valores:* 1 - 512 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.9 | This command was introduced. |

**Usage Guidelines:**

Given the equipment has ingress counters 1, 3, 5 and 7 and egress counters 2, 4, 6 and 8 configured.

```text
# show counters
INGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
1 One 6546 octets
3 Three 47984 octets
5 Five 1321 octets
7 Seven 71211 octets
EGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
2 Two 19655 octets
4 Four 75203 octets
6 Six 5616 octets
8 Eight 39458 octets
```

Let’s clear ingress counter 1:

```text
# clear counters ingress id 1
# show counters
INGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
1 One 0 octets
3 Three 47984 octets
5 Five 1321 octets
7 Seven 71211 octets
EGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
2 Two 19655 octets
4 Four 75203 octets
6 Six 5616 octets
8 Eight 39458 octets
```

Now let’s clear ingress counters 3 and 7 by using list syntax:

```text
# clear counters ingress id 3,7
# show counters
INGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
1 One 0 octets
3 Three 0 octets
5 Five 1321 octets
7 Seven 0 octets
EGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
2 Two 19655 octets
4 Four 75203 octets
6 Six 5616 octets
8 Eight 39458 octets
```

It is possible to clear multiple counters by using range syntax, so let’s clear egress counters from ID 4 up to ID 8. Note that in that range there are non-existent counters and they are going to be ignored:

```text
# clear counters egress id 4-8
```

Counter ID 5 doesn’t exist. Skipping... Counter ID 7 doesn’t exist. Skipping...

```text
# show counters
INGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
1 One 0 octets
3 Three 0 octets
5 Five 1321 octets
7 Seven 0 octets
EGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
2 Two 19655 octets
4 Four 0 octets
6 Six 0 octets
8 Eight 0 octets
```

To clear all counter of a given stage just omit the ID:

```text
# clear counters egress
# show counters
INGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
1 One 0 octets
3 Three 0 octets
5 Five 1321 octets
7 Seven 0 octets
EGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
2 Two 0 octets
4 Four 0 octets
6 Six 0 octets
8 Eight 0 octets
```

To clear all counters of all stages just omit all parameters:

```text
# clear counters
# show counters
INGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
1 One 0 octets
3 Three 0 octets
5 Five 0 octets
7 Seven 0 octets
EGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
2 Two 0 octets
4 Four 0 octets
6 Six 0 octets
8 Eight 0 octets
```

**Impacts and precautions:**

The clear operation is valid for all user interfaces. That means that a clear operation done through CLI, for example, will affect the values shown in all other user interfaces too i.e. SNMP and NETCONF.

**Hardware restrictions:**

None


### `clear statistics`

> **Página:** 142 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** This command clears the statistics counters of an interface.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
clear statistics interface-name
```

**Parameters:**

- `interface-name` — Interface id referencing chassis/slot/port respectively or an id referencing a specified LAG. — *Valores:* { { gigabit-ethernet | ten-gigabit-ethernet | twenty-fiveg-ethernet | forty-gigabit-ethernet | hundred-gigabit-ethernet | two-hundred-g-ethernet | four-hundred-g-ethernet } c/s/p | lag id } · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.2 | This command was introduced. |
| 3.0 | Added support for 40G interfaces. |
| 4.6 | Added support for 100G and LAG interfaces. |
| 5.0 | Added support for 25G. |
| 9.4 | Added support for 200G. |

**Usage Guidelines:**

The CLI and Netconf values are subject to this command and should not be used for accounting or billing.

**Impacts and precautions:**

Once issued, this command will set all counters to 0 on the network interface interface-name, on the CLI and NetConf access interfaces. Other access interfaces will not be cleared by this command. The values on these access interfaces should not be used for accounting or billing (see usage guidelines).

**Hardware restrictions:**

N/A


### `clear synchronization ptp statistics`

> **Página:** 144 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** This command clears the statistics counters of configured ptp interfaces.

**Supported Platforms:** This command is supported only in the following platforms: DM4376.

**Syntax:**

```text
clear synchronization ptp statistics
```

**Parameters:**

- `N/A` — N/A — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.6 | This command was introduced. |

**Usage Guidelines:**

Given the equipment has interface gigabit-ethernet-1/1/1 configured on synchronization.

```text
# show synchronization ptp interface statistics
interface gigabit-ethernet-1/1/1
```

Packet Type Received Received Processed Sent Discarded --------------------------------------------------------------------------- Sync 1 10 1000 100 Delay Request 2 3 5 4 Peer Delay Request 6 60 6000 60 Peer Delay Response 7 8 10 9 Follow Up 11 110 11000 1100 Delay Response 12 13 15 14 Peer Delay Follow Up 16 160 16000 1600 Announce 17 18 20 19 Signaling 21 210 21000 2100 Management 22 23 25 24 Now let’s clear synchronization ptp counters:

```text
# clear synchronization ptp statistics
# show synchronization ptp interface statistics
interface gigabit-ethernet-1/1/1
```

Packet Type Received Received Processed Sent Discarded --------------------------------------------------------------------------- Sync 0 0 0 0 Delay Request 0 0 0 0 Peer Delay Request 0 0 0 0 Peer Delay Response 0 0 0 0 Follow Up 0 0 0 0 Delay Response 0 0 0 0 Peer Delay Follow Up 0 0 0 0 Announce 0 0 0 0 Signaling 0 0 0 0 Management 0 0 0 0

**Impacts and precautions:**

A clear synchronization PTP operation done through CLI, for example, will affect the values from all synchronization PTP interfaces. When an interface is added or removed from the PTP synchronization interfaces list, all counters associated with all PTP interfaces will be reset as part of the API’s inherent behavior.

**Hardware restrictions:**

Platforms that supports Synchronism.


### `copy core-dump`

> **Página:** 147 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Copies a core-dump file using the TFTP or SCP protocol to valid host.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
copy core-dump filename protocol://ip-address/ [username login] [password pass] [source {ip-address | interface}]
```

**Parameters:**

- `filename` — Name of core dump file to be copied — *Valores:* File name or ‘all’ to copy all core dumps · *Default:* No default value.
- `protocol` — Protocol to be used to upload core dump file — *Valores:* tftp or scp · *Default:* None.
- `ip-address` — IP address of destination host. — *Valores:* a.b.c.d or X:X:X:X::X · *Default:* None.
- `username` — The username is required by SCP protocol. — *Valores:* Max. Length 40 · *Default:* N/A
- `password` — The password is required by SCP protocol. If ommited in the command, the system will ask for the password. — *Valores:* Max. Length 40 · *Default:* N/A
- `source {ip-address | interface}` — Specify the source ip address or the interface name where core dump file should be send through. — *Valores:* ip-address - IP address from a configured interface in a.b.c.d or X:X:X:X::X format; or interface - name of the management or l3 interface in l3-<name>, mgmt-<c>/<s>/<p> format. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. Changed parameters order and included ‘scp’ option for protocol param2.2 eter. |
| 2.4 | Included IPv6 and VRF support. |

**Usage Guidelines:**

To copy core-dump file to existing remote host using TFTP protocol as in the example below.

```text
DM4610# copy core-dump core-file.5407.111222333.core.gz tftp://172.22.110.12
```

Transfer complete.

```text
DM4610#
```

To copy core-dump file to existing remote host using SCP protocol as in the example below.

```text
DM4610# copy core-dump core-file.5407.111222333.core.gz scp://172.22.110.12/~
User name: user
Password: *****
```

Transfer complete.

```text
DM4610#
```

To copy core-dump file to existing remote host using SCP protocol and IPv6 as in the example below.

```text
DM4610# copy core-dump core-file.5407.111222333.core.gz scp://2001:db8::10/~
User name: user
Password: *****
```

Transfer complete.

```text
DM4610#
```

To copy core-dump file to existing remote host using TFTP protocol and source ip address as in the example below.

```text
DM4610# copy core-dump core-file.540.1.core.gz tftp://172.22.110.12 source 10.1.1.1
```

Transfer complete.

```text
DM4610#
```

To copy core-dump file to existing remote host using TFTP protocol and source interface as in the example below.

```text
DM4610# copy core-dump core-file.540.1.core.gz tftp://172.22.110.12 source l3-vlan200
```

Transfer complete.

```text
DM4610#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `copy file`

> **Página:** 151 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Copy file using TFTP or SCP protocol to/from valid host.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
copy file { local-filename | protocol://ip-address/remote-path } { protocol://ip-address/remote-path | remote-filename } [username login | password pass | port number | rename name | source {ip-address | interface} | time-stamped ]*
```

**Parameters:**

- `local-filename` — Name of local file to be copied to remote host. Names are limited to 255 characters and must not start with ‘.’ and ‘-’. — *Valores:* File name. · *Default:* N/A
- `protocol` — Protocol to be used to upload/download file — *Valores:* tftp or scp · *Default:* N/A
- `ip-address` — IP address of the host. — *Valores:* a.b.c.d or X:X:X:X::X. · *Default:* N/A
- `remote-path` — Remote file path. — *Valores:* File path. · *Default:* N/A
- `remote-filename` — Name of remote file to be copied from remote host. — *Valores:* File name. · *Default:* N/A
- `username login` — Specifies the login name to access a remote host. Use this only when protocol is scp. — *Valores:* Login name. · *Default:* N/A
- `password pass` — Specifies the login password to access a remote host. Use this only when protocol is scp. — *Valores:* Login password. · *Default:* N/A
- `port number` — Specifies the port number to access a remote host. — *Valores:* 0-65535. · *Default:* For tftp protocol is 69 and scp protocol is 22.
- `rename name` — Specifies the name to save file on device or remote host. Names are limited to 255 characters and must not start with ‘.’ and ‘-’. — *Valores:* File name. · *Default:* N/A
- `source {ip-address | interface}` — Specifies the source ip address or the interface name from which transfer should be started. — *Valores:* ip-address - IP address from a configured interface in a.b.c.d or X:X:X:X::X format; or interface - name of the management or l3 interface in l3-<name>, mgmt-<c>/<s>/<p> format. · *Default:* N/A
- `time-stamped` — Rename the transferred file in the server on device or remote host adding a suffix with the date in the following format YYYYMM-DD_hhmmss“. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |

**Usage Guidelines:**

To copy file to existing remote host using TFTP protocol.

```text
# copy file test tftp://1.2.1.1
```

Transfer complete.

```text
#
```

To copy file to existing remote IPv6 host using TFTP protocol.

```text
# copy file test tftp://2001:DB8::10
```

Transfer complete.

```text
#
```

To copy file to existing remote host using SCP protocol in a specific folder.

```text
# copy file test scp://1.2.1.1/dir/ username user password pass
```

Transfer complete.

```text
#
```

To copy file to existing remote host using SCP protocol in a specific folder and a specific port.

```text
# copy file test scp://1.2.1.1/dir/ username user password pass port 200
```

Transfer complete.

```text
#
```

To copy file to existing remote host using TFTP protocol in a specific folder.

```text
# copy file test tftp://1.2.1.1/dir/
```

Transfer complete.

```text
#
```

To copy file to existing remote host using TFTP protocol and rename the file.

```text
# copy file test tftp://1.2.1.1 rename test_renamed
```

Transfer complete.

```text
#
```

To copy file from existing remote host using TFTP protocol without rename.

```text
# copy file tftp://1.2.1.1 test
```

Transfer complete.

```text
#
```

To copy file from existing remote host using TFTP protocol and rename the file.

```text
# copy file tftp://1.2.1.1 test rename test_renamed
```

Transfer complete.

```text
#
```

To copy file from existing remote host using TFTP protocol with source IPv4 address.

```text
# copy file tftp://1.2.1.1 test source 1.1.1.1
```

Transfer complete.

```text
#
```

To copy file from existing remote host using TFTP protocol with source interface-name.

```text
# copy file tftp://1.2.1.1 test source mgmt-1/1/1
```

Transfer complete.

```text
#
```

To copy file from existing remote IPv6 host using TFTP protocol with source IPv6 address.

```text
# copy file tftp://2001::DB8::10 test source 2001:DB8::1
```

Transfer complete.

```text
#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `copy mibs`

> **Página:** 156 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Copies a compressed file containing the device MIB files via the TFTP or SCP protocol to a remote host.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
copy mibs protocol://ip-address/ [username login] [password pass] [source {ip-address | interface}]
```

**Parameters:**

- `protocol` — Protocol to be used to upload the compressed file. — *Valores:* tftp or scp · *Default:* None.
- `ip-address` — IP address of destination host. — *Valores:* a.b.c.d or X:X:X:X::X · *Default:* None.
- `username` — The username is required by the SCP protocol. — *Valores:* Max. Length 40 · *Default:* N/A
- `password` — The password is required by the SCP protocol. If ommited in the command, the system will prompt for the password. — *Valores:* Max. Length 40 · *Default:* N/A
- `source {ip-address | interface}` — Specifies the source IP address or the interface name from which the transfer should be initiated. — *Valores:* ip-address - IP address of a configured interface in a.b.c.d or X:X:X:X::X format; or interface - name of the management or l3 interface in l3-<name>, mgmt-<c>/<s>/<p> format. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4 | This command was introduced. |
| 5.6 | The parameter ‘source’ was added. |

**Usage Guidelines:**

Copying MIBs to a remote host using the TFTP protocol:

```text
DM4610# copy mibs tftp://172.22.110.12
```

File ’datacom-mibs.tar.gz’ successfully transferred.

```text
DM4610#
```

Copying MIBs to a remote host using the SCP protocol:

```text
DM4610# copy mibs scp://172.22.110.12/dir
User name: user
Password: *****
```

File ’datacom-mibs.tar.gz’ successfully transferred.

```text
DM4610#
```

Copying MIBs to a remote host using IPv6 and the SCP protocol:

```text
DM4610# copy mibs scp://2001:db8::10/dir
User name: user
Password: *****
```

File ’datacom-mibs.tar.gz’ successfully transferred.

```text
DM4610#
```

Copying MIBs to a remote host using the TFTP protocol and a source IP address:

```text
DM4610# copy mibs tftp://172.22.110.12 source 1.1.1.1
```

File ’datacom-mibs.tar.gz’ successfully transferred.

```text
DM4610#
```

Copying MIBs to a remote host using the SCP protocol and a source interface name:

```text
DM4610# copy mibs scp://172.22.110.12/dir source mgmt-1/1/1
User name: user
Password: *****
```

File ’datacom-mibs.tar.gz’ successfully transferred.

```text
DM4610#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `copy pcap`

> **Página:** 159 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Copies the pcap file generated by tcpdump using the TFTP or SCP protocol to valid host.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
copy pcap protocol://ip-address/ [username login] [password pass] [source {ip-address | interface}]
```

**Parameters:**

- `protocol` — Protocol to be used to upload pcap file — *Valores:* tftp or scp · *Default:* None.
- `ip-address` — IP address of destination host. — *Valores:* a.b.c.d or X:X:X:X::X · *Default:* None.
- `username` — The username is required by SCP protocol. If ommited in the command, the system will ask for the user-name. — *Valores:* Max. Length 40 · *Default:* N/A
- `password` — The password is required by SCP protocol. If ommited in the command, the system will ask for the password. — *Valores:* Max. Length 40 · *Default:* N/A
- `source {ip-address | interface}` — Specify the source IP address or the interface name where pcap file should be send through. — *Valores:* ip-address - IP address from a configured interface in a.b.c.d or X:X:X:X::X format; or interface - name of the management or l3 interface in l3-<name>, mgmt-<c>/<s>/<p> format. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 6.0 | This command was introduced. |

**Usage Guidelines:**

To copy pcap file to existing remote host using TFTP protocol as in the example below.

```text
# copy pcap tftp://172.22.110.12
```

Transfer complete.

```text
#
```

To copy pcap file to existing remote host using SCP protocol as in the example below.

```text
# copy pcap scp://172.22.110.12/~
User name: user
Password: *****
```

Transfer complete.

```text
#
```

To copy pcap file to existing remote host using SCP protocol and IPv6 as in the example below.

```text
# copy pcap scp://2001:db8::10/~
User name: user
Password: *****
```

Transfer complete.

```text
#
```

To copy pcap file to existing remote host using TFTP protocol and source ip address as in the example below.

```text
# copy pcap tftp://172.22.110.12 source 10.1.1.1
```

Transfer complete.

```text
#
```

To copy pcap file to existing remote host using TFTP protocol and source interface as in the example below.

```text
# copy pcap tftp://172.22.110.12 source l3-vlan200
```

Transfer complete.

```text
#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `counters`

> **Página:** 162 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create a User-Defined Counter instance.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
counters {ingress | egress} id counter-id type octets [description counter-description] {vlan vlan-id [inner-vlan vlan-id] | interface interface-name}*
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `ingress` — This parameter configures ingress user defined counters. — *Valores:* N/A · *Default:* N/A
- `egress` — This parameter configures egress user defined counters. — *Valores:* N/A · *Default:* N/A
- `id counter-id` — User defined counter identifier. — *Valores:* 1 - 512 · *Default:* N/A
- `type octets` — Define the type of data counted by this counter. — *Valores:* octets · *Default:* octets
- `description counter-description` — User defined counter description, used to identification. — *Valores:* String with a maximum of 128 characters. · *Default:* N/A
- `vlan vlan-id` — Apply this counter only in specific outer VLAN ID. — *Valores:* 1 - 4094 · *Default:* N/A
- `inner-vlan vlan-id` — Apply this counter only in specific inner VLAN ID. — *Valores:* 1 - 4094 · *Default:* N/A
- `interface interface-name` — Apply this counter only in specific interface. Multiple interface may be specified, and the counter will aggregate all these interfaces. — *Valores:* interface-type-chassis/slot/port | lag-id Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet and hundred-gigabit-ethernet. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.9 | This command was introduced. |
| 5.1 | Added support for 25G interfaces. |

**Usage Guidelines:**

Counters can be created specifying multiple interfaces to count only the traffic in the specified interfaces. Examples: The following example creates one counter instance to count the number of octets on the ingress side of VLAN 100 and interfaces gigabit-ethernet-1/1/4 and gigabit-ethernet-1/1/5.

```text
# config
Entering configuration mode terminal
(config)# counters
(counters)# ingress id 12
(counters-ingress-12)# vlan 100
(counters-ingress-12)# interface gigabit-ethernet-1/1/4
(counters-ingress-12)# interface gigabit-ethernet-1/1/5
(counters-ingress-12)# commit
```

Commit complete.

```text
(counters-ingress-12)#
```

**Impacts and precautions:**

With ACL: Ingress counters increment even for packets dropped by Ingress ACLs. With VLAN Mapping: For packets which Action Replace has been applied the inner-VLAN considered by the Ingress Counter is the VLAN that has just been replaced. On DM4270, DM4770 and DM4380 series: Ingress/Egress counters do not function when associated with VLANs in the selective encapsulation range (L2VPN Selective Encapsulation QinQ mode). Use a combined match of the service-delimiting VLAN and encapsulated VLANs as a workaround for ingress counters. No workaround is available for egress counters. Example of workaround for ingress counters: mpls l2vpn vpws-group SW-VPWS vpn VPWS-ENCAP qinq neighbor 10.10.10.11 pw-type vlan 1000 access-interface ten-gigabit-ethernet-1/1/1 encapsulation dot1q 50,60 counters ingress id 1 description "rx vlan50" type octets vlan 1000 inner-vlan 50 interface ten-gigabit-ethernet-1/1/1 ingress id 2 description "rx vlan60" type octets vlan 1000 inner-vlan 60 interface ten-gigabit-ethernet-1/1/1

**Hardware restrictions:**

On DM4611, DM4612 and DM4616 series: Ingress Counters are not supported. On DM4270, DM4770 and DM4380 series: it is not allowed to create an egress counter for an interface + VLAN when the interface is an untagged member of the VLAN. On DM4270, DM4770 and DM4380 series: Layer 2 Control Protocol tunneled packets are counted twice on matching ingress counters.


### `interface utilization`

> **Página:** 166 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** This command shows the port utilization bandwidth.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
show interface utilization interface-name [l1] [l2]
```

**Parameters:**

- `interface-name` — Single interface or a group of interfaces using regular expression. — *Valores:* String with a maximum of 64 characters. It accepts a string to match a single interface or a regular expression to match more than one interface (See Usage Guidelines). · *Default:* N/A
- `l1` — Displays L1 bandwidth utilization. — *Valores:* N/A · *Default:* N/A
- `l2` — Displays L2 bandwidth utilization. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.4 | This command was introduced. |

**Usage Guidelines:**

Example: Display L1 and L2 bandwidth of all available interfaces.

```text
#show interface utilization
```

Display L1 bandwidth of all available interfaces.

```text
#show interface utilization l1
```

Display L2 bandwidth of all available interfaces

```text
#show interface utilization l2
Repetition Mode
```

For monitoring the bandwidth it is useful to use this command within the <repeat> command: • Repeat the command every 2 seconds (default is 1 second):

```text
#show interface utilization forty* | repeat 2
```

Filtering interfaces: This command also has a property to refine and only display some interfaces. Some filters are: ^ | Matches the beginning of a string. [abc] | Character class, which matches any of the characters abc. Character ranges are specified by a pair of characters separated by a. r* | Matches zero or more rs. Common filters examples: • Match exactly an interface (pressing <tab> button will display all possible interfaces):

```text
#show interface utilization gigabit-ethernet-1/1/1
• Filter for forty-gigabit-ethernet interfaces (when available):
#show interface utilization forty*
• Filter for interfaces presents in chassis 1 and slot 2 (when available):
#show interface utilization *1/2/*
• Filter for forty-gigabit-ethernet interfaces and ten-gigabit-ethernet (when available):
#show interface utilization [ft]*
• Filter for any interfaces presents in chassis 1 and any slot (when available):
#show interface utilization *1/*/*
• Filter for a range of interfaces presents in chassis 1 and slot 2 (when available):
#show interface utilization *1/2/2-5
• Filter for some interfaces presents in chassis 1 and slot 2 (when available):
#show interface utilization *1/2/2,7,10
```

**Output Terms:**

Output Description L1 TX Bandwidth L1 bandwidth TX utilization. L1 RX Bandwidth L1 bandwidth RX utilization. L2 TX Bandwidth L2 bandwidth TX utilization. L2 RX Bandwidth L2 bandwidth RX utilization.

**Impacts and precautions:**

When the interval between the two last executions of this command is less than 1 minute, the measured and displayed bandwidth is the mean bandwidth during this interval. When the interval is greater than 1 minute, the displayed value is the instantaneous bandwidth. When this command is executed in more than one user session at the same time, the bandwidth value displayed is not guaranteed to be accurate. For more accurate results, use this command with <repeat> option in a single user session (See Usage Guidelines).

**Hardware restrictions:**

N/A


### `monitor session`

> **Página:** 170 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Create a monitor session and configure its parameters.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
monitor session id monitor session id destination interface interface-name monitor session id source interface interface-name [ traffic-type ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `monitor session id` — Sets the monitor session id. — *Valores:* 1 · *Default:* None
- `destination interface interface-name` — Sets the destination port for the monitoring session. — *Valores:* interface-type-chassis/slot/port Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet. · *Default:* None
- `source interface interface-name` — Adds a source port to the monitoring session. — *Valores:* interface-type-chassis/slot/port | lag-id Examples of interface-type: gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet. · *Default:* None
- `traffic-type` — Sets the traffic type to monitor on a source interface. — *Valores:* rx | tx | all · *Default:* rx (monitor the received traffic only)

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.2 | This command was introduced. |
| 5.0 | Added support for 25G interfaces. |

**Usage Guidelines:**

Example: This example shows how to create a monitor session.

```text
#config
Entering configuration mode terminal
(config)# monitor session 1
(monitor-session-1)# destination interface gigabit-ethernet-1/1/1
(monitor-session-1-destination)# exit
(monitor-session-1)# source interface ten-gigabit-ethernet-1/1/1 tx
(monitor-session-source-interface-gigabit-ethernet-1/1/1)# top
(config)# commit
```

Commit complete.

```text
(config)#
```

When adding a source interface to the monitor session, the default behaviour is to monitor its received traffic. Inside the interface configuration tree, the command tx or all will change the monitored traffic type.

**Impacts and precautions:**

• Only one monitor session is available for configuration. • Only pre-existing interfaces will be accepted when entering an interface name. • A LAG cannot be used as the session destination interface. • A LAG and its members cannot be used as source interfaces in the same monitor session. • The mirrored traffic is subjected to the QoS and shaping rules of the destination interface.

**Hardware restrictions:**

N/A


### `ping`

> **Página:** 173 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Ping is a utility that uses the ICMP protocol to test connectivity between IP networks devices.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
ping ipv4-address [ vrf name | size number | count number | interval time | fragment type | tos number | source {ip-address | interface} ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `ipv4-address` — The IPv4 address destination to verify the reachability. — *Valores:* a.b.c.d · *Default:* None.
- `vrf name` — The name of VRF to use. — *Valores:* Any VRF created. · *Default:* None.
- `size number` — ICMP payload size. — *Valores:* 0 - 65507 · *Default:* 56.
- `count number` — Number of packets to be sent. — *Valores:* 1 - 1000000000 · *Default:* 5.
- `interval number` — Time interval in seconds to generate each packet. — *Valores:* 1.0 - 86400.0 · *Default:* 1.0
- `fragment type` — Set the Path MTU Discovery strategy: The value prohibit prohibits fragmentation, even local one. The value discover does PMTU discovery, fragment locally when packet size is large. The value permit does not change fragmentation mode. — *Valores:* {prohibit | discover | permit} · *Default:* permit.
- `tos number` — Set Type of Service bits. — *Valores:* 0 - 255 · *Default:* None.
- `source {ip-address | interface}` — Specify the source IP address or the interface name from which packets should be sent. — *Valores:* ip-address - IP address from a configured interface in a.b.c.d format; or interface - name of the management or l3 interface in l3-<name>, mgmt-<c>/<s>/<p> format. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 5.4 | Added VRF support. |

**Usage Guidelines:**

The following example demonstrates how to use the ping command without any parameter. It will send 5 ICMP probes to the destination host.

```text
# ping 10.0.121.80
```

PING 10.0.121.80 (10.0.121.80) 56(84) bytes of data. 64 bytes from 10.0.121.80: icmp_seq=1 ttl=64 time=0.015 ms 64 bytes from 10.0.121.80: icmp_seq=2 ttl=64 time=0.033 ms 64 bytes from 10.0.121.80: icmp_seq=3 ttl=64 time=0.019 ms 64 bytes from 10.0.121.80: icmp_seq=4 ttl=64 time=0.033 ms 64 bytes from 10.0.121.80: icmp_seq=5 ttl=64 time=0.036 ms --- 10.0.121.80 ping statistics --- 5 packets transmitted, 5 received, 0% packet loss, time 3999ms rtt min/avg/max/mdev = 0.015/0.027/0.036/0.009 ms The following example demonstrates how to use the ping command with the “count” parameter:

```text
# ping 10.0.121.80 count 2
```

PING 10.0.121.80 (10.0.121.80) 56(84) bytes of data. 64 bytes from 10.0.121.80: icmp_seq=1 ttl=64 time=0.023 ms 64 bytes from 10.0.121.80: icmp_seq=2 ttl=64 time=0.034 ms --- 10.0.121.80 ping statistics --- 2 packets transmitted, 2 received, 0% packet loss, time 999ms rtt min/avg/max/mdev = 0.023/0.028/0.034/0.007 ms The following example demonstrates how to use the ping command with the “size” parameter:

```text
# ping 10.0.121.80 size 1500
```

PING 10.0.121.80 (10.0.121.80) 1500(1528) bytes of data. 1508 bytes from 10.0.121.80: icmp_seq=1 ttl=64 time=0.018 ms 1508 bytes from 10.0.121.80: icmp_seq=2 ttl=64 time=0.035 ms 1508 bytes from 10.0.121.80: icmp_seq=3 ttl=64 time=0.034 ms 1508 bytes from 10.0.121.80: icmp_seq=4 ttl=64 time=0.035 ms 1508 bytes from 10.0.121.80: icmp_seq=5 ttl=64 time=0.037 ms --- 10.0.121.80 ping statistics --- 5 packets transmitted, 5 received, 0% packet loss, time 3999ms rtt min/avg/max/mdev = 0.018/0.031/0.037/0.009 ms The following example demonstrates how to use the ping command with the “source” parameter using ip address:

```text
# ping 10.0.121.80 source 200.20.136.10
```

PING 10.0.121.80 (10.0.121.80) from 200.20.136.10 : 56(84) bytes of data. 64 bytes from 10.0.121.80: icmp_seq=1 ttl=64 time=0.018 ms 64 bytes from 10.0.121.80: icmp_seq=2 ttl=64 time=0.035 ms 64 bytes from 10.0.121.80: icmp_seq=3 ttl=64 time=0.034 ms 64 bytes from 10.0.121.80: icmp_seq=4 ttl=64 time=0.035 ms 64 bytes from 10.0.121.80: icmp_seq=5 ttl=64 time=0.037 ms --- 10.0.121.80 ping statistics --- 5 packets transmitted, 5 received, 0% packet loss, time 3999ms rtt min/avg/max/mdev = 0.018/0.031/0.037/0.009 ms The following example demonstrates how to use the ping command with the “source” parameter using interface name:

```text
# ping 10.0.121.80 source mgmt-1/1/1
```

PING 10.0.121.80 (10.0.121.80) from 11.12.0.14 eth0: 56(84) bytes of data. 64 bytes from 10.0.121.80: icmp_seq=1 ttl=64 time=0.018 ms 64 bytes from 10.0.121.80: icmp_seq=2 ttl=64 time=0.035 ms 64 bytes from 10.0.121.80: icmp_seq=3 ttl=64 time=0.034 ms 64 bytes from 10.0.121.80: icmp_seq=4 ttl=64 time=0.035 ms 64 bytes from 10.0.121.80: icmp_seq=5 ttl=64 time=0.037 ms --- 10.0.121.80 ping statistics --- 5 packets transmitted, 5 received, 0% packet loss, time 3999ms rtt min/avg/max/mdev = 0.018/0.031/0.037/0.009 ms

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `ping6`

> **Página:** 178 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Ping6 is a utility that uses the ICMPv6 protocol to test connectivity between IP networks devices.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
ping6 ipv6-address [ vrf name | size number | count number | interval time | tos number | source {ip-address | interface} ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `ipv6-address` — The IPv6 address destination to verify the reachability. — *Valores:* X:X:X:X::X. · *Default:* None.
- `vrf name` — The name of VRF to use. — *Valores:* Any VRF created. · *Default:* None.
- `size number` — ICMPv6 payload size. — *Valores:* 0 - 65507 · *Default:* 56.
- `count number` — Number of packets to be sent. — *Valores:* 1 - 1000000000 · *Default:* 5.
- `interval number` — Time interval in seconds to generate each packet. — *Valores:* 1.0 - 86400.0 · *Default:* 1.0
- `tos number` — Set Traffic Class bits. — *Valores:* 0 - 255 · *Default:* None.
- `source {ip-address | interface}` — Specify the source IP address or the interface name from which packets should be sent. — *Valores:* ip-address - IP address from a configured interface in X:X:X:X::X format; or interface - name of the management or l3 interface in l3-<name>, mgmt-<c>/<s>/<p> format. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | This command was introduced. |
| 6.0 | Added VRF support. |

**Usage Guidelines:**

The following example demonstrates how to use the ping6 command without any parameter. It will send 5 ICMPv6 probes to the destination host:

```text
# ping6 2001:DB8::1
```

PING 2001:DB8::1(2001:DB8::1) 56 data bytes 64 bytes from 2001:DB8::1: icmp_seq=1 ttl=64 time=0.027 ms 64 bytes from 2001:DB8::1: icmp_seq=2 ttl=64 time=0.028 ms 64 bytes from 2001:DB8::1: icmp_seq=3 ttl=64 time=0.038 ms 64 bytes from 2001:DB8::1: icmp_seq=4 ttl=64 time=0.038 ms 64 bytes from 2001:DB8::1: icmp_seq=5 ttl=64 time=0.051 ms --- 2001:DB8::1 ping statistics --- 5 packets transmitted, 5 received, 0% packet loss, time 3999ms rtt min/avg/max/mdev = 0.027/0.036/0.051/0.010 ms The following example demonstrates how to use the ping6 command with the “count” parameter:

```text
# ping6 2001:DB8::1 count 2
```

PING 2001:DB8::1(2001:DB8::1) 56 data bytes 64 bytes from 2001:DB8::1: icmp_seq=1 ttl=64 time=0.028 ms 64 bytes from 2001:DB8::1: icmp_seq=2 ttl=64 time=0.037 ms --- 2001:DB8::1 ping statistics --- 2 packets transmitted, 2 received, 0% packet loss, time 999ms rtt min/avg/max/mdev = 0.028/0.032/0.037/0.007 ms The following example demonstrates how to use the ping6 command with the “size” parameter:

```text
# ping6 2001:DB8::1 size 1500
```

PING 2001:DB8::1(2001:DB8::1) 1500 data bytes 1508 bytes from 2001:DB8::1: icmp_seq=1 ttl=64 time=0.050 ms 1508 bytes from 2001:DB8::1: icmp_seq=2 ttl=64 time=0.073 ms 1508 bytes from 2001:DB8::1: icmp_seq=3 ttl=64 time=0.039 ms 1508 bytes from 2001:DB8::1: icmp_seq=4 ttl=64 time=0.037 ms 1508 bytes from 2001:DB8::1: icmp_seq=5 ttl=64 time=0.040 ms --- 2001:DB8::1 ping statistics --- 5 packets transmitted, 5 received, 0% packet loss, time 3999ms rtt min/avg/max/mdev = 0.037/0.047/0.073/0.015 ms The following example demonstrates how to use the ping6 command with the “source” parameter using ip address:

```text
# ping6 2001:DB8::1 source 3001:AFF::2
```

PING 2001:DB8::1(2001:DB8::1) from 3001:AFF::2 : 56 data bytes 64 bytes from 2001:DB8::1: icmp_seq=1 ttl=64 time=0.027 ms 64 bytes from 2001:DB8::1: icmp_seq=2 ttl=64 time=0.028 ms 64 bytes from 2001:DB8::1: icmp_seq=3 ttl=64 time=0.038 ms 64 bytes from 2001:DB8::1: icmp_seq=4 ttl=64 time=0.038 ms 64 bytes from 2001:DB8::1: icmp_seq=5 ttl=64 time=0.051 ms --- 2001:DB8::1 ping statistics --- 5 packets transmitted, 5 received, 0% packet loss, time 3999ms rtt min/avg/max/mdev = 0.027/0.036/0.051/0.010 ms The following example demonstrates how to use the ping6 command with the “source” parameter using interface name:

```text
# ping6 2001:DB8::1 source mgmt-1/1/1
```

PING 2001:DB8::1(2001:DB8::1) from 11:12::14 eth0 : 56 data bytes 64 bytes from 2001:DB8::1: icmp_seq=1 ttl=64 time=0.027 ms 64 bytes from 2001:DB8::1: icmp_seq=2 ttl=64 time=0.028 ms 64 bytes from 2001:DB8::1: icmp_seq=3 ttl=64 time=0.038 ms 64 bytes from 2001:DB8::1: icmp_seq=4 ttl=64 time=0.038 ms 64 bytes from 2001:DB8::1: icmp_seq=5 ttl=64 time=0.051 ms --- 2001:DB8::1 ping statistics --- 5 packets transmitted, 5 received, 0% packet loss, time 3999ms rtt min/avg/max/mdev = 0.027/0.036/0.051/0.010 ms

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show alarm`

> **Página:** 182 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** sim

**Description:** Display the current active alarms.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show alarm
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

N/A

**Output Terms:**

Output Description Triggered on Time of when the alarm was triggered. Severity Severity of the alarm, can be either MINOR, MAJOR or CRITICAL. Source Source interface which triggered the alarm. Status Status of the alarm. Name Name of the alarm, prefixed with ’*’ when the alarm is unstable. Description Description of the alarm.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show core-dump`

> **Página:** 184 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** sim

**Description:** Show list core dump files.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show core-dump
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. The format of timestamp was changed to include the timezone offset 2.0 information. |

**Usage Guidelines:**

To show core-dump file list. Maximun files in list: 10

```text
DM4610# show core-dump
```

Filename | Size | Date created ------------------------------------------------------------------------ core-file.5407.1493214178.core.gz 0.99 MB 2017-04-26 13:42:58 UTC+0

```text
DM4610#
```

**Output Terms:**

Output Description Filename, size and Filename, size and timestamp of the core dump file. timestamp

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show counters`

> **Página:** 186 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays statistics counters for User-Defined Counter instances.

**Supported Platforms:** This command is not supported in the following platforms: DM4618, DM4920.

**Syntax:**

```text
show counters [ { ingress | egress } [ id counter-id ] ]
```

**Parameters:**

- `ingress` — This parameter displays ingress user defined counters only. — *Valores:* N/A · *Default:* N/A
- `egress` — This parameter displays egress user defined counters only. — *Valores:* N/A · *Default:* N/A
- `id counter-id` — User defined counter identifier. — *Valores:* 1 - 256 · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.9 | This command was introduced. |

**Usage Guidelines:**

Given the equipment has an ingress and an egress user defined counter configured, the command could result in the following output:

```text
# show counters
INGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
1 vlan100 1024 octets
EGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
1 vlan100 2048 octets
```

The output of the command when the user specifies the ingress counter-id 1 could look like this:

```text
# show counters ingress id 1
INGRESS COUNTERS
ID DESCRIPTION VALUE TYPE
--------------------------------
1 vlan100 1024 octets
```

**Output Terms:**

Output Description ID The user defined counter identifier. DESCRIPTION The user defined counter description. VALUE The current value of the user defined counter. TYPE The unit of the user defined counter current value.

**Impacts and precautions:**

The values presented by this command are accumulated since the last time the operator issued a clear command.

**Hardware restrictions:**

The maximum counter value is restricted by the width of the hardware counter storage.


### `show interface statistics`

> **Página:** 189 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** This command displays the statistics counters for an interface.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface interface-name statistics
```

**Parameters:**

- `interface-name` — Interface id referencing chassis/slot/port respectively or an id referencing a specified LAG. — *Valores:* { { gigabit-ethernet | ten-gigabit-ethernet | twenty-fiveg-ethernet | forty-gigabit-ethernet | hundred-gigabit-ethernet | two-hundred-g-ethernet | four-hundred-g-ethernet } c/s/p } | lag id } · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.2 | This command was introduced. |
| 3.0 | Added support for 40G interfaces. |
| 4.6 | Added support for 100G and LAG interfaces. |
| 5.0 | Added support for 25G. |
| 10.6 | Added support for 200G. |

**Usage Guidelines:**

The values presented by this command are accumulated since the last time the operator issued a clear statistics interface-name command. Because of this, these values should not be used for accounting or billing. A sample usage of the command is presented below: > show interface gigabit-ethernet 1/1/1 statistics Counter Value -------------------------- In Octets : 0 In Unicast Pkts : 0 In Broadcast Pkts : 0 In Multicast Pkts : 0 In Discards : 0 In Errors : 0 In Unknown Protos : 0 Out Octets : 0 Out Unicast Pkts : 0 Out Broadcast Pkts : 0 Out Multicast Pkts : 0 Out Discards : 0 Out Errors : 0

**Output Terms:**

Output Description In Octets The amount of octets that entered the network interface The amount of packets that entered the network interface to a uniIn Unicast Pkts cast address The amount of packets that entered the network interface to a broadIn Broadcast Pkts cast address Output Description The amount of packets that entered the network interface to a mulIn Multicast Pkts ticast address In Discards The amount of packets discarded by the network interface The amount of packets that entered the network interface with errors In Errors The amount of packets whose protocol was unknown that entered In Unknown Protos the network interface Out Octets The amount of octets that exited the network interface The amount of packets that exited the network interface to a unicast Out Unicast Pkts address Out Broadcast Pkts The amount of packets that exited the network interface to a broadcast address Out Multicast Pkts The amount of packets that exited the network interface to a multicast address The amount of packets discarded by the network interface in the Out Discards egress block Out Errors The amount of packets with errors in the egress block

**Impacts and precautions:**

The values presented via CLI and Netconf should not be used for accounting or billing (see usage guidelines for more information).

**Hardware restrictions:**

The maximum counter value is restricted by the width of the hardware counter storage.


### `show system cpu`

> **Página:** 193 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays information about CPU usage including the overall CPU load per chassi and slot on the equipment.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show system cpu [ detail | chassis chassis-id [ slot slot-id [ { load | core [ core-id ] } ] ]
```

**Parameters:**

- `detail` — Show the CPU usage of all process. — *Valores:* None. · *Default:* None.
- `chassis chassis-id` — Chassis identification. — *Valores:* 1. · *Default:* None.
- `slot slot-id` — Slot identification. — *Valores:* 1. · *Default:* None.
- `load` — Load information. — *Valores:* None. · *Default:* None.
- `core core-id` — Core information. — *Valores:* 0-1. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. |

**Usage Guidelines:**

Displaying load average of all CPUs, in particular slot, in different interval of time:

```text
DM4610# show system cpu chassis 1 slot 1 load
```

CPU load information: --- 5 seconds 1 minute 5 minutes active 60.0% 4.4% 100.0% idle 40.0% 96.6% 0.0% Displaying detailed information about a specific CPU core:

```text
DM4610# show system cpu chassis 1 slot 1 core 0
```

CPU core 0 information: --- 5 seconds 1 minute 5 minutes user 0.8% 1.0% 0.8% system 0.3% 0.8% 0.3% nice 0.0% 0.0% 0.0% wait 2.0% 5.6% 2.0% interrupt 0.0% 0.0% 0.0% softirq 0.0% 0.2% 0.0% active 1.0% 1.0% 1.0% idle 96.9% 92.4% 96.9% Displaying the load average, and also detailed information per-core for each chassis and slot:

```text
DM4610# show system cpu
Chassis/Slot: 1/1
```

CPU load information: --- 5 seconds 1 minute 5 minutes active 0.0% 2.9% 2.9% idle 100.0% 95.1% 97.3% CPU core 0 information: --- 5 seconds 1 minute 5 minutes user 0.2% 0.8% 0.2% system 0.3% 1.7% 0.3% nice 0.0% 0.0% 0.0% wait 0.0% 1.9% 0.0% interrupt 0.0% 0.0% 0.0% softirq 0.2% 0.2% 0.2% active 0.5% 0.5% 0.5% idle 99.4% 95.4% 99.4%

**Output Terms:**

Output Description user Statistics for CPU time spent in user mode. system Statistics for CPU time spent in system mode. nice Statistics for CPU time spent in user mode with low priority. wait Statistics for CPU time spent awaiting for I/O to complete. irq Statistics for CPU time spent in hardware interrupts. softirq Statistics for CPU time spent in software interrupts. active Statistics for active CPU time spent. idle Statistics for idle CPU time spent.

**Impacts and precautions:**

Some minutes after system initialization, the percentage is zero because no information was generated yet.

**Hardware restrictions:**

None.


### `show system memory`

> **Página:** 197 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays system memory information and usage statistics useful for monitoring and troubleshooting.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show system memory [ detail | chassis chassis-id [ slot slot-id ]]
```

**Parameters:**

- `detail` — Show the memory usage of all process. — *Valores:* None. · *Default:* None.
- `chassis chassis-id` — Chassis identification. — *Valores:* 1. · *Default:* None.
- `slot slot-id` — Slot identification. — *Valores:* 1. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.8 | This command was introduced. |
| 4.4 | Adds the ‘1 minute’ memory interval |

**Usage Guidelines:**

Report detailed memory information of the line card on slot 1 of chassis 1. There are four consolidation intervals expressing the trend line of memory consumption in the last thirty minutes. On non-modular equipments the values for chassi and slot are fixed at 1.

```text
DM4610# show system memory chassis 1 slot 1
```

Memory information: --- 5 seconds 1 minute 5 minutes 30 minutes Report detailed memory information of line cards on chassis 1. There are four consolidation intervals expressing the trend line of memory consumption in the last thirty minutes

```text
DM4610# show system memory chassis 1
```

Memory information: --- 5 seconds 1 minute 5 minutes 30 minutes Report detailed memory information of the entire system. There are four consolidation intervals expressing the trend line of memory consumption in the last thirty minutes.

```text
DM4610# show system memory
Chassis/Slot: 1/1
```

Memory information: --- 5 seconds 1 minute 5 minutes 30 minutes

**Output Terms:**

Output Description total Statistics for total usable RAM. used Statistics for memory in use by processes. available Statistics for memory available for starting new applications (not including swap memory). free Statistics for memory available for use by userspace programs, kernel data structures and the pagecache. buffered Statistics for buffered memory, used as temporary storage for raw disk blocks lower than 20 MiB. cached Statistics for cached memory, which is an in-memory cache for files read from disk (the page cache). slab_recl Statistics for reclaimable slab memory, which is a reclaimable in-kernel cache for data structures. slab_unrecl Statistics for non-reclaimable slab memory, which is a non-reclaimable in-kernel cache for data structures.

**Impacts and precautions:**

None.

**Hardware restrictions:**

None.


### `show system uptime`

> **Página:** 200 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows the system uptime.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show system uptime
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. The command “uptime” was replaced by “show system uptime”. The old 1.10 command was kept for compatibility. |

**Usage Guidelines:**

N/A

**Output Terms:**

Output Description Shows the time that the system is operational in “<Current time> Current uptime of up <uptime>, <Number of logged users>, load average: <in 1 system minute>, <in 5 minutes>, <in 15 minutes>” format

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show tech-support`

> **Página:** 202 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** sim

**Description:** Shows relevant information to be used by technical support.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show tech-support [ gpon | infra | l2 | l3 | mpls | no-running ]
```

**Parameters:**

- `tech-support` — Show all technical support informations. — *Valores:* No range value. · *Default:* No default value.
- `gpon` — Show gpon information more infrastructure informations. — *Valores:* No range value. · *Default:* No default value.
- `infra` — Show infrastructure informations. — *Valores:* No range value. · *Default:* No default value.
- `l2` — Show layer 2 information more infrastructure informations. — *Valores:* No range value. · *Default:* No default value.
- `l3` — Show layer 3 information more infrastruture informations. — *Valores:* No range value. · *Default:* No default value.
- `mpls` — Show mpls information more infrastruture informations. — *Valores:* No range value. · *Default:* No default value.
- `no-running` — Show technical information without the running-config. — *Valores:* No range value. · *Default:* No default value.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. Added parameter ‘no-running’ to exclude show running-config from tech6.0 support. |

**Usage Guidelines:**

The following example shows how to use the show tech-support without parameters, it will show all technical support informations:

```text
hostname# show tech-support
```

The following example shows how to use the show tech-support with gpon option, it will show gpon information more infrastructure informations:

```text
hostname# show tech-support gpon
```

The following example shows how to use the show tech-support with infra option, it will show infrastructure informations:

```text
hostname# show tech-support infra
```

The following example shows how to use the show tech-support with l2 option, it will show layer 2 information more infrastructure informations:

```text
hostname# show tech-support l2
```

The following example shows how to use the show tech-support with l3 option, it will show layer 3 information more infrastructure informations:

```text
hostname# show tech-support l3
```

**Output Terms:**

Output Description Status Shows relevant information to be used by technical support

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `tcpdump`

> **Página:** 206 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Start a debug session to capture network traffic received or transmitted by the CPU. Only inband management packets are captured, i.e., all traffic received or sent by outband management interfaces (such as mgmt 1/1/1) are not captured. Please note that simultaneous debug sessions are not allowed.

**Supported Platforms:** This command is not supported in the following platforms: DM4920.

**Syntax:**

```text
tcpdump packet-direction [ interface name ] [ count number ] [ verbosity-level level] [print-link-level-header] [ print-data format ] [ print-timestamp format ] [ filter tcpdump-filter ] [save-pcap]
```

**Parameters:**

- `packet-direction` — Packet direction (received, transmitted or both). — *Valores:* List of supported directions: rx, tx, and rx-and-tx. · *Default:* None.
- `interface name` — Name of the interface to be sniffed. — *Valores:* Name of the interface. · *Default:* Listen all interfaces.
- `count number` — Number of packets to be sniffed. — *Valores:* Integer number greater than zero. · *Default:* None.
- `verbosity-level level` — Level of verbosity of packet dump. — *Valores:* 1 - 3 · *Default:* Use non-verbose packet dump.
- `print-link-level-header` — Print link-level header of each packet. — *Valores:* N/A; · *Default:* Do not print link-level header information.
- `print-data format` — Print the data of each packet in hex and/or ASCII format. — *Valores:* List of supported formats: hex, link-level-hex, hex-ascii, and link-level-hex-ascii. · *Default:* None.
- `print-timestamp format` — Print timestamp of each packet. — *Valores:* List of supported formats and examples: - no: no timestamp is printed - utc: 1612286218.939735 - h-m-s: 2021-02-02 14:16:58.939735 - delta-current-previous: 00:00:00.000051 - delta-current-first: 00:00:00.001741 · *Default:* If not specified, time is shown for each packet. For instance:
- `14:16:58.939735. filter tcpdump-filter` — Tcpdump filter expression. Note that tcpdump filter presents an unusual behaviour when using “vlan” in the expression because “vlan” always causes an offset of 4 bytes to the following parameters of the filter. If a filter is passed as “vlan and arp”, tcpdump will correctly filter VLAN-encapsulated ARP packets. But “vlan or arp” instead of looking for VLAN-encapsulated packets or ARP (without VLAN) packets, will also look for VLAN-encapsulated ARP packets. — *Valores:* A Berkeley Packet Filter (BPF) expression. · *Default:* None.
- `save-pcap` — Save captured packets to a pcap file, which has a maximum size of 2MB. When this limit is reached, the file will be rotated, removing ~1MB associated with the oldest packets. When a new capture is started, the pcap file is removed, and data from previous capture sessions are thus discarded. If no packet is captured, no capture file is generated. — *Valores:* N/A; · *Default:* Do not save dump to pcap file.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 6.0 | This command was introduced. |

**Usage Guidelines:**

The following example demonstrates how to use tcpdump only with direction parameter:

```text
# tcpdump rx-and-tx
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
[TX Mode: INTERFACE, TX] - 13:53:51.378208 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
[TX Mode: INTERFACE, TX] - 13:53:52.407735 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
[TX Mode: INTERFACE, TX] - 13:53:53.431732 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
^C
3 packets captured
3 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates how to use tcpdump with interface parameter:

```text
# tcpdump rx interface gigabit-ethernet-1/1/1
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on gigabit-ethernet-1/1/1, link-type EN10MB (Ethernet), capture size 262144 bytes
[Interface: gigabit-ethernet-1/1/1, RX] - 15:31:56.661166 ARP, Reply 5.5.5.1 is-at 52:54:00:81:...
[Interface: gigabit-ethernet-1/1/1, RX] - 15:31:56.770118 ARP, Reply 5.5.5.1 is-at 52:54:00:81:...
[Interface: gigabit-ethernet-1/1/1, RX] - 15:31:56.878792 ARP, Reply 5.5.5.1 is-at 52:54:00:81:...
^C
3 packets captured
3 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates how to use tcpdump with interface parameter when there is a LAG interface:

```text
# tcpdump rx interface gigabit-ethernet-1/1/1 count 20
tcpdump: verbose output suppressed, use verbosity-level 1, 2 or 3 for full protocol decode
listening on gigabit-ethernet-1/1/1, link-type EN10MB (Ethernet), capture size 262144 bytes
[Physical interface: gigabit-ethernet-1/1/1, Interface: lag-1, RX] - 15:28:42.143215 ARP, Reply...
[Physical interface: gigabit-ethernet-1/1/1, Interface: lag-1, RX] - 15:28:42.263215 ARP, Reply...
[Physical interface: gigabit-ethernet-1/1/1, Interface: lag-1, RX] - 15:28:42.363215 ARP, Reply...
^C
3 packets captured
3 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
# tcpdump rx interface lag-1
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on lag-1, link-type EN10MB (Ethernet), capture size 262144 bytes
[Physical interface: gigabit-ethernet-1/1/3, Interface: lag-1, RX] - 15:28:42.205291 IP 5.5.5.1...
[Physical interface: gigabit-ethernet-1/1/1, Interface: lag-1, RX] - 15:28:42.263215 ARP, Reply...
[Physical interface: gigabit-ethernet-1/1/3, Interface: lag-1, RX] - 15:28:42.306467 IP 5.5.5.1...
^C
3 packets captured
3 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates how to use the tcpdump command with the “count” parameter:

```text
# tcpdump rx-and-tx count 1
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
[TX Mode: INTERFACE, TX] - 16:42:51.186861 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
1 packet captured
4 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates how to use the tcpdump command with the “verbosity-level” parameter:

```text
# tcpdump rx-and-tx verbosity-level 1
tcpdump: listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
[TX Mode: INTERFACE, TX] - 16:44:02.866870 ARP, Ethernet (len 6), IPv4 (len 4), Request who-has...
^C
1 packet captured
1 packet received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates how to use the tcpdump command with the “print-timestamp” parameter:

```text
# tcpdump rx-and-tx print-timestamp h-m-s
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
[TX Mode: INTERFACE, TX] - 2015-10-21 07:28:28.275022 ARP, Request who-has 1.1.1.1 tell 192.168...
[TX Mode: INTERFACE, TX] - 2015-10-21 07:28:29.298877 ARP, Request who-has 1.1.1.1 tell 192.168...
[TX Mode: INTERFACE, TX] - 2015-10-21 07:28:30.322868 ARP, Request who-has 1.1.1.1 tell 192.168...
^C
3 packets captured
3 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates how the timestamp is printed when “print-timestamp” is “delta-current-previous”:

```text
# tcpdump rx-and-tx print-timestamp delta-current-previous
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
[TX Mode: INTERFACE, TX] - 00:00:00.000000 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, len...
[TX Mode: INTERFACE, TX] - 00:00:01.024301 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, len...
[TX Mode: INTERFACE, TX] - 00:00:01.023696 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, len...
^C
3 packets captured
3 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates how the timestamp is printed when “print-timestamp” is “delta-current-first”:

```text
# tcpdump rx-and-tx print-timestamp delta-current-first
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
[TX Mode: INTERFACE, TX] - 00:00:00.000000 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, len...
[TX Mode: INTERFACE, TX] - 00:00:01.024301 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, len...
[TX Mode: INTERFACE, TX] - 00:00:02.047997 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, len...
^C
3 packets captured
3 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates how to use the tcpdump command with the “filter” parameter:

```text
# tcpdump rx-and-tx filter "arp"
tcpdump: verbose output suppressed, use verbosity-level 1, 2 or 3 for full protocol decode
listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
[TX Mode: INTERFACE, TX] - 16:04:10.991225 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
[TX Mode: INTERFACE, TX] - 16:04:12.019647 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
[TX Mode: INTERFACE, TX] - 16:04:13.043746 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
[TX Mode: INTERFACE, TX] - 16:04:14.067979 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
[TX Mode: INTERFACE, TX] - 16:04:15.091813 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
^C
5 packets captured
5 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
# tcpdump rx-and-tx filter "vlan and arp"
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
[Interface: gigabit-ethernet-1/1/3, RX] - 14:28:49.226863 ARP, Reply 5.5.5.1 is-at 52:54:00:81:...
[Interface: gigabit-ethernet-1/1/3, RX] - 14:28:49.327539 ARP, Reply 5.5.5.1 is-at 52:54:00:81:...
[Interface: gigabit-ethernet-1/1/3, RX] - 14:28:49.428315 ARP, Reply 5.5.5.1 is-at 52:54:00:81:...
[Interface: gigabit-ethernet-1/1/3, RX] - 14:28:49.528865 ARP, Reply 5.5.5.1 is-at 52:54:00:81:...
[Interface: gigabit-ethernet-1/1/3, RX] - 14:28:49.629842 ARP, Reply 5.5.5.1 is-at 52:54:00:81:...
^C
5 packets captured
5 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
# tcpdump rx-and-tx filter "ether proto 0x0806"
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
[TX Mode: INTERFACE, TX] - 16:04:10.991225 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
[TX Mode: INTERFACE, TX] - 16:04:12.019647 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
[TX Mode: INTERFACE, TX] - 16:04:13.043746 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
[TX Mode: INTERFACE, TX] - 16:04:14.067979 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
[TX Mode: INTERFACE, TX] - 16:04:15.091813 ARP, Request who-has 1.1.1.1 tell 192.168.1.80, leng...
^C
5 packets captured
5 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates how to use the tcpdump command with the “save-pcap” parameter:

```text
# tcpdump rx-and-tx save-pcap
tcpdump: listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
^C3 packets captured
3 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates how to use tcpdump and filter by VLAN ID:

```text
# tcpdump rx filter "vlan 20"
[Interface: gigabit-ethernet-1/1/1, RX] - 14:28:49.423160 ARP, Reply 5.5.5.1 is-at 52:54:00:81:...
^C
1 packets captured
1 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
# tcpdump rx print-link-level-header filter "vlan 20"
...9:06 (oui Unknown), ethertype 802.1Q (0x8100), length 64: vlan 20, p 0, ethertype ARP, Reply...
^C
1 packets captured
1 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

The following example demonstrates what happens when try to open a second tcpdump session:

```text
# tcpdump rx-and-tx
```

Error: already running by: admin ssh (cli from 192.168.1.127) on since 2021-03-02 14:27:29 The following example demonstrates the unusual behaviour of tcpdump when using filter with “vlan”:

```text
# tcpdump rx print-link-level-header filter "vlan and arp"
tcpdump: verbose output suppressed, use verbosity-level 1, 2 or 3 for full protocol decode
listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
...9:06 (oui Unknown), ethertype 802.1Q (0x8100), length 64: vlan 30, p 0, ethertype ARP, Reply...
^C
1 packets captured
1 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
# tcpdump rx print-link-level-header filter "vlan or arp"
tcpdump: verbose output suppressed, use verbosity-level 1, 2 or 3 for full protocol decode
listening on any, link-type EN10MB (Ethernet), capture size 262144 bytes
...9:06 (oui Unknown), ethertype 802.1Q (0x8100), length 64: vlan 20, p 0, ethertype ARP, Reply...
^C
1 packets captured
1 packets received by filter
0 packets dropped by metadata filters
0 packets dropped by kernel
```

**Impacts and precautions:**

None.

**Hardware restrictions:**

None


### `traceroute`

> **Página:** 214 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Traceroute is a utility for displaying all the hops to reach a destination and measuring transit delays of packets across an Internet Protocol (IP) network.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
traceroute ipv4-address [ vrf name | source {ip-address | interface} ]
```

**Parameters:**

- `ipv4-address` — The IPv4 address destination. — *Valores:* a.b.c.d · *Default:* None.
- `vrf name` — The name of VRF to use. — *Valores:* Any VRF created. · *Default:* None.
- `source {ip-address | interface}` — Specify the source IP address or the interface name from which packets should be sent. — *Valores:* ip-address - IP address from a configured interface in a.b.c.d format; or interface - name of the management or l3 interface in l3-<name>, mgmt-<c>/<s>/<p> format. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |
| 5.2 | Added source support. |
| 5.4 | Added VRF support. |

**Usage Guidelines:**

The following example demonstrates how to use the traceroute command.

```text
# traceroute 10.1.147.55
traceroute to 10.1.147.55 (10.1.147.55), 30 hops max, 60 byte packets
1 10.1.8.1 (10.1.8.1) 1.255 ms 5.530 ms 6.095 ms
2 10.1.63.18 (10.1.63.18) 1.172 ms 2.871 ms 3.436 ms
3 10.1.63.110 (10.1.63.110) 5.423 ms 10.524 ms 12.045 ms
4 10.1.147.55 (10.1.147.55) 0.321 ms 0.326 ms 0.313 ms
```

The following example demonstrates how to use the traceroute command with the “source” parameter using interface name:

```text
# traceroute 10.1.8.173 source mgmt-1/1/1
traceroute to 10.1.8.173 (10.1.8.173), 30 hops max, 38 byte packets
1 10.1.147.254 (10.1.147.254) 10.175 ms 7.070 ms 3.228 ms
2 10.1.63.109 (10.1.63.109) 1.139 ms 1.142 ms 1.251 ms
3 10.1.63.17 (10.1.63.17) 1.204 ms 1.245 ms 2.664 ms
4 10.1.8.173 (10.1.8.173) 0.334 ms 0.313 ms 0.295 ms
```

The following example demonstrates how to use the traceroute command with the “source” parameter using IP address:

```text
# traceroute 10.1.8.173 source 10.1.147.11
traceroute to 10.1.8.173 (10.1.8.173) from 10.1.147.11, 30 hops max, 38 byte packets
1 10.1.147.254 (10.1.147.254) 6.749 ms 5.596 ms 3.289 ms
2 10.1.63.109 (10.1.63.109) 1.286 ms 1.088 ms 1.484 ms
3 10.1.63.17 (10.1.63.17) 1.037 ms 1.221 ms 1.206 ms
4 10.1.8.173 (10.1.8.173) 0.557 ms 0.294 ms 0.261 ms
```

The following example demonstrates how to use the traceroute command with the “vrf” parameter:

```text
# traceroute 31.1.1.2 vrf yellow
traceroute to 31.1.1.2 (31.1.1.2), 30 hops max, 38 byte packets
1 21.1.1.1 (21.1.1.1) 1.687 ms 1.494 ms 1.455 ms
2 31.1.1.2 (31.1.1.2) 2.526 ms 0.859 ms 0.849 ms
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `traceroute6`

> **Página:** 217 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Traceroute is a utility for displaying all the hops to reach a destination and measuring transit delays of packets across an Internet Protocol version 6 (IPv6) network.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
traceroute6 ipv6-address [ vrf name ]
```

**Parameters:**

- `ipv6-address` — The IPv6 address destination. — *Valores:* X:X:X:X::X · *Default:* None.
- `vrf name` — The name of VRF to use. — *Valores:* Any VRF created. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.0 | This command was introduced. |
| 6.0 | Added VRF support. |

**Usage Guidelines:**

The following example demonstrates how to use the traceroute command.

```text
# traceroute6 2002::1
traceroute to 2002::1 (2002::1) from 2001::1, 30 hops max, 16 byte packets
1 2001::2 (2001::2) 11.438 ms 2.072 ms 1.962 ms
2 2002::1 (2002::1) 1.172 ms 1.327 ms 1.113 ms
```

The following example demonstrates how to use the traceroute command with the “vrf” parameter:

```text
# traceroute6 2002::1 vrf yellow
traceroute to 2002::1 (2002::1) from 2001::1, 30 hops max, 16 byte packets
1 2001::2 (2001::2) 11.438 ms 2.072 ms 1.962 ms
2 2002::1 (2002::1) 1.172 ms 1.327 ms 1.113 ms
```

As link-local addresses are not routable, the traceroute command with this kind of address must fail.

```text
# traceroute6 fe80::204:dfff:fecc:25cb
connect: Invalid argument
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A SNMP This topic describes the commands related to configuration and use of Simple Network Management Protocol (SNMP) such as commands to configure communities or to enable traps.


## SNMP

### `snmp agent`

> **Página:** 220 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Configures the SNMP agent.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
snmp agent { [ context vrf-name]* | [ disabled | enabled ] | engine-id { enterprise-number number | [ from-ip { a.b.c.d | x:x:x:x::x } | from-mac-address mac-address | from-text text | other string ] }* | ip { a.b.c.d | x:x:x:x::x } | max-message-size size | udp-port port | version { v1 | v2c | v3 }* }* snmp agent [ listen { interface interface-name } | [ udp-port port ] ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `context vrf-name` — Creates a context for SNMP requests enabling logical network entity mapping. SNMP contexts may be used to access MIB data within a VRF/VPN context. It must be used along snmp community context-map configuration in case of SNMPv1 and SNMPv2. — *Valores:* VRF name · *Default:* None.
- `[ disabled | enabled ]` — Disables or enables the SNMP agent. — *Valores:* disabled or enabled. · *Default:* disabled.
- `engine-id` — Configures the SNMP agent Engine ID. It is a local and unique identifier to be used for communication with SNMPv3 Agents and Managers. — *Valores:* { enterprise-number number | [ from-ip { a.b.c.d | x:x:x:x::x } | from-mac-address mac-address | from-text text | other string ] }* · *Default:* None.
- `enterprise-number number` — Assignes an Enterprise ID to assemble the Engine ID octets. — *Valores:* 0-4294967295. · *Default:* 3709.
- `from-ip { a.b.c.d | x:x:x:x::x }` — Assignes an IPv4 or IPv6 address to assemble the Engine ID octets. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* None.
- `from-mac-address mac-address` — Assignes a MAC address to assemble the Engine ID octets. — *Valores:* xx:xx:xx:xx:xx:xx. · *Default:* None.
- `from-text text` — Assignes a text to assemble the Engine ID octets. — *Valores:* String - maximum 27 characters. · *Default:* None.
- `other string` — Configures the engine ID based on a specified string pattern in accordance to RFC3411. — *Valores:* pattern “[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){0,27}” · *Default:* None.
- `ip { a.b.c.d | x:x:x:x::x }` — Configures an IPv4 or IPv6 as local SNMP agent address. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* None.
- `max-message-size size` — Configures the maximum SNMP agent message size that can be sent or received. — *Valores:* 484-214748364. · *Default:* 50000.
- `udp-port port` — Sets the UDP protocol port to be used for communication with the SNMP Agents and Managers. — *Valores:* UDP port. · *Default:* 161.
- `version { v1 | v2c | v3 }` — Configures the SNMP agent version. The options are SNMP version 1, SNMP version 2c and SNMP version 3. More than one option can be configured. — *Valores:* { v1 | v2c | v3 } · *Default:* v2c and v3.
- `listen interface interface-name [ udp-port port ]` — List of interfaces to listen for SNMP requests. — *Valores:* Interface name in format l3-<name> or loopback-<name>. · *Default:* None.
- `udp-port port` — Port on which SNMP will listen for requests on this interface. — *Valores:* UDP port. · *Default:* 161.

**Default:** disabled.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.10 | Only admin user can configure SNMP. |
| 2.4 | Supported extra-list parameter in SNMP agent. |
| 4.4 | Removed the option no for SNMP agent enabled and disabled. |
| 5.0 | Command extra-listen replaced by listen. |
| 5.8 | Added parameter context in SNMP agent command. Added support to loopback interface on SNMP agent listen configuration. 6.0 |

**Usage Guidelines:**

This command can be executed directly via CLI. The listen interface allows the configuration of a list of interfaces to listen for SNMP requests. This configuration can be used for managing SNMP on a VRF. Example: This example shows how to configure the SNMP agent using version 2c.

```text
# configure terminal
Entering configuration mode terminal
(config)# snmp agent version v2c
(config)# snmp agent ip 10.1.0.1
(config)# snmp agent enabled
(config)# commit
```

Commit complete. This example shows how to configure the SNMP agent listen interfaces.

```text
# configure terminal
Entering configuration mode terminal
(config)# snmp agent listen interface l3-vrf-blue
(config-interface-l3-vrf-blue)# commit
```

Commit complete.

**Impacts and precautions:**

The SNMP version 3 requires an engine ID. The Enterprise number 3709 is assigned by IANA to Teracom Telematica Ltda. Be very careful when using a different udp-port for SNMP agent listen interface in order to avoid conflicts with other protocols, such as DHCP (67/68), TFTP (69). In these cases SNMP agent listen interface might work but it can interfere in other protocols. The exception is NTP port (123), that is forbidden to be used, since it will not work. For SNMP listen interface without VRF, SNMP agent will always listen on 161 port, even when a listen interface is configured for another port. In such cases, both ports can be used for SNMP service. For listen interfaces with VRF, only the configured udp-port works. In order to use SNMP agent with VRF mgmt, use SNMP agent IP with the same IPv4 address as configured in out-of-band management interface (interface mgmt X/Y/Z). SNMP agent listen interface will only use the L3 interface primary IPv4 address. Secondary IPv4 address is not supported for L3 interfaces. Also, only the first IPv6 address will be used for L3 or loopback interface. SNMP agent listen interface only supports VRF with IPV4 address. VRF with IPv6 is not supported yet (L3 or loopback interfaces).

**Hardware restrictions:**

N/A


### `snmp community`

> **Página:** 226 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the SNMP communities to be used with managers and agents using version SNMPv1 or SNMPv2c.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
snmp community index [ context-map context | name community_name | sec-name security-name | target-tag identifier ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `index` — Specifies the community index. — *Valores:* String - maximum 32 characters. · *Default:* None.
- `context-map context` — Specifies the context mapping. SNMP requests for the related community will address MIB data within the VRF pointed by the SNMP context. — *Valores:* SNMP agent context. · *Default:* Empty.
- `name community_name` — Specifies the community name. It should be used in case it is different from the index. — *Valores:* String. · *Default:* None.
- `sec-name security-name` — Specifies the community security name corresponding to the community name in a security model independent format. — *Valores:* String - maximum 32 characters. · *Default:* None.
- `target-tag identifier` — Specifies the target tag to be used as an identifier to restrict access for this community. — *Valores:* String. · *Default:* None.

**Default:** N/A.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 5.8 | The parameter context-map was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Up to 32 communities can be created. Example: This example shows how to configure an SNMP community.

```text
# configure terminal
Entering configuration mode terminal
(config)# snmp community private name private-comm sec-name pvt
(config)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `snmp max-sessions-limit`

> **Página:** 229 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Puts a limit to the total number of concurrent SNMP sessions.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
snmp max-sessions-limit
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `number` — Sets maximum number of the concurrent SNMP sessions. — *Valores:* int - maximum 2 characters (range 1-32). · *Default:* 16

**Default:** 16

**History:**

| Release | Modification |
| --- | --- |
| 10.8 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the SNMP max-sessions-limit.

```text
# configure terminal
Entering configuration mode terminal
(config)# snmp max-sessions-limit 5
(config)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `snmp notify`

> **Página:** 231 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the SNMP notification for a specific target defined by tag identifier.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
snmp notify name tag identifier [ type { inform | trap } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `name` — Specifies the notification name. — *Valores:* String - maximum 32 characters. · *Default:* None.
- `tag identifier` — Specifies the notification target tag identifier. — *Valores:* String. · *Default:* None.
- `type { inform | trap }` — Specifies the notification type. — *Valores:* inform or trap. · *Default:* trap.

**Default:** N/A.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Up to 32 entries can be created. SNMP notifications can be sent as traps or inform requests. SNMP traps are unconfirmed notifications. SNMP informs are confirmed notifications. Example: This example shows how to configure the SNMP notification for the target std_v1_trap.

```text
# configure terminal
Entering configuration mode terminal
(config)# snmp notify std_v1_trap
(config-notify-std_v1_trap)# tag std_v1_trap
(config-notify-std_v1_trap)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `snmp system`

> **Página:** 233 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the SNMP system parameters.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
snmp system { contact text location loc }*
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `contact text` — Sets the system contact information. — *Valores:* String - maximum 255 characters. · *Default:* None.
- `location loc` — Sets the system location. — *Valores:* String - maximum 255 characters. · *Default:* None.

**Default:** N/A.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure the SNMP system parameters.

```text
# configure terminal
Entering configuration mode terminal
(config)# snmp system location Curitiba
(config)# snmp system contact "Teracom Telematica Ltda"
(config)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `snmp target`

> **Página:** 235 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a SNMP target list.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
snmp target name ip { a.b.c.d | x:x:x:x::x } { usm user-name name sec-level { auth-no-priv | auth-priv | no-auth-no-priv } | { v1 | v2c } sec-name security-name } [ engine-id end-id | retries num-retries | tag tag-list | timeout time | udp-port port | vrf vrf-name | source { ipv4 address IPv4address | interface interface-name } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `name` — Specifies the target name. — *Valores:* String - maximum 32 characters. · *Default:* None.
- `ip { a.b.c.d | x:x:x:x::x }` — Specifies the target IPv4 or IPv6 address. — *Valores:* a.b.c.d or x:x:x:x::x. · *Default:* None.
- `usm` — Configures the target to use SNMPv3 user based parameters. — *Valores:* user-name name sec-level { auth-no-priv | auth-priv | noauth-no-priv } · *Default:* None.
- `user-name name` — Specifies the SNMPv3 user name. — *Valores:* String - maximum 32 characters. · *Default:* None.
- `sec-level { auth-no-priv | auth-priv | no-auth-no-priv }` — Specifies the minimum SNMPv3 security level. — *Valores:* auth-no-priv, auth-priv or no-auth-no-priv. · *Default:* None.
- `{ v1 | v2c }` — Configures the target to use SNMPv1 or SNMPv2c parameters. — *Valores:* v1 or v2c. · *Default:* None.
- `sec-name security-name` — Specifies the SNMP target security name. — *Valores:* String - maximum 32 characters. · *Default:* None.
- `engine-id end-id` — (Optional) Specifies the target remote engine ID to receive SNMPv3 informs. — *Valores:* pattern “[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){0,27}”. · *Default:* None.
- `retries num-retries` — (Optional) Specifies the number of retries to receive SNMPv3 informs. — *Valores:* 0 - 255. · *Default:* 3.
- `tag tag-list` — (Optional) Specifies the target tag list. A list must be between brackets “[" and “]”. — *Valores:* String. · *Default:* None.
- `timeout time` — (Optional) Specifies the timeout in hundreds of seconds to receive SNMPv3 informs. — *Valores:* 0-4294967295. · *Default:* 1500.
- `udp-port port` — (Optional) Sets the UDP protocol port to be used for communication with the SNMP target entity. — *Valores:* 0-65532. · *Default:* 162.
- `vrf vrf-name` — (Optional) Specifies the name of VRF which the target can be reached. — *Valores:* String. · *Default:* None.
- `source ipv4 address IPv4address` — (Optional) Specifies the source IPv4 address to send SNMP notifications to target. — *Valores:* a.b.c.d · *Default:* None.
- `source interface interface-name` — (Optional) Specifies the interface used to send SNMP notifications to target. — *Valores:* Interface name in format l3-<name> or loopback-<id> · *Default:* None.

**Default:** N/A.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 5.0 | Add vrf option. |
| 6.0 | Add source ipv4 address and source interface options. |

**Usage Guidelines:**

This command can be executed directly via CLI. Up to 32 entries can be created. Example: This example shows how to configure a SNMP target entry.

```text
# configure terminal
Entering configuration mode terminal
(config)# snmp target outband
(config-target-outband)# ip 192.168.10.1
(config-target-outband)# tag [ std_v2_trap std_v3_trap ]
(config-target-outband)# usm user-name public
(config-target-outband)# usm sec-level no-auth-no-priv
(config-target-outband)# vrf red
(config-target-outband)# source ipv4 address 5.5.5.5
(config-target-outband)# commit
```

Commit complete.

**Impacts and precautions:**

The parameter engine-id must indicate an Engine ID identifier present in the snmp usm remote configuration. Take special care when configuring a different UDP port from default (162), since it must not conflict with well-known protocols or services, such as SNTP (123) and Syslog (514).

**Hardware restrictions:**

N/A


### `snmp traps`

> **Página:** 240 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This configuration allows the selection of traps that will be sent to the snmp target.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
snmp traps [ config-commit | cpu-core | cpu-load | link-status | login-fail | login-success ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `config-commit` — Enable the configCommit trap. — *Valores:* N/A · *Default:* N/A
- `cpu-core` — Enable the cpuCoreHighTrap trap. — *Valores:* N/A · *Default:* N/A
- `cpu-load` — Enable the cpuLoadHighTrap trap. — *Valores:* N/A · *Default:* N/A
- `link-status` — Enable the IF-MIB linkDown/linkUp traps. — *Valores:* N/A · *Default:* N/A
- `login-fail` — Enable the loginFail trap. — *Valores:* N/A · *Default:* N/A
- `login-success` — Enable the loginSuccess trap. — *Valores:* N/A · *Default:* N/A

**Default:** The following configuration are enabled: config-commit, cpu-core, cpu-load, link-status and login-success.

**History:**

| Release | Modification |
| --- | --- |
| 5.6 | This config was introduced. New configuration available: config-commit, cpu-core, cpu-load, login-fail 5.12 and login-success. |

**Usage Guidelines:**

The generation of traps can be enabled or disabled with this configuration.

**Impacts and precautions:**

Netconf connections don’t generate login traps.

**Hardware restrictions:**

N/A


### `snmp usm`

> **Página:** 243 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the SNMP user based security model.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
snmp usm { local | remote engine-id } user name [ auth { md5 | sha } { key hexlist | password pw } [ priv { aes | des } { key hexlist | password pw } ] | security-name sec-name ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `{ local | remote engine-id }` — Configures a local or remote user. — *Valores:* Remote user requires an engine ID according to the pattern “[0- 9a-fA-F]{2}(:[0-9a-fA-F]{2}){0,27}”. · *Default:* None.
- `user name` — Specifies the user name. — *Valores:* String - maximum 32 characters. · *Default:* None.
- `auth { md5 | sha } { key hexlist | password pw }` — (Optional) Enables user authentication based on md5 or sha mode. — *Valores:* md5 or sha. · *Default:* None.
- `key hexlist` — Specifies the authentication key in hexadecimal format. — *Valores:* pattern “(((([0-9A-Fa-f]{2}):)*([0-9A-Fa-f]{2}))){0,1}“. · *Default:* None.
- `password pw` — Specifies the authentication password. — *Valores:* String (length 8-255). · *Default:* None.
- `priv { aes | des }` — (Optional) Enables encryption for the authentication process. — *Valores:* AES or DES encryption. · *Default:* None.
- `security-name sec-name` — (Optional) Specifies the user security name in case it should be different from the user name. — *Valores:* String - maximum 32 characters. · *Default:* None.

**Default:** N/A.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Up to 32 local and remote entries can be created. Example: This example shows how to configure a local user based security model.

```text
# configure terminal
Entering configuration mode terminal
(config)# snmp usm local user public
(config-user-public)# auth sha password 12345678
(config-user-public)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `snmp vacm`

> **Página:** 246 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the SNMP group or MIB view based access control model.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
snmp vacm { group grp-name { member member-name sec-model { id | usm | v1 | v2c }* }* [ access { context } { sec-model-num | any | usm | v1 | v2c } { authno-priv | auth-priv | no-auth-no-priv } [ { notify-view | read-view | write-view } view-name ]* ]* | view view-name subtree oid { excluded | included }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `group grp-name` — Specifies the group name. — *Valores:* String - maximum 32 characters. · *Default:* None.
- `member member-name` — Configures a member list for the group. — *Valores:* String - maximum 32 characters. · *Default:* None.
- `sec-model { id | usm | v1 | v2c }*` — Configures the group security model list. — *Valores:* 1 .. 2147483647, usm, v1 or v2c. A list must be between brackets “[" and “]”. · *Default:* None.
- `access { context }` — Configures the SNMP context under which the access rights are applied. If no VRF is used, leave it in blank using “” (Two double quotes). — *Valores:* SNMP agent context. · *Default:* None.
- `access { sec-model-num | any | usm | v1 | v2c }` — (Optional) Configures the group access list under which the access rights are applied based on the security model. — *Valores:* 1 .. 2147483647, any, usm, v1 or v2c. · *Default:* None.
- `{ auth-no-priv | auth-priv | no-auth-no-priv }` — Defines the access rights priviledge mode. — *Valores:* auth-no-priv, auth-priv or no-auth-no-priv. · *Default:* None.
- `{ notify-view | read-view | write-view }* view-name` — (Optional) Defines the access rights for notification, read or write based on the MIB view name. — *Valores:* Mode and MIB view name. · *Default:* None.
- `view view-name` — Configures a MIB view based access control model. — *Valores:* String - maximum 32 characters. · *Default:* None.
- `subtree oid` — Configures the SNMP family subtree to be excluded or included in this MIB view. — *Valores:* pattern ‘((0-1*)|([2*].((0|([1-9]*.))|[*])))’ + ’(.((0|([1-9]*.))|[*]))*’. · *Default:* None.
- `{ excluded | included }` — The SNMP family subtree action for this MIB view. — *Valores:* excluded or included. · *Default:* None.

**Default:** N/A.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 5.8 | The parameter context was introduced. Add a pattern to VRF context allowing only the use of a-z, A-z, 0-9,_ and 7.0 -. |

**Usage Guidelines:**

This command can be executed directly via CLI. Up to 32 groups or views can be created. Example: This example shows how to configure a SNMP group access control.

```text
# configure terminal
Entering configuration mode terminal
(config)# snmp vacm group public
(config-group-public)# member public
(config-member-public)# sec-model [ usm v2c ]
(config-member-public)# commit
```

Commit complete. This example shows how to configure a SNMP MIB view access control.

```text
# configure terminal
Entering configuration mode terminal
(config)# snmp vacm view root
(config-view-root)# subtree 1.3
(config-subtree-1.3)# included
(config-subtree-1.3)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A LICENSE This topic describes the commands to manage licenses.


## License

### `license`

> **Página:** 250 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command is used to disable or enable a licensed feature.

**Supported Platforms:** This command is supported only in the following platforms: DM4170, DM4360, DM4370, DM4376, DM4378, DM4380, DM4270, DM4615, DM4770.

**Syntax:**

```text
license feature { disabled | enabled } key key
```

**Parameters:**

- `license feature` — Specifies the feature to be disabled or enabled. — *Valores:* String of the licensed feature. · *Default:* None.
- `{ disabled | enabled }` — Disables or enables the specified licensed feature. — *Valores:* disabled or enabled. · *Default:* None.
- `key key` — Specifies the key to disable or enable the licensed feature. — *Valores:* String. · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 3.0 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Please contact the support to consult the licensable features and how to obtain a key to disable or enable them. Example: This example shows how to enable the MPLS features.

```text
# configure terminal
Entering configuration mode terminal
(config)# license mpls enabled key 416195f4bd3a73243352aaf4e3eb06abfd35c9ed6f99c7f336ef37d263fd59970137cca031abe9d3c6ca5a2ef6a18362ab30e176edf215f4fb755802bf6f04118863140ee4150f85e9bfa6b707b9c1e0621242fa0740f82479888776f7e2d0f03232a7be9684beddd2200935331c885d104d2123c2f8d5e4fcb6f43d2fa799a04b0f17c3983cde6b800f55381da399e09013739b929b520e6f00f53a7b5bc7b94b0d96e7f556ff03e0cb855445bf1133cc6e43c059ba0763683dbc12b11c1f6144c2ef0dfa3f033707309613b88af24e22fa0da1b4f9fdc28ee1c90a9fa0539e71e4360f3133a007d5c8911f8068127dae7aa0add1b0580f627aab20528f9a4f9df66f247b76a562249a4747af8b14c9ac0d4071d3a372c6b6be8c7a3b46cbc0a68080e138ee15326775f706573e40432e83da93ddf8c0896a050cf78b2cd04583cb4ca7020cd948e78835d2fea848d2ff3bd9b9152272243ac93d497cc69062946c2cadfdd0a85337c93fbf01dab1395290cd1fcf6de85899dcf6c245454194c011e25f80a9bb42b84d24e358389c3a99daa556ef0e5d7b7202ed3bb4eca6884349fe03f38c791d686b0486480333b3e0063ed421e18b2151fca3011ef26c4c56729a116be5e1fd4258626d5989dc90a06101a93f64714a2bce615f5aa08680b2a12c60a24074ed5d15134d8c34131ff7746574abb0483b5ad8937555a82eb1
(config)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show license`

> **Página:** 253 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Access level audit · **Leitura (show/display):** sim

**Description:** This command shows the list of licensed features.

**Supported Platforms:** This command is not supported in the following platforms: DM4050, DM4250, DM4618.

**Syntax:**

```text
show license
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.2 | This command was introduced. The show command was modified to include the number of licenses avail4.9 able for a given feature. |

**Usage Guidelines:**

To show the list of licensed features available the following command can be used: If the number of licenses is not applicable to the feature, “N/A” is displayed.

```text
#show license
```

Feature Status Number of Licenses ---------- ---------- ------------------ mpls enabled N/A speed-100g-ports enabled 5 The example below shows the command output when the license is disabled:

```text
#show license
```

Feature Status Number of Licenses ---------- ---------- ------------------ mpls disabled N/A speed-100g-ports disabled N/A

**Output Terms:**

Output Description Feature Displays the feature name. Status Displays the license status.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A CHAPTER 4: INTERFACES This chapter describes the commands related to management of interfaces in the DmOS CLI. ETHERNET This topic describes the commands related to management of Ethernet interfaces such as commands to configure speed or to disable the interface.
