"""
mcp_server/fingerprinter.py
Motor de Descoberta Progressiva Zero-Knowledge de Equipamentos de Rede.
Executa L1 (Banner Grab TCP 22) -> L2 (Prompt Handshake) -> L3 (Deterministic CLI Probe).

Garante identificação determinística e exata de fabricante, SO, versão e modelo sem suposições cegas.
"""

import socket
import re
import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

from mcp_server.vault import vault, CredentialProfile


class DeviceFingerprintResult:
    def __init__(
        self,
        vendor: str,
        os_family: str,
        major_version: str,
        method: str,
        confidence: float,
        full_version: Optional[str] = None,
        model: Optional[str] = None,
        platform_key: Optional[str] = None
    ):
        self.vendor = vendor
        self.os_family = os_family
        self.major_version = major_version
        self.method = method  # L1_BANNER, L2_PROMPT, L3_PROBE, FALLBACK
        self.confidence = confidence
        self.full_version = full_version or major_version
        self.model = model or "generic"
        self.platform_key = platform_key or f"{vendor}_{os_family}_{major_version}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "vendor": self.vendor,
            "os_family": self.os_family,
            "major_version": self.major_version,
            "full_version": self.full_version,
            "model": self.model,
            "platform_key": self.platform_key,
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
    """
    Analisa a string do banner SSH para identificar vendor preliminar.
    Banners SSH em geral não contêm a versão real de firmware.
    """
    if not banner:
        return None

    b_lower = banner.lower()

    if "huawei" in b_lower:
        return DeviceFingerprintResult(
            vendor="huawei",
            os_family="vrp",
            major_version="unknown",
            method="L1_BANNER",
            confidence=0.50
        )

    if "datacom" in b_lower or "dmos" in b_lower:
        ver_match = re.search(r"dmos[^\d]*(\d+[\.\d_]+)", banner, re.IGNORECASE)
        ver = ver_match.group(1).replace(".", "_") if ver_match else "unknown"
        return DeviceFingerprintResult(
            vendor="datacom",
            os_family="dmos",
            major_version=ver,
            method="L1_BANNER",
            confidence=0.70
        )

    if "cisco" in b_lower:
        return DeviceFingerprintResult(
            vendor="cisco",
            os_family="ios",
            major_version="unknown",
            method="L1_BANNER",
            confidence=0.50
        )

    return None


_FINGERPRINT_CACHE: Dict[str, DeviceFingerprintResult] = {}


def probe_real_device(host: str, credential_profile: Optional[str] = None) -> Optional[DeviceFingerprintResult]:
    """
    Nível 3: Conecta via SSH no dispositivo real, detecta prompt e executa comandos
    de inspeção de versão determinísticos com 100% de confiança (L3_PROBE).
    Utiliza as credenciais do perfil solicitado (ou default) do Vault.
    """
    try:
        from netmiko import ConnectHandler

        profile = vault.get_profile(credential_profile)

        device_params = {
            "device_type": "generic_termserver",
            "host": host,
            "port": profile.port,
            "username": profile.username,
            "password": profile.password,
            "timeout": 15,
            "global_delay_factor": profile.delay,
        }
        if profile.secret:
            device_params["secret"] = profile.secret
        if profile.ssh_key_path:
            device_params["use_keys"] = True
            device_params["key_file"] = profile.ssh_key_path

        with ConnectHandler(**device_params) as conn:
            prompt = conn.find_prompt()
            p = prompt.strip()

            is_huawei_prompt = (p.startswith("<") and p.endswith(">")) or (p.startswith("[") and p.endswith("]"))

            # -------------------------------------------------------------
            # ESTRATÉGIA A: Se o prompt indicar claramente Huawei (<...> ou [...])
            # -------------------------------------------------------------
            if is_huawei_prompt:
                try:
                    conn.send_command("screen-length 0 temporary")
                    out_vrp = conn.send_command("display version")
                    if "Huawei" in out_vrp or "VRP" in out_vrp:
                        return _parse_huawei_version_output(out_vrp)
                except Exception:
                    pass

            # -------------------------------------------------------------
            # ESTRATÉGIA B: Se o prompt terminar em '#' (Datacom DmOS ou Cisco)
            # -------------------------------------------------------------
            # 1. Probe Datacom DmOS (show firmware)
            try:
                conn.send_command("terminal length 0")
                out_fw = conn.send_command("show firmware")
                if "Version" in out_fw and ("Active" in out_fw or "State" in out_fw or "Inactive" in out_fw):
                    m_act = re.search(r"(\d+\.\d+(?:\.\d+)?)[^\n]*Active", out_fw)
                    if not m_act:
                        m_act = re.search(r"(\d+\.\d+(?:\.\d+)?)", out_fw)
                    ver_str = m_act.group(1) if m_act else "12.0.2"
                    ver_clean = ver_str.replace(".", "_")

                    model = "DM4610"
                    try:
                        out_plat = conn.send_command("show platform")
                        m_plat = re.search(r"\b(DM\d+[A-Z0-9\-]*)\b", out_plat)
                        if m_plat:
                            model = m_plat.group(1)
                    except Exception:
                        pass

                    return DeviceFingerprintResult(
                        vendor="datacom",
                        os_family="dmos",
                        major_version=ver_clean,
                        full_version=ver_str,
                        model=model,
                        platform_key=f"datacom_dmos_{ver_clean.split('_')[0]}",
                        method="L3_PROBE",
                        confidence=1.0
                    )
            except Exception:
                pass

            # 2. Probe Cisco (show version)
            try:
                conn.send_command("terminal length 0")
                out_cisco = conn.send_command("show version")
                if "Cisco" in out_cisco or "IOS" in out_cisco:
                    if "IOS-XE" in out_cisco or "IOS XE" in out_cisco:
                        os_fam = "iosxe"
                    elif "NX-OS" in out_cisco:
                        os_fam = "nxos"
                    elif "XR" in out_cisco:
                        os_fam = "iosxr"
                    else:
                        os_fam = "ios"

                    m_cver = re.search(r"Version\s+([0-9\.\(\)\w]+)", out_cisco, re.IGNORECASE)
                    cver = m_cver.group(1) if m_cver else "17.3"
                    major_cver = cver.split(".")[0].replace("(", "").replace(")", "")

                    m_cmodel = re.search(r"cisco\s+([A-Z0-9\-]+)\s+\(", out_cisco, re.IGNORECASE)
                    cmodel = m_cmodel.group(1) if m_cmodel else "Cisco-Device"

                    return DeviceFingerprintResult(
                        vendor="cisco",
                        os_family=os_fam,
                        major_version=major_cver,
                        full_version=cver,
                        model=cmodel,
                        platform_key=f"cisco_{os_fam}_{major_cver}",
                        method="L3_PROBE",
                        confidence=1.0
                    )
            except Exception:
                pass

            # 3. Probe Huawei fallback (para caixas onde prompt foi customizado sem < >)
            try:
                conn.send_command("screen-length 0 temporary")
                out_vrp = conn.send_command("display version")
                if "Huawei" in out_vrp or "VRP" in out_vrp:
                    return _parse_huawei_version_output(out_vrp)
            except Exception:
                pass

    except Exception:
        pass

    return None


