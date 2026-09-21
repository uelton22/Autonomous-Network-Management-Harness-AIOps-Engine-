"""
mcp_server/ttp_engine.py
Motor do Pipeline Híbrido de Parsing TTP (Tier 1 < 5ms, Tier 2 Auto-Cura LLM, Tier 3 Pydantic)
e Orquestrador de Workflows DAG com Agregação Canônica OpenConfig.
"""

import os
import re
import json
import time
from pathlib import Path
from typing import Dict, Any, List, Optional, Type
from ttp import ttp
from pydantic import BaseModel, Field, ValidationError


# -------------------------------------------------------------------------
# SCHEMAS PYDANTIC E NORMALIZADORES MODULARES (TIER 3: OpenConfig Aligned)
# -------------------------------------------------------------------------

from mcp_server.schemas import (
    ACTION_SCHEMA_MAP,
    get_schema_for_action,
    DeviceInfoSchema,
    InterfacesSchema,
    InterfaceDetailItem,
    InterfaceSummaryStats,
    LinkAggregationSchema,
    LagItem,
    LagMemberItem,
    LagSummaryStats,
    BgpSummarySchema,
    BgpPeerItem,
    LLDPNeighborsSchema,
    LLDPNeighborItem,
)
from mcp_server.normalizers import normalize_records_pipeline



# -------------------------------------------------------------------------
# CHUNK SAMPLING (Para nunca enviar arquivos gigantes à LLM)
# -------------------------------------------------------------------------

def extract_representative_sample(raw_text: str, max_lines: int = 50) -> str:
    """
    Isola o cabeçalho (15 linhas), um miolo com repetições e o rodapé (10 linhas)
    para fornecer à LLM apenas a estrutura sintática sem gastar tokens com dumps gigantes.
    """
    lines = [line for line in raw_text.splitlines() if line.strip()]
    total_lines = len(lines)

    if total_lines <= max_lines:
        return raw_text

    head_size = 15
    tail_size = 10
    body_budget = max_lines - (head_size + tail_size)

    pattern = re.compile(
        r"^(\S+\s+\d+|\w+Ethernet\S*|interface\s+\S+|Chassis|Slot|Neighbor|BGP)",
        re.IGNORECASE
    )
    matching_indices = [idx for idx, line in enumerate(lines) if pattern.match(line.strip())]

    sampled_body = []
    if matching_indices:
        start = matching_indices[0]
        sampled_body = lines[start: min(start + body_budget, total_lines)]
    else:
        mid = total_lines // 2
        sampled_body = lines[mid: mid + body_budget]

    return (
        "\n".join(lines[:head_size])
        + "\n\n... [ESTRUTURA REPETITIVA OMITIDA PARA ECONOMIA DE TOKENS] ...\n\n"
        + "\n".join(sampled_body)
        + "\n\n... [FINAL DO DUMP] ...\n\n"
        + "\n".join(lines[-tail_size:])
    )


# -------------------------------------------------------------------------
# BUILT-IN CANONICAL TTP TEMPLATES (Templates de Referência por Fabricante)
# -------------------------------------------------------------------------

def get_builtin_ttp_template(action: str, vendor_os: str) -> str:
    """Retorna templates TTP de referência calibrados para cada fabricante/SO."""
    vos = vendor_os.lower()

    if action == "get_system_version":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="info">
Firmware version : {{ os_version }}
Release date     : {{ release_date | ORPHRASE }}
Active bank      : {{ active_bank }}
Status           : {{ status | ORPHRASE }}
</group>
<group name="info">
{{ os_version }} {{ state | contains('Active') }}
</group>
"""
        elif "vrp" in vos or "huawei" in vos:
            return """<group name="info">
