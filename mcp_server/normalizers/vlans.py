"""
mcp_server/normalizers/vlans.py
Normalizador canônico OpenConfig para VLANs de Rede (openconfig-vlan).
"""

from typing import List, Dict, Any
from datetime import datetime, timezone


def normalize_vlans(
    records: List[Dict[str, Any]],
    vendor: str,
    os_family: str,
    version: str,
    device_hostname: str
) -> Dict[str, Any]:
    """Normaliza registros de VLANs para o schema canônico OpenConfig."""
    vlans_list = []
    seen = set()

    for r in records:
        if not isinstance(r, dict):
            continue
        vlan_id_raw = r.get("vlan_id") or r.get("vlan") or r.get("id")
        if not vlan_id_raw:
            continue

        try:
            vlan_id = int(str(vlan_id_raw).strip())
        except (ValueError, TypeError):
            continue

        if vlan_id in seen:
            continue
        seen.add(vlan_id)

        name = str(r.get("name") or f"VLAN_{vlan_id}").strip()
        status = str(r.get("status") or "active").strip().lower()
        ports_raw = r.get("ports") or []
        if isinstance(ports_raw, str):
            ports = [p.strip() for p in ports_raw.split(",") if p.strip()]
        elif isinstance(ports_raw, list):
            ports = [str(p).strip() for p in ports_raw if str(p).strip()]
        else:
            ports = []

        vlans_list.append({
            "vlan_id": vlan_id,
            "name": name,
            "status": status,
            "ports": ports,
        })

    # Ordena por vlan_id
    vlans_list.sort(key=lambda x: x["vlan_id"])
    active_count = sum(1 for v in vlans_list if "act" in v["status"])

    return {
        "device": device_hostname,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total_vlans": len(vlans_list),
            "active_vlans": active_count,
        },
        "vlans": vlans_list,
    }
