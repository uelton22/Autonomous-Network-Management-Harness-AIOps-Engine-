"""
mcp_server/schemas/base.py
Modelos base e classes abstratas para Schemas Canônicos OpenConfig no AIOps Harness.
Garante padronização estrita de metadados, timestamps e serialização sem viés de fabricante.
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field


class OpenConfigBaseSchema(BaseModel):
    """Modelo base para todos os schemas OpenConfig normalizados."""
    device: str = Field(description="Hostname ou IP de gerência do equipamento")
    collected_at: Optional[str] = Field(default=None, description="Timestamp ISO-8601 da telemetria")

    class Config:
        populate_by_name = True
