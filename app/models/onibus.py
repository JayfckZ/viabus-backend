from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Onibus(Base):
    __tablename__ = "onibus"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    placa = Column(String, nullable=False)
    modelo = Column(String)
    tipo_layout_assentos = Column(String)
    total_assentos = Column(Integer)

    empresa = relationship("Empresa", backref="onibus")
    viagens = relationship("Viagem", backref="onibus")
