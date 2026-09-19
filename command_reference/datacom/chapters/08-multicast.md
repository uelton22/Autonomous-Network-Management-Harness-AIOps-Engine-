# Capítulo 8: Multicast

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## IGMP Snooping

### `clear multicast igmp snooping statistics`

> **Página:** 1277 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** não

**Description:** Resets IGMP snooping statistics.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
clear multicast igmp snooping statistics { instance [instance-id] | interface [interface-name][instance instance-id] }
```

**Parameters:**

- `instance` — Resets the statistics of the IGMP snooping instance. — *Valores:* N/A · *Default:* N/A
- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface` — Resets the IGMP snooping statistics of an interface. All interfaces will be affected if an interface is not defined. — *Valores:* N/A · *Default:* N/A
- `interface-name` — Name of the interface that will have its statistics cleared. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `instance instance-id` — IGMP snooping instance ID where the interface is configured. — *Valores:* 1-8. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.4 | Command syntax was modified. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: These examples show how to use this command.

```text
# clear multicast igmp snooping statistics instance 1
# clear multicast igmp snooping statistics interface gigabit-ethernet 1/1/1 instance 1
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping`

> **Página:** 1280 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an IGMP snooping instance.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping administrative-status`

> **Página:** 1282 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status on an IGMP snooping instance.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id administrative-status { up | down }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `administrative-status` — Configures the administrative status. — *Valores:* N/A · *Default:* N/A
- `up` — Activates (up) the IGMP snooping instance. — *Valores:* N/A · *Default:* N/A
- `down` — Deactivates (down) the IGMP snooping instance. — *Valores:* N/A · *Default:* N/A

**Default:** up.

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# config terminal
Entering configuration mode terminal
(config)# multicast igmp snooping 1 administrative-status down
(config-igmp-snooping-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping bridge-domain`

