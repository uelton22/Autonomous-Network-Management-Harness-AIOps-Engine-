"""
mcp_server/schemas/ospf.py
Schema Canônico OpenConfig para Vizinhos e Adjacências OSPF (openconfig-ospfv2).
"""

from typing import Optional, List
from pydantic import BaseModel, Field


class OspfNeighborItem(BaseModel):
    router_id: str = Field(description="Router ID do vizinho OSPF")
    state: str = Field(description="Estado da adjacência (Full, 2-Way, Init, Down, etc.)")
    local_interface: str = Field(description="Interface local conectada")
    area: Optional[str] = Field(default="0.0.0.0", description="Área OSPF")
    address: Optional[str] = Field(default=None, description="Endereço IP da interface do vizinho")
    priority: Optional[int] = Field(default=None, description="Prioridade OSPF")
    dr_state: Optional[str] = Field(default=None, description="Papel DR/BDR (DR, BDR, DROther, None)")
    dead_time: Optional[str] = Field(default=None, description="Dead timer restante")
    uptime: Optional[str] = Field(default=None, description="Tempo ativo da adjacência")


class OspfNeighborsSummary(BaseModel):
    total_neighbors: int = 0
    full_neighbors: int = 0


class OspfNeighborsSchema(BaseModel):
    device: str
    collected_at: Optional[str] = None
    summary: Optional[OspfNeighborsSummary] = None
    neighbors: List[OspfNeighborItem] = Field(default_factory=list)
