from sqlalchemy import Column, Integer, String, ForeignKey, Index, DateTime
from datetime import datetime, timedelta

from sqlalchemy.orm import relationship

from app.db.database import Base


class ReservaAssento(Base):
    __tablename__ = "reservas_assentos"

    id = Column(Integer, primary_key=True, index=True)
    viagem_id = Column(Integer, ForeignKey("viagens.id"), nullable=False)
    numero_assento = Column(Integer, nullable=False)
    sessao_id = Column(String, nullable=False)
    expira_em = Column(DateTime, nullable=False)

    __table_args__ = (
        Index("uq_reserva_viagem_assento", "viagem_id", "numero_assento", unique=True),
    )

    viagem = relationship("Viagem", backref="reservas")
