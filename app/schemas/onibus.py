from pydantic import BaseModel


class OnibusBase(BaseModel):
    empresa_id: int
    placa: str
    model: str | None = None
    tipo_layout_assentos: str | None = None
    total_assentos: int | None = None


class OnibusCreate(OnibusBase):
    pass


class OnibusResponse(OnibusBase):
    id: int

    class Config:
        from_attributes = True
