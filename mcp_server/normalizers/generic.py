"""
mcp_server/normalizers/generic.py
Normalizador Genérico Declarativo orientado a JSON Schema.
Permite normalizar qualquer ação ad-hoc ou recém-sintetizada sem a necessidade
de codificar um normalizador Python dedicado.
"""

import time
from typing import List, Dict, Any, Optional
from mcp_server.schemas.registry import get_json_schema_definition


class GenericOpenConfigNormalizer:
    """Normalizador declarativo baseado no JSON Schema em registry/schemas/."""

    @staticmethod
    def normalize(
        action: str,
        records: List[Dict[str, Any]],
        device_hostname: str
    ) -> Dict[str, Any]:
        schema_def = get_json_schema_definition(action)
        clean_records = []

        for r in records:
            if not isinstance(r, dict):
                continue
            cleaned = {}
            for k, v in r.items():
                if v is None:
                    continue
                if isinstance(v, str):
                    v_str = v.strip()
                    # Mapeamento canônico de status
                    if k.endswith("_status") or k == "status":
                        if "up" in v_str.lower():
                            v_str = "UP"
                        elif "down" in v_str.lower():
                            v_str = "DOWN"
                    # Conversão numérica segura
                    elif v_str.isdigit():
                        cleaned[k] = int(v_str)
                        continue
                    cleaned[k] = v_str
                else:
                    cleaned[k] = v
            if cleaned:
                clean_records.append(cleaned)

        # Identifica a propriedade de lista esperada pelo schema
        target_list_prop = action
        if schema_def and "properties" in schema_def:
            for prop_name, prop_val in schema_def["properties"].items():
                if prop_val.get("type") == "array" and prop_name not in ("summary", "metadata"):
                    target_list_prop = prop_name
                    break

        return {
            "device": device_hostname,
            "summary": {
                "total_records": len(clean_records)
            },
            target_list_prop: clean_records,
            "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }
