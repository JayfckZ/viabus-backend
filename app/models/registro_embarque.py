from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

from sqlalchemy.orm import relationship

from app.db.database import Base


class RegistroEmbarque(Base):
    __tablename__ = "registros_embarque"

    id = Column(Integer, primary_key=True, index=True)
    passagem_id = Column(Integer, ForeignKey("passagens.id"), nullable=False)
    verificado_por_usuario_id = Column(
        Integer, ForeignKey("usuarios.id"), nullable=False
    )
    verificado_em = Column(DateTime, default=datetime.utcnow)

    passagem = relationship("Passagem", backref="registros_embarque")
    usuario = relationship("Usuario", backref="registros_verificados")
