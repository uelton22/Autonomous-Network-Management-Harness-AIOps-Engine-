"""
mcp_server/audit_logger.py
Gerenciador de Trilha de Auditoria Transacional para Comandos de Configuração e Mutação (Editor/Full).
Grava registros imutáveis em storage/audit_log/ com metadados de execução, comandos enviados,
análise de erros de CLI e trechos relevantes da resposta do switch.
"""

import os
import json
import time
import uuid
from pathlib import Path
from typing import Dict, Any, List, Optional


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class AuditLogger:
    """Registrador e consultor de logs de auditoria de configurações de rede."""

    def __init__(self, storage_dir: Optional[str] = None):
        base = storage_dir or os.getenv("NETOPS_STORAGE_DIR", str(PROJECT_ROOT / "storage"))
        self.audit_dir = Path(base) / "audit_log"
        self.audit_dir.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _sanitize(name: str) -> str:
        return "".join(c if c.isalnum() or c in "._-" else "_" for c in name)

    def log_change(
        self,
        host: str,
        profile_used: str,
        privilege_level: str,
        platform_type: str,
        commands: List[str],
        raw_output: str,
        inspection_result: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Registra uma alteração de configuração em arquivo JSON na pasta de auditoria.
        Retorna o dicionário de auditoria contendo o audit_id gerado.
        """
        audit_id = str(uuid.uuid4())[:8]
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        iso_timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

        status = "applied" if inspection_result.get("is_success") else "failed"
        if status == "applied" and inspection_result.get("warnings"):
            status = "applied_with_warnings"

        record = {
            "audit_id": audit_id,
            "timestamp": iso_timestamp,
            "host": host,
            "profile_used": profile_used,
            "privilege_level": privilege_level,
            "platform_type": platform_type,
            "status": status,
            "commands_sent": commands,
            "errors_detected": inspection_result.get("errors", []),
            "warnings_detected": inspection_result.get("warnings", []),
            "summary": inspection_result.get("clean_summary", ""),
            "output_snippet": raw_output[:1000] if raw_output else ""
        }

        safe_host = self._sanitize(host)
        filename = f"{timestamp}_{safe_host}_{audit_id}.json"
        filepath = self.audit_dir / filename

        try:
            filepath.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
        except Exception as e:
            # Em caso de falha de I/O, não deve quebrar a execução mas registra aviso
            record["io_warning"] = f"Falha ao persistir arquivo de auditoria: {str(e)}"

        return record

    def list_logs(self, host: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Lista registros de auditoria mais recentes, opcionalmente filtrados por host."""
        if not self.audit_dir.exists():
            return []

        pattern = "*.json"
        if host:
            safe_host = self._sanitize(host)
            pattern = f"*_{safe_host}_*.json"

        files = sorted(
            self.audit_dir.glob(pattern),
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )

        results = []
        for f in files[:limit]:
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                # Retorna resumo sem o snippet gigante
                results.append({
                    "audit_id": data.get("audit_id"),
                    "timestamp": data.get("timestamp"),
                    "host": data.get("host"),
                    "profile_used": data.get("profile_used"),
                    "privilege_level": data.get("privilege_level"),
                    "status": data.get("status"),
                    "command_count": len(data.get("commands_sent", [])),
                    "commands_preview": data.get("commands_sent", [])[:3],
                    "errors_count": len(data.get("errors_detected", [])),
                    "errors": data.get("errors_detected", [])
                })
            except Exception:
                continue

        return results

    def get_log(self, audit_id: str) -> Optional[Dict[str, Any]]:
        """Recupera o registro completo de um log pelo audit_id."""
        if not self.audit_dir.exists():
            return None

        for f in self.audit_dir.glob(f"*_{audit_id}.json"):
            try:
                return json.loads(f.read_text(encoding="utf-8"))
            except Exception:
                return None
        return None


# Singleton global
audit_logger = AuditLogger()
