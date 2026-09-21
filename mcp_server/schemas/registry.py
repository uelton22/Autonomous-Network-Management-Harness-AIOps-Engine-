"""
mcp_server/schemas/registry.py
Registro Central de Schemas Pydantic OpenConfig para validação em tempo de execução.
Permite mapear ações canônicas aos seus respectivos modelos tipados.
"""

from typing import Dict, Type, Optional, Any
from pathlib import Path
import json
from pydantic import BaseModel

from mcp_server.schemas.device_info import DeviceInfoSchema
from mcp_server.schemas.system_users import SystemUsersSchema
from mcp_server.schemas.user_sessions import UserSessionsSchema


ACTION_SCHEMA_MAP: Dict[str, Type[BaseModel]] = {
    "get_system_version": DeviceInfoSchema,
    "get_hardware_model": DeviceInfoSchema,
    "get_system_uptime": DeviceInfoSchema,
    "get_system_users": SystemUsersSchema,
    "get_active_sessions": UserSessionsSchema,
}


def get_schema_for_action(action: str) -> Optional[Type[BaseModel]]:
    """Retorna a classe do modelo Pydantic para uma ação canônica, se registrada."""
    return ACTION_SCHEMA_MAP.get(action)


def get_json_schema_definition(schema_relative_path: str) -> Optional[Dict[str, Any]]:
    """Carrega o arquivo JSON Schema do diretório registry/schemas/ para validações declarativas."""
    try:
        p = Path(schema_relative_path)
        if not p.is_absolute():
            p = Path(__file__).resolve().parent.parent.parent / schema_relative_path
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        pass
    return None
