# Capítulo 18: Hardware

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## Environment

### `show environment`

> **Página:** 1910 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays real-time information about the device environment.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show environment [chassis chassis_id [slot slot_id]] [power]
```

**Parameters:**

- `chassis_id` — Chassis key identifier. If the value of this parameter is ‘*’ or ‘ ’, a list of all present chassis will be showed. — *Valores:* 1 · *Default:* None
- `slot_id` — Identifies a card present on a chassis (e.g: FAN, 1, etc.). If the value of this parameter is ‘*’ or ‘ ’, a list of all present cards will be showed. — *Valores:* 1 or FAN · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.2 | This command was introduced. |
| 1.8 | Fan information was introduced. |
| 2.4 | Removed fan alarm for HIGH speed. |
| 4.8 | Removed fan control information. |

**Usage Guidelines:**

This command is available when there are sensors or fans at hardware. Use slot parameter to filter the output or let unspecified slots to see all cards info. Example:

```text
DM4610# show environment
```

Temperature Sensors: ----------------------------------------------------------------------------- Chassis/ | Sensor | Temp | Alarm | Hyster | Status Slot/Id | | | Thresholds | | ----------------------------------------------------------------------------- 1/1/SENSOR1 | Card | 49.5 | 0.0 ~ 55.0 | 5.0 | NORMAL 1/1/SENSOR2 | Switch Fabric | 54.0 | 0.0 ~ 75.0 | 5.0 | NORMAL 1/1/SENSOR3 | GPON PHY/SFP | 59.0 | 0.0 ~ 75.0 | 5.0 | NORMAL 1/1/SENSOR4 | CPU | 55.0 | 0.0 ~ 75.0 | 5.0 | NORMAL 1/1/SENSOR5 | CPU Core | 65.3 | 0.0 ~ 110.0 | 5.0 | NORMAL 1/1/SENSOR2 | Switch Fabric Core | 54.0 | 0.0 ~ 75.0 | 5.0 | NORMAL 1/PSU1/SENSOR1 | PSU1 | 50.5 | 0.0 ~ 85.0 | 5.0 | NORMAL 1/PSU2/SENSOR1 | PSU2 | 47.5 | 0.0 ~ 85.0 | 5.0 | NORMAL ----------------------------------------------------------------------------- Sensors on not present transceivers(QSFPs) are displayed as N/A Status Fan Information: ----------------------------------------------- Chassis/Slot/Fan-ID | Speed(RPM) | Status ----------------------------------------------- 1/FAN/1 | 2500.0 | NORMAL 1/FAN/2 | 2419.0 | NORMAL 1/FAN/3 | 2343.0 | NORMAL ----------------------------------------------- Power Information: ---------------------------------------------- Chassis/PSU-ID | Status ---------------------------------------------- 1/PSU1 | POWER INPUT FAILURE 1/PSU2 | OK ----------------------------------------------

**Output Terms:**

Output Description Chassis/Slot/Id Indicates the physical location of the sensor inside the equipment. Sensor Brief description of which device the sensor is measuring. Temp. Current temperature measured by the sensor. Temperature limits of a specific sensor indicating its normal range of Alarm Thresholds operation. Hysteresis applied to the temperature limits (it indicates the temperHyster. ature that the Status change from LOW or HIGH to NORMAL). Indicates the current status of the measured temperature (NORMAL Temperature Status for adequate operation, LOW or HIGH for out of normal range of operation and ERROR when reading the sensor fail). Chassis/Slot/Fan-ID Indicates the physical location of the fan inside the equipment. Speed Current speed measured by the fan’s tachometer. Indicates the current status of the measured fan (NORMAL for adequate operation, LOW when its speed is lower than expected for adFan Status equate operation, ERROR when is not possible to read the tachometer’s value and FAIL when the fan status reports a failure). Indicates the current status of the PSUs (OK for adequate operation, POWER INPUT FAILURE when there is no external power, FUSE FAILPSU Status URE when the Fuse is blown, and ERROR when is not possible to read the PSU status)

**Impacts and precautions:**

Keep the fans module clear for the proper air flow. Keep the air filter of the fans module clean.

**Hardware restrictions:**

The sensors list depends on the equipment model.


### `show interface transceivers`

> **Página:** 1914 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Shows the status, digital diagnostics and basic information of all present transceivers.

**Supported Platforms:** This command is supported in all platforms.

**Syntax:**

```text
show interface [ transceivers [ interface_type [ interface_id | status | digital-diagnostics | dwdm-diagnostics | otdr-distances [ current-thresholds | rx-power-thresholds | temperature-thresholds | tx-power-thresholds | voltage-thresholds | otdr-lastdistance | application | available-application]]]]
```

**Parameters:**

- `interface_type` — Interface type identifier such as ‘gpon’, ‘gigabit-ethernet’, ‘ten-gigabit-ethernet’, etc. If the value of this parameter is unspecified or is the character ‘*’, a list of all present transceivers will be showed. — *Valores:* gpon, gigabit-ethernet, ten-gigabit-ethernet, twenty-five-g-ethernet, forty-gigabit-ethernet, hundred-gigabit-ethernet, four-hundredg-ethernet or mgmt-osc. · *Default:* N/A
- `interface_id` — Interface key identifier, chassis/slot/port. The interface_id equal to 1/2/3 is an example of chassis 1, slot 2 and port 3. If the value of this parameter is ‘*’ or ‘ ’, a list of all present transceivers will be showed. — *Valores:* chassis/slot/port · *Default:* N/A
- `digital-diagnostics` — Show only the digital-diagnostics of all present transceivers — *Valores:* N/A · *Default:* N/A
- `status` — Show only the status of all present transceivers — *Valores:* N/A · *Default:* N/A
- `dwdm-diagnostics` — Show only the DWDM diagnostics of all present transceivers. Only DWDM available transceivers will have valid values, others transceivers will show N/A. Available only in platform DM4920. — *Valores:* N/A · *Default:* N/A
- `otdr-distances` — Show all the link discontinuities of a specified present transceiver. If the transceiver does not have any discontinuity or does not have OTDR support, it will show “% No entries found.”. — *Valores:* N/A · *Default:* N/A
- `application` — Show the current CMIS application mode of a specified present transceiver. If the transceiver does not have CMIS support, it will not be displayed. — *Valores:* N/A · *Default:* N/A
- `available-application` — Show all the available CMIS application table of a specified present transceiver. If the transceiver does not have CMIS support, it will not be displayed. — *Valores:* N/A · *Default:* N/A

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 1.0 | This command was introduced. |
| 4.5.2 | Support to digital-diagnostics of forty-gigabit-ethernet transceivers. |
| 4.6 | Support to digital-diagnostics of hundred-ethernet transceivers. |
| 5.0 | Support to digital-diagnostics of twenty-five-ethernet transceivers. |
| 5.10 | Added information about transceiver supported fiber type. |
| 6.2 | Removed transceiver tx-fault status information. Support to dwdm-diagnostics of four-hundred-g-ethernet transceivers on 9.6 DM4920 platform. |
| 10.0 | Support to mgmt-osc interface transceivers on DM4920 platform. Support to otdr of mgmt-osc interface transceivers on DM4920 platform. 10.6 Support to Chromatic Dispersion for DM4920 transceiver dwdm diagnos10.8 tics Support to CMIS Appsel table options for transceivers with CMIS compli12.0 ance. |

**Usage Guidelines:**

Examples: Show the status of all gigabit-ethernet transceivers

```text
DM4610# show interface transceivers gigabit-ethernet status
---------------------------------------
Transceiver ID | Rx-LOS
---------------------------------------
gigabit-ethernet 1/1/2 | No
gigabit-ethernet 1/1/3 | Yes
gigabit-ethernet 1/1/4 | Yes
gigabit-ethernet 1/1/5 | Yes
gigabit-ethernet 1/1/6 | Yes
gigabit-ethernet 1/1/7 | No
---------------------------------------
```

Show the digital diagnostics of all gpon transceivers

```text
DM4610# show interface transceivers gpon digital-diagnostics
-----------------------------------------------------------------------------
```

Transceiver ID | Temperature | Voltage 3.3V | Current | Tx-Power | Rx-Power ----------------------------------------------------------------------------- gpon 1/1/2 | 41.64 C | 3.27 V | 0.0 mA |-39.99 dBm | 8.15 dBm gpon 1/1/8 | 36.24 C | 3.29 V | 0.0 mA | 8.16 dBm | 3.92 dBm ----------------------------------------------------------------------------- Show the status and the digital diagnostics of all forty-gigabit-ethernet transceivers

```text
DM4170# show interface transceivers forty-gigabit-ethernet
-------------------------------------------
Transceiver ID | Rx-LOS
-------------------------------------------
forty-gigabit-ethernet 1/1/1:1 | No
forty-gigabit-ethernet 1/1/1:2 | No
forty-gigabit-ethernet 1/1/1:3 | No
forty-gigabit-ethernet 1/1/1:4 | No
forty-gigabit-ethernet 1/1/2:1 | No
forty-gigabit-ethernet 1/1/2:2 | No
forty-gigabit-ethernet 1/1/2:3 | No
forty-gigabit-ethernet 1/1/2:4 | No
----------------------------------------------------
---------------------------------------------------------------------------------------------------
```

Transceiver ID | Temperature | Voltage 3.3V | Current | Tx-Power | Rx-Power --------------------------------------------------------------------------------------------------- forty-gigabit-ethernet 1/1/1 | 36.05 C | 3.26 V | N/A | N/A | N/A forty-gigabit-ethernet 1/1/1:1 | N/A | N/A | 24.02 mA | -2.18 dBm | -1.27 dBm forty-gigabit-ethernet 1/1/1:2 | N/A | N/A | 25.03 mA | -1.61 dBm | -0.92 dBm forty-gigabit-ethernet 1/1/1:3 | N/A | N/A | 25.03 mA | -2.22 dBm | -0.91 dBm forty-gigabit-ethernet 1/1/1:4 | N/A | N/A | 26.04 mA | -1.33 dBm | -0.6 dBm forty-gigabit-ethernet 1/1/2 | 32.4 C | 3.26 V | N/A | N/A | N/A forty-gigabit-ethernet 1/1/2:1 | N/A | N/A | 23.94 mA | -1.57 dBm | -1.46 dBm forty-gigabit-ethernet 1/1/2:2 | N/A | N/A | 24.02 mA | -1.52 dBm | -1.29 dBm forty-gigabit-ethernet 1/1/2:3 | N/A | N/A | 25.7 mA | -1.87 dBm | -1.29 dBm forty-gigabit-ethernet 1/1/2:4 | N/A | N/A | 26.71 mA | -1.69 dBm | -0.82 dBm --------------------------------------------------------------------------------------------------- Show the voltage digital diagnostics of all gigabit ethernet transceivers

```text
DM4610# show interface transceivers gigabit-ethernet digital-diagnostics
voltage-thresholds
-----------------------------------------------------------------------------
```

Transceiver ID | Voltage 3.3V | Alarm Thresholds | Warning Thresholds ----------------------------------------------------------------------------- gigabit-ethernet 1/1/2 | 3.29 V | 2.8 V ~ 3.8 V | 2.97 V ~ 3.6 V gigabit-ethernet 1/1/3 | 3.29 V | 2.8 V ~ 3.8 V | 2.97 V ~ 3.6 V gigabit-ethernet 1/1/4 | 3.3 V | 2.8 V ~ 3.8 V | 2.97 V ~ 3.6 V gigabit-ethernet 1/1/6 | 3.24 V | 3.0 V ~ 3.6 V | 3.0 V ~ 3.6 V gigabit-ethernet 1/1/7 | 3.29 V | 2.8 V ~ 3.8 V | 2.97 V ~ 3.6 V ----------------------------------------------------------------------------- Show a specific transceiver

```text
DM4610# show interface transceivers gigabit-ethernet 1/1/2
```

Information of transceiver gigabit-ethernet 1/1/2 Vendor Information Vendor Name: APAC Opto Serial Number: 9813050024 Part Number: LS38-E3C-TC-N-DD Type: SFP Media: OPTICAL Connector: LC Laser Wavelength: 1310 nm Fiber Type: Single-Mode Status Rx-LOS: No Information of transceiver gigabit-ethernet 1/1/2 Digital Diagnostics Temperature [C]: 41.71 [ -15.0 ~ 85.0] Voltage 3.3V [V]: 3.29 [ 2.8 ~ 3.8] Current [mA]: 9.72 [ 0.09 ~ 79.96] Tx-Power [dBm]: -6.23 [ -11.0 ~ -0.99] Rx-Power [dBm]: -6.86 [ -22.0 ~ -1.99] Show dwdm-diagnostics of all present transceivers

```text
DM4920# show interface transceivers dwdm-diagnostics
---------------------------------------------------------------------------------------- ...
```

Transceiver ID | OSNR | PREFEC BER | FERC | ... ---------------------------------------------------------------------------------------- ... four-hundred-g-ethernet 1/2/1 | 37.5 dB | 2.08e-04 | 2.08e-04 | ... four-hundred-g-ethernet 1/2/2 | 26.5 dB | 2.08e-04 | 2.08e-04 | ... four-hundred-g-ethernet 1/3/1 | 13.5 dB | 2.08e-04 | 2.08e-04 | ... hundred-gigabit-ethernet 1/2/1 | N/A | N/A | N/A | ... hundred-gigabit-ethernet 1/3/5 | N/A | N/A | N/A | ... ---------------------------------------------------------------------------------------- ... ------------------------------------ Q-Value | Q-Factor | CD ------------------------------------ 3.17 | 10.03 dB | 42 ps/nm 3.17 | 10.03 dB | 7 ps/nm 3.17 | 10.03 dB | 203 ps/nm N/A | N/A | N/A N/A | N/A | N/A ------------------------------------ Show dwdm-diagnostics to a specific interface type transceiver

```text
DM4920# show interface transceivers four-hundred-g-ethernet dwdm-diagnostics
---------------------------------------------------------------------------------------- ...
```

Transceiver ID | OSNR | PREFEC BER | FERC | ... ---------------------------------------------------------------------------------------- ... four-hundred-g-ethernet 1/2/1 | 37.5 dB | 2.08e-04 | 2.08e-04 | ... four-hundred-g-ethernet 1/2/2 | 26.5 dB | 2.08e-04 | 2.08e-04 | ... four-hundred-g-ethernet 1/3/1 | 13.5 dB | 2.08e-04 | 2.08e-04 | ... ---------------------------------------------------------------------------------------- ... ------------------------------------ Q-Value | Q-Factor | CD ------------------------------------ 3.17 | 10.03 dB | 42 ps/nm 3.17 | 10.03 dB | 7 ps/nm 3.17 | 10.03 dB | 203 ps/nm ------------------------------------ Show dwdm-diagnostics to a specific interface type and id transceiver

```text
DM4920# show interface transceivers four-hundred-g-ethernet 1/2/1 dwdm-diagnostics
VDM Statistics
OSNR : 37.5 dB
PREFEC BER : 2.08e-04
FERC : 2.08e-04
Q-VALUE : 3.17
Q-FACTOR : 10.03 dB
```

Chromatic Dispersion : 10 ps/nm Show otdr last distance of all present transceivers

```text
DM4920# show interface transceivers digital-diagnostics otdr-last-distance
-----------------------------------------------------------
```

Transceiver ID | Fault distance ----------------------------------------------------------- mgmt-osc 1/1/2 | 32455 [m] | mgmt-osc 1/1/3 | 76589 [m] | ----------------------------------------------------------- Show otdr last distance to a specific interface type and id transceiver

```text
DM4920# show interface transceivers mgmt-osc 1/1/2 digital-diagnostics
otdr-last-distance
OTDR
LAST DISTANCE :32455 [m]
```

Show all OTDR discontinuity values for a specific interface type and transceiver ID. Note: The interface must be specified (e.g., mgmt-osc 1/1/3).

```text
DM4920# show interface transceivers mgmt-osc 1/1/3 otdr-distances
Discontinuity Distance
-------------------------
1 3256 m
2 7865 m
3 18902 m
4 20345 m
5 76589 m
```

Show all available CMIS application profiles for a specific transceiver inserted on a given port interface. Note: The interface must be specified (e.g., four-hundred-g-ethernet 1/1/1).

```text
DM4780# show interface transceivers four-hundred-g-ethernet 1/1/1 available-application
Host
Appsel Interface Media Interface
```

Code HostLaneCount MediaLaneCount Name Name --------------------------------------------------------------------------- 1 8 4 100GBASE-LR4 100ZR DWDM ampl 2 4 2 400GAUI-8 400GBASE-LR8 3 8 4 400GAUI-8 400GBASE-SR8 4 4 2 400GAUI-8 400GBASE-LR4 5 8 8 400GAUI-8 400GBASE-DR4 Show the current CMIS appsel applied for a specific transceiver inserted in a given port interface. Note: The interface must be specified (e.g., four-hundred-g-ethernet 1/1/1).

```text
DM4780# show interface transceivers four-hundred-g-ethernet 1/1/1 application
Code: 5
Host Lane Count: 4
Media Lane Count: 8
Host Interface: 400GAUI-8
Media Interface: 400GBASE-SR8
```

**Output Terms:**

Output Description Transceiver ID Identification of the transceiver Temperature Temperature of the transceiver Voltage 3.3V Voltage being supplied to transceiver Current Current being drawn by the transceiver Tx-Power Power of the transmitted signal Rx-Power Power of the received signal Rx-LOS Loss of signal on reception Alarm Thresholds Range in which data values can vary before alarm Warning Thresholds Range in which data values can vary before warning Optical Signal to Noise Ratio which is a measure of signal quality in OSNR long distance fiber optic communications It represents the BER (Bit Error Rate) before the FEC (Forward-ErrorPREFEC BER Correction) algorithm act in the data FERC statistic means Frame Error Count which is a rate of nonFERC corrected bits Q-Value represents the system error rate tolerance. A higher QQ-Value VALUE means a better and more error tolerant signal Output Description Q-Factor is a measure of the quality of a digital signal, represents Q-Factor the ratio of the signal power to the noise power, taking into account the spectral width of the signal Chromatic Dispersion measures the dispersion of light, in ps/nm, as Chromatic it travels through an optical fiber, where different wavelengths propDispersion agate at different velocities. The Optical Time Domain Reflectometer (OTDR) last distance is the otdr-last-distance furthest discontinuity measured by that specific transceiver. This information is of special relevance because it represents the fiber break distance from the origin in case of a fiber break. Application selection code ID defined in CMIS standard to identify the Appsel Code application profile being used. Number of electrical lanes on the host side defined in CMIS standard. Host Lane Count Number of optical lanes on the media side defined in CMIS standard. Media Lane Count Host Interface Name of the host interface defined in CMIS standard, decoded from Name SFF-8024. Media Interface Name of the media interface defined in CMIS standard, decoded from Name SFF-8024.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

According to transceiver inserted, these shows could be available or not. DWDM-statistics are only available for the four-hundred-g-ethernet transceivers on the DM4920 platform. RESOURCES This topic describes the commands related to management of hardware resources.


## Resources

### `forwarding-resources`

> **Página:** 1923 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Admin · **Leitura (show/display):** não

**Description:** Forwarding resources configuration changes the switch forwarding table allocation profile, allowing to choose between L2 or L3 priority operation modes.

**Supported Platforms:** This command is supported only in the following platforms: DM4270, DM4380, DM4770, DM4378, DM4376, DM4370, DM4360, DM4170.

**Syntax:**

```text
forwarding-resources {profile profile-name}
```

**Parameters:**

- `profile profile-name` — The default profile balances L2 and L3 capacities for general use. The extended-ip profile reduces L2 capacity to increase maximum L3 routes entries. The extended-mac profile reduces L3 capacity to increase maximum L2 addresses entries. — *Valores:* {default | extended-ip | extended-mac} · *Default:* default

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4.0 | This command was introduced. Add support to following platforms: DM4360, DM4370, DM4376 and 10.4.0 DM4378. |

**Usage Guidelines:**

Example: This example shows how to update the forwarding table allocation profile to extended-ip.

```text
# forwarding-resources profile extended-ip
```

This change will take effect on next reboot.

```text
# reboot
```

Are you sure? [no,yes] yes

**Impacts and precautions:**

Changing the forwarding table allocation profile requires a reboot for the new profile to take effect.

**Hardware restrictions:**

The presence of this command is conditioned by hardware support. Not all profiles may be available for all models. The maximum capacity of each entry type for each profile is also hardware dependent. All profiles, except ‘Reserved-IP’, share the same forwarding resources table for IPv4 and IPv6/64. Profile Name MAC IPv4 IPv6/64 IPv6/128 Running Startup -------------------------------------------------------------------- default 32000 1024 512 256 true true extended-ipv4 32000 2048 1024 0 false false extended-ipv6-64 32000 1536 768 128 false false reserved-ip 32000 1024 256 128 false false The default profile, for instance, allows all sorts of combinations, given both AF limits, e.g.: 1024 IPv4 and 0 IPv6/64; 0 IPv4 and 512 IPv6/64; 512 IPv4 and 256 IPv6/64; and so on. In other hand, the ‘Reserved-IP’ profile will enforce the limits, so in the previous example table, for the Reserved-IP profile, we’re able to allocate 1024 IPv4 and 256 IPv6/64.


### `show forwarding-resources`

> **Página:** 1926 · **Modo:** Operational mode. It is possible to execute this command also in the Configuration mode by using the do keyword before the command. · **Privilégios:** Audit · **Leitura (show/display):** sim

**Description:** Displays information about forwarding table profiles status.

**Supported Platforms:** This command is supported only in the following platforms: DM4270, DM4380, DM4770, DM4378, DM4376, DM4370, DM4360, DM4170.

**Syntax:**

```text
show forwarding-resources
```

**Parameters:**

- `N/A`

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 5.4.0 | This command was introduced. Add support to following platforms: DM4360, DM4370, DM4376 and 10.4.0 DM4378. |

**Usage Guidelines:**

This example shows the command output when the default profile is active and the extended-mac is marked for the next reboot.

```text
# show forwarding-resources
```

Profile Name MAC IPv4 IPv6/64 IPv6/128 Running Startup ------------------------------------------------------------------- default 128000 128000 32000 4000 true false extended-ip 32000 168000 42000 10000 false false extended-mac 288000 16000 4000 1000 false true

**Output Terms:**

Output Description Profile Name Displays the profile name. MAC Displays the maximum L2 addresses of the profile. IPv4 Displays the maximum IPv4 routes of the profile. IPv6/64 Displays the maximum IPv6/64 routes of the profile. IPv6/128 Displays the maximum IPv6/128 routes of the profile. Running Indicates if the profile is active and running. Startup Indicates if the profile is marked to be active on next reboot.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

The presence of this command is conditioned by hardware support. Not all profiles may be available for all models. The maximum capacity of each entry type for each profile is also hardware dependent. All profiles, except ‘Reserved-IP’, share the same forwarding resources table for IPv4 and IPv6/64. Profile Name MAC IPv4 IPv6/64 IPv6/128 Running Startup -------------------------------------------------------------------- default 32000 1024 512 256 true true extended-ipv4 32000 2048 1024 0 false false extended-ipv6-64 32000 1536 768 128 false false reserved-ip 32000 1024 256 128 false false The default profile, for instance, allows all sorts of combinations, given both AF limits, e.g.: 1024 IPv4 and 0 IPv6/64; 0 IPv4 and 512 IPv6/64; 512 IPv4 and 256 IPv6/64; and so on. In other hand, the ‘Reserved-IP’ profile will enforce the limits, so in the previous example table, for the Reserved-IP profile, we’re able to allocate 1024 IPv4 and 256 IPv6/64. CHAPTER 19: CPU PROTECTION CPU DOS PROTECTION This topic describes the commands related to CPU Denial of Service (DoS) Protection.
