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
        if not uname or uname in seen or uname.lower() in ("session", "user", "username"):
            continue
        seen.add(uname)
        group = r.get("group", "N/A")
        if group == "N/A" or not group:
            group = "default"
        users.append({
            "username": uname,
            "group": group,
            "role": group,
            "authentication_type": "local",
            "password_configured": True if r.get("password_hash") else False
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
            is_cur = "*" in is_cur or "true" in is_cur.lower()

        sessions.append({
            "session_id": sid,
            "username": uname,
            "context": r.get("context", "cli"),
            "source_ip": r.get("source_ip", "local"),
            "protocol": r.get("protocol", "ssh"),
            "login_time": r.get("login_time"),
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