Huawei Versatile Routing Platform Software
VRP (R) software, Version {{ os_version }} ({{ model | ORPHRASE }})
HUAWEI {{ hostname }} uptime is {{ uptime_str | ORPHRASE }}
Patch Version: {{ patch_version }}
Hardware Model       : {{ hardware_model | ORPHRASE }}
</group>
"""

    elif action == "get_hardware_model":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="info">
{{ chassis_slot | exclude('-') }} {{ model }} - - {{ fw | ORPHRASE }}
</group>
<group name="info">
{{ chassis_slot | exclude('-') }} {{ model }} {{ role }} {{ status }} {{ fw | ORPHRASE }}
</group>
<group name="info">
 Product model       : {{ model }}
</group>
<group name="info">
   Part number       : {{ part_number }}
   Serial number     : {{ serial_number }}
   Product revision  : {{ product_revision }}
   PCB revision      : {{ pcb_revision }}
   Hardware version  : {{ hardware_version }}
</group>
"""
        elif "vrp" in vos or "huawei" in vos:
            return """<group name="info">
{{ chassis_slot }} {{ model }} {{ status }}
</group>
"""

    elif action == "get_system_uptime":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="info">
System Uptime : {{ uptime_str | ORPHRASE }}
</group>
<group name="info">
 {{ time }} up {{ uptime_str | ORPHRASE }}, {{ users }} user, load average: {{ load | ORPHRASE }}
</group>
"""
        elif "vrp" in vos or "huawei" in vos:
            return """<group name="info">
HUAWEI {{ hostname }} uptime is {{ uptime_str | ORPHRASE }}
</group>
"""

    elif action == "get_interface_summary":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="interfaces">
{{ name | exclude('ID') }}    {{ oper_status }}    {{ shutdown }}     {{ speed }}     {{ duplex }}    {{ disabled_by }}         {{ blocked_by }}        {{ lag }}   {{ description | ORPHRASE }}
</group>
<group name="interfaces">
{{ name | exclude('ID') }}    {{ oper_status }}    {{ shutdown }}     {{ speed }}     {{ duplex }}    {{ disabled_by }}         {{ blocked_by }}        {{ lag }}
</group>
<group name="interfaces">
{{ name }} {{ admin_status }} {{ oper_status }} {{ speed }} {{ duplex }} {{ type }} {{ description | ORPHRASE }}
</group>
"""
        elif "vrp" in vos or "huawei" in vos:
            return """<group name="interfaces">
{{ name | exclude("Interface") | exclude(":") }} {{ admin_status }} {{ oper_status }} {{ description | ORPHRASE }}
</group>
<group name="interfaces">
{{ name | exclude("Interface") | exclude(":") }} {{ admin_status }} {{ oper_status }}
</group>
<group name="interfaces">
{{ name }} {{ ip_address }} {{ admin_status }} {{ oper_status }} {{ vpn }}
</group>
"""

    elif action == "get_interface_detail":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="detail">
Interface {{ name }} is {{ admin_status }}, line protocol is {{ oper_status }}
  Hardware is {{ hardware | ORPHRASE }}, address is {{ mac_address }}
  Description: {{ description | ORPHRASE }}
  MTU {{ mtu }} bytes, BW {{ speed_bps }} Kbit/sec
  Last link flap: {{ last_flapped | ORPHRASE }}
    {{ in_errors | DIGIT }} input errors, {{ in_crc_errors | DIGIT }} CRC errors
    {{ out_errors | DIGIT }} output errors, {{ in_discards | DIGIT }} discards
</group>
"""
        elif "vrp" in vos or "huawei" in vos:
            return """<group name="detail">
{{ name }} current state : {{ admin_status }}
Line protocol current state : {{ oper_status }}
Description: {{ description | ORPHRASE }}
The Maximum Transmit Unit is {{ mtu }}
Internet Address is {{ ip_address }}
Hardware address is {{ mac_address }}
Last link flapped: {{ last_flapped | ORPHRASE }}
  {{ in_errors | DIGIT }} input errors, {{ in_crc_errors | DIGIT }} CRC errors
  {{ out_errors | DIGIT }} output errors, {{ in_discards | DIGIT }} discards
