from typing import List

from sqlalchemy.orm import Session
from app.models.passageiro import Passageiro
from app.schemas.passageiro import PassageiroCreate


class PassageiroRepository:

    @staticmethod
    def criar(db: Session, passageiro: PassageiroCreate) -> Passageiro:
        novo = Passageiro(**passageiro.model_dump())
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo

    @staticmethod
    def listar(db: Session, page: int = 1, limit: int = 20) -> List[Passageiro]:
        offset = (page - 1) * limit
        return db.query(Passageiro).offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, passageiro_id: int):
        return db.query(Passageiro).filter(Passageiro.id == passageiro_id).first()
