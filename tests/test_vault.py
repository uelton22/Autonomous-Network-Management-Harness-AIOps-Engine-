"""
tests/test_vault.py
Testes unitários automatizados para o Credentials Vault & Dynamic Profiles do Harness AIOps.
"""

import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
import yaml

from mcp_server.vault import VaultManager, CredentialProfile


class TestVaultManager(unittest.TestCase):

    def setUp(self):
        # Garante variáveis de teste no ambiente
        os.environ["TEST_SSH_USER"] = "test_user_env"
        os.environ["TEST_SSH_PASS"] = "secret_pass_123"

    def test_profile_masked_dict(self):
        """Valida que to_masked_dict nunca expõe senhas ou secrets em texto claro."""
        prof = CredentialProfile(
            name="sec_test",
            description="Teste de mascaramento",
            username="netops",
            password="UltraSecretPassword123!",
            secret="EnableSecret456!",
            port=2222
        )
        masked = prof.to_masked_dict()
        self.assertEqual(masked["name"], "sec_test")
        self.assertEqual(masked["username"], "netops")
        self.assertEqual(masked["port"], 2222)
        self.assertTrue(masked["has_password"])
        self.assertEqual(masked["password"], "********")
        self.assertTrue(masked["has_secret"])
        self.assertEqual(masked["secret"], "********")
        self.assertNotIn("UltraSecretPassword123!", str(masked))
        self.assertNotIn("EnableSecret456!", str(masked))

    def test_vault_load_and_list(self):
        """Valida leitura de YAML do Vault com múltiplos perfis."""
        with TemporaryDirectory() as tmpdir:
            cfg_path = Path(tmpdir) / "credentials.yaml"
            cfg_data = {
                "default_profile": "zabbix",
                "profiles": {
                    "zabbix": {
                        "description": "Perfil Zabbix",
                        "username": "zabbix",
                        "password": "zabbix_password",
                        "port": 22
                    },
                    "noc_core": {
                        "description": "Perfil NOC",
                        "username": "noc_admin",
                        "password": "noc_password",
                        "port": 2222
                    }
                }
            }
            cfg_path.write_text(yaml.dump(cfg_data), encoding="utf-8")

            vm = VaultManager(config_path=str(cfg_path))
            self.assertEqual(vm.default_profile, "zabbix")
            self.assertEqual(len(vm.profiles), 2)

            profiles_list = vm.list_profiles()
            self.assertEqual(len(profiles_list), 2)
            
            # Verifica mascaramento na listagem
            for p in profiles_list:
                self.assertEqual(p["password"], "********")

            # Verifica recuperação do segredo real apenas internamente em get_profile
            zabbix_prof = vm.get_profile("zabbix")
            self.assertEqual(zabbix_prof.password, "zabbix_password")

    def test_vault_env_variable_resolution(self):
        """Valida resolução de sintaxe env:VAR_NAME."""
        with TemporaryDirectory() as tmpdir:
            cfg_path = Path(tmpdir) / "credentials.yaml"
            cfg_data = {
                "default_profile": "env_prof",
                "profiles": {
                    "env_prof": {
                        "username": "env:TEST_SSH_USER",
                        "password": "env:TEST_SSH_PASS",
                        "port": 22
                    }
                }
            }
            cfg_path.write_text(yaml.dump(cfg_data), encoding="utf-8")

            vm = VaultManager(config_path=str(cfg_path))
            prof = vm.get_profile("env_prof")
            self.assertEqual(prof.username, "test_user_env")
            self.assertEqual(prof.password, "secret_pass_123")

    def test_vault_fernet_encryption(self):
        """Valida cifragem e decifragem de tokens Fernet (enc:...)."""
        vm = VaultManager(config_path="non_existent.yaml")
        raw_secret = "MinhaSenhaSuperSecreta@2026"
        token = vm.encrypt_secret(raw_secret)
        self.assertTrue(token.startswith("enc:"))
        
        decrypted = vm.decrypt_secret(token)
        self.assertEqual(decrypted, raw_secret)

    def test_vault_criteria_search(self):
        """Valida busca dinâmica por usuário ou porta."""
        with TemporaryDirectory() as tmpdir:
            cfg_path = Path(tmpdir) / "credentials.yaml"
            cfg_data = {
                "default_profile": "def",
                "profiles": {
                    "def": {
                        "username": "operator",
                        "password": "pass",
                        "port": 22
                    },
                    "custom_port": {
                        "username": "admin",
                        "password": "pass",
                        "port": 2222
                    }
                }
            }
            cfg_path.write_text(yaml.dump(cfg_data), encoding="utf-8")

            vm = VaultManager(config_path=str(cfg_path))
            
            # Busca por porta
            match_port = vm.find_profile_by_criteria(port=2222)
            self.assertIsNotNone(match_port)
            self.assertEqual(match_port.name, "custom_port")

            # Busca por usuário
            match_user = vm.find_profile_by_criteria(username="operator")
            self.assertIsNotNone(match_user)
            self.assertEqual(match_user.name, "def")

    def test_vault_fallback_to_env(self):
        """Valida fallback limpo para o .env caso credentials.yaml não exista."""
        os.environ["NETOPS_SSH_USER"] = "fallback_user"
        os.environ["NETOPS_SSH_PASSWORD"] = "fallback_pass"
        os.environ["NETOPS_SSH_PORT"] = "22"

        vm = VaultManager(config_path="/tmp/caminho_inexistente_12345/credentials.yaml")
        prof = vm.get_profile("default")
        self.assertIsNotNone(prof)
        self.assertEqual(prof.username, "fallback_user")
        self.assertEqual(prof.password, "fallback_pass")


if __name__ == "__main__":
    unittest.main()
