from datetime import date, datetime
from typing import List

from sqlalchemy.orm import Session

from app.models import Rota, Onibus
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
    def listar(
        db: Session,
        page: int = 1,
        limit: int = 20,
        origem: str | None = None,
        destino: str | None = None,
        data: date | None = None,
        empresa_id: int | None = None,
        tipo_onibus: str | None = None,
    ) -> List[Viagem]:
        offset = (page - 1) * limit

        query = db.query(Viagem).join(Rota).join(Onibus)

        if origem:
            query = query.filter(Rota.cidade_origem.ilike(f"%{origem}%"))

        if destino:
            query = query.filter(Rota.cidade_destino.ilike(f"%{destino}%"))

        if data:
            inicio = datetime.combine(data, datetime.min.time())
            fim = datetime.combine(data, datetime.max.time())

            query = query.filter(
                Viagem.data_hora_partida >= inicio, Viagem.data_hora_partida <= fim
            )

        if empresa_id:
            query = query.filter(Onibus.empresa_id == empresa_id)

        if tipo_onibus:
            query = query.filter(Onibus.tipo_layout_assentos == tipo_onibus)

        return query.offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, viagem_id: int):
        return db.query(Viagem).filter(Viagem.id == viagem_id).first()
