from abc import ABC, abstractmethod

from src.domains.entities.products import ProductEntity


class IProductsRepo(ABC):
    @abstractmethod
    def get_all_products(self) -> list[ProductEntity]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id) -> ProductEntity:
        pass

    @abstractmethod
    def create_product(self, product_entity: ProductEntity) -> ProductEntity:
        pass

    @abstractmethod
    def update_product(
        self, product_id, product_entity: ProductEntity
    ) -> ProductEntity:
        pass

    @abstractmethod
    def delete_product(self, product_id) -> None:
        pass
