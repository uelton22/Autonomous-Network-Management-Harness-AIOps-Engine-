"""
mcp_server/vault.py
Cofre de Credenciais e Perfis de Acesso Dinâmicos (Credentials Vault & Profiles).
Gerencia múltiplos perfis SSH de forma segura, com mascaramento de senhas,
resolução de variáveis de ambiente e suporte a criptografia Fernet.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional
import yaml
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


class CredentialProfile(BaseModel):
    """Modelo de dados de um Perfil de Acesso SSH."""
    name: str
    description: str = ""
    username: str = "admin"
    password: str = ""
    port: int = 22
    secret: Optional[str] = None
    ssh_key_path: Optional[str] = None
    delay: float = 1.0

    def to_masked_dict(self) -> Dict[str, Any]:
        """Retorna representação segura do perfil para exibição ao operador e APIs, sem expor senhas."""
        return {
            "name": self.name,
            "description": self.description,
            "username": self.username,
            "port": self.port,
            "has_password": bool(self.password),
            "password": "********" if self.password else None,
            "has_secret": bool(self.secret),
            "secret": "********" if self.secret else None,
            "ssh_key_path": self.ssh_key_path,
            "delay": self.delay
        }


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class VaultManager:
    """Gerenciador central de perfis de autenticação e segredos do Harness."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path or (PROJECT_ROOT / "registry" / "credentials.yaml"))
        self._profiles: Dict[str, CredentialProfile] = {}
        self._default_profile_name: str = "default"
        self.reload()

    @property
    def default_profile(self) -> str:
        """Nome do perfil padrão configurado."""
        return self._default_profile_name

    @property
    def profiles(self) -> Dict[str, CredentialProfile]:
        """Dicionário com os perfis carregados."""
        return self._profiles

    def _resolve_secret_value(self, val: Optional[str]) -> Optional[str]:
        """Resolve o valor real do segredo tratando env:VAR e enc:TOKEN."""
        if not val or not isinstance(val, str):
            return val
        
        val = val.strip()
        # 1. Resolução via Variável de Ambiente
        if val.startswith("env:"):
            env_var = val[4:].strip()
            return os.getenv(env_var, "")
            
        # 2. Resolução via Token Criptografado Fernet
        if val.startswith("enc:"):
            token = val[4:].strip()
            return self.decrypt_secret(token)
            
        return val

    def reload(self):
        """Carrega ou recarrega o catálogo de credenciais."""
        self._profiles.clear()
        
        if self.config_path.exists():
            try:
                data = yaml.safe_load(self.config_path.read_text(encoding="utf-8")) or {}
                self._default_profile_name = data.get("default_profile", "default")
                raw_profiles = data.get("profiles", {})
                
                for prof_name, cfg in raw_profiles.items():
                    resolved_user = self._resolve_secret_value(cfg.get("username", "admin")) or "admin"
                    resolved_pass = self._resolve_secret_value(cfg.get("password", "")) or ""
                    resolved_sec = self._resolve_secret_value(cfg.get("secret"))
                    resolved_key = self._resolve_secret_value(cfg.get("ssh_key_path"))
                    port_val = int(cfg.get("port", 22))
                    delay_val = float(cfg.get("delay", 1.0))
                    
                    profile = CredentialProfile(
                        name=prof_name,
                        description=cfg.get("description", ""),
                        username=resolved_user,
                        password=resolved_pass,
                        port=port_val,
                        secret=resolved_sec,
                        ssh_key_path=resolved_key,
                        delay=delay_val
                    )
                    self._profiles[prof_name] = profile
            except Exception as e:
                print(f"[VaultManager] Aviso: Erro ao carregar {self.config_path}: {e}")

        # Se nenhum perfil foi carregado, inicializa com o fallback padrão do .env
        if not self._profiles:
            env_user = os.getenv("NETOPS_SSH_USER", "admin")
            env_pass = os.getenv("NETOPS_SSH_PASSWORD") or os.getenv("NETOPS_SSH_PASS") or "admin"
            env_port = int(os.getenv("NETOPS_SSH_PORT", "22"))
            env_secret = os.getenv("NETOPS_SSH_SECRET")
            env_key = os.getenv("NETOPS_SSH_KEY_PATH")
            env_delay = float(os.getenv("NETOPS_SSH_DELAY", "1.0"))
            
            fallback = CredentialProfile(
                name="default",
                description="Perfil de fallback herdado diretamente do .env",
                username=env_user,
                password=env_pass,
                port=env_port,
                secret=env_secret,
                ssh_key_path=env_key,
                delay=env_delay
            )
            self._profiles["default"] = fallback
            self._default_profile_name = "default"

    @property
    def default_profile_name(self) -> str:
        return self._default_profile_name

    def list_profiles(self) -> List[Dict[str, Any]]:
        """Lista todos os perfis disponíveis com senhas rigorosamente mascaradas."""
        result = []
        for name, profile in self._profiles.items():
            info = profile.to_masked_dict()
            info["is_default"] = (name == self._default_profile_name)
            result.append(info)
        return result

    def get_profile(self, name_or_alias: Optional[str] = None) -> CredentialProfile:
        """
        Retorna o perfil solicitado ou o padrão.
        Suporta correspondência insensível a maiúsculas/minúsculas.
        """
        if not name_or_alias:
            name_or_alias = self._default_profile_name

        key = name_or_alias.strip().lower()

        # 1. Correspondência exata ou normalizada
        for prof_name, prof in self._profiles.items():
            if prof_name.lower() == key:
                return prof

        # 2. Se não encontrou, tenta buscar por username correspondente
        for prof in self._profiles.values():
            if prof.username.lower() == key:
                return prof

        available = list(self._profiles.keys())
        raise ValueError(
            f"Perfil de credencial '{name_or_alias}' não encontrado no cofre. "
            f"Perfis disponíveis: {available}"
        )

    def find_profile_by_criteria(
        self,
        username: Optional[str] = None,
        port: Optional[int] = None
    ) -> Optional[CredentialProfile]:
        """Localiza perfil compatível com base no nome de usuário e/ou porta especificados na query."""
        for prof in self._profiles.values():
            match_user = True
            match_port = True
            
            if username:
                match_user = (prof.username.lower() == username.strip().lower())
            if port is not None:
                match_port = (prof.port == int(port))
                
            if match_user and match_port:
                return prof
                
        return None

    # -------------------------------------------------------------------------
    # Criptografia Fernet para Segredos no Disco
    # -------------------------------------------------------------------------
    @staticmethod
    def _get_fernet_key() -> bytes:
        """Obtém ou deriva a chave mestra de criptografia do .env para exatamente 32 bytes url-safe base64."""
        import base64
        import hashlib
        raw_key = os.getenv("NETOPS_VAULT_KEY", "netops-aiops-default-vault-master-key-2026")
        digest = hashlib.sha256(raw_key.encode("utf-8")).digest()
        return base64.urlsafe_b64encode(digest)

    def encrypt_secret(self, text: str) -> str:
        """Criptografa uma senha ou segredo em token Fernet seguro."""
        try:
            from cryptography.fernet import Fernet
            f = Fernet(self._get_fernet_key())
            encrypted = f.encrypt(text.encode("utf-8"))
            return f"enc:{encrypted.decode('utf-8')}"
        except Exception as e:
            raise RuntimeError(f"Erro ao criptografar segredo: {e}")

    def decrypt_secret(self, token: str) -> str:
        """Descriptografa um token Fernet."""
        try:
            from cryptography.fernet import Fernet
            f = Fernet(self._get_fernet_key())
            clean_token = token.removeprefix("enc:").encode("utf-8")
            decrypted = f.decrypt(clean_token)
            return decrypted.decode("utf-8")
        except Exception as e:
            print(f"[VaultManager] Aviso: Falha ao descriptografar token: {e}")
            return ""


