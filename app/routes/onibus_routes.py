from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.onibus import OnibusCreate, OnibusResponse
from app.repositories.onibus_repository import OnibusRepository

router = APIRouter(prefix="/onibus", tags=["Onibus"])


@router.post("/", response_model=OnibusResponse)
def criar_onibus(onibus: OnibusCreate, db: Session = Depends(get_db)):
    return OnibusRepository.criar(db, onibus)


@router.get("/", response_model=list[OnibusResponse])
def listar_onibus(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return OnibusRepository.listar(db, page, limit)


@router.get("/{onibus_id}", response_model=OnibusResponse)
def buscar_onibus(onibus_id: int, db: Session = Depends(get_db)):
    onibus = OnibusRepository.buscar_por_id((db, onibus_id))
    if not onibus:
        raise HTTPException(status_code=404, detail="Ônibus não encontrado")
    return onibus
