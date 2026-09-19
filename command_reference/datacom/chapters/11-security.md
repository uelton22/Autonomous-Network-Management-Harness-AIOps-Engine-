# Capítulo 11: Security

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## AAA

### `aaa authentication-next-method-on-fail`

> **Página:** 1400 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Command to instruct AAA to use the next authentication method defined in the authentication order list, even when the current method returns a FAIL response. By default, AAA proceeds to the next authentication method only when there is an ERROR, which means that the security server has not responded to an authentication query. Because of this, no authentication has been attempted. A FAIL response means that the user has not met the criteria contained in the security server authentication database to be successfully authenticated. In order to force local user authentication in this situation, for example, authentication-next-method-on-fail must be enabled and local authentication must be present in the authentication order list.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
aaa authentication-next-method-on-fail
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.0.0 | This command was introduced. |

**Usage Guidelines:**

Example: This example shows how to enable the flag.

```text
DM4160# config
Entering configuration mode terminal
DM4610(config)# aaa authentication-next-method-on-fail
```

**Impacts and precautions:**

For local authentication, the next method is always tried on failure. But it is not recommended to use local before other methods on the authentication order list.

**Hardware restrictions:**

N/A


### `aaa authentication-order`

> **Página:** 1402 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Command to set user authentication Order. The order must be set using brackets and separated by spaces.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
aaa authentication-order { local | radius | tacacs }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `local` — Configure authentication order to authenticate user locally. — *Valores:* N/A. · *Default:* N/A.
- `radius` — Configure authentication order to authenticate user against a remote radius server. — *Valores:* N/A. · *Default:* N/A.
- `tacacs` — Configure authentication order to authenticate user against a remote tacacs server. — *Valores:* N/A. · *Default:* N/A.

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 2.4 | Added note for local authentication when the user is not present. |
| 1.4 | This command was introduced. |

**Usage Guidelines:**

After configuring the remote servers, authentication order must be set to determine in which order users will be authenticated. Using brackets allows user to replace older configurations. Example: This example shows how to set authentication order.

```text
DM4160# config
Entering configuration mode terminal
```

DM4610(config)# aaa authentication-order [ local radius tacacs ]

**Impacts and precautions:**

For local authentication when the user is not present the next authentication method will be attempted. For radius or tacacs the next method is used only if there is no connection to the server.

**Hardware restrictions:**

N/A


### `aaa authentication-type`

> **Página:** 1405 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Configures the authentication type for remote servers.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
aaa authentication-type tacacs { pap | ascii }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `tacacs` — Configures authentication type for TACACS servers. — *Valores:* { pap | ascii } · *Default:* pap

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 4.2.0 | This command was introduced. |

**Usage Guidelines:**

To authenticate users using TACACS the correct authentication type must be selected. The selected authentication type will be applied to all TACACS servers. Example: This example shows how to configure the authentication type.

```text
DM4160# config
Entering configuration mode terminal
```

DM4610(config)# aaa authentication-type tacacs ascii

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `aaa server radius`

