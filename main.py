from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import text
from app.infra.config import DBConnection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- CÓDIGO DE TESTE AO INICIAR ---
    print("🔍 Testando conexão com o Postgres...")
    try:
        with DBConnection() as db:
            db.session.execute(text("SELECT 1"))
            print("✅ Banco de Dados conectado!")
    except Exception as e:
        print(f"❌ Falha crítica na conexão: {e}")
        # Em produção, você pode querer interromper a subida do app aqui
        # raise e 
    # ----------------------------------
    yield
    # (Código aqui executa ao desligar o app)

app = FastAPI(lifespan=lifespan)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}