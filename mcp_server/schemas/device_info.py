"""
mcp_server/schemas/device_info.py
Schema Canônico OpenConfig para Versão, Hardware, Modelo e Uptime.
"""

from typing import Optional
from pydantic import BaseModel, Field


class DeviceInfoSchema(BaseModel):
    hostname: str = Field(description="Nome ou IP do equipamento")
    vendor: str = Field(description="Fabricante (huawei, datacom, cisco, etc.)")
    model: Optional[str] = Field(default="N/A", description="Modelo de hardware identificado")
    os_family: str = Field(description="Família do sistema operacional (vrp, dmos, ios, ios-xe, etc.)")
    os_version: str = Field(description="Versão de firmware ou software")
    patch_version: Optional[str] = Field(default=None, description="Patch ou release build")
    serial_number: Optional[str] = Field(default=None, description="Número de série do chassi")
    uptime_seconds: Optional[int] = Field(default=0, description="Uptime em segundos")
    uptime_str: Optional[str] = Field(default=None, description="Uptime em formato legível")
