from typing import List

from sqlalchemy.orm import Session
from app.models import Onibus
from app.schemas.onibus import OnibusCreate


class OnibusRepository:
    @staticmethod
    def criar(db: Session, onibus: OnibusCreate) -> Onibus:
        novo = Onibus(**onibus.model_dump())
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo

    @staticmethod
    def listar(db: Session, page: int = 1, limit: int = 20) -> List[Onibus]:
        offset = (page - 1) * limit
        return db.query(Onibus).offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, onibus_id: int) -> Onibus | None:
        return db.query(Onibus).filter(Onibus.id == onibus_id).first()
