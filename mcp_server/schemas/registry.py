"""
mcp_server/schemas/registry.py
Registro Central de Schemas Canônicos OpenConfig.
Mapeia ações canônicas aos respectivos modelos Pydantic e carrega dinamicamente
definições adicionais de registry/schemas/.
"""

import json
from pathlib import Path
from typing import Dict, Type, Optional
from pydantic import BaseModel

from mcp_server.schemas.device_info import DeviceInfoSchema
from mcp_server.schemas.interfaces import InterfacesSchema, InterfaceDetailItem
from mcp_server.schemas.link_aggregation import LinkAggregationSchema
from mcp_server.schemas.bgp import BgpSummarySchema
from mcp_server.schemas.lldp import LLDPNeighborsSchema
from mcp_server.schemas.system_users import SystemUsersSchema
from mcp_server.schemas.user_sessions import UserSessionsSchema
from mcp_server.schemas.ospf import OspfNeighborsSchema


ACTION_SCHEMA_MAP: Dict[str, Type[BaseModel]] = {
    "get_system_version": DeviceInfoSchema,
    "get_hardware_model": DeviceInfoSchema,
    "get_system_uptime": DeviceInfoSchema,
    "get_interface_summary": InterfacesSchema,
    "get_interface_detail": InterfaceDetailItem,
    "get_bgp_summary": BgpSummarySchema,
    "get_lldp_neighbors": LLDPNeighborsSchema,
    "get_link_aggregation": LinkAggregationSchema,
    "get_system_users": SystemUsersSchema,
    "get_active_sessions": UserSessionsSchema,
    "get_ospf_neighbors": OspfNeighborsSchema,
}


def get_schema_for_action(action: str) -> Optional[Type[BaseModel]]:
    """Retorna o modelo Pydantic associado à ação canônica."""
    return ACTION_SCHEMA_MAP.get(action)


def get_json_schema_definition(action: str, schemas_dir: str = "registry/schemas") -> Optional[Dict]:
    """Carrega o JSON Schema canônico em disco para a ação informada."""
    s_dir = Path(schemas_dir)
    # 1. Busca por nome exato da ação
    direct_file = s_dir / f"{action}.json"
    if direct_file.exists():
        return json.loads(direct_file.read_text(encoding="utf-8"))

    # 2. Busca por sufixos comuns
    normalized_name = action.replace("get_", "").replace("check_", "")
    suffix_file = s_dir / f"{normalized_name}.json"
    if suffix_file.exists():
        return json.loads(suffix_file.read_text(encoding="utf-8"))

    return None
