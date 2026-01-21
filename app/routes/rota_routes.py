from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.rota import RotaCreate, RotaResponse
from app.repositories.rota_repository import RotaRepository

router = APIRouter(prefix="/rotas", tags=["Rotas"])


@router.post("/", response_model=RotaResponse)
def criar_rota(rota: RotaCreate, db: Session = Depends(get_db)):
    return RotaRepository.criar(db, rota)


@router.get("/", response_model=list[RotaResponse])
def listar_rotas(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return RotaRepository.listar(db, page, limit)


@router.get("/{rota_id}", response_model=RotaResponse)
def buscar_rota(rota_id: int, db: Session = Depends(get_db)):
    rota = RotaRepository.buscar_por_id(db, rota_id)
    if not rota:
        raise HTTPException(status_code=404, detail="Rota não encontrada")
    return rota
