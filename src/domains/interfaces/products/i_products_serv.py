from abc import ABC, abstractmethod
from uuid import UUID

from src.application.dtos import ProductCreateDTO, ProductUpdateDTO
from src.domains.entities.products import ProductEntity


class IProductsService(ABC):
    @abstractmethod
    def get_all_products(self) -> list[ProductEntity]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: UUID) -> ProductEntity:
        pass

    @abstractmethod
    def get_product_by_sku(self, sku: str) -> ProductEntity:
        pass

    @abstractmethod
    def create_product(self, product_data: ProductCreateDTO) -> ProductEntity:
        pass

    @abstractmethod
    def update_product(
        self, product_id: UUID, product_data: ProductUpdateDTO
    ) -> ProductEntity:
        pass

    @abstractmethod
    def delete_product(self, product_id: UUID) -> None:
        pass
