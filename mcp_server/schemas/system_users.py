"""
mcp_server/schemas/system_users.py
Schema Canônico OpenConfig para Contas de Usuários do Sistema (openconfig-system/aaa).
"""

from typing import Optional, List
from pydantic import BaseModel, Field
from mcp_server.schemas.base import OpenConfigBaseSchema


class SystemUserItem(BaseModel):
    username: str = Field(description="Nome de usuário da conta de acesso")
    group: Optional[str] = Field(default="N/A", description="Grupo de permissão ou perfil (admin, config, audit)")
    role: Optional[str] = Field(default=None, description="Função canônica associada")
    authentication_type: Optional[str] = Field(default="local", description="Tipo de autenticação (local, radius, tacacs)")
    password_configured: Optional[bool] = Field(default=True, description="Indica se há credencial ou hash configurado")


class SystemUsersSummary(BaseModel):
    total_users: int = Field(default=0, description="Total de contas de usuários configuradas")


class SystemUsersSchema(OpenConfigBaseSchema):
    summary: Optional[SystemUsersSummary] = Field(default_factory=SystemUsersSummary)
    users: List[SystemUserItem] = Field(default_factory=list, description="Lista de usuários configurados")
