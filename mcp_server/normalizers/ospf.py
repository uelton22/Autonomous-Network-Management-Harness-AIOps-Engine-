"""
mcp_server/normalizers/ospf.py
Normalizador canônico OpenConfig para vizinhos e adjacências OSPF (openconfig-ospfv2).
"""

import time
from typing import List, Dict, Any


def normalize_ospf_neighbors(
    records: List[Dict[str, Any]],
    device_hostname: str
) -> Dict[str, Any]:
    neighbors = []
    seen = set()

    for r in records:
        if not isinstance(r, dict):
            continue

        router_id = (r.get("router_id") or "").strip()
        local_if = (r.get("local_interface") or "").strip()
        state = (r.get("state") or "").strip()

        # Ignora cabeçalhos ou linhas espúrias
        if not router_id or not local_if or router_id.lower() in ("neighbor", "router-id", "router id", "area id", "area"):
            continue
        if local_if.lower() in ("interface", "local", "name"):
            continue

        # Chave única para deduplicação
        key = (router_id, local_if)
        if key in seen:
            continue
        seen.add(key)

        dr_state = r.get("dr_state") or r.get("dr")
        # Trata formato combinado como Full/DR ou FULL/BDR
        if "/" in state:
            parts = state.split("/", 1)
            state = parts[0].strip().capitalize()
            if not dr_state:
                dr_state = parts[1].strip().upper()
        else:
            state = state.capitalize() if state else "Unknown"

        priority_raw = r.get("priority")
        priority = None
        if priority_raw is not None and str(priority_raw).isdigit():
            priority = int(priority_raw)

        area = (r.get("area") or "0.0.0.0").strip()
        address = (r.get("address") or r.get("neighbor_ip") or "").strip() or None
        dead_time = (r.get("dead_time") or "").strip() or None
        uptime = (r.get("uptime") or "").strip() or None

        neighbors.append({
            "router_id": router_id,
            "state": state,
            "local_interface": local_if,
            "area": area,
            "address": address,
            "priority": priority,
            "dr_state": dr_state if dr_state != "None" else None,
            "dead_time": dead_time,
            "uptime": uptime,
        })

    full_count = sum(1 for n in neighbors if n["state"].lower() == "full")

    return {
        "device": device_hostname,
        "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "summary": {
            "total_neighbors": len(neighbors),
            "full_neighbors": full_count
        },
        "neighbors": neighbors
    }
