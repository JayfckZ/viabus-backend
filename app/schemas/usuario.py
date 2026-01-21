from pydantic import BaseModel
from datetime import datetime


class UsuarioBase(BaseModel):
    nome: str
    email: str
    cargo: str


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioResponse(UsuarioBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True
