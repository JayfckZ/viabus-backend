from pydantic import BaseModel


class PassageiroBase(BaseModel):
    nome: str
    documento: str
    email: str | None = None
    telefone: str | None = None


class PassageiroCreate(PassageiroBase):
    pass


class PassageiroResponse(PassageiroBase):
    id: int

    class Config:
        from_attributes = True
