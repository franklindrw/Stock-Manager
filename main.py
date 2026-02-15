from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.controllers import products_router
from src.domains.exceptions import (
    DomainError,
    ProductNotFoundError,
    SkuAlreadyExistsError,
)

app = FastAPI(title="Inventory Microservice")


@app.exception_handler(RequestValidationError)
async def handle_request_validation_error(request, exc: RequestValidationError):
    errors = [
        {"field": error["loc"][-1], "message": error["msg"]} for error in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation error",
            "message": "Dados inválidos ou incompletos.",
            "details": errors,
        },
    )


@app.exception_handler(DomainError)
async def handle_domain_error(_, exc: DomainError):
    status_code = 400

    if isinstance(exc, ProductNotFoundError):
        status_code = 404

    if isinstance(exc, SkuAlreadyExistsError):
        status_code = 409

    return JSONResponse(
        status_code=status_code,
        content={"error": exc.__class__.__name__, "message": str(exc)},
    )


app.include_router(products_router, prefix="/products", tags=["Products"])


@app.get("/health")
def health_check():
    return {"status": "online", "version": "1.0.0"}
