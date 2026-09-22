# Cisco IOS Command Reference — Markdown + Dados Normalizados

Conversão do PDF `cf_command_ref.pdf` (Cisco **IOS** Configuration Fundamentals, Configuration Fundamentals) para um corpus estruturado no **mesmo padrão** Datacom/Huawei, otimizado para LLM e RAG/MCP.

## Conteúdo desta pasta

| Arquivo | Descrição |
| --- | --- |
| `chapters/NN-*.md` | Guia completo em Markdown, um arquivo por capítulo. |
| `cisco-commands.jsonl` | **Dados normalizados**: um JSON por comando (campos separados). |
| `cisco-commands.index.json` | Índice compacto (comando → capítulo/seção/página/arquivo). |

## Estatísticas

- **Comandos documentados:** 613
- **Comandos de leitura (show/clear/…):** 211
- **Capítulos:** 16

## Esquema do JSONL (idêntico ao Datacom/Huawei)

| Campo | Origem (Cisco) |
| --- | --- |
| `description` | parágrafo introdutório (To …) |
| `syntax` | bloco italic/bold |
| `parameters[]` | Syntax Description |
| `default` | Command Default |
| `command_mode` | Command Modes |
| `history[]` | Command History |
| `usage_guidelines` | Usage Guidelines |
| `examples[]` | Examples |

```jsonc
{
  "id": "cisco::IOS::0001",
  "command": "activation-character",
  "vendor": "cisco", "os": "IOS", "firmware": "Configuration Fundamentals",
  "chapter_num": 2, "chapter": "A through B", "category": "basics",
  "page": 30, "is_read_command": false,
  "description": "...", "syntax": "...",
  "parameters": [{"name": "...", "description": "...", "value": "", "default": ""}],
  "default": "...", "command_mode": "Line configuration",
  "history": [{"release": "10.0", "modification": "..."}],
  "markdown": "### `activation-character`", "text": "..."
}
```

## Capítulos

- [Capítulo 0: Front Matter](chapters/00-front-matter.md) — 0 comando(s)
- [Capítulo 1: Introduction](chapters/01-introduction.md) — 0 comando(s)
- [Capítulo 2: A through B](chapters/02-a-through-b.md) — 27 comando(s)
- [Capítulo 3: C commands](chapters/03-c-commands.md) — 35 comando(s)
- [Capítulo 4: D through E](chapters/04-d-through-e.md) — 43 comando(s)
- [Capítulo 5: F through K](chapters/05-f-through-k.md) — 39 comando(s)
- [Capítulo 6: L through mode](chapters/06-l-through-mode.md) — 58 comando(s)
- [Capítulo 7: monitor event-trace through Q](chapters/07-monitor-event-trace-through-q.md) — 59 comando(s)
- [Capítulo 8: R through setup](chapters/08-r-through-setup.md) — 67 comando(s)
- [Capítulo 9: show through show fm summary](chapters/09-show-through-show-fm-summary.md) — 68 comando(s)
- [Capítulo 10: show gsr through show monitor event trace](chapters/10-show-gsr-through-show-monitor-event-trace.md) — 44 comando(s)
- [Capítulo 11: show monitor permit list through show process memory](chapters/11-show-monitor-permit-list-through-show-process-memory.md) — 34 comando(s)
- [Capítulo 12: show protocols through showmon](chapters/12-show-protocols-through-showmon.md) — 41 comando(s)
- [Capítulo 13: slave auto-sync config through terminal-type](chapters/13-slave-auto-sync-config-through-terminal-type.md) — 64 comando(s)
- [Capítulo 14: test cable-diagnostics through xmodem](chapters/14-test-cable-diagnostics-through-xmodem.md) — 34 comando(s)
- [Capítulo 15: ASCII Character Set and Hexadecimal Values](chapters/15-ascii-character-set-and-hexadecimal-values.md) — 0 comando(s)

## Índice de comandos

