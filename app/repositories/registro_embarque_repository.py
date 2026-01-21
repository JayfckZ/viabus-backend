from typing import List

from sqlalchemy.orm import Session
from app.models.registro_embarque import RegistroEmbarque
from app.schemas.registro_embarque import RegistroEmbarqueCreate


class RegistroEmbarqueRepository:

    @staticmethod
    def criar(db: Session, registro: RegistroEmbarqueCreate) -> RegistroEmbarque:
        novo = RegistroEmbarque(**registro.model_dump())
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo

    @staticmethod
    def listar(db: Session, page: int = 1, limit: int = 20) -> List[RegistroEmbarque]:
        offset = (page - 1) * limit
        return db.query(RegistroEmbarque).offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, registro_id: int):
        return (
            db.query(RegistroEmbarque)
            .filter(RegistroEmbarque.id == registro_id)
            .first()
        )
