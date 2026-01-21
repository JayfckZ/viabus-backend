from pydantic import BaseModel
from datetime import datetime


class PagamentoBase(BaseModel):
    passagem_id: int
    metodo: str
    status: str
    pago_em: datetime | None = None
    transacao_id: str | None = None


class PagamentoCreate(PagamentoBase):
    pass


class PagamentoResponse(PagamentoBase):
    id: int

    class Config:
        from_attributes = True
