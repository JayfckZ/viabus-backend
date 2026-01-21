from pydantic import BaseModel
from datetime import datetime


class ReservaAssentoBase(BaseModel):
    viagem_id: int
    numero_assento: int
    sessao_id: str
    expira_em: datetime


class ReservaAssentoCreate(ReservaAssentoBase):
    pass


class ReservaAssentoResponse(ReservaAssentoBase):
    id: int

    class Config:
        from_attributes = True
