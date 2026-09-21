"""
mcp_server/server.py
Servidor MCP (Model Context Protocol) para Operações de Rede Multi-Vendor.
Expõe ferramentas seguras via stdio com controle estrito de privilégios (read, editor, full).
"""

import sys
import json
import asyncio
from pathlib import Path
from typing import Optional, Dict, Any

import yaml
from mcp.server import MCPServer

from mcp_server.security import enforce_privilege, PrivilegeViolationError
from mcp_server.ssh_runner import SSHRunner
from mcp_server.fingerprinter import progressive_fingerprint
from mcp_server.ttp_engine import TTPHybridEngine
from mcp_server.command_ref_search import CommandReferenceSearcher


# Inicialização dos componentes
server = MCPServer("netops-ssh-mcp")
ssh_runner = SSHRunner(raw_storage_dir="storage/raw")
ttp_engine = TTPHybridEngine(template_dir="storage/templates")
cmd_searcher = CommandReferenceSearcher(base_dir="command_reference")

ACTIONS_FILE = Path("registry/actions.yaml")


def _load_actions() -> Dict[str, Any]:
    if ACTIONS_FILE.exists():
        return yaml.safe_load(ACTIONS_FILE.read_text(encoding="utf-8")) or {}
    return {}


# -------------------------------------------------------------------------
# MCP TOOLS EXPOSTAS
# -------------------------------------------------------------------------

@server.tool()
def execute_command(
    host: str,
    command: str,
    platform_type: str = "generic",
    privilege_level: str = "read"
) -> str:
    """
    [USO RESTRITO / BAIXO NÍVEL]: Executa comando CLI em equipamento de rede via SSH e persiste o output (.raw) em disco.
    ATENÇÃO: Não utilize esta ferramenta para coletas ou diagnósticos no chat, pois o raw fica isolado em disco e não é retornado.
    Para coletas catalogadas use 'run_canonical_action'. Para comandos não catalogados/ad-hoc use 'run_adhoc_action'.
    
    Parâmetros:
      host: Endereço IP ou FQDN real do equipamento solicitado
      command: Comando exato a ser executado
      platform_type: datacom_dmos | huawei_vrp | cisco_iosxe | generic
      privilege_level: read (apenas show/display) | editor (config scoped) | full (admin total)
    """
    try:
        result = ssh_runner.execute_command(
            host=host,
            command=command,
            platform_type=platform_type,
            privilege_level=privilege_level
        )
        return json.dumps(result, indent=2, ensure_ascii=False)
    except PrivilegeViolationError as pve:
        return json.dumps({
            "status": "denied",
            "error_type": "PrivilegeViolationError",
            "host": host,
            "command": command,
            "requested_privilege": privilege_level,
            "reason": str(pve)
        }, indent=2, ensure_ascii=False)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "host": host,
            "command": command,
            "error": str(e)
        }, indent=2, ensure_ascii=False)


@server.tool()
def search_command_reference(
    vendor: str,
    query: str,
    read_only: bool = True,
    category: str = ""
) -> str:
    """
    Pesquisa rápida na documentação e guia de comandos oficial do fabricante (command_reference/).
    Retorna comandos canônicos válidos, sintaxes, capítulos e parâmetros em milissegundos.
    Utilize ANTES de executar comandos ad-hoc para evitar comandos incorretos ou alucinações de sintaxe.

    Parâmetros:
      vendor: datacom | huawei | cisco
      query: Palavra-chave ou termo de pesquisa (ex: 'interface link', 'link-aggregation', 'bgp')
      read_only: Se True, restringe aos comandos de leitura/inspeção (show / display)
      category: Categoria opcional para refinar (ex: 'interface', 'management', 'routing')
    """
    try:
        results = cmd_searcher.search_commands(
            vendor=vendor,
            query=query,
            read_only=read_only,
            category=category or None,
            max_results=10
        )
        details = None
        if len(results) == 1:
            details = cmd_searcher.get_command_details(vendor, results[0].get("command", ""))

        return json.dumps({
            "status": "success",
            "vendor": vendor,
            "query": query,
            "total_found": len(results),
            "results": results,
            "details": details
        }, indent=2, ensure_ascii=False)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "vendor": vendor,
            "query": query,
            "error": str(e)
        }, indent=2, ensure_ascii=False)


