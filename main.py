from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy import text
from src.infra import DBConnection

from src.controllers import products_router

app = FastAPI(title="Inventory Microservice")

app.include_router(products_router, prefix="/products", tags=["Products"])

@app.get("/health")
def health_check():
    return {"status": "online", "version": "1.0.0"}
