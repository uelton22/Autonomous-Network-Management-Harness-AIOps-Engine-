# Capítulo 17: Modular Chassis

> Fonte: `comand-reference-fw 12.0.2.pdf` · DmOS 12.0.2 · Datacom Command Reference

## Provisioning

### `provision`

> **Página:** 1907 · **Modo:** Configuration mode · **Privilégios:** Config · **Leitura (show/display):** não

**Description:** Provision a line card to the candidate configuration.

**Supported Platforms:** This command is supported only in the following platforms: DM4618, DM4920.

**Syntax:**

```text
provision [chassis {chassis_id} [slot {slot_name} [card-model {card_model}]]]
```

> _Use the no form to revert this command. For further information about the no form, read the chapter Using the "No" Form of a Command._

**Parameters:**

- `chassis chassis_id` — Chassis identifier. Currently only one chassis_id is supported. — *Valores:* 1 · *Default:* None
- `slot slot_name` — Identifies the slot where the card will be provisioned. — *Valores:* Slot number, depends on the platform model. · *Default:* None
- `card-model card_model` — Identifies the model of the card that will be provisioned in the slot. — *Valores:* LC-model, where model depends on slot and platform. · *Default:* None

**Default:** N/A

**History:**

| Release | Modification |
| --- | --- |
| 8.2 | This command was introduced. The command supports the card models LC-800, LC-OAC, and LC-2xOAC 9.4 on DM4920. The command supports the card models LC-OAB-S, LC-OAP-S, and LC10.0 OPS on DM4920. |

**Usage Guidelines:**

This command should be used to provision a line card to the system, and it takes effect immediately, creating the interfaces in the candidate configuration. An example of the command usage is shown below.

```text
DM4618# show platform
```

Chassis/Slot Product model Role Status Firmware version ------------ ----------------- ------- ------------ ---------------------- 1 DM4618 OLT - - Not available 1/1 32GPON Active Ready 8.2.0-274-1-g33ba7a14e0 1/2 LC-32GPON None Blocked Not available 1/FAN1 FAN 2U-F-50 None Ready Not available 1/FAN2 FAN 2U-F-50 None Ready Not available 1/FAN3 FAN 2U-F-50 None Ready Not available 1/PSU1 PSU 600 DC-F None Ready Not available 1/PSU2 PSU 600 AC-F None Ready Not available

```text
DM4618# show platform chassis 1 slot 2 detail
Chassis/Slot : 1/2
Product model : LC-32GPON
Role : None
Status : Blocked
Reason : Card Mismatch
```

Firmware version : Not available

```text
DM4618# config
Entering configuration mode terminal
```

DM4618(config)# provision chassis 1 slot 2 card-model LC-32GPON DM4618(config-slot-2)# commit Commit complete. DM4618(config)# exit

```text
DM4618# show platform
```

Chassis/Slot Product model Role Status Firmware version ------------ ----------------- ------- ------------ ---------------------- 1 DM4618 OLT - - Not available 1/1 32GPON Active Ready 8.2.0-274-1-g33ba7a14e0 1/2 LC-32GPON None Ready Not available 1/FAN1 FAN 2U-F-50 None Ready Not available 1/FAN2 FAN 2U-F-50 None Ready Not available 1/FAN3 FAN 2U-F-50 None Ready Not available 1/PSU1 PSU 600 DC-F None Ready Not available As shown in the above example, the LC-32GPON at slot 1/2 was previously blocked with reason “Card Mismatch”. After provisioning the card, it went to the “Ready” state, and its interfaces became available to be configured in the candidate configuration.

**Impacts and precautions:**

N/A

**Hardware restrictions:**

N/A CHAPTER 18: HARDWARE This chapter describes the CLI commands related to Hardware management of the DmOS. ENVIRONMENT This topic describes the commands related to management of environment conditions such as commands to inspect device’s temperature or to configure thermal alarms.