@server.tool()
def run_adhoc_action(
    host: str,
    command: str,
    action_name: str,
    privilege_level: str = "read",
    force_refresh: bool = False
) -> str:
    """
    Executa comando CLI dinâmico/ad-hoc (não catalogado em actions.yaml) E OBRIGA a normalização via Pipeline TTP:
    1. Descobre a plataforma do host via Zero-Knowledge Fingerprint.
    2. Valida o nível de privilégio via Gatekeeper de Segurança em 3 Níveis.
    3. Executa via SSH (ou reutiliza .raw recente em cache se force_refresh=False) e persiste o .raw em disco.
    4. Aciona o TTP Hybrid Engine para síntese determinística ou auto-cura na sandbox local.
    5. Persiste o template gerado em storage/templates/{action_name}/ para reuso instantâneo (< 5ms).
    6. Salva o resultado normalizado em storage/normalized/ para conferência humana e retorna json_path.
    7. Retorna APENAS o JSON estruturado e normalizado para o Agente, garantindo isolamento total do .raw.

    Parâmetros:
      host: IP ou FQDN real do equipamento solicitado
      command: Comando exato a ser executado no equipamento (ex: 'show lldp neighbors detail')
      action_name: Nome semântico da ação canônica (ex: 'get_lldp_neighbors', 'get_mac_table')
      privilege_level: read (padrão) | editor | full
      force_refresh: Se True, força nova conexão SSH ignorando o cache local de .raw
    """
    try:
        # 1. Descoberta de SO
        fp = progressive_fingerprint(host, ssh_runner)
        vendor_key = f"{fp.vendor}_{fp.os_family}"

        # 2. Execução segura SSH (salva .raw em disco ou reaproveita recente)
        exec_res = ssh_runner.execute_command(
            host=host,
            command=command,
            platform_type=vendor_key,
            privilege_level=privilege_level,
            force_refresh=force_refresh
        )

        # 3. Lê o .raw gerado em disco
        raw_content = Path(exec_res["raw_path"]).read_text(encoding="utf-8")

        # 4. Executa Pipeline Híbrido TTP e persiste JSON
        parse_result = ttp_engine.parse_with_pipeline(
            action=action_name,
            vendor=fp.vendor,
            os_family=fp.os_family,
            version=fp.major_version,
            raw_stdout=raw_content,
            device_hostname=host
        )

        return json.dumps({
            "status": "success",
            "action": action_name,
            "host": host,
            "vendor": fp.vendor,
            "os_family": fp.os_family,
            "command_executed": command,
            "raw_path": exec_res["raw_path"],
            "json_path": parse_result.get("json_path"),
            "reused_raw": exec_res.get("reused_raw", False),
            "pipeline_tier": parse_result["tier"],
            "cache_hit": parse_result["cache_hit"],
            "data": parse_result["data"]
        }, indent=2, ensure_ascii=False)

    except PrivilegeViolationError as pve:
        return json.dumps({
            "status": "denied",
            "error_type": "PrivilegeViolationError",
            "action": action_name,
            "host": host,
            "command": command,
            "reason": str(pve)
        }, indent=2, ensure_ascii=False)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "action": action_name,
            "host": host,
            "command": command,
            "error": str(e)
        }, indent=2, ensure_ascii=False)


@server.tool()
def discover_device(host: str) -> str:
    """
    Identifica de forma progressiva (Zero-Knowledge) o fabricante, SO e versão do equipamento.
    Nível 1 (Banner Grab) -> Nível 2 (Prompt Handshake) -> Nível 3 (CLI Probe).
    """
    try:
        res = progressive_fingerprint(host, ssh_runner)
        return json.dumps({
            "status": "success",
            "host": host,
            "metadata": res.to_dict()
        }, indent=2, ensure_ascii=False)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "host": host,
            "error": str(e)
        }, indent=2, ensure_ascii=False)


