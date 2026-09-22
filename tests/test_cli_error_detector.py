"""
tests/test_cli_error_detector.py
Testes unitários para o motor de detecção de erros de CLI (inspect_cli_output).
"""

import unittest
from mcp_server.cli_error_detector import inspect_cli_output


class TestCLIErrorDetector(unittest.TestCase):

    def test_cisco_success_output(self):
        """Saída de configuração Cisco limpa (com logs informacionais normais)."""
        output = """
CISCO-9000-IOS-XE-TESTE#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
CISCO-9000-IOS-XE-TE(config)#interface GigabitEthernet1/0/1
CISCO-9000-IOS-XE-TE(config-if)#description GE-teste
CISCO-9000-IOS-XE-TE(config-if)#no shutdown
CISCO-9000-IOS-XE-TE(config-if)#end
%SYS-5-CONFIG_I: Configured from console by nocs1 on vty0
CISCO-9000-IOS-XE-TESTE#
"""
        res = inspect_cli_output(output, platform_type="cisco_iosxe")
        self.assertTrue(res["is_success"])
        self.assertFalse(res["has_errors"])
        self.assertEqual(len(res["errors"]), 0)

    def test_cisco_ip_overlap_error(self):
        """Detecta erro de sobreposição de IP em Cisco (% Overlaps with...)."""
        output = """
CISCO-9000-IOS-XE-TE(config)#interface GigabitEthernet1/0/1
CISCO-9000-IOS-XE-TE(config-if)#ip address 10.0.0.1 255.255.255.252
% 10.0.0.0 overlaps with Vlan100
CISCO-9000-IOS-XE-TE(config-if)#no shutdown
"""
        res = inspect_cli_output(output, platform_type="cisco_iosxe")
        self.assertFalse(res["is_success"])
        self.assertTrue(res["has_errors"])
        self.assertTrue(any("overlaps with Vlan100" in e for e in res["errors"]))

    def test_cisco_incomplete_command(self):
        """Detecta comando incompleto ou inválido em Cisco."""
        output = """
CISCO-9000-IOS-XE-TE(config)#interface GigabitEthernet1/0/1
CISCO-9000-IOS-XE-TE(config-if)#ip address 10.0.0.1
% Incomplete command.
CISCO-9000-IOS-XE-TE(config-if)#badcommand
% Invalid input detected at '^' marker.
"""
        res = inspect_cli_output(output, platform_type="cisco_iosxe")
        self.assertFalse(res["is_success"])
        self.assertEqual(len(res["errors"]), 2)

    def test_datacom_syntax_and_commit_error(self):
        """Detecta erro de sintaxe e falha de commit em Datacom DmOS."""
        output = """
DM4770(config)# username teste
Error: Incomplete command
DM4770(config)# commit
Commit failed: Validation error on interface
"""
        res = inspect_cli_output(output, platform_type="datacom_dmos")
        self.assertFalse(res["is_success"])
        self.assertTrue(res["has_errors"])
        self.assertEqual(len(res["errors"]), 2)

    def test_huawei_unrecognized_command(self):
        """Detecta comando não reconhecido em Huawei VRP."""
        output = """
[Huawei] interface 10GE 1/0/1
Error: Unrecognized command found at '^' position.
"""
        res = inspect_cli_output(output, platform_type="huawei_vrp")
        self.assertFalse(res["is_success"])
        self.assertTrue(res["has_errors"])
        self.assertTrue(any("Unrecognized command" in e for e in res["errors"]))


if __name__ == "__main__":
    unittest.main()
