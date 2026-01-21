from typing import List

from sqlalchemy.orm import Session
from app.models.passagem import Passagem
from app.schemas.passagem import PassagemCreate


class PassagemRepository:

    @staticmethod
    def criar(db: Session, passagem: PassagemCreate) -> Passagem:
        nova = Passagem(**passagem.model_dump())
        db.add(nova)
        db.commit()
        db.refresh(nova)
        return nova

    @staticmethod
    def listar(db: Session, page: int = 1, limit: int = 20) -> List[Passagem]:
        offset = (page - 1) * limit
        return db.query(Passagem).offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, passagem_id: int):
        return db.query(Passagem).filter(Passagem.id == passagem_id).first()
