"""
mcp_server/normalizers/users.py
Normalizadores Canônicos OpenConfig para contas de usuários do sistema e sessões ativas.
"""

import time
from typing import List, Dict, Any


def normalize_system_users(records: List[Dict[str, Any]], device_hostname: str) -> Dict[str, Any]:
    """Normaliza saída bruta de usuários para o modelo OpenConfigSystemUsers."""
    users = []
    seen = set()
    for r in records:
        uname = r.get("username", "").strip()
        if not uname or uname in seen or uname.lower() in ("session", "user", "username", "n/a", "total"):
            continue
        seen.add(uname)
        group = r.get("group", "N/A")
        if (group == "N/A" or not group) and "admin_level" in r:
            lvl = str(r["admin_level"]).strip()
            group = f"level-{lvl}" if lvl else "default"
        elif (group == "N/A" or not group) and "privilege_level" in r:
            lvl = str(r["privilege_level"]).strip()
            group = f"level-{lvl}" if lvl else "default"
        elif group == "N/A" or not group:
            group = "default"

        role = r.get("role")
        if not role:
            if "admin_level" in r and str(r["admin_level"]).strip() == "15":
                role = "admin"
            elif group != "default":
                role = group
            else:
                role = "default"

        pwd_configured = True if (r.get("password_hash") or r.get("state") in ("A", "active", "B", "block")) else r.get("password_configured", True)

        users.append({
            "username": uname,
            "group": group,
            "role": role,
            "authentication_type": "local",
            "password_configured": pwd_configured
        })

    return {
        "device": device_hostname,
        "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "summary": {
            "total_users": len(users)
        },
        "users": users
    }


def normalize_user_sessions(records: List[Dict[str, Any]], device_hostname: str) -> Dict[str, Any]:
    """Normaliza saída bruta de sessões de usuários para o modelo OpenConfigUserSessions."""
    sessions = []
    seen_ids = set()
    for r in records:
        sid = str(r.get("session_id", "")).strip()
        uname = r.get("username", "").strip()
        if not sid or not uname or uname.lower() in ("session", "user", "username"):
            continue
        if sid in seen_ids:
            continue
        seen_ids.add(sid)
        is_cur = r.get("is_current", False)
        if isinstance(is_cur, str):
            is_cur = "*" in is_cur or "+" in is_cur or "true" in is_cur.lower()

        ctx = r.get("context", "cli")
        if r.get("context_num"):
            ctx = f"{ctx} {r.get('context_num')}".strip()

        proto = r.get("protocol") or "ssh"
        proto = proto.lower()

        login_time = r.get("login_time") or r.get("delay")

        sessions.append({
            "session_id": sid,
            "username": uname,
            "context": ctx,
            "source_ip": r.get("source_ip", "local"),
            "protocol": proto,
            "login_time": login_time,
            "mode": r.get("mode", "operational"),
            "is_current": is_cur
        })

    return {
        "device": device_hostname,
        "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "summary": {
            "total_sessions": len(sessions)
        },
        "sessions": sessions
    }
