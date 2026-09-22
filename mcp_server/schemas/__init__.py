"""
mcp_server/schemas
Pacote de Schemas Pydantic OpenConfig para Validação Estrita (Tier 3).
"""

from mcp_server.schemas.base import OpenConfigBaseSchema
from mcp_server.schemas.device_info import DeviceInfoSchema
from mcp_server.schemas.system_users import SystemUsersSchema
from mcp_server.schemas.registry import (
    ACTION_SCHEMA_MAP,
    get_schema_for_action,
    get_json_schema_definition,
)

__all__ = [
    "OpenConfigBaseSchema",
    "DeviceInfoSchema",
    "SystemUsersSchema",
    "ACTION_SCHEMA_MAP",
    "get_schema_for_action",
    "get_json_schema_definition",
]