</group>
"""

    elif action == "get_bgp_summary":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="peers">
{{ peer_ip }} {{ version }} {{ remote_as }} {{ msg_rcvd }} {{ msg_sent }} {{ tbl_ver }} {{ in_q }} {{ out_q }} {{ uptime }} {{ prefixes_received }}
</group>
"""
        elif "vrp" in vos or "huawei" in vos:
            return """<group name="peers">
  {{ peer_ip }} {{ version }} {{ remote_as }} {{ msg_rcvd }} {{ msg_sent }} {{ out_q }} {{ uptime }} {{ state }} {{ prefixes_received }}
</group>
"""

    elif action == "get_lldp_neighbors":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="neighbors">
{{ local_interface | exclude('LOCAL') }}  {{ neighbor_id }}  {{ chassis_subtype }}  {{ chassis_id }}  {{ system_name }}  {{ system_description | ORPHRASE }}  {{ caps_supp }}  {{ caps_en }}  {{ port_subtype }}  {{ port_id }}  {{ port_description | ORPHRASE }}
</group>
<group name="neighbors">
{{ local_interface | exclude('LOCAL') }}  {{ neighbor_id }}  {{ chassis_subtype }}  {{ chassis_id }}  {{ system_name }}  {{ port_id }}  {{ port_description | ORPHRASE }}
</group>
"""
        elif "vrp" in vos or "huawei" in vos:
            return """<group name="neighbors">
{{ local_interface | exclude('Local') }}  {{ system_name }}  {{ port_id }}  {{ holdtime }}
</group>
"""
        elif "cisco" in vos or "ios" in vos:
            return """<group name="neighbors">
{{ system_name | exclude('Device') }}  {{ local_interface }}  {{ holdtime }}  {{ caps }}  {{ port_id }}
</group>
"""

    elif action == "get_link_aggregation":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="aggregations">
{{ lag_id | DIGIT }} {{ interface }} {{ oper_status }} {{ aggregation_status }} {{ lacp_status }}
</group>
<group name="aggregations">
  {{ interface }} {{ oper_status }} {{ aggregation_status }} {{ lacp_status }}
</group>
<group name="aggregations">
{{ interface | exclude('ID') }}    {{ oper_status }}    {{ shutdown }}     {{ speed }}     {{ duplex }}    {{ disabled_by }}         {{ blocked_by }}        lag-{{ lag_id | DIGIT }}   {{ description | ORPHRASE }}
</group>
<group name="aggregations">
{{ interface | exclude('ID') }}    {{ oper_status }}    {{ shutdown }}     {{ speed }}     {{ duplex }}    {{ disabled_by }}         {{ blocked_by }}        lag-{{ lag_id | DIGIT }}
</group>
<group name="aggregations">
{{ lag_id | DIGIT }} {{ oper_status }} {{ mode }} {{ snmp_ifindex }} {{ description | ORPHRASE }}
</group>
<group name="aggregations">
{{ lag_id | DIGIT }} {{ oper_status }} {{ mode }} {{ snmp_ifindex }}
</group>
"""

        elif "vrp" in vos or "huawei" in vos:
            return """<group name="aggregations">
Eth-Trunk{{ lag_id | DIGIT }}'s state information is:
WorkingMode: {{ mode }}
Operate status: {{ oper_status }}
<group name="members">
{{ interface }}  {{ port_status }}  {{ weight }}
</group>
</group>
"""
        elif "cisco" in vos or "ios" in vos:
            return """<group name="aggregations">
{{ lag_id | DIGIT }}  Po{{ port_channel_id }}({{ oper_status }})  {{ protocol }}  {{ members | ORPHRASE }}
</group>
"""

    elif action == "get_system_users":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="users" default="N/A">
aaa user {{ username }}
 password {{ password_hash }}
 group {{ group }}
! {{ _exact_ }}
</group>
"""
        elif "vrp" in vos or "huawei" in vos:
            return """<group name="users">
  {{ username | exclude('User-name') | exclude('Total') }} {{ state }} {{ auth_mask }} {{ admin_level }}
