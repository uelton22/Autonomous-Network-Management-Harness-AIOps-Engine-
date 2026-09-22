"""
agent/runner.py
Orquestrador autônomo do Agente de Operações de Rede para LLMs Locais (Ollama, vLLM, etc.).
Gerencia o loop de Tool Calling, injeção do System Prompt e despacho determinístico.
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, List, Optional, Callable, Generator

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

from agent.tools import NETOPS_TOOLS, dispatch_tool


def get_system_prompt() -> str:
    """Carrega as regras mestre do AGENTS.md com ênfase em isolamento e segurança."""
    agents_file = Path("AGENTS.md")
    base_instructions = """Você é o Agente Autônomo de Operações de Rede (AIOps Agent), especialista em infraestrutura multi-vendor (Datacom DmOS, Huawei VRP e Cisco IOS-XE).

REGRAS MANDATÓRIAS INEGOCIÁVEIS:
1. ISOLAMENTO ESTRITO DO ALVO: Conecte-se e execute ações ÚNICA E EXCLUSIVAMENTE no IP ou hostname informado pelo operador. Nunca faça testes, probes ou consultas em outros hosts.
2. ZERO MOCKS: O ambiente é 100% real. Não existem mocks.
3. PRIVILÉGIO READ POR PADRÃO: Sempre utilize privilege_level="read" para inspeções e coletas. Se uma alteração for pedida, exija privilégio "editor" ou "full" com justificativa técnica clara em português.
4. ZERO LEITURA MANUAL DE .RAW: Toda informação que você apresentar ao operador DEVE derivar exclusivamente dos dados estruturados em JSON normalizados pelas ferramentas canônicas (run_canonical_action, run_adhoc_action ou discover_device).
5. COFRE DE CREDENCIAIS & PERFIS (VAULT): O sistema gerencia perfis de conexão SSH via Vault (ex: 'default', 'zabbix', 'admin', 'noc_core').
   - Se o operador indicar um perfil (ex: "usando perfil zabbix" ou "com usuário admin"), passe o parâmetro credential_profile="<nome>" na chamada das ferramentas.
   - Se o operador perguntar quais perfis existem ou pedir para escolher com qual perfil conectar, chame a ferramenta list_credential_profiles() e apresente a lista em formato de tabela Markdown (mostrando Nome, Usuário, Porta e Descrição). NUNCA invente senhas.
   - Se nenhum perfil for especificado, omita credential_profile ou passe vazio para que o Vault utilize o perfil padrão automaticamente.
6. FORMATO DE RESPOSTA: Apresente as respostas com tabelas claras em Markdown, destacando Fabricante, Modelo, Versão e dados coletados de forma executiva e profissional.
"""
    if agents_file.exists():
        try:
            full_content = agents_file.read_text(encoding="utf-8")
            return f"{base_instructions}\n\n--- DIRETRIZES COMPLETAS DO AGENTS.MD ---\n{full_content}"
        except Exception:
            return base_instructions
    return base_instructions


class LocalNetOpsAgent:
    """Orquestrador do Agente de Rede conectado a uma LLM Local."""

    def __init__(
        self,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
        api_key: Optional[str] = None,
        temperature: float = 0.1,
        active_profile: Optional[str] = None
    ):
        self.base_url = base_url or os.getenv("LLM_BASE_URL", "http://localhost:11434/v1")
        self.model = model or os.getenv("LLM_MODEL", "qwen2.5:14b")
        self.api_key = api_key or os.getenv("LLM_API_KEY", "ollama")
        self.temperature = float(os.getenv("LLM_TEMPERATURE", str(temperature)))
        self.active_profile = active_profile or os.getenv("NETOPS_DEFAULT_PROFILE", None)
        
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key
        )
        self.system_prompt = get_system_prompt()
        self.history: List[Dict[str, Any]] = [
            {"role": "system", "content": self.system_prompt}
        ]

    def check_health(self) -> Dict[str, Any]:
        """Verifica a conectividade com o servidor da LLM local e retorna status e modelos disponíveis."""
        try:
            models_res = self.client.models.list()
            available_models = [m.id for m in models_res.data]
            model_found = self.model in available_models or any(self.model in m for m in available_models)
            return {
                "status": "connected",
                "base_url": self.base_url,
                "configured_model": self.model,
                "model_ready": model_found,
                "available_models": available_models
            }
        except Exception as e:
            return {
                "status": "unreachable",
                "base_url": self.base_url,
                "configured_model": self.model,
                "error": str(e)
            }

    def clear_history(self):
        """Limpa o histórico da sessão de chat preservando o prompt de sistema."""
        self.history = [
            {"role": "system", "content": self.system_prompt}
        ]

    def chat(
        self,
        user_input: str,
        on_tool_start: Optional[Callable[[str, Dict[str, Any]], None]] = None,
        on_tool_finish: Optional[Callable[[str, Dict[str, Any]], None]] = None
    ) -> str:
        """
        Executa o ciclo completo de raciocínio do Agente com suporte a Tool Calling recursivo.
        """
        self.history.append({"role": "user", "content": user_input})
        
        max_turns = 10
        turn = 0

        while turn < max_turns:
            turn += 1
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
                tools=NETOPS_TOOLS,
                tool_choice="auto",
                temperature=self.temperature
            )
            
            choice = response.choices[0]
            msg = choice.message
            
            # Se a LLM solicitou chamadas de ferramenta
            if msg.tool_calls:
                # Serializa mensagem da LLM no formato aceito pelo histórico
                tool_calls_dict = [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    }
                    for tc in msg.tool_calls
                ]
                
                self.history.append({
                    "role": "assistant",
                    "content": msg.content or "",
                    "tool_calls": tool_calls_dict
                })
                
                # Executa cada tool_call solicitada
                for tc in msg.tool_calls:
                    fn_name = tc.function.name
                    try:
                        args = json.loads(tc.function.arguments)
                    except Exception:
                        args = {}
                    
                    if on_tool_start:
                        on_tool_start(fn_name, args)
                        
                    # Se houver um perfil ativo na sessão do operador e não tiver sido especificado
                    if self.active_profile and "credential_profile" not in args and fn_name != "list_credential_profiles" and fn_name != "search_command_reference":
                        args["credential_profile"] = self.active_profile

                    raw_result = dispatch_tool(fn_name, args)
                    
                    try:
                        parsed_res = json.loads(raw_result)
                    except Exception:
                        parsed_res = {"raw": raw_result}
                        
                    if on_tool_finish:
                        on_tool_finish(fn_name, parsed_res)
                        
                    self.history.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "name": fn_name,
                        "content": raw_result
                    })
                
                # Continua o loop para a LLM processar os dados normalizados retornados
                continue
            
            # Resposta textual final
            final_text = msg.content or "Nenhuma resposta textual gerada."
            self.history.append({"role": "assistant", "content": final_text})
            return final_text
            
        return "Limite de iterações de ferramentas atingido sem conclusão."
