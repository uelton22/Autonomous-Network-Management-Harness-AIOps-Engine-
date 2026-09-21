"""
mcp_server/normalizers/registry.py
Despachante Central de Normalização Canônica OpenConfig.
Conecta o resultado bruto do motor TTP aos normalizadores especializados
com fallback garantido para o Normalizador Genérico Declarativo.
"""

from typing import List, Dict, Any, Callable

from mcp_server.normalizers.device_info import normalize_device_info
from mcp_server.normalizers.interfaces import (
    normalize_interface_summary,
    normalize_interface_detail
)
from mcp_server.normalizers.link_aggregation import normalize_link_aggregation
from mcp_server.normalizers.bgp import normalize_bgp_summary
from mcp_server.normalizers.lldp import normalize_lldp_neighbors
from mcp_server.normalizers.users import normalize_system_users, normalize_user_sessions
from mcp_server.normalizers.ospf import normalize_ospf_neighbors
from mcp_server.normalizers.generic import GenericOpenConfigNormalizer


def normalize_records_pipeline(
    records: List[Dict[str, Any]],
    action: str,
    vendor: str,
    os_family: str,
    version: str,
    device_hostname: str
) -> Dict[str, Any]:
    """Despacha a normalização para a função especialista ou para o normalizador genérico."""
    if action in ("get_system_version", "get_hardware_model", "get_system_uptime"):
        return normalize_device_info(records, vendor, os_family, version, device_hostname)

    elif action == "get_interface_summary":
        return normalize_interface_summary(records, device_hostname)

    elif action == "get_interface_detail":
        return normalize_interface_detail(records, device_hostname)

    elif action == "get_link_aggregation":
        return normalize_link_aggregation(records, device_hostname)

    elif action == "get_bgp_summary":
        return normalize_bgp_summary(records, device_hostname)

    elif action == "get_lldp_neighbors":
        return normalize_lldp_neighbors(records, device_hostname)

    elif action == "get_system_users":
        return normalize_system_users(records, device_hostname)

    elif action == "get_active_sessions":
        return normalize_user_sessions(records, device_hostname)

    elif action == "get_ospf_neighbors":
        return normalize_ospf_neighbors(records, device_hostname)

    # Fallback Declarativo para novas ações
    return GenericOpenConfigNormalizer.normalize(action, records, device_hostname)