</group>
<group name="users">
{{ username | exclude('User-name') | exclude('Total') }} {{ state }} {{ auth_mask }} {{ admin_level }}
</group>
<group name="users">
  local-user {{ username }} password {{ password_type }} {{ password_hash }}
  local-user {{ username }} privilege level {{ privilege_level }}
  local-user {{ username }} service-type {{ service_type }}
</group>
"""
        elif "cisco" in vos or "ios" in vos:
            return """<group name="users" default="N/A">
username {{ username }} privilege {{ privilege_level }} secret {{ password_hash }}
username {{ username }} secret {{ password_hash }}
</group>
"""

    elif action == "get_active_sessions":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="sessions">
*{{ session_id }} {{ username }} {{ context }} {{ source_ip }} {{ protocol }} {{ login_time }} {{ mode }}
</group>
<group name="sessions">
 {{ session_id }} {{ username }} {{ context }} {{ source_ip }} {{ protocol }} {{ login_time }} {{ mode }}
</group>
"""
        elif "vrp" in vos or "huawei" in vos:
            return """<group name="sessions">
{{ is_current | contains('+') }} {{ session_id }} {{ context }} {{ context_num }} {{ delay }} {{ protocol }} {{ source_ip }} {{ authen_status }} {{ author_cmd }} Username : {{ username }}
</group>
<group name="sessions">
  {{ session_id }} {{ context }} {{ context_num }} {{ delay }} {{ protocol }} {{ source_ip }} {{ authen_status }} {{ author_cmd }} Username : {{ username }}
</group>
<group name="sessions">
{{ session_id }} {{ context }} {{ context_num }} {{ delay }} {{ protocol }} {{ source_ip }} {{ authen_status }} {{ author_cmd }} Username : {{ username }}
</group>
<group name="sessions">
  {{ session_id }} {{ is_current | contains('*') }} {{ mode }} {{ delay }} {{ username }} {{ source_ip }}
</group>
"""
        elif "cisco" in vos or "ios" in vos:
            return """<group name="sessions">
  {{ session_id }} {{ is_current | contains('*') }} {{ line }} {{ username }} {{ idle }} {{ location }}
</group>
"""

    elif action == "get_ospf_neighbors":
        if "dmos" in vos or "datacom" in vos:
            return """<group name="neighbors">
{{ router_id }} {{ priority | DIGIT }} {{ state }} {{ dr_state }} {{ address }} {{ local_interface }}
</group>
<group name="neighbors">
{{ router_id }} {{ priority | DIGIT }} {{ state }} {{ dead_time }} {{ address }} {{ local_interface }}
</group>
"""
        elif "vrp" in vos or "huawei" in vos:
            return """<group name="neighbors">
 {{ area }} {{ local_interface }} {{ router_id }} {{ state }}
</group>
<group name="neighbors">
 Area {{ area }} interface {{ local_ip }}({{ local_interface }})'s neighbors
 Router ID: {{ router_id }} Address: {{ address }}
</group>
"""
        elif "cisco" in vos or "ios" in vos:
            return """<group name="neighbors">
{{ router_id }} {{ priority | DIGIT }} {{ state }} {{ dead_time }} {{ address }} {{ local_interface }}
</group>
"""

    return "<group name=\"data\">\n{{ line | ORPHRASE }}\n</group>\n"



# -------------------------------------------------------------------------
# TTP HYBRID ENGINE & WORKFLOW ORCHESTRATOR
# -------------------------------------------------------------------------

