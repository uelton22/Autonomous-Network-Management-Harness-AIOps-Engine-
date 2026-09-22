"""
agent/tools.py
Mapeamento de ferramentas do MCP Server para o formato OpenAPI/OpenAI Function Calling,
permitindo que LLMs Locais (Ollama, vLLM, LM Studio) acionem as ferramentas diretamente.
"""

import json
from typing import Dict, Any, List

from mcp_server.server import (
    discover_device,
    run_canonical_action,
    run_adhoc_action,
    search_command_reference,
    run_workflow_dag,
    execute_command,
    list_credential_profiles
)

# Esquemas de Function Calling compatíveis com OpenAI / Ollama / vLLM
NETOPS_TOOLS: List[Dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "list_credential_profiles",
            "description": "Lista todos os perfis de credenciais SSH disponíveis no Vault (ex: zabbix, admin, noc_core) com nomes de usuário e portas, com senhas estritamente mascaradas.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "discover_device",
            "description": "Identifica de forma progressiva (Zero-Knowledge L1->L2->L3) o fabricante, modelo de hardware e versão exata do sistema operacional do equipamento informado.",
            "parameters": {
                "type": "object",
                "properties": {
                    "host": {
                        "type": "string",
                        "description": "Endereço IP ou hostname do equipamento alvo (ex: '10.0.0.1')"
                    },
                    "credential_profile": {
                        "type": "string",
                        "description": "Nome do perfil de credencial no Vault (ex: 'zabbix', 'admin', 'noc_core'). Opcional; se omitido, usa o perfil padrão ou inferido."
                    }
                },
                "required": ["host"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_canonical_action",
            "description": "Executa uma ação canônica catalogada com resolução de versão de SO em 5 níveis, parsing determinístico via TTP e validação estrita no modelo OpenConfig.",
            "parameters": {
                "type": "object",
                "properties": {
                    "host": {
                        "type": "string",
                        "description": "Endereço IP ou hostname do equipamento alvo"
                    },
                    "action": {
                        "type": "string",
                        "description": "Nome da ação canônica cadastrada em actions.yaml",
                        "enum": [
                            "get_system_version",
                            "get_hardware_model",
                            "get_system_uptime",
                            "get_system_users",
                            "get_active_sessions"
                        ]
                    },
                    "privilege_level": {
                        "type": "string",
                        "description": "Nível de privilégio de segurança exigido (padrão: 'read')",
                        "enum": ["read", "editor", "full"],
                        "default": "read"
                    },
                    "interface_name": {
                        "type": "string",
                        "description": "Identificador da interface se a ação exigir parâmetro (ex: '1/1/1')"
                    },
                    "force_refresh": {
                        "type": "boolean",
                        "description": "Se True, ignora o cache local de .raw de curta duração e força nova conexão SSH",
                        "default": False
                    },
                    "credential_profile": {
                        "type": "string",
                        "description": "Nome do perfil de credencial no Vault (ex: 'zabbix', 'admin', 'noc_core'). Opcional; se omitido, usa o perfil padrão ou inferido."
                    }
                },
                "required": ["host", "action"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_command_reference",
            "description": "Pesquisa na documentação e guias oficiais dos fabricantes (command_reference/) sintaxes exatas, parâmetros e descrições para evitar alucinações de comandos.",
            "parameters": {
                "type": "object",
                "properties": {
                    "vendor": {
                        "type": "string",
                        "description": "Fabricante do equipamento",
                        "enum": ["datacom", "huawei", "cisco"]
                    },
                    "query": {
                        "type": "string",
                        "description": "Termo de busca ou sintaxe desejada (ex: 'display eth-trunk', 'show users', 'bgp')"
                    },
                    "read_only": {
                        "type": "boolean",
                        "description": "Se True, restringe apenas a comandos de inspeção e leitura (show / display)",
                        "default": True
                    },
                    "category": {
                        "type": "string",
                        "description": "Categoria opcional (ex: 'interface', 'management', 'routing')"
                    },
                    "version": {
                        "type": "string",
                        "description": "Versão específica de SO se aplicável (ex: 'v200', 'V200R011C10', 'v800')"
                    }
                },
                "required": ["vendor", "query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_adhoc_action",
            "description": "Executa comando ad-hoc no equipamento e obriga a normalização determinística via TTP Hybrid Engine, persistindo o template e o JSON em disco.",
            "parameters": {
                "type": "object",
                "properties": {
                    "host": {
                        "type": "string",
                        "description": "Endereço IP ou hostname do equipamento alvo"
                    },
                    "command": {
                        "type": "string",
                        "description": "Comando exato de CLI a ser executado no switch/roteador"
                    },
                    "action_name": {
                        "type": "string",
                        "description": "Identificador semântico em snake_case para a ação (ex: 'get_lacp_status')"
                    },
                    "privilege_level": {
                        "type": "string",
                        "description": "Nível de privilégio de segurança (padrão: 'read')",
                        "enum": ["read", "editor", "full"],
                        "default": "read"
                    },
                    "force_refresh": {
                        "type": "boolean",
                        "description": "Se True, força nova conexão SSH ignorando o cache local",
                        "default": False
                    },
                    "credential_profile": {
                        "type": "string",
                        "description": "Nome do perfil de credencial no Vault (ex: 'zabbix', 'admin', 'noc_core'). Opcional; se omitido, usa o perfil padrão ou inferido."
                    }
                },
                "required": ["host", "command", "action_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_workflow_dag",
            "description": "Executa workflow orquestrado em DAG com filtros determinísticos em código local (sem consumir tokens da LLM) e agregação em modelo canônico OpenConfig.",
            "parameters": {
                "type": "object",
                "properties": {
                    "host": {
                        "type": "string",
                        "description": "Endereço IP ou hostname do equipamento alvo"
                    },
                    "workflow_name": {
                        "type": "string",
                        "description": "Nome do workflow registrado em actions.yaml (ex: 'diagnose_down_interfaces', 'diagnose_bgp_flapping')",
                        "default": "diagnose_down_interfaces"
                    },
                    "privilege_level": {
                        "type": "string",
                        "description": "Nível de privilégio exigido",
                        "enum": ["read", "editor", "full"],
                        "default": "read"
                    },
                    "credential_profile": {
                        "type": "string",
                        "description": "Nome do perfil de credencial no Vault (ex: 'zabbix', 'admin', 'noc_core'). Opcional; se omitido, usa o perfil padrão ou inferido."
                    }
                },
                "required": ["host", "workflow_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "execute_command",
            "description": "[USO RESTRITO PARA PROBES]: Executa comando de baixo nível no equipamento e salva o .raw em disco. Não use para coletas comuns pois o raw não é retornado.",
            "parameters": {
                "type": "object",
                "properties": {
                    "host": {
                        "type": "string",
                        "description": "Endereço IP ou hostname do equipamento alvo"
                    },
                    "command": {
                        "type": "string",
                        "description": "Comando exato a ser executado"
                    },
                    "platform_type": {
                        "type": "string",
                        "description": "Família de plataforma (datacom_dmos | huawei_vrp | cisco_iosxe | generic)",
                        "default": "generic"
                    },
                    "privilege_level": {
                        "type": "string",
                        "description": "Nível de privilégio (read | editor | full)",
                        "default": "read"
                    },
                    "credential_profile": {
                        "type": "string",
                        "description": "Nome do perfil de credencial no Vault (ex: 'zabbix', 'admin', 'noc_core'). Opcional; se omitido, usa o perfil padrão ou inferido."
                    }
                },
                "required": ["host", "command"]
            }
        }
    }
]

TOOL_DISPATCHER = {
    "list_credential_profiles": list_credential_profiles,
    "discover_device": discover_device,
    "run_canonical_action": run_canonical_action,
    "run_adhoc_action": run_adhoc_action,
    "search_command_reference": search_command_reference,
    "run_workflow_dag": run_workflow_dag,
    "execute_command": execute_command
}


def dispatch_tool(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Despacha a chamada da ferramenta solicitada pela LLM e retorna o resultado em string JSON."""
    if tool_name not in TOOL_DISPATCHER:
        return json.dumps({
            "status": "error",
            "error": f"Ferramenta desconhecida: '{tool_name}'"
        })
    func = TOOL_DISPATCHER[tool_name]
    try:
        return func(**arguments)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "tool": tool_name,
            "error": str(e)
        })
