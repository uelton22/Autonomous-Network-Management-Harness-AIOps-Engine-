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
        if not schema_def:
            # Resolve ação canônica -> arquivo em registry/schemas/
            for candidate in (
                f"registry/schemas/{action}.json",
                f"registry/schemas/{action.removeprefix('get_')}.json",
            ):
                schema_def = get_json_schema_definition(candidate)
                if schema_def:
                    break
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

        summary: Dict[str, Any] = {"total_records": len(clean_records)}
        if target_list_prop == "pseudowires":
            groups = {r.get("group") for r in clean_records if r.get("group")}
            summary = {
                "total_groups": len(groups),
                "total_pseudowires": len(clean_records),
            }
        elif target_list_prop == "vlans":
            # Deduplica por vlan_id (membership expandido pode repetir)
            dedup: Dict[Any, Dict[str, Any]] = {}
            for r in clean_records:
                vid = r.get("vlan_id")
                if vid is None:
                    continue
                if vid not in dedup:
                    dedup[vid] = r
            clean_records = list(dedup.values())
            summary = {"total_vlans": len(clean_records)}
        elif target_list_prop == "interfaces" and action == "get_l3_interfaces":
            for r in clean_records:
                # Normaliza códigos de tipo de endereço DmOS
                at = str(r.get("address_type", "")).upper()
                if at in ("P", "PRIMARY"):
                    r["address_type"] = "primary"
                elif at in ("S", "SECONDARY"):
                    r["address_type"] = "secondary"
                elif "V" in at:
                    r["address_type"] = "vrrp" if at == "V" else "primary+vrrp"
                st = str(r.get("state", r.get("oper_status", ""))).lower()
                if st in ("active", "up"):
                    r["oper_status"] = "UP"
                elif st in ("inactive", "down"):
                    r["oper_status"] = "DOWN"
                r.pop("state", None)
            unique_names = {r.get("name") for r in clean_records if r.get("name")}
            summary = {
                "total_interfaces": len(unique_names),
                "total_addresses": len(clean_records),
            }
        elif target_list_prop == "neighbors":
            for r in clean_records:
                st = str(r.get("state", "")).lower()
                if st in ("full", "2way", "2-way"):
                    r["state"] = "FULL" if "full" in st else "2-WAY"
            full_n = sum(1 for r in clean_records if str(r.get("state", "")).upper() == "FULL")
            summary = {
                "total_neighbors": len(clean_records),
                "full_neighbors": full_n,
            }
        elif target_list_prop == "processes":
            for r in clean_records:
                for k in ("admin_status", "oper_status"):
                    if k in r:
                        v = str(r[k]).lower()
                        r[k] = "UP" if v in ("up", "enable", "enabled", "active") else ("DOWN" if v in ("down", "disable", "disabled") else r[k])
                for bk in ("area_border_router", "as_border_router", "opaque_lsa_support"):
                    if bk in r:
                        v = str(r[bk]).lower()
                        r[bk] = v in ("yes", "true", "enable", "enabled")
            summary = {"total_processes": len(clean_records)}
        elif target_list_prop == "interfaces" and action == "get_ospf_interfaces":
            summary = {"total_interfaces": len(clean_records)}

        return {
            "device": device_hostname,
            "summary": summary,
            target_list_prop: clean_records,
            "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }
