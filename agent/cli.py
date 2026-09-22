"""
agent/cli.py
Interface Interativa no Terminal (CLI) para o Agente Autônomo de Redes.
Permite executar operações de rede com LLMs Locais (Ollama, vLLM, LM Studio) de forma simples e intuitiva.
"""

import sys
import os
from typing import Dict, Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.theme import Theme

from agent.runner import LocalNetOpsAgent
from mcp_server.vault import get_vault

# Configuração de cores e estilos
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green",
    "prompt": "bold magenta"
})

console = Console(theme=custom_theme)


def print_banner(agent: LocalNetOpsAgent, health: Dict[str, Any]):
    """Imprime o cabeçalho executivo e o status da LLM local."""
    console.clear()
    vault = get_vault()
    active_prof = agent.active_profile or vault.default_profile
    
    title = "[bold white]NetOps AIOps Harness[/bold white] — [bold cyan]Terminal Interativo Autônomo[/bold cyan]"
    subtitle = "[dim]Orquestração Multi-Vendor (Datacom DmOS | Huawei VRP | Cisco IOS-XE) com LLM Local[/dim]"
    console.print(Panel(f"{title}\n{subtitle}", border_style="cyan"))

    status_table = Table(show_header=False, box=None, padding=(0, 2))
    status_table.add_column("Chave", style="dim cyan")
    status_table.add_column("Valor", style="white")

    status_table.add_row("Endpoint LLM:", agent.base_url)
    status_table.add_row("Modelo Configurado:", f"[bold green]{agent.model}[/bold green]")
    
    if health["status"] == "connected":
        models_avail = ", ".join(health.get("available_models", [])[:4])
        if len(health.get("available_models", [])) > 4:
            models_avail += "..."
        status_table.add_row("Status da LLM:", "[bold green]● Online e Conectado[/bold green]")
        if models_avail:
            status_table.add_row("Modelos Detectados:", f"[dim]{models_avail}[/dim]")
    else:
        status_table.add_row("Status da LLM:", f"[bold yellow]▲ Offline ou Inacessível[/bold yellow] ({health.get('error', 'Sem resposta')})")
        status_table.add_row("Como Iniciar:", "[cyan]Execute em outro terminal: [bold white]ollama run qwen2.5:14b[/bold white] (ou [bold white]ollama serve[/bold white])[/cyan]")

    status_table.add_row("Perfil SSH Ativo:", f"[bold cyan]{active_prof}[/bold cyan] [dim](Vault com {len(vault.profiles)} perfis cadastrados)[/dim]")
    status_table.add_row("Gatekeeper Ativo:", "[bold red]3 Níveis[/bold red] (read padrão | editor | full)")
    status_table.add_row("Parsing Engine:", "[bold green]TTP Híbrido (< 5ms)[/bold green] + OpenConfig Canônico")
    
    console.print(Panel(status_table, title="[bold]Ambiente e Conectividade[/bold]", border_style="dim"))
    console.print("[dim]Comandos úteis: [bold]/help[/bold] (ajuda) | [bold]/profiles[/bold] (ver perfis) | [bold]/profile <nome>[/bold] (trocar perfil) | [bold]/clear[/bold] (limpar) | [bold]/exit[/bold] (sair)[/dim]\n")


def execute_query(agent: LocalNetOpsAgent, user_query: str):
    """Executa a intenção do usuário no agente com animação e feedback de ferramentas."""
    current_spinner = None

    def on_tool_start(tool_name: str, args: Dict[str, Any]):
        host = args.get("host", "alvo")
        action = args.get("action") or args.get("command") or args.get("query") or ""
        msg = f"[cyan]Executando ferramenta [bold white]{tool_name}[/bold white] no host [bold yellow]{host}[/bold yellow] {f'({action})' if action else ''}...[/cyan]"
        console.print(f"  [dim]↳[/dim] {msg}")

    def on_tool_finish(tool_name: str, result: Dict[str, Any]):
        status = result.get("status", "done")
        tier = result.get("pipeline_tier", "")
        cached = result.get("cache_hit", False)
        cache_str = "[dim green](Cache Hit < 5ms)[/dim green]" if cached else ""
        if status == "success":
            console.print(f"  [dim]✔[/dim] [green]Ação concluída com sucesso[/green] {cache_str}")
        elif status == "denied":
            console.print(f"  [bold red]✖ Bloqueado pelo Gatekeeper:[/bold red] {result.get('reason')}")
        else:
            console.print(f"  [yellow]ℹ Retorno:[/yellow] {status}")

    with console.status("[bold cyan]Processando intenção com a LLM local...[/bold cyan]", spinner="dots"):
        try:
            response_text = agent.chat(
                user_input=user_query,
                on_tool_start=on_tool_start,
                on_tool_finish=on_tool_finish
            )
        except Exception as e:
            console.print(f"\n[error]Erro ao processar consulta com a LLM:[/error] {e}")
            return

    console.print("\n" + "─" * 80)
    console.print(Markdown(response_text))
    console.print("─" * 80 + "\n")


