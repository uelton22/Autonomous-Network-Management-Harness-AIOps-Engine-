"""
mcp_server/ssh_runner.py
Conector SSH com persistência de .raw em disco e aplicação estrita do Gatekeeper de Privilégios.
Garante que saídas brutas fiquem em disco e nunca saturem o contexto da LLM.
"""

import os
import re
import time
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

from mcp_server.security import enforce_privilege, PrivilegeLevel


class SSHRunner:
    """Gerenciador de sessões e execuções SSH para equipamentos de rede."""

    def __init__(self, raw_storage_dir: str = "storage/raw"):
        self.raw_storage_dir = Path(raw_storage_dir)
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
        cache_ttl_seconds: int = 120
    ) -> Dict[str, Any]:
        """
        Executa comando com validação prévia de privilégios e persistência do .raw em disco.
        Conecta-se ao host real via SSH. Se existir um .raw recente (< cache_ttl_seconds)
        para o mesmo host e comando, reaproveita o arquivo evitando conexões redundantes.
        """
        # 1. Gatekeeper de Segurança em 3 Níveis
        active_privilege = enforce_privilege(command, privilege_level, platform_type)

        safe_host = self._sanitize_filename_component(host)
        safe_cmd = self._sanitize_filename_component(command[:30])

        # 2. Verificação de Cache de Curta Duração (Deduplicação de coletas)
        if not force_refresh:
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
                        "raw_path": str(existing.resolve()),
                        "raw_filename": existing.name,
                        "line_count": len(lines),
                        "bytes_count": len(raw_stdout.encode("utf-8")),
                        "reused_raw": True,
                        "cache_hit": True,
                        "raw_preview": "[RAW ISOLADO EM DISCO - REAPROVEITADO DO CACHE LOCAL]"
                    }

        # 3. Execução SSH Real no Equipamento
        raw_stdout = self._execute_real_ssh(host, command, platform_type)

        # 4. Persistência Obrigatória de .raw em Disco
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        raw_filename = f"{safe_host}_{timestamp}_{safe_cmd}.raw"
        raw_filepath = self.raw_storage_dir / raw_filename

        raw_filepath.write_text(raw_stdout, encoding="utf-8")

        lines = raw_stdout.splitlines()

        return {
            "status": "success",
            "host": host,
            "command": command,
            "platform_type": platform_type,
            "privilege_level": active_privilege.value,
            "raw_path": str(raw_filepath.resolve()),
            "raw_filename": raw_filename,
            "line_count": len(lines),
            "bytes_count": len(raw_stdout.encode("utf-8")),
            "reused_raw": False,
            "cache_hit": False,
            "raw_preview": "[RAW ISOLADO EM DISCO - PROIBIDO LEITURA MANUAL. UTILIZE RUN_CANONICAL_ACTION OU RUN_ADHOC_ACTION]"
        }

    def _execute_real_ssh(self, host: str, command: str, platform_type: str) -> str:
        """Executa comando em switch/roteador físico via Netmiko/Paramiko."""
        try:
            from netmiko import ConnectHandler
            
            port = int(os.getenv("NETOPS_SSH_PORT", "22"))
            user = os.getenv("NETOPS_SSH_USER", "admin")
            pwd = os.getenv("NETOPS_SSH_PASSWORD", "admin")
            secret = os.getenv("NETOPS_SSH_SECRET")
            delay = float(os.getenv("NETOPS_SSH_DELAY", "1.0"))

            device_params = {
                "device_type": self._map_netmiko_device_type(platform_type),
                "host": host,
                "port": port,
                "username": user,
                "password": pwd,
                "timeout": 20,
                "global_delay_factor": delay,
            }
            if secret:
                device_params["secret"] = secret

            with ConnectHandler(**device_params) as net_connect:
                # Terminal hygiene
                if "huawei" in platform_type.lower():
                    net_connect.send_command("screen-length 0 temporary")
                else:
                    net_connect.send_command("terminal length 0")
                output = net_connect.send_command(command)
                return output
        except Exception as e:
            # Em caso de falha de conexão real, levanta erro explícito
            raise ConnectionError(f"Falha ao conectar via SSH em {host}:{os.getenv('NETOPS_SSH_PORT', '22')}: {str(e)}")

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
