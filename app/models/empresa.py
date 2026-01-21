from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    telefone = Column(String, nullable=False)
