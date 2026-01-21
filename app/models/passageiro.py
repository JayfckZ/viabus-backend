from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Passageiro(Base):
    __tablename__ = "passageiros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    documento = Column(String, nullable=False)
    email = Column(String)
    telefone = Column(String)
