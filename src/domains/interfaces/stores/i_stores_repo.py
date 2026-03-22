from abc import ABC, abstractmethod
from uuid import UUID

from src.domains.entities.stores import StoreEntity


class IStoresRepo(ABC):
    @abstractmethod
    def get_stores(self) -> list[StoreEntity]:
        pass

    @abstractmethod
    def get_store_by_id(self, store_id: UUID) -> StoreEntity:
        pass

    @abstractmethod
    def create_store(self, store_data: StoreEntity) -> StoreEntity:
        pass

    @abstractmethod
    def update_store(self, store_id: UUID, store_data: StoreEntity) -> StoreEntity:
        pass

    @abstractmethod
    def delete_store(self, store_id: UUID) -> None:
        pass
