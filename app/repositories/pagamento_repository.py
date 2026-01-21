from typing import List

from sqlalchemy.orm import Session
from app.models.pagamento import Pagamento
from app.schemas.pagamento import PagamentoCreate


class PagamentoRepository:

    @staticmethod
    def criar(db: Session, pagamento: PagamentoCreate) -> Pagamento:
        novo = Pagamento(**pagamento.model_dump())
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo

    @staticmethod
    def listar(db: Session, page: int = 1, limit: int = 20) -> List[Pagamento]:
        offset = (page - 1) * limit
        return db.query(Pagamento).offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, pagamento_id: int):
        return db.query(Pagamento).filter(Pagamento.id == pagamento_id).first()