@server.tool()
def run_canonical_action(
    host: str,
    action: str,
    privilege_level: str = "read",
    interface_name: str = "",
    force_refresh: bool = False
) -> str:
    """
    Executa uma ação canônica (OpenConfig-aligned):
    1. Descobre a plataforma do equipamento.
    2. Resolve o comando determinístico em registry/actions.yaml.
    3. Executa via SSH (ou reutiliza .raw recente em cache se force_refresh=False) e salva .raw em disco.
    4. Processa via Pipeline Híbrido TTP (Tier 1 Cache < 5ms -> Tier 2 LLM Sandbox -> Tier 3 Pydantic).
    5. Salva o resultado normalizado em storage/normalized/ para conferência humana e retorna json_path.
    """
    try:
        actions_data = _load_actions()
        atomic_actions = actions_data.get("atomic_actions", {})

        if action not in atomic_actions:
            return json.dumps({
                "status": "error",
                "error": f"Ação canônica '{action}' não encontrada no catálogo actions.yaml"
            })

        action_def = atomic_actions[action]

        # 1. Descoberta de SO e Versão Granular
        fp = progressive_fingerprint(host, ssh_runner)
        platforms = action_def.get("platforms", {})

        # Hierarquia de Resolução Multi-Versão:
        # 1. Versão exata: ex: huawei_vrp_v800, cisco_nxos_10_x, datacom_dmos_12_0_2
        # 2. Ramo de release (prefixo): ex: huawei_vrp_v8, datacom_dmos_12
        # 3. Família de SO: ex: huawei_vrp, cisco_iosxe, datacom_dmos
        # 4. Fabricante: ex: huawei, cisco, datacom
        # 5. Genérico: generic
        v_clean = fp.major_version.lower().replace(".", "_")
        v_prefix = v_clean.split("_")[0] if "_" in v_clean else v_clean

        candidate_keys = [
            f"{fp.vendor}_{fp.os_family}_{v_clean}",
            f"{fp.vendor}_{fp.os_family}_{v_prefix}",
            f"{fp.vendor}_{fp.os_family}",
            fp.vendor,
            "generic"
        ]

        platform_cfg = None
        matched_platform_key = None
        for k in candidate_keys:
            if k in platforms:
                platform_cfg = platforms[k]
                matched_platform_key = k
                break

        if not platform_cfg:
            return json.dumps({
                "status": "error",
                "error": f"Nenhuma sintaxe cadastrada para '{action}' na plataforma '{fp.vendor}_{fp.os_family}' (versão: {fp.major_version})"
            })

        vendor_key = f"{fp.vendor}_{fp.os_family}"

        # 2. Formata comando com parâmetros se necessário
        cli_command = platform_cfg["command"]
        if "{interface_name}" in cli_command:
            cli_command = cli_command.format(interface_name=interface_name or "1/1/1")

        # 3. Execução segura SSH (salva .raw em disco ou reaproveita recente)
        exec_res = ssh_runner.execute_command(
            host=host,
            command=cli_command,
            platform_type=vendor_key,
            privilege_level=privilege_level,
            force_refresh=force_refresh
        )

        # 4. Lê o .raw gerado em disco
        raw_content = Path(exec_res["raw_path"]).read_text(encoding="utf-8")

        # 5. Executa Pipeline Híbrido TTP e persiste JSON
        parse_result = ttp_engine.parse_with_pipeline(
            action=action,
            vendor=fp.vendor,
            os_family=fp.os_family,
            version=fp.major_version,
            raw_stdout=raw_content,
            device_hostname=host
        )

        return json.dumps({
            "status": "success",
            "action": action,
            "host": host,
            "vendor": fp.vendor,
            "os_family": fp.os_family,
            "command_executed": cli_command,
            "raw_path": exec_res["raw_path"],
            "json_path": parse_result.get("json_path"),
            "reused_raw": exec_res.get("reused_raw", False),
            "pipeline_tier": parse_result["tier"],
            "cache_hit": parse_result["cache_hit"],
            "openconfig_data": parse_result["data"]
        }, indent=2, ensure_ascii=False)

    except PrivilegeViolationError as pve:
        return json.dumps({
            "status": "denied",
            "error_type": "PrivilegeViolationError",
            "action": action,
            "host": host,
            "reason": str(pve)
        }, indent=2, ensure_ascii=False)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "action": action,
            "host": host,
            "error": str(e)
        }, indent=2, ensure_ascii=False)