> **Página:** 1407 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Configure an (AAA) authentication, authorization and accounting remote RADIUS server.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
aaa server radius server name host IPv4address|IPv6address shared-secret secret [ authentication ] [ accounting ] [ retries number of retries ] [ authentication-port port number ] [ accounting-port port number ] [ source { ipv4 address IPv4address | ipv6 address IPv6address | interface interface-name } ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `server name` — Configures a name for the RADIUS server. — *Valores:* String with with maximum length of 64 · *Default:* None
- `host IPv4address or IPv6address` — Configures an address for the server. — *Valores:* a.b.c.d (IPv4) or x:x:x:x::x (IPv6) · *Default:* None
- `shared-secret secret` — Configures a secret that is shared with the server and used to validate the transaction. — *Valores:* String with maximum length of 128 · *Default:* N/A.
- `authentication` — Enables remote user authentication via authentication server, it will also enable authorization. — *Valores:* N/A · *Default:* N/A
- `accounting` — Enables remote accounting via accounting server. — *Valores:* N/A · *Default:* N/A
- `retries number of retries` — Configures server communication retries. — *Valores:* 1-5 · *Default:* 3
- `authentication-port port number` — Configures server authentication port to allow communication. — *Valores:* 0-65535 · *Default:* 1812
- `accounting-port port number` — Configures server accounting port to allow communication. — *Valores:* 0-65535 · *Default:* 1813
- `source ipv4 address IPv4address` — Specifies the source IPv4 address from which Radius server connection will be established. — *Valores:* a.b.c.d · *Default:* None
- `source ipv6 address IPv6address` — Specifies the source IPv6 address from which Radius server connection will be established. — *Valores:* x:x:x:x::x · *Default:* None
- `source interface interface-name` — Specifies the interface whose IP address will be used for all outgoing RADIUS packets. Interface must have an IPv4 or IPv6 address configured and cannot be associated with a VRF. — *Valores:* Interface name in format l3-<name> or loopback-<id>. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |
| 5.0 | Added support for source IPv4 address. |
| 10.2 | Added support for host and source IPv6 address. |

**Usage Guidelines:**

Configure remote servers before remote authentication can be enabled. Example: This example shows how to set a remote Radius server using an IPv4.

```text
DM4160# config
Entering configuration mode terminal
```

DM4610(config)# aaa server radius rad01 DM4610(config-radius-rad01)# host 10.1.1.1 DM4610(config-radius-rad01)# shared-secret dmos-radius DM4610(config-radius-rad01)# authentication DM4610(config-radius-rad01)# accounting Example: This example shows how to set a remote Radius server using an IPv6.

```text
DM4160# config
Entering configuration mode terminal
```

DM4610(config)# aaa server radius rad01 DM4610(config-radius-rad01)# host cafe::2 DM4610(config-radius-rad01)# shared-secret dmos-radius DM4610(config-radius-rad01)# authentication DM4610(config-radius-rad01)# accounting Example: This example shows how to configure an IPv4 source address for a remote Radius server.

```text
DM4160# config
Entering configuration mode terminal
```

DM4610(config)# aaa server radius rad01 DM4610(config-radius-rad01)# source ipv4 address 1.1.1.1 Example: This example shows how to configure an IPv6 source address for a remote Radius server.

```text
DM4160# config
Entering configuration mode terminal
```

DM4610(config)# aaa server radius rad01 DM4610(config-radius-rad01)# source ipv6 address c01a:c4f3::3

**Impacts and precautions:**

If the IPv4/IPv6 source address parameter is not a configured IPv4/IPv6 address of any interface, the Radius requests will not be sent to the server.

**Hardware restrictions:**

None


### `aaa server tacacs`

> **Página:** 1411 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Configures a remote TACACS+ server.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
aaa server tacacs server name host IPv4address|IPv6address shared-secret secret [ authentication ] [ authorization ] [ accounting ] [ timeout timeout time ] [ authentication-port port number ] [ authentication-type type ] [ source { ipv4 address IPv4address | ipv6 address IPv6address | interface interface-name } ] [ vrf vrf-name]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `server name` — Configures a name for the TACACS+ server. — *Valores:* String with with maximum length of 64 · *Default:* N/A
- `host IPv4address or IPv6address` — Configures an address for the server. — *Valores:* a.b.c.d (IPv4) or x:x:x:x::x (IPv6) · *Default:* N/A
- `shared-secret secret` — Configures a secret that is shared with the server and used to validate the transaction. — *Valores:* String with maximum length of 128 · *Default:* N/A
- `authentication` — Enables remote user authentication. — *Valores:* N/A · *Default:* N/A
- `authorization` — Enables remote user commands authorization. — *Valores:* N/A · *Default:* N/A
- `accounting` — Enables remote user commands accounting. — *Valores:* N/A · *Default:* N/A
- `timeout timeout time` — Configures server communication timeout. — *Valores:* 0-255 · *Default:* 5
- `authentication-port port number` — Configures server authentication port to allow communication. — *Valores:* 0-65535 · *Default:* tacacs: 49
- `authentication-type type` — The authentication encryption type requested from TACACS+ server. — *Valores:* { pap | ascii } · *Default:* pap
- `source ipv4 address IPv4address` — Specifies the source IPv4 address from which TACACS+ server connection will be established. — *Valores:* a.b.c.d · *Default:* None
- `source ipv6 address IPv6address` — Specifies the source IPv6 address from which TACACS+ server connection will be established. — *Valores:* x:x:x:x::x · *Default:* None
- `source interface interface-name` — Specifies the interface whose IP address will be used for all outgoing TACACS+ packets. Interface must have an IPv4 or IPv6 address configured and cannot be associated with a VRF In the case a loopback interface is selected and it belongs to a VRF, it’s needed to configure the VRF parameter too. — *Valores:* Interface name in format l3-<name> or loopback-<id>. · *Default:* None
- `vrf vrf-name` — Specifies the VRF used for all outgoing TACACS+ packets. VRF mgmt is not supported yet. — *Valores:* VRF name. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. |
| 4.0 | Added support for authorization and up to 5 servers. |
| 4.6 | Added support for accounting. |
| 5.0 | Added support for source interface. |
| 6.0 | Added support to interface loopback in VRF. |
| 10.2 | Added support for host and source IPv6 address. |

**Usage Guidelines:**

The remote servers must be previously configured before enabling the remote authentication on the equipment. The system supports up to 5 TACACS+ servers, that means 4 redundant servers. Once a server is reached for authorization, this server will be preferred for the command authorization until it is unreachable. If this server becomes unreachable the list of servers will be inspected to return the next available server for authorization. When there is a TACACS+ server with authentication and without authorization configured, the authorization level will be performed by user group. This group is mapped from the user privilege level present in the TACACS+ server used for authentication. Example: This example shows how to set a remote TACACS+ server for authentication, authorization and accounting services, using an IPv4.

```text
# config
Entering configuration mode terminal
(config)# aaa server tacacs tac01
(config-tacacs-tac01)# host 10.1.1.1
(config-tacacs-tac01)# shared-secret dmos-tacacs
(config-tacacs-tac01)# authentication
(config-tacacs-tac01)# authorization
(config-tacacs-tac01)# accounting
(config-tacacs-tac01)# commit
```

Example: This example shows how to set a remote TACACS+ server for authentication, authorization and accounting services, using an IPv6.

```text
# config
Entering configuration mode terminal
(config)# aaa server tacacs tac01
(config-tacacs-tac01)# host 2001:db8:85a3::8a2e:370:7334
(config-tacacs-tac01)# shared-secret dmos-tacacs
(config-tacacs-tac01)# authentication
(config-tacacs-tac01)# authorization
(config-tacacs-tac01)# accounting
(config-tacacs-tac01)# commit
```

Example: This example shows how to configure an IPv6 source address for a remote TACACS server.

```text
DM4160# config
Entering configuration mode terminal
```

DM4610(config)# aaa server tacacs tac01 DM4610(config-tacacs-tac01)# source ipv6 address c0c4:c01a::1 Example: This example shows how to use insert to add new server with the desired priority.

```text
(config)# insert aaa server tacacs tac3 before tac2
(config)# aaa server tacacs tac3 host 3.3.3.3 shared-secret 3333
(config-tacacs-tac3)# commit
```

Commit complete.

```text
(config-tacacs-tac3)#
(config)# show aaa server
aaa server tacacs tac1
host 1.1.1.1
shared-secret $7$kkfWsrXallbrgAQDad3S7w==
!
aaa server tacacs tac3
host 3.3.3.3
shared-secret $7$oSm7YUa2o6c+secJrARZhQ==
!
aaa server tacacs tac2
host 2.2.2.2
shared-secret $7$IVkBhwucZ66bhXM+00Vzzw==
!
```

Example: This example shows how to use move to change the server priority.

```text
(config)# move aaa server tacacs tac1 last
(config)# commit
```

Commit complete.

```text
(config)# show aaa server
aaa server tacacs tac3
host 3.3.3.3
shared-secret $7$oSm7YUa2o6c+secJrARZhQ==
!
aaa server tacacs tac2
host 2.2.2.2
shared-secret $7$IVkBhwucZ66bhXM+00Vzzw==
!
aaa server tacacs tac1
host 1.1.1.1
shared-secret $7$kkfWsrXallbrgAQDad3S7w==
!
```

Example: These examples show how to configure TACACS server to use a specific VRF.

```text
(config)# aaa server tacacs tacacs2 host 60.1.1.3 vrf green
(config)# commit
(config)# aaa server tacacs tacacs1 host 60.1.1.3 vrf green source interface loopback-1
(config)# commit
```

**Impacts and precautions:**

It is not recommended the configuration of the same user on both local host and remote authentication server when the group permission is different. Otherwise, the user authentication will be done and its privilege level will follow the higher permission. Currently, commands authorization and accounting via NETCONF are not supported. However, the authorization and accounting level will be performed by user group. This group is based on the user privilege level present in the TACACS+ server used for authentication. A privilege level of 15 is mapped to the admin group, otherwise the user is mapped to the audit group. It’s not possible to use multiple TACACs servers on different VRFs.

**Hardware restrictions:**

N/A


### `aaa user`

> **Página:** 1417 · **Modo:** Configuration mode · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** The AAA user command is used to create local users to access the device.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
aaa user username [change-password new-password new password old-password old password confirm-password confirm password] password password [group {admin|config|audit}] [ssh-public-key {public_key_file_name}]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `username` — Set a local user name. — *Valores:* String with maximum length of 64 · *Default:* None
- `new password` — New user password. — *Valores:* The password string should match the following rules: • The password must contain at least one number • The password must contain at least one lowercase letter • The password must contain at least one uppercase letter • The password must be at least 8 characters long • The password cannot be longer than 64 characters · *Default:* None
- `old password` — Old user password. — *Valores:* String with unlimited length · *Default:* None
- `confirm password` — Same as the old user password. — *Valores:* String with unlimited length · *Default:* None
- `password password` — Defines a user password. — *Valores:* The password string should match the following rules: • The password must contain at least one number • The password must contain at least one lowercase letter • The password must contain at least one uppercase letter • The password must be at least 8 characters long • The password cannot be longer than 64 characters · *Default:* None
- `group group` — Set a local privilege group for the new user. — *Valores:* { admin | config | audit } · *Default:* audit
- `ssh-public-key public_key_file_name` — Set a ssh public key to be used as the authentication method of the associated user. The ssh public key file must be uploaded separately. — *Valores:* String with maximum length of 64 · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 1.2 | Added group parameter. |
| 9.0 | Added strong password validation. |
| 10.8 | Added ssh-public-key parameter. |
| 11.0 | Removed the obligation of special characters on user passwords. |

**Usage Guidelines:**

Users with admin access can change any user password and every user can change it’s own password. Example: This example shows how to set a local user.

```text
DM4610# config
Entering configuration mode terminal
```

DM4610(config)# aaa user audit password Audit_p4ss group audit Login via serial has a 128 characters limitation to username and 64 for password.

**Impacts and precautions:**

Maximum number of local users are 32.

**Hardware restrictions:**

N/A


### `id`

> **Página:** 1421 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Command to show authenticated user and groups as well as user privilege level

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
id
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |

**Usage Guidelines:**

Example: This example shows the output of the command.

```text
DM4160# id
user = admin(0), gid=0, groups=admin
```

**Output Terms:**

Output Description user Display connected user gid Main group id that the connected user is member of groups Group names that the connected user is member of gids All group ids that the connected user is member of

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show aaa ssh_public_key`

> **Página:** 1423 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** sim

**Description:** Command to show the DmOS users that have a public ssh key configured and their respective authentication statuses. It does not display any information regarding DmOS users that do not have a ssh public key configured.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show aaa ssh_public_key
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 10.8.0 | This command was introduced. |

**Usage Guidelines:**

Example: This example shows the output of the command.

```text
DM4610# show aaa ssh-public-key
User: admin
ssh public key:
filename: my_key.pub
status: active
key code: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCg...
User: another_user
ssh public key:
filename: bad_key.pub
status: invalid-public-key-file
User: one_more_user
ssh public key:
filename: non-existent.pub
status: file-not-found
```

**Output Terms:**

Output Description User Display the DmOS username ssh public Display the file that has been configured for this user as a ssh public key/filename: key. Output Description The status of the ssh public key authentication. It can be one of the following values: • active: Indicates that this user has a public key properly configured and it can be used as an authentication method. • file-not-found: Indicates that the ssh public key has been corssh public rectly configured but the public key file is not present on the key/status: system, the file should be uploaded and the ssh public key configuration of this user must be reapplied. • invalid-public-key-file: Indicates that the ssh public key has been correctly configured, the file is present on DmOS, but it is not a valid public key file. If the status of this ssh public key is active, this field will display the ssh public key/key 40 first characters of the public key, it contains the key cryptography code: and the beginning of the key content.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `who`

> **Página:** 1426 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Command to show all authenticated users currently connected

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

**Usage Guidelines:**

Example: This example shows how to obtain logged users.

```text
DM4160# who
```

Session User Context From Proto Date Mode *12 admin cli 127.0.0.1 console 00:03:05 operational

**Output Terms:**

Output Description Session Session number referencing the authenticated user session. User User name of the authenticated user. Context Context in which the user is authenticated(eg.: cli) From Ip address from which the connection was estabilished. Proto Connection protocol being used(eg.: console). Date System time that user has been logged. Mode Command mode that user is using (eg.: operational).

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A PORT SECURITY This topic describes the commands related to management of interface restrictions.


## Port Security

### `anti-ip-spoofing`

> **Página:** 1428 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Anti-ip-spoofing is used for security reasons, it is possible to enable anti-ip-spoofing for a specific interface and add static IP configuration. When anti-ip-spoofing is enabled for an interface just granted traffic will be accepted by device, otherwise it will be dropped. Device considers granted traffic: • ARP packets; • ip-address received by DHCP connections through device; • ip-address configured in allowed-ip list; • PPP connections; • TLS connections; Currently if anti-ip-spoofing is enabled for (ten-)gigabit-ethernet interfaces, it will drop all IP traffic and will accept just following granted traffic: • ARP packets; • ip-address configured in allowed-ip list;

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
anti-ip-spoofing interface interface-name-chassis/slot/port or id allowed-ip ipv4 address ip-address vlan vid mac mac_addr allowed-ip all | ipv4-all | ipv6-all
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `interface interface-name` — Interface where configuration will be applied. Enables anti-ip-spoofing for ethernet interfaces. Anti-ip-spoofing is always enabled for service-ports. — *Valores:* [ten-gigabit-ethernet | gigabit-ethernet | service-port] · *Default:* None.
- `allowed-ip` — Option to configure a static IP rule. — *Valores:* None. · *Default:* None.
- `all` — Inform that all IP addresses in any VLAN will be permitted by device in the interface. — *Valores:* None. · *Default:* None.
- `ipv4-all` — Inform that all IPv4 addresses in any VLAN will be permitted by device. — *Valores:* None. · *Default:* None.
- `ipv6-all` — Inform that all IPv6 addresses in any VLAN will be permitted by device. — *Valores:* None. · *Default:* None.
- `ipv4 address ip-address` — IPv4 address of the client that will be permitted by device. — *Valores:* IPv4 address · *Default:* None.
- `vlan vid` — VLAN of packets that will be permitted by device. — *Valores:* 1-4094 · *Default:* None
- `mac mac-address` — Source MAC address of the client that will be permitted by device. — *Valores:* XX:XX:XX:XX:XX:XX · *Default:* None

**Default:** None.

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. Changed CLI layout for entire anti-ip-spoofing command. 1.6 Added “allowed-ip all” option. Added “allowed-ip ipv4-all” option. 1.10 Added “allowed-ip ipv6-all” option. |

**Usage Guidelines:**

Use the interface option to enable anti-ip-spoofing for a specific interface. Anti-ip-spoofing is always enabled for service-port interfaces, but these interfaces are accepted by anti-ip-spoofing command in order to configure allowed-ip rules. Inside interface node there are the options: allowed-ip ipv4 address, allowed-ip ipv4-all, allowed-ip ipv6-all and allowed-ip all. Using allowed-ip ipv4 address option the traffic with the source IPv4 address and VLAN can pass through the interface. Using allowed-ip ipv4-all option the traffic from any ipv4 and VLAN can pass through the interface. Note that for service-ports just packets from service vlan configured in service-port command will be accepted. Using allowed-ip ipv6-all option the traffic from any ipv6 and VLAN can pass through the interface. Note that for service-ports just packets from service vlan configured in service-port command will be accepted. Using allowed-ip all option the traffic from any ip can pass through the interface (this command is just allowed for service-port interfaces). See usage examples below: To enable anti-ip-spoofing for an interface (i.e: gigabit-ethernet 1/1/1), the following command must be issued. Note that anti-ip-spoofing is always enabled for service-ports.

```text
(config)#
(config)#anti-ip-spoofing
(config-ip-spoofing)#interface gigabit-ethernet-1/1/1
(config-ip-spoofing-gigabit-ethernet-1/1/1)#commit
```

To disable anti-ip-spoofing, the following command must be issued: Please note that all allowed-ip rules of this interface will be removed too.

```text
(config)#
(config)#anti-ip-spoofing
(config-ip-spoofing)#no interface gigabit-ethernet-1/1/1
(config-ip-spoofing)#commit
```

To allow all IPv4 addresses in any VLAN on a gigabit interface, the following command must be issued: Please note that all allowed-ip rules for IPv4 addresses on this interface will be removed too and that all IPv6 addresses will be blocked.

```text
(config)#
(config)#anti-ip-spoofing
(config-ip-spoofing)#interface gigabit-ethernet-1/1/1
(config-ip-spoofing-gigabit-ethernet-1/1/1)#allowed-ip ipv4-all
(config-ip-spoofing-gigabit-ethernet-1/1/1)#commit
```

To allow the client with IPv4 address 10.0.0.1, using VLAN id 10 on the service-port 1, to have the traffic pemitted, the following command must be issued:

```text
(config)#
(config)#anti-ip-spoofing
(config-ip-spoofing)#interface service-port-1
(config-ip-spoofing-service-port-1)#allowed-ip ipv4 address
10.0.0.1 vlan 10
(config-ip-spoofing-service-port-1)#commit
```

To remove an allowed-ip rule, the following command must be issued:

```text
(config)#
(config)#anti-ip-spoofing
(config-ip-spoofing)#interface service-port-1
(config-ip-spoofing-service-port-1)#no allowed-ip ipv4 address
10.0.0.1 vlan 10
(config-ip-spoofing-service-port-1)#commit
```

To allow the traffic from client with IP address 10.0.0.1 and MAC address F0:7D:00:00:00:01, using VLAN id 10 on the service-port 1, the following command must be issued:

```text
(config)#
(config)#anti-ip-spoofing
(config-ip-spoofing-service-port-1)#allowed-ip ipv4 address
10.0.0.1 vlan 10 mac F0:7D:00:00:00:01
(config-ip-spoofing-service-port-1)#commit
```

To allow the client with any IPv4 address on the service-port 2, to have the traffic pemitted, the following command must be issued:

```text
(config)#
(config)#anti-ip-spoofing
(config-ip-spoofing)#interface service-port-2
(config-ip-spoofing-service-port-2)#allowed-ip ipv4-all
(config-ip-spoofing-service-port-2)#commit
```

To allow the traffic from client with any IPv6 address on the service-port 1, the following command must be issued:

```text
(config)#
(config)#anti-ip-spoofing
(config-ip-spoofing)#interface service-port-1
(config-ip-spoofing-service-port-2)#allowed-ip ipv6-all
(config-ip-spoofing-service-port-2)#commit
```

To allow the client with any IP address on the service-port 1, to have the traffic pemitted, the following command must be issued:

```text
(config)#
(config)#anti-ip-spoofing
(config-ip-spoofing)#interface service-port-1
(config-ip-spoofing-service-port-2)#allowed-ip all
(config-ip-spoofing-service-port-2)#commit
```

Note that same effect is achieved by following commands:

```text
(config)#
(config)#anti-ip-spoofing
(config-ip-spoofing)#interface service-port-1
(config-ip-spoofing-service-port-2)#allowed-ip ipv4-all
(config-ip-spoofing-service-port-2)#allowed-ip ipv6-all
(config-ip-spoofing-service-port-2)#commit
```

To check if the configuration was applied, issue the show running-config command:

```text
#show running-config
anti-ip-spoofing
interface service-port-1
allowed-ip ipv4 10.0.0.1 vlan 10
!
interface service-port-2
allowed-ip all
!
!
```

**Impacts and precautions:**

Clients that use static IP address configuration shall have an allowed-ip configuration, otherwise its traffic won’t pass through the device. An interface with anti-ip-spoofing enabled will drop any IP traffic, will just allow ARP packets and traffic with IP addresses configured by allowed-ip or received by DHCP connections. TLS and PPP traffic will not be affected by anti-ip-spoofing configuration. For (ten-)gigabit-ethernet intefaces with anti-ip-spoofing enabled, just ARP packets and traffic with IP addresses configured by allowed-ip will be accepted. Anti-ip-spoofing should not be enabled for interfaces being used as Uplink interfaces, it was designed to be used in access-like interfaces. The misuse of anti-ip-spoofing feature with uplink-like interfaces can stop all traffic on it. Allowed-ip configuration will not work with service-ports without match and action configuration (VLAN translate).

**Hardware restrictions:**

For DM46xx family, the maximum number of allowed IP addresses is 1024. However, this limit is shared with DHCP entries. It means that equipment will be limited to 1024 connections (Static plus DHCP assigned addresses).


### `show allowed-ip`

> **Página:** 1435 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Access level audit · **Leitura (show/display):** sim

**Description:** This command shows the list of allowed ip entries.

**Supported Platforms:** This command is supported only in the following platforms: DM4610, DM4611, DM4612, DM4615, DM4616, DM4618.

**Syntax:**

```text
show allowed-ip [ mac mac-address | vlan vlan id | address ip-adress | interface interface-name-chassis/slot/port | entry-type type | status entry-status ]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `mac mac-address` — MAC address used to filter the output. — *Valores:* [ <XX:XX:XX:XX:XX:XX> MAC Address | all ] · *Default:* N/A
- `vlan vlan-id` — VLAN id used to filter the output. — *Valores:* [<1-4094> VLAN ID | all] · *Default:* N/A
- `address ip-address` — IP address used to filter the output. — *Valores:* [<A.B.C.D> IP Address | all | ipv4-all | ipv6-all] · *Default:* N/A
- `interface interface-name-chassis/slot/port` — Interface used to filter the output. — *Valores:* [ten-gigabit-ethernet | gigabit-ethernet | service-port] · *Default:* N/A
- `entry-type type` — Type of entry to filter the output. — *Valores:* [static | dhcp] · *Default:* N/A
- `status entry-status` — Entry status, indicate if entry is operational or not. — *Valores:* [active | pending] · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.4 | This command was introduced. Added Status column. 1.6 Allowed-ip table layout changed. Added new values: ipv4-all and ipv6-all. 1.10 Allowed-ip table layout changed. |

**Usage Guidelines:**

To simply show the list of all allowed IP entries the following command can be used:

```text
#show allowed-ip
```

It is possible to filter the results by MAC address, IP address, VLAN id, interface, entry type and status. Filter by MAC:

```text
#show allowed-ip mac 44:55:33:22:11:00
```

Filter by IP:

```text
#show allowed-ip address 10.0.0.1
```

Filter by Interface:

```text
#show allowed-ip interface gigabit-ethernet-1/1/1
```

Filter by VLAN:

```text
#show allowed-ip vlan 1100
```

Filter by Entry Type:

```text
#show allowed-ip entry-type static
```

Filter by Status:

```text
#show allowed-ip status active
```

**Output Terms:**

Output Description Display the MAC addresses associated with the allowed IP addresses. MAC-Address IP-Address Display the allowed IP addresses. VLAN Display the VLAN ids associated with the allowed IP entries. Entry-Type Display the Entry Types of the allowed IP entries. Interface Display the Interface on which the respective IP is allowed. Status Display the Status of the allowed IP entries.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A CHAPTER 12: OAM This chapter describes the CLI commands related to Operation, Administration and Management of the DmOS. CONTINUITY CHECK AND FAULT MANAGEMENT This topic describes the commands related to management of fault detection using CFM or Y.1731 such as commands to configure and inspect Maintenance End Points (MEPs), CCM rates or to execute on-demand Ethernet link trace.
