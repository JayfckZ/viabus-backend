from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from datetime import datetime

from sqlalchemy.orm import relationship

from app.db.database import Base


class Pagamento(Base):
    __tablename__ = "pagamentos"

    id = Column(Integer, primary_key=True, index=True)
    passagem_id = Column(Integer, ForeignKey("passagens.id"), nullable=False)
    metodo = Column(String, nullable=False)
    status = Column(String, nullable=False)
    pago_em = Column(DateTime)
    transacao_id = Column(String)

    passagem = relationship("Passagem", backref="pagamentos")