def show_profiles_table(vault, active_name: str):
    """Exibe os perfis de credenciais configurados no Vault em uma tabela Rich elegante."""
    table = Table(title="[bold cyan]Perfis de Credenciais SSH (Vault Seguro)[/bold cyan]", border_style="cyan")
    table.add_column("Perfil", style="bold white")
    table.add_column("Usuário", style="yellow")
    table.add_column("Porta", style="cyan", justify="right")
    table.add_column("Senha", style="dim")
    table.add_column("Chave SSH", style="dim")
    table.add_column("Status / Padrão", style="green")
    table.add_column("Descrição", style="white")

    for prof in vault.list_profiles():
        name = prof["name"]
        is_active = (name == active_name)
        status_tag = ""
        if is_active:
            status_tag = "[bold green]● ATIVO[/bold green]"
        elif prof["is_default"]:
            status_tag = "[dim green](default)[/dim green]"
        
        prof_name = f"[bold cyan]{name}[/bold cyan]" if is_active else name
        pwd_display = prof["password"] if prof["has_password"] else "[dim]nenhuma[/dim]"
        key_display = prof["ssh_key_path"] or "[dim]nenhuma[/dim]"

        table.add_row(
            prof_name,
            prof["username"],
            str(prof["port"]),
            pwd_display,
            key_display,
            status_tag,
            prof.get("description", "")
        )
    console.print(table)
    console.print("[dim]Para trocar de perfil use: [bold]/profile <nome>[/bold][/dim]\n")


def interactive_loop():
    """Loop de conversação interativa no terminal."""
    vault = get_vault()
    agent = LocalNetOpsAgent()
    health = agent.check_health()
    print_banner(agent, health)

    while True:
        try:
            cur_profile = agent.active_profile or vault.default_profile
            prompt_str = f"[bold cyan]netops[/bold cyan] [dim]({agent.model} | {cur_profile})[/dim] > "
            user_input = console.input(prompt_str).strip()

            if not user_input:
                continue

            # Comandos especiais do CLI
            if user_input.lower() in ("/exit", "/quit", "exit", "quit"):
                console.print("[dim]Encerrando sessão do Agente de Rede. Até logo![/dim]")
                break

            elif user_input.lower() in ("/clear", "clear", "cls"):
                agent.clear_history()
                print_banner(agent, agent.check_health())
                console.print("[green]Histórico da sessão reiniciado com sucesso.[/green]\n")
                continue

            elif user_input.lower() in ("/help", "help"):
                help_text = """
### Comandos Disponíveis no Terminal:
* `/profiles`: Lista todos os perfis de credenciais SSH cadastrados no Vault.
* `/profile <nome>`: Altera o perfil SSH ativo para a sessão (ex: `/profile zabbix`, `/profile admin`).
* `/model <nome>`: Altera o modelo da LLM dinamicamente (ex: `/model llama3.1:8b`).
* `/clear`: Limpa o histórico de diálogo preservando as regras de rede.
* `/status`: Revalida a conectividade com o Ollama/vLLM e exibe o cabeçalho.
* `/exit` ou `/quit`: Sai do terminal interativo.

### Exemplos de Intenções para Testar:
* `Identifique o equipamento no IP 100.75.9.252 usando o perfil zabbix.`
* `Liste os usuários locais e sessões ativas do switch 100.75.4.243.`
* `Quais perfis de conexão SSH estão disponíveis no cofre?`
* `Pesquise no manual da Huawei como configurar agregação eth-trunk.`
"""
                console.print(Markdown(help_text))
                continue

            elif user_input.lower() == "/profiles":
                cur_prof = agent.active_profile or vault.default_profile
                show_profiles_table(vault, cur_prof)
                continue

            elif user_input.lower().startswith("/profile"):
                parts = user_input.split(maxsplit=1)
                cur_prof = agent.active_profile or vault.default_profile
                if len(parts) > 1:
                    new_prof = parts[1].strip()
                    if new_prof in vault.profiles:
                        agent.active_profile = new_prof
                        console.print(f"[bold green]✔ Perfil de credencial alterado para: [cyan]{new_prof}[/cyan][/bold green] (usuário: {vault.profiles[new_prof].username})\n")
                    else:
                        avail = ", ".join(vault.profiles.keys())
                        console.print(f"[bold red]✖ Perfil '{new_prof}' não encontrado no Vault.[/bold red] Perfis disponíveis: [cyan]{avail}[/cyan]\n")
                else:
                    console.print(f"[yellow]Perfil ativo atual: [bold cyan]{cur_prof}[/bold cyan]. Uso: /profile <nome> (ou /profiles para listar)[/yellow]\n")
                continue

            elif user_input.lower().startswith("/model"):
                parts = user_input.split(maxsplit=1)
                if len(parts) > 1:
                    agent.model = parts[1].strip()
                    console.print(f"[green]Modelo alterado para: [bold]{agent.model}[/bold][/green]\n")
                else:
                    console.print(f"[yellow]Modelo atual: [bold]{agent.model}[/bold]. Uso: /model <nome>[/yellow]\n")
                continue

            elif user_input.lower() == "/status":
                h = agent.check_health()
                print_banner(agent, h)
                continue

            # Executa a pergunta do operador
            execute_query(agent, user_input)

        except (KeyboardInterrupt, EOFError):
            console.print("\n[dim]Sessão interrompida pelo operador. Até logo![/dim]")
            break


def main():
    """Ponto de entrada: aceita argumento direto ou inicia o modo interativo."""
    if len(sys.argv) > 1:
        # Modo direto via argumento (one-shot)
        query = " ".join(sys.argv[1:])
        agent = LocalNetOpsAgent()
        execute_query(agent, query)
    else:
        # Modo interativo
        interactive_loop()


if __name__ == "__main__":
    main()
