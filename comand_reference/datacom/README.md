# DmOS Command Reference — Markdown + Dados Normalizados

Conversão do PDF `comand-reference-fw 12.0.2.pdf` (Datacom **DmOS 12.0.2**) para um corpus estruturado, otimizado para leitura por LLM e indexação em RAG.

## Conteúdo desta pasta

| Arquivo | Descrição |
| --- | --- |
| `chapters/NN-*.md` | Guia completo em Markdown, um arquivo por capítulo. |
| `dmos-commands.jsonl` | **Dados normalizados**: um JSON por comando (campos separados). |
| `dmos-commands.index.json` | Índice compacto (comando → capítulo/seção/página/arquivo). |

## Estatísticas

- **Comandos documentados:** 573
- **Comandos de leitura (show/display):** 122
- **Capítulos:** 19

## Esquema do JSONL (normalização)

```jsonc
{
  "id": "datacom::DmOS-12.0.2::0001",
  "command": "session",
  "vendor": "datacom", "os": "DmOS", "firmware": "12.0.2",
  "chapter_num": 3, "chapter": "Management", "section": "CLI Settings",
  "category": "management",
  "page": 29, "is_read_command": false,
  "description": "...", "supported_platforms": "...",
  "syntax": "...", "syntax_note": "...",
  "parameters": [{"name": "...", "description": "...", "value": "...", "default": "..."}],
  "default": "...", "command_mode": "...", "required_privileges": "...",
  "history": [{"release": "1.0", "modification": "..."}],
  "usage_guidelines": "...", "examples": ["..."],
  "impacts_and_precautions": "...", "hardware_restrictions": "...",
  "extra_sections": {"Output Terms": "..."},
  "markdown": "### `session` ...",
  "text": "..."
}
```

## Capítulos

- [Capítulo 1: Product Concept](chapters/01-product-concept.md) — 0 comando(s)
- [Capítulo 2: Using the Command-Line Interface](chapters/02-using-the-command-line-interface.md) — 0 comando(s)
- [Capítulo 3: Management](chapters/03-management.md) — 72 comando(s)
- [Capítulo 4: Interfaces](chapters/04-interfaces.md) — 30 comando(s)
- [Capítulo 5: Layer 2 - Switching Protocols](chapters/05-layer-2-switching-protocols.md) — 37 comando(s)
- [Capítulo 6: Layer 3 - Routing](chapters/06-layer-3-routing.md) — 159 comando(s)
- [Capítulo 7: MPLS](chapters/07-mpls.md) — 92 comando(s)
- [Capítulo 8: Multicast](chapters/08-multicast.md) — 20 comando(s)
- [Capítulo 9: Quality of Service](chapters/09-quality-of-service.md) — 9 comando(s)
- [Capítulo 10: Access Lists](chapters/10-access-lists.md) — 5 comando(s)
- [Capítulo 11: Security](chapters/11-security.md) — 11 comando(s)
- [Capítulo 12: OAM](chapters/12-oam.md) — 47 comando(s)
- [Capítulo 13: Synchronization](chapters/13-synchronization.md) — 12 comando(s)
- [Capítulo 14: GPON](chapters/14-gpon.md) — 35 comando(s)
- [Capítulo 15: XGSPON](chapters/15-xgspon.md) — 8 comando(s)
- [Capítulo 16: Services](chapters/16-services.md) — 27 comando(s)
- [Capítulo 17: Modular Chassis](chapters/17-modular-chassis.md) — 1 comando(s)
- [Capítulo 18: Hardware](chapters/18-hardware.md) — 4 comando(s)
- [Capítulo 19: CPU Protection](chapters/19-cpu-protection.md) — 4 comando(s)

## Índice de comandos

| Comando | Cap. | Seção | Pág. | Arquivo |
| --- | --- | --- | --- | --- |
| [`debug`](chapters/03-management.md#debug) | 3 | CLI Settings | 22 | `03-management.md` |
| [`display-defaults`](chapters/03-management.md#display-defaults) | 3 | CLI Settings | 25 | `03-management.md` |
| [`screen-resize`](chapters/03-management.md#screen-resize) | 3 | CLI Settings | 27 | `03-management.md` |
| [`session`](chapters/03-management.md#session) | 3 | CLI Settings | 29 | `03-management.md` |
| [`user`](chapters/03-management.md#user) | 3 | CLI Settings | 32 | `03-management.md` |
| [`interface mgmt`](chapters/03-management.md#interface-mgmt) | 3 | Interfaces | 36 | `03-management.md` |
| [`interface mgmt-osc`](chapters/03-management.md#interface-mgmt-osc) | 3 | Interfaces | 42 | `03-management.md` |
| [`show interface mgmt-osc`](chapters/03-management.md#show-interface-mgmt-osc) | 3 | Interfaces | 45 | `03-management.md` |
| [`banner login`](chapters/03-management.md#banner-login) | 3 | Configuration | 48 | `03-management.md` |
| [`clear`](chapters/03-management.md#clear) | 3 | Configuration | 52 | `03-management.md` |
| [`commit`](chapters/03-management.md#commit) | 3 | Configuration | 54 | `03-management.md` |
| [`commit`](chapters/03-management.md#commit) | 3 | Configuration | 57 | `03-management.md` |
| [`commit abort`](chapters/03-management.md#commit-abort) | 3 | Configuration | 60 | `03-management.md` |
| [`commit check`](chapters/03-management.md#commit-check) | 3 | Configuration | 62 | `03-management.md` |
| [`commit confirmed`](chapters/03-management.md#commit-confirmed) | 3 | Configuration | 64 | `03-management.md` |
| [`compare file`](chapters/03-management.md#compare-file) | 3 | Configuration | 68 | `03-management.md` |
| [`config`](chapters/03-management.md#config) | 3 | Configuration | 71 | `03-management.md` |
| [`file`](chapters/03-management.md#file) | 3 | Configuration | 74 | `03-management.md` |
| [`hostname`](chapters/03-management.md#hostname) | 3 | Configuration | 77 | `03-management.md` |
| [`load factory-config`](chapters/03-management.md#load-factory-config) | 3 | Configuration | 80 | `03-management.md` |
| [`load merge`](chapters/03-management.md#load-merge) | 3 | Configuration | 82 | `03-management.md` |
| [`load override`](chapters/03-management.md#load-override) | 3 | Configuration | 85 | `03-management.md` |
| [`resolved`](chapters/03-management.md#resolved) | 3 | Configuration | 88 | `03-management.md` |
| [`rollback configuration`](chapters/03-management.md#rollback-configuration) | 3 | Configuration | 91 | `03-management.md` |
| [`rollback selective`](chapters/03-management.md#rollback-selective) | 3 | Configuration | 95 | `03-management.md` |
| [`save`](chapters/03-management.md#save) | 3 | Configuration | 99 | `03-management.md` |
| [`show`](chapters/03-management.md#show) | 3 | Configuration | 103 | `03-management.md` |
| [`show banner login`](chapters/03-management.md#show-banner-login) | 3 | Configuration | 106 | `03-management.md` |
| [`show configuration`](chapters/03-management.md#show-configuration) | 3 | Configuration | 108 | `03-management.md` |
| [`show configuration commit changes`](chapters/03-management.md#show-configuration-commit-changes) | 3 | Configuration | 112 | `03-management.md` |
| [`show configuration commit list.`](chapters/03-management.md#show-configuration-commit-list) | 3 | Configuration | 117 | `03-management.md` |
| [`show configuration rollback changes`](chapters/03-management.md#show-configuration-rollback-changes) | 3 | Configuration | 120 | `03-management.md` |
| [`show configuration running`](chapters/03-management.md#show-configuration-running) | 3 | Configuration | 124 | `03-management.md` |
| [`show running-config`](chapters/03-management.md#show-running-config) | 3 | Configuration | 127 | `03-management.md` |
| [`top`](chapters/03-management.md#top) | 3 | Configuration | 130 | `03-management.md` |
| [`request firmware onu add`](chapters/03-management.md#request-firmware-onu-add) | 3 | Firmware | 132 | `03-management.md` |
| [`request firmware onu remove`](chapters/03-management.md#request-firmware-onu-remove) | 3 | Firmware | 134 | `03-management.md` |
| [`clear core-dump`](chapters/03-management.md#clear-core-dump) | 3 | Diagnostics | 136 | `03-management.md` |
| [`clear counters`](chapters/03-management.md#clear-counters) | 3 | Diagnostics | 138 | `03-management.md` |
| [`clear statistics`](chapters/03-management.md#clear-statistics) | 3 | Diagnostics | 142 | `03-management.md` |
| [`clear synchronization ptp statistics`](chapters/03-management.md#clear-synchronization-ptp-statistics) | 3 | Diagnostics | 144 | `03-management.md` |
| [`copy core-dump`](chapters/03-management.md#copy-core-dump) | 3 | Diagnostics | 147 | `03-management.md` |
| [`copy file`](chapters/03-management.md#copy-file) | 3 | Diagnostics | 151 | `03-management.md` |
| [`copy mibs`](chapters/03-management.md#copy-mibs) | 3 | Diagnostics | 156 | `03-management.md` |
| [`copy pcap`](chapters/03-management.md#copy-pcap) | 3 | Diagnostics | 159 | `03-management.md` |
| [`counters`](chapters/03-management.md#counters) | 3 | Diagnostics | 162 | `03-management.md` |
| [`interface utilization`](chapters/03-management.md#interface-utilization) | 3 | Diagnostics | 166 | `03-management.md` |
| [`monitor session`](chapters/03-management.md#monitor-session) | 3 | Diagnostics | 170 | `03-management.md` |
| [`ping`](chapters/03-management.md#ping) | 3 | Diagnostics | 173 | `03-management.md` |
| [`ping6`](chapters/03-management.md#ping6) | 3 | Diagnostics | 178 | `03-management.md` |
| [`show alarm`](chapters/03-management.md#show-alarm) | 3 | Diagnostics | 182 | `03-management.md` |
| [`show core-dump`](chapters/03-management.md#show-core-dump) | 3 | Diagnostics | 184 | `03-management.md` |
| [`show counters`](chapters/03-management.md#show-counters) | 3 | Diagnostics | 186 | `03-management.md` |
| [`show interface statistics`](chapters/03-management.md#show-interface-statistics) | 3 | Diagnostics | 189 | `03-management.md` |
| [`show system cpu`](chapters/03-management.md#show-system-cpu) | 3 | Diagnostics | 193 | `03-management.md` |
| [`show system memory`](chapters/03-management.md#show-system-memory) | 3 | Diagnostics | 197 | `03-management.md` |
| [`show system uptime`](chapters/03-management.md#show-system-uptime) | 3 | Diagnostics | 200 | `03-management.md` |
| [`show tech-support`](chapters/03-management.md#show-tech-support) | 3 | Diagnostics | 202 | `03-management.md` |
| [`tcpdump`](chapters/03-management.md#tcpdump) | 3 | Diagnostics | 206 | `03-management.md` |
| [`traceroute`](chapters/03-management.md#traceroute) | 3 | Diagnostics | 214 | `03-management.md` |
| [`traceroute6`](chapters/03-management.md#traceroute6) | 3 | Diagnostics | 217 | `03-management.md` |
| [`snmp agent`](chapters/03-management.md#snmp-agent) | 3 | SNMP | 220 | `03-management.md` |
| [`snmp community`](chapters/03-management.md#snmp-community) | 3 | SNMP | 226 | `03-management.md` |
| [`snmp max-sessions-limit`](chapters/03-management.md#snmp-max-sessions-limit) | 3 | SNMP | 229 | `03-management.md` |
| [`snmp notify`](chapters/03-management.md#snmp-notify) | 3 | SNMP | 231 | `03-management.md` |
| [`snmp system`](chapters/03-management.md#snmp-system) | 3 | SNMP | 233 | `03-management.md` |
| [`snmp target`](chapters/03-management.md#snmp-target) | 3 | SNMP | 235 | `03-management.md` |
| [`snmp traps`](chapters/03-management.md#snmp-traps) | 3 | SNMP | 240 | `03-management.md` |
| [`snmp usm`](chapters/03-management.md#snmp-usm) | 3 | SNMP | 243 | `03-management.md` |
| [`snmp vacm`](chapters/03-management.md#snmp-vacm) | 3 | SNMP | 246 | `03-management.md` |
| [`license`](chapters/03-management.md#license) | 3 | License | 250 | `03-management.md` |
| [`show license`](chapters/03-management.md#show-license) | 3 | License | 253 | `03-management.md` |
| [`breakout interface`](chapters/04-interfaces.md#breakout-interface) | 4 | Ethernet | 255 | `04-interfaces.md` |
| [`dwdm interface`](chapters/04-interfaces.md#dwdm-interface) | 4 | Ethernet | 259 | `04-interfaces.md` |
| [`interface forty-gigabit-ethernet`](chapters/04-interfaces.md#interface-forty-gigabit-ethernet) | 4 | Ethernet | 262 | `04-interfaces.md` |
| [`interface four-hundred-g-ethernet`](chapters/04-interfaces.md#interface-four-hundred-g-ethernet) | 4 | Ethernet | 266 | `04-interfaces.md` |
| [`interface gigabit-ethernet`](chapters/04-interfaces.md#interface-gigabit-ethernet) | 4 | Ethernet | 271 | `04-interfaces.md` |
| [`interface hundred-gigabit-ethernet`](chapters/04-interfaces.md#interface-hundred-gigabit-ethernet) | 4 | Ethernet | 276 | `04-interfaces.md` |
| [`interface ten-gigabit-ethernet`](chapters/04-interfaces.md#interface-ten-gigabit-ethernet) | 4 | Ethernet | 281 | `04-interfaces.md` |
| [`interface twenty-five-g-ethernet`](chapters/04-interfaces.md#interface-twenty-five-g-ethernet) | 4 | Ethernet | 285 | `04-interfaces.md` |
| [`interface two-hundred-g-ethernet`](chapters/04-interfaces.md#interface-two-hundred-g-ethernet) | 4 | Ethernet | 289 | `04-interfaces.md` |
| [`show dwdm channels`](chapters/04-interfaces.md#show-dwdm-channels) | 4 | Ethernet | 293 | `04-interfaces.md` |
| [`show interface description`](chapters/04-interfaces.md#show-interface-description) | 4 | Ethernet | 295 | `04-interfaces.md` |
| [`show interface forty-gigabit-ethernet`](chapters/04-interfaces.md#show-interface-forty-gigabit-ethernet) | 4 | Ethernet | 298 | `04-interfaces.md` |
| [`show interface four-hundred-g-ethernet`](chapters/04-interfaces.md#show-interface-four-hundred-g-ethernet) | 4 | Ethernet | 301 | `04-interfaces.md` |
| [`show interface gigabit-ethernet`](chapters/04-interfaces.md#show-interface-gigabit-ethernet) | 4 | Ethernet | 305 | `04-interfaces.md` |
| [`show interface hundred-gigabit-ethernet`](chapters/04-interfaces.md#show-interface-hundred-gigabit-ethernet) | 4 | Ethernet | 308 | `04-interfaces.md` |
| [`show interface link`](chapters/04-interfaces.md#show-interface-link) | 4 | Ethernet | 311 | `04-interfaces.md` |
| [`show interface ten-gigabit-ethernet`](chapters/04-interfaces.md#show-interface-ten-gigabit-ethernet) | 4 | Ethernet | 315 | `04-interfaces.md` |
| [`show interface twenty-five-g-ethernet`](chapters/04-interfaces.md#show-interface-twenty-five-g-ethernet) | 4 | Ethernet | 318 | `04-interfaces.md` |
| [`show interface two-hundred-g-ethernet`](chapters/04-interfaces.md#show-interface-two-hundred-g-ethernet) | 4 | Ethernet | 322 | `04-interfaces.md` |
| [`interface l3`](chapters/04-interfaces.md#interface-l3) | 4 | L3 | 325 | `04-interfaces.md` |
| [`interface l3 vrf`](chapters/04-interfaces.md#interface-l3-vrf) | 4 | L3 | 332 | `04-interfaces.md` |
| [`show ip interface`](chapters/04-interfaces.md#show-ip-interface) | 4 | L3 | 335 | `04-interfaces.md` |
| [`show ipv6 interface`](chapters/04-interfaces.md#show-ipv6-interface) | 4 | L3 | 339 | `04-interfaces.md` |
| [`show router vrrp`](chapters/04-interfaces.md#show-router-vrrp) | 4 | L3 | 342 | `04-interfaces.md` |
| [`interface loopback`](chapters/04-interfaces.md#interface-loopback) | 4 | Loopback | 345 | `04-interfaces.md` |
| [`interface loopback vrf`](chapters/04-interfaces.md#interface-loopback-vrf) | 4 | Loopback | 349 | `04-interfaces.md` |
| [`edfa`](chapters/04-interfaces.md#edfa) | 4 | EDFA | 351 | `04-interfaces.md` |
| [`show edfa`](chapters/04-interfaces.md#show-edfa) | 4 | EDFA | 358 | `04-interfaces.md` |
| [`line-protection`](chapters/04-interfaces.md#line-protection) | 4 | Line-Protection | 363 | `04-interfaces.md` |
| [`show line-protection`](chapters/04-interfaces.md#show-line-protection) | 4 | Line-Protection | 368 | `04-interfaces.md` |
| [`clear mac-address-table`](chapters/05-layer-2-switching-protocols.md#clear-mac-address-table) | 5 | MAC Learning | 372 | `05-layer-2-switching-protocols.md` |
| [`mac-address-table aging-time`](chapters/05-layer-2-switching-protocols.md#mac-address-table-aging-time) | 5 | MAC Learning | 375 | `05-layer-2-switching-protocols.md` |
| [`mac-address-table interface learning`](chapters/05-layer-2-switching-protocols.md#mac-address-table-interface-learning) | 5 | MAC Learning | 377 | `05-layer-2-switching-protocols.md` |
| [`mac-address-table interface limit`](chapters/05-layer-2-switching-protocols.md#mac-address-table-interface-limit) | 5 | MAC Learning | 380 | `05-layer-2-switching-protocols.md` |
| [`mac-address-table vlan learning`](chapters/05-layer-2-switching-protocols.md#mac-address-table-vlan-learning) | 5 | MAC Learning | 383 | `05-layer-2-switching-protocols.md` |
| [`mac-address-table vlan limit`](chapters/05-layer-2-switching-protocols.md#mac-address-table-vlan-limit) | 5 | MAC Learning | 385 | `05-layer-2-switching-protocols.md` |
| [`show mac-address-table`](chapters/05-layer-2-switching-protocols.md#show-mac-address-table) | 5 | MAC Learning | 388 | `05-layer-2-switching-protocols.md` |
| [`dot1q vlan`](chapters/05-layer-2-switching-protocols.md#dot1q-vlan) | 5 | VLAN | 392 | `05-layer-2-switching-protocols.md` |
| [`dot1q vlan interface`](chapters/05-layer-2-switching-protocols.md#dot1q-vlan-interface) | 5 | VLAN | 394 | `05-layer-2-switching-protocols.md` |
| [`show dot1q vlan`](chapters/05-layer-2-switching-protocols.md#show-dot1q-vlan) | 5 | VLAN | 397 | `05-layer-2-switching-protocols.md` |
| [`switchport acceptable-frame-types`](chapters/05-layer-2-switching-protocols.md#switchport-acceptable-frame-types) | 5 | VLAN | 401 | `05-layer-2-switching-protocols.md` |
| [`switchport native-vlan`](chapters/05-layer-2-switching-protocols.md#switchport-native-vlan) | 5 | VLAN | 403 | `05-layer-2-switching-protocols.md` |
| [`switchport pcp`](chapters/05-layer-2-switching-protocols.md#switchport-pcp) | 5 | VLAN | 406 | `05-layer-2-switching-protocols.md` |
| [`switchport qinq`](chapters/05-layer-2-switching-protocols.md#switchport-qinq) | 5 | VLAN | 409 | `05-layer-2-switching-protocols.md` |
| [`switchport tpid`](chapters/05-layer-2-switching-protocols.md#switchport-tpid) | 5 | VLAN | 412 | `05-layer-2-switching-protocols.md` |
| [`vlan-mapping`](chapters/05-layer-2-switching-protocols.md#vlan-mapping) | 5 | VLAN | 414 | `05-layer-2-switching-protocols.md` |
| [`clear lacp`](chapters/05-layer-2-switching-protocols.md#clear-lacp) | 5 | Link Aggregation | 419 | `05-layer-2-switching-protocols.md` |
| [`link-aggregation`](chapters/05-layer-2-switching-protocols.md#link-aggregation) | 5 | Link Aggregation | 421 | `05-layer-2-switching-protocols.md` |
| [`link-aggregation mc-lag redundancy-group`](chapters/05-layer-2-switching-protocols.md#link-aggregation-mc-lag-redundancy-group) | 5 | Link Aggregation | 429 | `05-layer-2-switching-protocols.md` |
| [`show link-aggregation`](chapters/05-layer-2-switching-protocols.md#show-link-aggregation) | 5 | Link Aggregation | 433 | `05-layer-2-switching-protocols.md` |
| [`show spanning-tree`](chapters/05-layer-2-switching-protocols.md#show-spanning-tree) | 5 | Spanning-Tree | 441 | `05-layer-2-switching-protocols.md` |
| [`spanning-tree`](chapters/05-layer-2-switching-protocols.md#spanning-tree) | 5 | Spanning-Tree | 445 | `05-layer-2-switching-protocols.md` |
| [`spanning-tree mst`](chapters/05-layer-2-switching-protocols.md#spanning-tree-mst) | 5 | Spanning-Tree | 451 | `05-layer-2-switching-protocols.md` |
| [`erps ring`](chapters/05-layer-2-switching-protocols.md#erps-ring) | 5 | ERPS | 454 | `05-layer-2-switching-protocols.md` |
| [`show erps`](chapters/05-layer-2-switching-protocols.md#show-erps) | 5 | ERPS | 461 | `05-layer-2-switching-protocols.md` |
| [`eaps`](chapters/05-layer-2-switching-protocols.md#eaps) | 5 | EAPS | 465 | `05-layer-2-switching-protocols.md` |
| [`show eaps`](chapters/05-layer-2-switching-protocols.md#show-eaps) | 5 | EAPS | 470 | `05-layer-2-switching-protocols.md` |
| [`layer2-control-protocol interface protocols action action-type`](chapters/05-layer-2-switching-protocols.md#layer2-control-protocol-interface-protocols-action-action-type) | 5 | Control Protocols | 474 | `05-layer-2-switching-protocols.md` |
| [`layer2-control-protocol tunnel-mac`](chapters/05-layer-2-switching-protocols.md#layer2-control-protocol-tunnel-mac) | 5 | Control Protocols | 478 | `05-layer-2-switching-protocols.md` |
| [`layer2-control-protocol tunnel-priority`](chapters/05-layer-2-switching-protocols.md#layer2-control-protocol-tunnel-priority) | 5 | Control Protocols | 480 | `05-layer-2-switching-protocols.md` |
| [`layer2-control-protocol vlan protocols action action-type`](chapters/05-layer-2-switching-protocols.md#layer2-control-protocol-vlan-protocols-action-action-type) | 5 | Control Protocols | 482 | `05-layer-2-switching-protocols.md` |
| [`loopback-detection`](chapters/05-layer-2-switching-protocols.md#loopback-detection) | 5 | Loopback Detection | 485 | `05-layer-2-switching-protocols.md` |
| [`show loopback detection`](chapters/05-layer-2-switching-protocols.md#show-loopback-detection) | 5 | Loopback Detection | 488 | `05-layer-2-switching-protocols.md` |
| [`link-flap`](chapters/05-layer-2-switching-protocols.md#link-flap) | 5 | Link Flap Detection | 491 | `05-layer-2-switching-protocols.md` |
| [`show link-flap`](chapters/05-layer-2-switching-protocols.md#show-link-flap) | 5 | Link Flap Detection | 494 | `05-layer-2-switching-protocols.md` |
| [`hold-time`](chapters/05-layer-2-switching-protocols.md#hold-time) | 5 | Hold Time | 498 | `05-layer-2-switching-protocols.md` |
| [`backup-link`](chapters/05-layer-2-switching-protocols.md#backup-link) | 5 | Backup Link | 500 | `05-layer-2-switching-protocols.md` |
| [`clear ip host-table`](chapters/06-layer-3-routing.md#clear-ip-host-table) | 6 | Basic | 504 | `06-layer-3-routing.md` |
| [`ip arp aging-time`](chapters/06-layer-3-routing.md#ip-arp-aging-time) | 6 | Basic | 507 | `06-layer-3-routing.md` |
| [`prefix-list`](chapters/06-layer-3-routing.md#prefix-list) | 6 | Basic | 509 | `06-layer-3-routing.md` |
| [`router static address-family ipv4`](chapters/06-layer-3-routing.md#router-static-address-family-ipv4) | 6 | Basic | 513 | `06-layer-3-routing.md` |
| [`router static address-family ipv6`](chapters/06-layer-3-routing.md#router-static-address-family-ipv6) | 6 | Basic | 517 | `06-layer-3-routing.md` |
| [`show ip fib`](chapters/06-layer-3-routing.md#show-ip-fib) | 6 | Basic | 521 | `06-layer-3-routing.md` |
| [`show ip host-table`](chapters/06-layer-3-routing.md#show-ip-host-table) | 6 | Basic | 525 | `06-layer-3-routing.md` |
| [`show ip rib`](chapters/06-layer-3-routing.md#show-ip-rib) | 6 | Basic | 529 | `06-layer-3-routing.md` |
| [`show ip route`](chapters/06-layer-3-routing.md#show-ip-route) | 6 | Basic | 533 | `06-layer-3-routing.md` |
| [`show ipv6 fib`](chapters/06-layer-3-routing.md#show-ipv6-fib) | 6 | Basic | 537 | `06-layer-3-routing.md` |
| [`show ipv6 host-table`](chapters/06-layer-3-routing.md#show-ipv6-host-table) | 6 | Basic | 541 | `06-layer-3-routing.md` |
| [`show ipv6 rib`](chapters/06-layer-3-routing.md#show-ipv6-rib) | 6 | Basic | 545 | `06-layer-3-routing.md` |
| [`show ipv6 route`](chapters/06-layer-3-routing.md#show-ipv6-route) | 6 | Basic | 549 | `06-layer-3-routing.md` |
| [`show bfd session`](chapters/06-layer-3-routing.md#show-bfd-session) | 6 | BFD | 553 | `06-layer-3-routing.md` |
| [`clear bgp neighbor`](chapters/06-layer-3-routing.md#clear-bgp-neighbor) | 6 | BGP | 556 | `06-layer-3-routing.md` |
| [`clear bgp soft`](chapters/06-layer-3-routing.md#clear-bgp-soft) | 6 | BGP | 559 | `06-layer-3-routing.md` |
| [`router bgp`](chapters/06-layer-3-routing.md#router-bgp) | 6 | BGP | 562 | `06-layer-3-routing.md` |
| [`router bgp address-family`](chapters/06-layer-3-routing.md#router-bgp-address-family) | 6 | BGP | 564 | `06-layer-3-routing.md` |
| [`router bgp address-family`](chapters/06-layer-3-routing.md#router-bgp-address-family) | 6 | BGP | 567 | `06-layer-3-routing.md` |
| [`router bgp administrative-status`](chapters/06-layer-3-routing.md#router-bgp-administrative-status) | 6 | BGP | 570 | `06-layer-3-routing.md` |
| [`router bgp as-size`](chapters/06-layer-3-routing.md#router-bgp-as-size) | 6 | BGP | 572 | `06-layer-3-routing.md` |
| [`router bgp bgp cluster-id`](chapters/06-layer-3-routing.md#router-bgp-bgp-cluster-id) | 6 | BGP | 574 | `06-layer-3-routing.md` |
| [`router bgp bgp default-local-preference`](chapters/06-layer-3-routing.md#router-bgp-bgp-default-local-preference) | 6 | BGP | 576 | `06-layer-3-routing.md` |
| [`router bgp neighbor`](chapters/06-layer-3-routing.md#router-bgp-neighbor) | 6 | BGP | 578 | `06-layer-3-routing.md` |
| [`router bgp neighbor address-family`](chapters/06-layer-3-routing.md#router-bgp-neighbor-address-family) | 6 | BGP | 580 | `06-layer-3-routing.md` |
| [`router bgp neighbor address-family prefix-list`](chapters/06-layer-3-routing.md#router-bgp-neighbor-address-family-prefix-list) | 6 | BGP | 583 | `06-layer-3-routing.md` |
| [`router bgp neighbor address-family vpn`](chapters/06-layer-3-routing.md#router-bgp-neighbor-address-family-vpn) | 6 | BGP | 586 | `06-layer-3-routing.md` |
| [`router bgp neighbor administrative-status`](chapters/06-layer-3-routing.md#router-bgp-neighbor-administrative-status) | 6 | BGP | 589 | `06-layer-3-routing.md` |
| [`router bgp neighbor description`](chapters/06-layer-3-routing.md#router-bgp-neighbor-description) | 6 | BGP | 592 | `06-layer-3-routing.md` |
| [`router bgp neighbor ebgp-multihop`](chapters/06-layer-3-routing.md#router-bgp-neighbor-ebgp-multihop) | 6 | BGP | 595 | `06-layer-3-routing.md` |
| [`router bgp neighbor enforce-first-as`](chapters/06-layer-3-routing.md#router-bgp-neighbor-enforce-first-as) | 6 | BGP | 598 | `06-layer-3-routing.md` |
| [`router bgp neighbor maximum-prefix`](chapters/06-layer-3-routing.md#router-bgp-neighbor-maximum-prefix) | 6 | BGP | 601 | `06-layer-3-routing.md` |
| [`router bgp neighbor maximum-prefix-action`](chapters/06-layer-3-routing.md#router-bgp-neighbor-maximum-prefix-action) | 6 | BGP | 604 | `06-layer-3-routing.md` |
| [`router bgp neighbor next-hop-self`](chapters/06-layer-3-routing.md#router-bgp-neighbor-next-hop-self) | 6 | BGP | 607 | `06-layer-3-routing.md` |
| [`router bgp neighbor password`](chapters/06-layer-3-routing.md#router-bgp-neighbor-password) | 6 | BGP | 610 | `06-layer-3-routing.md` |
| [`router bgp neighbor remote-as`](chapters/06-layer-3-routing.md#router-bgp-neighbor-remote-as) | 6 | BGP | 613 | `06-layer-3-routing.md` |
| [`router bgp neighbor remove-private-as`](chapters/06-layer-3-routing.md#router-bgp-neighbor-remove-private-as) | 6 | BGP | 616 | `06-layer-3-routing.md` |
| [`router bgp neighbor route-policy`](chapters/06-layer-3-routing.md#router-bgp-neighbor-route-policy) | 6 | BGP | 618 | `06-layer-3-routing.md` |
| [`router bgp neighbor route-reflector`](chapters/06-layer-3-routing.md#router-bgp-neighbor-route-reflector) | 6 | BGP | 621 | `06-layer-3-routing.md` |
| [`router bgp neighbor timers hold-time`](chapters/06-layer-3-routing.md#router-bgp-neighbor-timers-hold-time) | 6 | BGP | 624 | `06-layer-3-routing.md` |
| [`router bgp neighbor timers keepalive`](chapters/06-layer-3-routing.md#router-bgp-neighbor-timers-keepalive) | 6 | BGP | 627 | `06-layer-3-routing.md` |
| [`router bgp neighbor update-source-address`](chapters/06-layer-3-routing.md#router-bgp-neighbor-update-source-address) | 6 | BGP | 630 | `06-layer-3-routing.md` |
| [`router bgp network address-family ipv4`](chapters/06-layer-3-routing.md#router-bgp-network-address-family-ipv4) | 6 | BGP | 633 | `06-layer-3-routing.md` |
| [`router bgp network address-family ipv6`](chapters/06-layer-3-routing.md#router-bgp-network-address-family-ipv6) | 6 | BGP | 636 | `06-layer-3-routing.md` |
| [`router bgp prefix-list`](chapters/06-layer-3-routing.md#router-bgp-prefix-list) | 6 | BGP | 639 | `06-layer-3-routing.md` |
| [`router bgp redistribute`](chapters/06-layer-3-routing.md#router-bgp-redistribute) | 6 | BGP | 644 | `06-layer-3-routing.md` |
| [`router bgp redistribute administrative-status`](chapters/06-layer-3-routing.md#router-bgp-redistribute-administrative-status) | 6 | BGP | 647 | `06-layer-3-routing.md` |
| [`router bgp redistribute match-address address-family ipv4`](chapters/06-layer-3-routing.md#router-bgp-redistribute-match-address-address-family-ipv4) | 6 | BGP | 650 | `06-layer-3-routing.md` |
| [`router bgp redistribute match-address address-family ipv6`](chapters/06-layer-3-routing.md#router-bgp-redistribute-match-address-address-family-ipv6) | 6 | BGP | 653 | `06-layer-3-routing.md` |
| [`router bgp route-map`](chapters/06-layer-3-routing.md#router-bgp-route-map) | 6 | BGP | 656 | `06-layer-3-routing.md` |
| [`router bgp route-map match-community`](chapters/06-layer-3-routing.md#router-bgp-route-map-match-community) | 6 | BGP | 662 | `06-layer-3-routing.md` |
| [`router bgp route-map match-extended-community`](chapters/06-layer-3-routing.md#router-bgp-route-map-match-extended-community) | 6 | BGP | 665 | `06-layer-3-routing.md` |
| [`router bgp route-map set-community`](chapters/06-layer-3-routing.md#router-bgp-route-map-set-community) | 6 | BGP | 668 | `06-layer-3-routing.md` |
| [`router bgp route-map set-community-action`](chapters/06-layer-3-routing.md#router-bgp-route-map-set-community-action) | 6 | BGP | 671 | `06-layer-3-routing.md` |
| [`router bgp route-policy`](chapters/06-layer-3-routing.md#router-bgp-route-policy) | 6 | BGP | 674 | `06-layer-3-routing.md` |
| [`router bgp router-id`](chapters/06-layer-3-routing.md#router-bgp-router-id) | 6 | BGP | 677 | `06-layer-3-routing.md` |
| [`router bgp vrf`](chapters/06-layer-3-routing.md#router-bgp-vrf) | 6 | BGP | 679 | `06-layer-3-routing.md` |
| [`router bgp vrf address-family`](chapters/06-layer-3-routing.md#router-bgp-vrf-address-family) | 6 | BGP | 681 | `06-layer-3-routing.md` |
| [`router bgp vrf address-family network`](chapters/06-layer-3-routing.md#router-bgp-vrf-address-family-network) | 6 | BGP | 684 | `06-layer-3-routing.md` |
| [`router bgp vrf address-family redistribute match-address`](chapters/06-layer-3-routing.md#router-bgp-vrf-address-family-redistribute-match-address) | 6 | BGP | 687 | `06-layer-3-routing.md` |
| [`router bgp vrf address-family { ipv4 \| ipv6 } unicast redistribute`](chapters/06-layer-3-routing.md#router-bgp-vrf-address-family-ipv4-ipv6-unicast-redistribute) | 6 | BGP | 690 | `06-layer-3-routing.md` |
| [`router bgp vrf address-family { ipv4 \| ipv6 } unicast redistribute administrative-status`](chapters/06-layer-3-routing.md#router-bgp-vrf-address-family-ipv4-ipv6-unicast-redistribute-administrative-status) | 6 | BGP | 694 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor) | 6 | BGP | 697 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor address-family`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor-address-family) | 6 | BGP | 700 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor address-family allow-as-in`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor-address-family-allow-as-in) | 6 | BGP | 703 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor address-family as-override`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor-address-family-as-override) | 6 | BGP | 706 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor address-family prefix-list`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor-address-family-prefix-list) | 6 | BGP | 709 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor administrative-status`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor-administrative-status) | 6 | BGP | 712 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor ebgp-multihop`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor-ebgp-multihop) | 6 | BGP | 715 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor next-hop-self`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor-next-hop-self) | 6 | BGP | 718 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor password`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor-password) | 6 | BGP | 721 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor remote-as`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor-remote-as) | 6 | BGP | 724 | `06-layer-3-routing.md` |
| [`router bgp vrf neighbor update-source-address`](chapters/06-layer-3-routing.md#router-bgp-vrf-neighbor-update-source-address) | 6 | BGP | 727 | `06-layer-3-routing.md` |
| [`router bgp vrf route-map set-community`](chapters/06-layer-3-routing.md#router-bgp-vrf-route-map-set-community) | 6 | BGP | 730 | `06-layer-3-routing.md` |
| [`router bgp vrf router-id`](chapters/06-layer-3-routing.md#router-bgp-vrf-router-id) | 6 | BGP | 733 | `06-layer-3-routing.md` |
| [`show ip bgp`](chapters/06-layer-3-routing.md#show-ip-bgp) | 6 | BGP | 736 | `06-layer-3-routing.md` |
| [`show ip bgp community`](chapters/06-layer-3-routing.md#show-ip-bgp-community) | 6 | BGP | 741 | `06-layer-3-routing.md` |
| [`show ip bgp neighbor`](chapters/06-layer-3-routing.md#show-ip-bgp-neighbor) | 6 | BGP | 744 | `06-layer-3-routing.md` |
| [`show ip bgp prefixes`](chapters/06-layer-3-routing.md#show-ip-bgp-prefixes) | 6 | BGP | 756 | `06-layer-3-routing.md` |
| [`show ip bgp vpnv4 labels`](chapters/06-layer-3-routing.md#show-ip-bgp-vpnv4-labels) | 6 | BGP | 761 | `06-layer-3-routing.md` |
| [`show ip bgp vpnv6 labels`](chapters/06-layer-3-routing.md#show-ip-bgp-vpnv6-labels) | 6 | BGP | 765 | `06-layer-3-routing.md` |
| [`clear ospf`](chapters/06-layer-3-routing.md#clear-ospf) | 6 | OSPF | 768 | `06-layer-3-routing.md` |
| [`router ospf`](chapters/06-layer-3-routing.md#router-ospf) | 6 | OSPF | 771 | `06-layer-3-routing.md` |
| [`router ospf administrative-status`](chapters/06-layer-3-routing.md#router-ospf-administrative-status) | 6 | OSPF | 774 | `06-layer-3-routing.md` |
| [`router ospf area`](chapters/06-layer-3-routing.md#router-ospf-area) | 6 | OSPF | 776 | `06-layer-3-routing.md` |
| [`router ospf area administrative-status`](chapters/06-layer-3-routing.md#router-ospf-area-administrative-status) | 6 | OSPF | 778 | `06-layer-3-routing.md` |
| [`router ospf area interface`](chapters/06-layer-3-routing.md#router-ospf-area-interface) | 6 | OSPF | 781 | `06-layer-3-routing.md` |
| [`router ospf area interface administrative-status`](chapters/06-layer-3-routing.md#router-ospf-area-interface-administrative-status) | 6 | OSPF | 784 | `06-layer-3-routing.md` |
| [`router ospf area interface authentication`](chapters/06-layer-3-routing.md#router-ospf-area-interface-authentication) | 6 | OSPF | 787 | `06-layer-3-routing.md` |
| [`router ospf area interface authentication-key`](chapters/06-layer-3-routing.md#router-ospf-area-interface-authentication-key) | 6 | OSPF | 790 | `06-layer-3-routing.md` |
| [`router ospf area interface bfd session-type`](chapters/06-layer-3-routing.md#router-ospf-area-interface-bfd-session-type) | 6 | OSPF | 793 | `06-layer-3-routing.md` |
| [`router ospf area interface cost`](chapters/06-layer-3-routing.md#router-ospf-area-interface-cost) | 6 | OSPF | 796 | `06-layer-3-routing.md` |
| [`router ospf area interface dead-interval`](chapters/06-layer-3-routing.md#router-ospf-area-interface-dead-interval) | 6 | OSPF | 799 | `06-layer-3-routing.md` |
| [`router ospf area interface hello-interval`](chapters/06-layer-3-routing.md#router-ospf-area-interface-hello-interval) | 6 | OSPF | 802 | `06-layer-3-routing.md` |
| [`router ospf area interface mtu-ignore`](chapters/06-layer-3-routing.md#router-ospf-area-interface-mtu-ignore) | 6 | OSPF | 805 | `06-layer-3-routing.md` |
| [`router ospf area interface network-type`](chapters/06-layer-3-routing.md#router-ospf-area-interface-network-type) | 6 | OSPF | 808 | `06-layer-3-routing.md` |
| [`router ospf area interface passive`](chapters/06-layer-3-routing.md#router-ospf-area-interface-passive) | 6 | OSPF | 811 | `06-layer-3-routing.md` |
| [`router ospf area interface router-priority`](chapters/06-layer-3-routing.md#router-ospf-area-interface-router-priority) | 6 | OSPF | 814 | `06-layer-3-routing.md` |
| [`router ospf area nssa`](chapters/06-layer-3-routing.md#router-ospf-area-nssa) | 6 | OSPF | 817 | `06-layer-3-routing.md` |
| [`router ospf area range`](chapters/06-layer-3-routing.md#router-ospf-area-range) | 6 | OSPF | 820 | `06-layer-3-routing.md` |
| [`router ospf area stub`](chapters/06-layer-3-routing.md#router-ospf-area-stub) | 6 | OSPF | 823 | `06-layer-3-routing.md` |
| [`router ospf auto-cost reference-bandwidth`](chapters/06-layer-3-routing.md#router-ospf-auto-cost-reference-bandwidth) | 6 | OSPF | 826 | `06-layer-3-routing.md` |
| [`router ospf export-prefix-list`](chapters/06-layer-3-routing.md#router-ospf-export-prefix-list) | 6 | OSPF | 829 | `06-layer-3-routing.md` |
| [`router ospf import-prefix-list`](chapters/06-layer-3-routing.md#router-ospf-import-prefix-list) | 6 | OSPF | 831 | `06-layer-3-routing.md` |
| [`router ospf max-metric`](chapters/06-layer-3-routing.md#router-ospf-max-metric) | 6 | OSPF | 834 | `06-layer-3-routing.md` |
| [`router ospf maximum paths`](chapters/06-layer-3-routing.md#router-ospf-maximum-paths) | 6 | OSPF | 837 | `06-layer-3-routing.md` |
| [`router ospf mpls-te router-id`](chapters/06-layer-3-routing.md#router-ospf-mpls-te-router-id) | 6 | OSPF | 839 | `06-layer-3-routing.md` |
| [`router ospf redistribute`](chapters/06-layer-3-routing.md#router-ospf-redistribute) | 6 | OSPF | 841 | `06-layer-3-routing.md` |
| [`router ospf rfc1583-compatible`](chapters/06-layer-3-routing.md#router-ospf-rfc1583-compatible) | 6 | OSPF | 845 | `06-layer-3-routing.md` |
| [`router ospf router-id`](chapters/06-layer-3-routing.md#router-ospf-router-id) | 6 | OSPF | 848 | `06-layer-3-routing.md` |
| [`router ospf timers lsa-arrival`](chapters/06-layer-3-routing.md#router-ospf-timers-lsa-arrival) | 6 | OSPF | 850 | `06-layer-3-routing.md` |
| [`router ospf timers throttle lsa-originate`](chapters/06-layer-3-routing.md#router-ospf-timers-throttle-lsa-originate) | 6 | OSPF | 853 | `06-layer-3-routing.md` |
| [`router ospf timers throttle spf`](chapters/06-layer-3-routing.md#router-ospf-timers-throttle-spf) | 6 | OSPF | 856 | `06-layer-3-routing.md` |
| [`show ip ospf`](chapters/06-layer-3-routing.md#show-ip-ospf) | 6 | OSPF | 859 | `06-layer-3-routing.md` |
| [`show ip ospf database`](chapters/06-layer-3-routing.md#show-ip-ospf-database) | 6 | OSPF | 863 | `06-layer-3-routing.md` |
| [`show ip ospf interface`](chapters/06-layer-3-routing.md#show-ip-ospf-interface) | 6 | OSPF | 870 | `06-layer-3-routing.md` |
| [`show ip ospf neighbor`](chapters/06-layer-3-routing.md#show-ip-ospf-neighbor) | 6 | OSPF | 879 | `06-layer-3-routing.md` |
| [`clear ospfv3`](chapters/06-layer-3-routing.md#clear-ospfv3) | 6 | OSPFv3 | 883 | `06-layer-3-routing.md` |
| [`router ospfv3`](chapters/06-layer-3-routing.md#router-ospfv3) | 6 | OSPFv3 | 885 | `06-layer-3-routing.md` |
| [`router ospfv3 administrative-status`](chapters/06-layer-3-routing.md#router-ospfv3-administrative-status) | 6 | OSPFv3 | 887 | `06-layer-3-routing.md` |
| [`router ospfv3 advertise-max-metric`](chapters/06-layer-3-routing.md#router-ospfv3-advertise-max-metric) | 6 | OSPFv3 | 889 | `06-layer-3-routing.md` |
| [`router ospfv3 area`](chapters/06-layer-3-routing.md#router-ospfv3-area) | 6 | OSPFv3 | 892 | `06-layer-3-routing.md` |
| [`router ospfv3 area administrative-status`](chapters/06-layer-3-routing.md#router-ospfv3-area-administrative-status) | 6 | OSPFv3 | 894 | `06-layer-3-routing.md` |
| [`router ospfv3 area interface`](chapters/06-layer-3-routing.md#router-ospfv3-area-interface) | 6 | OSPFv3 | 896 | `06-layer-3-routing.md` |
| [`router ospfv3 area interface administrative-status`](chapters/06-layer-3-routing.md#router-ospfv3-area-interface-administrative-status) | 6 | OSPFv3 | 898 | `06-layer-3-routing.md` |
| [`router ospfv3 area interface cost`](chapters/06-layer-3-routing.md#router-ospfv3-area-interface-cost) | 6 | OSPFv3 | 901 | `06-layer-3-routing.md` |
| [`router ospfv3 area interface dead-interval`](chapters/06-layer-3-routing.md#router-ospfv3-area-interface-dead-interval) | 6 | OSPFv3 | 904 | `06-layer-3-routing.md` |
| [`router ospfv3 area interface hello-interval`](chapters/06-layer-3-routing.md#router-ospfv3-area-interface-hello-interval) | 6 | OSPFv3 | 907 | `06-layer-3-routing.md` |
| [`router ospfv3 area interface mtu-ignore`](chapters/06-layer-3-routing.md#router-ospfv3-area-interface-mtu-ignore) | 6 | OSPFv3 | 910 | `06-layer-3-routing.md` |
| [`router ospfv3 area interface network-type`](chapters/06-layer-3-routing.md#router-ospfv3-area-interface-network-type) | 6 | OSPFv3 | 913 | `06-layer-3-routing.md` |
| [`router ospfv3 area interface passive`](chapters/06-layer-3-routing.md#router-ospfv3-area-interface-passive) | 6 | OSPFv3 | 916 | `06-layer-3-routing.md` |
| [`router ospfv3 area range`](chapters/06-layer-3-routing.md#router-ospfv3-area-range) | 6 | OSPFv3 | 919 | `06-layer-3-routing.md` |
| [`router ospfv3 maximum paths`](chapters/06-layer-3-routing.md#router-ospfv3-maximum-paths) | 6 | OSPFv3 | 922 | `06-layer-3-routing.md` |
| [`router ospfv3 redistribute`](chapters/06-layer-3-routing.md#router-ospfv3-redistribute) | 6 | OSPFv3 | 924 | `06-layer-3-routing.md` |
| [`router ospfv3 router-id`](chapters/06-layer-3-routing.md#router-ospfv3-router-id) | 6 | OSPFv3 | 927 | `06-layer-3-routing.md` |
| [`router ospfv3 timers lsa-arrival`](chapters/06-layer-3-routing.md#router-ospfv3-timers-lsa-arrival) | 6 | OSPFv3 | 929 | `06-layer-3-routing.md` |
| [`router ospfv3 timers throttle lsa-originate`](chapters/06-layer-3-routing.md#router-ospfv3-timers-throttle-lsa-originate) | 6 | OSPFv3 | 931 | `06-layer-3-routing.md` |
| [`router ospfv3 timers throttle spf`](chapters/06-layer-3-routing.md#router-ospfv3-timers-throttle-spf) | 6 | OSPFv3 | 934 | `06-layer-3-routing.md` |
| [`show ipv6 ospf`](chapters/06-layer-3-routing.md#show-ipv6-ospf) | 6 | OSPFv3 | 937 | `06-layer-3-routing.md` |
| [`show ipv6 ospf database`](chapters/06-layer-3-routing.md#show-ipv6-ospf-database) | 6 | OSPFv3 | 940 | `06-layer-3-routing.md` |
| [`show ipv6 ospf neighbor`](chapters/06-layer-3-routing.md#show-ipv6-ospf-neighbor) | 6 | OSPFv3 | 949 | `06-layer-3-routing.md` |
| [`router vrrp`](chapters/06-layer-3-routing.md#router-vrrp) | 6 | VRRP | 952 | `06-layer-3-routing.md` |
| [`router vrrp interface`](chapters/06-layer-3-routing.md#router-vrrp-interface) | 6 | VRRP | 954 | `06-layer-3-routing.md` |
| [`router vrrp interface address-family`](chapters/06-layer-3-routing.md#router-vrrp-interface-address-family) | 6 | VRRP | 956 | `06-layer-3-routing.md` |
| [`router vrrp interface address-family vr-id`](chapters/06-layer-3-routing.md#router-vrrp-interface-address-family-vr-id) | 6 | VRRP | 958 | `06-layer-3-routing.md` |
| [`router vrrp interface address-family vr-id address`](chapters/06-layer-3-routing.md#router-vrrp-interface-address-family-vr-id-address) | 6 | VRRP | 960 | `06-layer-3-routing.md` |
| [`router vrrp interface address-family vr-id administrative-status`](chapters/06-layer-3-routing.md#router-vrrp-interface-address-family-vr-id-administrative-status) | 6 | VRRP | 963 | `06-layer-3-routing.md` |
| [`router vrrp interface address-family vr-id advertisement-interval`](chapters/06-layer-3-routing.md#router-vrrp-interface-address-family-vr-id-advertisement-interval) | 6 | VRRP | 966 | `06-layer-3-routing.md` |
| [`router vrrp interface address-family vr-id authentication`](chapters/06-layer-3-routing.md#router-vrrp-interface-address-family-vr-id-authentication) | 6 | VRRP | 969 | `06-layer-3-routing.md` |
| [`router vrrp interface address-family vr-id preempt`](chapters/06-layer-3-routing.md#router-vrrp-interface-address-family-vr-id-preempt) | 6 | VRRP | 972 | `06-layer-3-routing.md` |
| [`router vrrp interface address-family vr-id priority`](chapters/06-layer-3-routing.md#router-vrrp-interface-address-family-vr-id-priority) | 6 | VRRP | 975 | `06-layer-3-routing.md` |
| [`router vrrp interface address-family vr-id track`](chapters/06-layer-3-routing.md#router-vrrp-interface-address-family-vr-id-track) | 6 | VRRP | 978 | `06-layer-3-routing.md` |
| [`router vrrp interface address-family vr-id version`](chapters/06-layer-3-routing.md#router-vrrp-interface-address-family-vr-id-version) | 6 | VRRP | 981 | `06-layer-3-routing.md` |
| [`router pbr`](chapters/06-layer-3-routing.md#router-pbr) | 6 | PBR | 984 | `06-layer-3-routing.md` |
| [`show router pbr`](chapters/06-layer-3-routing.md#show-router-pbr) | 6 | PBR | 989 | `06-layer-3-routing.md` |
| [`vrf`](chapters/06-layer-3-routing.md#vrf) | 6 | VRF | 992 | `06-layer-3-routing.md` |
| [`vrf address-family ipv4 unicast`](chapters/06-layer-3-routing.md#vrf-address-family-ipv4-unicast) | 6 | VRF | 995 | `06-layer-3-routing.md` |
| [`vrf rd`](chapters/06-layer-3-routing.md#vrf-rd) | 6 | VRF | 997 | `06-layer-3-routing.md` |
| [`vrf route-target`](chapters/06-layer-3-routing.md#vrf-route-target) | 6 | VRF | 999 | `06-layer-3-routing.md` |
| [`show mpls forwarding-table`](chapters/07-mpls.md#show-mpls-forwarding-table) | 7 | Infra | 1002 | `07-mpls.md` |
| [`show mpls traffic-eng tunnel-te brief`](chapters/07-mpls.md#show-mpls-traffic-eng-tunnel-te-brief) | 7 | Infra | 1008 | `07-mpls.md` |
| [`show mpls traffic-eng tunnel-te id \| name`](chapters/07-mpls.md#show-mpls-traffic-eng-tunnel-te-id-name) | 7 | Infra | 1015 | `07-mpls.md` |
| [`clear mpls l2vpn counters vpls`](chapters/07-mpls.md#clear-mpls-l2vpn-counters-vpls) | 7 | L2VPN | 1020 | `07-mpls.md` |
| [`clear mpls l2vpn counters vpws`](chapters/07-mpls.md#clear-mpls-l2vpn-counters-vpws) | 7 | L2VPN | 1022 | `07-mpls.md` |
| [`clear mpls l2vpn mac-address vpls`](chapters/07-mpls.md#clear-mpls-l2vpn-mac-address-vpls) | 7 | L2VPN | 1024 | `07-mpls.md` |
| [`mpls l2vpn logging pw-status`](chapters/07-mpls.md#mpls-l2vpn-logging-pw-status) | 7 | L2VPN | 1026 | `07-mpls.md` |
| [`mpls l2vpn vpls-group`](chapters/07-mpls.md#mpls-l2vpn-vpls-group) | 7 | L2VPN | 1028 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn) | 7 | L2VPN | 1030 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn administrative-status`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-administrative-status) | 7 | L2VPN | 1032 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain) | 7 | L2VPN | 1035 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain access-interface`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain-access-interface) | 7 | L2VPN | 1038 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain access-interface administrative-status`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain-access-interface-administrative-status) | 7 | L2VPN | 1041 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain access-interface encapsulation dot1q`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain-access-interface-encapsulation-dot1q) | 7 | L2VPN | 1044 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain access-interface encapsulation untagged`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain-access-interface-encapsulation-untagged) | 7 | L2VPN | 1047 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain administrative-status`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain-administrative-status) | 7 | L2VPN | 1050 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain bridge-mtu`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain-bridge-mtu) | 7 | L2VPN | 1053 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain dot1q`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain-dot1q) | 7 | L2VPN | 1056 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain mac-limit`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain-mac-limit) | 7 | L2VPN | 1059 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain qinq`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain-qinq) | 7 | L2VPN | 1062 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn bridge-domain transparent-lanservice`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-bridge-domain-transparent-lanservice) | 7 | L2VPN | 1065 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn description`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-description) | 7 | L2VPN | 1068 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi) | 7 | L2VPN | 1071 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi administrative-status`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi-administrative-status) | 7 | L2VPN | 1074 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi neighbor`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi-neighbor) | 7 | L2VPN | 1077 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi neighbor administrative-status`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi-neighbor-administrative-status) | 7 | L2VPN | 1080 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi neighbor pw-id`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi-neighbor-pw-id) | 7 | L2VPN | 1083 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi neighbor pw-load-balance`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi-neighbor-pw-load-balance) | 7 | L2VPN | 1086 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi neighbor pw-load-balance flow-label`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi-neighbor-pw-load-balance-flow-label) | 7 | L2VPN | 1089 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi neighbor pw-mtu`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi-neighbor-pw-mtu) | 7 | L2VPN | 1092 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi neighbor split-horizon`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi-neighbor-split-horizon) | 7 | L2VPN | 1095 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi neighbor tunnel-interface`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi-neighbor-tunnel-interface) | 7 | L2VPN | 1098 | `07-mpls.md` |
| [`mpls l2vpn vpls-group vpn vfi pw-type`](chapters/07-mpls.md#mpls-l2vpn-vpls-group-vpn-vfi-pw-type) | 7 | L2VPN | 1101 | `07-mpls.md` |
| [`mpls l2vpn vpws-group`](chapters/07-mpls.md#mpls-l2vpn-vpws-group) | 7 | L2VPN | 1104 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn) | 7 | L2VPN | 1106 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn access-interface`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-access-interface) | 7 | L2VPN | 1108 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn access-interface administrative-status`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-access-interface-administrative-status) | 7 | L2VPN | 1111 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn access-interface dot1q`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-access-interface-dot1q) | 7 | L2VPN | 1114 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn access-interface encapsulation dot1q`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-access-interface-encapsulation-dot1q) | 7 | L2VPN | 1117 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn access-interface encapsulation untagged`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-access-interface-encapsulation-untagged) | 7 | L2VPN | 1120 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn access-interface mtu`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-access-interface-mtu) | 7 | L2VPN | 1123 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn administrative-status`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-administrative-status) | 7 | L2VPN | 1126 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn backup-neighbor`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-backup-neighbor) | 7 | L2VPN | 1129 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn description`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-description) | 7 | L2VPN | 1132 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn neighbor`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-neighbor) | 7 | L2VPN | 1135 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn neighbor administrative-status`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-neighbor-administrative-status) | 7 | L2VPN | 1138 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn neighbor pw-id`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-neighbor-pw-id) | 7 | L2VPN | 1141 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn neighbor pw-load-balance`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-neighbor-pw-load-balance) | 7 | L2VPN | 1144 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn neighbor pw-load-balance flow-label`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-neighbor-pw-load-balance-flow-label) | 7 | L2VPN | 1147 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn neighbor pw-mtu`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-neighbor-pw-mtu) | 7 | L2VPN | 1150 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn neighbor pw-type`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-neighbor-pw-type) | 7 | L2VPN | 1153 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn neighbor tunnel-interface`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-neighbor-tunnel-interface) | 7 | L2VPN | 1156 | `07-mpls.md` |
| [`mpls l2vpn vpws-group vpn qinq`](chapters/07-mpls.md#mpls-l2vpn-vpws-group-vpn-qinq) | 7 | L2VPN | 1159 | `07-mpls.md` |
| [`show mpls l2vpn counters`](chapters/07-mpls.md#show-mpls-l2vpn-counters) | 7 | L2VPN | 1162 | `07-mpls.md` |
| [`show mpls l2vpn hardware`](chapters/07-mpls.md#show-mpls-l2vpn-hardware) | 7 | L2VPN | 1166 | `07-mpls.md` |
| [`show mpls l2vpn vpls-group`](chapters/07-mpls.md#show-mpls-l2vpn-vpls-group) | 7 | L2VPN | 1172 | `07-mpls.md` |
| [`show mpls l2vpn vpws-group`](chapters/07-mpls.md#show-mpls-l2vpn-vpws-group) | 7 | L2VPN | 1179 | `07-mpls.md` |
| [`show mpls l3vpn`](chapters/07-mpls.md#show-mpls-l3vpn) | 7 | L3VPN | 1186 | `07-mpls.md` |
| [`interface tunnel-te`](chapters/07-mpls.md#interface-tunnel-te) | 7 | RSVP | 1190 | `07-mpls.md` |
| [`interface tunnel-te administrative-status`](chapters/07-mpls.md#interface-tunnel-te-administrative-status) | 7 | RSVP | 1192 | `07-mpls.md` |
| [`interface tunnel-te description`](chapters/07-mpls.md#interface-tunnel-te-description) | 7 | RSVP | 1194 | `07-mpls.md` |
| [`interface tunnel-te destination`](chapters/07-mpls.md#interface-tunnel-te-destination) | 7 | RSVP | 1196 | `07-mpls.md` |
| [`interface tunnel-te name`](chapters/07-mpls.md#interface-tunnel-te-name) | 7 | RSVP | 1198 | `07-mpls.md` |
| [`interface tunnel-te path-option`](chapters/07-mpls.md#interface-tunnel-te-path-option) | 7 | RSVP | 1200 | `07-mpls.md` |
| [`interface tunnel-te path-option`](chapters/07-mpls.md#interface-tunnel-te-path-option) | 7 | RSVP | 1202 | `07-mpls.md` |
| [`interface tunnel-te path-option dynamic attribute-set`](chapters/07-mpls.md#interface-tunnel-te-path-option-dynamic-attribute-set) | 7 | RSVP | 1205 | `07-mpls.md` |
| [`interface tunnel-te path-option explicit name`](chapters/07-mpls.md#interface-tunnel-te-path-option-explicit-name) | 7 | RSVP | 1208 | `07-mpls.md` |
| [`mpls rsvp`](chapters/07-mpls.md#mpls-rsvp) | 7 | RSVP | 1211 | `07-mpls.md` |
| [`mpls rsvp hello`](chapters/07-mpls.md#mpls-rsvp-hello) | 7 | RSVP | 1213 | `07-mpls.md` |
| [`mpls rsvp interface`](chapters/07-mpls.md#mpls-rsvp-interface) | 7 | RSVP | 1215 | `07-mpls.md` |
| [`mpls rsvp refresh`](chapters/07-mpls.md#mpls-rsvp-refresh) | 7 | RSVP | 1218 | `07-mpls.md` |
| [`mpls traffic-eng`](chapters/07-mpls.md#mpls-traffic-eng) | 7 | RSVP | 1220 | `07-mpls.md` |
| [`mpls traffic-eng attribute-set`](chapters/07-mpls.md#mpls-traffic-eng-attribute-set) | 7 | RSVP | 1222 | `07-mpls.md` |
| [`mpls traffic-eng attribute-set path-option`](chapters/07-mpls.md#mpls-traffic-eng-attribute-set-path-option) | 7 | RSVP | 1224 | `07-mpls.md` |
| [`mpls traffic-eng attribute-set path-option affinity-flags exclude-any`](chapters/07-mpls.md#mpls-traffic-eng-attribute-set-path-option-affinity-flags-exclude-any) | 7 | RSVP | 1227 | `07-mpls.md` |
| [`mpls traffic-eng attribute-set path-option affinity-flags include-all`](chapters/07-mpls.md#mpls-traffic-eng-attribute-set-path-option-affinity-flags-include-all) | 7 | RSVP | 1230 | `07-mpls.md` |
| [`mpls traffic-eng attribute-set path-option affinity-flags include-any`](chapters/07-mpls.md#mpls-traffic-eng-attribute-set-path-option-affinity-flags-include-any) | 7 | RSVP | 1233 | `07-mpls.md` |
| [`mpls traffic-eng explicit-path`](chapters/07-mpls.md#mpls-traffic-eng-explicit-path) | 7 | RSVP | 1236 | `07-mpls.md` |
| [`mpls traffic-eng explicit-path hop`](chapters/07-mpls.md#mpls-traffic-eng-explicit-path-hop) | 7 | RSVP | 1238 | `07-mpls.md` |
| [`mpls traffic-eng interface`](chapters/07-mpls.md#mpls-traffic-eng-interface) | 7 | RSVP | 1241 | `07-mpls.md` |
| [`mpls traffic-eng interface affinity-flags`](chapters/07-mpls.md#mpls-traffic-eng-interface-affinity-flags) | 7 | RSVP | 1243 | `07-mpls.md` |
| [`mpls ldp lsr-id`](chapters/07-mpls.md#mpls-ldp-lsr-id) | 7 | LDP | 1246 | `07-mpls.md` |
| [`mpls ldp lsr-id interface`](chapters/07-mpls.md#mpls-ldp-lsr-id-interface) | 7 | LDP | 1248 | `07-mpls.md` |
| [`mpls ldp lsr-id interface hello-holdtime`](chapters/07-mpls.md#mpls-ldp-lsr-id-interface-hello-holdtime) | 7 | LDP | 1250 | `07-mpls.md` |
| [`mpls ldp lsr-id interface keep-alive-holdtime`](chapters/07-mpls.md#mpls-ldp-lsr-id-interface-keep-alive-holdtime) | 7 | LDP | 1253 | `07-mpls.md` |
| [`mpls ldp lsr-id neighbor targeted`](chapters/07-mpls.md#mpls-ldp-lsr-id-neighbor-targeted) | 7 | LDP | 1256 | `07-mpls.md` |
| [`mpls ldp lsr-id neighbor targeted hello-holdtime`](chapters/07-mpls.md#mpls-ldp-lsr-id-neighbor-targeted-hello-holdtime) | 7 | LDP | 1258 | `07-mpls.md` |
| [`mpls ldp lsr-id neighbor targeted keep-alive-holdtime`](chapters/07-mpls.md#mpls-ldp-lsr-id-neighbor-targeted-keep-alive-holdtime) | 7 | LDP | 1261 | `07-mpls.md` |
| [`mpls ldp lsr-id neighbor targeted password`](chapters/07-mpls.md#mpls-ldp-lsr-id-neighbor-targeted-password) | 7 | LDP | 1264 | `07-mpls.md` |
| [`show mpls ldp database`](chapters/07-mpls.md#show-mpls-ldp-database) | 7 | LDP | 1267 | `07-mpls.md` |
| [`show mpls ldp neighbor`](chapters/07-mpls.md#show-mpls-ldp-neighbor) | 7 | LDP | 1270 | `07-mpls.md` |
| [`show mpls ldp parameters`](chapters/07-mpls.md#show-mpls-ldp-parameters) | 7 | LDP | 1274 | `07-mpls.md` |
| [`clear multicast igmp snooping statistics`](chapters/08-multicast.md#clear-multicast-igmp-snooping-statistics) | 8 | IGMP Snooping | 1277 | `08-multicast.md` |
| [`multicast igmp snooping`](chapters/08-multicast.md#multicast-igmp-snooping) | 8 | IGMP Snooping | 1280 | `08-multicast.md` |
| [`multicast igmp snooping administrative-status`](chapters/08-multicast.md#multicast-igmp-snooping-administrative-status) | 8 | IGMP Snooping | 1282 | `08-multicast.md` |
| [`multicast igmp snooping bridge-domain`](chapters/08-multicast.md#multicast-igmp-snooping-bridge-domain) | 8 | IGMP Snooping | 1285 | `08-multicast.md` |
| [`multicast igmp snooping interface`](chapters/08-multicast.md#multicast-igmp-snooping-interface) | 8 | IGMP Snooping | 1287 | `08-multicast.md` |
| [`multicast igmp snooping interface administrative-status`](chapters/08-multicast.md#multicast-igmp-snooping-interface-administrative-status) | 8 | IGMP Snooping | 1290 | `08-multicast.md` |
| [`multicast igmp snooping interface group-limit`](chapters/08-multicast.md#multicast-igmp-snooping-interface-group-limit) | 8 | IGMP Snooping | 1293 | `08-multicast.md` |
| [`multicast igmp snooping interface ignore`](chapters/08-multicast.md#multicast-igmp-snooping-interface-ignore) | 8 | IGMP Snooping | 1296 | `08-multicast.md` |
| [`multicast igmp snooping interface immediate-leave`](chapters/08-multicast.md#multicast-igmp-snooping-interface-immediate-leave) | 8 | IGMP Snooping | 1299 | `08-multicast.md` |
| [`multicast igmp snooping interface last-member-query`](chapters/08-multicast.md#multicast-igmp-snooping-interface-last-member-query) | 8 | IGMP Snooping | 1302 | `08-multicast.md` |
| [`multicast igmp snooping interface maximum response time`](chapters/08-multicast.md#multicast-igmp-snooping-interface-maximum-response-time) | 8 | IGMP Snooping | 1305 | `08-multicast.md` |
| [`multicast igmp snooping interface mrouter`](chapters/08-multicast.md#multicast-igmp-snooping-interface-mrouter) | 8 | IGMP Snooping | 1308 | `08-multicast.md` |
| [`multicast igmp snooping interface query interval`](chapters/08-multicast.md#multicast-igmp-snooping-interface-query-interval) | 8 | IGMP Snooping | 1311 | `08-multicast.md` |
| [`multicast igmp snooping interface robustness-variable`](chapters/08-multicast.md#multicast-igmp-snooping-interface-robustness-variable) | 8 | IGMP Snooping | 1314 | `08-multicast.md` |
| [`multicast igmp snooping interface version`](chapters/08-multicast.md#multicast-igmp-snooping-interface-version) | 8 | IGMP Snooping | 1317 | `08-multicast.md` |
| [`show multicast igmp snooping`](chapters/08-multicast.md#show-multicast-igmp-snooping) | 8 | IGMP Snooping | 1320 | `08-multicast.md` |
| [`show multicast igmp snooping groups`](chapters/08-multicast.md#show-multicast-igmp-snooping-groups) | 8 | IGMP Snooping | 1324 | `08-multicast.md` |
| [`show multicast igmp snooping mrouter`](chapters/08-multicast.md#show-multicast-igmp-snooping-mrouter) | 8 | IGMP Snooping | 1329 | `08-multicast.md` |
| [`show multicast igmp snooping port`](chapters/08-multicast.md#show-multicast-igmp-snooping-port) | 8 | IGMP Snooping | 1332 | `08-multicast.md` |
| [`show multicast igmp snooping statistics`](chapters/08-multicast.md#show-multicast-igmp-snooping-statistics) | 8 | IGMP Snooping | 1337 | `08-multicast.md` |
| [`qos policer hierarchical`](chapters/09-quality-of-service.md#qos-policer-hierarchical) | 9 | QoS Policer | 1340 | `09-quality-of-service.md` |
| [`qos policer instance`](chapters/09-quality-of-service.md#qos-policer-instance) | 9 | QoS Policer | 1343 | `09-quality-of-service.md` |
| [`qos policer profile`](chapters/09-quality-of-service.md#qos-policer-profile) | 9 | QoS Policer | 1348 | `09-quality-of-service.md` |
| [`show qos policer`](chapters/09-quality-of-service.md#show-qos-policer) | 9 | QoS Policer | 1353 | `09-quality-of-service.md` |
| [`show qos policer resources`](chapters/09-quality-of-service.md#show-qos-policer-resources) | 9 | QoS Policer | 1357 | `09-quality-of-service.md` |
| [`qos interface scheduler-profile`](chapters/09-quality-of-service.md#qos-interface-scheduler-profile) | 9 | QoS Packet Scheduler and Egress Shapers | 1360 | `09-quality-of-service.md` |
| [`qos scheduler-profile`](chapters/09-quality-of-service.md#qos-scheduler-profile) | 9 | QoS Packet Scheduler and Egress Shapers | 1363 | `09-quality-of-service.md` |
| [`rate-limit`](chapters/09-quality-of-service.md#rate-limit) | 9 | QoS Packet Scheduler and Egress Shapers | 1367 | `09-quality-of-service.md` |
| [`switchport interface storm-control`](chapters/09-quality-of-service.md#switchport-interface-storm-control) | 9 | Storm Control | 1370 | `09-quality-of-service.md` |
| [`access-list acl-profile`](chapters/10-access-lists.md#access-list-acl-profile) | 10 | Basic ACLs | 1374 | `10-access-lists.md` |
| [`access-list interface`](chapters/10-access-lists.md#access-list-interface) | 10 | Basic ACLs | 1377 | `10-access-lists.md` |
| [`access-list protection`](chapters/10-access-lists.md#access-list-protection) | 10 | Basic ACLs | 1380 | `10-access-lists.md` |
| [`access-list-entry`](chapters/10-access-lists.md#access-list-entry) | 10 | Basic ACLs | 1383 | `10-access-lists.md` |
| [`show acl-resources`](chapters/10-access-lists.md#show-acl-resources) | 10 | Basic ACLs | 1394 | `10-access-lists.md` |
| [`aaa authentication-next-method-on-fail`](chapters/11-security.md#aaa-authentication-next-method-on-fail) | 11 | AAA | 1400 | `11-security.md` |
| [`aaa authentication-order`](chapters/11-security.md#aaa-authentication-order) | 11 | AAA | 1402 | `11-security.md` |
| [`aaa authentication-type`](chapters/11-security.md#aaa-authentication-type) | 11 | AAA | 1405 | `11-security.md` |
| [`aaa server radius`](chapters/11-security.md#aaa-server-radius) | 11 | AAA | 1407 | `11-security.md` |
| [`aaa server tacacs`](chapters/11-security.md#aaa-server-tacacs) | 11 | AAA | 1411 | `11-security.md` |
| [`aaa user`](chapters/11-security.md#aaa-user) | 11 | AAA | 1417 | `11-security.md` |
| [`id`](chapters/11-security.md#id) | 11 | AAA | 1421 | `11-security.md` |
| [`show aaa ssh_public_key`](chapters/11-security.md#show-aaa-ssh-public-key) | 11 | AAA | 1423 | `11-security.md` |
| [`who`](chapters/11-security.md#who) | 11 | AAA | 1426 | `11-security.md` |
| [`anti-ip-spoofing`](chapters/11-security.md#anti-ip-spoofing) | 11 | Port Security | 1428 | `11-security.md` |
| [`show allowed-ip`](chapters/11-security.md#show-allowed-ip) | 11 | Port Security | 1435 | `11-security.md` |
| [`cfm delay-measurement probe`](chapters/12-oam.md#cfm-delay-measurement-probe) | 12 | Continuity Check and Fault Management | 1439 | `12-oam.md` |
| [`cfm ma`](chapters/12-oam.md#cfm-ma) | 12 | Continuity Check and Fault Management | 1444 | `12-oam.md` |
| [`cfm ma ais`](chapters/12-oam.md#cfm-ma-ais) | 12 | Continuity Check and Fault Management | 1448 | `12-oam.md` |
| [`cfm md`](chapters/12-oam.md#cfm-md) | 12 | Continuity Check and Fault Management | 1452 | `12-oam.md` |
| [`cfm mep`](chapters/12-oam.md#cfm-mep) | 12 | Continuity Check and Fault Management | 1454 | `12-oam.md` |
| [`cfm mep continuity-check`](chapters/12-oam.md#cfm-mep-continuity-check) | 12 | Continuity Check and Fault Management | 1458 | `12-oam.md` |
| [`clear oam cfm statistics`](chapters/12-oam.md#clear-oam-cfm-statistics) | 12 | Continuity Check and Fault Management | 1462 | `12-oam.md` |
| [`delay-measurement`](chapters/12-oam.md#delay-measurement) | 12 | Continuity Check and Fault Management | 1464 | `12-oam.md` |
| [`linktrace`](chapters/12-oam.md#linktrace) | 12 | Continuity Check and Fault Management | 1468 | `12-oam.md` |
| [`loopback`](chapters/12-oam.md#loopback) | 12 | Continuity Check and Fault Management | 1471 | `12-oam.md` |
| [`show oam cfm delay-measurement`](chapters/12-oam.md#show-oam-cfm-delay-measurement) | 12 | Continuity Check and Fault Management | 1475 | `12-oam.md` |
| [`show oam cfm local`](chapters/12-oam.md#show-oam-cfm-local) | 12 | Continuity Check and Fault Management | 1479 | `12-oam.md` |
| [`show oam cfm remote`](chapters/12-oam.md#show-oam-cfm-remote) | 12 | Continuity Check and Fault Management | 1484 | `12-oam.md` |
| [`traffic-loop`](chapters/12-oam.md#traffic-loop) | 12 | Activation Test | 1488 | `12-oam.md` |
| [`efm`](chapters/12-oam.md#efm) | 12 | EFM | 1491 | `12-oam.md` |
| [`show oam efm`](chapters/12-oam.md#show-oam-efm) | 12 | EFM | 1493 | `12-oam.md` |
| [`lldp`](chapters/12-oam.md#lldp) | 12 | LLDP | 1496 | `12-oam.md` |
| [`show lldp local`](chapters/12-oam.md#show-lldp-local) | 12 | LLDP | 1501 | `12-oam.md` |
| [`show lldp neighbors`](chapters/12-oam.md#show-lldp-neighbors) | 12 | LLDP | 1506 | `12-oam.md` |
| [`show oam twamp reflector connection`](chapters/12-oam.md#show-oam-twamp-reflector-connection) | 12 | TWAMP | 1511 | `12-oam.md` |
| [`show oam twamp reflector test-session`](chapters/12-oam.md#show-oam-twamp-reflector-test-session) | 12 | TWAMP | 1515 | `12-oam.md` |
| [`show oam twamp sender connection`](chapters/12-oam.md#show-oam-twamp-sender-connection) | 12 | TWAMP | 1519 | `12-oam.md` |
| [`twamp reflector`](chapters/12-oam.md#twamp-reflector) | 12 | TWAMP | 1525 | `12-oam.md` |
| [`twamp reflector administrative-status`](chapters/12-oam.md#twamp-reflector-administrative-status) | 12 | TWAMP | 1527 | `12-oam.md` |
| [`twamp reflector client-address`](chapters/12-oam.md#twamp-reflector-client-address) | 12 | TWAMP | 1529 | `12-oam.md` |
| [`twamp reflector client-network`](chapters/12-oam.md#twamp-reflector-client-network) | 12 | TWAMP | 1531 | `12-oam.md` |
| [`twamp reflector port`](chapters/12-oam.md#twamp-reflector-port) | 12 | TWAMP | 1533 | `12-oam.md` |
| [`twamp reflector vrf`](chapters/12-oam.md#twamp-reflector-vrf) | 12 | TWAMP | 1535 | `12-oam.md` |
| [`twamp sender administrative-status`](chapters/12-oam.md#twamp-sender-administrative-status) | 12 | TWAMP | 1537 | `12-oam.md` |
| [`twamp sender connection`](chapters/12-oam.md#twamp-sender-connection) | 12 | TWAMP | 1539 | `12-oam.md` |
| [`twamp sender connection`](chapters/12-oam.md#twamp-sender-connection) | 12 | TWAMP | 1541 | `12-oam.md` |
| [`twamp sender connection interval`](chapters/12-oam.md#twamp-sender-connection-interval) | 12 | TWAMP | 1544 | `12-oam.md` |
| [`twamp sender connection number-of-packets`](chapters/12-oam.md#twamp-sender-connection-number-of-packets) | 12 | TWAMP | 1546 | `12-oam.md` |
| [`twamp sender connection server-port`](chapters/12-oam.md#twamp-sender-connection-server-port) | 12 | TWAMP | 1548 | `12-oam.md` |
| [`twamp sender connection test-session`](chapters/12-oam.md#twamp-sender-connection-test-session) | 12 | TWAMP | 1550 | `12-oam.md` |
| [`twamp sender connection test-session dscp`](chapters/12-oam.md#twamp-sender-connection-test-session-dscp) | 12 | TWAMP | 1553 | `12-oam.md` |
| [`twamp sender connection test-session max-port`](chapters/12-oam.md#twamp-sender-connection-test-session-max-port) | 12 | TWAMP | 1556 | `12-oam.md` |
| [`twamp sender connection test-session min-port`](chapters/12-oam.md#twamp-sender-connection-test-session-min-port) | 12 | TWAMP | 1559 | `12-oam.md` |
| [`twamp sender connection test-session packet-size`](chapters/12-oam.md#twamp-sender-connection-test-session-packet-size) | 12 | TWAMP | 1562 | `12-oam.md` |
| [`twamp sender connection vrf`](chapters/12-oam.md#twamp-sender-connection-vrf) | 12 | TWAMP | 1565 | `12-oam.md` |
| [`sflow agent ipv4`](chapters/12-oam.md#sflow-agent-ipv4) | 12 | sFlow | 1567 | `12-oam.md` |
| [`sflow collector`](chapters/12-oam.md#sflow-collector) | 12 | sFlow | 1569 | `12-oam.md` |
| [`sflow interface`](chapters/12-oam.md#sflow-interface) | 12 | sFlow | 1572 | `12-oam.md` |
| [`remote-devices`](chapters/12-oam.md#remote-devices) | 12 | Remote Devices Management | 1577 | `12-oam.md` |
| [`show remote-devices`](chapters/12-oam.md#show-remote-devices) | 12 | Remote Devices Management | 1579 | `12-oam.md` |
| [`icmp-probe`](chapters/12-oam.md#icmp-probe) | 12 | ICMP-Probe | 1582 | `12-oam.md` |
| [`show icmp-probe`](chapters/12-oam.md#show-icmp-probe) | 12 | ICMP-Probe | 1588 | `12-oam.md` |
| [`clock`](chapters/13-synchronization.md#clock) | 13 | NTP | 1592 | `13-synchronization.md` |
| [`set system clock`](chapters/13-synchronization.md#set-system-clock) | 13 | NTP | 1595 | `13-synchronization.md` |
| [`show sntp`](chapters/13-synchronization.md#show-sntp) | 13 | NTP | 1597 | `13-synchronization.md` |
| [`show system clock`](chapters/13-synchronization.md#show-system-clock) | 13 | NTP | 1600 | `13-synchronization.md` |
| [`sntp`](chapters/13-synchronization.md#sntp) | 13 | NTP | 1602 | `13-synchronization.md` |
| [`show synchronization synce quality-level`](chapters/13-synchronization.md#show-synchronization-synce-quality-level) | 13 | SyncE | 1608 | `13-synchronization.md` |
| [`synchronization synce quality-level`](chapters/13-synchronization.md#synchronization-synce-quality-level) | 13 | SyncE | 1611 | `13-synchronization.md` |
| [`show synchronization ptp`](chapters/13-synchronization.md#show-synchronization-ptp) | 13 | IEEE 1588 | 1614 | `13-synchronization.md` |
| [`synchronization ptp`](chapters/13-synchronization.md#synchronization-ptp) | 13 | IEEE 1588 | 1620 | `13-synchronization.md` |
| [`synchronization sync-source`](chapters/13-synchronization.md#synchronization-sync-source) | 13 | IEEE 1588 | 1624 | `13-synchronization.md` |
| [`synchronization sync-source`](chapters/13-synchronization.md#synchronization-sync-source) | 13 | IEEE 1588 | 1626 | `13-synchronization.md` |
| [`synchronization transparent-clock`](chapters/13-synchronization.md#synchronization-transparent-clock) | 13 | IEEE 1588 | 1629 | `13-synchronization.md` |
| [`aes-key-exchange`](chapters/14-gpon.md#aes-key-exchange) | 14 | OLT | 1631 | `14-gpon.md` |
| [`clear interface statistics gpon`](chapters/14-gpon.md#clear-interface-statistics-gpon) | 14 | OLT | 1633 | `14-gpon.md` |
| [`interface gpon`](chapters/14-gpon.md#interface-gpon) | 14 | OLT | 1636 | `14-gpon.md` |
| [`load default-gpon-profiles`](chapters/14-gpon.md#load-default-gpon-profiles) | 14 | OLT | 1640 | `14-gpon.md` |
| [`onu-auto-provisioning`](chapters/14-gpon.md#onu-auto-provisioning) | 14 | OLT | 1644 | `14-gpon.md` |
| [`profile gpon line-profile`](chapters/14-gpon.md#profile-gpon-line-profile) | 14 | OLT | 1652 | `14-gpon.md` |
| [`rg-one-shot-prov`](chapters/14-gpon.md#rg-one-shot-prov) | 14 | OLT | 1659 | `14-gpon.md` |
| [`service vlan block`](chapters/14-gpon.md#service-vlan-block) | 14 | OLT | 1661 | `14-gpon.md` |
| [`service vlan type`](chapters/14-gpon.md#service-vlan-type) | 14 | OLT | 1663 | `14-gpon.md` |
| [`service-port`](chapters/14-gpon.md#service-port) | 14 | OLT | 1665 | `14-gpon.md` |
| [`show interface gpon`](chapters/14-gpon.md#show-interface-gpon) | 14 | OLT | 1670 | `14-gpon.md` |
| [`profile gpon bandwidth-profile`](chapters/14-gpon.md#profile-gpon-bandwidth-profile) | 14 | ONU Profiles | 1678 | `14-gpon.md` |
| [`profile gpon gem-traffic-profile`](chapters/14-gpon.md#profile-gpon-gem-traffic-profile) | 14 | ONU Profiles | 1684 | `14-gpon.md` |
| [`profile gpon media-profile`](chapters/14-gpon.md#profile-gpon-media-profile) | 14 | ONU Profiles | 1687 | `14-gpon.md` |
| [`profile gpon onu-profile`](chapters/14-gpon.md#profile-gpon-onu-profile) | 14 | ONU Profiles | 1691 | `14-gpon.md` |
| [`profile gpon rg-profile`](chapters/14-gpon.md#profile-gpon-rg-profile) | 14 | ONU Profiles | 1694 | `14-gpon.md` |
| [`profile gpon service-profile`](chapters/14-gpon.md#profile-gpon-service-profile) | 14 | ONU Profiles | 1706 | `14-gpon.md` |
| [`profile gpon sip-agent-profile`](chapters/14-gpon.md#profile-gpon-sip-agent-profile) | 14 | ONU Profiles | 1708 | `14-gpon.md` |
| [`profile gpon snmp-profile`](chapters/14-gpon.md#profile-gpon-snmp-profile) | 14 | ONU Profiles | 1711 | `14-gpon.md` |
| [`profile gpon tr069-acs-profile`](chapters/14-gpon.md#profile-gpon-tr069-acs-profile) | 14 | ONU Profiles | 1717 | `14-gpon.md` |
| [`vlan-mapping`](chapters/14-gpon.md#vlan-mapping) | 14 | ONU Profiles | 1720 | `14-gpon.md` |
| [`interface {gpon \| xgspon} onu`](chapters/14-gpon.md#interface-gpon-xgspon-onu) | 14 | ONU | 1725 | `14-gpon.md` |
| [`onu-auth-method`](chapters/14-gpon.md#onu-auth-method) | 14 | ONU | 1739 | `14-gpon.md` |
| [`onu-enable`](chapters/14-gpon.md#onu-enable) | 14 | ONU | 1741 | `14-gpon.md` |
| [`onu-force-status-update`](chapters/14-gpon.md#onu-force-status-update) | 14 | ONU | 1743 | `14-gpon.md` |
| [`onu-reset`](chapters/14-gpon.md#onu-reset) | 14 | ONU | 1745 | `14-gpon.md` |
| [`request firmware onu cancel`](chapters/14-gpon.md#request-firmware-onu-cancel) | 14 | ONU | 1747 | `14-gpon.md` |
| [`request firmware onu install`](chapters/14-gpon.md#request-firmware-onu-install) | 14 | ONU | 1749 | `14-gpon.md` |
| [`rg-reprovision`](chapters/14-gpon.md#rg-reprovision) | 14 | ONU | 1753 | `14-gpon.md` |
| [`show firmware`](chapters/14-gpon.md#show-firmware) | 14 | ONU | 1755 | `14-gpon.md` |
| [`show interface gpon onu`](chapters/14-gpon.md#show-interface-gpon-onu) | 14 | ONU | 1757 | `14-gpon.md` |
| [`show interface gpon onu Ethernet`](chapters/14-gpon.md#show-interface-gpon-onu-ethernet) | 14 | ONU | 1764 | `14-gpon.md` |
| [`show interface gpon onu gem`](chapters/14-gpon.md#show-interface-gpon-onu-gem) | 14 | ONU | 1769 | `14-gpon.md` |
| [`show onu-global-count`](chapters/14-gpon.md#show-onu-global-count) | 14 | ONU | 1774 | `14-gpon.md` |
| [`show onu-interface-count`](chapters/14-gpon.md#show-onu-interface-count) | 14 | ONU | 1776 | `14-gpon.md` |
| [`clear interface statistics xgspon`](chapters/15-xgspon.md#clear-interface-statistics-xgspon) | 15 | OLT | 1778 | `15-xgspon.md` |
| [`interface xgspon`](chapters/15-xgspon.md#interface-xgspon) | 15 | OLT | 1781 | `15-xgspon.md` |
| [`load default-xgspon-profiles`](chapters/15-xgspon.md#load-default-xgspon-profiles) | 15 | OLT | 1785 | `15-xgspon.md` |
| [`show interface xgspon`](chapters/15-xgspon.md#show-interface-xgspon) | 15 | OLT | 1789 | `15-xgspon.md` |
| [`profile gpon onu-profile`](chapters/15-xgspon.md#profile-gpon-onu-profile) | 15 | ONU Profiles | 1797 | `15-xgspon.md` |
| [`show interface xgspon onu`](chapters/15-xgspon.md#show-interface-xgspon-onu) | 15 | ONU | 1800 | `15-xgspon.md` |
| [`show interface xgspon onu Ethernet`](chapters/15-xgspon.md#show-interface-xgspon-onu-ethernet) | 15 | ONU | 1807 | `15-xgspon.md` |
| [`show interface xgspon onu gem`](chapters/15-xgspon.md#show-interface-xgspon-onu-gem) | 15 | ONU | 1812 | `15-xgspon.md` |
| [`assistant-task`](chapters/16-services.md#assistant-task) | 16 | Management | 1816 | `16-services.md` |
| [`logout`](chapters/16-services.md#logout) | 16 | Management | 1825 | `16-services.md` |
| [`management`](chapters/16-services.md#management) | 16 | Management | 1828 | `16-services.md` |
| [`show assistant-task`](chapters/16-services.md#show-assistant-task) | 16 | Management | 1830 | `16-services.md` |
| [`show ssh-server`](chapters/16-services.md#show-ssh-server) | 16 | Management | 1834 | `16-services.md` |
| [`ssh`](chapters/16-services.md#ssh) | 16 | Management | 1836 | `16-services.md` |
| [`ssh-server`](chapters/16-services.md#ssh-server) | 16 | Management | 1839 | `16-services.md` |
| [`ssh-server`](chapters/16-services.md#ssh-server) | 16 | Management | 1843 | `16-services.md` |
| [`telnet`](chapters/16-services.md#telnet) | 16 | Management | 1846 | `16-services.md` |
| [`telnet-server`](chapters/16-services.md#telnet-server) | 16 | Management | 1848 | `16-services.md` |
| [`who`](chapters/16-services.md#who) | 16 | Management | 1851 | `16-services.md` |
| [`card-model`](chapters/16-services.md#card-model) | 16 | System | 1854 | `16-services.md` |
| [`clear log`](chapters/16-services.md#clear-log) | 16 | System | 1857 | `16-services.md` |
| [`log`](chapters/16-services.md#log) | 16 | System | 1859 | `16-services.md` |
| [`reboot`](chapters/16-services.md#reboot) | 16 | System | 1863 | `16-services.md` |
| [`reboot-forced`](chapters/16-services.md#reboot-forced) | 16 | System | 1865 | `16-services.md` |
| [`show inventory`](chapters/16-services.md#show-inventory) | 16 | System | 1867 | `16-services.md` |
| [`show log`](chapters/16-services.md#show-log) | 16 | System | 1873 | `16-services.md` |
| [`show platform`](chapters/16-services.md#show-platform) | 16 | System | 1877 | `16-services.md` |
| [`show system reboot`](chapters/16-services.md#show-system-reboot) | 16 | System | 1880 | `16-services.md` |
| [`dhcp l2-relay`](chapters/16-services.md#dhcp-l2-relay) | 16 | DHCP | 1882 | `16-services.md` |
| [`dhcp relay`](chapters/16-services.md#dhcp-relay) | 16 | DHCP | 1888 | `16-services.md` |
| [`dhcp relay if-option`](chapters/16-services.md#dhcp-relay-if-option) | 16 | DHCP | 1894 | `16-services.md` |
| [`show dhcp l2-relay`](chapters/16-services.md#show-dhcp-l2-relay) | 16 | DHCP | 1897 | `16-services.md` |
| [`intermediate-agent Chassi/Slot/Port`](chapters/16-services.md#intermediate-agent-chassi-slot-port) | 16 | PPP | 1899 | `16-services.md` |
| [`pppoe`](chapters/16-services.md#pppoe) | 16 | PPP | 1903 | `16-services.md` |
| [`show pppoe intermediate-agent sessions interface gpon Chassi/Slot/Port`](chapters/16-services.md#show-pppoe-intermediate-agent-sessions-interface-gpon-chassi-slot-port) | 16 | PPP | 1905 | `16-services.md` |
| [`provision`](chapters/17-modular-chassis.md#provision) | 17 | Provisioning | 1907 | `17-modular-chassis.md` |
| [`show environment`](chapters/18-hardware.md#show-environment) | 18 | Environment | 1910 | `18-hardware.md` |
| [`show interface transceivers`](chapters/18-hardware.md#show-interface-transceivers) | 18 | Environment | 1914 | `18-hardware.md` |
| [`forwarding-resources`](chapters/18-hardware.md#forwarding-resources) | 18 | Resources | 1923 | `18-hardware.md` |
| [`show forwarding-resources`](chapters/18-hardware.md#show-forwarding-resources) | 18 | Resources | 1926 | `18-hardware.md` |
| [`clear cpu-dos-protect counters`](chapters/19-cpu-protection.md#clear-cpu-dos-protect-counters) | 19 | CPU DoS Protection | 1929 | `19-cpu-protection.md` |
| [`cpu-dos-protect global`](chapters/19-cpu-protection.md#cpu-dos-protect-global) | 19 | CPU DoS Protection | 1932 | `19-cpu-protection.md` |
| [`cpu-dos-protect protocols`](chapters/19-cpu-protection.md#cpu-dos-protect-protocols) | 19 | CPU DoS Protection | 1934 | `19-cpu-protection.md` |
| [`show cpu-dos-protect`](chapters/19-cpu-protection.md#show-cpu-dos-protect) | 19 | CPU DoS Protection | 1937 | `19-cpu-protection.md` |
