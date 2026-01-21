from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.empresa import EmpresaCreate, EmpresaResponse
from app.repositories.empresa_repository import EmpresaRepository

router = APIRouter(prefix="/empresas", tags=["Empresas"])


@router.post("/", response_model=EmpresaResponse)
def criar_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    try:
        return EmpresaRepository.criar(db, empresa)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[EmpresaResponse])
def listar_empresas(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return EmpresaRepository.listar(db, page, limit)


@router.get("/{empresa_id}", response_model=EmpresaResponse)
def buscar_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = EmpresaRepository.buscar_por_id(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa
