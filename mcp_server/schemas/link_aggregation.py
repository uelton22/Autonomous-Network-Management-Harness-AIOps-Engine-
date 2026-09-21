"""
mcp_server/schemas/link_aggregation.py
Schema Canônico OpenConfig Unificado para Agregações de Enlace (LAG / LACP / Eth-Trunk / Port-Channel).
Agnóstico de fabricante: atende integralmente Datacom DmOS, Huawei VRP e Cisco IOS/IOS-XE.
"""

from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class LagMemberItem(BaseModel):
    interface: str = Field(description="Nome da interface física membro (ex: 1/1/5, 100GE3/0/1, TenGigabitEthernet1/0/1)")
    oper_status: str = Field(default="UNKNOWN", description="Status operacional da porta física (UP / DOWN)")
    aggregation_status: str = Field(default="active", description="Status na agregação (active, standby, suspended, down)")
    lacp_status: Optional[str] = Field(default=None, description="Estado do protocolo LACP (Selected, Standby, etc.)")
    port_priority: Optional[int] = Field(default=None, description="Prioridade LACP da porta")
    weight: Optional[int] = Field(default=None, description="Peso/Weight operacional no trunk (Huawei/Datacom)")


class LagItem(BaseModel):
    lag_id: str = Field(description="Identificador numérico ou alfanumérico da agregação (ex: '1', '29')")
    name: str = Field(description="Nome canônico ou de interface (ex: 'lag 1', 'Eth-Trunk29', 'Port-channel1')")
    oper_status: str = Field(default="UNKNOWN", description="Status operacional da agregação (UP / DOWN)")
    admin_status: Optional[str] = Field(default="UP", description="Status administrativo da agregação")
    mode: Optional[str] = Field(default="UNKNOWN", description="Modo operacional (LACP_ACTIVE, LACP_PASSIVE, STATIC)")
    min_links: Optional[int] = Field(default=1, description="Mínimo de portas ativas requeridas para manter o enlace UP")
    description: Optional[str] = Field(default=None, description="Descrição configurada no trunk")
    members: List[LagMemberItem] = Field(default_factory=list, description="Lista de portas físicas participantes")


class LagSummaryStats(BaseModel):
    total_aggregations: int = 0
    active_aggregations: int = 0
    down_aggregations: int = 0
    total_members: int = 0
    active_members: int = 0


class LinkAggregationSchema(BaseModel):
    device: str = Field(description="Hostname ou IP do equipamento")
    summary: Optional[LagSummaryStats] = None
    link_aggregations: List[LagItem] = Field(default_factory=list, description="Agregações de enlace configuradas")
    collected_at: Optional[str] = None
