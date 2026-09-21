"""
mcp_server/normalizers/lldp.py
Normalizador canônico OpenConfig para descoberta de vizinhos LLDP.
"""

from typing import List, Dict, Any


def normalize_lldp_neighbors(
    records: List[Dict[str, Any]],
    device_hostname: str
) -> Dict[str, Any]:
    neighbors = []
    for r in records:
        loc_if = (r.get("local_interface") or "").strip()
        if not loc_if or loc_if in ("LOCAL", "LOCAL INTERFACE", "Interface", "Name", "ID", "Copyright", "VRP", "HUAWEI") or loc_if.startswith("-"):
            continue
        neighbors.append({
            "local_interface": loc_if,
            "neighbor_id": r.get("neighbor_id"),
            "chassis_subtype": r.get("chassis_subtype"),
            "chassis_id": r.get("chassis_id"),
            "system_name": r.get("system_name"),
            "system_description": r.get("system_description"),
            "port_subtype": r.get("port_subtype"),
            "port_id": r.get("port_id"),
            "port_description": r.get("port_description"),
            "management_address": r.get("management_address"),
        })

    return {
        "device": device_hostname,
        "neighbors": neighbors
    }
