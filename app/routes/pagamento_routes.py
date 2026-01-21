from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.pagamento import PagamentoCreate, PagamentoResponse
from app.repositories.pagamento_repository import PagamentoRepository

router = APIRouter(prefix="/pagamentos", tags=["Pagamentos"])


@router.post("/", response_model=PagamentoResponse)
def criar_pagamento(pagamento: PagamentoCreate, db: Session = Depends(get_db)):
    return PagamentoRepository.criar(db, pagamento)


@router.get("/", response_model=list[PagamentoResponse])
def listar_pagamentos(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return PagamentoRepository.listar(db, page, limit)


@router.get("/{pagamento_id}", response_model=PagamentoResponse)
def buscar_pagamento(pagamento_id: int, db: Session = Depends(get_db)):
    pagamento = PagamentoRepository.buscar_por_id(db, pagamento_id)
    if not pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    return pagamento
