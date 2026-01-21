from typing import List

from sqlalchemy.orm import Session
from app.models.reserva_assento import ReservaAssento
from app.schemas.reserva_assento import ReservaAssentoCreate


class ReservaAssentoRepository:

    @staticmethod
    def criar(db: Session, reserva: ReservaAssentoCreate) -> ReservaAssento:
        nova = ReservaAssento(**reserva.model_dump())
        db.add(nova)
        db.commit()
        db.refresh(nova)
        return nova

    @staticmethod
    def listar(db: Session, page: int = 1, limit: int = 20) -> List[ReservaAssento]:
        offset = (page - 1) * limit
        return db.query(ReservaAssento).offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, reserva_id: int):
        return db.query(ReservaAssento).filter(ReservaAssento.id == reserva_id).first()
