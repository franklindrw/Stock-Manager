from fastapi import FastAPI

from src.controllers import products_router

app = FastAPI(title="Inventory Microservice")

app.include_router(products_router, prefix="/products", tags=["Products"])


@app.get("/health")
def health_check():
    return {"status": "online", "version": "1.0.0"}