# Instância global Singleton do VaultManager
vault = VaultManager()


def get_vault() -> VaultManager:
    """Retorna a instância singleton do VaultManager."""
    return vault


# -------------------------------------------------------------------------
# Utilitário CLI do Vault
# -------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "--list":
            print("Perfis de Credenciais Cadastrados no Cofre:")
            for p in vault.list_profiles():
                def_marker = " (PADRÃO)" if p["is_default"] else ""
                print(f"- [{p['name']}]{def_marker}: usuário={p['username']}, porta={p['port']}, senha={p['password']}")
        elif cmd == "--encrypt" and len(sys.argv) > 2:
            secret_input = sys.argv[2]
            encrypted = vault.encrypt_secret(secret_input)
            print(f"Token Criptografado para uso em credentials.yaml:\n{encrypted}")
        elif cmd == "--gen-key":
            from cryptography.fernet import Fernet
            new_key = Fernet.generate_key().decode("utf-8")
            print(f"Nova chave mestra para NETOPS_VAULT_KEY no .env:\nNETOPS_VAULT_KEY={new_key}")
        else:
            print("Uso: python -m mcp_server.vault [--list | --encrypt <senha> | --gen-key]")
    else:
        print("Vault carregado com sucesso. Perfis ativos:", [p["name"] for p in vault.list_profiles()])
