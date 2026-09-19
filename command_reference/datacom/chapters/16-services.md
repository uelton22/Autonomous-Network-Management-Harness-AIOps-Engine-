# Capítulo 16: Services

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## Management

### `assistant-task`

> **Página:** 1816 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Configures tasks to be executed at a scheduled time.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
assistant-task task-name action cli-file file-name [enabled|disabled] assistant-task task-name schedule {recursive|once} [day day] [hour hour] [minute minute] [month month] [weekday weekday] [second second] assistant-task task-name run-now assistant-task task-name action watch cli-cmd cli-cmd match match cli-file file-name regex regex [disable-after-match]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `task-name` — Name of assistant task. — *Valores:* Text (1-100 characters) · *Default:* N/A
- `action` — Action to be executed by the assistant-task. — *Valores:* N/A · *Default:* N/A
- `cli-file file-name` — File containing CLI commands. Special characters are not allowed in the file or in the file name. Must be an ASCII file. — *Valores:* File name · *Default:* N/A
- `enabled` — Enables the assistant-task. This parameter takes effect only for scheduled actions. — *Valores:* N/A · *Default:* N/A
- `disabled` — Disables the assistant-task. This parameter takes effect only for scheduled actions. — *Valores:* N/A · *Default:* N/A
- `schedule recursive` — Indicates this task is to be executed recursively at a configured time. — *Valores:* N/A · *Default:* N/A
- `schedule once` — Indicates this task is to be executed once at a configured time. — *Valores:* N/A · *Default:* N/A
- `day day` — Day of month when the task is to be executed. If omitted, task will be executed every day. If task is recursive, it may contain ranges. Field value can be asterisk (*), which always stands for “first-last”, that is, any day or 1-31 range. — *Valores:* 1-31 · *Default:* N/A
- `hour hour` — Hour when the task is to be executed. If task is recursive, it may contain ranges. Field value can be asterisk (*), which always stands for “first-last”, that is, any hour or 0-23 range. — *Valores:* 0-23 · *Default:* 0
- `minute minute` — Minute when the task is to be executed. If task is recursive, it may contain ranges. Field value can be asterisk (*), which always stands for “first-last”, that is, any minute or 0-59 range. — *Valores:* 0-59 · *Default:* 0
- `month month` — Month when the task is to be executed. If omitted, task will be executed every month. If task is recursive, it may contain ranges. Field value can be asterisk (*), which always stands for “first-last”, that is, any month or 1-12 range. — *Valores:* 1-12 · *Default:* N/A
- `weekday weekday` — Weekday when the task is to be executed. If omitted, task will be executed every day. If task is recursive, it may contain ranges. Field value can be asterisk (*), which always stands for “first-last”, that is, any weekday or 0-6 range. — *Valores:* 0-7 (where 0 and 7 correspond to Sunday) · *Default:* N/A
- `second second` — Second when the task is to be executed. If omitted, task will be executed every second 0. If task is recursive, it may contain ranges. Field value can be asterisk (*), which always stands for “first-last”, that is, any second or 0-59 range. — *Valores:* 0-59 · *Default:* 0
- `run-now` — Executes a committed task immediately ignoring the scheduled configuration and the enabled/disabled parameter. — *Valores:* N/A · *Default:* N/A
- `watch` — Actions to be executed based on a watch/match pattern. — *Valores:* N/A · *Default:* N/A
- `cli-cmd cli-cmd` — CLI command in quotes to be executed according to schedule. Special characters are not allowed in the file or in the file name. Must be an ASCII file. — *Valores:* CLI command · *Default:* N/A
- `match match` — Match and its related actions to be executed when a regex pattern is found. — *Valores:* Match name · *Default:* N/A
- `regex regex` — Regular expression pattern in quotes for match configuration. — *Valores:* Regex pattern · *Default:* N/A
- `disable-after-match` — Disables the assistant-task after a regex match. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.9 | This command was introduced. |
| 5.0 | Watch command addition |

**Usage Guidelines:**

This command is used to configure frequent tasks to be scheduled by the user. Example: First of all you must create a CLI command file and transfer it to the equipment. Alternatively, it is possible to edit or create a new file using the ‘file edit <filename>’ command. Remember that the ‘config’ command must be included in the file to enter the configure mode. When saving files, use the ‘save overwrite’ option to avoid being asked about existing files. The example below shows a file that can be used to save a configuration backup and send it to a tftp server.

```text
# file show backup.cli
show running-config | save overwrite backup.cfg
copy file backup.cfg tftp://10.1.1.1
#
```

Assistant task runs in non-interactive mode, so there is no need to include the confirmation response in the command file. Older DmOS versions, such as 4.10.2, required the confirmation response to be included. This will not work anymore. Operators need to remove all confirmation responses from existing cli command files, using file edit command, otherwise the assistant task may return a failure during its execution. Configure a task to be run once today at midnight (no time/date specified):

```text
# config
Entering configuration mode terminal
(config)# assistant-task backup
(config-assistant-task-backup)# action cli-file backup.cli
(config-assistant-task-backup)# schedule once
(config)# commit
```

Commit complete. Configure a task to be run once Sunday at midnight:

```text
# config
Entering configuration mode terminal
(config)# assistant-task backup
(config-assistant-task-backup)# action cli-file backup.cli
(config-assistant-task-backup)# schedule once weekday 0
(config)# commit
```

Commit complete. Configure a task to be run from Monday to Friday, except Thursday, at 8am and 6pm. It is possible to provide a combination of range and list:

```text
# config
Entering configuration mode terminal
(config)# assistant-task backup
(config-assistant-task-backup)# action cli-file backup.cli
(config-assistant-task-backup)# schedule recursive hour 8,18
(config-assistant-task-backup)# schedule recursive weekday 1-3,5
(config)# commit
```

Commit complete. Configure a task to be run at the first day of the month at 9am:

```text
# config
Entering configuration mode terminal
(config)# assistant-task backup
(config-assistant-task-backup)# action cli-file backup.cli
(config-assistant-task-backup)# schedule recursive hour 9 day 1
(config)# commit
```

Commit complete. Run a configured task immediately to test if it is running correctly. The run-now command will work even if the task is disabled. After executing this command, use the show assistant-task command to see the command result.

```text
# config
Entering configuration mode terminal
(config)# assistant-task backup
(config-assistant-task-backup)# action cli-file backup.cli
(config-assistant-task-backup)# schedule recursive day 1
(config-assistant-task-backup)# commit
```

Commit complete.

```text
(config-assistant-task-backup)# run-now
(config-assistant-task-backup)# top; exit
# show assistant-task backup last-success output
```

Last successful execution - Thu Aug 29 09:23:35 -03 2019 < Transfer complete. > It is possible to inspect currently running tasks by using the show command. Running tasks can also be interrupted by disabling them:

```text
# show assistant-task
TASK
```

NAME LAST START LAST FAILURE LAST SUCCESS STATUS -------------------------------------------------------------------------------------------- backup Tue Aug 20 23:00:00 -03 2019 - - running

```text
# config
(config)# assistant-task backup
(config-assistant-task-backup)# disabled
(config-assistant-task-backup)# commit
(config-assistant-task-backup)# top ; exit
# show assistant-task
TASK
```

NAME LAST START LAST FAILURE LAST SUCCESS STATUS -------------------------------------------------------------------------------------------- backup Tue Aug 20 23:00:00 -03 2019 - - disabled Configure a task to be run every second (no time/date specified) checking a link health and when a problem occurs changes the link interface.

