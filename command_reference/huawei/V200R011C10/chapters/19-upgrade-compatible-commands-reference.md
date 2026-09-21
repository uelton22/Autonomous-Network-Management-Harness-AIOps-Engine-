# Capítulo 19: Upgrade-compatible Commands Reference

> Fonte: `doc_huawei_datacom/huawei` · Huawei VRP Issue 14 (2021-10-20) · S1720, S2700, S5700, and S6720 Series Ethernet Switches

This chapter describes upgrade-compatible commands of each feature of all fixed switches.Upgrade-compatible commands are supported in earlier versions, but are deleted in the new version or have the command format changed. They exist to prevent configuration loss or impact on other configurations after the upgrade. Due to version evolution, there may be changes on upgrade-compatible commands supported by some products. This chapter does not describe the differences. Upgrade-compatible commands are classified into two types based on user operations:

- You can write these commands to the configuration file but cannot run them in the CLI after the device restarts.

- You can run these commands by entering commands in their complete format. NOTE You are not advised to use upgrade-compatible commands to perform operations on the device. If required, perform operations under the guidance of technical support personnel. 19.1 Basic Configuration Compatible Commands 19.2 Device Management Compatible Commands 19.3 Interface Management Compatible Commands 19.4 Ethernet Switching Compatible Commands 19.5 IP Service Compatible Commands 19.6 IP Multicast Compatible Commands 19.7 MPLS compatible command 19.8 VPN compatible command

## Basic Configuration Compatible Commands

19.9 WLAN Compatible Commands 19.10 Reliability Compatible Commands 19.11 User Access and Authentication Compatible Commands 19.12 Security Compatible Commands 19.13 QoS Compatible Commands 19.14 Network Management Compatible Commands 19.1.1 set authentication password simple (upgrade-compatible command) 19.1.2 certificate load (upgrade-compatible command) 19.1.3 set device usb-deployment password (upgrade-compatible command) 19.1.4 set save-configuration backup-to-server server (upgrade-compatible command) 19.1.5 set save-configuration (upgrade-compatible command) 19.1.6 snmp-agent trap enable configuration (upgrade-compatible command) 19.1.7 snmp-agent trap enable ssh (upgrade-compatible command) 19.1.8 snmp-agent trap enable system (upgrade-compatible command) 19.1.9 snmp-agent trap enable flash (upgrade-compatible command) 19.1.10 super password (upgrade-compatible command) 19.1.11 trusted-ca load (upgrade-compatible command)

### `set authentication password simple (upgrade- compatible command)`

> **Página:** 2 · **Views (Modo):** User view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The set authentication password simple command sets the simple format for a local authentiction password.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
set authentication password simple password
```

**Parameters:**

- `password` — Specifies a password. — *Valores:* The value is a string of 1 to 16 characters. The password must contain at least two of the following characters: upper-case character, lower- case character, digit, and special character. Special character except the question mark (?) and space.

**Usage Guidelines:**

It is replaced by the set authentication password command. This command is saved in simple text after it is configured, which brings security risks. Saving the command configuration in ciphertext is recommended.

**Task Name and Operations:**

| Task Name | Operations |
| --- | --- |
| telnet-server | write |


### `certificate load (upgrade-compatible command)`

> **Página:** 3 · **Views (Modo):** SSL policy view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The certificate load command loads a digital certificate in the Secure Sockets Layer (SSL) policy view. The undo certificate load command unloads a digital certificate for the SSL policy. By default, no digital certificate is loaded for the SSL policy.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
# Load a PEM digital certificate for the SSL policy.
certificate load pem-cert cert-filename key-pair { dsa | rsa } key-file key-filename auth-code auth-code
# Load a PFX digital certificate for the SSL policy.
certificate load pfx-cert cert-filename key-pair { dsa | rsa } { mac mac-code |
key-file key-filename } auth-code auth-code
# Load a PEM certificate chain for the SSL policy.
certificate load pem-chain cert-filename key-pair { dsa | rsa } key-file key-filename auth-code auth-code
```

**Parameters:**

- `pem-cert` — Loads a PEM digital certificate for the SSL policy. A PEM digital certificate has a file name extension .pem. A PEM digital certificate transfers text data between systems. — *Valores:* -
- `cert-filename` — Specifies the name of a certificate file. The file is in the subdirectory of the system directory security. If the security directory does not exist in the system, create this directory. — *Valores:* The value is a string of 1 to 64 characters. The file name is the same as that of the uploaded file.
- `key-pair` — Specifies the key pair type. — *Valores:* -
- `dsa` — Sets the key pair type to DSA. — *Valores:* -
- `rsa` — Sets the key pair type to RSA. — *Valores:* -
- `key-file key- filename` — Specifies the key pair file. The file is in the subdirectory of the system directory security. If the security directory does not exist in the system, create this directory. — *Valores:* The value is a string of 1 to 64 characters. The file name is the same as that of the uploaded file.
- `auth-code auth-code` — Specifies the authentication code of the key pair file. The authentication code verifies user identity to ensure that only authorized clients access the server. — *Valores:* When the authentication code is in plain text, the value is a string of 1 to 31 case-sensitive characters without any space.
- `pfx-cert` — Loads a PFX digital certificate for the SSL policy. A PFX digital certificate has a file name extension .pfx. A digital certificate can be converted from the PFX format to another format. — *Valores:* -
- `mac mac- code` — Specifies a message authentication code. The message authentication code ensures the packet data reliability and security. — *Valores:* When the authentication code is in plain text, the value is a string of 1 to 31 case-sensitive characters without any space.
- `pem-chain` — Specifies a PEM certificate chain. — *Valores:* -

**Usage Guidelines:**

**Usage Scenario**

SSL security mechanism includes:

- Data transmission security: Uses the symmetric key algorithm to encrypt data.

- Message integrity: uses the multiplexed analog component (MAC) algorithm to ensure message integrity.

- Identity authentication mechanism: authenticates users based on the digital signatures and certificates. The Certificate Authority (CA) issues PEM, ASN1, and PFX digital certificates that provide user identity information. Based on digital certificates, users establish trust relationships with partners who require high security. A digital certificate data includes the applicant information such as the applicant's name, applicant's public key, digital signature of the CA that issues the certificate, and the certificate validity period. A certificate chain can be released when a certificate is sent so that the receiver can have all certificates in the certificate chain.

**Prerequisites**

Before running the certificate load command, you have run the ssl policy command to create the SSL policy in the system view.

**Precautions**

- You can load a certificate or certificate chain for only one SSL policy. Before loading a certificate or certificate chain, you must unload the existing certificate or certificate chain.

- When you configure an SSL policy to load a certificate or certificate chain, ensure that the maximum length of the key pair in the certificate or certificate chain is 2048 bits. If the length of the key pair exceeds 2048 bits, the certificate file or certificate chain file cannot be uploaded to the device.

**Example:**

