from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.application.dtos import ProductCreateDTO, ProductResponseDTO, ProductUpdateDTO
from src.application.services import ProductsService
from src.infra.database import DBConnection
from src.infra.repositories import AlchemyProductsRepo

router = APIRouter()


# Dependências
def get_db_session():
    """Retorna uma sessão do banco de dados"""
    with DBConnection() as db:
        yield db.session


# Monta o repository
def get_products_repository(session: Annotated[Session, Depends(get_db_session)]):
    """Retorna uma instância do repositório de produtos"""
    return AlchemyProductsRepo(session)


# Monta o servico
def get_products_service(
    repository: Annotated[AlchemyProductsRepo, Depends(get_products_repository)],
):
    """Retorna uma instância do serviço de produtos"""
    return ProductsService(repository)


# Routes
@router.get("", response_model=list[ProductResponseDTO])
def list_products(service: Annotated[ProductsService, Depends(get_products_service)]):
    return service.get_all_products()


@router.get("/{product_id}", response_model=ProductResponseDTO)
def get_product(
    product_id: UUID,
    service: Annotated[ProductsService, Depends(get_products_service)],
):
    return service.get_product_by_id(product_id)


@router.get("/sku/{sku}", response_model=ProductResponseDTO)
def get_product_by_sku(
    sku: str,
    service: Annotated[ProductsService, Depends(get_products_service)],
):
    return service.get_product_by_sku(sku)


@router.post("", response_model=ProductResponseDTO, status_code=201)
def create_product(
    product_data: ProductCreateDTO,
    service: Annotated[ProductsService, Depends(get_products_service)],
):
    return service.create_product(product_data)


@router.put("/{product_id}", response_model=ProductResponseDTO)
def update_product(
    product_id: UUID,
    product_data: ProductUpdateDTO,
    service: Annotated[ProductsService, Depends(get_products_service)],
):
    return service.update_product(product_id, product_data)


@router.delete("/{product_id}", status_code=204)
def delete_product(
    product_id: UUID,
    service: Annotated[ProductsService, Depends(get_products_service)],
):
    service.delete_product(product_id)
