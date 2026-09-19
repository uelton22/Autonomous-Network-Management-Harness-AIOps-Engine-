"""
mcp_server/security.py
Gatekeeper de Segurança e Validação de Privilégios em 3 Níveis (read, editor, full).
Garante que comandos perigosos ou de configuração sejam bloqueados antes do envio ao SSH.
"""

from enum import Enum
import re
from typing import Tuple, Optional


class PrivilegeLevel(str, Enum):
    READ = "read"
    EDITOR = "editor"
    FULL = "full"

    @classmethod
    def from_string(cls, val: str) -> "PrivilegeLevel":
        v = (val or "").strip().lower()
        if v in ("read", "readonly", "audit", "ready"):
            return cls.READ
        elif v in ("editor", "operator", "config"):
            return cls.EDITOR
        elif v in ("full", "admin", "root", "superuser"):
            return cls.FULL
        raise ValueError(f"Nível de privilégio inválido: '{val}'. Valores permitidos: read, editor, full")


class PrivilegeViolationError(Exception):
    """Exceção levantada quando um comando viola o nível de privilégio concedido."""
    pass


# -------------------------------------------------------------------------
# PADRÕES DE REGEX PARA VALIDAÇÃO DE COMANDOS
# -------------------------------------------------------------------------

# Comandos expressamente permitidos em modo READ (Inspeção / Auditoria)
READ_ALLOWED_PATTERNS = [
    re.compile(r"^\s*show\s+", re.IGNORECASE),
    re.compile(r"^\s*display\s+", re.IGNORECASE),
    re.compile(r"^\s*dir(\s+|$|\?)", re.IGNORECASE),
    re.compile(r"^\s*ping(\s+|$)", re.IGNORECASE),
    re.compile(r"^\s*traceroute(\s+|$)", re.IGNORECASE),
    re.compile(r"^\s*tracert(\s+|$)", re.IGNORECASE),
]

# Blacklist estrita para modo READ (bloqueia qualquer modo de config ou mutação)
READ_BLOCKED_PATTERNS = [
    re.compile(r"\b(system-view|sys)\b", re.IGNORECASE),
    re.compile(r"\b(configure\s+terminal|conf\s+t|config)\b", re.IGNORECASE),
    re.compile(r"\b(reboot|reload|reset|power-off|shutdown-system)\b", re.IGNORECASE),
    re.compile(r"\b(save|write|commit)\b", re.IGNORECASE),
    re.compile(r"\b(format|erase|delete|rmdir|remove)\b", re.IGNORECASE),
    re.compile(r"\b(shutdown)\b", re.IGNORECASE),
    re.compile(r"^\s*(undo|no)\s+", re.IGNORECASE),
    re.compile(r"\b(patch|upgrade|boot-loader|firmware\s+upgrade)\b", re.IGNORECASE),
    re.compile(r"\b(user|password|aaa|radius|tacacs)\b", re.IGNORECASE),
    re.compile(r"\b(clear\s+configuration|factory-default)\b", re.IGNORECASE),
]

# Blacklist estrita para modo EDITOR (permite configs pontuais, mas bloqueia desastres)
EDITOR_BLOCKED_PATTERNS = [
    re.compile(r"\b(reboot|reload|power-off)\b", re.IGNORECASE),
    re.compile(r"\b(format|erase\s+flash|erase\s+startup-config)\b", re.IGNORECASE),
    re.compile(r"\b(factory-default|clear\s+configuration\s+all)\b", re.IGNORECASE),
    re.compile(r"\b(undo\s+aaa|no\s+aaa|undo\s+local-user)\b", re.IGNORECASE),
    re.compile(r"\b(password\s+cipher|user\s+admin\s+password)\b", re.IGNORECASE),
    re.compile(r"\b(upgrade\s+software|install\s+all)\b", re.IGNORECASE),
]


def validate_command_privilege(
    command: str,
    privilege_level: PrivilegeLevel,
    platform_type: str = "generic"
) -> Tuple[bool, Optional[str]]:
    """
    Valida se um comando é permitido sob o nível de privilégio especificado.
    
    Retorna:
        (True, None) se permitido.
        (False, reason_str) se bloqueado.
    """
    cmd = (command or "").strip()
    if not cmd:
        return False, "Comando vazio não pode ser executado."

    if privilege_level == PrivilegeLevel.FULL:
        # Nível FULL tem acesso irrestrito
        return True, None

    if privilege_level == PrivilegeLevel.READ:
        # 1. Verifica se viola a blacklist de leitura
        for blocked in READ_BLOCKED_PATTERNS:
            if blocked.search(cmd):
                return False, (
                    f"Comando '{cmd}' BLOQUEADO sob privilégio READ. "
                    f"Tentativa de entrar em modo de configuração ou executar ação modificadora/destrutiva."
                )

        # 2. Verifica se atende a whitelist de leitura (deve iniciar com show, display, dir, ping, traceroute)
        is_read_allowed = any(pattern.match(cmd) for pattern in READ_ALLOWED_PATTERNS)
        if not is_read_allowed:
            return False, (
                f"Comando '{cmd}' NÃO PERMITIDO sob privilégio READ. "
                f"Apenas comandos de inspeção ('show', 'display', 'dir', 'ping', 'traceroute') são autorizados."
            )
        return True, None

    if privilege_level == PrivilegeLevel.EDITOR:
        # Modo editor permite show/display e comandos operacionais, mas bloqueia ações catastróficas
        for blocked in EDITOR_BLOCKED_PATTERNS:
            if blocked.search(cmd):
                return False, (
                    f"Comando '{cmd}' BLOQUEADO sob privilégio EDITOR. "
                    f"Ação destrutiva ou de risco crítico à integridade do equipamento."
                )
        return True, None

    return False, f"Nível de privilégio desconhecido: {privilege_level}"


def enforce_privilege(command: str, privilege_level_str: str, platform_type: str = "generic") -> PrivilegeLevel:
    """
    Aplica a validação e levanta PrivilegeViolationError caso o comando seja rejeitado.
    """
    level = PrivilegeLevel.from_string(privilege_level_str)
    allowed, reason = validate_command_privilege(command, level, platform_type)
    if not allowed:
        raise PrivilegeViolationError(reason)
    return level
