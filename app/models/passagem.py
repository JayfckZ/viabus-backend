from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric, Index
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


class Passagem(Base):
    __tablename__ = "passagens"

    id = Column(Integer, primary_key=True, index=True)
    viagem_id = Column(Integer, ForeignKey("viagens.id"), nullable=False)
    passageiro_id = Column(Integer, ForeignKey("passageiros.id"), nullable=False)
    numero_assento = Column(Integer, nullable=False)
    preco = Column(Numeric(10, 2), nullable=False)
    status = Column(String, default="ativo")
    qr_code = Column(String)
    comprado_em = Column(DateTime, default=datetime.utcnow)

    passageiro = relationship("Passageiro", backref="passagens")
    viagem = relationship("Viagem", backref="passagens")

    __table_args__ = (
        Index("uq_viagem_assento", "viagem_id", "numero_assento", unique=True),
    )
