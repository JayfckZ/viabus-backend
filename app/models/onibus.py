from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.enums.tipo_onibus import TipoOnibus


class Onibus(Base):
    __tablename__ = "onibus"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)
    placa = Column(String, nullable=False)
    modelo = Column(String)
    tipo_layout_assentos = Column(
        SqlEnum(TipoOnibus, name="tipo_layout_assentos"), nullable=False
    )
    total_assentos = Column(Integer)

    empresa = relationship("Empresa", backref="onibus")
    viagens = relationship("Viagem", backref="onibus")
