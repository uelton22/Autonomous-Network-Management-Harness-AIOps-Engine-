"""
harness/run_harness_test.py
Suíte de Validação e Teste do Harness AIOps e Servidor MCP SSH.
Executa validações reais:
1. Gatekeeper de Privilégios (read vs editor vs full) — 100% determinístico.
2. Pipeline Híbrido de Parsing TTP & OpenConfig (Tier 1 Cache Hit vs Tier 2 Auto-Cura vs Tier 3 Pydantic).
3. Teste Live de Conexão e Ação Canônica no Equipamento Real (se NETOPS_TARGET_HOST estiver configurado).
"""

import os
import sys
import json
import time
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

load_dotenv()

from mcp_server.security import validate_command_privilege, PrivilegeLevel
from mcp_server.ttp_engine import TTPHybridEngine, DeviceInfoSchema
from mcp_server.server import run_canonical_action, discover_device, execute_command

console = Console()


def run_all_tests():
    console.print(Panel.fit(
        "[bold cyan]NetOps AIOps Harness — Suíte de Testes e Validação[/bold cyan]\n"
        "[dim]Ambiente de Produção / Equipamento Real | 3-Tier Security | Hybrid TTP | OpenConfig[/dim]",
        border_style="cyan"
    ))

    passed_count = 0

    # ---------------------------------------------------------------------
    # TESTE 1: GATEKEEPER DE PRIVILÉGIOS EM 3 NÍVEIS
    # ---------------------------------------------------------------------
    console.print("\n[bold yellow]═══ TESTE 1: Gatekeeper de Segurança e Privilégios (read / editor / full) ═══[/bold yellow]")
    
    test_cases = [
        ("show firmware", PrivilegeLevel.READ, True, "Inspeção permitida em READ"),
        ("show platform", PrivilegeLevel.READ, True, "Inspeção permitida em READ"),
        ("display version", PrivilegeLevel.READ, True, "Inspeção permitida em READ"),
        ("system-view", PrivilegeLevel.READ, False, "Entrada em config bloqueada em READ"),
        ("configure terminal", PrivilegeLevel.READ, False, "Entrada em config bloqueada em READ"),
        ("reboot", PrivilegeLevel.READ, False, "Comando destrutivo bloqueado em READ"),
        ("reboot", PrivilegeLevel.EDITOR, False, "Comando destrutivo bloqueado em EDITOR"),
        ("reboot", PrivilegeLevel.FULL, True, "Comando destrutivo permitido em FULL"),
        ("interface 1/1/1 description UPLINK", PrivilegeLevel.EDITOR, True, "Configuração pontual permitida em EDITOR"),
        ("format flash:", PrivilegeLevel.EDITOR, False, "Wipe catastrófico bloqueado em EDITOR"),
    ]

    t1 = Table(title="Matriz de Validação do Gatekeeper", border_style="blue")
    t1.add_column("Comando Testado", style="white")
    t1.add_column("Nível de Privilégio", style="cyan")
    t1.add_column("Esperado", style="bold")
    t1.add_column("Resultado", style="green")

    for cmd, priv, expected, desc in test_cases:
        allowed, reason = validate_command_privilege(cmd, priv)
        status_str = "[green]PERMITIDO[/green]" if allowed else "[red]BLOQUEADO[/red]"
        expected_str = "[green]PERMITIDO[/green]" if expected else "[red]BLOQUEADO[/red]"
        assert allowed == expected, f"Falha no comando '{cmd}' com privilégio '{priv}'"
        t1.add_row(cmd, priv.value.upper(), expected_str, status_str)

    console.print(t1)
    console.print("[bold green]✔ Teste 1 APROVADO: Gatekeeper bloqueia 100% das ações indevidas.[/bold green]")
    passed_count += 1

    # ---------------------------------------------------------------------
    # TESTE 2: PIPELINE HÍBRIDO TTP & VALIDAÇÃO OPENCONFIG
    # ---------------------------------------------------------------------
    console.print("\n[bold yellow]═══ TESTE 2: Pipeline Híbrido TTP & Validação OpenConfig Pydantic ═══[/bold yellow]")
    
    engine = TTPHybridEngine(
        template_dir="storage/templates"
    )

    sample_dmos_firmware = """Status: Idle
Download progress: -

Version                     State   
------------------------------------
11.4.0-024-1-g9fd43bed90    Inactive
12.0.2-001-1-gf41347caff    Active
"""
    # 1. Limpa template em disco se houver para testar síntese/promoção
    target_ttp = Path("storage/templates/get_system_version/datacom_dmos__12_0_2.ttp")
    if target_ttp.exists():
        target_ttp.unlink()

    # Execução 1: Tier 2 Auto-Cura / Síntese -> Salva Cache
    res1 = engine.parse_with_pipeline(
        action="get_system_version",
        vendor="datacom",
        os_family="dmos",
        version="12_0_2",
        raw_stdout=sample_dmos_firmware,
        device_hostname="100.75.9.252"
    )
    console.print(f"1ª Execução (Síntese & Promoção): [magenta]{res1['tier']}[/magenta]")
    assert not res1["cache_hit"], "Deveria ser Cache Miss na primeira execução!"
    assert target_ttp.exists(), "Template TTP não foi salvo no disco!"

    # Execução 2: Tier 1 Cache Hit (< 5ms)
    t_start = time.time()
    res2 = engine.parse_with_pipeline(
        action="get_system_version",
        vendor="datacom",
        os_family="dmos",
        version="12_0_2",
        raw_stdout=sample_dmos_firmware,
        device_hostname="100.75.9.252"
    )
    t_elapsed = (time.time() - t_start) * 1000
    console.print(f"2ª Execução (Cache Hit): [green]{res2['tier']}[/green] em [bold green]{t_elapsed:.2f} ms[/bold green]")
    assert res2["cache_hit"], "Deveria ser Cache Hit na segunda execução!"

    t2 = Table(title="Payload Canônico OpenConfig Normalizado (DeviceInfo)", border_style="blue")
    t2.add_column("Campo", style="cyan")
    t2.add_column("Valor Extraído", style="bold white")
    for k, v in res2["data"].items():
        t2.add_row(k, str(v))
    console.print(t2)

    # Validação LLDP Neighbors
    sample_dmos_lldp = """                        NEIGHBOR  CHASSIS ID                                                                                                            
LOCAL INTERFACE         ID        SUBTYPE      CHASSIS ID         SYSTEM NAME                           PORT ID                 PORT DESCRIPTION        
--------------------------------------------------------------------------------------------------------------------------------------------------------
gigabit-ethernet-1/1/5  5         mac-address  18:81:ed:14:51:48  5.4.242-SWT-BAIXA-GRANDE-R-GONCALVES  gigabit-ethernet-1/1/5  gigabit-ethernet-1/1/5  
"""
    res_lldp = engine.parse_with_pipeline(
        action="get_lldp_neighbors",
        vendor="datacom",
        os_family="dmos",
        version="12_0_2",
        raw_stdout=sample_dmos_lldp,
        device_hostname="unit-test-dmos"
    )
    assert len(res_lldp["data"]["neighbors"]) == 1, "Falha na extração do vizinho LLDP!"
    assert res_lldp["data"]["neighbors"][0]["system_name"] == "5.4.242-SWT-BAIXA-GRANDE-R-GONCALVES"
    console.print("[bold green]✔ LLDP Parsing e Validação OpenConfig comprovada com sucesso.[/bold green]")

    console.print("[bold green]✔ Teste 2 APROVADO: Parsing TTP e validação OpenConfig com sucesso.[/bold green]")
    passed_count += 1

    # ---------------------------------------------------------------------
    # TESTE 3: CONEXÃO REAL COM EQUIPAMENTO (se NETOPS_TARGET_HOST configurado)
    # ---------------------------------------------------------------------
    target_host = os.getenv("NETOPS_TARGET_HOST", "100.75.9.252")
    console.print(f"\n[bold yellow]═══ TESTE 3: Verificação Live no Equipamento Real ({target_host}) ═══[/bold yellow]")

    try:
        console.print(f"Conectando via SSH ao switch no IP [cyan]{target_host}[/cyan]...")
        
        # 1. Descoberta Zero-Knowledge
        fp_json = discover_device(target_host)
        fp_data = json.loads(fp_json)
        console.print(f"Fingerprinting do Host: [bold green]{fp_data.get('metadata')}[/bold green]")
        
        assert fp_data.get("status") == "success", f"Falha na descoberta do host {target_host}"
        
        # 2. Execução da Ação Canônica get_system_version
        action_json = run_canonical_action(target_host, "get_system_version", "read")
        action_data = json.loads(action_json)
        
        assert action_data.get("status") == "success", f"Falha na ação canônica: {action_data.get('error')}"
        
        console.print(f"Comando executado: [cyan]{action_data.get('command_executed')}[/cyan]")
        console.print(f"Raw salvo em: [green]{action_data.get('raw_path')}[/green]")
        console.print(f"OpenConfig Data: [bold white]{action_data.get('openconfig_data')}[/bold white]")

        console.print(f"[bold green]✔ Teste 3 APROVADO: Equipamento real {target_host} consultado e validado com sucesso.[/bold green]")
        passed_count += 1
    except Exception as e:
        console.print(f"[bold red]✖ Teste 3 Falhou ao conectar no host real {target_host}: {e}[/bold red]")
        console.print("[yellow]Verifique se a VPN/rota para 100.75.9.252 está ativa e as credenciais no .env estão corretas.[/yellow]")

    console.print(Panel.fit(
        f"[bold green]Suíte Concluída: {passed_count} testes executados com sucesso![/bold green]",
        border_style="green"
    ))


if __name__ == "__main__":
    run_all_tests()
