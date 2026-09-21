"""
mcp_server/schemas/device_info.py
Schema Canônico OpenConfig para Informações de Dispositivo (openconfig-platform).
"""

from typing import Optional
from pydantic import BaseModel, Field


class DeviceInfoSchema(BaseModel):
    """Modelo canônico para informações básicas do sistema e hardware."""
    hostname: str = Field(description="Hostname do equipamento ou IP de gerenciamento")
    vendor: str = Field(description="Fabricante detectado (datacom, huawei, cisco)")
    model: str = Field(description="Modelo de hardware identificado")
    os_family: str = Field(description="Família de sistema operacional (dmos, vrp, iosxe)")
    os_version: str = Field(description="Versão principal do sistema operacional ou release")
    patch_version: Optional[str] = Field(default=None, description="Versão de patch aplicada")
    serial_number: Optional[str] = Field(default=None, description="Número de série do chassi")
    uptime_seconds: Optional[int] = Field(default=None, description="Tempo de atividade em segundos")
    uptime_str: Optional[str] = Field(default=None, description="Tempo de atividade em formato legível")
