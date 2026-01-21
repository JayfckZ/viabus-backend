from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.passagem import PassagemCreate, PassagemResponse
from app.repositories.passagem_repository import PassagemRepository

router = APIRouter(prefix="/passagens", tags=["Passagens"])


@router.post("/", response_model=PassagemResponse)
def criar_passagem(passagem: PassagemCreate, db: Session = Depends(get_db)):
    return PassagemRepository.criar(db, passagem)


@router.get("/", response_model=list[PassagemResponse])
def listar_passagens(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return PassagemRepository.listar(db, page, limit)


@router.get("/{passagem_id}", response_model=PassagemResponse)
def buscar_passagem(passagem_id: int, db: Session = Depends(get_db)):
    passagem = PassagemRepository.buscar_por_id(db, passagem_id)
    if not passagem:
        raise HTTPException(status_code=404, detail="Passagem não encontrada")
    return passagem
