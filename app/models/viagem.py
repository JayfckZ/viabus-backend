from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


class Viagem(Base):
    __tablename__ = "viagens"

    id = Column(Integer, primary_key=True, index=True)
    rota_id = Column(Integer, ForeignKey("rotas.id"), nullable=False)
    onibus_id = Column(Integer, ForeignKey("onibus.id"), nullable=False)
    data_hora_partida = Column(DateTime, nullable=False)
    numero_plataforma = Column(Integer)
    status = Column(String, default="agendado")

    rota = relationship("Rota", backref="viagens")