class TTPHybridEngine:
    """Motor de Parsing Híbrido com cache Tier 1, auto-cura Tier 2 e validação Tier 3."""

    def __init__(self, template_dir: str = "storage/templates", normalized_storage_dir: str = "storage/normalized"):
        self.template_dir = Path(template_dir)
        self.template_dir.mkdir(parents=True, exist_ok=True)
        self.normalized_storage_dir = Path(normalized_storage_dir)
        self.normalized_storage_dir.mkdir(parents=True, exist_ok=True)

    def _get_template_path(self, action: str, vendor_os: str, version: str) -> Path:
        sanitized_ver = version.lower().replace(".", "_")
        return self.template_dir / action / f"{vendor_os.lower()}__{sanitized_ver}.ttp"

    def save_normalized_json(
        self,
        device_hostname: str,
        action: str,
        data: Dict[str, Any],
        timestamp: Optional[str] = None
    ) -> Path:
        """Salva os dados normalizados em JSON legível no disco para conferência humana e auditoria."""
        if not timestamp:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
        safe_host = re.sub(r"[^a-zA-Z0-9_\-]", "_", device_hostname)
        safe_action = re.sub(r"[^a-zA-Z0-9_\-]", "_", action)
        json_filename = f"{safe_host}_{timestamp}_{safe_action}.json"
        json_filepath = self.normalized_storage_dir / json_filename
        json_filepath.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        return json_filepath

    def execute_local_ttp(self, raw_data: str, template_content: str) -> List[Dict[str, Any]]:
        """Executa TTP determinístico em Python e desempacota grupos aninhados."""
        try:
            parser = ttp(data=raw_data, template=template_content)
            parser.parse()
            res = parser.result()
            if not res or not isinstance(res, list):
                return []
            
            flat = res[0]
            if isinstance(flat, list) and len(flat) == 1 and isinstance(flat[0], dict):
                flat = flat[0]
            elif isinstance(flat, list) and len(flat) > 0 and isinstance(flat[0], list):
                flat = flat[0]

            if isinstance(flat, dict):
                for group_key in ("interfaces", "detail", "info", "peers", "neighbors", "aggregations", "users", "sessions", "data"):
                    if group_key in flat:
                        val = flat[group_key]
                        return val if isinstance(val, list) else [val]
                return [flat]
            elif isinstance(flat, list):
                return flat
            return []
        except Exception:
            return []

    def parse_with_pipeline(
        self,
        action: str,
        vendor: str,
        os_family: str,
        version: str,
        raw_stdout: str,
        device_hostname: str = "device"
    ) -> Dict[str, Any]:
        """
        Executa o pipeline completo:
        Tier 1: Cache de Templates (< 5ms)
        Tier 2: Auto-geração LLM + Sandbox + Loop de Feedback
        Tier 3: Validação Estrita OpenConfig
        Persistência: Grava o JSON normalizado resultante em storage/normalized/ para conferência humana.
        """
        vendor_os = f"{vendor}_{os_family}"
        template_file = self._get_template_path(action, vendor_os, version)
        schema_cls = ACTION_SCHEMA_MAP.get(action)

        # -----------------------------------------------------------------
        # TIER 1: FAST-PATH DETERMINÍSTICO (CACHE HIT < 5ms)
        # -----------------------------------------------------------------
        if template_file.exists():
            template_code = template_file.read_text(encoding="utf-8")
            parsed_records = self.execute_local_ttp(raw_stdout, template_code)
            if parsed_records:
                normalized = self._normalize_records(parsed_records, action, vendor, os_family, version, device_hostname)
                if schema_cls:
                    try:
                        validated = schema_cls.model_validate(normalized)
                        data_dump = validated.model_dump()
                        json_file = self.save_normalized_json(device_hostname, action, data_dump)
                        return {
                            "tier": "Tier 1: Fast-Path Cache (< 5ms)",
                            "cache_hit": True,
                            "json_path": str(json_file.resolve()),
                            "data": data_dump
                        }
                    except ValidationError:
                        pass  # Template do cache desatualizado, prossegue para Tier 2
                else:
                    json_file = self.save_normalized_json(device_hostname, action, normalized)
                    return {
                        "tier": "Tier 1: Fast-Path Cache (< 5ms)",
                        "cache_hit": True,
                        "json_path": str(json_file.resolve()),
                        "data": normalized
                    }

        # -----------------------------------------------------------------
        # TIER 2: AUTO-CURA VIA LLM, SANDBOX E APROVAÇÃO
        # -----------------------------------------------------------------
        sampled_raw = extract_representative_sample(raw_stdout)
        max_retries = 3
        last_error = "Nenhum erro prévio."

        for attempt in range(1, max_retries + 1):
            # Síntese do template (via Gemini ou Built-in Canônico)
            ttp_code = self._synthesize_ttp(action, vendor_os, sampled_raw, schema_cls, last_error)

            # Sandbox de Teste: Executa no .raw integral
            test_records = self.execute_local_ttp(raw_stdout, ttp_code)
            if not test_records:
                last_error = f"Tentativa {attempt}: TTP retornou lista vazia. Variáveis não deram match."
                continue

            normalized = self._normalize_records(test_records, action, vendor, os_family, version, device_hostname)
            if schema_cls:
                try:
                    validated = schema_cls.model_validate(normalized)
                    # SUCESSO: Salva e promove para o cache
                    template_file.parent.mkdir(parents=True, exist_ok=True)
                    template_file.write_text(ttp_code, encoding="utf-8")
                    data_dump = validated.model_dump()
                    json_file = self.save_normalized_json(device_hostname, action, data_dump)

                    return {
                        "tier": f"Tier 2: LLM Auto-Healing (Tentativa {attempt}) -> Promovido para Cache",
                        "cache_hit": False,
                        "json_path": str(json_file.resolve()),
                        "data": data_dump
                    }
                except ValidationError as ve:
                    last_error = f"Tentativa {attempt}: Validação Pydantic falhou: {ve}"
            else:
                # SUCESSO para ação ad-hoc: Salva e promove para o cache
                template_file.parent.mkdir(parents=True, exist_ok=True)
                template_file.write_text(ttp_code, encoding="utf-8")
                json_file = self.save_normalized_json(device_hostname, action, normalized)

                return {
                    "tier": f"Tier 2: LLM Auto-Healing (Tentativa {attempt}) -> Promovido para Cache",
                    "cache_hit": False,
                    "json_path": str(json_file.resolve()),
                    "data": normalized
                }

        raise RuntimeError(f"Falha de parsing após {max_retries} tentativas. Último erro: {last_error}")

    def _synthesize_ttp(
        self,
        action: str,
        vendor_os: str,
        sampled_raw: str,
        schema_cls: Optional[Type[BaseModel]],
        last_error: str
    ) -> str:
        """Gera o template TTP usando Gemini (se chave presente) ou template built-in calibrado."""
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            try:
                from google import genai
                client = genai.Client(api_key=api_key)
                schema_info = json.dumps(schema_cls.model_json_schema(), indent=2) if schema_cls else "{}"
                prompt = f"""
Você é um engenheiro sênior de redes especialista em parsing TTP (Template Text Parser).
Crie um template TTP rigoroso para processar o output CLI de rede abaixo.

SISTEMA OPERACIONAL: {vendor_os}
AÇÃO CANÔNICA: {action}

SAÍDA CLI AMOSTRADA:
{sampled_raw}

SCHEMA JSON ESPERADO:
{schema_info}

FEEDBACK DA TENTATIVA ANTERIOR:
{last_error}

REGRAS ESTREITAS:
1. Retorne APENAS o código do template TTP entre ```ttp ... ```.
2. Utilize tags <group name="..."> adequadas.
3. Garanta que o nome das variáveis TTP coincida com os campos do schema.
"""
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                text = response.text or ""
                if "```ttp" in text:
                    return text.split("```ttp")[1].split("```")[0].strip()
                elif "```" in text:
                    return text.split("```")[1].split("```")[0].strip()
                return text.strip()
            except Exception:
                pass

        # Fallback para template built-in canônico
        return get_builtin_ttp_template(action, vendor_os)

    def _normalize_records(
        self,
        records: List[Dict[str, Any]],
        action: str,
        vendor: str,
        os_family: str,
        version: str,
        device_hostname: str
    ) -> Dict[str, Any]:
        """Converte dicionários brutos do TTP no payload esperado pelo schema OpenConfig via pipeline modular."""
        return normalize_records_pipeline(
            records=records,
            action=action,
            vendor=vendor,
            os_family=os_family,
            version=version,
            device_hostname=device_hostname
        )