```text
# file show connectTo1.cli
config
no dot1q vlan 500
dot1q vlan 500
no interface 1/1/10
interface 1/1/9
commit
top
exit
#
# file show connectTo2.cli
config
no dot1q vlan 500
dot1q vlan 500
no interface 1/1/9
interface 1/1/10
commit
top
exit
#
# config
Entering configuration mode terminal
(config)# assistant-task vlanSwitch
(config-assistant-task-vlanSwitch)# schedule recursive minute * hour * second 0-59
(config-assistant-task-vlanSwitch)# action watch cli-cmd "ping 10.1.1.2 | include
\"100% packet l\" | count ; show running-config dot1q vlan 500 |
include ethernet ;"
(config-assistant-task-vlanSwitch)# action watch match M0
(config-assistant-task-match-M0)# cli-file connectTo1.cli
(config-assistant-task-match-M0)# regex ".*Count: 1 lines.*.*1/1/10"
(config-assistant-task-match-M0)# exit
(config-assistant-task-vlanSwitch)# action watch match M1
(config-assistant-task-match-M1)# cli-file connectTo2.cli
(config-assistant-task-match-M1)# regex ".*Count: 1 lines.*.*1/1/9"
(config-assistant-task-match-M1)# exit
(config-assistant-task-vlanSwitch)# commit
```

Commit complete. Schedule example to run an assistant task at 00:00 on the first day of every month:

```text
(config)# assistant-task example
(config-assistant-task-example)# schedule recursive minute 0 hour 0 day 1 month *
```

Schedule example to run an assistant task at 01:00 every day:

```text
(config)# assistant-task example
(config-assistant-task-example)# schedule recursive minute 0 hour 1 day * month *
```

Schedule example to run an assistant task at minute 30 of every hour:

```text
(config)# assistant-task example
(config-assistant-task-example)# schedule recursive minute 30 hour * day * month *
```

Schedule example to run an assistant task at 03:00 every Sunday:

```text
(config)# assistant-task example
(config-assistant-task-example)# schedule recursive minute 0 hour 3 weekday 0 month *
```

**Impacts and precautions:**

Commands executed by the assistant-task feature are executed by special users called batch_<task_name>. This user may appear in logs depending on the commands present in the CLI file. Tasks configured to run only once will be automatically disabled after executed. It is possible to reschedule it to run at a later date by enabling it again. ATTENTION: When saving files in the CLI script, be careful not to let them grow indefinitely to avoid using all available memory. Use copy-file to transfer it to another machine and remove them. ATTENTION: Do not use “| repeat” or other commands that do not return, otherwise the assistant task will not be able to log its output and the task will run indefinitely, until it is disabled.

**Hardware restrictions:**

N/A


### `logout`

> **Página:** 1825 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Terminates a specific session or all CLI and NETCONF sessions of a specific user. If no session or user is specified, the current session is terminated. If the terminated session held the configure exclusive lock, it will be released.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
logout [ session session-id | user user-name ]
```

**Parameters:**

- `session session-id` — Terminates a specific session. — *Valores:* Integer value representing the session ID, which can be obtained by using command “who” or by pressing <TAB>. · *Default:* N/A
- `user user-name` — Terminates all CLI and NETCONF sessions of a specific user. — *Valores:* String representing the user name. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

Before using this command, use command “who” to check the existing sessions. The session marked with a “*" is the current one. Example: This example shows how to logout a specific session.

```text
# who
```

Session User Context From Proto Date Mode *22 admin cli 127.0.0.1 console 17:10:47 operational 21 config cli 192.168.0.26 telnet 17:10:37 operational 19 config cli 192.168.0.26 ssh 17:10:03 operational 18 audit cli 192.168.0.26 ssh 17:09:38 operational

```text
# logout session 21
# who
```

Session User Context From Proto Date Mode *22 admin cli 127.0.0.1 console 17:10:47 operational 19 config cli 192.168.0.26 ssh 17:10:03 operational 18 audit cli 192.168.0.26 ssh 17:09:38 operational

```text
#
```

This example shows how to logout all sessions of a specific user.

```text
# who
```

Session User Context From Proto Date Mode 24 config cli 192.168.0.26 telnet 17:14:27 operational 23 audit cli 192.168.0.26 ssh 17:14:20 operational *22 admin cli 127.0.0.1 console 17:10:47 operational 19 config cli 192.168.0.26 ssh 17:10:03 operational

```text
# logout user config
# who
```

Session User Context From Proto Date Mode 23 audit cli 192.168.0.26 ssh 17:14:20 operational *22 admin cli 127.0.0.1 console 17:10:47 operational

```text
#
```

The logged out user will receive a message informing what happened: login: config Password: Welcome to the DmOS CLI config connected from 192.168.0.26 using telnet on

```text
#
```

Message from admin@ at 2017-03-27 17:12:13... Your session has been terminated by admin

```text
# Connection closed by foreign host.
```

**Impacts and precautions:**

All uncommitted changes in the terminated sessions will be lost.

**Hardware restrictions:**

N/A


### `management`

> **Página:** 1828 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the transport output mode.

**Supported Platforms:** This command is supported only in the following platforms: DM4340.

**Syntax:**

```text
management transport-output
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `transport-output` — Management of SSH and Telnet connections to external hosts. The value none disables both SSH and Telnet connections to external hosts. The value ssh enables only SSH connections to external hosts. The value telnet enables only Telnet connections to external hosts. — *Valores:* { none | ssh | telnet } · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 11.6 | This command was introduced. |

**Usage Guidelines:**

SSH and Telnet connections to external hosts can be enabled or disabled through this command. If no transport output configuration is applied, SSH and Telnet connections to external hosts are allowed by default. The following example shows how to enable only SSH connections to external hosts while blocking Telnet:

```text
# config
(config)# management transport-output ssh
(config)# commit
```

Commit complete.

```text
(config)# end
#
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show assistant-task`

