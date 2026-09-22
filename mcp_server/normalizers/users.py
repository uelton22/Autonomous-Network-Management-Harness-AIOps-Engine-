"""
mcp_server/normalizers/users.py
Normalizador canônico OpenConfig para contas de usuários locais e privilégios.
"""

from typing import List, Dict, Any
from datetime import datetime, timezone


def normalize_system_users(
    records: List[Dict[str, Any]],
    vendor: str,
    os_family: str,
    version: str,
    device_hostname: str
) -> Dict[str, Any]:
    """Normaliza registros brutos de usuários de qualquer fabricante para o schema OpenConfig."""
    users_list = []
    seen = set()

    for r in records:
        if not isinstance(r, dict):
            continue
        uname = r.get("username")
        if not uname or uname in seen:
            continue
        seen.add(uname)

        # Trata nível numérico de privilégio
        priv_raw = r.get("privilege") or r.get("privilege_level") or r.get("level")
        priv_int = None
        if priv_raw is not None:
            try:
                priv_int = int(priv_raw)
            except (ValueError, TypeError):
                priv_int = 15 if "admin" in str(priv_raw).lower() else 1

        # Determina role
        role = r.get("role") or r.get("group")
        if not role:
            if priv_int is not None and priv_int >= 15:
                role = "admin"
            else:
                role = "operator"

        # Trata autenticação / hash / senha
        auth_type = r.get("algorithm") or r.get("auth_type") or r.get("secret_type")
        if not auth_type:
            if r.get("secret"):
                auth_type = "secret"
            elif r.get("password"):
                auth_type = "password"
            else:
                auth_type = "local"

        users_list.append({
            "username": uname,
            "role": role,
            "privilege_level": priv_int if priv_int is not None else 15,
            "group": r.get("group", role),
            "authentication_type": auth_type,
            "password_configured": True,
        })

    admin_count = sum(1 for u in users_list if u.get("role") == "admin" or (u.get("privilege_level") or 0) >= 15)

    return {
        "device": device_hostname,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total_users": len(users_list),
            "admin_users": admin_count,
        },
        "users": users_list,
    }
