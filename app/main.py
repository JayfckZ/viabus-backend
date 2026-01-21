import os

from fastapi import FastAPI
from dotenv import load_dotenv
from app.db.database import Base, engine
from app.models import *
from app.routes import *

app = FastAPI(title="API ViaBus")

app.include_router(empresa_router)
app.include_router(onibus_router)
app.include_router(rota_router)
app.include_router(viagem_router)
app.include_router(passageiro_router)
app.include_router(passagem_router)
app.include_router(pagamento_router)
app.include_router(reserva_assento_router)
app.include_router(registro_embarque_router)
app.include_router(usuario_router)


@app.on_event("startup")
def criar_tabelas():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return {"Hello": "World"}
