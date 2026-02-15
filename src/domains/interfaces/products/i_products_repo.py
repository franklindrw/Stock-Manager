from abc import ABC, abstractmethod
from uuid import UUID

from src.domains.entities.products import ProductEntity


class IProductsRepo(ABC):
    @abstractmethod
    def get_all_products(self) -> list[ProductEntity]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: UUID) -> ProductEntity:
        pass

    @abstractmethod
    def create_product(self, product_entity: ProductEntity) -> ProductEntity:
        pass

    @abstractmethod
    def update_product(
        self, product_id: UUID, product_entity: ProductEntity
    ) -> ProductEntity:
        pass

    @abstractmethod
    def delete_product(self, product_id: UUID) -> None:
        pass
