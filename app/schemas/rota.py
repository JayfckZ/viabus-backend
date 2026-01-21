from pydantic import BaseModel


class RotaBase(BaseModel):
    cidade_origem: str
    cidade_destino: str
    distancia_km: int | None = None
    tempo_estimado_min: int | None = None


class RotaCreate(RotaBase):
    pass


class RotaResponse(RotaBase):
    id: int

    class Config:
        from_attributes = True
