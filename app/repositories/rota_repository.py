from typing import List

from sqlalchemy.orm import Session
from app.models.rota import Rota
from app.schemas.rota import RotaCreate


class RotaRepository:

    @staticmethod
    def criar(db: Session, rota: RotaCreate) -> Rota:
        nova = Rota(**rota.model_dump())
        db.add(nova)
        db.commit()
        db.refresh(nova)
        return nova

    @staticmethod
    def listar(db: Session, page: int = 1, limit: int = 20) -> List[Rota]:
        offset = (page - 1) * limit
        return db.query(Rota).offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, rota_id: int):
        return db.query(Rota).filter(Rota.id == rota_id).first()
