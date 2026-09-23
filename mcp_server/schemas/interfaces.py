"""
mcp_server/schemas/interfaces.py
Schema Canônico OpenConfig para Interfaces de Rede (openconfig-interfaces).
"""

from typing import List, Optional
from pydantic import BaseModel, Field

from mcp_server.schemas.base import OpenConfigBaseSchema


class InterfaceItem(BaseModel):
    """Representa uma interface de rede e seus atributos operacionais."""
    name: str = Field(description="Nome da interface (ex: GigabitEthernet1/0/1)")
    ip_address: Optional[str] = Field(default="unassigned", description="Endereço IP configurado ou unassigned")
    admin_status: str = Field(default="UP", description="Status administrativo (UP ou DOWN)")
    oper_status: str = Field(default="DOWN", description="Status operacional (UP ou DOWN)")
    method: Optional[str] = Field(default=None, description="Método de configuração do IP")
    description: Optional[str] = Field(default=None, description="Descrição configurada na interface")


class InterfacesSummary(BaseModel):
    """Resumo estatístico de contagem de interfaces."""
    total_interfaces: int = Field(default=0, description="Total de interfaces mapeadas")
    up_interfaces: int = Field(default=0, description="Interfaces operacionais (UP)")
    down_interfaces: int = Field(default=0, description="Interfaces caídas ou desabilitadas (DOWN)")


class InterfacesSchema(OpenConfigBaseSchema):
    """Modelo canônico unificado para listas e resumos de interfaces."""
    interfaces: List[InterfaceItem] = Field(default_factory=list, description="Lista de interfaces")
    summary: Optional[InterfacesSummary] = Field(default=None, description="Resumo quantitativo")
