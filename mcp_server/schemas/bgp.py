"""
mcp_server/schemas/bgp.py
Schema Canônico OpenConfig para Sessões e Resumo BGP.
"""

from typing import Optional, List
from pydantic import BaseModel, Field


class BgpPeerItem(BaseModel):
    peer_ip: str = Field(description="Endereço IP do vizinho BGP")
    remote_as: int = Field(description="AS remoto")
    state: str = Field(description="Estado da sessão (Established, Idle, Active, Connect)")
    peer_group: Optional[str] = None
    uptime: Optional[str] = None
    prefixes_received: Optional[int] = 0
    prefixes_accepted: Optional[int] = 0


class BgpSummarySchema(BaseModel):
    device: str
    local_as: Optional[int] = None
    router_id: Optional[str] = None
    peers: List[BgpPeerItem] = Field(default_factory=list)
    collected_at: Optional[str] = None
