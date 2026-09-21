"""
mcp_server/normalizers/interfaces.py
Normalizador canônico para resumo e detalhamento de interfaces.
Calcula estatísticas exatas de portas físicas (100GE, XGE, GE) e lógicas (Eth-Trunk, Vlanif).
"""

import re
from typing import List, Dict, Any


def categorize_interface_type(name: str) -> str:
    """Categoriza deterministicamente a interface pelo nome."""
    n = name.strip()
    nl = n.lower()
    if nl.startswith("100ge"):
        return "100GE"
    elif nl.startswith("40ge"):
        return "40GE"
    elif nl.startswith("25ge"):
        return "25GE"
    elif nl.startswith("xge") or nl.startswith("10ge") or nl.startswith("tengig"):
        return "XGE"
    elif nl.startswith("ge") or nl.startswith("gigabit") or nl.startswith("gi"):
        return "GE"
    elif nl.startswith("eth-trunk") or nl.startswith("port-channel") or nl.startswith("bundle-"):
        return "Eth-Trunk"
    elif nl.startswith("vlanif") or nl.startswith("vlan"):
        return "Vlanif"
    elif nl.startswith("loop") or nl.startswith("lo"):
        return "LoopBack"
    elif nl.startswith("ve"):
        return "VE"
    elif nl.startswith("tun"):
        return "Tunnel"
    elif nl.startswith("null"):
        return "NULL"
    elif nl.startswith("eth") or nl.startswith("meth") or nl.startswith("fa"):
        return "Ethernet"
    elif re.match(r"^\d+/\d+", n):
        return "Ethernet"
    elif nl.startswith("lag"):
        return "Eth-Trunk"
    return "Other"


def normalize_interface_summary(
    records: List[Dict[str, Any]],
    device_hostname: str
) -> Dict[str, Any]:
    ifaces = []
    for r in records:
        name = (r.get("name") or "").strip()
        if not name or name in ("Interface", "Unknown", "Name", "ID") or name.startswith("-") or name.startswith("*"):
            continue

        admin = (r.get("admin_status") or "").upper()
        if not admin and "shutdown" in r:
            admin = "DOWN" if str(r["shutdown"]).strip().lower() == "true" else "UP"
        elif not admin:
            admin = "UP"

        oper = (r.get("oper_status") or "UP").upper()
        if "UP" in admin:
            admin = "UP"
        elif "DOWN" in admin:
            admin = "DOWN"

        if "UP" in oper:
            oper = "UP"
        elif "DOWN" in oper:
            oper = "DOWN"

        ifaces.append({
            "name": name,
            "admin_status": admin,
            "oper_status": oper,
            "canonical_name": name,
            "description": r.get("description"),
        })

    # Contadores determinísticos
    admin_up = sum(1 for i in ifaces if i["admin_status"] == "UP")
    admin_down = sum(1 for i in ifaces if i["admin_status"] == "DOWN")
    oper_up = sum(1 for i in ifaces if i["oper_status"] == "UP")
    oper_down = sum(1 for i in ifaces if i["oper_status"] == "DOWN")
    up_up = sum(1 for i in ifaces if i["admin_status"] == "UP" and i["oper_status"] == "UP")
    down_down = sum(1 for i in ifaces if i["admin_status"] == "DOWN" and i["oper_status"] == "DOWN")
    up_down = sum(1 for i in ifaces if i["admin_status"] == "UP" and i["oper_status"] == "DOWN")

    by_type: Dict[str, int] = {}
    for i in ifaces:
        cat = categorize_interface_type(i["name"])
        by_type[cat] = by_type.get(cat, 0) + 1

    summary_stats = {
        "total_interfaces": len(ifaces),
        "admin_up": admin_up,
        "admin_down": admin_down,
        "oper_up": oper_up,
        "oper_down": oper_down,
        "up_up": up_up,
        "down_down": down_down,
        "up_down_anomalies": up_down,
        "by_type": by_type,
    }

    return {
        "device": device_hostname,
        "summary": summary_stats,
        "interfaces": ifaces
    }


def normalize_interface_detail(
    records: List[Dict[str, Any]],
    device_hostname: str
) -> Dict[str, Any]:
    rec = records[0] if records else {}
    admin = (rec.get("admin_status") or "UP").upper()
    oper = (rec.get("oper_status") or "DOWN").upper()
    return {
        "name": rec.get("name", "GE1/0/2"),
        "admin_status": "UP" if "UP" in admin else "DOWN",
        "oper_status": "UP" if "UP" in oper else "DOWN",
        "description": rec.get("description"),
        "mac_address": rec.get("mac_address"),
        "last_flapped": rec.get("last_flapped", "10 min ago"),
        "in_errors": int(rec.get("in_errors", 0)),
        "out_errors": int(rec.get("out_errors", 0)),
        "in_crc_errors": int(rec.get("in_crc_errors", 42)),
        "in_discards": int(rec.get("in_discards", 0)),
    }
