"""
mcp_server/fingerprinter.py
Motor de Descoberta Progressiva Zero-Knowledge de Equipamentos de Rede.
Executa L1 (Banner Grab TCP 22) -> L2 (Prompt Handshake) -> L3 (Deterministic CLI Probe).
"""

import socket
import re
import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

class DeviceFingerprintResult:
    def __init__(self, vendor: str, os_family: str, major_version: str, method: str, confidence: float):
        self.vendor = vendor
        self.os_family = os_family
        self.major_version = major_version
        self.method = method  # L1_BANNER, L2_PROMPT, L3_PROBE
        self.confidence = confidence

    def to_dict(self) -> Dict[str, Any]:
        return {
            "vendor": self.vendor,
            "os_family": self.os_family,
            "major_version": self.major_version,
            "method": self.method,
            "confidence": self.confidence,
        }


def grab_tcp_banner(host: str, port: int = 22, timeout: float = 3.0) -> Optional[str]:
    """Nível 1: Lê os primeiros bytes antes de qualquer autenticação SSH."""
    try:
        with socket.create_connection((host, port), timeout=timeout) as s:
            s.settimeout(timeout)
            banner = s.recv(1024).decode("utf-8", errors="ignore")
            return banner
    except Exception:
        return None


def inspect_banner(banner: str) -> Optional[DeviceFingerprintResult]:
    """Analisa a string do banner SSH para identificar vendor e SO."""
    if not banner:
        return None

    b_lower = banner.lower()

    # Huawei
    if "huawei" in b_lower:
        # Ex: SSH-2.0-Huawei-1.58
        return DeviceFingerprintResult(
            vendor="huawei",
            os_family="vrp",
            major_version="v800",
            method="L1_BANNER",
            confidence=0.95
        )

    # Datacom
    if "datacom" in b_lower or "dmos" in b_lower:
        # Ex: SSH-2.0-Datacom-DmOS-12.0.2
        ver_match = re.search(r"dmos[^\d]*(\d+[\.\d_]+)", banner, re.IGNORECASE)
        if ver_match:
            ver = ver_match.group(1).replace(".", "_")
        else:
            matches = re.findall(r"(\d+\.\d+(?:\.\d+)?)", banner)
            ver = matches[-1].replace(".", "_") if matches else "12_0_2"
        return DeviceFingerprintResult(
            vendor="datacom",
            os_family="dmos",
            major_version=ver,
            method="L1_BANNER",
            confidence=0.98
        )

    # Cisco
    if "cisco" in b_lower:
        return DeviceFingerprintResult(
            vendor="cisco",
            os_family="ios-xe",
            major_version="17_x",
            method="L1_BANNER",
            confidence=0.90
        )

    return None


def inspect_prompt(prompt: str) -> Optional[DeviceFingerprintResult]:
    """Nível 2: Analisa delimitadores de prompt após o handshake SSH."""
    if not prompt:
        return None

    p = prompt.strip()

    # Huawei: <hostname> ou [hostname]
    if (p.startswith("<") and p.endswith(">")) or (p.startswith("[") and p.endswith("]")):
        return DeviceFingerprintResult(
            vendor="huawei",
            os_family="vrp",
            major_version="v800",
            method="L2_PROMPT",
            confidence=0.90
        )

    # Datacom DmOS: DM4610# ou DmOS# ou user@hostname#
    if re.search(r"\b(DM\d+|DmOS)\b", p, re.IGNORECASE) or p.startswith("DM"):
        return DeviceFingerprintResult(
            vendor="datacom",
            os_family="dmos",
            major_version="12_0_2",
            method="L2_PROMPT",
            confidence=0.92
        )

    # Cisco / Generic
    if p.endswith("#") or p.endswith(">"):
        return DeviceFingerprintResult(
            vendor="cisco",
            os_family="ios",
            major_version="15_x",
            method="L2_PROMPT",
            confidence=0.75
        )

    return None

_FINGERPRINT_CACHE: Dict[str, DeviceFingerprintResult] = {}


