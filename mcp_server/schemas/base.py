"""
mcp_server/schemas/base.py
Classe base canônica para todos os modelos Pydantic OpenConfig do NetOps Harness.
"""

from typing import Dict, Any, Optional
from pydantic import BaseModel, ConfigDict


class OpenConfigBaseSchema(BaseModel):
    """Modelo base para schemas canônicos OpenConfig."""
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    device: Optional[str] = None
    collected_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Converte o modelo Pydantic para dicionário primitivo limpo."""
        return self.model_dump(exclude_none=False)
