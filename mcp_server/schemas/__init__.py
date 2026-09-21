"""
mcp_server/schemas
Módulo de Schemas Canônicos OpenConfig (Tier 3: Tipagem e Validação Pydantic).
"""

from mcp_server.schemas.base import OpenConfigBaseSchema
from mcp_server.schemas.device_info import DeviceInfoSchema
from mcp_server.schemas.registry import ACTION_SCHEMA_MAP, get_schema_for_action, get_json_schema_definition

__all__ = [
    "OpenConfigBaseSchema",
    "DeviceInfoSchema",
    "ACTION_SCHEMA_MAP",
    "get_schema_for_action",
    "get_json_schema_definition",
]
