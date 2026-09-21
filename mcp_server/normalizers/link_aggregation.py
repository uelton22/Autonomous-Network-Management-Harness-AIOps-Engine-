"""
mcp_server/normalizers/link_aggregation.py
Normalizador canônico OpenConfig para Agregações de Enlace (LAG / LACP / Eth-Trunk / Port-Channel).
Unifica saídas de Datacom DmOS, Huawei VRP e Cisco IOS/IOS-XE sob a entidade universal link_aggregations.
"""

import time
from typing import List, Dict, Any, Optional


def normalize_link_aggregation(
    records: List[Dict[str, Any]],
    device_hostname: str
) -> Dict[str, Any]:
    lag_map: Dict[str, Dict[str, Any]] = {}
    current_lag_id: Optional[str] = None

    for r in records:
        if not isinstance(r, dict):
            continue

        lag_id = r.get("lag_id") or r.get("trunk_id") or r.get("channel_group")
        if lag_id and str(lag_id).strip():
            current_lag_id = str(lag_id).strip()
        elif current_lag_id:
            lag_id = current_lag_id

        if not lag_id:
            continue

        lag_id_str = str(lag_id).strip()
        if lag_id_str not in lag_map:
            # Formatação do nome canônico preservando semântica
            raw_name = r.get("name") or lag_id_str
            if not any(raw_name.lower().startswith(p) for p in ("eth-trunk", "po", "port-channel", "lag", "bundle-")):
                lag_name = f"lag {lag_id_str}"
            else:
                lag_name = raw_name

            lag_map[lag_id_str] = {
                "lag_id": lag_id_str,
                "name": lag_name,
                "oper_status": "UP",
                "admin_status": "UP",
                "mode": r.get("mode") or "LACP",
                "min_links": int(r.get("min_links", 1)),
                "description": r.get("description"),
                "members": []
            }

        iface = (r.get("interface") or r.get("port") or "").strip()
        if iface and iface not in ("Interface", "Name", "ID", "Interface Name", "Port") and not iface.startswith("-"):
            op_stat = (r.get("oper_status") or r.get("port_status") or "UP").upper()
            if "UP" in op_stat:
                op_stat = "UP"
            elif "DOWN" in op_stat:
                op_stat = "DOWN"
            else:
                op_stat = "UNKNOWN"

            agg_stat = (r.get("aggregation_status") or "active").strip().lower()
            lacp_stat = r.get("lacp_status") or r.get("state")
            weight = int(r["weight"]) if "weight" in r and str(r["weight"]).isdigit() else None

            lag_map[lag_id_str]["members"].append({
                "interface": iface,
                "oper_status": op_stat,
                "aggregation_status": agg_stat,
                "lacp_status": lacp_stat,
                "weight": weight
            })

    lags_list = []
    total_members = 0
    active_members = 0

    for lag_entry in lag_map.values():
        m_list = lag_entry["members"]
        total_members += len(m_list)
        up_m = [m for m in m_list if m["oper_status"] == "UP" and m["aggregation_status"] == "active"]
        active_members += len(up_m)
        lag_entry["oper_status"] = "UP" if len(up_m) >= lag_entry["min_links"] else ("DOWN" if m_list else lag_entry.get("oper_status", "DOWN"))
        lags_list.append(lag_entry)

    summary = {
        "total_aggregations": len(lags_list),
        "active_aggregations": sum(1 for l in lags_list if l["oper_status"] == "UP"),
        "down_aggregations": sum(1 for l in lags_list if l["oper_status"] == "DOWN"),
        "total_members": total_members,
        "active_members": active_members
    }

    return {
        "device": device_hostname,
        "summary": summary,
        "link_aggregations": lags_list,
        "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
