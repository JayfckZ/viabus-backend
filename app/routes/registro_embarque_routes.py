from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.registro_embarque import (
    RegistroEmbarqueCreate,
    RegistroEmbarqueResponse,
)
from app.repositories.registro_embarque_repository import RegistroEmbarqueRepository

router = APIRouter(prefix="/embarques", tags=["Registros de Embarque"])


@router.post("/", response_model=RegistroEmbarqueResponse)
def criar_registro(registro: RegistroEmbarqueCreate, db: Session = Depends(get_db)):
    return RegistroEmbarqueRepository.criar(db, registro)


@router.get("/", response_model=list[RegistroEmbarqueResponse])
def listar_registros(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return RegistroEmbarqueRepository.listar(db, page, limit)


@router.get("/{registro_id}", response_model=RegistroEmbarqueResponse)
def buscar_registro(registro_id: int, db: Session = Depends(get_db)):
    registro = RegistroEmbarqueRepository.buscar_por_id(db, registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    return registro