| Comando | Cap. | Seção | Pág. | Arquivo |
| --- | --- | --- | --- | --- |
| [`activation-character`](chapters/02-a-through-b.md#activation-character) | 2 |  | 30 | `02-a-through-b.md` |
| [`alias`](chapters/02-a-through-b.md#alias) | 2 |  | 30 | `02-a-through-b.md` |
| [`archive`](chapters/02-a-through-b.md#archive) | 2 |  | 34 | `02-a-through-b.md` |
| [`archive config`](chapters/02-a-through-b.md#archive-config) | 2 |  | 35 | `02-a-through-b.md` |
| [`archive log config persistent save`](chapters/02-a-through-b.md#archive-log-config-persistent-save) | 2 |  | 37 | `02-a-through-b.md` |
| [`archive tar`](chapters/02-a-through-b.md#archive-tar) | 2 |  | 38 | `02-a-through-b.md` |
| [`async-bootp`](chapters/02-a-through-b.md#async-bootp) | 2 |  | 40 | `02-a-through-b.md` |
| [`attach`](chapters/02-a-through-b.md#attach) | 2 |  | 42 | `02-a-through-b.md` |
| [`autobaud`](chapters/02-a-through-b.md#autobaud) | 2 |  | 45 | `02-a-through-b.md` |
| [`auto-sync`](chapters/02-a-through-b.md#auto-sync) | 2 |  | 46 | `02-a-through-b.md` |
| [`autoupgrade disk-cleanup`](chapters/02-a-through-b.md#autoupgrade-disk-cleanup) | 2 |  | 48 | `02-a-through-b.md` |
| [`autoupgrade ida url`](chapters/02-a-through-b.md#autoupgrade-ida-url) | 2 |  | 49 | `02-a-through-b.md` |
| [`autoupgrade status email`](chapters/02-a-through-b.md#autoupgrade-status-email) | 2 |  | 50 | `02-a-through-b.md` |
| [`banner exec`](chapters/02-a-through-b.md#banner-exec) | 2 |  | 51 | `02-a-through-b.md` |
| [`banner incoming`](chapters/02-a-through-b.md#banner-incoming) | 2 |  | 53 | `02-a-through-b.md` |
| [`banner login`](chapters/02-a-through-b.md#banner-login) | 2 |  | 55 | `02-a-through-b.md` |
| [`banner motd`](chapters/02-a-through-b.md#banner-motd) | 2 |  | 56 | `02-a-through-b.md` |
| [`banner slip-ppp`](chapters/02-a-through-b.md#banner-slip-ppp) | 2 |  | 58 | `02-a-through-b.md` |
| [`boot`](chapters/02-a-through-b.md#boot) | 2 |  | 60 | `02-a-through-b.md` |
| [`boot bootldr`](chapters/02-a-through-b.md#boot-bootldr) | 2 |  | 64 | `02-a-through-b.md` |
| [`boot bootstrap`](chapters/02-a-through-b.md#boot-bootstrap) | 2 |  | 65 | `02-a-through-b.md` |
| [`boot config`](chapters/02-a-through-b.md#boot-config) | 2 |  | 67 | `02-a-through-b.md` |
| [`boot host`](chapters/02-a-through-b.md#boot-host) | 2 |  | 69 | `02-a-through-b.md` |
| [`boot network`](chapters/02-a-through-b.md#boot-network) | 2 |  | 71 | `02-a-through-b.md` |
| [`boot system`](chapters/02-a-through-b.md#boot-system) | 2 |  | 74 | `02-a-through-b.md` |
| [`boot-end-marker`](chapters/02-a-through-b.md#boot-end-marker) | 2 |  | 79 | `02-a-through-b.md` |
| [`boot-start-marker`](chapters/02-a-through-b.md#boot-start-marker) | 2 |  | 81 | `02-a-through-b.md` |
| [`cd`](chapters/03-c-commands.md#cd) | 3 |  | 86 | `03-c-commands.md` |
| [`clear archive log config`](chapters/03-c-commands.md#clear-archive-log-config) | 3 |  | 87 | `03-c-commands.md` |
| [`clear catalyst6000 traffic-meter`](chapters/03-c-commands.md#clear-catalyst6000-traffic-meter) | 3 |  | 88 | `03-c-commands.md` |
| [`clear configuration lock`](chapters/03-c-commands.md#clear-configuration-lock) | 3 |  | 89 | `03-c-commands.md` |
| [`clear diagnostic event-log`](chapters/03-c-commands.md#clear-diagnostic-event-log) | 3 |  | 90 | `03-c-commands.md` |
| [`clear ip http client cache`](chapters/03-c-commands.md#clear-ip-http-client-cache) | 3 |  | 91 | `03-c-commands.md` |
| [`clear logging`](chapters/03-c-commands.md#clear-logging) | 3 |  | 92 | `03-c-commands.md` |
| [`clear logging system`](chapters/03-c-commands.md#clear-logging-system) | 3 |  | 93 | `03-c-commands.md` |
| [`clear logging xml`](chapters/03-c-commands.md#clear-logging-xml) | 3 |  | 94 | `03-c-commands.md` |
| [`clear memory low-water-mark`](chapters/03-c-commands.md#clear-memory-low-water-mark) | 3 |  | 95 | `03-c-commands.md` |
| [`clear mls statistics`](chapters/03-c-commands.md#clear-mls-statistics) | 3 |  | 95 | `03-c-commands.md` |
| [`clear parser cache`](chapters/03-c-commands.md#clear-parser-cache) | 3 |  | 96 | `03-c-commands.md` |
| [`clear parser statistics`](chapters/03-c-commands.md#clear-parser-statistics) | 3 |  | 97 | `03-c-commands.md` |
| [`clear platform netint`](chapters/03-c-commands.md#clear-platform-netint) | 3 |  | 99 | `03-c-commands.md` |
| [`clear processes interrupt mask`](chapters/03-c-commands.md#clear-processes-interrupt-mask) | 3 |  | 99 | `03-c-commands.md` |
| [`clear scp accounting`](chapters/03-c-commands.md#clear-scp-accounting) | 3 |  | 100 | `03-c-commands.md` |
| [`clear tcp`](chapters/03-c-commands.md#clear-tcp) | 3 |  | 101 | `03-c-commands.md` |
| [`clear vlan counters`](chapters/03-c-commands.md#clear-vlan-counters) | 3 |  | 102 | `03-c-commands.md` |
| [`clock`](chapters/03-c-commands.md#clock) | 3 |  | 103 | `03-c-commands.md` |
| [`clock initialize nvram`](chapters/03-c-commands.md#clock-initialize-nvram) | 3 |  | 104 | `03-c-commands.md` |
| [`config-register`](chapters/03-c-commands.md#config-register) | 3 |  | 105 | `03-c-commands.md` |
| [`configure check syntax`](chapters/03-c-commands.md#configure-check-syntax) | 3 |  | 106 | `03-c-commands.md` |
| [`configuration mode exclusive`](chapters/03-c-commands.md#configuration-mode-exclusive) | 3 |  | 107 | `03-c-commands.md` |
| [`configure confirm`](chapters/03-c-commands.md#configure-confirm) | 3 |  | 113 | `03-c-commands.md` |
| [`configure memory`](chapters/03-c-commands.md#configure-memory) | 3 |  | 114 | `03-c-commands.md` |
| [`configure replace`](chapters/03-c-commands.md#configure-replace) | 3 |  | 115 | `03-c-commands.md` |
| [`configure revert`](chapters/03-c-commands.md#configure-revert) | 3 |  | 119 | `03-c-commands.md` |
| [`configure terminal`](chapters/03-c-commands.md#configure-terminal) | 3 |  | 121 | `03-c-commands.md` |
| [`confreg`](chapters/03-c-commands.md#confreg) | 3 |  | 122 | `03-c-commands.md` |
| [`continue (ROM monitor)`](chapters/03-c-commands.md#continue-rom-monitor) | 3 |  | 124 | `03-c-commands.md` |
| [`copy`](chapters/03-c-commands.md#copy) | 3 |  | 125 | `03-c-commands.md` |
| [`copy logging system`](chapters/03-c-commands.md#copy-logging-system) | 3 |  | 144 | `03-c-commands.md` |
| [`copy xmodem`](chapters/03-c-commands.md#copy-xmodem) | 3 |  | 146 | `03-c-commands.md` |
| [`copy ymodem`](chapters/03-c-commands.md#copy-ymodem) | 3 |  | 147 | `03-c-commands.md` |
| [`copy noverify`](chapters/03-c-commands.md#copy-noverify) | 3 |  | 148 | `03-c-commands.md` |
| [`databits`](chapters/04-d-through-e.md#databits) | 4 |  | 154 | `04-d-through-e.md` |
| [`data-character-bits`](chapters/04-d-through-e.md#data-character-bits) | 4 |  | 155 | `04-d-through-e.md` |
| [`default-value data-character-bits`](chapters/04-d-through-e.md#default-value-data-character-bits) | 4 |  | 156 | `04-d-through-e.md` |
| [`default-value exec-character-bits`](chapters/04-d-through-e.md#default-value-exec-character-bits) | 4 |  | 156 | `04-d-through-e.md` |
| [`default-value modem-interval`](chapters/04-d-through-e.md#default-value-modem-interval) | 4 |  | 157 | `04-d-through-e.md` |
| [`default-value special-character-bits`](chapters/04-d-through-e.md#default-value-special-character-bits) | 4 |  | 158 | `04-d-through-e.md` |
| [`define interface-range`](chapters/04-d-through-e.md#define-interface-range) | 4 |  | 159 | `04-d-through-e.md` |
| [`delete`](chapters/04-d-through-e.md#delete) | 4 |  | 160 | `04-d-through-e.md` |
| [`diag`](chapters/04-d-through-e.md#diag) | 4 |  | 163 | `04-d-through-e.md` |
| [`diagnostic bootup level`](chapters/04-d-through-e.md#diagnostic-bootup-level) | 4 |  | 165 | `04-d-through-e.md` |
| [`diagnostic cns`](chapters/04-d-through-e.md#diagnostic-cns) | 4 |  | 166 | `04-d-through-e.md` |
| [`diagnostic event-log size`](chapters/04-d-through-e.md#diagnostic-event-log-size) | 4 |  | 168 | `04-d-through-e.md` |
| [`diagnostic level`](chapters/04-d-through-e.md#diagnostic-level) | 4 |  | 169 | `04-d-through-e.md` |
| [`diagnostic monitor`](chapters/04-d-through-e.md#diagnostic-monitor) | 4 |  | 170 | `04-d-through-e.md` |
| [`diagnostic ondemand`](chapters/04-d-through-e.md#diagnostic-ondemand) | 4 |  | 174 | `04-d-through-e.md` |
| [`diagnostic schedule module`](chapters/04-d-through-e.md#diagnostic-schedule-module) | 4 |  | 175 | `04-d-through-e.md` |
| [`diagnostic start`](chapters/04-d-through-e.md#diagnostic-start) | 4 |  | 177 | `04-d-through-e.md` |
| [`diagnostic stop`](chapters/04-d-through-e.md#diagnostic-stop) | 4 |  | 181 | `04-d-through-e.md` |
| [`dir`](chapters/04-d-through-e.md#dir) | 4 |  | 183 | `04-d-through-e.md` |
| [`disable`](chapters/04-d-through-e.md#disable) | 4 |  | 186 | `04-d-through-e.md` |
| [`disconnect-character`](chapters/04-d-through-e.md#disconnect-character) | 4 |  | 186 | `04-d-through-e.md` |
| [`dispatch-character`](chapters/04-d-through-e.md#dispatch-character) | 4 |  | 187 | `04-d-through-e.md` |
| [`dispatch-machine`](chapters/04-d-through-e.md#dispatch-machine) | 4 |  | 188 | `04-d-through-e.md` |
| [`dispatch-timeout`](chapters/04-d-through-e.md#dispatch-timeout) | 4 |  | 189 | `04-d-through-e.md` |
| [`do`](chapters/04-d-through-e.md#do) | 4 |  | 190 | `04-d-through-e.md` |
| [`downward-compatible-config`](chapters/04-d-through-e.md#downward-compatible-config) | 4 |  | 192 | `04-d-through-e.md` |
| [`editing`](chapters/04-d-through-e.md#editing) | 4 |  | 193 | `04-d-through-e.md` |
| [`enable`](chapters/04-d-through-e.md#enable) | 4 |  | 196 | `04-d-through-e.md` |
| [`enable last-resort`](chapters/04-d-through-e.md#enable-last-resort) | 4 |  | 199 | `04-d-through-e.md` |
| [`end`](chapters/04-d-through-e.md#end) | 4 |  | 199 | `04-d-through-e.md` |
| [`environment-monitor shutdown temperature`](chapters/04-d-through-e.md#environment-monitor-shutdown-temperature) | 4 |  | 200 | `04-d-through-e.md` |
| [`environment temperature-controlled`](chapters/04-d-through-e.md#environment-temperature-controlled) | 4 |  | 201 | `04-d-through-e.md` |
| [`erase`](chapters/04-d-through-e.md#erase) | 4 |  | 202 | `04-d-through-e.md` |
| [`errdisable detect cause`](chapters/04-d-through-e.md#errdisable-detect-cause) | 4 |  | 205 | `04-d-through-e.md` |
| [`errdisable recovery`](chapters/04-d-through-e.md#errdisable-recovery) | 4 |  | 206 | `04-d-through-e.md` |
| [`escape-character`](chapters/04-d-through-e.md#escape-character) | 4 |  | 208 | `04-d-through-e.md` |
| [`exec`](chapters/04-d-through-e.md#exec) | 4 |  | 210 | `04-d-through-e.md` |
| [`exec-banner`](chapters/04-d-through-e.md#exec-banner) | 4 |  | 211 | `04-d-through-e.md` |
| [`exec-character-bits`](chapters/04-d-through-e.md#exec-character-bits) | 4 |  | 213 | `04-d-through-e.md` |
| [`exec-timeout`](chapters/04-d-through-e.md#exec-timeout) | 4 |  | 214 | `04-d-through-e.md` |
| [`execute-on`](chapters/04-d-through-e.md#execute-on) | 4 |  | 215 | `04-d-through-e.md` |
| [`exit (EXEC)`](chapters/04-d-through-e.md#exit-exec) | 4 |  | 219 | `04-d-through-e.md` |
| [`exit (global)`](chapters/04-d-through-e.md#exit-global) | 4 |  | 219 | `04-d-through-e.md` |
| [`factory-reset all`](chapters/05-f-through-k.md#factory-reset-all) | 5 |  | 222 | `05-f-through-k.md` |
| [`factory-reset keep-licensing-info`](chapters/05-f-through-k.md#factory-reset-keep-licensing-info) | 5 |  | 222 | `05-f-through-k.md` |
| [`factory-reset all secure 3-pass`](chapters/05-f-through-k.md#factory-reset-all-secure-3-pass) | 5 |  | 223 | `05-f-through-k.md` |
| [`file privilege`](chapters/05-f-through-k.md#file-privilege) | 5 |  | 224 | `05-f-through-k.md` |
| [`file prompt`](chapters/05-f-through-k.md#file-prompt) | 5 |  | 224 | `05-f-through-k.md` |
| [`file verify auto`](chapters/05-f-through-k.md#file-verify-auto) | 5 |  | 225 | `05-f-through-k.md` |
| [`format`](chapters/05-f-through-k.md#format) | 5 |  | 226 | `05-f-through-k.md` |
| [`fsck`](chapters/05-f-through-k.md#fsck) | 5 |  | 230 | `05-f-through-k.md` |
| [`full-help`](chapters/05-f-through-k.md#full-help) | 5 |  | 235 | `05-f-through-k.md` |
| [`help`](chapters/05-f-through-k.md#help) | 5 |  | 237 | `05-f-through-k.md` |
| [`hidekeys`](chapters/05-f-through-k.md#hidekeys) | 5 |  | 238 | `05-f-through-k.md` |
| [`history`](chapters/05-f-through-k.md#history) | 5 |  | 240 | `05-f-through-k.md` |
| [`history size`](chapters/05-f-through-k.md#history-size) | 5 |  | 241 | `05-f-through-k.md` |
| [`hold-character`](chapters/05-f-through-k.md#hold-character) | 5 |  | 242 | `05-f-through-k.md` |
| [`hostname`](chapters/05-f-through-k.md#hostname) | 5 |  | 242 | `05-f-through-k.md` |
| [`hw-module reset`](chapters/05-f-through-k.md#hw-module-reset) | 5 |  | 244 | `05-f-through-k.md` |
| [`hw-module shutdown`](chapters/05-f-through-k.md#hw-module-shutdown) | 5 |  | 245 | `05-f-through-k.md` |
| [`insecure`](chapters/05-f-through-k.md#insecure) | 5 |  | 245 | `05-f-through-k.md` |
| [`install`](chapters/05-f-through-k.md#install) | 5 |  | 246 | `05-f-through-k.md` |
| [`international`](chapters/05-f-through-k.md#international) | 5 |  | 249 | `05-f-through-k.md` |
| [`ip bootp server`](chapters/05-f-through-k.md#ip-bootp-server) | 5 |  | 250 | `05-f-through-k.md` |
| [`ip finger`](chapters/05-f-through-k.md#ip-finger) | 5 |  | 251 | `05-f-through-k.md` |
| [`ip ftp passive`](chapters/05-f-through-k.md#ip-ftp-passive) | 5 |  | 252 | `05-f-through-k.md` |
| [`ip ftp password`](chapters/05-f-through-k.md#ip-ftp-password) | 5 |  | 253 | `05-f-through-k.md` |
| [`ip ftp source-interface`](chapters/05-f-through-k.md#ip-ftp-source-interface) | 5 |  | 254 | `05-f-through-k.md` |
| [`ip ftp username`](chapters/05-f-through-k.md#ip-ftp-username) | 5 |  | 255 | `05-f-through-k.md` |
| [`ip rarp-server`](chapters/05-f-through-k.md#ip-rarp-server) | 5 |  | 256 | `05-f-through-k.md` |
| [`ip rcmd domain-lookup`](chapters/05-f-through-k.md#ip-rcmd-domain-lookup) | 5 |  | 258 | `05-f-through-k.md` |
| [`ip rcmd rcp-enable`](chapters/05-f-through-k.md#ip-rcmd-rcp-enable) | 5 |  | 259 | `05-f-through-k.md` |
| [`ip rcmd remote-host`](chapters/05-f-through-k.md#ip-rcmd-remote-host) | 5 |  | 260 | `05-f-through-k.md` |
| [`ip rcmd remote-username`](chapters/05-f-through-k.md#ip-rcmd-remote-username) | 5 |  | 262 | `05-f-through-k.md` |
| [`ip rcmd rsh-enable`](chapters/05-f-through-k.md#ip-rcmd-rsh-enable) | 5 |  | 263 | `05-f-through-k.md` |
| [`ip rcmd source-interface`](chapters/05-f-through-k.md#ip-rcmd-source-interface) | 5 |  | 264 | `05-f-through-k.md` |
| [`ip telnet source-interface`](chapters/05-f-through-k.md#ip-telnet-source-interface) | 5 |  | 266 | `05-f-through-k.md` |
| [`ip tftp blocksize`](chapters/05-f-through-k.md#ip-tftp-blocksize) | 5 |  | 266 | `05-f-through-k.md` |
| [`ip tftp boot-interface`](chapters/05-f-through-k.md#ip-tftp-boot-interface) | 5 |  | 267 | `05-f-through-k.md` |
| [`ip tftp min-timeout`](chapters/05-f-through-k.md#ip-tftp-min-timeout) | 5 |  | 268 | `05-f-through-k.md` |
| [`ip tftp source-interface`](chapters/05-f-through-k.md#ip-tftp-source-interface) | 5 |  | 268 | `05-f-through-k.md` |
| [`ip wccp web-cache accelerated`](chapters/05-f-through-k.md#ip-wccp-web-cache-accelerated) | 5 |  | 270 | `05-f-through-k.md` |
| [`length`](chapters/06-l-through-mode.md#length) | 6 |  | 274 | `06-l-through-mode.md` |
| [`load-interval`](chapters/06-l-through-mode.md#load-interval) | 6 |  | 274 | `06-l-through-mode.md` |
| [`location`](chapters/06-l-through-mode.md#location) | 6 |  | 276 | `06-l-through-mode.md` |
| [`lock`](chapters/06-l-through-mode.md#lock) | 6 |  | 277 | `06-l-through-mode.md` |
| [`lockable`](chapters/06-l-through-mode.md#lockable) | 6 |  | 278 | `06-l-through-mode.md` |
| [`log config`](chapters/06-l-through-mode.md#log-config) | 6 |  | 279 | `06-l-through-mode.md` |
| [`logging buffered`](chapters/06-l-through-mode.md#logging-buffered) | 6 |  | 280 | `06-l-through-mode.md` |
| [`logging buginf`](chapters/06-l-through-mode.md#logging-buginf) | 6 |  | 283 | `06-l-through-mode.md` |
| [`logging enable`](chapters/06-l-through-mode.md#logging-enable) | 6 |  | 284 | `06-l-through-mode.md` |
| [`logging esm config`](chapters/06-l-through-mode.md#logging-esm-config) | 6 |  | 285 | `06-l-through-mode.md` |
| [`logging event bundle-status`](chapters/06-l-through-mode.md#logging-event-bundle-status) | 6 |  | 286 | `06-l-through-mode.md` |
| [`logging event link-status (global configuration)`](chapters/06-l-through-mode.md#logging-event-link-status-global-configuration) | 6 |  | 287 | `06-l-through-mode.md` |
| [`logging event link-status (interface configuration)`](chapters/06-l-through-mode.md#logging-event-link-status-interface-configuration) | 6 |  | 288 | `06-l-through-mode.md` |
| [`logging event subif-link-status`](chapters/06-l-through-mode.md#logging-event-subif-link-status) | 6 |  | 289 | `06-l-through-mode.md` |
| [`logging event trunk-status`](chapters/06-l-through-mode.md#logging-event-trunk-status) | 6 |  | 290 | `06-l-through-mode.md` |
| [`logging reload`](chapters/06-l-through-mode.md#logging-reload) | 6 |  | 291 | `06-l-through-mode.md` |
| [`logging ip access-list cache (global configuration)`](chapters/06-l-through-mode.md#logging-ip-access-list-cache-global-configuration) | 6 |  | 292 | `06-l-through-mode.md` |
| [`logging ip access-list cache (interface configuration)`](chapters/06-l-through-mode.md#logging-ip-access-list-cache-interface-configuration) | 6 |  | 294 | `06-l-through-mode.md` |
| [`logging persistent (config-archive-log-cfg)`](chapters/06-l-through-mode.md#logging-persistent-config-archive-log-cfg) | 6 |  | 295 | `06-l-through-mode.md` |
| [`logging persistent reload (config-archive-log-cfg)`](chapters/06-l-through-mode.md#logging-persistent-reload-config-archive-log-cfg) | 6 |  | 296 | `06-l-through-mode.md` |
| [`logging purge-log buffer days`](chapters/06-l-through-mode.md#logging-purge-log-buffer-days) | 6 |  | 297 | `06-l-through-mode.md` |
| [`logging size`](chapters/06-l-through-mode.md#logging-size) | 6 |  | 298 | `06-l-through-mode.md` |
| [`logging synchronous`](chapters/06-l-through-mode.md#logging-synchronous) | 6 |  | 299 | `06-l-through-mode.md` |
| [`logging system`](chapters/06-l-through-mode.md#logging-system) | 6 |  | 302 | `06-l-through-mode.md` |
| [`logout`](chapters/06-l-through-mode.md#logout) | 6 |  | 303 | `06-l-through-mode.md` |
| [`logout-warning`](chapters/06-l-through-mode.md#logout-warning) | 6 |  | 303 | `06-l-through-mode.md` |
| [`macro (global configuration)`](chapters/06-l-through-mode.md#macro-global-configuration) | 6 |  | 304 | `06-l-through-mode.md` |
| [`macro (interface configuration)`](chapters/06-l-through-mode.md#macro-interface-configuration) | 6 |  | 306 | `06-l-through-mode.md` |
| [`maximum`](chapters/06-l-through-mode.md#maximum) | 6 |  | 307 | `06-l-through-mode.md` |
| [`memory cache error-recovery`](chapters/06-l-through-mode.md#memory-cache-error-recovery) | 6 |  | 309 | `06-l-through-mode.md` |
| [`memory cache error-recovery options`](chapters/06-l-through-mode.md#memory-cache-error-recovery-options) | 6 |  | 310 | `06-l-through-mode.md` |
| [`memory free low-watermark`](chapters/06-l-through-mode.md#memory-free-low-watermark) | 6 |  | 310 | `06-l-through-mode.md` |
| [`memory lite`](chapters/06-l-through-mode.md#memory-lite) | 6 |  | 312 | `06-l-through-mode.md` |
| [`memory reserve`](chapters/06-l-through-mode.md#memory-reserve) | 6 |  | 312 | `06-l-through-mode.md` |
| [`memory reserve critical`](chapters/06-l-through-mode.md#memory-reserve-critical) | 6 |  | 314 | `06-l-through-mode.md` |
| [`memory sanity`](chapters/06-l-through-mode.md#memory-sanity) | 6 |  | 315 | `06-l-through-mode.md` |
| [`memory scan`](chapters/06-l-through-mode.md#memory-scan) | 6 |  | 316 | `06-l-through-mode.md` |
| [`memory-size iomem`](chapters/06-l-through-mode.md#memory-size-iomem) | 6 |  | 316 | `06-l-through-mode.md` |
| [`menu (EXEC)`](chapters/06-l-through-mode.md#menu-exec) | 6 |  | 317 | `06-l-through-mode.md` |
| [`menu menu-name single-space`](chapters/06-l-through-mode.md#menu-menu-name-single-space) | 6 |  | 319 | `06-l-through-mode.md` |
| [`menu clear-screen`](chapters/06-l-through-mode.md#menu-clear-screen) | 6 |  | 320 | `06-l-through-mode.md` |
| [`menu command`](chapters/06-l-through-mode.md#menu-command) | 6 |  | 321 | `06-l-through-mode.md` |
| [`menu default`](chapters/06-l-through-mode.md#menu-default) | 6 |  | 323 | `06-l-through-mode.md` |
| [`menu line-mode`](chapters/06-l-through-mode.md#menu-line-mode) | 6 |  | 324 | `06-l-through-mode.md` |
| [`menu options`](chapters/06-l-through-mode.md#menu-options) | 6 |  | 325 | `06-l-through-mode.md` |
| [`menu prompt`](chapters/06-l-through-mode.md#menu-prompt) | 6 |  | 326 | `06-l-through-mode.md` |
| [`menu status-line`](chapters/06-l-through-mode.md#menu-status-line) | 6 |  | 327 | `06-l-through-mode.md` |
| [`menu text`](chapters/06-l-through-mode.md#menu-text) | 6 |  | 328 | `06-l-through-mode.md` |
| [`menu title`](chapters/06-l-through-mode.md#menu-title) | 6 |  | 329 | `06-l-through-mode.md` |
| [`microcode (12000)`](chapters/06-l-through-mode.md#microcode-12000) | 6 |  | 331 | `06-l-through-mode.md` |
| [`microcode (7000/7500)`](chapters/06-l-through-mode.md#microcode-7000-7500) | 6 |  | 332 | `06-l-through-mode.md` |
| [`microcode (7200)`](chapters/06-l-through-mode.md#microcode-7200) | 6 |  | 333 | `06-l-through-mode.md` |
| [`microcode reload (12000)`](chapters/06-l-through-mode.md#microcode-reload-12000) | 6 |  | 334 | `06-l-through-mode.md` |
| [`microcode reload (7000 7500)`](chapters/06-l-through-mode.md#microcode-reload-7000-7500) | 6 |  | 335 | `06-l-through-mode.md` |
| [`microcode reload (7200)`](chapters/06-l-through-mode.md#microcode-reload-7200) | 6 |  | 336 | `06-l-through-mode.md` |
| [`mkdir`](chapters/06-l-through-mode.md#mkdir) | 6 |  | 337 | `06-l-through-mode.md` |
| [`mkdir disk0:`](chapters/06-l-through-mode.md#mkdir-disk0) | 6 |  | 338 | `06-l-through-mode.md` |
| [`mode`](chapters/06-l-through-mode.md#mode) | 6 |  | 339 | `06-l-through-mode.md` |
| [`monitor event-trace (EXEC)`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-exec) | 7 |  | 344 | `07-monitor-event-trace-through-q.md` |
| [`monitor event-trace (global)`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-global) | 7 |  | 347 | `07-monitor-event-trace-through-q.md` |
| [`monitor event-trace crypto pki`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-crypto-pki) | 7 |  | 350 | `07-monitor-event-trace-through-q.md` |
| [`monitor event-trace crypto ipsec`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-crypto-ipsec) | 7 |  | 351 | `07-monitor-event-trace-through-q.md` |
| [`monitor event-trace crypto ikev2`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-crypto-ikev2) | 7 |  | 352 | `07-monitor-event-trace-through-q.md` |
| [`monitor event-trace crypto ikev2 event`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-crypto-ikev2-event) | 7 |  | 352 | `07-monitor-event-trace-through-q.md` |
| [`monitor event-trace crypto ikev2 event dump-file`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-crypto-ikev2-event-dump-file) | 7 |  | 353 | `07-monitor-event-trace-through-q.md` |
| [`monitor event-trace crypto ikev2 event size`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-crypto-ikev2-event-size) | 7 |  | 354 | `07-monitor-event-trace-through-q.md` |
| [`monitor event-trace crypto ikev2 event stacktrace`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-crypto-ikev2-event-stacktrace) | 7 |  | 355 | `07-monitor-event-trace-through-q.md` |
| [`monitor event-trace crypto pki`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-crypto-pki) | 7 |  | 356 | `07-monitor-event-trace-through-q.md` |
| [`monitor event-trace dump-traces`](chapters/07-monitor-event-trace-through-q.md#monitor-event-trace-dump-traces) | 7 |  | 357 | `07-monitor-event-trace-through-q.md` |
| [`monitor pcm-tracer capture-destination`](chapters/07-monitor-event-trace-through-q.md#monitor-pcm-tracer-capture-destination) | 7 |  | 358 | `07-monitor-event-trace-through-q.md` |
| [`monitor pcm-tracer delayed-start`](chapters/07-monitor-event-trace-through-q.md#monitor-pcm-tracer-delayed-start) | 7 |  | 360 | `07-monitor-event-trace-through-q.md` |
| [`monitor pcm-tracer profile`](chapters/07-monitor-event-trace-through-q.md#monitor-pcm-tracer-profile) | 7 |  | 361 | `07-monitor-event-trace-through-q.md` |
| [`monitor permit-list`](chapters/07-monitor-event-trace-through-q.md#monitor-permit-list) | 7 |  | 362 | `07-monitor-event-trace-through-q.md` |
| [`monitor session egress replication-mode`](chapters/07-monitor-event-trace-through-q.md#monitor-session-egress-replication-mode) | 7 |  | 363 | `07-monitor-event-trace-through-q.md` |
| [`monitor session type`](chapters/07-monitor-event-trace-through-q.md#monitor-session-type) | 7 |  | 365 | `07-monitor-event-trace-through-q.md` |
| [`mop device-code`](chapters/07-monitor-event-trace-through-q.md#mop-device-code) | 7 |  | 373 | `07-monitor-event-trace-through-q.md` |
| [`mop retransmit-timer`](chapters/07-monitor-event-trace-through-q.md#mop-retransmit-timer) | 7 |  | 374 | `07-monitor-event-trace-through-q.md` |
| [`mop retries`](chapters/07-monitor-event-trace-through-q.md#mop-retries) | 7 |  | 375 | `07-monitor-event-trace-through-q.md` |
| [`more`](chapters/07-monitor-event-trace-through-q.md#more) | 7 |  | 376 | `07-monitor-event-trace-through-q.md` |
| [`more url begin`](chapters/07-monitor-event-trace-through-q.md#more-url-begin) | 7 |  | 378 | `07-monitor-event-trace-through-q.md` |
| [`more url exclude`](chapters/07-monitor-event-trace-through-q.md#more-url-exclude) | 7 |  | 380 | `07-monitor-event-trace-through-q.md` |
| [`more url include`](chapters/07-monitor-event-trace-through-q.md#more-url-include) | 7 |  | 382 | `07-monitor-event-trace-through-q.md` |
| [`more flh:logfile`](chapters/07-monitor-event-trace-through-q.md#more-flh-logfile) | 7 |  | 383 | `07-monitor-event-trace-through-q.md` |
| [`motd-banner`](chapters/07-monitor-event-trace-through-q.md#motd-banner) | 7 |  | 385 | `07-monitor-event-trace-through-q.md` |
| [`name-connection`](chapters/07-monitor-event-trace-through-q.md#name-connection) | 7 |  | 386 | `07-monitor-event-trace-through-q.md` |
| [`nmsp enable`](chapters/07-monitor-event-trace-through-q.md#nmsp-enable) | 7 |  | 387 | `07-monitor-event-trace-through-q.md` |
| [`nmsp strong-cipher`](chapters/07-monitor-event-trace-through-q.md#nmsp-strong-cipher) | 7 |  | 388 | `07-monitor-event-trace-through-q.md` |
| [`no menu`](chapters/07-monitor-event-trace-through-q.md#no-menu) | 7 |  | 388 | `07-monitor-event-trace-through-q.md` |
| [`notify`](chapters/07-monitor-event-trace-through-q.md#notify) | 7 |  | 389 | `07-monitor-event-trace-through-q.md` |
| [`notify syslog`](chapters/07-monitor-event-trace-through-q.md#notify-syslog) | 7 |  | 390 | `07-monitor-event-trace-through-q.md` |
| [`padding`](chapters/07-monitor-event-trace-through-q.md#padding) | 7 |  | 391 | `07-monitor-event-trace-through-q.md` |
| [`parity`](chapters/07-monitor-event-trace-through-q.md#parity) | 7 |  | 392 | `07-monitor-event-trace-through-q.md` |
| [`parser cache`](chapters/07-monitor-event-trace-through-q.md#parser-cache) | 7 |  | 393 | `07-monitor-event-trace-through-q.md` |
| [`parser command serializer`](chapters/07-monitor-event-trace-through-q.md#parser-command-serializer) | 7 |  | 394 | `07-monitor-event-trace-through-q.md` |
| [`parser config cache interface`](chapters/07-monitor-event-trace-through-q.md#parser-config-cache-interface) | 7 |  | 395 | `07-monitor-event-trace-through-q.md` |
| [`parser config partition`](chapters/07-monitor-event-trace-through-q.md#parser-config-partition) | 7 |  | 396 | `07-monitor-event-trace-through-q.md` |
| [`parser maximum`](chapters/07-monitor-event-trace-through-q.md#parser-maximum) | 7 |  | 398 | `07-monitor-event-trace-through-q.md` |
| [`partition`](chapters/07-monitor-event-trace-through-q.md#partition) | 7 |  | 398 | `07-monitor-event-trace-through-q.md` |
| [`path (archive configuration)`](chapters/07-monitor-event-trace-through-q.md#path-archive-configuration) | 7 |  | 400 | `07-monitor-event-trace-through-q.md` |
| [`periodic`](chapters/07-monitor-event-trace-through-q.md#periodic) | 7 |  | 403 | `07-monitor-event-trace-through-q.md` |
| [`ping`](chapters/07-monitor-event-trace-through-q.md#ping) | 7 |  | 406 | `07-monitor-event-trace-through-q.md` |
| [`ping (privileged)`](chapters/07-monitor-event-trace-through-q.md#ping-privileged) | 7 |  | 410 | `07-monitor-event-trace-through-q.md` |
| [`ping ip`](chapters/07-monitor-event-trace-through-q.md#ping-ip) | 7 |  | 414 | `07-monitor-event-trace-through-q.md` |
| [`ping srb`](chapters/07-monitor-event-trace-through-q.md#ping-srb) | 7 |  | 417 | `07-monitor-event-trace-through-q.md` |
| [`ping vrf`](chapters/07-monitor-event-trace-through-q.md#ping-vrf) | 7 |  | 418 | `07-monitor-event-trace-through-q.md` |
| [`platform qfp drops threshold`](chapters/07-monitor-event-trace-through-q.md#platform-qfp-drops-threshold) | 7 |  | 421 | `07-monitor-event-trace-through-q.md` |
| [`platform shell`](chapters/07-monitor-event-trace-through-q.md#platform-shell) | 7 |  | 422 | `07-monitor-event-trace-through-q.md` |
| [`power enable`](chapters/07-monitor-event-trace-through-q.md#power-enable) | 7 |  | 423 | `07-monitor-event-trace-through-q.md` |
| [`power redundancy-mode`](chapters/07-monitor-event-trace-through-q.md#power-redundancy-mode) | 7 |  | 424 | `07-monitor-event-trace-through-q.md` |
| [`printer`](chapters/07-monitor-event-trace-through-q.md#printer) | 7 |  | 425 | `07-monitor-event-trace-through-q.md` |
| [`private`](chapters/07-monitor-event-trace-through-q.md#private) | 7 |  | 426 | `07-monitor-event-trace-through-q.md` |
| [`process cpu statistics limit entry-percentage`](chapters/07-monitor-event-trace-through-q.md#process-cpu-statistics-limit-entry-percentage) | 7 |  | 427 | `07-monitor-event-trace-through-q.md` |
| [`process cpu threshold type`](chapters/07-monitor-event-trace-through-q.md#process-cpu-threshold-type) | 7 |  | 428 | `07-monitor-event-trace-through-q.md` |
| [`process-max-time`](chapters/07-monitor-event-trace-through-q.md#process-max-time) | 7 |  | 429 | `07-monitor-event-trace-through-q.md` |
| [`prompt`](chapters/07-monitor-event-trace-through-q.md#prompt) | 7 |  | 430 | `07-monitor-event-trace-through-q.md` |
| [`prompt config`](chapters/07-monitor-event-trace-through-q.md#prompt-config) | 7 |  | 431 | `07-monitor-event-trace-through-q.md` |
| [`pwd`](chapters/07-monitor-event-trace-through-q.md#pwd) | 7 |  | 432 | `07-monitor-event-trace-through-q.md` |
| [`refuse-message`](chapters/08-r-through-setup.md#refuse-message) | 8 |  | 434 | `08-r-through-setup.md` |
| [`regexp optimize`](chapters/08-r-through-setup.md#regexp-optimize) | 8 |  | 435 | `08-r-through-setup.md` |
| [`reload`](chapters/08-r-through-setup.md#reload) | 8 |  | 435 | `08-r-through-setup.md` |
| [`remote command`](chapters/08-r-through-setup.md#remote-command) | 8 |  | 439 | `08-r-through-setup.md` |
| [`remote login`](chapters/08-r-through-setup.md#remote-login) | 8 |  | 440 | `08-r-through-setup.md` |
| [`remote-span`](chapters/08-r-through-setup.md#remote-span) | 8 |  | 442 | `08-r-through-setup.md` |
| [`rename`](chapters/08-r-through-setup.md#rename) | 8 |  | 442 | `08-r-through-setup.md` |
| [`request consent-token accept-response shell-access`](chapters/08-r-through-setup.md#request-consent-token-accept-response-shell-access) | 8 |  | 443 | `08-r-through-setup.md` |
| [`request consent-token generate-challenge shell-access`](chapters/08-r-through-setup.md#request-consent-token-generate-challenge-shell-access) | 8 |  | 444 | `08-r-through-setup.md` |
| [`request consent-token terminate-auth`](chapters/08-r-through-setup.md#request-consent-token-terminate-auth) | 8 |  | 445 | `08-r-through-setup.md` |
| [`request platform software package describe file`](chapters/08-r-through-setup.md#request-platform-software-package-describe-file) | 8 |  | 445 | `08-r-through-setup.md` |
| [`request platform software package expand file`](chapters/08-r-through-setup.md#request-platform-software-package-expand-file) | 8 |  | 451 | `08-r-through-setup.md` |
| [`request platform software package install commit`](chapters/08-r-through-setup.md#request-platform-software-package-install-commit) | 8 |  | 454 | `08-r-through-setup.md` |
| [`request platform software package install file`](chapters/08-r-through-setup.md#request-platform-software-package-install-file) | 8 |  | 455 | `08-r-through-setup.md` |
| [`request platform software package install rollback`](chapters/08-r-through-setup.md#request-platform-software-package-install-rollback) | 8 |  | 462 | `08-r-through-setup.md` |
| [`request platform software package install snapshot`](chapters/08-r-through-setup.md#request-platform-software-package-install-snapshot) | 8 |  | 463 | `08-r-through-setup.md` |
| [`request platform software process release`](chapters/08-r-through-setup.md#request-platform-software-process-release) | 8 |  | 465 | `08-r-through-setup.md` |
| [`request platform software system shell`](chapters/08-r-through-setup.md#request-platform-software-system-shell) | 8 |  | 466 | `08-r-through-setup.md` |
| [`request platform software shell session output format`](chapters/08-r-through-setup.md#request-platform-software-shell-session-output-format) | 8 |  | 467 | `08-r-through-setup.md` |
| [`request platform software snapshot`](chapters/08-r-through-setup.md#request-platform-software-snapshot) | 8 |  | 469 | `08-r-through-setup.md` |
| [`request platform software vty attach`](chapters/08-r-through-setup.md#request-platform-software-vty-attach) | 8 |  | 471 | `08-r-through-setup.md` |
| [`revision`](chapters/08-r-through-setup.md#revision) | 8 |  | 472 | `08-r-through-setup.md` |
| [`rmdir`](chapters/08-r-through-setup.md#rmdir) | 8 |  | 473 | `08-r-through-setup.md` |
| [`rommon-pref`](chapters/08-r-through-setup.md#rommon-pref) | 8 |  | 474 | `08-r-through-setup.md` |
| [`route-converge-interval`](chapters/08-r-through-setup.md#route-converge-interval) | 8 |  | 475 | `08-r-through-setup.md` |
| [`rsh`](chapters/08-r-through-setup.md#rsh) | 8 |  | 476 | `08-r-through-setup.md` |
| [`scheduler allocate`](chapters/08-r-through-setup.md#scheduler-allocate) | 8 |  | 477 | `08-r-through-setup.md` |
| [`scheduler heapcheck enable`](chapters/08-r-through-setup.md#scheduler-heapcheck-enable) | 8 |  | 478 | `08-r-through-setup.md` |
| [`scheduler heapcheck poll`](chapters/08-r-through-setup.md#scheduler-heapcheck-poll) | 8 |  | 479 | `08-r-through-setup.md` |
| [`scheduler heapcheck process`](chapters/08-r-through-setup.md#scheduler-heapcheck-process) | 8 |  | 480 | `08-r-through-setup.md` |
| [`scheduler interrupt mask profile`](chapters/08-r-through-setup.md#scheduler-interrupt-mask-profile) | 8 |  | 481 | `08-r-through-setup.md` |
| [`scheduler interrupt mask size`](chapters/08-r-through-setup.md#scheduler-interrupt-mask-size) | 8 |  | 482 | `08-r-through-setup.md` |
| [`scheduler interrupt mask time`](chapters/08-r-through-setup.md#scheduler-interrupt-mask-time) | 8 |  | 483 | `08-r-through-setup.md` |
| [`scheduler interval`](chapters/08-r-through-setup.md#scheduler-interval) | 8 |  | 484 | `08-r-through-setup.md` |
| [`scheduler isr-watchdog`](chapters/08-r-through-setup.md#scheduler-isr-watchdog) | 8 |  | 485 | `08-r-through-setup.md` |
| [`scheduler max-sched-time`](chapters/08-r-through-setup.md#scheduler-max-sched-time) | 8 |  | 485 | `08-r-through-setup.md` |
| [`scheduler process-watchdog`](chapters/08-r-through-setup.md#scheduler-process-watchdog) | 8 |  | 486 | `08-r-through-setup.md` |
| [`scheduler timercheck process`](chapters/08-r-through-setup.md#scheduler-timercheck-process) | 8 |  | 487 | `08-r-through-setup.md` |
| [`scheduler timercheck system context`](chapters/08-r-through-setup.md#scheduler-timercheck-system-context) | 8 |  | 488 | `08-r-through-setup.md` |
| [`send`](chapters/08-r-through-setup.md#send) | 8 |  | 488 | `08-r-through-setup.md` |
| [`service compress-config`](chapters/08-r-through-setup.md#service-compress-config) | 8 |  | 490 | `08-r-through-setup.md` |
| [`service config`](chapters/08-r-through-setup.md#service-config) | 8 |  | 491 | `08-r-through-setup.md` |
| [`service counters max age`](chapters/08-r-through-setup.md#service-counters-max-age) | 8 |  | 493 | `08-r-through-setup.md` |
| [`service decimal-tty`](chapters/08-r-through-setup.md#service-decimal-tty) | 8 |  | 494 | `08-r-through-setup.md` |
| [`service exec-wait`](chapters/08-r-through-setup.md#service-exec-wait) | 8 |  | 494 | `08-r-through-setup.md` |
| [`service hide-telnet-address`](chapters/08-r-through-setup.md#service-hide-telnet-address) | 8 |  | 495 | `08-r-through-setup.md` |
| [`service linenumber`](chapters/08-r-through-setup.md#service-linenumber) | 8 |  | 496 | `08-r-through-setup.md` |
| [`service nagle`](chapters/08-r-through-setup.md#service-nagle) | 8 |  | 497 | `08-r-through-setup.md` |
| [`service prompt config`](chapters/08-r-through-setup.md#service-prompt-config) | 8 |  | 498 | `08-r-through-setup.md` |
| [`service sequence-numbers`](chapters/08-r-through-setup.md#service-sequence-numbers) | 8 |  | 499 | `08-r-through-setup.md` |
| [`service slave-log`](chapters/08-r-through-setup.md#service-slave-log) | 8 |  | 499 | `08-r-through-setup.md` |
| [`service tcp-keepalives-in`](chapters/08-r-through-setup.md#service-tcp-keepalives-in) | 8 |  | 500 | `08-r-through-setup.md` |
| [`service tcp-keepalives-out`](chapters/08-r-through-setup.md#service-tcp-keepalives-out) | 8 |  | 501 | `08-r-through-setup.md` |
| [`service tcp-small-servers`](chapters/08-r-through-setup.md#service-tcp-small-servers) | 8 |  | 501 | `08-r-through-setup.md` |
| [`service telnet-zeroidle`](chapters/08-r-through-setup.md#service-telnet-zeroidle) | 8 |  | 503 | `08-r-through-setup.md` |
| [`service timestamps`](chapters/08-r-through-setup.md#service-timestamps) | 8 |  | 503 | `08-r-through-setup.md` |
| [`service udp-small-servers`](chapters/08-r-through-setup.md#service-udp-small-servers) | 8 |  | 508 | `08-r-through-setup.md` |
| [`service-module apa traffic-management`](chapters/08-r-through-setup.md#service-module-apa-traffic-management) | 8 |  | 509 | `08-r-through-setup.md` |
| [`service-module wlan-ap bootimage`](chapters/08-r-through-setup.md#service-module-wlan-ap-bootimage) | 8 |  | 510 | `08-r-through-setup.md` |
| [`service-module wlan-ap reload`](chapters/08-r-through-setup.md#service-module-wlan-ap-reload) | 8 |  | 511 | `08-r-through-setup.md` |
| [`service-module wlan-ap reset`](chapters/08-r-through-setup.md#service-module-wlan-ap-reset) | 8 |  | 513 | `08-r-through-setup.md` |
| [`service-module wlan-ap session`](chapters/08-r-through-setup.md#service-module-wlan-ap-session) | 8 |  | 514 | `08-r-through-setup.md` |
| [`service-module wlan-ap statistics`](chapters/08-r-through-setup.md#service-module-wlan-ap-statistics) | 8 |  | 515 | `08-r-through-setup.md` |
| [`service-module wlan-ap status`](chapters/08-r-through-setup.md#service-module-wlan-ap-status) | 8 |  | 516 | `08-r-through-setup.md` |
| [`session slot`](chapters/08-r-through-setup.md#session-slot) | 8 |  | 517 | `08-r-through-setup.md` |
| [`set memory debug incremental starting-time`](chapters/08-r-through-setup.md#set-memory-debug-incremental-starting-time) | 8 |  | 518 | `08-r-through-setup.md` |
| [`setup`](chapters/08-r-through-setup.md#setup) | 8 |  | 519 | `08-r-through-setup.md` |
| [`show`](chapters/09-show-through-show-fm-summary.md#show) | 9 |  | 528 | `09-show-through-show-fm-summary.md` |
| [`show command append`](chapters/09-show-through-show-fm-summary.md#show-command-append) | 9 |  | 529 | `09-show-through-show-fm-summary.md` |
| [`show command begin`](chapters/09-show-through-show-fm-summary.md#show-command-begin) | 9 |  | 530 | `09-show-through-show-fm-summary.md` |
| [`show command exclude`](chapters/09-show-through-show-fm-summary.md#show-command-exclude) | 9 |  | 532 | `09-show-through-show-fm-summary.md` |
| [`show command include`](chapters/09-show-through-show-fm-summary.md#show-command-include) | 9 |  | 534 | `09-show-through-show-fm-summary.md` |
| [`show command redirect`](chapters/09-show-through-show-fm-summary.md#show-command-redirect) | 9 |  | 536 | `09-show-through-show-fm-summary.md` |
| [`show command section`](chapters/09-show-through-show-fm-summary.md#show-command-section) | 9 |  | 537 | `09-show-through-show-fm-summary.md` |
| [`show command tee`](chapters/09-show-through-show-fm-summary.md#show-command-tee) | 9 |  | 538 | `09-show-through-show-fm-summary.md` |
| [`show (Flash file system)`](chapters/09-show-through-show-fm-summary.md#show-flash-file-system) | 9 |  | 539 | `09-show-through-show-fm-summary.md` |
| [`show aliases`](chapters/09-show-through-show-fm-summary.md#show-aliases) | 9 |  | 548 | `09-show-through-show-fm-summary.md` |
| [`show alignment`](chapters/09-show-through-show-fm-summary.md#show-alignment) | 9 |  | 548 | `09-show-through-show-fm-summary.md` |
| [`show archive`](chapters/09-show-through-show-fm-summary.md#show-archive) | 9 |  | 551 | `09-show-through-show-fm-summary.md` |
| [`show archive config differences`](chapters/09-show-through-show-fm-summary.md#show-archive-config-differences) | 9 |  | 553 | `09-show-through-show-fm-summary.md` |
| [`show archive config incremental-diffs`](chapters/09-show-through-show-fm-summary.md#show-archive-config-incremental-diffs) | 9 |  | 555 | `09-show-through-show-fm-summary.md` |
| [`show archive config rollback timer`](chapters/09-show-through-show-fm-summary.md#show-archive-config-rollback-timer) | 9 |  | 557 | `09-show-through-show-fm-summary.md` |
| [`show archive log config`](chapters/09-show-through-show-fm-summary.md#show-archive-log-config) | 9 |  | 558 | `09-show-through-show-fm-summary.md` |
| [`show as5400`](chapters/09-show-through-show-fm-summary.md#show-as5400) | 9 |  | 562 | `09-show-through-show-fm-summary.md` |
| [`show async bootp`](chapters/09-show-through-show-fm-summary.md#show-async-bootp) | 9 |  | 564 | `09-show-through-show-fm-summary.md` |
| [`show autoupgrade configuration unknown`](chapters/09-show-through-show-fm-summary.md#show-autoupgrade-configuration-unknown) | 9 |  | 565 | `09-show-through-show-fm-summary.md` |
| [`show bcm560x`](chapters/09-show-through-show-fm-summary.md#show-bcm560x) | 9 |  | 566 | `09-show-through-show-fm-summary.md` |
| [`show bootflash:`](chapters/09-show-through-show-fm-summary.md#show-bootflash) | 9 |  | 567 | `09-show-through-show-fm-summary.md` |
| [`show bootvar`](chapters/09-show-through-show-fm-summary.md#show-bootvar) | 9 |  | 569 | `09-show-through-show-fm-summary.md` |
| [`show buffers`](chapters/09-show-through-show-fm-summary.md#show-buffers) | 9 |  | 572 | `09-show-through-show-fm-summary.md` |
| [`show c2600`](chapters/09-show-through-show-fm-summary.md#show-c2600) | 9 |  | 581 | `09-show-through-show-fm-summary.md` |
| [`show c7200`](chapters/09-show-through-show-fm-summary.md#show-c7200) | 9 |  | 583 | `09-show-through-show-fm-summary.md` |
| [`show catalyst6000`](chapters/09-show-through-show-fm-summary.md#show-catalyst6000) | 9 |  | 584 | `09-show-through-show-fm-summary.md` |
| [`show cls`](chapters/09-show-through-show-fm-summary.md#show-cls) | 9 |  | 586 | `09-show-through-show-fm-summary.md` |
| [`show config id`](chapters/09-show-through-show-fm-summary.md#show-config-id) | 9 |  | 588 | `09-show-through-show-fm-summary.md` |
| [`show configuration id`](chapters/09-show-through-show-fm-summary.md#show-configuration-id) | 9 |  | 589 | `09-show-through-show-fm-summary.md` |
| [`show configuration lock`](chapters/09-show-through-show-fm-summary.md#show-configuration-lock) | 9 |  | 590 | `09-show-through-show-fm-summary.md` |
| [`show context`](chapters/09-show-through-show-fm-summary.md#show-context) | 9 |  | 594 | `09-show-through-show-fm-summary.md` |
| [`show controllers (GRP image)`](chapters/09-show-through-show-fm-summary.md#show-controllers-grp-image) | 9 |  | 597 | `09-show-through-show-fm-summary.md` |
| [`show controllers (line card image)`](chapters/09-show-through-show-fm-summary.md#show-controllers-line-card-image) | 9 |  | 598 | `09-show-through-show-fm-summary.md` |
| [`show controllers logging`](chapters/09-show-through-show-fm-summary.md#show-controllers-logging) | 9 |  | 606 | `09-show-through-show-fm-summary.md` |
| [`show controllers tech-support`](chapters/09-show-through-show-fm-summary.md#show-controllers-tech-support) | 9 |  | 608 | `09-show-through-show-fm-summary.md` |
| [`show coverage history`](chapters/09-show-through-show-fm-summary.md#show-coverage-history) | 9 |  | 609 | `09-show-through-show-fm-summary.md` |
| [`show data-corruption`](chapters/09-show-through-show-fm-summary.md#show-data-corruption) | 9 |  | 610 | `09-show-through-show-fm-summary.md` |
| [`show debugging`](chapters/09-show-through-show-fm-summary.md#show-debugging) | 9 |  | 611 | `09-show-through-show-fm-summary.md` |
| [`show declassify`](chapters/09-show-through-show-fm-summary.md#show-declassify) | 9 |  | 613 | `09-show-through-show-fm-summary.md` |
| [`show derived-config`](chapters/09-show-through-show-fm-summary.md#show-derived-config) | 9 |  | 614 | `09-show-through-show-fm-summary.md` |
| [`show diagnostic cns`](chapters/09-show-through-show-fm-summary.md#show-diagnostic-cns) | 9 |  | 617 | `09-show-through-show-fm-summary.md` |
| [`show diagnostic sanity`](chapters/09-show-through-show-fm-summary.md#show-diagnostic-sanity) | 9 |  | 618 | `09-show-through-show-fm-summary.md` |
| [`show disk`](chapters/09-show-through-show-fm-summary.md#show-disk) | 9 |  | 622 | `09-show-through-show-fm-summary.md` |
| [`show disk0:`](chapters/09-show-through-show-fm-summary.md#show-disk0) | 9 |  | 624 | `09-show-through-show-fm-summary.md` |
| [`show disk1:`](chapters/09-show-through-show-fm-summary.md#show-disk1) | 9 |  | 626 | `09-show-through-show-fm-summary.md` |
| [`show drops`](chapters/09-show-through-show-fm-summary.md#show-drops) | 9 |  | 628 | `09-show-through-show-fm-summary.md` |
| [`show environment`](chapters/09-show-through-show-fm-summary.md#show-environment) | 9 |  | 629 | `09-show-through-show-fm-summary.md` |
| [`show environment alarm`](chapters/09-show-through-show-fm-summary.md#show-environment-alarm) | 9 |  | 656 | `09-show-through-show-fm-summary.md` |
| [`show environment connector`](chapters/09-show-through-show-fm-summary.md#show-environment-connector) | 9 |  | 659 | `09-show-through-show-fm-summary.md` |
| [`show environment cooling`](chapters/09-show-through-show-fm-summary.md#show-environment-cooling) | 9 |  | 660 | `09-show-through-show-fm-summary.md` |
| [`show environment status`](chapters/09-show-through-show-fm-summary.md#show-environment-status) | 9 |  | 661 | `09-show-through-show-fm-summary.md` |
| [`show environment temperature`](chapters/09-show-through-show-fm-summary.md#show-environment-temperature) | 9 |  | 663 | `09-show-through-show-fm-summary.md` |
| [`show errdisable detect`](chapters/09-show-through-show-fm-summary.md#show-errdisable-detect) | 9 |  | 666 | `09-show-through-show-fm-summary.md` |
| [`show errdisable recovery`](chapters/09-show-through-show-fm-summary.md#show-errdisable-recovery) | 9 |  | 667 | `09-show-through-show-fm-summary.md` |
| [`show fastblk`](chapters/09-show-through-show-fm-summary.md#show-fastblk) | 9 |  | 668 | `09-show-through-show-fm-summary.md` |
| [`show file descriptors`](chapters/09-show-through-show-fm-summary.md#show-file-descriptors) | 9 |  | 669 | `09-show-through-show-fm-summary.md` |
| [`show file information`](chapters/09-show-through-show-fm-summary.md#show-file-information) | 9 |  | 670 | `09-show-through-show-fm-summary.md` |
| [`show file systems`](chapters/09-show-through-show-fm-summary.md#show-file-systems) | 9 |  | 671 | `09-show-through-show-fm-summary.md` |
| [`show fm inspect`](chapters/09-show-through-show-fm-summary.md#show-fm-inspect) | 9 |  | 673 | `09-show-through-show-fm-summary.md` |
| [`show fm interface`](chapters/09-show-through-show-fm-summary.md#show-fm-interface) | 9 |  | 675 | `09-show-through-show-fm-summary.md` |
| [`show fm reflexive`](chapters/09-show-through-show-fm-summary.md#show-fm-reflexive) | 9 |  | 677 | `09-show-through-show-fm-summary.md` |
| [`show fm summary`](chapters/09-show-through-show-fm-summary.md#show-fm-summary) | 9 |  | 678 | `09-show-through-show-fm-summary.md` |
| [`show funi`](chapters/09-show-through-show-fm-summary.md#show-funi) | 9 |  | 679 | `09-show-through-show-fm-summary.md` |
| [`show identity policy`](chapters/09-show-through-show-fm-summary.md#show-identity-policy) | 9 |  | 682 | `09-show-through-show-fm-summary.md` |
| [`show identity profile`](chapters/09-show-through-show-fm-summary.md#show-identity-profile) | 9 |  | 683 | `09-show-through-show-fm-summary.md` |
| [`show install`](chapters/09-show-through-show-fm-summary.md#show-install) | 9 |  | 683 | `09-show-through-show-fm-summary.md` |
| [`show platform software snapshot status`](chapters/09-show-through-show-fm-summary.md#show-platform-software-snapshot-status) | 9 |  | 685 | `09-show-through-show-fm-summary.md` |
| [`show power usage`](chapters/09-show-through-show-fm-summary.md#show-power-usage) | 9 |  | 686 | `09-show-through-show-fm-summary.md` |
| [`show gsr`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-gsr) | 10 |  | 690 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show gt64010 (7200)`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-gt64010-7200) | 10 |  | 691 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show hardware`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-hardware) | 10 |  | 692 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show health-monitor`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-health-monitor) | 10 |  | 693 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show history`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-history) | 10 |  | 694 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show history all`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-history-all) | 10 |  | 695 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show hosts`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-hosts) | 10 |  | 697 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show html`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-html) | 10 |  | 700 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show idb`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-idb) | 10 |  | 701 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show idprom`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-idprom) | 10 |  | 702 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show inventory`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-inventory) | 10 |  | 708 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show location`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-location) | 10 |  | 711 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show logging`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-logging) | 10 |  | 713 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show logging count`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-logging-count) | 10 |  | 719 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show logging history`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-logging-history) | 10 |  | 721 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show ip ports all`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-ip-ports-all) | 10 |  | 723 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show logging system`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-logging-system) | 10 |  | 725 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show logging xml`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-logging-xml) | 10 |  | 727 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory) | 10 |  | 729 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory allocating-process`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-allocating-process) | 10 |  | 735 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory dead`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-dead) | 10 |  | 737 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory debug incremental`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-debug-incremental) | 10 |  | 739 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory debug leaks`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-debug-leaks) | 10 |  | 741 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory debug references`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-debug-references) | 10 |  | 748 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory debug unused`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-debug-unused) | 10 |  | 749 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory detailed`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-detailed) | 10 |  | 750 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory ecc`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-ecc) | 10 |  | 756 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory events`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-events) | 10 |  | 758 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory failures alloc`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-failures-alloc) | 10 |  | 759 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory fast`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-fast) | 10 |  | 760 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory fragment`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-fragment) | 10 |  | 762 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory lite-chunks`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-lite-chunks) | 10 |  | 765 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory multibus`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-multibus) | 10 |  | 767 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory pci`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-pci) | 10 |  | 768 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory processor`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-processor) | 10 |  | 769 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory scan`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-scan) | 10 |  | 773 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory statistics history`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-statistics-history) | 10 |  | 775 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory traceback`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-traceback) | 10 |  | 777 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show memory transient`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-memory-transient) | 10 |  | 778 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show microcode`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-microcode) | 10 |  | 779 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show mls statistics`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-mls-statistics) | 10 |  | 780 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show module`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-module) | 10 |  | 782 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show monitor event-trace`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-monitor-event-trace) | 10 |  | 785 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show monitor event-trace flexvpn`](chapters/10-show-gsr-through-show-monitor-event-trace.md#show-monitor-event-trace-flexvpn) | 10 |  | 791 | `10-show-gsr-through-show-monitor-event-trace.md` |
| [`show monitor permit-list`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-monitor-permit-list) | 11 |  | 796 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show monitor session`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-monitor-session) | 11 |  | 796 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show msfc`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-msfc) | 11 |  | 801 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show pagp`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-pagp) | 11 |  | 804 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show parser dump`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-parser-dump) | 11 |  | 806 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show parser macro`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-parser-macro) | 11 |  | 818 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show parser statistics`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-parser-statistics) | 11 |  | 819 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show pci`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-pci) | 11 |  | 821 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show pci hardware`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-pci-hardware) | 11 |  | 822 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show perf-meas`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-perf-meas) | 11 |  | 823 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform) | 11 |  | 825 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform bridge`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-bridge) | 11 |  | 837 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform cfm`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-cfm) | 11 |  | 838 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform diag`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-diag) | 11 |  | 839 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform hardware capacity`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-hardware-capacity) | 11 |  | 841 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform isg`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-isg) | 11 |  | 848 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform oam`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-oam) | 11 |  | 849 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform redundancy`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-redundancy) | 11 |  | 850 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform software filesystem`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-software-filesystem) | 11 |  | 851 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform software memory`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-software-memory) | 11 |  | 854 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform software mount`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-software-mount) | 11 |  | 859 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform software process list`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-software-process-list) | 11 |  | 863 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform process slot`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-process-slot) | 11 |  | 872 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform software snapshot status`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-software-snapshot-status) | 11 |  | 874 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform software tech-support`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-software-tech-support) | 11 |  | 875 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform subscriber-group`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-subscriber-group) | 11 |  | 877 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show platform supervisor`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-platform-supervisor) | 11 |  | 878 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show power`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-power) | 11 |  | 879 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show processes`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-processes) | 11 |  | 884 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show processes cpu`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-processes-cpu) | 11 |  | 891 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show processes detailed`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-processes-detailed) | 11 |  | 903 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show processes interrupt mask buffer`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-processes-interrupt-mask-buffer) | 11 |  | 907 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show processes interrupt mask detail`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-processes-interrupt-mask-detail) | 11 |  | 908 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show processes memory`](chapters/11-show-monitor-permit-list-through-show-process-memory.md#show-processes-memory) | 11 |  | 909 | `11-show-monitor-permit-list-through-show-process-memory.md` |
| [`show protocols`](chapters/12-show-protocols-through-showmon.md#show-protocols) | 12 |  | 924 | `12-show-protocols-through-showmon.md` |
| [`show region`](chapters/12-show-protocols-through-showmon.md#show-region) | 12 |  | 928 | `12-show-protocols-through-showmon.md` |
| [`show registry`](chapters/12-show-protocols-through-showmon.md#show-registry) | 12 |  | 930 | `12-show-protocols-through-showmon.md` |
| [`show reload`](chapters/12-show-protocols-through-showmon.md#show-reload) | 12 |  | 933 | `12-show-protocols-through-showmon.md` |
| [`show reload history`](chapters/12-show-protocols-through-showmon.md#show-reload-history) | 12 |  | 933 | `12-show-protocols-through-showmon.md` |
| [`show resource-pool queue`](chapters/12-show-protocols-through-showmon.md#show-resource-pool-queue) | 12 |  | 936 | `12-show-protocols-through-showmon.md` |
| [`show rhosts`](chapters/12-show-protocols-through-showmon.md#show-rhosts) | 12 |  | 937 | `12-show-protocols-through-showmon.md` |
| [`show rom-monitor`](chapters/12-show-protocols-through-showmon.md#show-rom-monitor) | 12 |  | 938 | `12-show-protocols-through-showmon.md` |
| [`show rom-monitor slot`](chapters/12-show-protocols-through-showmon.md#show-rom-monitor-slot) | 12 |  | 941 | `12-show-protocols-through-showmon.md` |
| [`show running identity policy`](chapters/12-show-protocols-through-showmon.md#show-running-identity-policy) | 12 |  | 942 | `12-show-protocols-through-showmon.md` |
| [`show running identity profile`](chapters/12-show-protocols-through-showmon.md#show-running-identity-profile) | 12 |  | 942 | `12-show-protocols-through-showmon.md` |
| [`show running-config`](chapters/12-show-protocols-through-showmon.md#show-running-config) | 12 |  | 943 | `12-show-protocols-through-showmon.md` |
| [`show running-config control-plane`](chapters/12-show-protocols-through-showmon.md#show-running-config-control-plane) | 12 |  | 951 | `12-show-protocols-through-showmon.md` |
| [`show running-config map-class`](chapters/12-show-protocols-through-showmon.md#show-running-config-map-class) | 12 |  | 952 | `12-show-protocols-through-showmon.md` |
| [`show running-config partition`](chapters/12-show-protocols-through-showmon.md#show-running-config-partition) | 12 |  | 954 | `12-show-protocols-through-showmon.md` |
| [`show scp`](chapters/12-show-protocols-through-showmon.md#show-scp) | 12 |  | 957 | `12-show-protocols-through-showmon.md` |
| [`show slot`](chapters/12-show-protocols-through-showmon.md#show-slot) | 12 |  | 959 | `12-show-protocols-through-showmon.md` |
| [`show slot0:`](chapters/12-show-protocols-through-showmon.md#show-slot0) | 12 |  | 962 | `12-show-protocols-through-showmon.md` |
| [`show slot1:`](chapters/12-show-protocols-through-showmon.md#show-slot1) | 12 |  | 965 | `12-show-protocols-through-showmon.md` |
| [`show software authenticity file`](chapters/12-show-protocols-through-showmon.md#show-software-authenticity-file) | 12 |  | 967 | `12-show-protocols-through-showmon.md` |
| [`show software authenticity keys`](chapters/12-show-protocols-through-showmon.md#show-software-authenticity-keys) | 12 |  | 969 | `12-show-protocols-through-showmon.md` |
| [`show software authenticity running`](chapters/12-show-protocols-through-showmon.md#show-software-authenticity-running) | 12 |  | 970 | `12-show-protocols-through-showmon.md` |
| [`show software package`](chapters/12-show-protocols-through-showmon.md#show-software-package) | 12 |  | 972 | `12-show-protocols-through-showmon.md` |
| [`show software installer rollback-timer`](chapters/12-show-protocols-through-showmon.md#show-software-installer-rollback-timer) | 12 |  | 976 | `12-show-protocols-through-showmon.md` |
| [`show stacks`](chapters/12-show-protocols-through-showmon.md#show-stacks) | 12 |  | 977 | `12-show-protocols-through-showmon.md` |
| [`show subsys`](chapters/12-show-protocols-through-showmon.md#show-subsys) | 12 |  | 979 | `12-show-protocols-through-showmon.md` |
| [`show sup-bootflash`](chapters/12-show-protocols-through-showmon.md#show-sup-bootflash) | 12 |  | 980 | `12-show-protocols-through-showmon.md` |
| [`show system jumbomtu`](chapters/12-show-protocols-through-showmon.md#show-system-jumbomtu) | 12 |  | 983 | `12-show-protocols-through-showmon.md` |
| [`show tech-support`](chapters/12-show-protocols-through-showmon.md#show-tech-support) | 12 |  | 983 | `12-show-protocols-through-showmon.md` |
| [`show template`](chapters/12-show-protocols-through-showmon.md#show-template) | 12 |  | 994 | `12-show-protocols-through-showmon.md` |
| [`show usb controllers`](chapters/12-show-protocols-through-showmon.md#show-usb-controllers) | 12 |  | 994 | `12-show-protocols-through-showmon.md` |
| [`show usb device`](chapters/12-show-protocols-through-showmon.md#show-usb-device) | 12 |  | 996 | `12-show-protocols-through-showmon.md` |
| [`show usb driver`](chapters/12-show-protocols-through-showmon.md#show-usb-driver) | 12 |  | 999 | `12-show-protocols-through-showmon.md` |
| [`show usb port`](chapters/12-show-protocols-through-showmon.md#show-usb-port) | 12 |  | 1000 | `12-show-protocols-through-showmon.md` |
| [`show usb tree`](chapters/12-show-protocols-through-showmon.md#show-usb-tree) | 12 |  | 1001 | `12-show-protocols-through-showmon.md` |
| [`show usbtoken`](chapters/12-show-protocols-through-showmon.md#show-usbtoken) | 12 |  | 1001 | `12-show-protocols-through-showmon.md` |
| [`show version`](chapters/12-show-protocols-through-showmon.md#show-version) | 12 |  | 1002 | `12-show-protocols-through-showmon.md` |
| [`show warm-reboot`](chapters/12-show-protocols-through-showmon.md#show-warm-reboot) | 12 |  | 1025 | `12-show-protocols-through-showmon.md` |
| [`show wiretap`](chapters/12-show-protocols-through-showmon.md#show-wiretap) | 12 |  | 1026 | `12-show-protocols-through-showmon.md` |
| [`show whoami`](chapters/12-show-protocols-through-showmon.md#show-whoami) | 12 |  | 1027 | `12-show-protocols-through-showmon.md` |
| [`showmon`](chapters/12-show-protocols-through-showmon.md#showmon) | 12 |  | 1028 | `12-show-protocols-through-showmon.md` |
| [`slave auto-sync config`](chapters/13-slave-auto-sync-config-through-terminal-type.md#slave-auto-sync-config) | 13 |  | 1030 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`slave default-slot`](chapters/13-slave-auto-sync-config-through-terminal-type.md#slave-default-slot) | 13 |  | 1031 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`slave image`](chapters/13-slave-auto-sync-config-through-terminal-type.md#slave-image) | 13 |  | 1032 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`slave reload`](chapters/13-slave-auto-sync-config-through-terminal-type.md#slave-reload) | 13 |  | 1033 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`slave sync config`](chapters/13-slave-auto-sync-config-through-terminal-type.md#slave-sync-config) | 13 |  | 1034 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`slave terminal`](chapters/13-slave-auto-sync-config-through-terminal-type.md#slave-terminal) | 13 |  | 1035 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software clean`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-clean) | 13 |  | 1036 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software commit`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-commit) | 13 |  | 1038 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software expand`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-expand) | 13 |  | 1041 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software install file`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-install-file) | 13 |  | 1046 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software install source switch`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-install-source-switch) | 13 |  | 1049 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software install source switch`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-install-source-switch) | 13 |  | 1053 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software provision`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-provision) | 13 |  | 1056 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software repackage`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-repackage) | 13 |  | 1058 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software rollback`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-rollback) | 13 |  | 1058 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software source list`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-source-list) | 13 |  | 1061 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`software uninstall`](chapters/13-slave-auto-sync-config-through-terminal-type.md#software-uninstall) | 13 |  | 1062 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`special-character-bits`](chapters/13-slave-auto-sync-config-through-terminal-type.md#special-character-bits) | 13 |  | 1063 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`squeeze`](chapters/13-slave-auto-sync-config-through-terminal-type.md#squeeze) | 13 |  | 1064 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`stack-mib portname`](chapters/13-slave-auto-sync-config-through-terminal-type.md#stack-mib-portname) | 13 |  | 1067 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`state-machine`](chapters/13-slave-auto-sync-config-through-terminal-type.md#state-machine) | 13 |  | 1067 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`stopbits`](chapters/13-slave-auto-sync-config-through-terminal-type.md#stopbits) | 13 |  | 1069 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`storm-control level`](chapters/13-slave-auto-sync-config-through-terminal-type.md#storm-control-level) | 13 |  | 1069 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`sync-restart-delay`](chapters/13-slave-auto-sync-config-through-terminal-type.md#sync-restart-delay) | 13 |  | 1071 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`systat`](chapters/13-slave-auto-sync-config-through-terminal-type.md#systat) | 13 |  | 1072 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`system flowcontrol bus`](chapters/13-slave-auto-sync-config-through-terminal-type.md#system-flowcontrol-bus) | 13 |  | 1073 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`system jumbomtu`](chapters/13-slave-auto-sync-config-through-terminal-type.md#system-jumbomtu) | 13 |  | 1074 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`tdm clock priority`](chapters/13-slave-auto-sync-config-through-terminal-type.md#tdm-clock-priority) | 13 |  | 1075 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal data-character-bits`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-data-character-bits) | 13 |  | 1077 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal databits`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-databits) | 13 |  | 1077 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal dispatch-character`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-dispatch-character) | 13 |  | 1078 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal dispatch-timeout`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-dispatch-timeout) | 13 |  | 1079 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal download`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-download) | 13 |  | 1080 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal editing`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-editing) | 13 |  | 1081 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal escape-character`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-escape-character) | 13 |  | 1081 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal exec-character-bits`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-exec-character-bits) | 13 |  | 1082 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal flowcontrol`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-flowcontrol) | 13 |  | 1083 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal full-help`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-full-help) | 13 |  | 1084 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal history`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-history) | 13 |  | 1085 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal history size`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-history-size) | 13 |  | 1086 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal hold-character`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-hold-character) | 13 |  | 1088 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal international`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-international) | 13 |  | 1089 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal keymap-type`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-keymap-type) | 13 |  | 1090 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal length`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-length) | 13 |  | 1091 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal monitor`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-monitor) | 13 |  | 1092 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal notify`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-notify) | 13 |  | 1092 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal padding`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-padding) | 13 |  | 1093 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal parity`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-parity) | 13 |  | 1094 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal rxspeed`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-rxspeed) | 13 |  | 1094 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal special-character-bits`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-special-character-bits) | 13 |  | 1095 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal speed`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-speed) | 13 |  | 1096 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal start-character`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-start-character) | 13 |  | 1097 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal stop-character`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-stop-character) | 13 |  | 1098 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal stopbits`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-stopbits) | 13 |  | 1098 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal telnet break-on-ip`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-telnet-break-on-ip) | 13 |  | 1099 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal telnet refuse-negotiations`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-telnet-refuse-negotiations) | 13 |  | 1100 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal telnet speed`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-telnet-speed) | 13 |  | 1101 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal telnet sync-on-break`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-telnet-sync-on-break) | 13 |  | 1101 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal telnet transparent`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-telnet-transparent) | 13 |  | 1102 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal terminal-type`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-terminal-type) | 13 |  | 1103 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal txspeed`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-txspeed) | 13 |  | 1103 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal width`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-width) | 13 |  | 1104 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal-queue entry-retry-interval`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-queue-entry-retry-interval) | 13 |  | 1105 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`terminal-type`](chapters/13-slave-auto-sync-config-through-terminal-type.md#terminal-type) | 13 |  | 1106 | `13-slave-auto-sync-config-through-terminal-type.md` |
| [`test cable-diagnostics`](chapters/14-test-cable-diagnostics-through-xmodem.md#test-cable-diagnostics) | 14 |  | 1108 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`test flash`](chapters/14-test-cable-diagnostics-through-xmodem.md#test-flash) | 14 |  | 1109 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`test interfaces`](chapters/14-test-cable-diagnostics-through-xmodem.md#test-interfaces) | 14 |  | 1110 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`test memory`](chapters/14-test-cable-diagnostics-through-xmodem.md#test-memory) | 14 |  | 1111 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`test memory destroy`](chapters/14-test-cable-diagnostics-through-xmodem.md#test-memory-destroy) | 14 |  | 1111 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`test platform police get`](chapters/14-test-cable-diagnostics-through-xmodem.md#test-platform-police-get) | 14 |  | 1112 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`test platform police set`](chapters/14-test-cable-diagnostics-through-xmodem.md#test-platform-police-set) | 14 |  | 1113 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`tftp-server`](chapters/14-test-cable-diagnostics-through-xmodem.md#tftp-server) | 14 |  | 1114 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`time-period`](chapters/14-test-cable-diagnostics-through-xmodem.md#time-period) | 14 |  | 1117 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`trace (privileged)`](chapters/14-test-cable-diagnostics-through-xmodem.md#trace-privileged) | 14 |  | 1118 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`trace (user)`](chapters/14-test-cable-diagnostics-through-xmodem.md#trace-user) | 14 |  | 1122 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`traceroute`](chapters/14-test-cable-diagnostics-through-xmodem.md#traceroute) | 14 |  | 1124 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`traceroute mac`](chapters/14-test-cable-diagnostics-through-xmodem.md#traceroute-mac) | 14 |  | 1127 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`undelete`](chapters/14-test-cable-diagnostics-through-xmodem.md#undelete) | 14 |  | 1130 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`unprofile`](chapters/14-test-cable-diagnostics-through-xmodem.md#unprofile) | 14 |  | 1132 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`upgrade automatic abortversion`](chapters/14-test-cable-diagnostics-through-xmodem.md#upgrade-automatic-abortversion) | 14 |  | 1132 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`upgrade automatic getversion`](chapters/14-test-cable-diagnostics-through-xmodem.md#upgrade-automatic-getversion) | 14 |  | 1133 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`upgrade automatic runversion`](chapters/14-test-cable-diagnostics-through-xmodem.md#upgrade-automatic-runversion) | 14 |  | 1136 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`upgrade filesystem monlib`](chapters/14-test-cable-diagnostics-through-xmodem.md#upgrade-filesystem-monlib) | 14 |  | 1137 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`upgrade rom-monitor`](chapters/14-test-cable-diagnostics-through-xmodem.md#upgrade-rom-monitor) | 14 |  | 1138 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`upgrade filesystem monlib`](chapters/14-test-cable-diagnostics-through-xmodem.md#upgrade-filesystem-monlib) | 14 |  | 1142 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`upgrade rom-monitor preference`](chapters/14-test-cable-diagnostics-through-xmodem.md#upgrade-rom-monitor-preference) | 14 |  | 1143 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`vacant-message`](chapters/14-test-cable-diagnostics-through-xmodem.md#vacant-message) | 14 |  | 1144 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`verify`](chapters/14-test-cable-diagnostics-through-xmodem.md#verify) | 14 |  | 1145 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`vtp`](chapters/14-test-cable-diagnostics-through-xmodem.md#vtp) | 14 |  | 1150 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`warm-reboot`](chapters/14-test-cable-diagnostics-through-xmodem.md#warm-reboot) | 14 |  | 1153 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`where`](chapters/14-test-cable-diagnostics-through-xmodem.md#where) | 14 |  | 1154 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`width`](chapters/14-test-cable-diagnostics-through-xmodem.md#width) | 14 |  | 1155 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`write core`](chapters/14-test-cable-diagnostics-through-xmodem.md#write-core) | 14 |  | 1156 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`write memory`](chapters/14-test-cable-diagnostics-through-xmodem.md#write-memory) | 14 |  | 1157 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`write mib-data`](chapters/14-test-cable-diagnostics-through-xmodem.md#write-mib-data) | 14 |  | 1158 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`write network`](chapters/14-test-cable-diagnostics-through-xmodem.md#write-network) | 14 |  | 1159 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`write terminal`](chapters/14-test-cable-diagnostics-through-xmodem.md#write-terminal) | 14 |  | 1160 | `14-test-cable-diagnostics-through-xmodem.md` |
| [`xmodem`](chapters/14-test-cable-diagnostics-through-xmodem.md#xmodem) | 14 |  | 1160 | `14-test-cable-diagnostics-through-xmodem.md` |
