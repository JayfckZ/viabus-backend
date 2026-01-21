from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models.empresa import Empresa
from app.schemas.empresa import EmpresaCreate


class EmpresaRepository:

    @staticmethod
    def criar(db: Session, empresa: EmpresaCreate) -> Empresa:
        nova_empresa = Empresa(
            nome=empresa.nome,
            cnpj=empresa.cnpj,
            email=empresa.email,
            telefone=empresa.telefone,
        )
        try:
            db.add(nova_empresa)
            db.commit()
            db.refresh(nova_empresa)
            return nova_empresa
        except IntegrityError:
            db.rollback()
            raise ValueError("Email já cadastrado")

    @staticmethod
    def listar(db: Session, page: int = 1, limit: int = 20) -> List[Empresa]:
        offset = (page - 1) * limit
        return db.query(Empresa).offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, empresa_id: int) -> Empresa | None:
        return db.query(Empresa).filter(Empresa.id == empresa_id).first()
