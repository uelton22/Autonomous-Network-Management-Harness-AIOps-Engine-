"""
mcp_server/normalizers/interfaces.py
Normalizador canônico OpenConfig para resumo de interfaces de rede (openconfig-interfaces).
"""

from typing import List, Dict, Any
from datetime import datetime, timezone


def normalize_interfaces_summary(
    records: List[Dict[str, Any]],
    vendor: str,
    os_family: str,
    version: str,
    device_hostname: str
) -> Dict[str, Any]:
    """Normaliza registros de interfaces para o schema canônico OpenConfig."""
    interfaces_list = []
    seen = set()

    for r in records:
        if not isinstance(r, dict):
            continue
        name = r.get("name") or r.get("interface")
        if not name:
            continue

        # Ignora cabeçalhos tabulares residuais
        name_clean = name.strip()
        if name_clean.lower() in ("interface", "id", "port", "name", "ifname"):
            continue

        if name_clean in seen:
            continue
        seen.add(name_clean)

        raw_admin = str(r.get("admin_status") or r.get("status") or "UP").upper()
        if "DOWN" in raw_admin or "ADMIN" in raw_admin or "SHUT" in raw_admin or "DISABLE" in raw_admin:
            admin_status = "DOWN"
        else:
            admin_status = "UP"

        raw_oper = str(r.get("oper_status") or r.get("protocol") or "DOWN").upper()
        if "UP" in raw_oper:
            oper_status = "UP"
        else:
            oper_status = "DOWN"

        ip_raw = r.get("ip_address") or r.get("ip") or "unassigned"
        if ip_raw.lower() in ("unassigned", "--", "none", "ip-address"):
            ip_raw = "unassigned"

        interfaces_list.append({
            "name": name_clean,
            "ip_address": ip_raw,
            "admin_status": admin_status,
            "oper_status": oper_status,
            "method": r.get("method"),
            "description": r.get("description"),
        })

    up_count = sum(1 for iface in interfaces_list if iface["oper_status"] == "UP")
    down_count = sum(1 for iface in interfaces_list if iface["oper_status"] == "DOWN")

    return {
        "device": device_hostname,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total_interfaces": len(interfaces_list),
            "up_interfaces": up_count,
            "down_interfaces": down_count,
        },
        "interfaces": interfaces_list,
    }
