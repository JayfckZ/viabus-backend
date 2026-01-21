from pydantic import BaseModel
from datetime import datetime


class RegistroEmbarqueBase(BaseModel):
    passagem_id: int
    verificado_por_usuario_id: int
    verificado_em: datetime | None = None


class RegistroEmbarqueCreate(RegistroEmbarqueBase):
    pass


class RegistroEmbarqueResponse(RegistroEmbarqueBase):
    id: int

    class Config:
        from_attributes = True
