"""
mcp_server/schemas/vlans.py
Schema Canônico OpenConfig para VLANs de Rede (openconfig-vlan).
"""

from typing import List, Optional
from pydantic import BaseModel, Field

from mcp_server.schemas.base import OpenConfigBaseSchema


class VlanItem(BaseModel):
    """Representa uma VLAN individual configurada no equipamento."""
    vlan_id: int = Field(description="ID numérico da VLAN")
    name: str = Field(description="Nome descritivo da VLAN")
    status: str = Field(default="active", description="Status da VLAN (active, suspended, etc.)")
    ports: List[str] = Field(default_factory=list, description="Lista de portas vinculadas")


class VlansSummary(BaseModel):
    """Métricas agregadas sobre VLANs."""
    total_vlans: int = Field(default=0, description="Total de VLANs cadastradas")
    active_vlans: int = Field(default=0, description="Total de VLANs ativas")


class VlansSchema(OpenConfigBaseSchema):
    """Modelo canônico para lista e detalhes de VLANs."""
    vlans: List[VlanItem] = Field(default_factory=list, description="Lista de VLANs")
    summary: Optional[VlansSummary] = Field(default=None, description="Resumo quantitativo de VLANs")
