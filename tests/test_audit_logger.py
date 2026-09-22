"""
tests/test_audit_logger.py
Testes unitários para o gerenciador de logs de auditoria (AuditLogger).
"""

import unittest
import shutil
from pathlib import Path
from mcp_server.audit_logger import AuditLogger


class TestAuditLogger(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path("tests/temp_storage")
        self.logger = AuditLogger(storage_dir=str(self.test_dir))

    def tearDown(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_log_and_list_change(self):
        """Valida gravação e listagem de alteração de configuração."""
        record = self.logger.log_change(
            host="100.75.9.252",
            profile_used="zabbix",
            privilege_level="editor",
            platform_type="datacom_dmos",
            commands=["interface gigabit-ethernet 1/1/1", "description Link-Uplink"],
            raw_output="DM4770(config-if)# description Link-Uplink\n",
            inspection_result={
                "is_success": True,
                "has_errors": False,
                "errors": [],
                "warnings": [],
                "clean_summary": "Configuração aplicada sem erros."
            }
        )

        self.assertIsNotNone(record.get("audit_id"))
        self.assertEqual(record["status"], "applied")
        self.assertEqual(record["host"], "100.75.9.252")

        # Testa listagem
        logs = self.logger.list_logs(host="100.75.9.252")
        self.assertGreaterEqual(len(logs), 1)
        self.assertEqual(logs[0]["audit_id"], record["audit_id"])

        # Testa consulta detalhada
        detail = self.logger.get_log(record["audit_id"])
        self.assertIsNotNone(detail)
        self.assertEqual(detail["commands_sent"], ["interface gigabit-ethernet 1/1/1", "description Link-Uplink"])

    def test_log_failed_change(self):
        """Valida que configurações com erro de CLI são marcadas com status failed."""
        record = self.logger.log_change(
            host="devnetsandboxiosxec9k.cisco.com",
            profile_used="cisco",
            privilege_level="editor",
            platform_type="cisco_iosxe",
            commands=["ip address 10.0.0.1 255.255.255.252"],
            raw_output="% 10.0.0.0 overlaps with Vlan100\n",
            inspection_result={
                "is_success": False,
                "has_errors": True,
                "errors": ["% 10.0.0.0 overlaps with Vlan100"],
                "warnings": [],
                "clean_summary": "Falha na configuração: 1 erro(s) retornado(s)."
            }
        )

        self.assertEqual(record["status"], "failed")
        self.assertEqual(len(record["errors_detected"]), 1)


if __name__ == "__main__":
    unittest.main()