```text
# Load a PEM digital certificate for the SSL policy.
<HUAWEI> system-view
[HUAWEI] ssl policy ftp_server
[HUAWEI-ssl-policy-ftp_server] certificate load pem-cert servercert.pem key-pair dsa key-file
serverkey.pem auth-code 123456
# Load a PFX digital certificate for the SSL policy.
<HUAWEI> system-view
[HUAWEI] ssl policy http_server
[HUAWEI-ssl-policy-http_server] certificate load pfx-cert servercert.pfx key-pair dsa key-file
serverkey.pfx auth-code %$%$"DlqKik*GE*~`u4H+LFJ(K-=%$%$
# Load a PEM certificate chain for the SSL policy.
<HUAWEI> system-view
[HUAWEI] ssl policy http_server
[HUAWEI-ssl-policy-http_server] certificate load pem-chain chain-servercert.pem key-pair dsa key-file
chain-servercertkey.pem auth-code 123456
```


### `set device usb-deployment password (upgrade- compatible command)`

> **Página:** 6 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The set device usb-deployment password command sets an authentication password for USB-based deployment.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
set device usb-deployment password password
```

**Parameters:**

- `password` — Specifies the authentication password for USB-based deployment. — *Valores:* -

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. A user with a level lower than the management level cannot query the password configured using this command. If this user query the configuration file, the password is displayed as asterisks (******).


### `set save-configuration backup-to-server server (upgrade-compatible command)`

> **Página:** 7 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The set save-configuration backup-to-server server command specifies the server where the system periodically saves the configuration file. The undo set save-configuration backup-to-server server command cancels the server where the system periodically saves the configuration file. By default, the system does not periodically save configurations to the server.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
set save-configuration backup-to-server server server-ip [ transport-type { ftp |
sftp } ] path path user user-name password password
set save-configuration backup-to-server server server-ip user user-name
password password [ path path ]
undo set save-configuration backup-to-server server [ server-ip ]
```

**Parameters:**

- `server server-ip` — Specifies the IP address of the server where the system periodically saves the configuration file. — *Valores:* -
- `transport-type` — Specifies the mode in which the configuration file is transmitted to the server. — *Valores:* The value can be ftp or sftp.
- `user user-name` — Specifies the name of the user who saves the configuration file on the server. — *Valores:* The value is a string of 1 to 64 case-sensitive characters without spaces.
- `password password` — Specifies the password of the user who saves the configuration file on the server. — *Valores:* The value is a string of 1 to 16 or 32 case-sensitive characters without spaces.
- `path path` — Specifies the relative save path on the server. — *Valores:* The value is a string of 1 to 64 case-sensitive characters without spaces.

**Usage Guidelines:**

**Usage Scenario**

Run this command to periodically save the configuration file to the server.

**Precautions**

If the mode in which the configuration file is transmitted to the server is not specified, FTP is used. If the specified path on the server does not exist, configuration files cannot be sent to the server. The system then sends an alarm message indicating the transmission failure to the NMS, and the transmission failure is recorded as a log message on the device. The user name and password must be the same as those used in FTP or SFTP login mode.

**Example:**

```text
# Specify the server to which the system periodically sends the configuration file,
```

and set the transmission mode to FTP.

```text
<HUAWEI> system-view
[HUAWEI] set save-configuration backup-to-server server 10.1.1.1 transport-type ftp path d:/ftp user
huawei password huawei@1234
```


### `set save-configuration (upgrade-compatible command)`

> **Página:** 8 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** Using the set save-configuration command, you can enable automatic saving of configurations. Using the undo set save-configuration command, you can disable automatic saving of configurations. By default, automatic saving of configurations is not enabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
set save-configuration nochange-time nochange-time
undo set save-configuration nochange-time [ nochange-time ]
```

**Parameters:**

- `nochange-time nochange-time` — Specifies a period and configures the system to automatically save configurations if no configurations are changed over the specified period. — *Valores:* The value is an integer ranging from 30 to 43200, in minutes. The default value is 30.

**Usage Guidelines:**

If nochange-time nochange-time is specified in the command, the system automatically saves configurations if no configuration changes in the period specified by nochange-time. If the interval from the time of the last configuration to the current time is shorter than the set interval, the system cancels the current automatic saving operation.

**Example:**

```text
# Configure the system to automatically save configurations at 60-minute
```

intervals if no configuration changes in the period.

```text
<HUAWEI> system-view
[HUAWEI] set save-configuration nochange-time 60
```


### `snmp-agent trap enable configuration (upgrade- compatible command)`

> **Página:** 9 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable configuration command enables the trap function of the Configuration module. By default, the trap function of the Configuration module is disabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable configuration
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After the upgrade, this command is no longer supported, and it is replaced by the snmp-agent trap enable feature-name configuration command.


### `snmp-agent trap enable ssh (upgrade-compatible command)`

> **Página:** 10 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable ssh command enables the trap function of the SSH module. By default, the alarm function of the SSH module is disabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable ssh
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade.


### `snmp-agent trap enable system (upgrade-compatible command)`

> **Página:** 11 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable system command enables the trap function of the system module. By default, the trap function of the system module is enabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable system
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After the upgrade, this command is no longer supported, and it is replaced by the snmp-agent trap enable feature-name system command.


### `snmp-agent trap enable flash (upgrade-compatible command)`

> **Página:** 11 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable flash command enables the trap function of the flash module. By default, the trap function of the flash module is disabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable flash
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After the upgrade, this command is no longer supported, and it is replaced by the snmp-agent trap enable feature-name vfs { hwflhopernotification | hwflhsyncfailnotification | hwflhsyncsuccessnotification } command.


### `super password (upgrade-compatible command)`

> **Página:** 12 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The super password command sets the password used to change a user from a lower level to a higher level. The undo super password command cancels the current configuration. By default, the system does not set the password used to change a user from a lower level to a higher level.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
super password [ level user-level ] simple simple-password
```

**Parameters:**

- `level user-level` — Specifies a user level. — *Valores:* The value is an integer that ranges from 1 to 15. By default, the system sets passwords for users of level 3.
- `simple simple- password` — Specifies the simple password for changing a user level. — *Valores:* The value is a string of 1 to 16 case- sensitive characters.

**Usage Guidelines:**

**Usage Scenario**

The device makes it possible to switch a user from a lower level to a higher level. To prevent illegal intrusion of unauthorized users, when a user switches to a higher user level, the system authenticates the user identity by requiring the user to input the password for the higher user level.

- If the cipher cipher-password parameter is not specified, the system starts the interactive password setting mode. Enter a plain text password of 6 to 16 characters. The requirements for the password are the same as the requirements for the plain text password configured when the cipher keyword is specified. The password you enter will not be displayed on the device. You can press CTRL_C to cancel the password setting.

- The password is in plain or cipher text and displayed on the device when the cipher cipher-password parameter is specified. When you run the super command to switch the user level, the password must be entered in plain text.

- Whether the password is entered in cipher or interactive mode, the password is saved in cipher text to the configuration file. Therefore, the password cannot be obtained from the system after it is set. Keep the password secure.

- This command is saved in simple text after it is configured, which brings security risks. Saving the command configuration in ciphertext is recommended.

**Example:**

```text
# Set the password used when low-level users switch to level 10 to huawei2012.
<HUAWEI> system-view
[HUAWEI] super password level 10 simple huawei2012
```


### `trusted-ca load (upgrade-compatible command)`

> **Página:** 13 · **Views (Modo):** SSL policy view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The trusted-ca load command loads the trusted CA file for the SSL policy for the FTP client. The undo trusted-ca load command unloads the trusted CA file of the SSL policy. By default, no trusted CA file is loaded for the SSL policy.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
# Load the trusted CA file for the SSL policy in PFX format.
trusted-ca load pfx-ca ca-filename auth-code { auth-code | cipher auth-code }
```

**Parameters:**

- `pfx-ca` — Load the trusted CA file for the SSL policy in PFX format. — *Valores:* -
- `ca-filename` — Specifies the name of the trusted CA file. The file is in the subdirectory of the system directory security. If the security directory does not exist in the system, create this directory. — *Valores:* The value is a string of 1 to 64 characters. The file name is the same as that of the uploaded file.
- `auth-code auth-code` — Specifies the verification code for the trusted CA file in PFX format. The authentication code verifies user identity to ensure that only authorized users can log in to the server. — *Valores:* When the authentication code is in plain text, the value is a string of 1 to 31 case-sensitive characters without any space.

**Usage Guidelines:**

**Usage Scenario**

CAs that are widely trusted in the world are called root CAs. Root CAs can authorize other lower-level CAs. The identity information about a CA is provided in the file of a trusted CA. To ensure the communication security and verify the server validity, you must run the trusted-ca load command to load the trusted CA file.

**Prerequisites**

Before running the trusted-ca load command, you have run the ssl policy command to create the SSL policy in the system view.

**Precautions**

A maximum of four trusted CA files can be loaded for an SSL policy.

**Example:**

```text
# Load the trusted CA file for the SSL policy in PFX format.
<HUAWEI> system-view
[HUAWEI] ssl policy ftp_server
[HUAWEI-ssl-policy-ftp_server] trusted-ca load pfx-ca servercert.pfx auth-code cipher 123456
```


## Device Management Compatible Commands

19.2.1 cpu-usage threshold (upgrade-compatible command) 19.2.2 display autosave config (upgrade-compatible command) 19.2.3 display fault-management (upgrade-compatible command) 19.2.4 display fault-management alarm information (upgrade-compatible command) 19.2.5 dual-active detect mode direct (upgrade-compatible command) 19.2.6 dual-active detect mode relay (upgrade-compatible command) 19.2.7 dual-active exclude (upgrade-compatible command) 19.2.8 dual-active relay (upgrade-compatible command) 19.2.9 dual-active restore (upgrade-compatible command) 19.2.10 fault-management alarm (upgrade-compatible command) 19.2.11 poe af-inrush enable (upgrade-compatible command) 19.2.12 reset fault-management (upgrade-compatible command) 19.2.13 ntp-service authentication-keyid (upgrade-compatible command)

### `cpu-usage threshold (upgrade-compatible command)`

> **Página:** 15 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The cpu-usage threshold command sets the upper and lower CPU usage alarm thresholds.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
cpu-usage threshold [ unit unit-id ] { high | low } threshold-value
```

**Parameters:**

- `high` — Specifies the upper CPU usage alarm threshold. — *Valores:* -
- `low` — Specifies the lower CPU usage alarm threshold. — *Valores:* -
- `unit unit-id` — ● Specifies the slot ID if stacking is not configured. ● Specifies the stack ID if stacking is configured. — *Valores:* The value range depends on the device configuration.
- `threshold- value` — Specifies the alarm threshold of CPU usage. — *Valores:* ● The value is an integer that ranges from 2 to 100 when specifies the upper CPU usage alarm threshold. ● The value is an integer that ranges from 1 to 99 when specifies the lower CPU usage alarm threshold.

**Usage Guidelines:**

When the CPU usage is not within the allowed range, a log is recorded. You can conveniently know CPU usage through log information.


### `display autosave config (upgrade-compatible command)`

> **Página:** 16 · **Views (Modo):** All views · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** sim

**Description (Function):** The display autosave config command displays the configuration about the autosave function, including the status of the autosave function, time for autosave check, threshold of the CPU usage, and interval during which configurations are not changed.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display autosave config
```

**Usage Guidelines:**

After the autosave function is configured, you can run the display autosave config command to check whether the configured parameters are correct. You can also run this command to check whether the parameters about the autosave function are properly configured when autosave cannot function normally. If not, run the set save-configuration command to adjust the parameters to restore the normal state of the autosave function.

**Example:**

```text
# Display the configuration about the autosave function.
<HUAWEI> display autosave config
Auto save function status: enable
Auto save checking interval: 60 minutes
The threshold of the CPU usage: 50%
The interval of the configuration not changing: 30 minutes
```

Table 19-1 Description of the display autosave config command output

| Item | Description |
| --- | --- |
| Auto save function status | Indicates the status of the autosave function: ● Enable ● Disable |
| Auto save checking interval | Indicates the time for autosave check. |
| The threshold of the CPU usage | Indicates the threshold of the CPU usage during the autosave operation. |
| The interval of the configuration not changing | Indicates the interval during which system configurations are not changed. |


### `display fault-management (upgrade-compatible command)`

> **Página:** 17 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display fault-management command displays the contents of an alarm message, active alarm message, or event.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display fault-management { alarm | active-alarm | event } [ sequence-number
sequence-number ]
```

**Parameters:**

- `alarm` — Displays information about alarms. — *Valores:* -
- `active-alarm` — Displays information about active alarms. — *Valores:* -
- `event` — Displays information about events. — *Valores:* -
- `sequence- number sequence-number` — Specifies the number of an alarm message, active alarm message, or event. — *Valores:* The value is an integer ranging from 0 to 2147483647. When the value is 0, information about all alarm messages, active messages, or events is displayed.

**Usage Guidelines:**

This command helps you obtain the contents of all alarm messages or one alarm message on a device.

**Example:**

```text
# Display the contents of active alarm messages in the system.
<HUAWEI> display fault-management active-alarm
A/B/C/D/E/F/G/H/I/J
A=Sequence, B=RootKindFlag(Independent|RootCause|nonRootCause)
C=Generating time, D=Clearing time
E=ID, F=Name, G=Level, H=State
I=Description information for locating(Para info, Reason info)
J=RootCause alarm sequence(Only for nonRootCause alarm)
1/Independent/2008-10-13 01:49:45+08:00/-/0x41932001/hwLldpEnabled/Warning/Sta
rt/OID: 1.3.6.1.4.1.2011.5.25.134.2.1 Global LLDP is enabled.
2/Independent/2008-10-13 01:50:06+08:00/-/0x41932000/lldpRemTablesChange/Warni
ng/Start/OID: 1.0.8802.1.1.2.0.0.1 Neighbor information is changed. (LldpStatsRe
mTablesInserts=1, LldpStatsRemTablesDeletes=0, LldpStatsRemTablesDrops=0, LldpSt
atsRemTablesAgeouts=0)
5/Independent/2008-10-13 02:22:52+08:00/-/0x40c12014/hwPortPhysicalEthHalfDupl
exAlarm/Minor/Start/OID 1.3.6.1.4.1.2011.5.25.129.2.5.11 The port works in half
duplex mode. (EntityPhysicalIndex=10, BaseTrapSeverity=3, BaseTrapProbableCause=
1024, BaseTrapEventType=8, EntPhysicalName=GigabitEthernet0/0/5, RelativeResourc
e=interface GigabitEthernet0/0/5)
```


### `display fault-management alarm information (upgrade-compatible command)`

> **Página:** 19 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display fault-management alarm information command displays registration information about an alarm message.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display fault-management alarm information [ alarm-name ]
```

**Parameters:**

- `alarm-name` — Specifies the name of an alarm message. — *Valores:* The value is a case-sensitive string of 1 to 256 characters without spaces.

**Usage Guidelines:**

None

**Example:**

```text
# Check registration information about the alarm message named linkUp.
<HUAWEI> display fault-management alarm information linkUp
**********************************
AlarmName: linkUp
AlarmType: Resume Alarm
AlarmLevel: Cleared
Suppress Period: NA
CauseAlarmName: linkDown
Match VB Name: ifIndex
**********************************
```

Table 19-2 Description of the display fault-management alarm information command output

| Item | Description |
| --- | --- |
| AlarmName | Name of an alarm message |
| AlarmType | Type of an alarm |

| Item | Description |
| --- | --- |
| AlarmLevel | Level of an alarm |
| Suppress Period | Suppress period of an alarm |
| CauseAlarmNam e | Name of the corresponding root alarm |
| Match VB Name | Contents of the matching rule set for the alarm messages |


### `dual-active detect mode direct (upgrade-compatible command)`

> **Página:** 20 · **Views (Modo):** GE interface view, XGE interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The dual-active detect mode direct command enables DAD in direct mode on a specified interface. By default, DAD is disabled on an interface in a stack.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
dual-active detect mode direct
```

**Usage Guidelines:**

**Usage Scenario**

DAD in direct mode applies to a stack containing two DAD-supporting member switches.

**Prerequisites**

The stack containing two member switches is running properly, and DAD in relay mode is not configured for the stack.

**Precautions**

Disabling DAD in direct mode on an interface restores the forwarding function on the interface. If a loop exists on the network, a broadcast store occurs. It is replaced by the mad detect mode direct command.

**Example:**

```text
# Configure DAD in direct mode on GigabitEthernet1/0/1.
<HUAWEI> system-view
[HUAWEI] interface gigabitethernet 1/0/1
[HUAWEI-GigabitEthernet1/0/1] dual-active detect mode direct
Warning: This command will block the port, and no other configuration running on this port is
recommended. Continue?[Y/N]:y
```


### `dual-active detect mode relay (upgrade-compatible command)`

> **Página:** 21 · **Views (Modo):** Eth-Trunk interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The dual-active detect mode relay command enables DAD in relay mode on a specified interface. By default, DAD is disabled on an interface in a stack.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
dual-active detect mode relay
```

**Usage Guidelines:**

**Usage Scenario**

You can configure DAD in relay mode only when a stack containing two member switches is configured with an inter-chassis Eth-Trunk and a proxy device supports the relay function.

**Prerequisites**

The stack containing two member switches is running properly, and DAD in direct mode is not configured for the stack.

**Precautions**

It is replaced by the mad detect mode relay command.

**Example:**

```text
# Configure DAD in relay mode on Eth-Trunk 10.
<HUAWEI> system-view
[HUAWEI] interface eth-trunk 10
[HUAWEI-Eth-Trunk10] dual-active detect mode relay
```


### `dual-active exclude (upgrade-compatible command)`

> **Página:** 22 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The dual-active exclude command excludes specified interfaces of a stack from shutdown. By default, only physical member ports are excluded from shutdown.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
dual-active exclude interface { interface-type interface-number1 [ to interface-type interface-number2 ] } &<1-10>
```

**Parameters:**

- `interface { interface- type interface- number1 [ to interface-type interface-number2 ] }` — Specifies the type and number of an interface: ● interface-type specifies the type of the interface. ● interface-number1 specifies the number of the first interface. ● interface-number2 specifies the number of the second interface. — *Valores:* The value of interface-number2 must be larger than that of interface-number1.

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can be run when it is entered in full. After the upgrade, it is replaced by the mad exclude command.


### `dual-active relay (upgrade-compatible command)`

> **Página:** 23 · **Views (Modo):** Eth-Trunk interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The dual-active relay command enables the relay function on a specified interface of a proxy device. By default, the relay function is disabled on an interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
dual-active relay
```

**Usage Guidelines:**

In DAD in relay mode, you need to use the dual-active relay command to configure the relay function on a specified Eth-Trunk interface of a proxy device. Member interfaces of the Eth-Trunk interface forward DAD packets to each other so that member switches can exchange DAD packets. It is replaced by the mad relay command.

**Example:**

```text
# Enable the relay function on Eth-Trunk 10 of a proxy device.
<HUAWEI> system-view
[HUAWEI] interface eth-trunk 10
[HUAWEI-Eth-Trunk10] dual-active relay
```


### `dual-active restore (upgrade-compatible command)`

> **Página:** 23 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The dual-active restore command restores the blocked interfaces of the standby switch that enters the Recovery state after its stack splits.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
dual-active restore
```

**Usage Guidelines:**

**Usage Scenario**

After a stack splits, if the active switch fails, you can restore the blocked interfaces of the standby switch that enters the Recovery state to make the standby switch to take over the active role.

**Precautions**

When the active switch is working properly, do not use this command. Otherwise, DAD detects a dual-active scenario again and blocks all service interfaces, causing interface status flapping. It is replaced by the mad restore command.

**Example:**

```text
# Restore all the blocked interfaces of the standby switch that enters the Recovery
```

state after its stack splits.

```text
<HUAWEI> system-view
[HUAWEI] dual-active restore
```


### `fault-management alarm (upgrade-compatible command)`

> **Página:** 24 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The fault-management alarm command configures the type or level of an alarm message or event. The undo fault-management alarm command cancels the type or level of an alarm message or event.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
fault-management alarm alarm-name level alarm-level
undo fault-management alarm alarm-name [ level ]
```

**Parameters:**

- `alarm alarm-name` — Specifies the name of an alarm message or event. — *Valores:* The value is a case- sensitive string of 1 to 64 characters without spaces.
- `level alarm- level` — Specifies the level of an alarm message or event. Mappings between alarm levels and severity levels: 1. Critical: Indicates that a service affecting condition has occurred and an immediate corrective action is required. Such a severity can be reported. For example, when a managed object becomes totally out of service, its capability must be restored. 2. Major: Indicates that a service affecting condition has developed and an urgent corrective action is required. Such a severity can be reported. For example, when there is a severe degradation in the capability of a managed object, its full capability must be restored. 3. Minor: Indicates the existence of a non- service affecting fault condition and that corrective action should be taken in order to prevent a more serious (for example, service affecting) fault. Such a severity can be reported. For example, when the detected alarm condition is not currently degrading the capacity of the managed object. 4. Warning: Indicates the detection of a potential or impending service affecting fault, before any significant effects have been felt. Action should be taken to further diagnose (if necessary) and correct the problem in order to prevent it from becoming a more serious service affecting fault. 5. Indeterminate: Indicates that the severity level cannot be determined. 6. Cleared: Indicates the clearing of one or more previously reported alarms. This alarm clears all alarms for this managed object that have the same Alarm type, Probable cause and Specific problems (if given). Multiple associated notifications may be cleared by using the Correlated notifications parameter. — *Valores:* The value is a character string. In the X.733 standard, according to the severity level and emergency level, alarm messages are classified into six levels. The more serious event an alarm message indicates, the smaller alarm-level is. Critical indicates the alarm severity 1; whereas Cleared indicates the alarm severity 6.

**Usage Guidelines:**

Alarm messages can be classified into root alarm messages and resume-alarm messages. All the alarms are saved on the device. Events can be classified into critical events and events. Critical events are saved on a device and can be obtained by the NMS. Events are not saved on a device. The fault-management alarm command can be used to promote or degrade the level of an alarm message according to the severity level and emergency level of the alarm message.

**Example:**

```text
# Set the alarm severity of the alarm message named hwCfgManEventlog to
```

major respectively.

```text
<HUAWEI> system-view
[HUAWEI] fault-management alarm hwCfgManEventlog level major
```


### `poe af-inrush enable (upgrade-compatible command)`

> **Página:** 27 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The poe af-inrush enable command changes the power supply standards of interfaces from 802.3at to 802.3af. The undo poe af-inrush enable command restores the power supply standards of interfaces to 802.3at. By default, interfaces comply with 802.3at.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
poe af-inrush enable [ slot slot-id ]
undo poe af-inrush enable [ slot slot-id ]
```

**Parameters:**

- `slot slot-id` — Specifies the stack ID. — *Valores:* The value is 0 if stacking is not configured. The value ranges from 0 to 8 if stacking is configured.

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After the upgrade, it is replaced by the poe af-inrush enable command in the interface view.


### `reset fault-management (upgrade-compatible command)`

> **Página:** 28 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The reset fault-management command clears all alarm messages.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
reset fault-management { active-alarm | event } [ sequence-number sequence-number ]
```

**Parameters:**

- `active-alarm` — Clears information about active alarms. — *Valores:* -
- `event` — Clears event information. — *Valores:* -
- `sequence-number sequence-number` — Specifies the number of an alarm message. — *Valores:* The value is an integer ranging from 0 to 2147483647. If the value is 0, it indicates that all alarm messages are cleared.

**Usage Guidelines:**

If sequence-number is not specified, the system clears all the alarm messages on the device. NO TICE After this command is run, all alarm messages on a device are cleared and cannot be restored.

**Example:**

```text
# Clear all active alarm messages.
<HUAWEI> system-view
[HUAWEI] reset fault-management active-alarm
```


### `ntp-service authentication-keyid (upgrade-compatible command)`

> **Página:** 29 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Management level · **Leitura (display/show):** não

**Description (Function):** The ntp-service authentication-keyid command sets NTP authentication key. The undo ntp-service authentication-keyid command removes NTP authentication key. By default, no authentication key is set.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
ntp-service authentication-keyid key-id authentication-mode { md5 | hmac-sha256 } plain password-plain
undo ntp-service authentication-keyid key-id
```

**Parameters:**

- `key-id` — Indicates the key number. — *Valores:* Key ID is an integer and ranges from 1 to 4294967295.
- `authentication- mode md5` — Indicates MD5 authentication mode. — *Valores:* -
- `authentication- mode hmac-sha256` — Indicates HMAC-SHA256 authentication mode. — *Valores:* -
- `plain password-plain` — Indicates that the configured password is displayed in plain text, and specifies the password. NOTICE If plain is selected, the password is saved in the configuration file in plain text. This brings security risks. — *Valores:* The password is a string of 1 to 255 case- sensitive characters without spaces.

**Usage Guidelines:**

**Usage Scenario**

On a network that requires high security, the NTP authentication must be enabled. You can configure password authentication between client and server, which guarantee the client only to synchronize with server successfully authenticated, and improve network security. If the NTP authentication function is enabled, a reliable key should be configured at the same time. Keys configured on the client and the server must be identical. NOTE In NTP symmetric peer mode, the symmetric active peer functions as a client and the symmetric passive peer functions as a server.

**Follow-up Procedure**

You can configure multiple keys for each device. After the NTP authentication key is configured, you need to set the key to reliable using the ntp-service reliable authentication-keyid command. If you do not set the key to reliable, the NTP key does not take effect.

**Precautions**

To ensure security, you are advised to use the HMAC-SHA256 algorithm, which is more secure, for NTP authentication. You can configure a maximum of 1024 keys for each device. If the NTP authentication key is a reliable key, it automatically becomes unreliable when you delete the key. You do not need to run the undo ntp-service reliable authentication-keyid command.

**Example:**

```text
# Set authentication text to abc in HMAC-SHA256 authentication with plain
```

option.

```text
<HUAWEI> system-view
[HUAWEI] ntp-service authentication-keyid 10 authentication-mode hmac-sha256 plain abc
```


## Interface Management Compatible Commands

19.3.1 Ethernet Interface Compatible Commands

### `Ethernet Interface Compatible Commands`

> **Página:** 31 · **Views (Modo):** System review · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable port command enables the system to generate an alarm when the inbound or outbound bandwidth usage on all Ethernet subinterfaces exceeds the threshold.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable port { input-rate | output-rate }
```

**Parameters:**

- `input-rate` — Enables the system to generate an alarm when the inbound bandwidth usage on all Ethernet sub-interfaces exceeds the threshold. — *Valores:* -
- `output-rate` — Enable the system to generate an alarm when the outbound bandwidth usage on all Ethernet sub-interfaces exceeds the threshold. — *Valores:* -

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. If the threshold for the inbound or outbound bandwidth usage has been configured on an Ethernet sub-interface, you can enable the system to generate an alarm when the threshold is exceeded. This allows you to determine whether the device is functioning normally. After the configuration is complete, the system generates an alarm when the bandwidth usage exceeds or falls below the threshold.

**Example:**

None


## Ethernet Switching Compatible Commands

19.4.1 MAC Compatible Commands 19.4.2 Link Aggregation Compatible Commands 19.4.3 VLAN Compatible Commands 19.4.4 Voice VLAN Compatible Commands 19.4.5 GVRP Compatible Commands 19.4.6 STP Compatible Commands 19.4.7 L2PT Compatible Commands

### `MAC Compatible Commands`

> **Página:** 35 · **Views (Modo):** Ethernet interface view, GE interface view, XGE interface view, Eth-Trunk interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The port-security maximum command sets the maximum number of MAC addresses that can be learned on an interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
port-security maximum max-number
```

**Parameters:**

- `max-number` — Specifies the maximum number of MAC addresses that can be learned by an interface. — *Valores:* The value is an integer that ranges from 1 to 4096.

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can be run when it is entered in full. After the upgrade, it is replaced by the port-security max-mac-num command.


### `Link Aggregation Compatible Commands`

> **Página:** 38 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** Using the ssnmp-agent trap enable eth-trunk command, you can enable the Simple Network Management Protocol (SNMP) trap function on an Eth-Trunk. Using the undo snmp-agent trap enable eth-trunk command, you can disable the SNMP trap function on an Eth-Trunk. By default, the SNMP trap function is disabled on an Eth-Trunk.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable eth-trunk
undo snmp-agent trap enable eth-trunk
```

**Usage Guidelines:**

If the SNMP trap function is enabled on an Eth-Trunk, the system sends a trap to the network management system (NMS) server in case of when the following exceptions occurs:

- The negotiation of the LAG fails.

- The bandwidth of the LAG is lost. For example, if the lower threshold of the number of active interfaces is set by using the least active-linknumber command and if the number of active interfaces is smaller than this value, the Eth-Trunk becomes Down and the system sends the trap.

- Part of the bandwidth of the LAG is lost. When one of active interfaces fails, the system sends the trap because the number of active interfaces is reduced.

**Example:**

```text
# Enable the SNMP trap function on an Eth-Trunk so that the trap can be sent to
```

the NMS server promptly when the status of the LAG changes.

```text
<HUAWEI> system-view
[HUAWEI] snmp-agent trap enable eth-trunk
```


### `VLAN Compatible Commands`

> **Página:** 41 · **Views (Modo):** GE interface view, XGE interface view, Eth-Trunk interface view, port group view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The port mux-vlan enable command enables the MUX VLAN function on an interface. The undo port mux-vlan enable command disables the MUX VLAN function on an interface. By default, the MUX VLAN function is disabled on an interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
port mux-vlan enable
undo port mux-vlan enable
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can be run when it is entered in full. After the upgrade, it is replaced by the port mux-vlan enable vlan command.


### `Voice VLAN Compatible Commands`

> **Página:** 42 · **Views (Modo):** GE interface view, Ethernet interface view, XGE interface view, Eth-Trunk interface view, port group view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The voice-vlan enable command enables the voice VLAN function on an interface. By default, the voice VLAN function is disabled on an interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
voice-vlan enable
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can be run when it is entered in full. After the upgrade, it is replaced by the voice-vlan vlan-id enable command.


### `GVRP Compatible Commands`

> **Página:** 43 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The garp leaveall timer command sets the GARP LeaveAll timer.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
garp leaveall timer timer-value
```

**Parameters:**

- `timer-value` — Specifies the value of the GARP LeaveAll timer. — *Valores:* The value is an integer that ranges from 65 to 32765 and that can be exactly divided by 5, in centiseconds. The value of the LeaveAll timer must be greater than the values of Leave timers on all the interfaces.

**Usage Guidelines:**

**Usage Scenario**

When a GARP participant is enabled, the LeaveAll timer is started. When the LeaveAll timer expires, the GARP participant sends LeaveAll messages to request other GARP participants to re-register all its attributes. Then the LeaveAll timer restarts. Devices on a network may have different settings for the LeaveAll timer. In this case, all the devices use the smallest LeaveAll timer value on the network. When the LeaveAll timer of a device expires, the device sends LeaveAll messages to other devices. After other devices receive the LeaveAll messages, they reset their LeaveAll timers. Therefore, only the LeaveAll timer with the smallest value takes effect even if devices have different settings for the LeaveAll timer.

**Prerequisites**

Before setting GARP timers on an interface, you must enable GVRP globally.

**Precautions**

The Leave timer length on an interface is restricted by the global LeaveAll timer length. When configuring the global LeaveAll timer, ensure that all the interfaces that have a GARP Leave timer configured are working properly.

**Example:**

```text
# Set the LeaveAll timer to 510 centiseconds.
<HUAWEI> system-view
[HUAWEI] garp leaveall timer 510
```


### `STP Compatible Commands`

> **Página:** 44 · **Views (Modo):** System view or MST process region view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The stp tc-protection command enables the trap function for the Topology Change (TC) BPDU protection. The undo stp tc-protection command disables the trap function for the TC BPDU protection. By default, the trap function for the TC BPDU protection is disabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
stp tc-protection
undo stp tc-protection
```

**Usage Guidelines:**

**Usage Scenario**

The TC attack defense function is enabled by default, you can run the stp tc-protection interval command to set the time that a device needs to process the maximum number of TC BPDUs which is configured using the stp tc-protection threshold command. If there are packets exceeding the maximum number, the switch processes the packets after the time specified in the stp tc-protection interval command expires. For example, if the time is set to 10 seconds and the maximum number is set to 5, when a switch receives TC BPDUs, the switch processes only the first 5 TC BPDUs within 10 seconds and processes the other TC BPDUs after the time expires. In this way, the device does not frequently update its MAC address entries and ARP entries, reducing CPU usage. To learn about detailed processing information on TC BPDUs, run the stp tc-protection command to enable the trap function for the TC BPDU protection. After the function is enabled, MSTP_1.3.6.1.4.1.2011.5.25.42.4.2.15 hwMstpiTcGuarded and MSTP_1.3.6.1.4.1.2011.5.25.42.4.2.16 hwMstpProTcGuarded are generated.

**Precautions**

The trap function for the TC BPDU protection takes effect only when the snmp-agent trap enable feature-name mstp and stp tc-protection are both run.


### `L2PT Compatible Commands`

> **Página:** 47 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The l2protocol-tunnel user-defined-protocol command defines the characteristics of a Layer 2 protocol whose packets are transparently transmitted, including the protocol name, Ethernet encapsulation type, destination MAC address of packets, multicast MAC address replacing the destination multicast MAC address of packets, and priority of packets. By default, there is no user-defined characteristics of a Layer 2 protocol whose packets are transparently transmitted.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
l2protocol-tunnel user-defined-protocol protocol-name protocol-mac protocol-mac encape-type { ethernetii protocol-type protocol-type | llc dsap dsap-value
ssap ssap-value | snap protocol-type protocol-type } group-mac { group-mac |
default-group-mac } [ priority priority-id ]
```

**Parameters:**

- `protocol- name` — Specifies the name of a user-defined Layer 2 protocol whose packets are transparently transmitted. — *Valores:* The name is a string of 1 to 31 case- insensitive characters without spaces. When quotation marks are used around the string, spaces are allowed in the string.
- `protocol-mac protocol-mac` — Specifies the destination multicast MAC address of the Layer 2 protocol packets that are transparently transmitted. This MAC address must be an ordinary MAC address that has not been used on the S1720, S2700, S5700, and S6720. — *Valores:* The address is in the format of H-H-H, H indicating a 4-bit hexadecimal number.
- `encape-type` — Defines the encapsulation format for Layer 2 protocol packets that are transparently transmitted. ● ethernetii: indicates Ethernet_II, the encapsulation format for Layer 2 protocol packets that are transparently transmitted. ● llc:: indicates Logical Link Control (LLC), the encapsulation format for Layer 2 protocol packets that are transparently transmitted. ● snap: indicates Sub-Network Access Protocol (SNAP), the encapsulation format for Layer 2 protocol packets that are transparently transmitted. When transparently-transmitted Layer 2 protocol packets carry the same protocol MAC address and protocol type, you can use the parameter encap-type to define different encapsulation formats to differentiate these packets. — *Valores:* -
- `protocol- type protocol-type` — Specifies the value of Ethernet encapsulation type. — *Valores:* The value is a hexadecimal number ranging from 0600 to FFFF.
- `dsap dsap- value` — Specifies the destination service access point. — *Valores:* The value ranges from 0x00 to 0xff, in hexadecimal format.
- `ssap ssap- value` — Specifies the source service access point. — *Valores:* The value ranges from 0x00 to 0xff, in hexadecimal format.
- `group-mac group-mac` — Specifies the multicast MAC address that replaces the destination multicast MAC address of the Layer 2 protocol packets that are transparently transmitted. The address must be an ordinary MAC address, which cannot be the MAC address of bridge protocol data units (BPDUs), the MAC address of Smart Link protocol packets, or a special MAC address. — *Valores:* The address is in the format of H-H-H, H indicating a 4-bit hexadecimal number.
- `default- group-mac` — Specifies the default MAC address of a multicast group, which is 0100-0ccd-cdd0. This parameter can simplify the configuration and reduce the configuration error. For example: Most Layer 2 protocols can be classified by types. Default MAC addresses of Layer 2 protocols in the same type are the same. In this case, you can attach the parameter default-group-mac to the l2protocol- tunnel user-defined-protocol command to reduce the configuration workload and the probability of configuration error. — *Valores:* -
- `priority priority-id` — Specifies the priority of the Layer 2 protocol packets that are transparently transmitted. — *Valores:* The value is an integer that ranges from 1 to 7. The default value is 0.

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can be run when it is entered in full. After the upgrade, it is replaced by the l2protocol-tunnel user-defined-protocol command.


## IP Service Compatible Commands

19.5.1 ARP Compatible Commands 19.5.2 DHCP Upgrade-compatible Commands

### `ARP Compatible Commands`

> **Página:** 55 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The arp learning ip-network-cross enable command enables inter-network segment ARP learning on interfaces.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
arp learning ip-network-cross enable
```

**Usage Guidelines:**

**Usage Scenario**

In V200R010C00 and later versions, inter-network segment ARP learning is disabled on interfaces by default. If the system software of a switch is upgraded from V200R005C00 or a later version to V200R010C00SPC600 or a later version, inter-network segment ARP learning is enabled on interfaces. If you run the display this include-default command in the system view after the configuration is restored, the command output includes arp learning ip-network-cross enable.

**Precautions**

This command can be used only in the configuration restoration stage. After the configuration is restored, you cannot configure this command manually.


### `DHCP Upgrade-compatible Commands`

> **Página:** 56 · **Views (Modo):** Interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The dhcpv6 relay destination command enables the DHCPv6 relay function on interfaces and configures the IPv6 address of the DHCPv6 server or next-hop relay agent. By default, the DHCPv6 relay function is disabled on an interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
dhcpv6 relay destination ipv6-address interface interface-type interface-number
```

**Parameters:**

- `ipv6-address` — Specifies the destination address of relay messages, which can be the IPv6 address of the DHCPv6 server or next hop relay agent. — *Valores:* The value is a 32-digit hexadecimal number, in the format X:X:X:X:X:X:X:X.
- `interface interface-type interface-number` — Specifies the type and number of the outbound interface of relay messages. — *Valores:* -

**Usage Guidelines:**

When a client applies to a DHCPv6 server on a different network segment for an IPv6 address, you need to deploy a relay agent between the client and the DHCPv6 server. In this manner, the relay agent transmits DHCPv6 messages exchanged between the client and the DHCPv6 server.

**Example:**

```text
# Bind a MAC address 2020-e2f3-2a3b to the global IP address pool global1.
<HUAWEI> system-view
[HUAWEI] ip pool global1
[HUAWEI-ip-pool-global1] static-bind mac-address 2020-e2f3-2a3b
```

19.5.2.10 dhcpv6 relay destination (upgrade-compatible command)


## IP Multicast Compatible Commands

19.6.1 MLD Snooping Compatible Commands

### `MLD Snooping Compatible Commands`

> **Página:** 69 · **Views (Modo):** VLAN view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The mld-snooping group-policy command configures an IPv6 multicast group policy in a VLAN.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
mld-snooping group-policy acl6-number mld-version [ default-permit ]
```

**Parameters:**

- `acl6-number` — Specifies the number of an IPv6 ACL that defines a range of multicast groups. A basic or advanced ACL can be used in an IPv6 multicast group policy. — *Valores:* The value is an integer that ranges from 2000 to 3999.
- `mld-version` — Applies the multicast group policy only to the MLD messages of the specified version. If this parameter is not specified, the multicast group policy applies to all MLD messages. — *Valores:* The value is 1 or 3. ● 1: MLDv1 ● 2: MLDv2
- `default-permit` — Configures the multicast group policy to permit all groups by default. That is, if the referenced ACL has no rules, the multicast group policy allows hosts in the VLAN to join all groups. — *Valores:* -

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade.

**Example:**

```text
# Prevent MLDv2 hosts in VLAN 4 from joining IPv6 multicast group ff1e::1/32.
<HUAWEI> system-view
[HUAWEI] acl ipv6 number 2001
[HUAWEI-acl6-basic-2001] rule deny source ff1e::1/32
[HUAWEI-acl6-basic-2001] quit
[HUAWEI] mld-snooping enable
[HUAWEI] vlan 4
[HUAWEI-vlan4] mld-snooping enable
[HUAWEI-vlan4] mld-snooping group-policy 2001 2 default-permit
```


## MPLS compatible command

19.7.1 explicit-path (upgrade-compatible command) 19.7.2 mpls rsvp-te authentication handshake (upgrade-compatible command) 19.7.3 mpls rsvp-te send-message (upgrade-compatible command) 19.7.4 mpls te max-reservable-bandwidth (upgrade-compatible command) 19.7.5 mpls te bypass-tunnel bandwidth (upgrade-compatible command) 19.7.6 mpls te protect-switch manual (upgrade-compatible command) 19.7.7 snmp-agent trap enable (MPLS) (upgrade-compatible command) 19.7.8 snmp-agent trap enable feature-name ldp (upgrade-compatible command) 19.7.9 static-cr-lsp ingress bandwidth (upgrade-compatible command) 19.7.10 static-cr-lsp transit bandwidth (upgrade-compatible command) 19.7.11 undo mpls te auto-frr (upgrade-compatible command)

### `explicit-path (upgrade-compatible command)`

> **Página:** 72 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** Using the explicit-path command, you can configure an explicit path of a tunnel. By default, no explicit path of a tunnel is configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
explicit-path path-name { enable | disable }
```

**Parameters:**

- `path-name` — Indicates the name of an explicit path. — *Valores:* The value is a string of 1 to 31 characters.
- `enable` — Enables the explicit path of a tunnel. — *Valores:* -
- `disable` — Disables the explicit path of a tunnel. — *Valores:* -

**Usage Guidelines:**

You can configure an explicit path only after MPLS TE is enabled. The addresses of the hops along the explicit path cannot overlap or loops cannot occur. If a loop occurs, CSPF detects the loop and fails to calculate the path. When the explicit path is in use, you cannot perform the following operations:

- Run the explicit-path path-name disable command to disable the explicit path.

- Run the undo explicit-path command to delete the explicit path.

**Example:**

```text
# Create an explicit path named path1.
<HUAWEI> system-view
[HUAWEI] mpls
[HUAWEI-mpls] mpls te
[HUAWEI-mpls] quit
[HUAWEI] explicit-path path1 enable
[HUAWEI-explicit-path-path1]
```


### `mpls rsvp-te authentication handshake (upgrade- compatible command)`

> **Página:** 73 · **Views (Modo):** VLANIF interface view, GE interface view, XGE interface view, 40GE interface view, Eth-trunk interface view, RSVP-TE neighbor view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The mpls rsvp-te authentication handshake command configures the RSVP-TE handshake mechanism and sets a local password. The undo mpls rsvp-te authentication handshake command deletes the RSVP-TE handshake mechanism configuration. By default, no RSVP-TE handshake mechanism is configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
mpls rsvp-te authentication handshake local-secret
undo mpls rsvp-te authentication handshake
```

**Parameters:**

- `local-secret` — Specifies the local password. — *Valores:* The value is a string of 8 to 40 characters without spaces. It has no default value.

**Usage Guidelines:**

**Usage Scenario**

Enhanced RSVP authentication can be configured to improve the system security and the capability to authenticate users in the unfavorable environment such as network congestion. Enhanced RSVP authentication functions are as follows:

- Sets the sliding window size for RSVP authentication messages.

- Configures the RSVP-TE handshake mechanism and sets the local password. Traditional RSVP authentication is used to prevent an unauthorized remote node from setting up a neighbor relationship with the local node. It also prevents attacks (such as maliciously reserving a large number of bandwidth resources) initiated by a remote node after the remote node constructs pseudo RSVP messages to set up an RSVP neighbor relationship with the local node. Traditional RSVP authentication, however, cannot prevent anti-replay attacks or prevent the problem of neighbor relationship termination due to RSVP message disorder. In an unfavorable environment, the mpls rsvp-te authentication handshake command can be used to configure the RSVP-TE handshake mechanism and sets the local password to prevent anti-replay and improve network security.

**Prerequisites**

The RSVP authentication function must have been enabled by running the mpls rsvp-te authentication { { cipher | plain } auth-key | keychain keychain-name } command in the interface view or the MPLS RSVP-TE neighbor view.

**Precautions**

local-secret is valid only on the local device and can be different from local-secret configured on neighbors.

**Example:**

```text
# Configure the RSVP-TE handshake mechanism.
<HUAWEI> system-view
[HUAWEI] interface vlanif 100
[HUAWEI-Vlanif100] mpls
[HUAWEI-Vlanif100] mpls te
[HUAWEI-Vlanif100] mpls rsvp-te
[HUAWEI-Vlanif100] mpls rsvp-te authentication cipher beijing123
[HUAWEI-Vlanif100] mpls rsvp-te authentication handshake 12345678
# Configure the RSVP-TE handshake mechanism.
<HUAWEI> system-view
[HUAWEI] interface gigabitethernet 0/0/1
[HUAWEI-GigabitEthernet0/0/1] undo portswitch
[HUAWEI-GigabitEthernet0/0/1] mpls
[HUAWEI-GigabitEthernet0/0/1] mpls te
[HUAWEI-GigabitEthernet0/0/1] mpls rsvp-te
[HUAWEI-GigabitEthernet0/0/1] mpls rsvp-te authentication cipher beijing123
[HUAWEI-GigabitEthernet0/0/1] mpls rsvp-te authentication handshake 12345678
```


### `mpls rsvp-te send-message (upgrade-compatible command)`

> **Página:** 75 · **Views (Modo):** MPLS view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The mpls rsvp-te send-message command configures the formats of objects in a sent message. The undo mpls rsvp-te send-message command restores the default configuration. By default, the formats of objects in the sent message are not configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
mpls rsvp-te send-message suggest-label exclude
undo mpls rsvp-te send-message suggest-label exclude
```

**Parameters:**

- `suggest-label exclude` — Indicates that an RSVP message does not carry the suggest-label object. — *Valores:* -

**Usage Guidelines:**

**Usage Scenario**

The mpls rsvp-te send-message command controls the formats of objects in the messages sent by nodes. If required, you can use this command to adjust the transmission of messages so that downstream nodes can use the carried object format in processing.

**Precautions**

The modification takes effect only for new LSPs. Configurations of the four formats of objects in a sent message can take effect simultaneously.

**Example:**

```text
# Exclude the suggest-label object from a message.
<HUAWEI> system-view
[HUAWEI] mpls
[HUAWEI-mpls] mpls rsvp-te send-message suggest-label exclude
```


### `mpls te max-reservable-bandwidth (upgrade- compatible command)`

> **Página:** 76 · **Views (Modo):** Interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The mpls te max-reservable-bandwidth command sets the maximum reservable bandwidth of a link. The maximum reservable bandwidth of a link is not configured by default.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
mpls te max-reservable-bandwidth bw-value [ bc1 bc1-bw-value ]
```

**Parameters:**

- `bw-value` — Specifies the maximum reservable link bandwidth. — *Valores:* The value is an integer ranging from 0 to 40000000, in kbit/s. The default value is 0.
- `bc1 bc1-bw- value` — Specifies the maximum reservable bandwidth for a BC1 link. — *Valores:* The value is an integer ranging from 0 to 40000000, in kbit/s. The default value is 0.

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After an upgrade, this command is no longer supported, and it is replaced by the mpls te bandwidth max-reservable-bandwidth command.


### `mpls te bypass-tunnel bandwidth (upgrade-compatible command)`

> **Página:** 77 · **Views (Modo):** Tunnel interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** Using the mpls te bypass-tunnel bandwidth command, you can configure the bypass LSP bandwidth. By default, no bypass LSP bandwidth is configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
mpls te bypass-tunnel bandwidth { bandwidth | { bc0 | bc1 } { bandwidth | un-limited } }
```

**Parameters:**

- `bandwidth` — Specifies the bandwidth that the bypass tunnel can protect. — *Valores:* The value is an integer that ranges from 1 to 32000000, in kbit/s.
- `bc0` — Indicates the BC0 bandwidth (global bandwidth) that the bypass tunnel can protect. — *Valores:* -
- `bc1` — Indicates the BC1 bandwidth (subaddress pool bandwidth) that the bypass tunnel can protect. — *Valores:* -
- `un-limited` — Indicates that there is no limit on the total bandwidth that can be protected. — *Valores:* -

**Usage Guidelines:**

The total bandwidth of LSPs protected by the bypass tunnel is not more than the bandwidth of the primary tunnel. When multiple bypass tunnels exist, the system selects a single bypass tunnel through the best-fit algorithm. The total bandwidth of all the LSPs protected by the bypass tunnel is not greater than the bandwidth of the primary tunnel. When multiple bypass tunnels exist, the system determines the bypass tunnel through the best-fit algorithm.

**Example:**

```text
# Configure Tunnel1 to protect the LSPs that use the BC0 bandwidth and set no
```

limit on the bandwidth to be protected.

```text
<HUAWEI> system-view
[HUAWEI] interface tunnel 1
[HUAWEI-Tunnel1] tunnel-protocol mpls te
[HUAWEI-Tunnel1] destination 2.2.2.2
[HUAWEI-Tunnel1] mpls te tunnel-id 100
[HUAWEI-Tunnel1] mpls te bypass-tunnel bandwidth bc0 un-limited
[HUAWEI-Tunnel1] mpls te commit
```


### `mpls te protect-switch manual (upgrade-compatible command)`

> **Página:** 78 · **Views (Modo):** Tunnel interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The mpls te protect-switch manual command sends a manual switchover request to a specified tunnel. By default, no manual switching request for a specified tunnel is configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
mpls te protect-switch manual [ work-lsp | protect-lsp ]
```

**Parameters:**

- `work-lsp` — Switches traffic manually to the primary tunnel. — *Valores:* -
- `protect-lsp` — Switches traffic manually to a protection tunnel. — *Valores:* -

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After an upgrade, this command is no longer supported, and it is replaced by the mpls te protect-switch manual command.


### `snmp-agent trap enable (MPLS) (upgrade-compatible command)`

> **Página:** 79 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable command enables SNMP traps with a related parameter. The undo snmp-agent trap enable command disables SNMP traps with a related parameter.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable { static-lsp | ldp | lsp [ mplsxcup | mplsxcdown ] |
tunnel-ps | te { tunnel-reop | te-frr [ private ] | hot-standby | ordinary |
bandwidth-change } | [ te ] tunnel }
undo snmp-agent trap enable { static-lsp | ldp | lsp [ mplsxcup | mplsxcdown ]
| tunnel-ps | te { tunnel-reop | te-frr [ private ] | hot-standby | ordinary |
bandwidth-change } | [ te ] tunnel }
```

**Parameters:**

- `static-lsp` — Enables the trap of static LSPs. — *Valores:* -
- `ldp` — Enables LDP traps. — *Valores:* -
- `lsp mplsxcup` — Enables the mplsXCUp trap. — *Valores:* -
- `lsp mplsxcdown` — Enables the mplsXCDown trap. — *Valores:* -
- `tunnel-ps` — Enables the TE protection switching trap. — *Valores:* -
- `te tunnel-reop` — Enables trap of the TE route re-optimization. — *Valores:* -
- `te te-frr` — Enables the public trap of TE FRR. — *Valores:* -
- `te-frr private` — Enables the private trap of TE FRR. — *Valores:* -
- `te hot-standby` — Enables the trap of the hot-standby CR-LSP. — *Valores:* -
- `te ordinary` — Enables the trap of the ordinary CR-LSP. — *Valores:* -
- `bandwidth-change` — Enables the system to send related private traps when the tunnel bandwidth changes. — *Valores:* -
- `tunnel` — Enables the trap of the tunnel. — *Valores:* -

**Usage Guidelines:**

By default, the trap function is disabled in the process of the MPLS LSP establishment. To check the status of an LSP, run the snmp-agent trap enable lsp { mplsxcup | mplsxcdown } command when mplsXCUp or mplsXCDown is enabled. After the undo snmp-agent trap enable command is run, information about mplsXCUp or mplsXCDown is not displayed, and the status of the trap is unchanged. When you run the snmp-agent trap enable command again, information about the restored trap is displayed.

**Example:**

```text
# Enable the private trap of TE FRR.
<HUAWEI> system-view
[HUAWEI] snmp-agent trap enable te te-frr private
# Enable the mplsXCUp trap.
<HUAWEI> system-view
[HUAWEI] snmp-agent trap enable lsp mplsxcup
Warning: Enabling the alarm function will lead to the generation of excessive a
larms. Continue? [Y/N]
```


### `snmp-agent trap enable feature-name ldp (upgrade- compatible command)`

> **Página:** 80 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable feature-name ldp command enables the trap for the MPLS LDP module. The undo snmp-agent trap enable feature-name ldp command disables the trap for the MPLS LDP module. By default, the trap is disabled for the MPLS LDP module.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable feature-name ldp trap-name { session-down |
session-up }
undo snmp-agent trap enable feature-name ldp trap-name { session-down |
session-up }
```

**Parameters:**

- `trap-name` — Enables the trap of MPLS LDP events of a specified type. — *Valores:* -
- `session-down` — Enables the trap of the event that an LDP session goes Down in the MIB. — *Valores:* -
- `session-up` — Enables the trap of the event that an LDP session goes Up in the MIB. — *Valores:* -

**Usage Guidelines:**

Run the snmp-agent trap enable feature-name ldp command to enable the LDP session trap. Currently, all traps of the MPLS LDP module are non-excessive trap. The frequent LDP session status changes do not trigger a large number of traps.

**Example:**

```text
# Enable the trap of the event that an LDP session is reestablished.
<HUAWEI> system-view
[HUAWEI] snmp-agent trap enable feature-name ldp trap-name session-up
```


### `static-cr-lsp ingress bandwidth (upgrade-compatible command)`

> **Página:** 81 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** Using the static-cr-lsp ingress bandwidth command, you can configure a static CR-LSP and specify its bandwidth on the ingress LSR. By default, no static CR-LSP on the ingress LSR is configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
static-cr-lsp ingress { tunnel-interface tunnel interface-number | tunnel-name }
destination destination-address { nexthop next-hop-address | outgoing-interface
interface-type interface-number } * out-label out-label bandwidth { bc0 | bc1 }
bandwidth
```

**Parameters:**

- `tunnel-interface tunnel interface- number` — Specifies the tunnel interface of a static CR-LSP. interface-number indicates the tunnel interface number. — *Valores:* -
- `tunnel-name` — Specifies the name of a CR- LSP. — *Valores:* The name is a string of 1 to 19 case-sensitive characters, spaces and abbreviation not supported. If you use the interface Tunnel 2 command to create a tunnel interface for a static CR-LSP, the tunnel name in the static-cr-lsp ingress command must be formatted as "Tunnel2", otherwise, the tunnel cannot be created. There is no such a limit for the transit node and egress node.
- `destination destination- address` — Specifies the destination IP address of a static CR-LSP. — *Valores:* -
- `nexthop next- hop-address` — Specifies the next-hop IP address of a static CR-LSP. — *Valores:* -
- `outgoing- interface interface-type interface-number` — Specifies the type and number of an outgoing interface. This parameter is only applicable to a P2P link. — *Valores:* -
- `out-label out- label` — Specifies the value of an outgoing label. — *Valores:* out-label is an integer ranging from 16 to 1048575.
- `bc0` — Specifies BC0 bandwidth of a static CR-LSP. — *Valores:* -
- `bc1` — Specifies BC1 bandwidth of a static CR-LSP. — *Valores:* -
- `bandwidth` — Specifies the bandwidth required by a CR-LSP. — *Valores:* The value ranges from 0 to 4000000000, in kbit/s. The default value is 0.

**Usage Guidelines:**

Before setting up an MPLS TE tunnel through a static CR-LSP, configure a static route or an IGP to ensure connectivity between LSRs, and enable basic MPLS and MPLS TE functions.

**Example:**

```text
# Configure the static CR-LSP named Tunnel1, with the destination IP address
```

being 10.1.3.1, the next-hop address being 10.1.1.2, the outgoing label being 237, and the required bandwidth being 20 kbit/s from BC0 on the ingress.

```text
<HUAWEI> system-view
[HUAWEI] static-cr-lsp ingress tunnel-interface Tunnel 1 destination 10.1.3.1 nexthop 10.1.1.2 out-label 237 bandwidth bc0 20
```


### `static-cr-lsp transit bandwidth (upgrade-compatible command)`

> **Página:** 83 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** Using the static-cr-lsp transit bandwidth command, you can configure a static CR-LSP and specify its bandwidth on a transit LSR. By default, no static CR-LSP on a transit LSR is configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
static-cr-lsp transit lsp-name [ incoming-interface interface-type interface-number ] in-label in-label { nexthop next-hop-address | outgoing-interface
interface-type interface-number } * out-label out-label bandwidth { bc0 | bc1 }
bandwidth [ description description ]
```

**Parameters:**

- `lsp-name` — Specifies the CR-LSP name. — *Valores:* The name is a string of 1 to 19 case-sensitive characters, spaces not supported.
- `incoming-interface interface-type interface-number` — Specifies the name of an incoming interface. — *Valores:* -
- `in-label in-label` — Specifies the value of an incoming label. — *Valores:* An integer ranging from 16 to 1023
- `nexthop next-hop- address` — Specifies the next-hop address. — *Valores:* -
- `outgoing-interface interface-type interface-number` — Specifies the name of an outgoing interface. — *Valores:* -
- `out-label out-label` — Specifies the value of an outgoing label. — *Valores:* An integer ranging from 16 to 1048575.
- `bc0` — Obtains the bandwidth from BC0. — *Valores:* -
- `bc1` — Obtains the bandwidth from BC1. — *Valores:* -
- `bandwidth` — Specifies the bandwidth required by a CR-LSP. — *Valores:* The value ranges from 0 to 4000000000, in kbit/s. The default value is 0.
- `description description` — Specifies the description information. — *Valores:* -

**Usage Guidelines:**

Before setting up an MPLS TE tunnel through a static CR-LSP, configure a static route or an IGP to ensure connectivity between LSRs, and enable basic MPLS and MPLS TE functions.

**Example:**

```text
# Configure the static CR-LSP named tunnel34, with the incoming interface being
```

VLANIF10, the incoming label being 123, the outgoing interface being VLANIF20, the outgoing label as 253, the required BC0 bandwidth being 20 kbit/s on the transit node.

```text
<HUAWEI> system-view
[HUAWEI] static-cr-lsp transit tunnel34 incoming-interface vlanif 10 in-label 123 outgoing-interface
vlanif 20 out-label 253 bandwidth bc0 20
```


### `undo mpls te auto-frr (upgrade-compatible command)`

> **Página:** 84 · **Views (Modo):** Interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The undo mpls te auto-frr command disables MPLS TE Auto FRR in the interface view.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
undo mpls te auto-frr
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After the upgrade, this command is no longer supported, and it is replaced by the mpls te auto-frr block command.


## VPN compatible command

19.8.1 display ipv6 prefix-limit statistics (upgrade-compatible command) 19.8.2 display ipv6 vpn-instance (upgrade-compatible command) 19.8.3 ipv6 binding vpn6-instance (upgrade-compatible command) 19.8.4 ipv6 vpn6-instance (upgrade-compatible command) 19.8.5 link-alive (upgrade-compatible command) 19.8.6 snmp-agent trap enable feature-name l3vpn (upgrade-compatible command) 19.8.7 snmp-agent trap enable l3vpn (upgrade-compatible command) 19.8.8 sa authentication-hex (upgrade-compatible command) 19.8.9 sa encryption-hex (upgrade-compatible command) 19.8.10 sa string-key (upgrade-compatible command)

### `display ipv6 prefix-limit statistics (upgrade-compatible command)`

> **Página:** 85 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display ipv6 prefix-limit statistics command displays the statistics of the prefix limits of IPv6 VPN instances.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display ipv6 prefix-limit { all-vpn6-instance | vpn6-instance vpn-instance-name } statistics
```

**Parameters:**

- `all-vpn6-instance` — Indicates all IPv6 VPN instances. — *Valores:* -
- `vpn6-instance vpn-instance- name` — Specifies the name of an IPv6 VPN instance. — *Valores:* -

**Usage Guidelines:**

You can run the display ipv6 prefix-limit statistics command to view the number of times that a protocol re-adds or deletes routes according to the prefix limit of a specified IPv6 VPN instance.

**Example:**

```text
# Display the statistics of the prefix limits of all IPv6 VPN instances.
<HUAWEI> display ipv6 prefix-limit all-vpn6-instance statistics
-------------------------------------------------------------------------------
IPv6 VPN instance name: vrf1
DenyAdd TryAddInDelState NotifyDelAll NotifyDelFinish NotifyAddRoute
DIRECT 0 0 0 0 0
STATIC 0 0 0 0 0
OSPFv3 11 3 1 0 5
IS-IS 106 0 1 0 5
RIPng 98 0 1 1 5
BGP 2 0 1 1 5
------------------------------------------------------------------------------
IPv6 VPN instance name: VPN123
DenyAdd TryAddInDelState NotifyDelAll NotifyDelFinish NotifyAddRoute
DIRECT 0 0 0 0 0
STATIC 0 0 0 0 0
OSPFv3 11 3 1 0 5
IS-IS 106 0 1 0 5
RIPng 98 0 1 1 5
BGP 2 0 1 1 5
```

Table 19-3 Description of the display ipv6 prefix-limit statistics command output

| Item | Description |
| --- | --- |
| DenyAdd | Number of routes that the protocol fails to add to the RIB because of the prefix limit. |
| TryAddInDelState | Number of routes that the protocol fails to add to the RIB because the RIB is in the process of deleting routes. |
| NotifyDelAll | Number of times that the RIB notifies the protocol of deleting routes when the prefix limit is decreased. |
| NotifyDelFinish | Number of times that the protocol notifies the RIB of completion of deleting routes. |
| NotifyAddRoute | Number of times that the RIB notifies the protocol of re-adding routes. |

```text
# Display the statistics of the prefix limit of the IPv6 VPN instance named vrf1.
<HUAWEI> display ipv6 prefix-limit vpn6-instance vrf1 statistics
-------------------------------------------------------------------------------
IPv6 VPN instance name: vrf1
DenyAdd TryAddInDelState NotifyDelAll NotifyDelFinish NotifyAddRoute
DIRECT 0 0 0 0 0
STATIC 0 0 0 0 0
OSPFv3 11 3 1 0 5
IS-IS 106 0 1 0 5
RIPng 98 0 1 1 5
BGP 2 0 1 1 5
```


### `display ipv6 vpn-instance (upgrade-compatible command)`

> **Página:** 87 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display ipv6 vpn6-instance command displays information about an IPv6 VPN instance.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display ipv6 vpn6-instance [ brief | verbose ] [ vpn6-instance-name ]
```

**Parameters:**

- `brief` — Displays summary information about an IPv6 VPN instance. — *Valores:* -
- `verbose` — Displays detailed information about the IPv6 VPN instances and their associated interfaces. — *Valores:* -
- `vpn6-instance- name` — Specifies the name of an IPv6 VPN instance. — *Valores:* The name is a string of 1 to 31 case-sensitive characters.

**Usage Guidelines:**

If a VPN instance is configured, you can check the configuration of the instance by using the display ipv6 vpn6-instance command. You can also use this command to view the VPN instances configured on the local device. When no parameters are specified, the command displays brief information about all the configured VPN instances.

**Example:**

```text
# View brief information about all the configured IPv6 VPN instances.
<HUAWEI> display ipv6 vpn6-instance
Total VPN-Instances configured : 3
Total IPv4 VPN-Instances configured : 2
Total IPv6 VPN-Instances configured : 1
VPN-Instance Name RD Address-family
vpn1
vpna 100:1 IPv4
vpna 100:3 IPv6
vpnb 100:2 IPv4
```

Table 19-4 Description of the display ip vpn-instance command output

| Item | Description |
| --- | --- |
| Total VPN-Instances configured | Total number of VPN instances configured on the local end. |
| Total IPv4 VPN-Instances configured | Total number of locally configured VPN instances for which IPv4 address families are enabled. |
| Total IPv6 VPN-Instances configured | Total number of locally configured VPN instances for which IPv6 address families are enabled. |
| VPN-Instance Name | Name of the VPN instance. |

| Item | Description |
| --- | --- |
| RD | RD of the VPN instance IPv4 address family or IPv6 address family. |
| Creation Time | Time when an IPv4 or IPv6 address family is enabled for the VPN instance. |
| Address-family | Address family enabled for the VPN instance. The address family can be: ● Null, if no address family is enabled. ● ipv4, if only the IPv4 address family is enabled. ● ipv6, if only the IPv6 address family is enabled. |

```text
<HUAWEI> display ipv6 vpn6-instance brief
Total VPN-Instances configured : 3
Total IPv4 VPN-Instances configured : 2
Total IPv6 VPN-Instances configured : 1
VPN-Instance Name RD Address-family
vpn1
vpna 100:1 IPv4
vpna 100:3 IPv6
vpnb 100:2 IPv4
# View detailed information about all IPv6 VPN instances.
<HUAWEI> display ipv6 vpn-instance verbose
Total VPN-Instances configured : 1
Total IPv4 VPN-Instances configured : 1
Total IPv6 VPN-Instances configured : 1
VPN-Instance Name and ID : vpna, 6
Description : vpna-1
Service ID : 12
Interfaces : Vlanif10
Address family ipv4
Create date : 2012/12/3 15:36:20 UTC+08:00
Up time : 6 days, 04 hours, 41 minutes and 57 seconds
Route Distinguisher : 100:1
Export VPN Targets : 1:1
Import VPN Targets : 1:1
Label Policy : label per instance
Per-Instance Label : 1024
IP FRR Route Policy : 20
VPN FRR Route Policy : 12
Import Route Policy : 10
Export Route Policy : 20
Tunnel Policy : bindTE
Maximum Routes Limit : 2000
Threshold Routes Limit : 80%
Maximum Prefixes Limit : 1024
Threshold Prefixes Limit : 50%
Install Mode : route-unchanged
Log Interval : 10
Address family ipv6
Create date : 2012/12/3 15:36:20 UTC+08:00
Up time : 6 days, 04 hours, 41 minutes and 57 seconds
Log Interval : 5
```

Table 19-5 Description of the display ip vpn-instance verbose command output

| Item | Description |
| --- | --- |
| Total VPN-Instances configured | Total number of VPN instances configured on the local end. |
| Total IPv4 VPN-Instances configured | Total number of locally configured VPN instances for which IPv4 address families are enabled. |
| Total IPv6 VPN-Instances configured | Total number of locally configured VPN instances for which IPv6 address families are enabled. |
| VPN-Instance Name and ID | Name and ID of the VPN instance. The ID is assigned by the system, which facilitates indexing. |
| Description | Description of the VPN instance. This field is displayed in the command output only when the description (VPN instance view) command is used. |
| Service ID | Service ID of the VPN instance. This item is displayed only after the service-id (VPN instance view) command is run in the VPN instance view. |
| Interfaces | Interfaces bound to the VPN instance. This field is displayed only after the ip binding vpn-instance command is configured on these interfaces. |
| Address family ipv4 | Information about the IPv4 address family enabled for the VPN instance. |
| Address family ipv6 | Information about the IPv6 address family enabled for the VPN instance. |
| Create date | Time when the VPN instance is created. |
| Up time | Period during which the VPN instance maintains in the Up state. |
| Route Distinguisher | RD of the VPN instance IPv4 address family or IPv6 address family |
| Export VPN Targets | Route Target list in the outbound direction. To set the VPN target, run the vpn-target command. |

| Item | Description |
| --- | --- |
| Import VPN Targets | Route Target list in the inbound direction. To set the VPN target, run the vpn-target command. |
| Label Policy | Label policy: ● label per instance: indicates that the same label is allocated to routes of a VPN instance. This field is displayed in the command output only when the apply-label per- instance command is run in the VPN instance view. ● label per route: indicates that each route of a VPN instance is assigned a label. Label allocation for routes of a VPN instance is implemented in this mode. |
| Per-Instance Label | Label value used when all VPN routes of the VPN instance address family share one label. This field is displayed only after the apply-label per- instance command is run in the VPN instance address family view. |
| IP FRR Route Policy | IP FRR route policy used for the address family. This item is displayed only after the ip frr command is run in the VPN instance IPv4 address family view. |
| VPN FRR Route Policy | VPN FRR route policy used for the address family. This item is displayed only after the vpn frr command is run in the VPN instance IPv4 address family view. |
| Import Route Policy | Import Route-Policy applied to the VPN instance. This field is displayed only after the import route-policy command is run in the VPN instance address family view. |
| Export Route Policy | Export Route-Policy applied to the VPN instance. This field is displayed only after the export route-policy command is run in the VPN instance address family view. |

| Item | Description |
| --- | --- |
| Tunnel Policy | Tunnel policy applied to the VPN instance. This field is displayed only after the tnl-policy command is run in the VPN instance address family view. |
| Maximum Routes Limit | Maximum number of routes supported by the current address family. This field is displayed only after the routing-table limit command is run in the VPN instance address family view. |
| Threshold Routes Limit | Percentage of the maximum number of routes specified for the current address family. When the maximum number of routes reaches the percentage threshold, an alarm is generated.This field is displayed only after the routing-table limit command is run in the VPN instance address family view. |
| Maximum Prefixes Limit | Maximum number of prefixes supported by the current address family of the VPN instanceThis field is displayed only after the prefix limit command is run in the VPN instance address family view. |
| Threshold Prefixes Limit | Percentage of the maximum number of prefixes specified for the current address family of the VPN instance. When the maximum number of prefixes reaches the percentage threshold, an alarm is generated.This field is displayed only after the prefix limit command is run in the VPN instance address family view. |
| Install Mode | Method of processing routes. The prefix limit command can be used to specify the route processing method when the threshold is lowered due to the number of route prefixes exceeding the upper threshold. ● If route-unchanged is configured, routes in the routing information base (RIB) table remain unchanged. ● If route-unchanged is not configured, all routes in the RIB table are deleted and the routes are re-installed in the RIB table. |

| Item | Description |
| --- | --- |
| Log Interval | Interval for displaying log messages when the number of VPN instance routes exceeds the maximum value. The default interval is 5 seconds. The value can be set by the command limit-log-interval. |


### `ipv6 binding vpn6-instance (upgrade-compatible command)`

> **Página:** 93 · **Views (Modo):** Interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The ipv6 binding vpn6-instance command binds the current interface to an IPv6 VPN instance. The undo ipv6 binding vpn6-instance command unbinds the current interface from an IPv6 VPN instance. By default, an interface is a public network interface and is not bound to any IPv6 VPN instance.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
ipv6 binding vpn6-instance vpn6-instance-name
undo ipv6 binding vpn6-instance vpn6-instance-name
```

**Parameters:**

- `vpn6-instance- name` — Specifies the name of an IPv6 VPN instance. — *Valores:* The name is a string of 1 to 31 case-sensitive characters.

**Usage Guidelines:**

After an IPv6 VPN instance is created, the device interfaces belonging to the IPv6 VPN instance need to be bound to the instance; otherwise, the interfaces are public network interfaces. After an interface is bound to an IPv6 VPN instance or an interface is unbound from an IPv6 VPN instance, the Layer 3 features such as the IPv6 address and IPv6 routing protocol configured on this interface are deleted.


### `ipv6 vpn6-instance (upgrade-compatible command)`

> **Página:** 94 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The ipv6 vpn6-instance command creates an IPv6 VPN instance and displays the IPv6 VPN instance view. The undo ipv6 vpn6-instance command deletes a specified IPv6 VPN instance. By default, no IPv6 VPN instance exists.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
ipv6 vpn6-instance vpn6-instance-name
undo ipv6 vpn6-instance vpn6-instance-name
```

**Parameters:**

- `vpn6-instance- name` — Specifies the name of an IPv6 VPN instance. — *Valores:* The name is a string of 1 to 31 case-sensitive characters without any spaces.

**Usage Guidelines:**

After this command is run, an IPv6 VPN instance is created and the IPv6 VPN instance view is displayed..


### `link-alive (upgrade-compatible command)`

> **Página:** 94 · **Views (Modo):** Tunnel interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The link-alive command enables the link-alive function on a GRE tunnel. The undo link-alive command disables the link-alive function on a GRE tunnel. By default, the link-alive function is disabled on a GRE tunnel.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
link-alive [ period period ] [ retry-times retry-times ]
undo link-alive
```

**Parameters:**

- `period` — Specifies the interval for sending link-alive packets. — *Valores:* The value is an integer that ranges from 1 to 32767, in seconds. The default value is 5.
- `retry-times retry-times` — Specifies the tunnel- unreachable counter value. — *Valores:* The value is an integer that ranges from 1 to 255. The default value is 3.

**Usage Guidelines:**

The link-alive function takes effect on a GRE tunnel immediately after you run the link-alive command on the tunnel interface. After you run the undo link-alive command, the link-alive function immediately becomes invalid. The source end of a GRE tunnel periodically sends link-alive packets. The tunnel-unreachable counter increases by 1 every time a link-alive packet is sent. If the source end does not receive any response packet when the tunnel-unreachable counter value reaches retry-times, the source end considers the remote end unreachable.

**Example:**

```text
# Enable the link-alive function on a GRE tunnel and retain the default parameter
```

values.

```text
<HUAWEI> system-view
[HUAWEI] interface tunnel 1
[HUAWEI-Tunnel1] tunnel-protocol gre
[HUAWEI-Tunnel1] link-alive
# Disable the link-alive function on a GRE tunnel.
<HUAWEI> system-view
[HUAWEI] interface tunnel 1
[HUAWEI-Tunnel1] undo link-alive
# Enable the link-alive function on a GRE tunnel. Set the interval for sending link-alive packets to 12 seconds and retain the default tunnel-unreachable counter
```

value.

```text
<HUAWEI> system-view
[HUAWEI] interface tunnel 1
[HUAWEI-Tunnel1] link-alive period 12
# Enable the link-alive function on a GRE tunnel. Set the interval for sending link-alive packets to 12 seconds and the tunnel-unreachable counter to 4.
<HUAWEI> system-view
[HUAWEI] interface tunnel 1
[HUAWEI-Tunnel1] link-alive period 12 retry-times 4
```


### `snmp-agent trap enable feature-name l3vpn (upgrade- compatible command)`

> **Página:** 96 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable feature-name l3vpn command enables the trap function for the L3VPN module. The undo snmp-agent trap enable feature-name l3vpn command disables the trap function for the L3VPN module. By default, the trap function for the L3VPN module is disabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable feature-name l3vpn trap-name
l3vpn_mib_trap_mid_exceed
undo snmp-agent trap enable feature-name l3vpn trap-name
l3vpn_mib_trap_mid_exceed
```

**Parameters:**

- `trap-name` — Enables the traps of L3VPN events of specified types. — *Valores:* -
- `l3vpn_mib_trap_mid_exceed` — Enables the trap of the event indicating that the number of private route prefixes exceeds the middle threshold. — *Valores:* -

**Usage Guidelines:**

The Simple Network Management Protocol (SNMP) is a standard network management protocol widely used on TCP/IP networks. It uses a central computer (a network management station) that runs network management software to manage network elements. The management agent on the network element automatically reports traps to the network management station. After that, the network administrator immediately takes measures to resolve the problem. The snmp-agent trap enable feature-name l3vpn command enables the trap function for L3VPN modules.

**Example:**

```text
# Enable the trap of the event indicating that the number of private route prefixes
```

exceeds the middle threshold in the system view.

```text
<HUAWEI> system-view
[HUAWEI] snmp-agent trap enable feature-name l3vpn trap-name l3vpn_mib_trap_mid_exceed
```


### `snmp-agent trap enable l3vpn (upgrade-compatible command)`

> **Página:** 97 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable l3vpn command enables the device to send the L3VPN trap message. The undo snmp-agent trap enable l3vpn command prohibits the device from sending the L3VPN trap message. By default, the L3VPN trap message cannot be sent.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable l3vpn
undo snmp-agent trap enable l3vpn
```

**Usage Guidelines:**

None

**Example:**

```text
# Permit the device to send the L3VPN trap message.
<HUAWEI> system-view
[HUAWEI] snmp-agent trap enable l3vpn
```


### `sa authentication-hex (upgrade-compatible command)`

> **Página:** 98 · **Views (Modo):** SA view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The sa authentication-hex command sets an authentication in hexadecimal format or cipher text for Security Associations (SAs).

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
sa authentication-hex { inbound | outbound } { ah | esp } plain hex-plain-key
```

**Parameters:**

- `inbound` — Specifies SA parameters for incoming packets. — *Valores:* -
- `outbound` — Specifies SA parameters for outgoing packets. — *Valores:* -
- `ah` — Specifies SA parameters for Authentication Header (AH). If the security proposal applied to an SA uses AH, ah must be configured in the sa authentication-hex command. — *Valores:* -
- `esp` — Specifies SA parameters for Encapsulating Security Payload (ESP). If the security proposal applied to an SA uses ESP, esp must be configured in the sa authentication-hex command. — *Valores:* -
- `plain` — Indicates the plain text used for authentication. — *Valores:* -
- `hex-plain- key` — Specifies the plain text key. — *Valores:* The value is in hexadecimal notation. ● If authentication algorithm Message Digest 5 (MD5) is used, the length of the key is 16 bytes. ● If authentication algorithm Secure Hash Algorithm-1 (SHA-1) is used, the length of the key is 20 bytes. ● If authentication algorithm SHA2-256 is used, the length of the key is 32 bytes. NOTE The MD5 and SHA-1 authentication algorithms have security risks; therefore, you are advised to use SHA-256 preferentially.

**Usage Guidelines:**

This command is upgrade compatible and can be executed during configuration recovery. Users cannot manually configure this command. After the upgrade, this command is no longer supported, and it is replaced by the sa authentication-hex command.


### `sa encryption-hex (upgrade-compatible command)`

> **Página:** 99 · **Views (Modo):** SA view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The sa encryption-hex command configures an encryption key for manual Security Association (SA) in hexadecimal format.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
sa encryption-hex { inbound | outbound } { ah | esp } plain hex-plain-key
```

**Parameters:**

- `inbound` — Specifies SA parameters for incoming packets. — *Valores:* -
- `outbound` — Specifies SA parameters for outgoing packets. — *Valores:* -
- `ah` — Specifies SA parameters for Authentication Header (AH). If the security proposal applied to an SA uses AH, ah must be configured in the sa encryption-hex command. — *Valores:* -
- `esp` — Specifies SA parameters for Encapsulating Security Payload (ESP). If the security proposal applied to an SA uses ESP, esp must be configured in the sa encryption-hex command. — *Valores:* -
- `plain` — Indicates the plaintext used for authentication. — *Valores:* -
- `hex-plain- key` — Specifies the plaintext key. — *Valores:* The value is in hexadecimal notation. ● If encryption algorithm Data Encryption Standard (DES) is used, the length of the key is 8 bytes. ● If encryption algorithm Triple Data Encryption Standard (3DES) is used, the length of the key is 24 bytes. ● If encryption algorithm Advanced Encryption Standard 128 (AES-128) is used, the length of the key is 16 bytes. ● If encryption algorithm AES-192 is used, the length of the key is 24 bytes. ● If encryption algorithm AES-256 is used, the length of the key is 32 bytes. NOTE The DES and 3DES encryption algorithms have security risks; therefore, you are advised to use AES-128, AES-192 or AES-256 preferentially.

**Usage Guidelines:**

This command is upgrade compatible and can be executed during configuration recovery. Users cannot manually configure this command. After the upgrade, this command is no longer supported, and it is replaced by the sa encryption-hex command.


### `sa string-key (upgrade-compatible command)`

> **Página:** 101 · **Views (Modo):** SA view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The sa string-key command configures an authentication key in the string format.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
sa string-key { inbound | outbound } { ah | esp } plain string-plain-key
```

**Parameters:**

- `inbound` — Specifies SA parameters for incoming packets. — *Valores:* -
- `outbound` — Specifies SA parameters for outgoing packets. — *Valores:* -
- `ah` — Specifies SA parameters for Authentication Header (AH). If the security proposal applied to an SA uses AH, ah must be configured in the sa string-key command. — *Valores:* -
- `esp` — Specifies SA parameters for Encapsulating Security Payload (ESP). If the security proposal applied to an SA uses ESP, esp must be configured in the sa string-key command. — *Valores:* -
- `plain` — Indicates the plaintext used for authentication. — *Valores:* -
- `string-plain- key` — Specifies the plaintext key. — *Valores:* The value is a string of 1 to 127 case-sensitive characters.

**Usage Guidelines:**

This command is upgrade compatible and can be executed during configuration recovery. Users cannot manually configure this command. After the upgrade, this command is no longer supported, and it is replaced by the sa string-key command.


## WLAN Compatible Commands

19.9.1 ap-location (upgrade-compatible command) 19.9.2 traffic-filter (AP wired port profile view) (upgrade-compatible command) 19.9.3 traffic-filter (traffic profile view) (upgrade-compatible command)

### `ap-location (upgrade-compatible command)`

> **Página:** 102 · **Views (Modo):** AP view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** ap-location command sets the latitude and longitude of an AP. By default, no latitude or longitude is configured for an AP.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
ap-location longitude { e | w } longitude-value latitude { s | n } latitude-value
ap-location latitude { s | n } latitude-value longitude { e | w } longitude-value
```

**Parameters:**

- `longitude e longitude- value` — Specifies the east longitude value of an AP. — *Valores:* The value supports two formats: degrees, minutes, and seconds (DMS) and decimal degrees (DD). ● The DMS format is XXX-XX-XX. XXX ranges from 0 to 180, and XX ranges from 0 to 59. ● The DD format is XXX.XXXXXXXXX. XXX ranges from 0 to 180, and XXXXXXXXX is a decimal supporting a maximum of 9 digits. For example, the east longitude value of an AP can be set to longitude e 120-45-23 in DMS format and longitude e 120.756333333 in DD format.
- `longitude w longitude- value` — Specifies the west longitude value of an AP. — *Valores:* The value supports two formats: DMS and DD. ● The DMS format is XXX-XX-XX. XXX ranges from 0 to 180, and XX ranges from 0 to 59. ● The DD format is XXX.XXXXXXXXX. XXX ranges from 0 to 180, and XXXXXXXXX is a decimal supporting a maximum of 9 digits. For example, the west longitude value of an AP can be set to longitude w 120-45-23 in DMS format and longitude w 120.756333333 in DD format.
- `latitude s latitude- value` — Specifies the south longitude value of an AP. — *Valores:* The value supports two formats: DMS and DD. ● The DMS format is XX-XX-XX. The first XX ranges from 0 to 90, and the other XXs range from 0 to 59. ● The DD format is XX.XXXXXXXXX. XX ranges from 0 to 90, and XXXXXXXXX is a decimal supporting a maximum of 9 digits. For example, the south longitude value of an AP can be set to latitude s 78-45-23 in DMS format and latitude s 78.756333333 in DD format.
- `latitude n latitude- value` — Specifies the north longitude value of an AP. — *Valores:* The value supports two formats: DMS and DD. ● The DMS format is XX-XX-XX. The first XX ranges from 0 to 90, and the other XXs range from 0 to 59. ● The DD format is XX.XXXXXXXXX. XX ranges from 0 to 90, and XXXXXXXXX is a decimal supporting a maximum of 9 digits. For example, the north longitude value of an AP can be set to latitude n 78-45-23 in DMS format and latitude n 78.756333333 in DD format.

**Usage Guidelines:**

You can run this command to set the longitude and latitude of an AP for easily locating it.


### `traffic-filter (AP wired port profile view) (upgrade- compatible command)`

> **Página:** 104 · **Views (Modo):** AP wired port profile view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The traffic-filter command configures ACL-based IPv4 packet filtering on an AP's wired interface. The undo traffic-filter command cancels ACL-based IPv4 packet filtering configuration on an AP's wired interface. By default, ACL-based IPv4 packet filtering is not configured on an AP's wired interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
traffic-filter { inbound | outbound } acl { acl-number | name acl-name }
undo traffic-filter { inbound | outbound }
```

**Parameters:**

- `inbound` — Configures ACL-based IPv4 packet filtering in the inbound direction. — *Valores:* -
- `outbound` — Configures ACL-based IPv4 packet filtering in the outbound direction. — *Valores:* -
- `acl` — Filters IPv4 packets based on a specified ACL. — *Valores:* -
- `acl-number` — Specifies an ACL number. — *Valores:* The ACL must exist. The value is an integer that ranges from 3000 to 3031.
- `name acl-name` — Filters IPv4 packets based on a named ACL. acl-name indicates the ACL name. — *Valores:* The ACL name must exist. The value range is the same as that of the acl- number parameter.

**Usage Guidelines:**

**Usage scenario**

The rules for an AP's wired interface to filter IPv4 packets based on ACLs are as follows:

- If the action in the ACL rule is deny, the device discards IPv4 packets matching the rule.

- If the action in the ACL rule is permit, the device allows IPv4 packets matching the rule to pass through.

- If no rule is matched, IPv4 packets are allowed to pass through.

**Prerequisites**

An ACL rule has been created by running the acl [ number ] acl-number [ match-order { auto | config } ] or acl name acl-name acl-number [ match-order { auto | config } ] command.

**Precautions**

The traffic-filter command can reference an ACL with no rule configured. You can configure a rule for the ACL after running this command. You can configure IPv4 packet filtering based on only one ACL in one direction. If a referenced ACL needs to be replaced, configure a new ACL to overwrite the original one.


### `traffic-filter (traffic profile view) (upgrade-compatible command)`

> **Página:** 106 · **Views (Modo):** Traffic profile view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The traffic-filter command configures ACL-based IPv4 packet filtering in a traffic profile. The undo traffic-filter command cancels configuration of ACL-based IPv4 packet filtering in a traffic profile. By default, ACL-based IPv4 packet filtering is not configured in a traffic profile.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
traffic-filter { inbound | outbound } acl { acl-number1 | acl-number2 | name acl-name }
undo traffic-filter { inbound | outbound }
```

**Parameters:**

- `inbound` — Configures ACL-based IPv4 packet filtering in the inbound direction. — *Valores:* -
- `outbound` — Configures ACL-based IPv4 packet filtering in the outbound direction. — *Valores:* -
- `acl` — Filters IPv4 packets based on a specified ACL. — *Valores:* -
- `acl-number` — Specifies an ACL number. — *Valores:* The ACL must exist. The value is an integer that ranges from 3000 to 3031 and from 6000 to 6031. ● 3000 to 3031: advanced ACLs ● 6000 to 6031: user ACLs
- `name acl-name` — Filters IPv4 packets based on a named ACL. acl-name indicates the ACL name. — *Valores:* The ACL name must exist. The value range is the same as that of the acl- number parameter.

**Usage Guidelines:**

**Usage Scenario**

After the traffic-filter command is executed in the traffic profile view, the device filters packets matching a specified ACL rule:

- If the action in the ACL rule is deny, the device discards IPv4 packets matching the rule.

- If the action in the ACL rule is permit, the device allows IPv4 packets matching the rule to pass through.

- If no rule is matched, IPv4 packets are allowed to pass through.

**Prerequisites**

An ACL rule has been created by running the acl [ number ] acl-number [ match-order { auto | config } ] or acl name acl-name acl-number [ match-order { auto | config } ] command.

**Precautions**

The traffic-filter command can reference an ACL with no rule configured. You can configure a rule for the ACL after running this command. You can configure IPv4 packet filtering based on only one ACL in one direction. If a referenced ACL needs to be replaced, configure a new ACL to overwrite the original one.


## Reliability Compatible Commands

19.10.1 BFD Compatible Commands 19.10.2 DLDP Compatible Commands 19.10.3 Ethernet OAM Compatible Commands

### `BFD Compatible Commands`

> **Página:** 108 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable bfd command enables the trap function for the BFD module. By default, the trap function is disabled for the BFD module.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable bfd
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. It is replaced by the snmp-agent trap enable feature-name bfd command in the system view.

**Example:**

```text
# Create a BFD6 session named test to test the single-hop link.
<HUAWEI> system-view
[HUAWEI] bfd
[HUAWEI-bfd] quit
[HUAWEI] bfd test bind peer-ipv6 2001::1 vpn6-instance vpn1 interface gigabitethernet 0/0/1
[HUAWEI-bfd-session-test] discriminator local 1
[HUAWEI-bfd-session-test] discriminator remote 2
[HUAWEI-bfd-session-test] commit
```

19.10.1.2 display bfd statistics session (upgrade-compatible command)


### `DLDP Compatible Commands`

> **Página:** 113 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The dldp authentication-mode md5-compatible command configures MD5- compatible authentication. By default, DLDP packets are not authenticated.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
dldp authentication-mode md5-compatible md5-password
```

**Parameters:**

- `md5-compatible md5- password` — Uses MD5-compatible to authenticate DLDP packets exchanged between the interfaces on the local and neighbor devices.md5- password specifies the MD5-compatible authentication password. NOTE To ensure security, the password is saved in cipher text in the configuration file. — *Valores:* The value is a string of 1 to 16 case-sensitive characters in plain text without any question mark (?) and space. NOTE During the upgrade, the device is compatible with the cipher-text passwords with different lengths before the upgrade.

**Usage Guidelines:**

Scenario This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. When the device that uses MD5 authentication is upgraded from V200R001 or V200R002 to V200R008 or later, to ensure compatibility, upgrade the DLDP authentication mode to MD5-compatible. Running the dldp authentication-mode md5-compatible command is equivalent to running the dldp authentication-mode command in the system view.


### `Ethernet OAM Compatible Commands`

> **Página:** 115 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent trap enable test-packet command enables an Ethernet OAM module to send traps to the NMS. By default, an Ethernet OAM module is enabled to send traps to the NMS.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent trap enable test-packet
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. It is replaced by the snmp-agent trap enable feature-name efm command.


## User Access and Authentication Compatible Commands

19.11.1 AAA Compatible Commands 19.11.2 NAC Compatible Commands

### `AAA Compatible Commands`

> **Página:** 125 · **Views (Modo):** RADIUS server template view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The radius-server user-name domain-included force command configures the device encapsulate the domain name in the user name in RADIUS packets to be sent to a RADIUS server.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
radius-server user-name domain-included force
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. Its function is the same as that of the radius-server user-name domain-included command.


### `NAC Compatible Commands`

> **Página:** 142 · **Views (Modo):** VLANIF interface view, Ethernet interface view, GE interface view, XGE interface view, 40GE interface view, Eth-Trunk interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The web-auth-server command binds a Portal server template to an interface. The undo web-auth-server command unbinds a Portal server template from an interface. By default, no Portal server template is bound to an interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
● Layer 2 interface view
web-auth-server server-name [ bak-server-name ] direct
undo web-auth-server [ server-name [ bak-server-name ] direct ]
● VLANIF interface view
web-auth-server server-name [ bak-server-name ] { direct | layer3 }
undo web-auth-server [ server-name [ bak-server-name ] { direct | layer3 } ]
● Routed main interface view
web-auth-server server-name [ bak-server-name ] layer3
undo web-auth-server [ server-name [ bak-server-name ] layer3 ]
```

**Parameters:**

- `server-name` — Specifies the name of the Portal server template. — *Valores:* The value must be an existing Portal server template name.
- `bak-server- name` — Specifies the name of the secondary Portal server template. NOTE The name of the secondary Portal server template cannot be configured to the command-line keywords direct and layer3. — *Valores:* The value must be an existing Portal server template name.
- `direct` — Specifies Layer 2 authentication as the Portal authentication mode. When there is no Layer 3 forwarding device between the device and users, configure the Layer 2 authentication mode. — *Valores:* -
- `layer3` — Specifies Layer 3 authentication as the Portal authentication mode. When there is a Layer 3 forwarding device between the device and users, configure the Layer 3 authentication mode. — *Valores:* -

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After the upgrade, this command is no longer supported, and it is replaced by the web-auth-server server-name [ bak-server-name ] { direct | layer3 } command in the portal access profile view.

**Example:**

```text
# Configure voice VLAN 100 in the service scheme huawei.
<HUAWEI> system-view
[HUAWEI] aaa
[HUAWEI-aaa] service-scheme huawei
[HUAWEI-aaa-service-huawei] voice-vlan 100
```

19.11.2.44 web-auth-server (interface view) (upgrade-compatible


## Security Compatible Commands

19.12.1 ACL Compatible Commands 19.12.2 Local Attack Defense Compatible Commands 19.12.3 Attack Defense Compatible Commands 19.12.4 Traffic Suppression Compatible Commands 19.12.5 ARP Security Compatible Commands 19.12.6 DHCP Snooping Compatible Commands 19.12.7 Keychain Upgrade-compatible Commands 19.12.8 PKI Compatible Commands

### `ACL Compatible Commands`

> **Página:** 190 · **Views (Modo):** Advanced ACL6 view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The rule command adds or modifies advanced ACL6 rules.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
rule [ rule-id ] { deny | permit } ipv6-ah [ destination { destination-ipv6-address
prefix-length | destination-ipv6-address/prefix-length | destination-ipv6-address
postfix postfix-length | any } | dscp dscp | fragment | logging | precedence
precedence | source { source-ipv6-address prefix-length | source-ipv6-address/
prefix-length | source-ipv6-address postfix postfix-length | any } | time-range
time-name | tos tos | vpn-instance vpn-instance-name ] *
rule [ rule-id ] { deny | permit } ipv6-esp [ destination { destination-ipv6-
address prefix-length | destination-ipv6-address/prefix-length | destination-ipv6-
address postfix postfix-length | any } | dscp dscp | fragment | logging |
precedence precedence | source { source-ipv6-address prefix-length | source-ipv6-
address/prefix-length | source-ipv6-address postfix postfix-length | any } | time-range time-name | tos tos | vpn-instance vpn-instance-name ] *
```

**Parameters:**

- `rule-id` — Indicates the ID of an ACL6 rule. — *Valores:* The value ranges from 0 to 2047. ● If the ID of a rule is specified and the rule exists, the new rule is added to the rule with this ID, that is, the old rule is modified. ● If the rule associated with a rule ID does not exist, a rule can be created with this rule ID and its position in the ACL is determined by the rule ID. ● If no rule ID is specified, the device allocates an ID to the new rule. The rule IDs are sorted in ascending order.
- `deny` — Discards packets that do not match ACL rules. — *Valores:* -
- `permit` — Allows packets to pass. — *Valores:* -
- `ipv6-ah` — Indicates the protocol type. — *Valores:* -
- `ipv6-esp` — Indicates the protocol type. — *Valores:* -
- `destination { destination -ipv6- address prefix- length | destination- ipv6- address/ prefix- length | any }` — Indicates the destination address and prefix of a packet. — *Valores:* destination-ipv6-address is expressed in hexadecimal notation. The value of prefix-length is an integer that ranges from 1 to 128. You can also use any to represent any destination address.
- `destination destination- ipv6-address postfix postfix- length` — Indicates the destination address and the length of destination address postfix. — *Valores:* destination-ipv6-address indicates the destination address and is expressed in hexadecimal notation. postfix-length is an integer that ranges from 1 to 64.
- `dscp dscp` — Specifies the value of a Differentiated Services CodePoint (DSCP). — *Valores:* The value ranges from 0 to 63.
- `fragment` — Indicates that the rule is valid for only non-initial fragments. — *Valores:* -
- `logging` — Indicates whether to record logs for packets that meet ACL rules. — *Valores:* Log contents include the ACL rule ID, pass or discard of packets, type of the protocol over IP, source or destination address, source or destination port number, and number of packets.
- `precedence precedence` — Filters packets by priority. — *Valores:* The value is a name or a digit that ranges from 0 to 7.
- `source { source- ipv6-address prefix- length | source-ipv6- address/ prefix- length | any }` — Indicates the source address and prefix of a packet. — *Valores:* source-ipv6-address indicates the source address and is expressed in hexadecimal notation. prefix-length is an integer that ranges from 1 to 128. You can also use any to represent any source address.
- `source source-ipv6- address postfix postfix- length` — Indicates the source address and the length of source address postfix. — *Valores:* source-ipv6-address indicates the source address and is expressed in hexadecimal notation. postfix-length is an integer that ranges from 1 to 64.
- `time-range time-name` — Specifies the time range only in which ACL6 rules are effective. time-name indicates the name of the time range. — *Valores:* The value is a string of 1 to 32 characters.
- `tos tos` — Filters packets by Type of Service (ToS). — *Valores:* The value is a name or a digit that ranges from 0 to 15.
- `vpn- instance vpn- instance- name` — Specifies the name of a VPN instance. — *Valores:* The vpn-instance must already exist.

**Usage Guidelines:**

**Usage Scenario**

Advanced ACL6s classify data packets based on the source IP address, destination IP address, source port number, destination port number, and protocol type.

**Prerequisites**

An ACL6 has been created before the rule is configured.

**Precautions**

If the specified rule ID already exists and the new rule conflicts with the original rule, the new rule replaces the original rule. To modify an existing rule, delete the old rule, and then create a new rule. Otherwise, the configuration result may be incorrect. When you use the undo rule command to delete an ACL6 rule, the rule ID must exist. If the rule ID is unknown, you can use the display acl ipv6 command to view the rule ID. The undo rule command deletes an ACL6 rule even if the ACL6 rule is referenced. Exercise caution when you run the undo rule command.

**Example:**

```text
# Create an advanced ACL6 with ID 3000 and configure a rule that allows only
```

IPv6 ESP packets with the source IPv6 address 2030:5060::9050 and mask 64 to pass.

```text
<HUAWEI> system-view
[HUAWEI] acl ipv6 number 3000
[HUAWEI-acl6-adv-3000] rule 0 permit ipv6-esp source 2030:5060::9050/64
```


### `Local Attack Defense Compatible Commands`

> **Página:** 197 · **Views (Modo):** Attack defense policy view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The deny command sets the discard action taken for packets sent to the CPU. The undo deny command restores the default action taken for packets sent to the CPU. By default, the device limits the rate of protocol packets and user-defined flows based on the CAR configuration.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
deny packet-type bpdu
deny packet-type ftp-dynamic
deny packet-type hotlimit
deny packet-type smlk-rrpp
deny packet-type nac-dhcp
undo deny packet-type bpdu
undo deny packet-type ftp-dynamic
undo deny packet-type hotlimit
undo deny packet-type smlk-rrpp
undo deny packet-type nac-dhcp
```

**Parameters:**

- `packet-type bpdu` — Discards bpdu packets . — *Valores:* -
- `packet-type ftp-dynamic` — Discards ftp-dynamic packets. — *Valores:* -
- `packet-type hotlimit` — Discards hop-limit packets. — *Valores:* -
- `packet-type smlk-rrpp` — Discards smlk-rrpp packets. — *Valores:* -
- `packet-type nac-dhcp` — Discards nac-dhcp packets. — *Valores:* -

**Usage Guidelines:**

If you run the deny and car commands for the same type of packets sent to the CPU, the command that runs later takes effect. The undo deny command restores the default action taken for packets sent to the CPU. After you run this command, the system limits the rate of packets sent to the CPU based on the configured CIR and CBS values.

**Example:**

```text
# Set the discard action taken for bpdu packets sent to the CPU attack in defense
```

policy test.

```text
<HUAWEI> system-view
[HUAWEI] cpu-defend policy test
[HUAWEI-cpu-defend-policy-test] deny packet-type bpdu
```


### `Attack Defense Compatible Commands`

> **Página:** 200 · **Views (Modo):** System view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The application-apperceive default drop command enables the device to discard the received packets when no matching application layer association policy exists. The undo application-apperceive default drop command enables the device to deliver the received packets to the upper layer when no matching application layer association policy exists. By default, the device is enabled to deliver the received packets to the upper layer when no matching application layer association policy exists.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
application-apperceive default drop
undo application-apperceive default drop
```

**Usage Guidelines:**

After the application-apperceive default drop command is run, if a protocol is not enabled in the system view nor in the interface view, the device discards all the packets of this protocol type.

**Example:**

```text
# Enable the device to discard the received packets when no matching application
```

layer association policy exists.

```text
<HUAWEI> system-view
[HUAWEI] application-apperceive default drop
```


### `Traffic Suppression Compatible Commands`

> **Página:** 201 · **Views (Modo):** Ethernet interface view, GE interface view, XGE interface view, port group view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The storm-control action sets the storm control action to shutdown. The undo storm-control action command cancels the configuration. By default, no storm control action is configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
storm-control action shutdown
undo storm-control action
```

**Parameters:**

- `shutdown` — Shuts down an interface. — *Valores:* -

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can be run when it is entered in full. It is replaced by the storm-control action error-down command.

**Example:**

```text
# Configure the storm control action is shutdown on GE0/0/1.
<HUAWEI> system-view
[HUAWEI] interface gigabitethernet 0/0/1
[HUAWEI-GigabitEthernet0/0/1] storm-control action shutdown
```


### `ARP Security Compatible Commands`

> **Página:** 205 · **Views (Modo):** Ethernet interface view, GE interface view, XGE interface view, 40GE interface view, MultiGE interface view, Eth-Trunk interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The arp filter source command enables ARP gateway protection for the specified IP address. The undo arp filter source command disables ARP gateway protection for the specified IP address. By default, ARP gateway protection is disabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
arp filter source ip-address
undo arp filter source { ip-address | all }
```

**Parameters:**

- `ip-address` — Specifies the protected gateway IP address. — *Valores:* The value is in dotted decimal notation.
- `all` — Disables ARP gateway protection for all IP addresses in the current view. — *Valores:* -

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After the upgrade, it is replaced by the arp trust source command.

**Example:**

```text
# Configure GE0/0/1 to allow 200 ARP packet to pass through in 10 seconds, and
```

configure GE0/0/1 to discard all ARP packets in 60 seconds when the number of ARP packets exceeds the limit.

```text
<HUAWEI> system-view
[HUAWEI] interface gigabitethernet 0/0/1
[HUAWEI-GigabitEthernet0/0/1] arp anti-attack rate-limit enable
[HUAWEI-GigabitEthernet0/0/1] arp anti-attack rate-limit 200 10 block timer 60
```

19.12.5.2 arp filter source (upgrade-compatible command)


### `DHCP Snooping Compatible Commands`

> **Página:** 208 · **Views (Modo):** Ethernet interface view, GE interface view, XGE interface view, Eth-Trunk interface view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** The dhcp snooping trusted no-user-binding command configures an interface as the trusted interface. The undo dhcp snooping trusted no-user-binding command restores the default state of an interface. By default, no trusted interface is configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
dhcp snooping trusted no-user-binding
undo dhcp snooping trusted no-user-binding
```

**Usage Guidelines:**

When DHCP snooping is enabled on an interface, the interface is an untrusted interface by default. After you use the dhcp snooping trusted no-user-binding command in the interface view, the interface becomes a trusted interface. This command can only be used during a configuration restoration.

**Example:**

```text
# Configure a trusted interface GE0/0/1.
<HUAWEI> system-view
[HUAWEI] dhcp enable
[HUAWEI] dhcp snooping enable
[HUAWEI] interface gigabitethernet 0/0/1
[HUAWEI-GigabitEthernet0/0/1] dhcp snooping trusted no-user-binding
```


### `Keychain Upgrade-compatible Commands`

> **Página:** 229 · **Views (Modo):** Key-ID view · **Default Level (Privilégio):** 2: Configuration Level · **Leitura (display/show):** não

**Description (Function):** The send-time command makes a key act as a send key for the specified interval of time. The undo send-time command deletes the send-time configuration. By default, no send-time is configured.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
send-time utc start-time start-date { duration { duration-value | infinite } | { to
end-time end-date } }
```

**Parameters:**

- `utc` — Specifies that the given time is in Coordinated Universal Time (UTC) format. — *Valores:* -
- `start-time` — Specifies the start send time. — *Valores:* In HH:MM format. The value ranges from 00:00 to 23:59.
- `start-date` — Specify the start date. — *Valores:* In YYYY-MM-DD format. The value ranges from 1970-01-01 to 2050-12-31.
- `duration duration-value` — Specifies the duration of the send time in minutes. — *Valores:* The value ranges from 1 to 26280000.
- `infinite` — Specifies that the key will be acting as a send key forever from the configured start-time. — *Valores:* -
- `to` — Acts as a separator. — *Valores:* -
- `end-time` — Specifies the end send time. — *Valores:* In HH:MM format. The value ranges from 00:00 to 23:59. The end-time should be greater than the start-time.
- `end-date` — Specifies the end date. — *Valores:* In YYYY-MM-DD format. The value ranges from 1970-01-01 to 2050-12-31.
- `daily` — Specifies the daily send timing for the given key. — *Valores:* -

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. It is replaced by the send-time start-time start-date { duration { duration-value | infinite } | { to end-time end-date } } command.


### `PKI Compatible Commands`

> **Página:** 232 · **Views (Modo):** PKI realm view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The usage command configures the purpose description for a certificate public key. By default, a certificate public key does not have a purpose description.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
usage { ike | ssl-client | ssl-server } *
```

**Parameters:**

- `ike` — Specifies the usage of a key as ike. That is, the key is used to set up an IPSec tunnel. — *Valores:* -
- `ssl-client` — Specifies the usage of a key as ssl- client. That is, the key is used by the SSL client to set up an SSL session. — *Valores:* -
- `ssl-server` — Specifies the usage of a key as ssl- server. That is, the key is used by the SSL server to set up an SSL session. — *Valores:* -

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After the upgrade, this command is no longer supported, and it is replaced by the key-usage { ike | ssl-client | ssl-server } * command.


## QoS Compatible Commands

19.13.1 count (upgrade-compatible command)

### `count (upgrade-compatible command)`

> **Página:** 235 · **Views (Modo):** Traffic behavior view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** Using the count command, you can enable the function of counting packets that match traffic classification rules. By default, the counting function is disabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
count
```

**Usage Guidelines:**

When there are many traffic classification rules on the switch, you can run the count command to count the specific traffic. The counting start time is the time when the policy is applied. Currently, the switch counts packets rather than bytes.

**Example:**

```text
# Configure the traffic policy p1 so that the switch counts packets that flow
```

through GigabitEthernet 0/0/1. After a period of time, the switch displays the traffic statistics.

```text
<HUAWEI> system-view
[HUAWEI] traffic classifier c1
[HUAWEI-classifier-c1] if-match any
[HUAWEI-classifier-c1] quit
[HUAWEI] traffic behavior b1
[HUAWEI-behavior-b1] count
[HUAWEI-behavior-b1] quit
[HUAWEI] traffic policy p1
[HUAWEI-trafficpolicy-p1] classifier c1 behavior b1
[HUAWEI-trafficpolicy-p1] quit
[HUAWEI] interface gigabitethernet 0/0/1
[HUAWEI-GigabitEthernet0/0/1] traffic-policy p1 inbound
[HUAWEI-GigabitEthernet0/0/1] display traffic policy interface gigabitethernet 0/0/1
Interface: GigabitEthernet0/0/1
Direction: Inbound
Policy: p1
Classifier: c1
Rule(s) : if-match any
Behavior: b1
Count
Matched : 10 (Packets)
```


## Network Management Compatible Commands

19.14.1 SNMP Compatible Commands 19.14.2 NQA Compatible Commands 19.14.3 Mirror Compatible Commands

### `SNMP Compatible Commands`

> **Página:** 236 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The snmp-agent usm-user command adds a user to an SNMP user group. The undo snmp-agent usm-user command deletes a user from an SNMP user group. By default, the SNMP user group has no users added. NOTE It is recommended that you deliver the snmp-agent usm-user v3 user-name group-name authentication-mode { md5 | sha } password [ privacy-mode { des56 | aes128 | aes192 | aes256 | 3des } encrypt-password ] [ acl acl-number ] to the switch from the NMS. Do not directly configure the command on the switch.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
snmp-agent usm-user v3 user-name group-name simple [ authentication-mode
{ md5 | sha } password [ privacy-mode { des56 | aes128 | aes192 | aes256 |
3des } encrypt-password ] ] [ acl acl-number ]
snmp-agent usm-user v3 user-name group-name [ cipher ] [ authentication-mode { md5 | sha } password [ privacy-mode { des56 | aes128 | aes192 | aes256
| 3des } encrypt-password ] ] [ acl acl-number ]
undo snmp-agent usm-user v3 user-name group-name [ engineid engineid |
local ]
```

**Parameters:**

- `v3` — Indicates that the security mode in SNMPv3 is adopted. — *Valores:* -
- `user-name` — Specifies the name of a user. — *Valores:* It is a string of 1 to 32 case-sensitive characters without spaces.
- `group-name` — Specifies the name of the group to which a user belongs. — *Valores:* It is a string of 1 to 32 case-sensitive characters without spaces.
- `simple` — Indicates the simple authentication. — *Valores:* -
- `cipher` — Specifies that the password is in ciphertext, which is the default password type. If this parameter is specified, you can enter only a password in ciphertext. This type of password can be viewed using the configuration file. — *Valores:* -
- `authentication- mode` — Sets the authentication mode. NOTE Authentication is a process in which the SNMP agent (or the NMS) confirms that the message is received from an authorized NMS (or SNMP agent) and the message is not changed during transmission. RFC 2104 defines Keyed-Hashing for Message Authentication Code (HMAC), an effective tool that uses the security hash function and key to generate the message authentication code. This tool is widely used in the Internet. HMAC used in SNMP includes HWAC-MD5-96 and HWAC- SHA-96. The hash function of HWAC-MD5-96 is MD5 that uses 128-bit authKey to generate the key. The hash function of HWAC-SHA-96 is SHA-1 that uses 160-bit authKey to generate the key. — *Valores:* -
- `md5 | sha` — Indicates the authentication protocol. ● md5: Specifies HMAC-MD5-96 as the authentication protocol. ● sha: Specifies HMAC-SHA-96 as the authentication protocol. — *Valores:* -
- `password` — Specifies the password for user authentication. — *Valores:* For plain-text password, the value is a string of 6 to 64 characters by default, and the minimum length is 6 characters. If the set password min-length command is run to set the minimum length of passwords to a value greater than 6, the minimum length is the value configured using the set password min- length command. For cipher-text password, the value is a string of 32 to 104 characters. NOTE The password cannot be the same as the user name or reverse of the user name. The password must contain at least two types of characters, including letters, digits, and special characters. The special characters cannot be question mark (?) or space.
- `privacy-mode` — Specifies the authentication with encryption. The system adopts the cipher block chaining (CBC) code of the data encryption standard (DES) and uses 128-bit privKey to generate the key. The NMS uses the key to calculate the CBC code and then adds the CBC code to the message while the SNMP agent fetches the authentication code through the same key and then obtains the actual information. Like the identification authentication, the encryption requires the NMS and the SNMP agent to share the same key to encrypt and decrypt the message. — *Valores:* -
- `des56 | aes128 | aes192 | aes256 | 3des` — Indicates the encryption protocol. — *Valores:* -
- `encrypt-password` — Indicates the encryption password. — *Valores:* For plain-text password, the value is a string of 6 to 64 characters by default, and the minimum length is 6 characters. If the set password min-length command is run to set the minimum length of passwords to a value greater than 6, the minimum length is the value configured using the set password min- length command. For cipher-text password, the value is a string of 32 to 104 characters. NOTE The password cannot be the same as the user name or reverse of the user name. The password must contain at least two types of characters, including letters, digits, and special characters. The special characters cannot be question mark (?) or space.
- `acl acl-number` — Specifies the ACL number of the access view. — *Valores:* The value is an integer that ranges from 2000 to 2999.
- `engineid engineid` — Specifies the ID of the engine associated with a user. — *Valores:* The value is a string of 10 to 64 case-insensitive characters without spaces.
- `local` — Indicates the local entity user. — *Valores:* -

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade.


### `NQA Compatible Commands`

> **Página:** 244 · **Views (Modo):** NQA view · **Default Level (Privilégio):** 2: Configuration level · **Leitura (display/show):** não

**Description (Function):** Using the send-trap overthreshold command, you can configure conditions for sending trap messages. Using the undo send-trap overthreshold command, you can delete the previous configuration. By default, the device is disabled from sending traps.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
send-trap overthreshold
undo send-trap overthreshold
```

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can only be run during the configuration restoration phase of the upgrade. After the upgrade, this command is no longer supported, and it is replaced by the send-trap rtd command.


### `Mirror Compatible Commands`

> **Página:** 244 · **Views (Modo):** Traffic behavior view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The port-mirroring command configures a mirroring behavior on an interface.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
port-mirroring to observe-port index
```

**Parameters:**

- `index` — Specifies the index of a global observing interface. — *Valores:* The value is integer.

**Usage Guidelines:**

This command is available to aid upgrade compatibility. It can be run when it is entered in full.

**Example:**

```text
# Mirror traffic to observing interface with index 1.
<HUAWEI> system-view
[HUAWEI] traffic behavior b1
[HUAWEI-traffic-behavior-b1] port-mirroring to observe-port 1
```
