from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import text
from app.infra.config import DBConnection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- CODIGO DE TESTE AO INICIAR ---
    print("Testando conexao com o Postgres...")
    try:
        with DBConnection() as db:
            db.session.execute(text("SELECT 1"))
            print("✅ Banco de Dados conectado!")
    except Exception as e:
        print(f"Falha critica na conexao: {e}")
        # raise e
    # ----------------------------------
    yield
    # (Codigo aqui executa ao desligar o app)

app = FastAPI(lifespan=lifespan)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
