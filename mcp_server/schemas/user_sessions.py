"""
mcp_server/schemas/user_sessions.py
Schema Canônico OpenConfig para Sessões de Usuários Ativas (openconfig-system).
"""

from typing import Optional, List
from pydantic import BaseModel, Field
from mcp_server.schemas.base import OpenConfigBaseSchema


class UserSessionItem(BaseModel):
    session_id: str = Field(description="Identificador único da sessão ou tty/vty")
    username: str = Field(description="Nome do usuário autenticado")
    context: Optional[str] = Field(default="cli", description="Contexto de acesso (cli, snmp, console, etc.)")
    source_ip: Optional[str] = Field(default="local", description="Endereço IP de origem")
    protocol: Optional[str] = Field(default="ssh", description="Protocolo da sessão (ssh, udp, telnet)")
    login_time: Optional[str] = Field(default=None, description="Horário ou data de início")
    mode: Optional[str] = Field(default="operational", description="Modo operacional da sessão")
    is_current: Optional[bool] = Field(default=False, description="Indica se é a sessão atual")


class UserSessionsSummary(BaseModel):
    total_sessions: int = Field(default=0, description="Total de sessões ativas")


class UserSessionsSchema(OpenConfigBaseSchema):
    summary: Optional[UserSessionsSummary] = Field(default_factory=UserSessionsSummary)
    sessions: List[UserSessionItem] = Field(default_factory=list, description="Lista de sessões ativas")
