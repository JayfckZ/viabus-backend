from pydantic import BaseModel
from datetime import datetime


class PassagemBase(BaseModel):
    viagem_id: int
    passageiro_id: int
    numero_assento: int
    preco: float
    status: str | None = "ativo"


class PassagemCreate(PassagemBase):
    pass


class PassagemResponse(PassagemBase):
    id: int
    comprado_em: datetime | None = None
    qr_code: str | None = None

    class Config:
        from_attributes = True
