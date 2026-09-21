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


class CommandReferenceSearcher:
    """Buscador e indexador em memória para manuais de comandos dos fabricantes com suporte multi-versão."""

    def __init__(self, base_dir: str = "command_reference"):
        self.base_dir = Path(base_dir)
        self._index_cache: Dict[str, List[Dict[str, Any]]] = {}

    def list_available_versions(self, vendor: str) -> List[str]:
        """Lista todas as subpastas de versão disponíveis para o fabricante especificado."""
        v = vendor.lower()
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
        v = vendor.lower()
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

        # Caso 2: Não existem subpastas de versão (ex: Datacom direto na raiz da pasta datacom/)
        return [("default", vendor_dir)]

    def _load_dir_index(self, version_tag: str, directory: Path) -> List[Dict[str, Any]]:
        """Carrega e anota os índices JSON ou markdown de um diretório específico."""
        records: List[Dict[str, Any]] = []

        # 1. Procurar por arquivos de índice (*index.json)
        index_files = list(directory.glob("*index.json"))
        if index_files:
            for idx_file in index_files:
                try:
                    data = json.loads(idx_file.read_text(encoding="utf-8"))
                    if isinstance(data, list):
                        for item in data:
                            entry = dict(item)
                            entry["doc_version"] = version_tag
                            # Garante que o caminho relativo do arquivo aponte a partir da base
                            if "file" in entry:
                                entry["file_relative"] = str((directory / entry["file"]).relative_to(self.base_dir))
                            records.append(entry)
                except Exception:
                    pass
            return records

        # 2. Fallback: Se não houver index.json, indexa headers dos arquivos .md em chapters/
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
                                "chapter": md_file.stem,
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
        target_dirs = self._get_target_dirs(vendor, version)
        if not target_dirs:
            return []

        records: List[Dict[str, Any]] = []
        for v_tag, v_dir in target_dirs:
            cache_key = f"{vendor.lower()}_{v_tag.lower()}"
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
        Pesquisa comandos por palavra-chave ou termos.
        Suporta filtragem por:
        - Privilégio (read_only: show / display)
        - Categoria
        - Versão do SO (ex: 'v200', 'V200R011C10', 'v600')
        """
        index_records = self._load_vendor_index(vendor, version)
        if not index_records:
            return []

        q_terms = [t.lower().strip() for t in query.split() if t.strip()]
        matches: List[Dict[str, Any]] = []

        for rec in index_records:
            # Filtro de privilégio (somente comandos de leitura se read_only=True)
            if read_only and not rec.get("is_read_command", False):
                cmd_name = rec.get("command", "").lower()
                if not (cmd_name.startswith("show") or cmd_name.startswith("display")):
                    continue

            # Filtro de categoria
            if category and rec.get("category", "").lower() != category.lower():
                continue

            cmd_text = f"{rec.get('command', '')} {rec.get('section', '')} {rec.get('chapter', '')} {rec.get('category', '')}".lower()

            if all(term in cmd_text for term in q_terms):
                matches.append(rec)
                if len(matches) >= max_results:
                    break

        return matches

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