> **Página:** 1830 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Used to list assistant-task results.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show assistant-task [task-name [[last-start|last-failure|last-success|task-status] [output]]
```

**Parameters:**

- `task-name` — Name of assistant task. — *Valores:* Text (1 to 100 characters) · *Default:* N/A
- `last-start` — Shows the timestamp of the last execution start. — *Valores:* N/A · *Default:* N/A
- `last-failure` — Shows the timestamp of the last unsuccessful execution. — *Valores:* N/A · *Default:* N/A
- `last-success` — Shows the timestamp of the last successful execution. — *Valores:* N/A · *Default:* N/A
- `task-status` — Shows the current task status. — *Valores:* idle | running | disabled · *Default:* N/A
- `output` — Shows the task output between “< >”(may be empty depending on the executed task). — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.9 | This command was introduced. |

**Usage Guidelines:**

The examples below show how to use the command show assistant-task. Example: Listing all configured tasks:

```text
# show assistant-task
TASK
```

NAME LAST START LAST FAILURE LAST SUCCESS STATUS --------------------------------------------------------------------------------------------- task_1 Fri Aug 20 08:46:00 -03 2019 Tue Aug 20 10:00:15 -03 2019 - idle task_2 Fri Aug 21 06:11:00 -03 2019 - - running It is possible to see a specific task, by providing the task name:

```text
# show assistant-task task_1
TASK
```

NAME LAST START LAST FAILURE LAST SUCCESS STATUS --------------------------------------------------------------------------------------------- task_1 Fri Aug 20 08:46:00 -03 2019 Tue Aug 20 10:00:15 -03 2019 - idle To see the actual output of executed task:

```text
DM4170# show assistant-task task_1 last-failure output
```

Last failed execution - Tue Aug 20 10:00:15 -03 2019 < The file backup.cli does not exist > The same is valid for successful output:

```text
DM4170# show assistant-task task_2 last-success output
% No entries found.
```

To see the actual status of the task:

```text
DM4170# show assistant-task task_1 task-status
Task status - idle
```

**Output Terms:**

Output Description Task Name Name of assistant task. Last Start Start time of the last execution. Last Failure Time of the last unsuccessful execution. Last Success Time of the last successful execution. Task status Current status of the task. Examples of this command are displayed in the Usage Guidelines Task output field

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show ssh-server`

> **Página:** 1834 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** sim

**Description:** Show the public key from Secure shell (SSH) server

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show ssh-server { public-key }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `public-key` — Show the public key of internal ssh-server. — *Valores:* No value. · *Default:* No default value.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | possible show the public keys and delete keys of equipment. The options include the all keys or by type keys. |

**Usage Guidelines:**

To show ssh public keys

```text
# show ssh-server public-key
Key information
```

Type: Size: Date Generated: Data:

**Output Terms:**

Output Description Status Internal public key from server

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `ssh`

> **Página:** 1836 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** “SSH” is an utility whose purpose is to allow the user to connect to a remote network host or device through a secure encrypted connection, after the connection has been established it is possible to execute commands on the remote destination host or device.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
ssh [ username@ ] ipv4-address [ port port-number ] [ vrf vrf-name ] [legacy]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `username@` — User name to login. — *Valores:* N/A · *Default:* User logged in the system.
- `ipv4-address` — Destination IPv4 address to connect. — *Valores:* N/A · *Default:* No default value.
- `port port-number` — Destination port. — *Valores:* 1-65535 · *Default:* 22
- `vrf vrf-name` — Specifies the VRF used for all outgoing SSH packets. — *Valores:* VRF name · *Default:* None
- `legacy` — Use this parameter to connect to SSH servers with old openSSH versions. Supported algorithms: HostKeyAlgorithms=ssh-dss,ssh-rsa, Ciphers=aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3descbc, KexAlgorithms=diffie-hellman-group1-sha1,diffie-hellmangroup14-sha1. — *Valores:* N/A · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 7.0 | Added VRF support. Added legacy parameter. On previous DmOS versions, the equipment |
| 8.0 | tried to connect automatically to SSH servers with old openSSH. From 8.0 version, it’s needed to use the parameter legacy explicitly. |

**Usage Guidelines:**

The following example shows how to use the ssh command with all options:

```text
hostname# ssh thomaz@10.0.120.80 port 23 vrf green legacy
```

The following example shows how to use the ssh command without server port, it will use the default value (22):

```text
hostname# ssh thomaz@10.0.120.80
```

The following example uses only ip address, it will use the logged user and the default port:

```text
hostname# ssh 10.0.120.80
```

**Impacts and precautions:**

VRFs global and mgmt are not supported.

**Hardware restrictions:**

N/A


### `ssh-server`

> **Página:** 1839 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** SSH server configurations.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
ssh-server { legacy-support | max-connections max-connections-number | port port-number}*
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `legacy-support` — Support for ssh clients running openssh versions older than 7.2. — *Valores:* N/A · *Default:* N/A
- `max-connections max-connections-number` — Defines the maximum number of SSH connections via CLI for each address family. NETCONF access connections are handled separately. — *Valores:* 1-16 · *Default:* 8
- `port port-number` — Defines the SSH server port number via CLI. — *Valores:* 22 | 1024-65535 · *Default:* 22

**Default:** N/A.

**History:**

| Release | Modification |
| --- | --- |
| 1.8.2 | Added support for ssh clients running openssh versions older than 7.0. |
| 1.12 | Parameter max-connections was added. |
| 2.4 | Parameter port was added. Legacy parameter must be used for ssh clients running openssh versions 8.0 older than 7.2. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure ssh-server legacy-support.

```text
(config)# ssh-server legacy-support
(config)# commit
```

The following warnings were generated: ’ssh-server’: Enabling legacy ssh key exchange algorithms will bring security vulnerabilities. Proceed? [yes,no] yes Commit complete. This example shows how to configure no ssh-server legacy-support.

```text
(config)# no ssh-server legacy-support
(config)# commit
```

Commit complete. To limit number of SSH connections Example: This example shows how to configure ssh-server max-connections.

```text
(config)# ssh-server max-connections 2
(config)# commit
```

Commit complete. This example shows how to return the number of ssh max-connection to the default value.

```text
(config)# no ssh-server max-connections
(config)# commit
```

Commit complete. To configure the port number of SSH Example: This example shows how to configure ssh-server port number.

```text
(config)# ssh-server port 2048
(config)# commit
```

The following warnings were generated: ’ssh-server port’: New SSH connections must use the configured port. Proceed? [yes,no] yes Commit complete. This example shows how to return the port number of ssh to the default value.

```text
(config)# no ssh-server port
(config)# commit
```

The following warnings were generated: ’ssh-server port’: New SSH connections must use the configured port. Proceed? [yes,no] yes Commit complete.

**Impacts and precautions:**

When legacy-support is enabled, a deprecated key exchange algorithm will be used. This can bring security vulnerabilities.

**Hardware restrictions:**

None.


### `ssh-server`

> **Página:** 1843 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Secure shell (SSH) server, for secure access from remote hosts.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
ssh-server generate-key { type | size }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `type` — Specifies the type of key to create. — *Valores:* {all | dsa | rsa | ecdsa | ed25519} · *Default:* None.
- `size` — Specifies the size of key to create. The option only present in keys of the type rsa. — *Valores:* 1024-2048 · *Default:* None.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | possible show the public keys and delete keys of equipment. The options include the all keys or by type keys. |
| 4.0 | Added support for ECDSA and ED25519 keys. |

**Usage Guidelines:**

To generated new keys, all types

```text
# ssh-server generate-key all
```

Really want to do this? [yes,no] yes Generated keys

```text
#
```

To generated keys dsa type

```text
# ssh-server generate-key dsa
```

Really want to do this? [yes,no] yes Generated keys

```text
#
```

To generated keys ecdsa type

```text
# ssh-server generate-key ecdsa
```

Really want to do this? [yes,no] yes Generated keys

```text
#
```

To generated keys ed25519 type

```text
# ssh-server generate-key ed25519
```

Really want to do this? [yes,no] yes Generated keys

```text
#
```

To generated keys rsa type

```text
# ssh-server generate-key rsa size 1024
```

Really want to do this? [yes,no] yes Generated keys

```text
#
```

**Output Terms:**

Output Description Status ‘Generated keys’ if success. Error message otherwise

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `telnet`

> **Página:** 1846 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** “TELNET” is a network protocol which uses TCP to stablish a connection with the destination host. Through TELNET it is possible to run programs, transmit data and execute many other remote administration tasks such as changing various settings on a device.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
telnet host [ port port-number ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `host` — Specifies the destination IPv4 address. — *Valores:* None. · *Default:* None.
- `port port-number` — (Optional) Specifies the destination port number. — *Valores:* Range: 1-65535 · *Default:* 23

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

The following example shows how to use the telnet command with all options:

```text
hostname# telnet 10.0.120.88 port 56
```

The following example shows how to use the telnet command without server port, it will use the default value (23):

```text
hostname# telnet 10.0.120.88
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `telnet-server`

> **Página:** 1848 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures internal telnet server for external access.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
telnet-server { enabled | disabled | max-connections max-connections-number | port port-number }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `enabled` — Enables the telnet server. — *Valores:* N/A · *Default:* N/A
- `disabled` — Disables the telnet server. — *Valores:* N/A · *Default:* N/A
- `max-connections max-connections-number` — Defines the maximum number of Telnet connections via CLI for each address family. — *Valores:* 1-16 · *Default:* 8
- `port port-number` — Defines the Telnet server port number via CLI. — *Valores:* 23 | 1024-65535 · *Default:* 23

**Default:** Disabled.

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. |
| 1.12 | Parameter max-connections was added. |
| 5.12 | Parameter port was added. |

**Usage Guidelines:**

Enable example:

```text
# config
(config)# telnet-server enabled
(config)# commit
```

Commit complete. Disable example:

```text
# config
(config)# telnet-server disabled
(config)# commit
```

Commit complete. To limit number of Telnet connections

```text
(config)# telnet-server max-connections 2
(config)# commit
```

Commit complete. This example shows how to return the number of telnet max-connection to the default value.

```text
(config)# no telnet-server max-connections
(config)# commit
```

Commit complete. This example shows how to configure telnet-server port number. DM4400(config)# telnet-server port 2048 DM4400(config)# commit Commit complete. This example shows how to return the port number of telnet to the default value. DM4400(config)# no telnet-server port DM4400(config)# Commit Commit complete.

**Impacts and precautions:**

None.

**Hardware restrictions:**

None.


### `who`

> **Página:** 1851 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Lists the current user sessions.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
who
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 4.6 | Telnet connections are now indicated by protocol ‘tcp’. |

**Usage Guidelines:**

Example:

```text
(config)# do who
```

Session User Context From Proto Date Mode 27 admin cli 192.168.0.10 tcp 20:41:25 config-exclusive 26 admin netconf 192.168.0.26 ssh 20:55:29 operational *25 admin cli 127.0.0.1 console 20:41:23 config-terminal

**Output Terms:**

Output Description Session Session identification User Connected user Context User session context: cli, netconf or snmp From Connection source IP address Proto Protocol used for connection: ssh, tcp (telnet) or console Date/time of user connection (date is only shown if different from Date current date) Output Description Current user mode: operational, config-exclusive, config-terminal or Mode config-shared

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A SYSTEM This topic describes the commands related to the device management such as commands of reboot and stacking.


## System

### `card-model`

> **Página:** 1854 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Switch the card-model to select 24XS+3CX or 24XS+4QX interface set.

**Supported Platforms:** This command is supported only in the following platforms: DM4270.

**Syntax:**

```text
card-model [card-model {card_model}]
```

**Parameters:**

- `card-model card_model` — Identifies the model of the card that will be used by DmOS. — *Valores:* 24XS+3CX or 24XS+4QX · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.7 | This command was introduced. |
| 4.9 | Addition of the 24XS+2QX+1CX option. Replaces card model 24XS+2CX with 24XS+3CX. Removes the support 5.12 to choose the model 24XS+2QX+1CX. |

**Usage Guidelines:**

The DM4270 has a flexible interface set composed of 24 10 Gbps Ethernet interfaces and four interfaces that can be used in two physical configurations: - three 100 Gbps interfaces; - four 40 Gbps interfaces. This design results in the two supported card-models: 24XS+3CX and 24XS+4QX. The “card-model” command selects which interface set will be used and takes effect after the factory configuration is automatically loaded and the device is rebooted. An example of the command usage is shown below.

```text
DM4270# card-model 24XS+4QX
```

Warning: The system will automatically reboot and load the factory configuration. Proceed with this action? [yes,NO] yes Loading. Done. Switching to runlevel: 6 Broadcast message from root@DM4270 (pts/0) (Thu Jan 10 17:04:37 2019): The system is going down for reboot NOW! Commit complete.

**Impacts and precautions:**

This command will cause the factory-config to be loaded and will reboot the device immediately. Be aware that this operation will cause loss of remote management access.

**Hardware restrictions:**

N/A


### `clear log`

> **Página:** 1857 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** This command allows you to delete all logs persisted in equipment.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
clear log
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `N/A`

**Default:** N/A

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


### `log`

> **Página:** 1859 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** This command focuses all logs system settings.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
log { severity { alert | critical | emergency | error | informational | notice | warning } | cli-commands | syslog ip-address [ vrf vrf-name ] [ port port ] [ source { ipv4 address ip-address | interface interface-name } ]}
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `severity { alert | critical | emergency | error | informational | notice | warning }` — This parameter allows you to set the minimum log level to be persisted. — *Valores:* N/A · *Default:* informational
- `cli-commands` — Include executed CLI commands in the user logs tagged with component “confd_audit”. — *Valores:* N/A · *Default:* None
- `syslog ip-address` — This parameter allows the registration of IP(v4/v6) hosts to receive the logs generated by the equipment. It can add up to six hosts. — *Valores:* a.b.c.d or X:X:X:X::X. · *Default:* None
- `vrf vrf-name` — (Optional) Specifies the name of VRF which the syslog server can be reached. — *Valores:* String. · *Default:* None.
- `port port` — (Optional) Specifies the port that syslog server is listening for UDP syslog messages. — *Valores:* 514, 1025-65534 · *Default:* 514
- `source ipv4 address ip-address` — (Optional) Specify the source ip address where syslog messages should be send through. — *Valores:* a.b.c.d. · *Default:* None
- `source interface interface-name` — (Optional) Specify the source interface where syslog messages should be send through. — *Valores:* Interface name in format l3-<name> or loopback-<id>. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 5.2 | Added vrf option to syslog configuration. |
| 5.12 | Added option to configure UDP port for syslog server. Added option to configure source ipv4 address and interface for syslog 6.0 server. Added option to allow commands executed on CLI to be shown in the 10.8.0 User Logs. |

**Usage Guidelines:**

Enable syslog to server 172.22.110.101, associate to vrf green, configure a UDP port and source ip-address 172.22.110.10

```text
# config
(config)# vrf green
(config-vrf-green)# top
(config)# dot1q vlan 100
(config-vlan-100))# top
(config)# interface l3 l3
(config-l3-l3)# lower-layer-if vlan 100
(config-l3-l3)# ipv4 address 172.22.110.10/24
(config-l3-l3)# vrf green
(config-l3-l3)# top
(config)# log syslog 172.22.110.101 vrf green port 5000 source ipv4 address 172.22.110.10
(config-syslog-172.22.110.101)# commit
```

Commit complete. Enable cli-commands configuration.

```text
# config
(config)# log cli-commands
(config)# commit
```

Commit complete.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `reboot`

> **Página:** 1863 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Restarts the system.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
reboot
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.2 | This command was introduced. |
| 1.10 | The chassis and slot parameters were removed. |

**Usage Guidelines:**

This command is to be used when the user wants to restart the entire system. For restarting the system in cases when the system can not be restarted using this command, see the reboot-forced command. This command is safe because it only restarts the system after terminating its activities that includes storing the remaining data and unmounting the partitions.

**Impacts and precautions:**

None

**Hardware restrictions:**

None


### `reboot-forced`

> **Página:** 1865 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Restarts the system using forced mode.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
reboot-forced
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.2 | This command was introduced. |
| 1.10 | The chassis and slot parameters were removed. |

**Usage Guidelines:**

This command is to be used when the user wants to restart the system despite any software hang problem that may happen, which would prevent the system of being restarted using the reboot command.

**Impacts and precautions:**

It may cause permanent loss of configuration or other data, because a critical operation can be interrupted. It can happen if the equipment was restarted during a configuration commit or firmware activation, for example. Use only if the reboot command fails.

**Hardware restrictions:**

None


### `show inventory`

> **Página:** 1867 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** This command displays the system inventory information, including the part number, hardware version, serial number and other relevant information.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show inventory [chassis {chassis_id} [brief | factory-codes | macs | transceivers | slot {slot_id} [brief | factory-codes | macs | transceivers | port [port_type] [port_id] [mac | transceiver]]]]
```

**Parameters:**

- `chassis chassis_id` — Chassis Identifier. If the value of this parameter is ‘*’ or ‘ ’, a list of all present chassis will be shown. Currently only one chassis_id is supported. — *Valores:* 1 · *Default:* None
- `brief` — Shows brief inventory information about the chassis or a specific card. — *Valores:* N/A · *Default:* N/A
- `factory-codes` — Shows factory information about the chassis or a specific card. — *Valores:* N/A · *Default:* N/A
- `macs` — Shows the MAC addresses of all ports of the chassis or a specific card. — *Valores:* N/A · *Default:* N/A
- `transceivers` — Shows inventory information about all transceivers present on chassis or a specific card. — *Valores:* N/A · *Default:* N/A
- `slot slot_id` — Identifies a card present on chassis. If the value of this parameter is ‘*’ or ‘ ’, a list of all present cards will be shown. This will be dependent on the product being managed. The values below are for Dm4610. — *Valores:* 1, PSU1, PSU2 or FAN · *Default:* None
- `port port_type` — Identifies the desired type of port present on the card. If the value of this parameter is ‘*’ or ‘ ’, a list of all ports of the card will be shown. This will be dependent on the product being managed. The values below are for Dm4610. — *Valores:* gigabit-ethernet, gpon or ten-gigabit-ethernet · *Default:* None
- `port_type port_id` — Identifies a port of a specific type. If the value of this parameter is ‘*’ or ‘ ’, a list of all ports of the card with the desired type will be shown. This parameter values are dependent on the card present at the card. The value below is for Dm4610 cards. — *Valores:* 1-12 · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.2 | Added support for displaying transceiver inventory information |
| 5.10 | Added fiber type information for transceivers |

**Usage Guidelines:**

The user can display information about chassis, slots, ports and transceivers. Please see below examples of usage for each type of inventory information in display. This example shows how to display the chassis inventory

```text
DM4610# show inventory chassis 1
Chassis : 1
Product model : DM4610
Chassis/Slot : 1/1
Product model : 8GPON+8GX+4GT+2XS
...
```

This example shows how to display a slot’s inventory

```text
DM4610# show inventory chassis 1 slot PSU1
Chassis/Slot : 1/PSU1
```

Product model : PSU 120 AC Part number : 800.5079.03 Serial number : 3047214 Product revision : 3 ... This example shows how to display a transceiver’s inventory

```text
DM4610# show inventory chassis 1 slot 1 port gigabit-ethernet 1 transceiver
Interface gigabit-ethernet 1/1/1
Port type : Transceiver
Transceiver information
Presence : Yes
```

Vendor name : APAC Opto ...

**Output Terms:**

Output Description Chassis/Slot Chassis and slot identification Product model Hardware model of the product/card Part number Product part number Serial number Product serial number Product revision Product revision PCB revision Printed Circuit Board revision Hardware version Hardware version Operat. temp. Range of operating temperature System MAC address Product MAC Address in hexadecimal presentation Factory code Equipment factory information Interface Physical interface type and location in the format Chassis/Slot/Port MAC address Interface MAC Address in hexadecimal presentation, if applicable Port type Port type of the interface, which may be Electrical or Transceiver Transceiver Presence and inventory information of the transceiver information Presence Informs if the transceiver is present Output Description Vendor name Name of the vendor that provides this Transceiver Serial number Transceiver serial number Part number Transceiver part number Type Transceiver type, e.g., SFP, QSFP. Media Transceiver media, e.g., Optical, Electrical. Connector Transceiver connector Laser wavelength Transceiver wavelength Fiber Type Transceiver supported fiber type, e.g., Single Mode, Multimode. Ethernet standards Transceiver supportted ethernet standards Digital Diagnostics Transceiver digital diagnostics thresholds thresholds

**Impacts and precautions:**

If any value is identified as Not Available, it will be considered as having no meaning in that particular chassis/slot/interface. If any value is identified as Unknown, it means that the value is valid for that particular chassis/slot/interface, but it wasn’t possible to obtain that information.

**Hardware restrictions:**

N/A


### `show log`

> **Página:** 1873 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display all logs persisted in equipment.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show log [component {components}* | severity {severities}* | tail {number_of_logs}]
```

**Parameters:**

- `component {components}*` — If this filter is used, only messages generated by the specified components are displayed. A component is an identifier for the functionality which the log message refers to. More than one component can be filtered at the same time. — *Valores:* {components}* · *Default:* N/A
- `severity {severities}*` — If this filter is used, only messages generated with the specified severities will be displayed. More than one severity can be filtered at the same time. — *Valores:* alert, critical, emergency, error, informational, notice, warning · *Default:* N/A
- `tail {number_of_logs}` — Show only the last logs. — *Valores:* 1-65535. · *Default:* 10

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. New format for logs output. Added MessageCode, ProcessName and PID 1.8 fields. |
| 1.12 | Added the parameter ‘tail’ that allows to show only the last logs. |

**Usage Guidelines:**

Log entries are displayed in the following general format: Date Time : Slot : <Severity> %Component-MessageCode : ProcessName[PID] : Text This example shows how to display all equipment logs:

```text
DM4610# show log
```

Show Contents of All Known UserLog Files *** Active Log File *** 2015-07-23 00:01:33.919 : 1/1 : <Info> %SYS_CONFIG-HOSTNAME_CHANGED : sys_configd[2025] : The hostname of equipment has been changed to: ’DM4610’ 2015-07-23 00:02:13.106 : 1/1 : <Notice> %CARDMGR-CARD_INSERTED : card-mgr[2032] : Card inserted in slot 1/1 (model: 8GPON+8GX+4GT+2XS, serial number: 3048274) 2015-07-23 00:02:15.907 : 1/1 : <Notice> %CARDMGR-CARD_INSERTED : card-mgr[2032] : Card inserted in slot 1/PSU1 (model: Not supported, serial number: 3047195) 2015-07-23 00:02:15.914 : 1/1 : <Notice> %CARDMGR-CARD_INSERTED : card-mgr[2032] : Card inserted in slot 1/FAN (model: DM4610 FAN, serial number: Not available) 2015-07-23 00:02:16.209 : 1/1 : <Notice> %TCV-TCV_INSERTED : tcvd[2047] : Transceiver inserted at interface gigabit-ethernet-1/1/1. 2015-07-23 00:02:16.253 : 1/1 : <Notice> %TCV-TCV_INSERTED : tcvd[2047] : Transceiver inserted at interface gigabit-ethernet-1/1/8. ** End of log ** (6 records) This example shows how to display logs generated by specific components:

```text
DM4610# show log component aaa card_manager
```

Show Contents of All Known UserLog Files *** Active Log File *** 2015-07-23 00:02:13.106 : 1/1 : <Notice> %CARDMGR-CARD_INSERTED : card-mgr[2032] : Card inserted in slot 1/1 (model: 8GPON+8GX+4GT+2XS, serial number: 3048274) 2015-07-23 00:02:15.907 : 1/1 : <Notice> %CARDMGR-CARD_INSERTED : card-mgr[2032] : Card inserted in slot 1/PSU1 (model: Not supported, serial number: 3047195) 2015-07-23 00:02:15.914 : 1/1 : <Notice> %CARDMGR-CARD_INSERTED : card-mgr[2032] : Card inserted in slot 1/FAN (model: DM4610 FAN, serial number: Not available) 2015-07-23 00:05:36.545 : 1/1 : <Info> %AAA-GROUP_ASSIGN : authenticationd[2060] : User [admin]: Was assigned to groups: admin. ** End of log ** (5 records) This example shows how to display logs from specific severities:

```text
DM4610# show log severity informational warning
```

Show Contents of All Known UserLog Files *** Active Log File *** 2015-07-23 00:02:12.238 : 1/1 : <Info> %CARDAPP-INITIAL_SYSTEM_SETUP_STARTED : card-app[2153] : The system initial configuration has been started 2015-07-23 00:02:15.343 : 1/1 : <Info> %HWMONITOR-FAN_DETECTED : hal_devices [2179] : New FAN device detected. FAN ID 1/FAN/1 2015-07-23 00:02:16.253 : 1/1 : <Info> %CARDAPP-INITIAL_SYSTEM_SETUP_FINISHED : card-app[2153] : The system initialization is complete 2015-07-23 00:02:21.009 : 1/1 : <Warn> %TCV-UNSUPPORTED_TCV_INSERTED : tcvd[2210] : Unsupported transceiver detected in interface gigabit-ethernet-1/1/1. Ethernet Standard 1000BASE-T read from transceiver. 2015-07-23 00:02:23.217 : 1/1 : <Warn> %ETHL1-ETHL1_STATUS_DOWN : ethl1portmgr [2266] : Interface gigabit-ethernet-1/1/4 changed state to down (Admin state: up) ** End of log ** (5 records)

**Output Terms:**

Output Description Date Date of log entry in the format: YYYY-MM-DD. Time of log entry in the format: hh:mm:ss.ddd (3 digits for the deciTime mal fraction of a second). Slot Chassis/slot where the log message was generated. Severity Severity level of the log message. An identifier for the functionality which the log message refers to. Component Each log Component comprises a set of Message Codes. MessageCode An identifier (mnemonic) for the log message. The name of the operational system process that generated the log ProcessName message. It may not be unique. The ID of the operational system process that generated the log mesPID sage. It is unique inside the corresponding slot. It may not be unique across a multi-CPU system. The log message itself, which may contain fixed and variable parts, Text describing an event.

**Impacts and precautions:**

The use of show log or another verbose command under serial interface may cause the session to become unresponsive to user intervention (until the command finishes its execution). Consider this before executing the respective command.

**Hardware restrictions:**

N/A


### `show platform`

> **Página:** 1877 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** This command is used to show information about the system cards, like firmware version and status.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show platform [chassis {chassis_id} [detail | slot {slot_id} [detail]]]
```

**Parameters:**

- `chassis chassis_id` — Chassis identifier. If the value of this parameter is ‘*’ a list of all present chassis will be shown. Currently only one chassis_id is supported. — *Valores:* 1 · *Default:* None
- `detail` — Shows detailed system information about a chassis or a specific card. — *Valores:* N/A · *Default:* N/A
- `slot slot_id` — Identifies a card present on chassis. If the value of this parameter is ‘*’ a list of all present cards will be shown. This parameter will be dependent on the product being managed. The possible values for Dm4610 are displayed below. — *Valores:* 1, PSU1, PSU2 or FAN · *Default:* None

**Default:** N/A. There is no default profile.

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.2 | The command was changed and the detail option was introduced. |

**Usage Guidelines:**

The user can display status, role and firmware version information about all chassis and cards present at the system. Some of the information for it can be found at other commands, like show inventory and show firmware, so this is the place to summarize it and display it in a concise form. An example of the command is displayed below.

```text
DM4610# show platform
```

Chassis/Slot Product model Role Status Firmware version ------------- ----------------- ------- ------------ ---------------------- 1 DM4610 - - Not available 1/1 8GPON+8GX+4GT+2XS Master Ready 1.4.0-116-1-ga3bd61b 1/FAN DM4610 FAN Passive Ready Not available 1/PSU2 PSU 120 AC Passive Ready Not available

**Output Terms:**

Output Description Chassis/Slot Chassis and slot identification Product model Hardware model of the chassis or slot Role Role of each card: Master, Standby, Active or Passive Status Status of each card: Ready, Initializing, Blocked, or Failed Firmware version Firmware version of the card, if available

**Impacts and precautions:**

If any value is identified as Not Available, it will be considered as having no meaning in that particular chassis/slot. Example of this is the field “Firmware version” in the command displayed at the Usage guidelines.

**Hardware restrictions:**

N/A


### `show system reboot`

> **Página:** 1880 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** sim

**Description:** Shows the reason of the last system reboot.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show system reboot
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0 | This command was introduced. |
| 5.2.0 | Added internal power supply failure reboot reason. |

**Usage Guidelines:**

This command should be used when the user wants to identify the reason of the last (most recent) system reboot. Possible reboot causes: - Reboot requested by user; - Firmware activation requested by user; - Over Temperature Protection (OTP) mode recovery; - Power input failure; - Internal power supply failure; - System failure (crash); - Unknown reason. This information remains available until the next reboot, and then it gets overwritten. This status is logged in user logs, and is available through SNMP.

**Output Terms:**

Output Description Last reboot cause Shows the last reboot reason.

**Impacts and precautions:**

None

**Hardware restrictions:**

None DHCP This topic describes the commands related to management of DHCP Server and Relay such as commands to configure DHCP Pools and timers or to inspect the devices connected to local server.


## DHCP

### `dhcp l2-relay`

> **Página:** 1882 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure settings related to the DHCP Relay L2. For DHCPv4 packets, DHCP L2 Relay is responsible for the insertion of DHCP information option 82 field as specified in Section 3.9.1/TR-101 and 5.7/TR-156. For DHCPv6 packets, DHCP L2 Relay is responsible for the exchange of the DHCPv6 message using Relay-Forward/Relay-Reply message format and for the insertion of Interface-ID option as specified in Section 5.7/TR-177. This function only works for packets switched among GPON service-ports and uplink ethernet ports. Packets switched among ethernet ports are forwarded transparently.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
dhcp l2-relay [ vlan vlan-id ] [ circuit-id format format ] [filter-by {ip | mac}]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `vlan vlan-id` — Enable DHCP Relay L2 on VLAN. Max number of VLANs is 234. The options to configure are: a single VLAN, list or range of VLANs and both combinations, range and list. — *Valores:* 1-4094 · *Default:* None
- `circuit-id format format` — Configure a format template for DHCP Relay L2 Option 82 Circuit-ID, for DHCPv4, or Interface-ID option, for DHCPv6. The format template can be composed by literal text and the combination of available fields separated by, at least, one delimiter. Available fields are described below, and are case insensitive. Optional fields: <gemPort> <oltSlot> <panelPort> <onuId> <onuSerial> <hostname> <onuSlot> <svlan> Delimiters: space . / : Note: Ensure that the Circuit-ID is unique for each device. Using duplicate or non-unique Circuit-IDs may cause misidentification or conflicts on the DHCP server side, leading to incorrect IP assignments or service issues. — *Valores:* Text up to 136 characters. Valid characters are A-Z, a-z, 0-9, space and . / @ : The circuit-id generated by this template must not exceed 63 bytes. · *Default:* <hostname> eth <oltSlot>/<panelPort>/<onuId>/<onuSlot>/
- `<gemPort>:<svlan> filter-by {ip | mac}` — Configure a data traffic filter rule. The filter by IP option (default mode) allows the data traffic with anti-ip-spoofing functionality. On the filter by MAC mode, the traffic is allowed via MAC address. — *Valores:* List of supported filters: ip and mac. · *Default:* ip.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.6 | This command was introduced. |
| 5.6 | Command was modified from ‘dhcp relay’ to ‘dhcp l2-relay’. |
| 6.4 | Support to custom Circuit-ID format. |
| 7.0 | Support to traffic filter by MAC. |
| 8.0 | Support to DHCPv6 messages. |

**Usage Guidelines:**

Usage example of configuring a VLAN of ID 15:

```text
# config
(config)# dhcp l2-relay vlan 15
(config)# commit
```

Commit complete. Usage example of configuring a VLAN range from ID 1 to 10:

```text
# config
(config)# dhcp l2-relay vlan 1-10
(config)# commit
```

Commit complete. Usage example of configuring a list containing the VLAN IDs 1, 10 and 15:

```text
# config
(config)# dhcp relay vlan 1,10,15
(config)# commit
```

Commit complete. Usage example of configuring circuit-id format with a fixed string, onuSerial and gemPort:

```text
# config
(config)# dhcp l2-relay circuit-id format <onuSerial> fixed string <gemPort>
(config)# commit
```

Commit complete. Usage example of configuring a VLAN of ID 20 with filter by MAC:

```text
# config
(config)# dhcp l2-relay vlan 20 filter-by mac
(config)# commit
```

Commit complete.

**Output Terms:**

Output Description <hostname> Hostname for this equipment. Equipment line card slot. Fixed value 1 for equipment that doesn’t <oltSlot> support line card. <panelPort> Equipment ponlink numeric id as seen physically in panel. <onuId> Numeric ONU ID (0-127) configured within a PON. <onuSerial> ONU Serial value (e.g. DACM12345678). <svlan> Uplink Service VLAN. <gemPort> ONU numeric config-level GEM ID (1-40). <onuSlot> Fixed value 0.

**Impacts and precautions:**

For backward compability purposes, ‘dhcp relay vlan’ command is mapped to ‘dhcp l2- relay vlan’. Avoid setting dhcp l2-relay to a VLAN configured as ‘service vlan type tls’, since it will disable DHCP traffic inspection. When DHCP relay is turned on for a given VLAN, it monitors for DHCP packets of all service-ports running over this VLAN. After the DHCPv4 session is properly established, a filter is installed at HW level to allow traffic on the respective service-port for the particular assigned IPv4 address. After the DHCPv6 session is properly established, a filter is installed at HW level to allow traffic on the respective service-port for all IPv6 addresses. If there is no renew within the assigned lease time, the filter is removed, blocking all user traffic for the particular service-port. Server DHCP packets (such as DHCPACK or REPLY) received on service-ports are silent discarded. Downstream DHCP packets that not match circuit-id sintax are discarded. Circuit-id format <hostname> field is used to determine whether a downstream dhcp packet must be processed or forwarded to other ethernet interfaces. When this field is not configured, the packet will be processed if circuit-id information format matches. For DHCPv4 packets, DHCP L2 relay inserts information option 82 with suboption 1 and suboption 2, with the following content as defined in R-127/TR-156: 1) Suboption 1 - Default Agent Circuit ID: <hostname> eth <oltSlot>/<oltPort>/<onuId>/0/<gemPort>:<svlan> Example for VLAN 333, gem 2, onu 55, PON link 1/1/3: DM4610 eth 1/3/55/0/2:333 2) Suboption 2 - Remote Circuit ID: Contains the ONU name configured under the ONU configuration path. For DHCPv6 packets, DHCP L2 relay encapsulates the original DHCP message into a Relay-Forward/Relay-Reply message and inserts Interface-ID option, with the following content as defined in R-127/TR-156: 1) Interface-ID: <hostname> eth <oltSlot>/<oltPort>/<onuId>/0/<gemPort>:<svlan> Example for VLAN 333, gem 2, onu 55, PON link 1/1/3: DM4610 eth 1/3/55/0/2:333

**Hardware restrictions:**

On DM4618, the parameter filter-by is not supported as this platform has no filter limitation and that way is able to use only the default mode (IP option).


### `dhcp relay`

> **Página:** 1888 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure settings related to the DHCP Relay Agent function.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618, DM4920.

**Syntax:**

```text
dhcp relay instance-name dhcp relay instance-name server ipv4 a.b.c.d dhcp relay instance-name interface interface-name dhcp relay instance-name information [ check | option | trust-all | policy { keep | drop | replace } ] dhcp relay instance-name vrf vrf-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-name` — Specifies the name of the DHCP Relay instance. — *Valores:* String with up to 64 characters. · *Default:* N/A
- `server ipv4 a.b.c.d` — Specifies a list of DHCP servers that will be used by the DHCP relay agent to forward DHCP client messages. Up to 16 DHCP server IPv4 addresses can be specified. — *Valores:* IPv4 address in a.b.c.d format. · *Default:* N/A
- `interface interface-name` — Specifies a list of L3 interfaces to be part of the DHCP relay agent instance pool. Adding a L3 interface to the DHCP agent instance means that all DHCP client packets arriving in the related VLAN will be relayed to the configured DHCP servers. — *Valores:* It must be a valid L3 interface name with “l3-” prefix. L3 interface must be in the same VRF of DHCP relay instance. · *Default:* N/A
- `information check` — If enabled, DHCP Relay will check for a valid option 82 coming from DHCP server packets and drop them in case they don’t contain an option 82. This configuration is valid only for drop and replace information policies and when information option is enabled. When information policy is set to keep mode, check configuration is ignored, that is, no verification is performed. — *Valores:* N/A · *Default:* Enabled.
- `information option` — When enabled, instructs the DHCP Relay agent to add DHCP option 82 to DHCP client packets. DHCP relay agent will strip off option 82 from packets arriving from the DHCP server before sending them back to the user side. Option 82 circuit-ID is filled with the physical interface short name from which the DHCP client packet arrived plus the VLAN information. That is, circuit-ID will have the format <itf-name>:<vlan-id>, for example “1ge-1/1/1:4012”, “10ge-1/1/1:4012”, “40ge-1/1/1:4012”, “100ge-1/1/1:4012”. Option 82 remote-ID is always equal to the in-band management MAC/hardware address of the switch. — *Valores:* N/A · *Default:* Disabled.
- `information trust-all` — Instructs the DHCP relay agent to trust DHCP client packets containing information option 82 but without GIADDR set. By default, if the gateway address (GIADDR) is set to all zeros in the DHCP packet and the relay agent information option is already present in the packet, the DHCP relay agent will discard the packet. In other words, when the configuration is disabled (default), DHCP relay discards messages carrying option 82. Use the command to override this behavior and accept the packets. This configuration is independent from the information policy (keep/drop/replace). When trust-all is enabled, the relay agent will replace or set the GIADDR field to its own IP address when GIADDR is not present or when it is set to all zeros. — *Valores:* N/A · *Default:* Disabled.
- `information policy` — Configures the information option 82 strategy for the DHCP relay agent instance. Policy behavior: • keep: Packet has no option 82 field: append option 82 Packet includes an option 82 field: keep incoming option 82 untouched • replace: Packet has no option 82 field: append option 82 Packet includes an option 82 field: replace incoming option 82, rewriting circuit/remote IDs • drop: Packet has no option 82 field: append option 82 Packet includes an option 82 field: drop packet — *Valores:* drop | keep | replace · *Default:* replace
- `vrf vrf-name` — Assign a VRF instance to the DHCP relay agent instance. — *Valores:* Name of an existent VRF. · *Default:* global

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.2 | DHCP Relay command added. |
| 8.0 | The VRF parameter was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a DHCP Relay for VLAN 200 relaying client requests to VLAN 300 with DHCP option 82 turned on.

```text
(config)# dot1q vlan 200
(config-vlan-200)# interface gigabit-ethernet-1/1/1-24
(config-dot1q-interface-gigabit-ethernet-1/1/1-24)# top
(config)# dot1q vlan 300
(config-vlan-300)# interface ten-gigabit-ethernet-1/1/1-2
(config-dot1q-interface-ten-gigabit-ethernet-1/1/1-2)# top
(config)# interface l3 itf-vlan200
(config-l3-itf-vlan200)# ipv4 address 192.168.1.25/24
(config-l3-itf-vlan200)# lower-layer-if vlan 200
(config-l3-itf-vlan200)# top
(config)# interface l3 itf-vlan300
(config-l3-itf-vlan300)# ipv4 address 10.1.1.25/24
(config-l3-itf-vlan300)# lower-layer-if vlan 300
(config-l3-itf-vlan300)# top
(config)# dhcp relay test
(dhcp-relay-test)# server ipv4 10.1.1.100
(config-ipv4-10.1.1.100)# exit
(dhcp-relay-test)# information option
(dhcp-relay-test)# interface l3-itf-vlan200
(config-interface-l3-itf-vlan200)# exit
```

Following the settings above, this configuration shows how to configure a switch to relay DHCP client messages with VLAN 200 coming from an OLT with DHCP option 82 relay agent turned on.