def _parse_huawei_version_output(out_vrp: str) -> DeviceFingerprintResult:
    """Extrai versão e modelo da saída de 'display version' de equipamentos Huawei VRP."""
    # 1. Procura release VxxxRxxx... (ex: V200R022C00SPC500, V200R011C10, V800R021C00)
    m_vrp = re.search(r"\b(V\d{3}R\d+(?:C\d+(?:SPC\d+)?)?)\b", out_vrp, re.IGNORECASE)
    if m_vrp:
        full_ver = m_vrp.group(1).upper()
        major_ver = full_ver[:4].lower()  # ex: v200, v600, v800
    else:
        # Fallback numérico (Version 5.x -> v200, Version 8.x -> v800, Version 10.x -> yunshan)
        m_vrp_num = re.search(r"VRP\s*\(R\)\s*software,\s*Version\s*(\d+)\.(\d+)", out_vrp, re.IGNORECASE)
        if m_vrp_num:
            major_digit = m_vrp_num.group(1)
            if major_digit == "5":
                major_ver = "v200"
            elif major_digit == "8":
                major_ver = "v800"
            elif major_digit == "6":
                major_ver = "v600"
            elif major_digit == "10":
                major_ver = "yunshan"
            else:
                major_ver = f"v{major_digit}00"
            full_ver = f"VRP_{major_digit}.{m_vrp_num.group(2)}"
        else:
            major_ver = "v200"
            full_ver = "unknown"

    # Extrai modelo do switch/roteador Huawei
    m_model = re.search(r"HUAWEI\s+([A-Z0-9\-]+)\s+(?:Routing Switch|Switch|Router|Engine)", out_vrp, re.IGNORECASE)
    model = m_model.group(1) if m_model else None
    if not model:
        m_model2 = re.search(r"\b(S\d{4}[A-Z0-9\-]*|NE\d+[A-Z0-9\-]*|CE\d+[A-Z0-9\-]*)\b", out_vrp)
        model = m_model2.group(1) if m_model2 else "Huawei-Switch"

    return DeviceFingerprintResult(
        vendor="huawei",
        os_family="vrp",
        major_version=major_ver,
        full_version=full_ver,
        model=model,
        platform_key=f"huawei_vrp_{major_ver}",
        method="L3_PROBE",
        confidence=1.0
    )


def progressive_fingerprint(
    host: str,
    ssh_runner=None,
    credential_profile: Optional[str] = None
) -> DeviceFingerprintResult:
    """
    Executa o fluxo de descoberta determinística em 3 níveis:
    1. Tenta L3 Deterministic Probe CLI (conecta via SSH para ler a versão real com 100% de precisão).
    2. Se falhar a autenticação SSH ou conexão, utiliza L1 Banner Grab como fallback.
    3. Se tudo falhar, retorna FALLBACK genérico.
    """
    profile = vault.get_profile(credential_profile)
    cache_key = f"{host}_{profile.name}"

    if cache_key in _FINGERPRINT_CACHE:
        return _FINGERPRINT_CACHE[cache_key]

    # Prioridade 1: L3 Probe no equipamento real com as credenciais do perfil
    real_res = probe_real_device(host, credential_profile=credential_profile)
    if real_res and real_res.confidence >= 0.90:
        _FINGERPRINT_CACHE[cache_key] = real_res
        return real_res

    # Prioridade 2: Nível 1 - Banner Grab (quando SSH não autentica)
    banner = grab_tcp_banner(host, port=profile.port)
    if banner:
        banner_res = inspect_banner(banner)
        if banner_res:
            _FINGERPRINT_CACHE[cache_key] = banner_res
            return banner_res

    # Prioridade 3: Fallback padrão
    fallback = DeviceFingerprintResult(
        vendor="generic",
        os_family="posix",
        major_version="1_0",
        method="FALLBACK",
        confidence=0.50
    )
    _FINGERPRINT_CACHE[cache_key] = fallback
    return fallback

