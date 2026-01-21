from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Rota(Base):
    __tablename__ = "rotas"

    id = Column(Integer, primary_key=True, index=True)
    cidade_origem = Column(String, nullable=False)
    cidade_destino = Column(String, nullable=False)
    distancia_km = Column(Integer)
    tempo_estimado_min = Column(Integer)
