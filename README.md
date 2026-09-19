# Autonomous Network Management Harness (AIOps Engine)

> **Normalização Multi-Vendor Inteligente com Agentes Distribuídos, Servidor MCP SSH e Orquestração DAG.**

Este projeto implementa um **Harness de Rede Orientado a Agente (Markdown/YAML First)** operável por qualquer sessão de IA (Cursor, Claude Code, Antigravity, Codex), com controle estrito de privilégios em 3 níveis e pipeline híbrido de parsing TTP alinhado aos padrões OpenConfig.

---

## 1. Destaques da Arquitetura

1. **Gatekeeper de Segurança em 3 Níveis (`read`, `editor`, `full`)**:
   - `read`: Apenas comandos de inspeção (`show *`, `display *`, `dir`, `ping`, `traceroute`). Bloqueia imediatamente qualquer comando de configuração (`system-view`, `config`), mutação (`shutdown`, `undo`) ou destrutivo (`reboot`, `reset`).
   - `editor`: Permite leituras e alterações operacionais pontuais previamente autorizadas (ex: descrição de interface), bloqueando ações catastróficas.
   - `full`: Acesso irrestrito (nível admin/superuser).
2. **Descoberta Progressiva Zero-Knowledge**:
   - Identifica o equipamento em 3 etapas determinísticas: **L1 Banner Grab (TCP 22)** $\rightarrow$ **L2 Prompt Handshake** $\rightarrow$ **L3 Deterministic CLI Probe**.
3. **Isolamento de `.raw` em Disco**:
   - Dumps gigantes de CLI são gravados fisicamente em `storage/raw/*.raw` e **nunca são enviados integralmente à LLM**, prevenindo saturação de contexto, alucinações e custos de token.
4. **Pipeline Híbrido de Parsing TTP (3 Tiers)**:
   - **Tier 1 (Fast-Path < 5ms)**: TTP determinístico via templates cacheados em `storage/templates/`.
   - **Tier 2 (Auto-Cura LLM & Sandbox)**: Em caso de Cache Miss ou alteração de layout, a LLM sintetiza o template com auxílio da Vendor Skill, testa contra o `.raw` integral no Sandbox local e valida no schema Pydantic antes de promover ao cache.
   - **Tier 3 (Strict Validation)**: Validação estrita em modelos Pydantic OpenConfig (`device_info`, `interfaces`, `bgp_summary`).
5. **Orquestração Multietapa (Workflows DAG)**:
   - Resolução de investigações complexas em grafo: coleta resumida $\rightarrow$ filtro determinístico em código local (sem LLM) $\rightarrow$ coleta detalhada em lote apenas nas portas com falha $\rightarrow$ agregação canônica OpenConfig.

---

## 2. Estrutura do Repositório

