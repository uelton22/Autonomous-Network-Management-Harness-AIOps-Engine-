"""
mcp_server/cli_error_detector.py
Motor de Detecção, Extração e Classificação de Erros de CLI em Comandos de Configuração.
Inspeciona saídas de equipamentos Cisco, Datacom e Huawei para identificar rejeições de comando,
erros de sintaxe, sobreposição de sub-redes (% Overlaps), falhas de commit e parâmetros inválidos.
"""

import re
from typing import Dict, Any, List, Optional


# Padrões de linhas informacionais da Cisco que começam com % mas NÃO são erros de configuração
CISCO_INFO_PATTERNS = [
    re.compile(r"^%SYS-\d+", re.IGNORECASE),
    re.compile(r"^%LINK-\d+", re.IGNORECASE),
    re.compile(r"^%LINEPROTO-\d+", re.IGNORECASE),
    re.compile(r"^%SSH-\d+", re.IGNORECASE),
    re.compile(r"^%BGP-\d+", re.IGNORECASE),
    re.compile(r"^%OSPF-\d+", re.IGNORECASE),
]

# Padrões explícitos de erro da Cisco
CISCO_ERROR_PATTERNS = [
    re.compile(r"%\s*Invalid\s+input\s+detected\s+at\s+'\^'\s*marker", re.IGNORECASE),
    re.compile(r"%\s*Incomplete\s+command", re.IGNORECASE),
    re.compile(r"%\s*Ambiguous\s+command", re.IGNORECASE),
    re.compile(r"%\s*\d+\.\d+\.\d+\.\d+.*overlaps\s+with", re.IGNORECASE),
    re.compile(r"%\s*Authorization\s+failed", re.IGNORECASE),
    re.compile(r"%\s*Configuration\s+failed", re.IGNORECASE),
    re.compile(r"%\s*Failed\s+to", re.IGNORECASE),
    re.compile(r"%\s*Error\b", re.IGNORECASE),
    re.compile(r"%\s*Bad\s+IP\s+address", re.IGNORECASE),
    re.compile(r"%\s*Subnet\s+masks\s+must\s+match", re.IGNORECASE),
    re.compile(r"%\s*Command\s+rejected", re.IGNORECASE),
    re.compile(r"%\s*Cannot\s+", re.IGNORECASE),
    re.compile(r"%\s*Duplicate\s+", re.IGNORECASE),
]

# Padrões explícitos de erro da Datacom DmOS
DATACOM_ERROR_PATTERNS = [
    re.compile(r"^Error:\s+.*", re.IGNORECASE),
    re.compile(r"^%\s*Error:\s+.*", re.IGNORECASE),
    re.compile(r"syntax\s+error:\s+.*", re.IGNORECASE),
    re.compile(r"Commit\s+failed.*", re.IGNORECASE),
    re.compile(r"Failed\s+to\s+.*", re.IGNORECASE),
    re.compile(r"Incomplete\s+command", re.IGNORECASE),
    re.compile(r"Ambiguous\s+command", re.IGNORECASE),
    re.compile(r"Unknown\s+command", re.IGNORECASE),
    re.compile(r"Command\s+rejected", re.IGNORECASE),
    re.compile(r"Value\s+out\s+of\s+range", re.IGNORECASE),
    re.compile(r"Already\s+exists", re.IGNORECASE),
    re.compile(r"Not\s+found", re.IGNORECASE),
]

