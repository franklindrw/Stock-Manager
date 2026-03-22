from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.application.dtos import StoreCreateDTO, StoreResponseDTO, StoreUpdateDTO
from src.application.services import StoresService
from src.domains.entities.stores import StoreEntity
from src.infra.database import DBConnection
from src.infra.repositories import AlchemyStoresRepo

router = APIRouter()


# Dependências
def get_db_session():
    """Retorna uma sessão do banco de dados"""
    with DBConnection() as db:
        yield db.session


# Monta o repository
def get_stores_repository(session: Annotated[Session, Depends(get_db_session)]):
    """Retorna uma instância do repositório de lojas"""
    return AlchemyStoresRepo(session)


# Monta o servico
def get_stores_service(
    repository: Annotated[AlchemyStoresRepo, Depends(get_stores_repository)],
):
    """Retorna uma instância do serviço de lojas"""
    return StoresService(repository)


# Routes
@router.get("", response_model=list[StoreResponseDTO])
def list_stores(service: Annotated[StoresService, Depends(get_stores_service)]):
    return service.get_stores()


@router.get("/{store_id}", response_model=StoreResponseDTO)
def get_store(
    store_id: UUID,
    service: Annotated[StoresService, Depends(get_stores_service)],
):
    return service.get_store_by_id(store_id)


@router.post("", response_model=StoreResponseDTO, status_code=201)
def create_store(
    store_data: StoreCreateDTO,
    service: Annotated[StoresService, Depends(get_stores_service)],
):
    new_store = StoreEntity(**store_data.model_dump())
    return service.create_store(new_store)


@router.put("/{store_id}", response_model=StoreResponseDTO)
def update_store(
    store_id: UUID,
    store_data: StoreUpdateDTO,
    service: Annotated[StoresService, Depends(get_stores_service)],
):
    existing_store = service.get_store_by_id(store_id)
    update_data = store_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(existing_store, key, value)

    return service.update_store(store_id, existing_store)


@router.delete("/{store_id}", status_code=204)
def delete_store(
    store_id: UUID,
    service: Annotated[StoresService, Depends(get_stores_service)],
):
    service.delete_store(store_id)
