from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.enums.tipo_onibus import TipoOnibus
from app.schemas.viagem import ViagemCreate, ViagemResponse
from app.repositories.viagem_repository import ViagemRepository

router = APIRouter(prefix="/viagens", tags=["Viagens"])


@router.post("/", response_model=ViagemResponse)
def criar_viagem(viagem: ViagemCreate, db: Session = Depends(get_db)):
    return ViagemRepository.criar(db, viagem)


@router.get("/", response_model=list[ViagemResponse])
def listar_viagens(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    origem: str | None = None,
    destino: str | None = None,
    data: date | None = None,
    empresa_id: int | None = None,
    tipo_onibus: TipoOnibus | None = None,
    db: Session = Depends(get_db),
):
    return ViagemRepository.listar(
        db=db,
        page=page,
        limit=limit,
        origem=origem,
        destino=destino,
        data=data,
        empresa_id=empresa_id,
        tipo_onibus=tipo_onibus,
    )


@router.get("/{viagem_id}", response_model=ViagemResponse)
def buscar_viagem(viagem_id: int, db: Session = Depends(get_db)):
    viagem = ViagemRepository.buscar_por_id(db, viagem_id)
    if not viagem:
        raise HTTPException(status_code=404, detail="Viagem não encontrada")
    return viagem
