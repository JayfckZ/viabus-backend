from pydantic import BaseModel
from datetime import datetime


class ViagemBase(BaseModel):
    rota_id: int
    onibus_id: int
    data_hora_partida: datetime
    numero_plataforma: int | None = None
    status: str | None = "agendado"


class ViagemCreate(ViagemBase):
    pass


class ViagemResponse(ViagemBase):
    id: int

    class Config:
        from_attributes = True
