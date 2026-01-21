from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.passageiro import PassageiroCreate, PassageiroResponse
from app.repositories.passageiro_repository import PassageiroRepository

router = APIRouter(prefix="/passageiros", tags=["Passageiros"])


@router.post("/", response_model=PassageiroResponse)
def criar_passageiro(passageiro: PassageiroCreate, db: Session = Depends(get_db)):
    return PassageiroRepository.criar(db, passageiro)


@router.get("/", response_model=list[PassageiroResponse])
def listar_passageiros(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return PassageiroRepository.listar(db, page, limit)


@router.get("/{passageiro_id}", response_model=PassageiroResponse)
def buscar_passageiro(passageiro_id: int, db: Session = Depends(get_db)):
    passageiro = PassageiroRepository.buscar_por_id(db, passageiro_id)
    if not passageiro:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")
    return passageiro
