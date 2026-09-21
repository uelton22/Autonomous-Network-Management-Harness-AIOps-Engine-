# Capítulo 17: Free Mobility Commands

> Fonte: `doc_huawei_datacom/huawei` · Huawei VRP Issue 14 (2021-10-20) · S1720, S2700, S5700, and S6720 Series Ethernet Switches

## Free Mobility Configuration Commands

17.1 Free Mobility Configuration Commands 17.1.1 Command Support 17.1.2 display group-policy status 17.1.3 group-policy controller 17.1.4 group-policy version Only the S5720HI supports the commands in this chapter.

### `display group-policy status`

> **Página:** 1 · **Views (Modo):** All views · **Default Level (Privilégio):** 1: Monitoring level · **Leitura (display/show):** sim

**Description (Function):** The display group-policy status command displays the status of the controller associated with the device.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
display group-policy status
```

**Usage Guidelines:**

After running the 17.1.3 group-policy controller command, you can run this command to check the status of the controller associated with the device.

**Example:**

```text
# Display the status of the controller associated with the device.
<HUAWEI> display group-policy status
<HUAWEI> display group-policy status
Controller IP address: 192.168.1.1
Controller port: 5222
Backup controller IP address: -
Backup controller port: -
Source IP address: 192.168.10.1
State: not connected
Connected controller: master
Device protocol version: 2
Controller protocol version: -
```

Table 17-1 Description of the display group-policy status command output

| Item | Description |
| --- | --- |
| Controller IP address | IP address of the master controller. To configure the IP address of the master controller, run the 17.1.3 group-policy controller command. |
| Controller port | Port number of the master controller that exchanges packets with the device. To configure the port number of the master controller, run the 17.1.3 group- policy controller command. |
| Backup controller IP address | IP address of the backup controller. To configure the IP address of the backup controller, run the 17.1.3 group-policy controller command. |
| Backup controller port | Port number of the backup controller that exchanges packets with the device. To configure the port number of the backup controller, run the 17.1.3 group- policy controller command. |

| Item | Description |
| --- | --- |
| Source IP address | Source IP address that the device uses to communicate with the controller. To configure the source IP address, run the 17.1.3 group-policy controller command. |
| State | Status of the connection between the device and controller. ● disabled: indicates that the free mobility function is disabled. ● not connected: indicates that the device and controller are not connected. ● working: indicates that the device and controller have been connected. |
| Connected controller | Controller connected to the device. ● master: indicates the master controller. ● slave: indicates the backup controller. ● none: indicates that the device and controller are not connected. |
| Device protocol version | Protocol version number of the device. |
| Controller protocol version | Protocol version number of the controller. The parameter displays - when the device is not registered on the controller. |

**Related Topics:**

- 17.1.3 group-policy controller


### `group-policy controller`

> **Página:** 3 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The group-policy controller command enables the free mobility function. The undo group-policy controller command restores the default configurations. By default, the free mobility function is disabled.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
group-policy controller ip-address1 [ port-number1 ] [ backup ip-address2
[ port-number2 ] ] password password [ src-ip ip-address3 ]
undo group-policy controller
```

**Parameters:**

- `ip-address1 [ port- number1 ]` — Specifies the IP address of the master controller and the port number for exchanging packets between the master controller and device. If no port number is configured, the default port number 5222 is used. — *Valores:* ip-address1: The value is in dotted decimal notation. port-number1: The value is an integer that ranges from 1 to 65535.
- `backup ip- address2 [ port- number2 ]` — Specifies the IP address of the backup controller and the port number for exchanging packets between the backup controller and device. If no port number is configured, the default port number 5222 is used. — *Valores:* ip-address2: The value is in dotted decimal notation. port-number2: The value is an integer that ranges from 1 to 65535.
- `password password` — Specifies the password for connecting the device to controllers. — *Valores:* The connection password configured on the device must be the same as the connection password configured on the controllers. Password rule on the controllers: ● The length should be between 8 to 32 characters. (The password can be a plain text of 8 to 32 characters or a cipher text of 48 to 68 characters.) ● Must contain two type characters in combinations as follows: Digits, upper case letter, lower case letter, special characters. ● Cannot contain over two same letters. ● Cannot same to name or reverse name.
- `src-ip ip- address3` — Specifies the source IP address that the device uses to communicate with the controller. If this parameter is not configured, the device selects one of its own IP addresses to communicate with the controller. — *Valores:* The value is in dotted decimal notation.

**Usage Guidelines:**

**Usage Scenario**

The free mobility function allows a user to obtain the same network access policy regardless of the user's location and IP address used. In addition, user access policies only need to be uniformly deployed and managed on controllers, which simplifies network deployment. After the free mobility function is enabled using this command on access devices, the device can connect to the controllers. The administrator deploys network access policies for users uniformly on controllers and deliver them to the devices. The devices then can control the users' network access policies.

**Precautions**

This command cannot be run on the device when the controller delivers services to the device.

**Example:**

```text
# Enable the free mobility function, and configure the controller IP address to
```

10.1.1.11 and connection password to huawei@123.

```text
<HUAWEI> system-view
[HUAWEI] group-policy controller 10.1.1.11 password huawei@123
```

**Related Topics:**

- 17.1.2 display group-policy status


### `group-policy version`

> **Página:** 6 · **Views (Modo):** System view · **Default Level (Privilégio):** 3: Management level · **Leitura (display/show):** não

**Description (Function):** The group-policy version command configures the user group version or user group policy version used for free mobility.

**Supported Platforms:** S1720, S2700, S5700, and S6720 Series Ethernet Switches

**Syntax (Format):**

```text
group-policy { user-group | user-group-policy } version version
```

**Parameters:**

- `user-group` — Specifies a user group. — *Valores:* -
- `user-group- policy` — Specifies a user group policy. — *Valores:* -
- `version version` — Specifies a version. — *Valores:* The value is an integer that ranges from 0 to 4294967295. NOTE The version needs to be obtained from the controller database. The configured version must be consistent with the version obtained from the controller database. Otherwise, the switch configuration is inconsistent with the controller configuration or the controller configuration fails to be delivered to the switch.

**Usage Guidelines:**

**Usage Scenario**

When a switch is connected to the controller and has free mobility configured, the switch's user group version and user group policy version used for free mobility are restored to 0 if the group-policy controller command configuration is deleted incorrectly from the switch. In this situation, the switch and controller have inconsistent user group versions and user group policy versions used for free mobility. This inconsistency leads to a failure to deliver the free mobility configuration from the controller to the switch even though the group-policy controller command is configured again on the switch. To address this issue, run the group-policy version command on the switch to configure the user group version and user group policy version used for free mobility. This configuration can restore the function that delivers the free mobility configuration from the controller to the switch.

**Precautions**

- The group-policy version command can be used to restore communication between a switch and the controller only when the group-policy controller command configuration is deleted incorrectly. Do not use the group-policy version command when the switch communicates with the controller normally.

- If you run the group-policy version command multiple times, only the latest configuration takes effect.

- The group-policy version command configuration is not recorded in the configuration file after this command is executed. To verify the command configuration, run the display group-policy health command in the diagnostic view. In the command output, CMDC_CONTROLLER_UGSYNINCREMET_CONTROL indicates the user group version, and CMDC_CONTROLLER_UGPSYNINCREMET_CONTROL indicates the user group policy version.

**Example:**

```text
# Set the user group version used for free mobility to 20.
<HUAWEI> system-view
[HUAWEI] group-policy user-group version 20
```
