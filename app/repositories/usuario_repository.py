from typing import List

from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate


class UsuarioRepository:

    @staticmethod
    def criar(db: Session, usuario: UsuarioCreate) -> Usuario:
        novo = Usuario(
            nome=usuario.nome,
            email=usuario.email,
            cargo=usuario.cargo,
            senha_hash=usuario.senha,
        )
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return novo

    @staticmethod
    def listar(db: Session, page: int = 1, limit: int = 20) -> List[Usuario]:
        offset = (page - 1) * limit
        return db.query(Usuario).offset(offset).limit(limit).all()

    @staticmethod
    def buscar_por_id(db: Session, usuario_id: int):
        return db.query(Usuario).filter(Usuario.id == usuario_id).first()