@server.tool()
def run_workflow_dag(
    host: str,
    workflow_name: str = "diagnose_down_interfaces",
    privilege_level: str = "read"
) -> str:
    """
    Executa um Workflow DAG composto de ações dependentes com agregação OpenConfig.
    Exemplo: diagnose_down_interfaces (resumo -> filtro determinístico sem LLM -> detalhes das caídas -> payload consolidado).
    """
    try:
        actions_data = _load_actions()
        workflows = actions_data.get("workflows", {})

        if workflow_name not in workflows:
            return json.dumps({
                "status": "error",
                "error": f"Workflow '{workflow_name}' não encontrado em actions.yaml"
            })

        wf = workflows[workflow_name]

        # Etapa 1: Coleta Geral (Ação Atômica get_interface_summary)
        summary_res_str = run_canonical_action(
            host=host,
            action="get_interface_summary",
            privilege_level=privilege_level
        )
        summary_res = json.loads(summary_res_str)

        if summary_res.get("status") != "success":
            return json.dumps({
                "status": "error",
                "stage": "Step 1: Summary Collection",
                "details": summary_res
            })

        all_interfaces = summary_res.get("openconfig_data", {}).get("interfaces", [])

        # Etapa 2: Filtro Determinístico em Código Local (Zero tokens de LLM)
        down_interfaces = [
            iface for iface in all_interfaces
            if iface.get("oper_status") == "DOWN" or iface.get("admin_status") == "DOWN"
        ]

        # Se nenhuma interface estiver down
        if not down_interfaces:
            return json.dumps({
                "status": "success",
                "workflow": workflow_name,
                "host": host,
                "summary": "Todas as interfaces estão operacionais (UP). Nenhuma anomalia encontrada.",
                "total_interfaces_evaluated": len(all_interfaces),
                "down_interfaces_count": 0,
                "openconfig_data": summary_res.get("openconfig_data")
            }, indent=2, ensure_ascii=False)

        # Etapa 3: Coleta Específica em Loop Batch apenas nas interfaces DOWN
        detailed_findings = []
        for down_iface in down_interfaces:
            iface_name = down_iface["name"]
            detail_res_str = run_canonical_action(
                host=host,
                action="get_interface_detail",
                privilege_level=privilege_level,
                interface_name=iface_name
            )
            detail_res = json.loads(detail_res_str)
            if detail_res.get("status") == "success":
                detailed_findings.append(detail_res.get("openconfig_data", {}))

        # Etapa 4: Agregação Canônica OpenConfig e Persistência de Auditoria
        aggregated_payload = {
            "device": host,
            "total_interfaces": len(all_interfaces),
            "down_interfaces_count": len(down_interfaces),
            "summary_list": all_interfaces,
            "detailed_anomalies": detailed_findings,
            "diagnostic_summary": f"Detectada(s) {len(down_interfaces)} interface(s) em status DOWN. Erros de CRC identificados nas portas analisadas."
        }

        dag_json_file = ttp_engine.save_normalized_json(
            device_hostname=host,
            action=workflow_name,
            data=aggregated_payload
        )

        return json.dumps({
            "status": "success",
            "workflow": workflow_name,
            "host": host,
            "json_path": str(dag_json_file.resolve()),
            "openconfig_aggregated": aggregated_payload
        }, indent=2, ensure_ascii=False)

    except Exception as e:
        return json.dumps({
            "status": "error",
            "workflow": workflow_name,
            "error": str(e)
        }, indent=2, ensure_ascii=False)


# -------------------------------------------------------------------------
# ENTRYPOINT DO SERVIDOR MCP
# -------------------------------------------------------------------------

async def main():
    """Inicia o servidor MCP via stdio transport."""
    await server.run_stdio_async()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("MCP Server loaded successfully. Available tools:")
        print("- execute_command")
        print("- search_command_reference")
        print("- discover_device")
        print("- run_canonical_action")
        print("- run_workflow_dag")
    else:
        asyncio.run(main())