```text
(config)# dhcp relay test
(dhcp-relay-test)# information policy keep
(dhcp-relay-test)# information trust-all
```

Also following the settings above, this configuration shows how to configure a switch to relay DHCP client messages using vrf and with VLAN 200 coming from an OLT with DHCP option 82 relay agent turned on.

```text
(config)# vrf red
(config-vrf-red)# top
(config)# interface l3 itf-vlan200
(config-l3-itf-vlan200)# vrf red
(config-l3-itf-vlan200)# top
(config)# interface l3 itf-vlan300
(config-l3-itf-vlan300)# vrf red
(config-l3-itf-vlan300)# top
(config)# dhcp relay test
(dhcp-relay-test)# vrf red
```

**Impacts and precautions:**

The maximum number of DHCP relay instances will be limited to the maximum L3 interfaces allowed. In scenarios with a very high load of DHCP messages, the system can experience an increase of CPU usage for a period of time until DHCP sessions are established. It is not possible to set a specific source IP or source interface to be used to send relayed packets to the DHCP server. DmOS will set the source IP address of the interface from which the target network is reachable. Information option is filled with the physical interface name, regardless this interface is a part of a link aggregation or not. For platforms that have service vlan configuration (such as OLTs), DHCP relay cannot be turned on for a TLS service vlan.