> **Página:** 1285 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures a bridge domain on an IGMP snooping instance.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id bridge-domain id bridge-domain-id
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `bridge-domain id bridge-domain-id` — Configures the bridge domain. — *Valores:* N/A · *Default:* N/A
- `id bridge-domain-id` — Bridge domaind ID to be configured on the IGMP snooping instance. — *Valores:* 1-4093. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1 bridge-domain id 1000
(config-igmp-snooping-1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface`

> **Página:** 1287 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an interface on an IGMP snooping instance.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface to be configured on the IGMP snooping instance. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1 interface gigabit-ethernet-1/1/1
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface administrative-status`

> **Página:** 1290 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the desired administrative status on an interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name administrative-status { up | down }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `administrative-status` — Configures the administrative status on the interface. — *Valores:* N/A · *Default:* N/A
- `up` — Activates (up) the interface. — *Valores:* N/A · *Default:* N/A
- `down` — Deactivates (down) the interface. — *Valores:* N/A · *Default:* N/A

**Default:** up.

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# interface gigabit-ethernet-1/1/1
(config-igmp-interface-gigabit-ethernet-1/1/1)# administrative-status down
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface group-limit`

> **Página:** 1293 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the maximum number of multicast groups allowed on an interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name group-limit limit
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `group-limit limit` — Maximum number of groups allowed on the interface. 0 (zero) means unlimited. — *Valores:* 0-3000. · *Default:* N/A

**Default:** 0.

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# interface gigabit-ethernet-1/1/1
(config-igmp-interface-gigabit-ethernet-1/1/1)# group-limit 100
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface ignore`

> **Página:** 1296 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures which version of the IGMP packets should be ignored on an interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name ignore { igmp-v1 | igmp-v2 }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `ignore` — Configures which version of the IGMP packets should be ignored. — *Valores:* N/A · *Default:* N/A
- `igmp-v1` — Configures the interface to ignore IGMPv1 packets. — *Valores:* N/A · *Default:* N/A
- `igmp-v2` — Configures the interface to ignore IGMPv2 packets. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# interface gigabit-ethernet-1/1/1 ignore igmp-v1
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface immediate-leave`

> **Página:** 1299 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the immediate leave on an interface. In immediate leave mode, the group membership on an interface is immediately deleted right after receiving an IGMP Leave message i.e. any group-specific or group-and-source queries is not sent before deleting the entry.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name immediate-leave
```

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `immediate-leave` — Enable the immediate leave on the interface. — *Valores:* N/A · *Default:* N/A

**Default:** Disabled.

**History:**

| Release | Modification |
| --- | --- |
| 1.12 | This command was introduced. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# interface gigabit-ethernet-1/1/1
(config-igmp-interface-gigabit-ethernet-1/1/1)# immediate-leave
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface last-member-query`

> **Página:** 1302 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the interval of time in seconds between the group-specific query messages on an interface. The group-specific-query messages have their Max Response time set to the value of the last member query interval. If no Reports are received after the response time of the last query expires, the group is removed.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name last-member-query interval seconds
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `last-member-query` — Configures the last-member-query. — *Valores:* N/A · *Default:* N/A
- `interval seconds` — Interval of time to be configured on the interface. — *Valores:* 1-25. · *Default:* N/A

**Default:** 1.

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# interface gigabit-ethernet-1/1/1
(config-igmp-interface-gigabit-ethernet-1/1/1)# last-member-query interval 2
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface maximum response time`

> **Página:** 1305 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the maximum response time on an interface. It specifies the maximum allowed time which the host interface is expected to reply to an IGMP General Query message. In addition, it is applied along with other timers to modify the group membership interval (robustness-variable x query-interval + max-response-time).

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name max-response-time seconds
```

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `max-response-time seconds` — The maximum response time to be configured on the interface. — *Valores:* 1-25. · *Default:* N/A

**Default:** 10.

**History:**

| Release | Modification |
| --- | --- |
| 1.12 | This command was introduced. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# interface gigabit-ethernet-1/1/1
(config-igmp-interface-gigabit-ethernet-1/1/1)# max-response-time 15
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface mrouter`

> **Página:** 1308 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures an interface as a multicast router interface, host interface, or capable of being either of them. An interface can learn if it is a router interface by detecting the reception of Query messages.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name mrouter { always | learn-queries | never }
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id. · *Default:* N/A
- `mrouter` — Configures the mrouter option of the interface. — *Valores:* N/A · *Default:* N/A
- `always` — Configures the interface to be a multicast router interface. — *Valores:* N/A · *Default:* N/A
- `learn-queries` — Configures the interface to learn via the detection of Query messages. — *Valores:* N/A · *Default:* N/A
- `never` — Configures the interface to be a host interface. — *Valores:* N/A · *Default:* N/A

**Default:** learn-queries.

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# interface gigabit-ethernet-1/1/1
(config-igmp-interface-gigabit-ethernet-1/1/1)# mrouter always
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface query interval`

> **Página:** 1311 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the query interval on an interface. It specifies the frequency at which the IGMP General Query messages are sent from an interface. In addition, it is applied along with other timers to modify the group membership interval (robustness-variable x query-interval + max-response-time).

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name query-interval seconds
```

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `query-interval seconds` — The query interval to be configured on the interface. — *Valores:* 125-3600. · *Default:* N/A

**Default:** 125.

**History:**

| Release | Modification |
| --- | --- |
| 1.12 | This command was introduced. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# interface gigabit-ethernet-1/1/1
(config-igmp-interface-gigabit-ethernet-1/1/1)# query-interval 300
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface robustness-variable`

> **Página:** 1314 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the value of robustness-variable which allows tuning for the expected packet loss on a subnetwork. The robustness-variable modifies certain IGMP message intervals for IGMPv2 and IGMPv3. By increasing its value, the packet loss tolerance is increased, but the leave latency in the subnetwork is also increased.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name robustness-variable variable
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `robustness-variable variable` — Value of robustness-variable to be configured on the interface. — *Valores:* N/A · *Default:* N/A

**Default:** 2.

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# interface gigabit-ethernet-1/1/1
(config-igmp-interface-gigabit-ethernet-1/1/1)# robustness-variable 5
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `multicast igmp snooping interface version`

> **Página:** 1317 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Configures the IGMP version on an interface.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
multicast igmp snooping instance-id interface interface-name version version
```

**Parameters:**

- `instance-id` — IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface interface-name` — Interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A
- `version version` — IGMP version to be configured on the interface. — *Valores:* 1-3. · *Default:* N/A

**Default:** 3.

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
(config)# multicast igmp snooping 1
(config-igmp-snooping-1)# interface gigabit-ethernet-1/1/1
(config-igmp-interface-gigabit-ethernet-1/1/1)# version 2
(config-igmp-interface-gigabit-ethernet-1/1/1)# commit
```

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show multicast igmp snooping`

> **Página:** 1320 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about IGMP snooping instances.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
show multicast igmp snooping instance-id
```

**Parameters:**

- `instance-id` — Shows information about the specified IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show multicast igmp snooping 1
IGMP Snooping Instance: 1;
```

Bridge Domain: vlan; ID: 2000; Administrative State: enable; Operational state: Up; Interface: gigabit-ethernet-1/1/9; Query Interval (Configured Value): 125 seconds; Query Interval (Value In Use): 125 seconds; Query Maximum Response Time (Configured Value): 10 seconds; Query Maximum Response Time (Value In Use): 10 seconds; Groups Limit: 0; Sources Limit: 0; Robustness (Configured Value): 2; Robustness (Value In Use): 2; Last Member Query Interval (Configured Value): 1 seconds; Last Member Query Interval (Value In Use): 1 seconds; Drop IGMPv1 packets: false; Drop IGMPv2 packets: false; Immediate Leave: false; Query Before Immediate Leave: false; Interface: gigabit-ethernet-1/1/10; Query Interval (Configured Value): 125 seconds; Query Interval (Value In Use): 125 seconds; Query Maximum Response Time (Configured Value): 10 seconds; Query Maximum Response Time (Value In Use): 10 seconds; Groups Limit: 0; Sources Limit: 0; Robustness (Configured Value): 2; Robustness (Value In Use): 2; Last Member Query Interval (Configured Value): 1 seconds; Last Member Query Interval (Value In Use): 1 seconds; Drop IGMPv1 packets: false; Drop IGMPv2 packets: false; Immediate Leave: false; Query Before Immediate Leave: false; Interface: service-port-201; Query Interval (Configured Value): 125 seconds; Query Interval (Value In Use): 125 seconds; Query Maximum Response Time (Configured Value): 10 seconds; Query Maximum Response Time (Value In Use): 10 seconds; Groups Limit: 0; Sources Limit: 0; Robustness (Configured Value): 2; Robustness (Value In Use): 2; Last Member Query Interval (Configured Value): 1 seconds; Last Member Query Interval (Value In Use): 1 seconds; Drop IGMPv1 packets: false; Drop IGMPv2 packets: false; Immediate Leave: false; Query Before Immediate Leave: false; Interface: service-port-202; Query Interval (Configured Value): 125 seconds; Query Interval (Value In Use): 125 seconds; Query Maximum Response Time (Configured Value): 10 seconds; Query Maximum Response Time (Value In Use): 10 seconds; Groups Limit: 0; Sources Limit: 0; Robustness (Configured Value): 2; Robustness (Value In Use): 2; Last Member Query Interval (Configured Value): 1 seconds; Last Member Query Interval (Value In Use): 1 seconds; Drop IGMPv1 packets: false; Drop IGMPv2 packets: false; Immediate Leave: false; Query Before Immediate Leave: false;

**Output Terms:**

Output Description IGMP Snooping Indicates the IGMP snooping instance. Instance Bridge Domain Indicates the bridge domain type and its ID. Administrative Indicates the administrative state of the IGMP snooping instance (enState able/disable). Indicates the operational state of the IGMP snooping instance Operational state (Up/Down). Output Description Shows IGMP snooping information related to a specific network interInterface face.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show multicast igmp snooping groups`

> **Página:** 1324 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows information about IGMP snooping groups.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
show multicast igmp snooping groups [{brief | detail | extensive} [instance-id] [ipv4-address] [interface-name]]
```

**Parameters:**

- `brief` — Shows a summary of the active multicast group memberships. — *Valores:* N/A · *Default:* N/A
- `detail` — Shows detailed information about the active multicast group memberships. — *Valores:* N/A · *Default:* N/A
- `extensive` — Shows detailed information about the active multicast group memberships, and the IGMP snooping instance. — *Valores:* N/A · *Default:* N/A
- `instance-id` — Shows information about the specified IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `ipv4-address` — Filters the command output by the multicast group IP address. — *Valores:* a.b.c.d. · *Default:* N/A
- `interface-name` — Filters the command output by the provided network interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.0 | Source address field was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show multicast igmp snooping groups
```

ID Group-address Source-address Interface Uptime Expires Last-reporter -- ------------- -------------- --------- ------- ------- -------------- 1 226.2.2.2 172.16.0.1 service-port-201 99 160 100.2.2.103 IGMP Snooping Instance: 1; Group address: 226.2.2.2; Source address: 172.16.0.1; Interface: service-port-201; Version: V3; Last reporter: 100.2.2.103; Exclude state expire: 00:00:00; Uptime: 00:01:40; Expires: 00:02:39; IGMP Snooping Instance: 1; Bridge Domain:vlan; ID: 2000; Group address: 226.2.2.2; Source address: 172.16.0.1; Filter mode: Include; Membership type: dynamic; Interface: service-port-201; Version: V3; Last reporter: 100.2.2.103; Exclude state expire: 00:00:00; Uptime: 00:01:40; Expires: 00:02:39; Host timer: V1: 00:00:00; V2: 00:02:39; Source filter mode: Include;

```text
# show multicast igmp snooping groups brief
```

ID Group-address Source-address Interface Uptime Expires Last-reporter -- ------------- -------------- --------- ------- ------- -------------- 1 226.2.2.2 172.16.0.1 service-port-201 99 160 100.2.2.103

```text
# show multicast igmp snooping groups detail
IGMP Snooping Instance: 1;
Group address: 226.2.2.2;
Source address: 172.16.0.1;
Interface: service-port-201;
Version: V3;
Last reporter: 100.2.2.103;
Exclude state expire: 00:00:00;
Uptime: 00:01:40; Expires: 00:02:39;
# show multicast igmp snooping groups extensive
IGMP Snooping Instance: 1;
Bridge Domain:vlan; ID: 2000;
Group address: 226.2.2.2;
Source address: 172.16.0.1;
Filter mode: Include;
Membership type: dynamic;
Interface: service-port-201;
Version: V3;
Last reporter: 100.2.2.103;
Exclude state expire: 00:00:00;
Uptime: 00:01:40; Expires: 00:02:39;
```

Host timer: V1: 00:00:00; V2: 00:02:39; Source filter mode: Include;

**Output Terms:**

Output Description ID Indicates the IGMP snooping instance ID. Group address Indicates the multicast group membership address. Source address Indicates the specific source address. Indicates the network interface where the multicast group memberInterface ship is active. Indicates the amount of time (in seconds) that the multicast group Uptime membership is active. Indicates the amount of time (in seconds) for the multicast group Expires membership to become inactive, if no other IGMP report messages is received on the interface. Output Description Indicates the IP address of the last host to report that multicast group Last Reporter membership.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show multicast igmp snooping mrouter`

> **Página:** 1329 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows which interfaces are multicast router interfaces, host interfaces, or capable of being either of them.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
show multicast igmp snooping mrouter [instance-id [interface-name]]
```

**Parameters:**

- `instance-id` — Filters output by the provided IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface-name` — Filters the command output by the provided network interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show multicast igmp snooping mrouter 1
```

ID VLAN Interface MRouter Learned -- ---- --------- ------------- ------- 1 2000 gigabit-ethernet-1/1/9 yes - 1 2000 gigabit-ethernet-1/1/10 learn-queries no 1 2000 service-port-201 no - 1 2000 service-port-202 no -

```text
# show multicast igmp snooping mrouter 1 gigabit-ethernet-1/1/9
```

ID VLAN Interface MRouter Learned -- ---- --------- ------------- ------- 1 2000 gigabit-ethernet-1/1/9 yes -

**Output Terms:**

Output Description ID Indicates the IGMP snooping instance ID. VLAN Indicates the VLAN ID. Interface Indicates the network interface. Indicates whether the interface is statically configured as a multicast MRouter router interface (yes), host interface (no), or capable of being either of them (learn-queries). Indicates whether the interface is a multicast router interface (yes) Learned or host interface (no). This field is only valid for the interfaces that are configured in the learn-queries mode.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show multicast igmp snooping port`

> **Página:** 1332 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows IGMP snooping interface information.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
show multicast igmp snooping port [{brief | detail | extensive} [instance-id] [interface-name]]
```

**Parameters:**

- `brief` — Shows a summary of the IGMP snooping interface information. — *Valores:* N/A · *Default:* N/A
- `detail` — Shows detailed information about the IGMP snooping interfaces. — *Valores:* N/A · *Default:* N/A
- `extensive` — Shows detailed information about the IGMP snooping interfaces, and the IGMP activity as well. — *Valores:* N/A · *Default:* N/A
- `instance-id` — Filters the command output by the provided IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A
- `interface-name` — Filters the command output by the provided network interface name. — *Valores:* hundred-gigabit-ethernet-chassis/slot/port | forty-gigabit-ethernetchassis/slot/port | twenty-five-g-ethernet-chassis/slot/port | ten-gigabit-ethernet-chassis/slot/port | gigabit-ethernet-chassis/slot/port | lag-id | service-port-id. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |
| 1.12 | Support for LAG was added. |
| 3.0 | Support for 40-gigabit Ethernet was added. |
| 4.6 | Support for 100-gigabit Ethernet was added. |
| 5.0 | Support for 25-gigabit Ethernet was added. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show multicast igmp snooping port brief 1 service-port-202
Queries (sent) Msgs (recv)
```

ID Interface Ad Op Ver Joins General Specific Invalid Total -- --------- -- ---- --- -------- -------- -------- -------- -------- 1 service-port-202 en up 3 8 2 10 0 13

```text
# show multicast igmp snooping port detail 1 service-port-202
IGMP Snooping Instance: 1;
Interface: service-port-202;
Administrative state: enable;
Operational state: up;
IGMP version: 3;
```

IGMP query interval: 125 seconds; IGMP querier timeout: 0 seconds; IGMP querier last changed: 0 seconds; IGMP querier robustness: 2; IGMP max query response time is 10 seconds; Last member query count: 2; Startup query interval: 31 seconds; Startup query count: 2; Last member query response interval: 1 seconds;

```text
# show multicast igmp snooping port extensive 1 service-port-202
IGMP Snooping Instance: 1;
```

Bridge Domain: vlan; ID: 2000; Interface: service-port-202; Administrative state: enable; Operational state: up; IGMP version: 3; IGMP query interval: 125 seconds; IGMP querier timeout: 0 seconds; IGMP querier last changed: 0 seconds; IGMP querier robustness: 2; IGMP max query response time is 10 seconds; Last member query count: 2; Startup query interval: 31 seconds; Startup query count: 2; Last member query response interval: 1 seconds; IGMP activity: Joins: 8; Failed joins: 0; Counters last reset: 13559 seconds; Peak groups: 1; Sent: General queries sent: 2; Specific queries sent: 10; Received: Wrong version queries: 0; Invalid messages: 0; IGMP v1 messages: 0; IGMP v2 messages: 13; IGMP v3 messages: 0; Total messages: 13;

**Output Terms:**

Output Description ID Indicates the IGMP snooping instance ID. Interface Indicates the network interface. Ad Indicates the administrative status of the interface. Op Indicates the operational status of the interface. Ver Indicates the configured IGMP version on the interface. Indicates the number of IGMP report messages received by the inJoins terface. Indicates the number of IGMP general query messages sent by the General Queries interface. Indicates the number of IGMP specific query messages sent by the Specific Queries interface. Output Description Indicates the number of invalid IGMP messages received by the inInvalid Msgs terface. Indicates the total amount of IGMP messages exchanged by the inTotal terface.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A


### `show multicast igmp snooping statistics`

> **Página:** 1337 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows IGMP snooping statistics.

**Supported Platforms:** This command is not supported in the following platforms: DM4340, DM4618, DM4920.

**Syntax:**

```text
show multicast igmp snooping statistics [instance-id]
```

**Parameters:**

- `instance-id` — Filters the command output by the provided IGMP snooping instance ID. — *Valores:* 1-8. · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.10 | This command was introduced. |

**Usage Guidelines:**

This command can be executed directly via CLI. Example: This example shows how to use this command.

```text
# show multicast igmp snooping statistics 1
IGMP Snooping: 1;
```

Bridge Domain: vlan; ID: 2000; IGMP messages: Valid: Received queries: 0; Received reports: 12; Received leaves: 9; Total: 21; Filtered: Received queries: 7; Received reports: 0; Exceeded limit: 0; Groups & sources: 0; Link local: 0; Other: 0; Total: 7; Bad: Checksum: 0; Router alert: 0; Other: 0; Total: 0; Other: Sent queries: 26; Snooping queries: 0;

**Output Terms:**

Output Description IGMP Snooping Indicates the IGMP snooping instance ID. Bridge Domain Displays bridge domain information. Indicates the number of each IGMP message type sent and received IGMP messages by the IGMP snooping instance.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A CHAPTER 9: QUALITY OF SERVICE This chapter describes the commands related to management of QoS in the DmOS CLI. QOS POLICER This topic describes the commands related to Policer and Meter such as commands to configure CIR and PIR or to inspect bandwidth rates.
