"""
mcp_server/command_ref_search.py
Motor de busca e consulta estruturada para documentação de comandos em command_reference/.
Permite que agentes e ferramentas localizem comandos canônicos, sintaxes exatas,
modos de execução, parâmetros e restrições em milissegundos.

Suporta:
- Documentação na raiz do vendor: ex: command_reference/datacom/
- Documentação em subpastas de versão: ex: command_reference/huawei/V200R011C10/, V600, V800
- Resolução inteligente de versões (ex: 'v200', 'V200R011', 'v200r011c10', '200')
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class CommandReferenceSearcher:
    """Buscador e indexador em memória para manuais de comandos dos fabricantes com suporte multi-versão."""

    def __init__(self, base_dir: Optional[str] = None):
        self.base_dir = Path(base_dir or (PROJECT_ROOT / "command_reference"))
        self._index_cache: Dict[str, List[Dict[str, Any]]] = {}

    @staticmethod
    def _normalize_vendor(vendor: str) -> str:
        """Normaliza variações e aliases de nomes de fabricantes (ex: cisco_iosxe, ios -> cisco)."""
        v = vendor.lower().strip()
        if any(x in v for x in ["cisco", "ios"]):
            return "cisco"
        if any(x in v for x in ["datacom", "dmos"]):
            return "datacom"
        if any(x in v for x in ["huawei", "vrp"]):
            return "huawei"
        return v

    def list_available_versions(self, vendor: str) -> List[str]:
        """Lista todas as subpastas de versão disponíveis para o fabricante especificado."""
        v = self._normalize_vendor(vendor)
        vendor_dir = self.base_dir / v
        if not vendor_dir.exists():
            return []

        subdirs = [
            d.name for d in vendor_dir.iterdir()
            if d.is_dir() and not d.name.startswith(".") and d.name.lower() != "chapters"
        ]
        return sorted(subdirs)

    def _get_target_dirs(self, vendor: str, version: Optional[str] = None) -> List[Tuple[str, Path]]:
        """
        Retorna a lista de tuplas (version_tag, directory_path) correspondentes.
        Se version for especificado, busca correspondência exata ou por prefixo.
        Se não especificado, retorna todas as versões disponíveis ou a pasta raiz.
        """
        v = self._normalize_vendor(vendor)
        vendor_dir = self.base_dir / v
        if not vendor_dir.exists():
            return []

        available_versions = self.list_available_versions(v)

        # Caso 1: Existem subpastas de versão (ex: Huawei com V200R011C10, V600, V800)
        if available_versions:
            if version and version.strip():
                ver_clean = re.sub(r"[^a-zA-Z0-9]", "", version).lower()
                matched = []
                # Match 1: substring mútua (ex: 'v200' em 'v200r011c10')
                for v_name in available_versions:
                    v_clean = re.sub(r"[^a-zA-Z0-9]", "", v_name).lower()
                    if ver_clean in v_clean or v_clean in ver_clean:
                        matched.append((v_name, vendor_dir / v_name))
                if matched:
                    return matched

                # Match 2: correspondência numérica maior (ex: '200' em '20001110')
                digits_req = re.sub(r"\D", "", version)
                if digits_req:
                    for v_name in available_versions:
                        digits_avail = re.sub(r"\D", "", v_name)
                        if digits_req in digits_avail or digits_avail.startswith(digits_req):
                            matched.append((v_name, vendor_dir / v_name))
                if matched:
                    return matched

            # Se nenhuma versão foi solicitada ou não houve match estrito, retorna todas as versões disponíveis
            return [(v_name, vendor_dir / v_name) for v_name in available_versions]

        # Caso 2: Não existem subpastas de versão (ex: Cisco ou Datacom direto na raiz da pasta)
        return [("default", vendor_dir)]

    def _load_dir_index(self, version_tag: str, directory: Path) -> List[Dict[str, Any]]:
        """Carrega e anota os índices JSON, JSONL ou markdown de um diretório específico com dados ricos."""
        records: List[Dict[str, Any]] = []

        # 1. Preferência: Arquivos .jsonl completos (contêm descrição, sintaxe, parâmetros e exemplos)
        jsonl_files = list(directory.glob("*.jsonl"))
        if jsonl_files:
            for j_file in jsonl_files:
                try:
                    with open(j_file, "r", encoding="utf-8") as f:
                        for line in f:
                            if not line.strip():
                                continue
                            item = json.loads(line)
                            cmd_name = item.get("command", "")
                            is_read = item.get("is_read_command", False) or cmd_name.startswith("show") or cmd_name.startswith("display")
                            
                            # Sintaxe limpa para busca
                            entry = {
                                "command": cmd_name,
                                "description": item.get("description", "")[:200],  # resumo de busca
                                "syntax": item.get("syntax", ""),
                                "command_mode": item.get("command_mode", ""),
                                "category": item.get("category", ""),
                                "chapter": item.get("chapter", ""),
                                "section": item.get("section", ""),
                                "page": item.get("page", 0),
                                "is_read_command": is_read,
                                "file": item.get("file", f"chapters/{item.get('chapter_num', 0):02d}.md"),
                                "doc_version": version_tag,
                                "file_relative": str((directory / item.get("file", "")).relative_to(self.base_dir)) if "file" in item else ""
                            }
                            records.append(entry)
                    if records:
                        return records
                except Exception:
                    pass

        # 2. Fallback: Arquivos de índice compacto (*index.json)
        index_files = list(directory.glob("*index.json"))
        if index_files:
            for idx_file in index_files:
                try:
                    data = json.loads(idx_file.read_text(encoding="utf-8"))
                    if isinstance(data, list):
                        for item in data:
                            entry = dict(item)
                            entry["doc_version"] = version_tag
                            if "file" in entry:
                                entry["file_relative"] = str((directory / entry["file"]).relative_to(self.base_dir))
                            records.append(entry)
                except Exception:
                    pass
            if records:
                return records

        # 3. Fallback adicional: Arquivos .md em chapters/
        chapters_dir = directory / "chapters"
        if chapters_dir.exists():
            for md_file in chapters_dir.glob("*.md"):
                try:
                    content = md_file.read_text(encoding="utf-8")
                    for line in content.splitlines():
                        if line.startswith("### `") or line.startswith("## `"):
                            cmd_name = line.split("`")[1].strip()
                            is_read = cmd_name.startswith("show") or cmd_name.startswith("display")
                            records.append({
                                "command": cmd_name,
                                "description": "",
                                "syntax": cmd_name,
                                "command_mode": "",
                                "category": "",
                                "chapter": md_file.stem,
                                "section": "",
                                "file": str(md_file.relative_to(directory)),
                                "file_relative": str(md_file.relative_to(self.base_dir)),
                                "is_read_command": is_read,
                                "doc_version": version_tag
                            })
                except Exception:
                    pass

        return records

    def _load_vendor_index(self, vendor: str, version: Optional[str] = None) -> List[Dict[str, Any]]:
        """Carrega o índice JSON compacto do fabricante respeitando a versão solicitada."""
        norm_vendor = self._normalize_vendor(vendor)
        target_dirs = self._get_target_dirs(norm_vendor, version)
        if not target_dirs:
            return []

        records: List[Dict[str, Any]] = []
        for v_tag, v_dir in target_dirs:
            cache_key = f"{norm_vendor}_{v_tag.lower()}"
            if cache_key in self._index_cache:
                records.extend(self._index_cache[cache_key])
            else:
                dir_records = self._load_dir_index(v_tag, v_dir)
                self._index_cache[cache_key] = dir_records
                records.extend(dir_records)

        return records

    def search_commands(
        self,
        vendor: str,
        query: str,
        read_only: bool = True,
        category: Optional[str] = None,
        version: Optional[str] = None,
        max_results: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Pesquisa comandos por palavra-chave ou termos com pontuação de relevância.
        Suporta:
        - Busca em nome do comando, descrição semântica e sintaxe.
        - Fallback inteligente se read_only=True não encontrar resultados.
        - Versão do SO (ex: 'v200', 'V200R011C10', 'v600').
        """
        norm_vendor = self._normalize_vendor(vendor)
        index_records = self._load_vendor_index(norm_vendor, version)
        if not index_records:
            return []

        clean_query = query.lower().strip()
        q_terms = [t for t in clean_query.split() if t]

        def _score_and_filter(rec: Dict[str, Any], enforce_read_only: bool) -> int:
            cmd_name = rec.get("command", "").lower()
            is_read = rec.get("is_read_command", False) or cmd_name.startswith("show") or cmd_name.startswith("display")

            if enforce_read_only and not is_read:
                return -1

            if category and rec.get("category", "").lower() != category.lower():
                return -1

            desc = rec.get("description", "").lower()
            syntax = rec.get("syntax", "").lower()
            chapter = rec.get("chapter", "").lower()
            sec = rec.get("section", "").lower()
            full_text = f"{cmd_name} {syntax} {desc} {chapter} {sec}"

            # Deve conter todos os termos pesquisados em algum lugar do registro
            if not all(term in full_text for term in q_terms):
                return -1

            score = 0
            # Pontuação por correspondência exata no comando
            if cmd_name == clean_query:
                score += 200
            elif cmd_name.startswith(clean_query):
                score += 100
            elif clean_query in cmd_name:
                score += 60

            # Termos individuais no comando
            for term in q_terms:
                if term in cmd_name:
                    score += 25
                if term in syntax:
                    score += 15
                if term in desc:
                    score += 10

            return score

        # 1ª Tentativa: respeitando read_only
        scored_matches = []
        for rec in index_records:
            s = _score_and_filter(rec, enforce_read_only=read_only)
            if s > 0:
                scored_matches.append((s, rec))

        # 2ª Tentativa: se read_only=True retornou 0, faz fallback relaxando read_only para não deixar o operador no vácuo
        if not scored_matches and read_only:
            for rec in index_records:
                s = _score_and_filter(rec, enforce_read_only=False)
                if s > 0:
                    r_copy = dict(rec)
                    r_copy["read_only_fallback"] = True
                    scored_matches.append((s, r_copy))

        # Ordena pelo score decrescente
        scored_matches.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scored_matches[:max_results]]

    def get_command_details(
        self,
        vendor: str,
        command_name: str,
        version: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Recupera os detalhes completos (sintaxe, parâmetros, exemplos, modos)
        do arquivo JSONL ou markdown correspondente, respeitando a versão.
        """
        target_dirs = self._get_target_dirs(vendor, version)
        if not target_dirs:
            return None

        cmd_clean = command_name.strip().lower()

        for v_tag, v_dir in target_dirs:
            # 1. Tentar localizar no arquivo .jsonl
            jsonl_files = list(v_dir.glob("*.jsonl"))
            for j_file in jsonl_files:
                try:
                    with open(j_file, "r", encoding="utf-8") as f:
                        for line in f:
                            if f'"{command_name}"' in line or f'"{cmd_clean}"' in line.lower():
                                entry = json.loads(line)
                                if entry.get("command", "").strip().lower() == cmd_clean:
                                    entry["doc_version"] = v_tag
                                    return entry
                except Exception:
                    pass

            # 2. Tentar fallback no arquivo .md correspondente no índice
            matches = self.search_commands(
                vendor=vendor,
                query=command_name,
                read_only=False,
                version=v_tag,
                max_results=1
            )
            if matches and "file" in matches[0]:
                doc_file = v_dir / matches[0]["file"]
                if doc_file.exists():
                    return {
                        "command": matches[0].get("command"),
                        "chapter": matches[0].get("chapter"),
                        "doc_version": v_tag,
                        "file_path": str(doc_file.resolve()),
                        "summary": f"Consulte o arquivo markdown: {doc_file.name}"
                    }

        return None


# Instância singleton do buscador
_global_searcher: Optional[CommandReferenceSearcher] = None


def get_command_ref_searcher() -> CommandReferenceSearcher:
    """Retorna a instância global singleton do buscador de documentação."""
    global _global_searcher
    if _global_searcher is None:
        _global_searcher = CommandReferenceSearcher()
    return _global_searcher
