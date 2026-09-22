"""
mcp_server/ssh_runner.py
Conector SSH com persistência de .raw em disco e aplicação estrita do Gatekeeper de Privilégios.
Garante que saídas brutas fiquem em disco e nunca saturem o contexto da LLM.
"""

import os
import re
import time
import hashlib
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

from mcp_server.security import enforce_privilege, PrivilegeLevel
from mcp_server.vault import vault, CredentialProfile
from mcp_server.cli_error_detector import inspect_cli_output
from mcp_server.audit_logger import audit_logger


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class SSHRunner:
    """Gerenciador de sessões e execuções SSH para equipamentos de rede."""

    def __init__(self, raw_storage_dir: Optional[str] = None):
        if raw_storage_dir:
            self.raw_storage_dir = Path(raw_storage_dir)
        else:
            base = os.getenv("NETOPS_STORAGE_DIR", str(PROJECT_ROOT / "storage"))
            self.raw_storage_dir = Path(base) / "raw"
        self.raw_storage_dir.mkdir(parents=True, exist_ok=True)

    def _sanitize_filename_component(self, text: str) -> str:
        """Limpa strings para uso seguro em nomes de arquivo."""
        clean = re.sub(r"[^a-zA-Z0-9_\-]", "_", text)
        return re.sub(r"_+", "_", clean).strip("_")

    def execute_command(
        self,
        host: str,
        command: str,
        platform_type: str = "generic",
        privilege_level: str = "read",
        force_refresh: bool = False,
        cache_ttl_seconds: int = 120,
        credential_profile: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Executa comando com validação prévia de privilégios e persistência do .raw em disco.
        Conecta-se ao host real via SSH utilizando o perfil de credenciais solicitado (ou o padrão).
        Se existir um .raw recente (< cache_ttl_seconds) para o mesmo host, perfil e comando,
        reaproveita o arquivo evitando conexões redundantes.
        """
        # 1. Resolução do Perfil de Credenciais no Cofre
        profile = vault.get_profile(credential_profile)

        # 2. Gatekeeper de Segurança em 3 Níveis
        active_privilege = enforce_privilege(command, privilege_level, platform_type)

        safe_host = self._sanitize_filename_component(host)
        cmd_hash = hashlib.md5(command.strip().encode("utf-8")).hexdigest()[:8]
        safe_cmd = f"{self._sanitize_filename_component(command[:30])}_{cmd_hash}"
        safe_prof = self._sanitize_filename_component(profile.name)

        # 3. Verificação de Cache de Curta Duração (Deduplicação de coletas apenas para READ)
        if not force_refresh and active_privilege == PrivilegeLevel.READ:
            pattern = f"{safe_host}_*_{safe_cmd}.raw"
            existing_raws = sorted(
                self.raw_storage_dir.glob(pattern),
                key=lambda p: p.stat().st_mtime,
                reverse=True
            )
            now = time.time()
            for existing in existing_raws:
                file_age = now - existing.stat().st_mtime
                if file_age <= cache_ttl_seconds:
                    raw_stdout = existing.read_text(encoding="utf-8")
                    lines = raw_stdout.splitlines()
                    return {
                        "status": "success",
                        "host": host,
                        "command": command,
                        "platform_type": platform_type,
                        "privilege_level": active_privilege.value,
                        "profile_used": profile.name,
                        "username_used": profile.username,
                        "port_used": profile.port,
                        "raw_path": str(existing.resolve()),
                        "raw_filename": existing.name,
                        "line_count": len(lines),
                        "bytes_count": len(raw_stdout.encode("utf-8")),
                        "reused_raw": True,
                        "cache_hit": True,
                        "raw_preview": "[RAW ISOLADO EM DISCO - REAPROVEITADO DO CACHE LOCAL]"
                    }

        # 4. Execução SSH Real no Equipamento com o Perfil Resolvido
        raw_stdout = self._execute_real_ssh(
            host,
            command,
            platform_type,
            profile=profile,
            privilege_level=active_privilege.value
        )

        # 5. Persistência Obrigatória de .raw em Disco
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        raw_filename = f"{safe_host}_{timestamp}_{safe_cmd}.raw"
        raw_filepath = self.raw_storage_dir / raw_filename

        raw_filepath.write_text(raw_stdout, encoding="utf-8")

        lines = raw_stdout.splitlines()

        # 6. Para comandos de configuração (EDITOR ou FULL), executa inspeção de erros e auditoria
        if active_privilege in (PrivilegeLevel.EDITOR, PrivilegeLevel.FULL):
            inspection = inspect_cli_output(raw_stdout, platform_type)
            config_lines = [l.strip() for l in command.splitlines() if l.strip()]
            audit_record = audit_logger.log_change(
                host=host,
                profile_used=profile.name,
                privilege_level=active_privilege.value,
                platform_type=platform_type,
                commands=config_lines,
                raw_output=raw_stdout,
                inspection_result=inspection
            )

            status = audit_record["status"]
            return {
                "status": status,
                "host": host,
                "command": command,
                "platform_type": platform_type,
                "privilege_level": active_privilege.value,
                "profile_used": profile.name,
                "username_used": profile.username,
                "port_used": profile.port,
                "audit_id": audit_record["audit_id"],
                "is_success": inspection["is_success"],
                "has_errors": inspection["has_errors"],
                "errors_detected": inspection["errors"],
                "warnings_detected": inspection["warnings"],
                "summary": inspection["clean_summary"],
                "raw_path": str(raw_filepath.resolve()),
                "raw_filename": raw_filename,
                "line_count": len(lines),
                "bytes_count": len(raw_stdout.encode("utf-8")),
                "output_snippet": raw_stdout[:500] if inspection["has_errors"] else "[CONFIG ENVIADA COM SUCESSO - REGISTRADA EM AUDITORIA]"
            }

        # Para comandos de leitura (READ), mantém isolamento padrão de RAW
        return {
            "status": "success",
            "host": host,
            "command": command,
            "platform_type": platform_type,
            "privilege_level": active_privilege.value,
            "profile_used": profile.name,
            "username_used": profile.username,
            "port_used": profile.port,
            "raw_path": str(raw_filepath.resolve()),
            "raw_filename": raw_filename,
            "line_count": len(lines),
            "bytes_count": len(raw_stdout.encode("utf-8")),
            "reused_raw": False,
            "cache_hit": False,
            "raw_preview": "[RAW ISOLADO EM DISCO - PROIBIDO LEITURA MANUAL. UTILIZE RUN_CANONICAL_ACTION OU RUN_ADHOC_ACTION]"
        }

    def _execute_real_ssh(
        self,
        host: str,
        command: str,
        platform_type: str,
        profile: Optional[CredentialProfile] = None,
        privilege_level: str = "read"
    ) -> str:
        """Executa comando em switch/roteador físico via Netmiko/Paramiko com perfil de credenciais."""
        if profile is None:
            profile = vault.get_profile()

        try:
            from netmiko import ConnectHandler

            device_params = {
                "device_type": self._map_netmiko_device_type(platform_type),
                "host": host,
                "port": profile.port,
                "username": profile.username,
                "password": profile.password,
                "timeout": 20,
                "global_delay_factor": profile.delay,
            }
            if profile.secret:
                device_params["secret"] = profile.secret
            if profile.ssh_key_path:
                device_params["use_keys"] = True
                device_params["key_file"] = profile.ssh_key_path

            with ConnectHandler(**device_params) as net_connect:
                # Terminal hygiene
                if "huawei" in platform_type.lower():
                    net_connect.send_command("screen-length 0 temporary")
                else:
                    net_connect.send_command("terminal length 0")

                is_exec = any(command.strip().lower().startswith(p) for p in ("show ", "display ", "ping ", "traceroute ", "tracert ", "dir", "who", "write"))
                if privilege_level in ("editor", "full") and not is_exec:
                    config_lines = [line.strip() for line in command.splitlines() if line.strip()]
                    output = net_connect.send_config_set(config_lines)
                else:
                    output = net_connect.send_command(command)
                return output

        except Exception as e:
            # Em caso de falha de conexão real, levanta erro explícito com porta e perfil
            raise ConnectionError(
                f"Falha ao conectar via SSH em {host}:{profile.port} (perfil: '{profile.name}', usuário: '{profile.username}'): {str(e)}"
            )

    def _map_netmiko_device_type(self, platform_type: str) -> str:
        pt = platform_type.lower()
        if "huawei" in pt:
            return "huawei"
        if "datacom" in pt or "dmos" in pt:
            return "cisco_ios"  # Netmiko usa cisco_ios ou terminal_server como base para DmOS
        if "cisco" in pt:
            return "cisco_ios"
        if "juniper" in pt:
            return "juniper_junos"
        return "generic_termserver"
