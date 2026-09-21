"""
mcp_server/schemas/interfaces.py
Schema Canônico OpenConfig para Resumo e Detalhes de Interfaces de Rede.
Inclui categorização determinística e pré-calculada de tipos (100GE, XGE, GE, etc.).
"""

from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class InterfaceDetailItem(BaseModel):
    name: str = Field(description="Nome da interface física ou lógica (ex: 100GE3/0/0, 1/1/1)")
    admin_status: str = Field(description="UP, DOWN ou TESTING")
    oper_status: str = Field(description="UP, DOWN ou TESTING")
    canonical_name: Optional[str] = None
    description: Optional[str] = None
    speed_bps: Optional[int] = None
    mac_address: Optional[str] = None
    last_flapped: Optional[str] = None
    in_errors: Optional[int] = 0
    out_errors: Optional[int] = 0
    in_crc_errors: Optional[int] = 0
    in_discards: Optional[int] = 0


class InterfaceSummaryStats(BaseModel):
    total_interfaces: int = 0
    admin_up: int = 0
    admin_down: int = 0
    oper_up: int = 0
    oper_down: int = 0
    up_up: int = 0
    down_down: int = 0
    up_down_anomalies: int = 0
    by_type: Dict[str, int] = Field(default_factory=dict)


class InterfacesSchema(BaseModel):
    device: str
    summary: Optional[InterfaceSummaryStats] = None
    interfaces: List[InterfaceDetailItem]
    collected_at: Optional[str] = None
