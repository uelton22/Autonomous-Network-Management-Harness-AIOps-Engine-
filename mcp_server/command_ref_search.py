"""
mcp_server/command_ref_search.py
Motor de busca e consulta estruturada para documentação de comandos em command_reference/.
Permite que agentes e ferramentas localizem comandos canônicos, sintaxes exatas,
modos de execução, parâmetros e restrições em milissegundos.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional


class CommandReferenceSearcher:
    """Buscador e indexador em memória para manuais de comandos dos fabricantes."""

    def __init__(self, base_dir: str = "command_reference"):
        self.base_dir = Path(base_dir)
        self._index_cache: Dict[str, List[Dict[str, Any]]] = {}

    def _load_vendor_index(self, vendor: str) -> List[Dict[str, Any]]:
        """Carrega o índice JSON compacto do fabricante."""
        v = vendor.lower()
        if v in self._index_cache:
            return self._index_cache[v]

        vendor_dir = self.base_dir / v
        if not vendor_dir.exists():
            return []

        # Procurar por arquivos de índice (*index.json)
        index_files = list(vendor_dir.glob("*index.json"))
        records: List[Dict[str, Any]] = []

        if index_files:
            for idx_file in index_files:
                try:
                    data = json.loads(idx_file.read_text(encoding="utf-8"))
                    if isinstance(data, list):
                        records.extend(data)
                except Exception:
                    pass
        else:
            # Fallback: se não houver index.json, indexa headers dos arquivos .md em chapters/
            chapters_dir = vendor_dir / "chapters"
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
                                    "file": str(md_file.relative_to(vendor_dir)),
                                    "is_read_command": is_read
                                })
                    except Exception:
                        pass

        self._index_cache[v] = records
        return records

    def search_commands(
        self,
        vendor: str,
        query: str,
        read_only: bool = True,
        category: Optional[str] = None,
        max_results: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Pesquisa comandos por palavra-chave ou termos.
        Filtragem opcional por comandos de leitura (show / display) e categoria.
        """
        index_records = self._load_vendor_index(vendor)
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

    def get_command_details(self, vendor: str, command_name: str) -> Optional[Dict[str, Any]]:
        """
        Recupera os detalhes completos (sintaxe, parâmetros, exemplos, modos)
        do arquivo JSONL ou markdown correspondente.
        """
        v = vendor.lower()
        vendor_dir = self.base_dir / v
        if not vendor_dir.exists():
            return None

        # 1. Tentar localizar no arquivo .jsonl
        jsonl_files = list(vendor_dir.glob("*.jsonl"))
        for j_file in jsonl_files:
            try:
                with open(j_file, "r", encoding="utf-8") as f:
                    for line in f:
                        if not line.strip():
                            continue
                        entry = json.loads(line)
                        if entry.get("command", "").strip().lower() == command_name.strip().lower():
                            return entry
            except Exception:
                pass

        # 2. Tentar fallback no arquivo .md correspondente no índice
        matches = self.search_commands(vendor=v, query=command_name, read_only=False, max_results=1)
        if matches and "file" in matches[0]:
            doc_file = vendor_dir / matches[0]["file"]
            if doc_file.exists():
                return {
                    "command": matches[0].get("command"),
                    "chapter": matches[0].get("chapter"),
                    "file_path": str(doc_file.resolve()),
                    "summary": f"Consulte o arquivo markdown: {doc_file.name}"
                }

        return None
