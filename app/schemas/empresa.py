from pydantic import BaseModel


class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    email: str
    telefone: str


class EmpresaCreate(EmpresaBase):
    pass


class EmpresaResponse(EmpresaBase):
    id: int

    class Config:
        from_attributes = True
