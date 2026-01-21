from pydantic import BaseModel

from app.enums.tipo_onibus import TipoOnibus


class OnibusBase(BaseModel):
    empresa_id: int
    placa: str
    modelo: str | None = None
    tipo_layout_assentos: TipoOnibus
    total_assentos: int | None = None


class OnibusCreate(OnibusBase):
    pass


class OnibusResponse(OnibusBase):
    id: int

    class Config:
        from_attributes = True
