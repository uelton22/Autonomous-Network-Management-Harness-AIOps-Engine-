# Claude Code Guidelines: Network AIOps Harness

## Overview
This repository implements an autonomous, multi-vendor network management harness (Datacom DmOS, Huawei VRP, Cisco IOS-XE) driven by file-based rules, canonical action mappings, and an MCP SSH server with a 3-tier privilege gatekeeper.

## Core Commands
- Run MCP Server in test mode: `source .venv/bin/activate && python3 -m mcp_server.server --test`
- Run full harness test suite: `source .venv/bin/activate && python3 -m harness.run_harness_test`

## Key Architecture Rules
- All CLI commands must be resolved via `registry/actions.yaml`.
- Datacom commands must strictly adhere to DmOS syntax (`show firmware`, `show platform | include DM`, `show system uptime`, `show interface brief`).
- Privilege gatekeeper enforces 3 tiers: `read`, `editor`, `full`. Read is the mandatory default.
- CLI raw outputs are written directly to `storage/raw/*.raw` on disk and parsed locally via TTP templates (`storage/templates/`).
- **No Manual .RAW Reading**: Agents must NEVER manually read `.raw` files using filesystem tools. All responses must rely strictly on structured JSON produced by `run_canonical_action` or `run_adhoc_action`.
- Multi-step investigations must follow the DAG pattern (`diagnose_down_interfaces`).
- **Target Host Isolation**: Execute strictly and exclusively on the target host/IP specified by the operator. No mock devices exist in the codebase. Never query unspecified hosts.
- Refer to `AGENTS.md` for the complete step-by-step reasoning and execution cycle.