def probe_real_device(host: str) -> Optional[DeviceFingerprintResult]:
    """Conecta no dispositivo real para capturar prompt (L2) e executar probes CLI (L3)."""
    try:
        import os
        from netmiko import ConnectHandler

        port = int(os.getenv("NETOPS_SSH_PORT", "22"))
        user = os.getenv("NETOPS_SSH_USER", "admin")
        pwd = os.getenv("NETOPS_SSH_PASSWORD", "admin")
        secret = os.getenv("NETOPS_SSH_SECRET")
        delay = float(os.getenv("NETOPS_SSH_DELAY", "1.0"))

        device_params = {
            "device_type": "generic_termserver",
            "host": host,
            "port": port,
            "username": user,
            "password": pwd,
            "timeout": 15,
            "global_delay_factor": delay,
        }
        if secret:
            device_params["secret"] = secret

        with ConnectHandler(**device_params) as conn:
            # L2: Prompt check
            prompt = conn.find_prompt()
            res_l2 = inspect_prompt(prompt)
            if res_l2 and res_l2.confidence >= 0.90:
                return res_l2

            # L3: Probing CLI
            conn.send_command("terminal length 0")

            # 1. Test Datacom DmOS
            try:
                out_fw = conn.send_command("show firmware")
                if "Version" in out_fw and ("Active" in out_fw or "State" in out_fw or "Inactive" in out_fw):
                    m = re.search(r"(\d+\.\d+(?:\.\d+)?)[^\n]*Active", out_fw)
                    if not m:
                        m = re.search(r"(\d+\.\d+(?:\.\d+)?)", out_fw)
                    ver = m.group(1).replace(".", "_") if m else "12_0_2"
                    return DeviceFingerprintResult(
                        vendor="datacom",
                        os_family="dmos",
                        major_version=ver,
                        method="L3_PROBE",
                        confidence=1.0
                    )
            except Exception:
                pass

            # 2. Test Huawei VRP
            try:
                conn.send_command("screen-length 0 temporary")
                out_vrp = conn.send_command("display version")
                if "Huawei" in out_vrp or "VRP" in out_vrp:
                    m = re.search(r"Version\s+(\d+\.\d+|V\d+R\d+)", out_vrp, re.IGNORECASE)
                    ver = m.group(1).replace(".", "_") if m else "v800"
                    return DeviceFingerprintResult(
                        vendor="huawei",
                        os_family="vrp",
                        major_version=ver,
                        method="L3_PROBE",
                        confidence=1.0
                    )
            except Exception:
                pass

            # 3. Test Cisco
            try:
                out_cisco = conn.send_command("show version")
                if "Cisco" in out_cisco or "IOS" in out_cisco:
                    m = re.search(r"Version\s+(\d+\.\d+)", out_cisco, re.IGNORECASE)
                    ver = m.group(1).replace(".", "_") if m else "17_x"
                    return DeviceFingerprintResult(
                        vendor="cisco",
                        os_family="iosxe",
                        major_version=ver,
                        method="L3_PROBE",
                        confidence=1.0
                    )
            except Exception:
                pass

            if res_l2:
                return res_l2

    except Exception:
        pass

    return None


def progressive_fingerprint(host: str, ssh_runner=None) -> DeviceFingerprintResult:
    """
    Executa o fluxo completo de descoberta em 3 níveis:
    L1: Banner Grab
    L2: Prompt Handshake
    L3: Deterministic Probe CLI
    """
    if host in _FINGERPRINT_CACHE:
        return _FINGERPRINT_CACHE[host]

    # 1. Nível 1: Banner Grab
    banner = grab_tcp_banner(host)
    if banner:
        res = inspect_banner(banner)
        if res and res.confidence >= 0.90:
            _FINGERPRINT_CACHE[host] = res
            return res

    # 2. Nível 2 / Nível 3: Probing CLI em Equipamento Real via SSH
    real_res = probe_real_device(host)
    if real_res:
        _FINGERPRINT_CACHE[host] = real_res
        return real_res

    # Fallback default
    fallback = DeviceFingerprintResult(
        vendor="generic",
        os_family="posix",
        major_version="1_0",
        method="FALLBACK",
        confidence=0.50
    )
    _FINGERPRINT_CACHE[host] = fallback
    return fallback