**Hardware restrictions:**

N/A


### `dhcp relay if-option`

> **Página:** 1894 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configure interface specific settings related to the DHCP Relay Agent function.

**Supported Platforms:** This command is not supported in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4618, DM4920.

**Syntax:**

```text
dhcp relay instance-name if-option interface-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `if-option interface-name` — Enter in per-interface information configuration. Configuration made for any specific interface will override the DHCP relay instance information settings for the given interface. Other interfaces without if-option specific settings will follow the DHCP relay instance information configuration. — *Valores:* It must be a valid ethernet interface name, such as gigabit-ethernet-X/Y/Z or ten-gigabit-ethernet-X/Y/Z. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.2 | DHCP Relay if-option command added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to configure a DHCP Relay for VLAN 200 relaying client requests to VLAN 300 with DHCP option 82 turned on. For gigabit-ethernet-1/1/1, interface is configured as trusted and with keep information policy. This configuration can be used to relay DHCP client messages coming from an OLT with DHCP option 82 relay agent turned on which is connected to gigabit-ethernet-1/1/1.

```text
(config)# dot1q vlan 200
(config-vlan-200)# interface gigabit-ethernet-1/1/1-24
(config-dot1q-interface-gigabit-ethernet-1/1/1-24)# top
(config)# dot1q vlan 300
(config-vlan-300)# interface ten-gigabit-ethernet-1/1/1-2
(config-dot1q-interface-ten-gigabit-ethernet-1/1/1-2)# top
(config)# interface l3 itf-vlan200
(config-l3-itf-vlan200)# ipv4 address 192.168.1.25/24
(config-l3-itf-vlan200)# lower-layer-if vlan 200
(config-l3-itf-vlan200)# top
(config)# interface l3 itf-vlan300
(config-l3-itf-vlan300)# ipv4 address 10.1.1.25/24
(config-l3-itf-vlan300)# lower-layer-if vlan 300
(config-l3-itf-vlan300)# top
(config)# dhcp relay test
(dhcp-relay-test)# server ipv4 10.1.1.100
(config-ipv4-10.1.1.100)# exit
(dhcp-relay-test)# information option
(dhcp-relay-test)# interface l3-itf-vlan200
(config-interface-l3-itf-vlan200)# exit
(config-relay-tste)# if-option gigabit-ethernet-1/1/1
(config-if-option-gigabit-ethernet-1/1/1)# information option
(config-if-option-gigabit-ethernet-1/1/1)# information policy keep
(config-if-option-gigabit-ethernet-1/1/1)# information trust-all
(config-if-option-gigabit-ethernet-1/1/1)# exit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show dhcp l2-relay`

