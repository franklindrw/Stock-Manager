from abc import ABC, abstractmethod

from src.application.dtos import ProductCreateDTO, ProductResponseDTO, ProductUpdateDTO


class IProductsService(ABC):
    @abstractmethod
    def get_all_products(self) -> list[ProductResponseDTO]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: str) -> ProductResponseDTO:
        pass

    @abstractmethod
    def create_product(self, product_data: ProductCreateDTO) -> ProductResponseDTO:
        pass

    @abstractmethod
    def update_product(
        self, product_id: str, product_data: ProductUpdateDTO
    ) -> ProductResponseDTO:
        pass

    @abstractmethod
    def delete_product(self, product_id: str) -> None:
        pass