# Padrões explícitos de erro da Huawei VRP
HUAWEI_ERROR_PATTERNS = [
    re.compile(r"^Error:\s+.*", re.IGNORECASE),
    re.compile(r"Unrecognized\s+command\s+found\s+at\s+'\^'\s*position", re.IGNORECASE),
    re.compile(r"Wrong\s+parameter\s+found\s+at\s+'\^'\s*position", re.IGNORECASE),
    re.compile(r"Incomplete\s+command\s+found\s+at\s+'\^'\s*position", re.IGNORECASE),
    re.compile(r"Too\s+many\s+parameters\s+found\s+at\s+'\^'\s*position", re.IGNORECASE),
    re.compile(r"Ambiguous\s+command\s+found\s+at\s+'\^'\s*position", re.IGNORECASE),
    re.compile(r"The\s+command\s+was\s+not\s+found", re.IGNORECASE),
    re.compile(r"Failed\s+to\s+commit", re.IGNORECASE),
    re.compile(r"Can\s+not\s+configure", re.IGNORECASE),
    re.compile(r"The\s+port\s+is\s+already", re.IGNORECASE),
    re.compile(r"Already\s+exists", re.IGNORECASE),
]


def _normalize_vendor(platform_type: str) -> str:
    p = (platform_type or "").lower().strip()
    if any(x in p for x in ["cisco", "ios"]):
        return "cisco"
    if any(x in p for x in ["datacom", "dmos"]):
        return "datacom"
    if any(x in p for x in ["huawei", "vrp"]):
        return "huawei"
    return "generic"


def inspect_cli_output(output: str, platform_type: str = "generic") -> Dict[str, Any]:
    """
    Analisa a saída textual retornada pelo equipamento após execução de comandos.
    
    Retorna:
    {
        "is_success": True / False,
        "has_errors": True / False,
        "errors": ["% 10.0.0.0 overlaps with Vlan100", ...],
        "warnings": [...],
        "clean_summary": "Configuração aplicada sem erros detectados." ou resumo do erro
    }
    """
    if not output:
        return {
            "is_success": True,
            "has_errors": False,
            "errors": [],
            "warnings": [],
            "clean_summary": "Saída vazia recebida do equipamento."
        }

    vendor = _normalize_vendor(platform_type)
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    
    detected_errors: List[str] = []
    detected_warnings: List[str] = []

    for line in lines:
        # 1. Regras para Cisco
        if vendor == "cisco" or vendor == "generic":
            # Descarta informacionais (ex: %SYS-5-CONFIG_I)
            if any(info_pat.search(line) for info_pat in CISCO_INFO_PATTERNS):
                continue
            # Testa erros conhecidos
            if any(err_pat.search(line) for err_pat in CISCO_ERROR_PATTERNS):
                if line not in detected_errors:
                    detected_errors.append(line)
                continue
            # Linhas que iniciam com % genéricas que não foram descartadas
            if line.startswith("% ") and not any(p.search(line) for p in CISCO_INFO_PATTERNS):
                if line not in detected_errors:
                    detected_errors.append(line)
                continue

        # 2. Regras para Datacom
        if vendor == "datacom" or vendor == "generic":
            if any(err_pat.search(line) for err_pat in DATACOM_ERROR_PATTERNS):
                if line not in detected_errors:
                    detected_errors.append(line)
                continue

        # 3. Regras para Huawei
        if vendor == "huawei" or vendor == "generic":
            if any(err_pat.search(line) for err_pat in HUAWEI_ERROR_PATTERNS):
                if line not in detected_errors:
                    detected_errors.append(line)
                continue
            # Huawei 'Warning:' ou 'Info:' informacional
            if line.startswith("Warning:") or "is not recommended" in line.lower():
                if line not in detected_warnings:
                    detected_warnings.append(line)

    has_errors = len(detected_errors) > 0
    is_success = not has_errors

    if is_success:
        summary = "Configuração enviada sem erros detectados pela CLI."
        if detected_warnings:
            summary += f" ({len(detected_warnings)} aviso(s) detectado(s))"
    else:
        summary = f"Falha na configuração: {len(detected_errors)} erro(s) retornado(s) pelo equipamento: {'; '.join(detected_errors[:2])}"

    return {
        "is_success": is_success,
        "has_errors": has_errors,
        "errors": detected_errors,
        "warnings": detected_warnings,
        "clean_summary": summary
    }
