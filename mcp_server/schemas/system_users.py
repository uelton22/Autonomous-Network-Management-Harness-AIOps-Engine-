"""
mcp_server/schemas/system_users.py
Schema Canônico OpenConfig para Contas de Usuários Locais (openconfig-system:system/aaa).
"""

from typing import List, Optional
from pydantic import BaseModel, Field

from mcp_server.schemas.base import OpenConfigBaseSchema


class SystemUserItem(BaseModel):
    """Representa um usuário local configurado no equipamento."""
    username: str = Field(description="Nome de usuário da conta")
    role: Optional[str] = Field(default="admin", description="Papel ou perfil textual (admin, operator, etc.)")
    privilege_level: Optional[int] = Field(default=None, description="Nível numérico de privilégio do usuário")
    group: Optional[str] = Field(default=None, description="Grupo ou perfil associado")
    authentication_type: Optional[str] = Field(default=None, description="Algoritmo de hash ou método de autenticação")
    password_configured: bool = Field(default=True, description="Indica se existe senha ou hash configurado")


class UsersSummary(BaseModel):
    """Métricas agregadas sobre usuários do sistema."""
    total_users: int = Field(default=0, description="Total de usuários locais configurados")
    admin_users: int = Field(default=0, description="Total de usuários com privilégios administrativos")


class SystemUsersSchema(OpenConfigBaseSchema):
    """Modelo canônico para lista de usuários locais e privilégios."""
    users: List[SystemUserItem] = Field(default_factory=list, description="Lista de usuários locais")
    summary: Optional[UsersSummary] = Field(default=None, description="Métricas de resumo de usuários")
