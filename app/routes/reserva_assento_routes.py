from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.reserva_assento import ReservaAssentoCreate, ReservaAssentoResponse
from app.repositories.reserva_assento_repository import ReservaAssentoRepository

router = APIRouter(prefix="/reservas", tags=["Reservas de Assento"])


@router.post("/", response_model=ReservaAssentoResponse)
def criar_reserva(reserva: ReservaAssentoCreate, db: Session = Depends(get_db)):
    return ReservaAssentoRepository.criar(db, reserva)


@router.get("/", response_model=list[ReservaAssentoResponse])
def listar_reservas(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return ReservaAssentoRepository.listar(db, page, limit)


@router.get("/{reserva_id}", response_model=ReservaAssentoResponse)
def buscar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = ReservaAssentoRepository.buscar_por_id(db, reserva_id)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    return reserva
