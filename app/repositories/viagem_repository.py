from typing import List

from sqlalchemy.orm import Session
from app.models.viagem import Viagem
from app.schemas.viagem import ViagemCreate


class ViagemRepository:

    @staticmethod
    def criar(db: Session, viagem: ViagemCreate) -> Viagem:
        nova = Viagem(**viagem.model_dump())
        db.add(nova)
        db.commit()
        db.refresh(nova)
        return nova

    @staticmethod
    def listar(db: Session, page: int = 1, limit: int = 20) -> List[Viagem]:
        offset = (page - 1) * limit
        return db.query(Viagem).offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, viagem_id: int):
        return db.query(Viagem).filter(Viagem.id == viagem_id).first()
