"""
mcp_server/normalizers/bgp.py
Normalizador canônico OpenConfig para sessões e vizinhos BGP.
"""

from typing import List, Dict, Any


def normalize_bgp_summary(
    records: List[Dict[str, Any]],
    device_hostname: str
) -> Dict[str, Any]:
    peers = []
    for r in records:
        peer_ip = (r.get("peer_ip") or "").strip()
        if not peer_ip or "%" in peer_ip or "No" in peer_ip or "Neighbor" in peer_ip or peer_ip.startswith("-"):
            continue
        try:
            rem_as = int(r.get("remote_as", 0))
        except (ValueError, TypeError):
            rem_as = 0
        try:
            pfx_rcvd = int(r.get("prefixes_received", 0))
        except (ValueError, TypeError):
            pfx_rcvd = 0

        peers.append({
            "peer_ip": peer_ip,
            "remote_as": rem_as,
            "state": r.get("state", "Established"),
            "uptime": r.get("uptime", ""),
            "prefixes_received": pfx_rcvd,
        })

    return {
        "device": device_hostname,
        "local_as": None,
        "router_id": None,
        "peers": peers
    }