```
LLM_ssh_project/
├── AGENTS.md                          # Guia mestre do Agente Autônomo de Redes
├── .cursorrules                       # Regras para Cursor IDE
├── CLAUDE.md                          # Regras para Claude Code
│
├── registry/
│   ├── actions.yaml                   # Catálogo canônico de ações e DAGs
│   └── schemas/
│       ├── device_info.json           # Schema OpenConfig: device_info
│       ├── interfaces.json            # Schema OpenConfig: interfaces
│       └── bgp_summary.json           # Schema OpenConfig: bgp_summary
│
├── rules/
│   ├── 01-privilege-policy.md         # Política dos 3 níveis de privilégio
│   ├── 02-terminal-hygiene.md         # Pagers, prompts e timeouts
│   ├── 03-raw-data-handling.md        # Política de persistência de .raw em disco
│   ├── 04-dag-orchestration.md        # Diretrizes de execução de DAGs
│   └── 05-openconfig-norms.md         # Mapeamento para OpenConfig
│
├── skills/
│   ├── device-fingerprinting/
│   │   └── SKILL.md                   # SOP de descoberta L1, L2, L3
│   ├── ttp-self-healing/
│   │   └── SKILL.md                   # SOP de auto-cura de templates TTP
│   ├── dag-workflow-runner/
│   │   └── SKILL.md                   # SOP de orquestração de comandos dependentes
│   ├── network-vendor-datacom/
│   │   └── SKILL.md                   # Dialeto Datacom DmOS (show firmware, platform, etc.)
│   ├── network-vendor-huawei/
│   │   └── SKILL.md                   # Dialeto Huawei VRP (display version, etc.)
│   └── network-vendor-cisco/
│       └── SKILL.md                   # Dialeto Cisco IOS/IOS-XE
│
├── docs/
│   └── adrs/                          # Architecture Decision Records
│       ├── ADR-001-harness-markdown-first.md
│       ├── ADR-002-3-tier-privilege-gatekeeper.md
│       ├── ADR-003-hybrid-parsing-ttp-pipeline.md
│       ├── ADR-004-raw-disk-persistence-chunking.md
│       └── ADR-005-dag-multi-step-orchestration.md
│
├── harness/
│   ├── scenarios/                     # Cenários para execução no chat do IDE
│   │   ├── 01-datacom-discovery-and-version.md
│   │   ├── 02-privilege-guardrail-violation.md
│   │   ├── 03-raw-chunking-and-ttp-healing.md
│   │   └── 04-dag-down-interfaces-workflow.md
│   └── run_harness_test.py            # Runner de validação automatizada
│
├── storage/
│   ├── raw/                           # Gravação física dos arquivos .raw
│   └── templates/                     # Cache de templates TTP validados
│
└── mcp_server/                        # Servidor MCP SSH em Python
    ├── server.py                      # Entrypoint MCP stdio
    ├── security.py                    # Validador de privilégios (read/editor/full)
    ├── fingerprinter.py               # Descoberta L1/L2/L3
    ├── ssh_runner.py                  # SSH runner com gravação de .raw
    ├── ttp_engine.py                  # Motor Tier 1 / Sandbox Tier 2 / Tier 3
    └── mcp_config.json                # Configuração para Cursor e Claude Code
```

---

## 3. Como Executar os Testes Automatizados

Ative o ambiente virtual e execute a suíte de validação:

```bash
source .venv/bin/activate
python3 -m harness.run_harness_test
```

A suíte executará e comprovará:
1. **Descoberta Zero-Knowledge** de Datacom DM4610 e Huawei NE40E.
2. **Gatekeeper de Privilégios** bloqueando comandos proibidos e liberando comandos autorizados.
3. **Persistência de `.raw`** diretamente em `storage/raw/`.
4. **Auto-Cura TTP**: Cache Miss $\rightarrow$ Síntese $\rightarrow$ Validação em Sandbox $\rightarrow$ Promoção $\rightarrow$ Cache Hit (< 5ms) na 2ª vez.
5. **Orquestração Multietapa DAG**: Diagnóstico completo de interfaces DOWN via brief $\rightarrow$ filtro $\rightarrow$ detalhe em lote $\rightarrow$ agregação OpenConfig.

---

## 4. Configuração do Servidor MCP no Cursor / Claude Code

Para habilitar o servidor MCP nas suas ferramentas de IA:

### Cursor (`~/.cursor/mcp.json` ou `.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "netops-ssh-mcp": {
      "command": "/Users/uelton/Documents/Desenvolvimento/web2026/LLM_ssh_project/.venv/bin/python",
      "args": ["-m", "mcp_server.server"],
      "env": {
        "PYTHONPATH": "/Users/uelton/Documents/Desenvolvimento/web2026/LLM_ssh_project"
      }
    }
  }
}
```

### Claude Desktop / Claude Code (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "netops-ssh-mcp": {
      "command": "/Users/uelton/Documents/Desenvolvimento/web2026/LLM_ssh_project/.venv/bin/python",
      "args": ["-m", "mcp_server.server"]
    }
  }
}
```
