"""
mcp_server/normalizers/registry.py
Despachante Central de Normalização Canônica OpenConfig.
Conecta o resultado bruto do motor TTP aos normalizadores especializados
com fallback garantido para o Normalizador Genérico Declarativo.
"""

from typing import List, Dict, Any

from mcp_server.normalizers.device_info import normalize_device_info
from mcp_server.normalizers.users import normalize_system_users
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

    if action == "get_system_users":
        return normalize_system_users(records, vendor, os_family, version, device_hostname)

    # Fallback Declarativo para novas ações dinâmicas
    return GenericOpenConfigNormalizer.normalize(action, records, device_hostname)
