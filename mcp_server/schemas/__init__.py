"""
mcp_server/schemas
Módulo de Schemas Canônicos OpenConfig unificados para operações de rede multi-vendor.
"""

from mcp_server.schemas.base import OpenConfigBaseSchema
from mcp_server.schemas.device_info import DeviceInfoSchema
from mcp_server.schemas.interfaces import InterfacesSchema, InterfaceDetailItem, InterfaceSummaryStats
from mcp_server.schemas.link_aggregation import LinkAggregationSchema, LagItem, LagMemberItem, LagSummaryStats
from mcp_server.schemas.bgp import BgpSummarySchema, BgpPeerItem
from mcp_server.schemas.lldp import LLDPNeighborsSchema, LLDPNeighborItem
from mcp_server.schemas.system_users import SystemUsersSchema, SystemUserItem, SystemUsersSummary
from mcp_server.schemas.user_sessions import UserSessionsSchema, UserSessionItem, UserSessionsSummary
from mcp_server.schemas.registry import ACTION_SCHEMA_MAP, get_schema_for_action, get_json_schema_definition

__all__ = [
    "OpenConfigBaseSchema",
    "DeviceInfoSchema",
    "InterfacesSchema",
    "InterfaceDetailItem",
    "InterfaceSummaryStats",
    "LinkAggregationSchema",
    "LagItem",
    "LagMemberItem",
    "LagSummaryStats",
    "BgpSummarySchema",
    "BgpPeerItem",
    "LLDPNeighborsSchema",
    "LLDPNeighborItem",
    "SystemUsersSchema",
    "SystemUserItem",
    "SystemUsersSummary",
    "UserSessionsSchema",
    "UserSessionItem",
    "UserSessionsSummary",
    "ACTION_SCHEMA_MAP",
    "get_schema_for_action",
    "get_json_schema_definition",
]
