"""
mcp_server/schemas/lldp.py
Schema Canônico OpenConfig para Vizinhos LLDP (Link Layer Discovery Protocol).
"""

from typing import Optional, List
from pydantic import BaseModel, Field


class LLDPNeighborItem(BaseModel):
    local_interface: str = Field(description="Interface local do switch")
    neighbor_id: Optional[str] = None
    chassis_subtype: Optional[str] = None
    chassis_id: Optional[str] = None
    system_name: Optional[str] = None
    system_description: Optional[str] = None
    port_subtype: Optional[str] = None
    port_id: Optional[str] = None
    port_description: Optional[str] = None
    management_address: Optional[str] = None


class LLDPNeighborsSchema(BaseModel):
    device: str
    neighbors: List[LLDPNeighborItem] = Field(default_factory=list)
    collected_at: Optional[str] = None