> **Página:** 1897 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Display information about the configured dhcp l2 relay agents.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
show dhcp l2-relay
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 8.4 | This command was introduced. |

**Usage Guidelines:**

Given the equipment has DHCP L2 relay configured and the following IP/Prefixes were granted: IP Address 200.0.0.51, Interface service-port-1, VLAN 3001, IP Address 2012::100, Interface service-port-2, VLAN 3002, IP Address da7a:c03::/64, Interface service-port-3 and VLAN 3003. Let’s see the show information: IP Address/Prefix Interface VLAN ----------------------------------------------------------------------------- 200.0.0.51 service-port-1 3001 2012::100 service-port-2 3002 da7a:c03::/64 service-port-3 3003

**Output Terms:**

Output Description IP Address/Prefix IP address or prefix granted to the l2 relay agent. Interface Interface which the IP address or prefix was assigned VLAN Vlan which the l2 relay agent is configured.

**Impacts and precautions:**

None

**Hardware restrictions:**

None PPP This topic describes the commands related to management of PPP services such as commands to configure PPPoE or PPP CHAP.


## PPP

### `intermediate-agent Chassi/Slot/Port`

> **Página:** 1899 · **Modo:** Configuration mode · **Privilégios:** Access level config · **Leitura (show/display):** não

**Description:** Configuration of PPPoE Intermediate Agent.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
intermediate-agent Chassi/Slot/Port intermediate-agent Chassi/Slot/Port sub-option circuit-id intermediate-agent Chassi/Slot/Port sub-option format intermediate-agent Chassi/Slot/Port sub-option remote-id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `Chassi/Slot/Port` — Indicates the Chassi/Slot/Port configured. — *Valores:* 1/1/1 · *Default:* None
- `sub-option circuit-id circuit-id` — Sets the circuit identifier — *Valores:* None · *Default:* true
- `sub-option format format` — Configure a format template for PPPoE Circuit-ID, sub-option circuit-id must be enabled. The format template can be composed by literal text and the combination of available fields separated by, at least, one delimiter. Available fields are described below, and are case insensitive. Optional fields: <hostname> <oltSlot> <panelPort> <onuId> <onuSerial> <onuSlot> <gemPort> <svlan> Delimiters: space . / : — *Valores:* Text up to 136 characters. Valid characters are A-Z, a-z, 0-9, space and . / @ : The circuit-id generated by this template must not exceed 63 bytes. · *Default:* <hostname> eth <oltSlot>/<panelPort>/<onuId>/<onuSlot>/
- `<gemPort>:<svlan> sub-option remote-id remote-id` — Sets the remote identifier — *Valores:* None · *Default:* true

**Default:** N/A. There is no default profile.

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |
| 8.0 | Support to custom Circuit-ID format. |

**Usage Guidelines:**

Usage example of configuring circuit-id format with a fixed string, onuSerial and gemPort:

```text
# config
(config)# pppoe intermediate-agent 1/1 sub-option format <onuSerial> fixed string <gemPort>
(config)# commit
```

Commit complete.

**Output Terms:**

Output Description <hostname> Hostname for this equipment. Equipment line card slot. Fixed value 1 for equipment that doesn’t <oltSlot> support line card. <panelPort> Equipment ponlink numeric id as seen physically in panel. <onuId> Numeric ONU ID (0-127) configured within a PON. Output Description <onuSerial> ONU Serial value (e.g. DACM12345678). <onuSlot> Fixed value 0. <gemPort> ONU numeric config-level GEM ID (1-40). <svlan> Uplink Service VLAN.

**Impacts and precautions:**

None

**Hardware restrictions:**

None


### `pppoe`

> **Página:** 1903 · **Modo:** Configuration mode · **Privilégios:** Access level config · **Leitura (show/display):** não

**Description:** This module contains definitions for the PPPoE(Point-to-Point Protocol over Ethernet)

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
pppoe
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `None` — None — *Valores:* None · *Default:* None

**Default:** N/A. There is no default profile.

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |

**Usage Guidelines:**

None

**Output Terms:**

Output Description None None.

**Impacts and precautions:**

None

**Hardware restrictions:**

None


### `show pppoe intermediate-agent sessions interface gpon Chassi/Slot/Port`

> **Página:** 1905 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Access level audit · **Leitura (show/display):** sim

**Description:** Show information about active PPPoE sessions.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
show pppoe intermediate-agent sessions interface gpon Chassi/Slot/Port
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `Chassi/Slot/Port` — Indicates the Chassi/Slot/Port configured. — *Valores:* 1/1/1 · *Default:* None

**Default:** N/A. There is no default profile.

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |

**Usage Guidelines:**

None

**Output Terms:**

Output Description interface, ONU ID, session id, remote Interfaces. mac

**Impacts and precautions:**

None

**Hardware restrictions:**

None CHAPTER 17: MODULAR CHASSIS This chapter describes the commands related to management of a modular chassis in the DmOS CLI. PROVISIONING This topic describes commands related to card provisioning in DmOS CLI.
