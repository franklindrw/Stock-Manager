from uuid import UUID

from src.domains.entities.stores import StoreEntity
from src.domains.interfaces.stores import IStoresRepo


class StoresService(IStoresRepo):
    def __init__(self, repository: IStoresRepo):
        self.repository = repository

    def get_stores(self) -> list[StoreEntity]:
        return self.repository.get_stores()

    def get_store_by_id(self, store_id: UUID) -> StoreEntity:
        return self.repository.get_store_by_id(store_id)

    def create_store(self, store_data: StoreEntity) -> StoreEntity:
        return self.repository.create_store(store_data)

    def update_store(self, store_id: UUID, store_data: StoreEntity) -> StoreEntity:
        return self.repository.update_store(store_id, store_data)

    def delete_store(self, store_id: UUID) -> None:
        self.repository.delete_store(store_id)
