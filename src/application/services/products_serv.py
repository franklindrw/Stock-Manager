from uuid import UUID

from src.application.dtos import ProductCreateDTO, ProductUpdateDTO
from src.domains.entities.products import ProductEntity
from src.domains.exceptions import ProductNotFoundError, SkuAlreadyExistsError
from src.domains.interfaces.products import IProductsRepo, IProductsService


class ProductsService(IProductsService):
    def __init__(self, repository: IProductsRepo):
        self.repository = repository

    def get_all_products(self) -> list[ProductEntity]:
        return self.repository.get_all_products()

    def get_product_by_id(self, product_id: UUID) -> ProductEntity:
        product = self.repository.get_product_by_id(product_id)

        if not product:
            raise ProductNotFoundError(product_id)

        return product

    def get_product_by_sku(self, sku: str) -> ProductEntity:
        product = self.repository.get_product_by_sku(sku)

        if not product:
            raise ProductNotFoundError(sku)

        return product

    def create_product(self, product_data: ProductCreateDTO):
        # Verificar se já existe um produto com o mesmo SKU
        existing_product = self.repository.get_product_by_sku(product_data.sku)

        if existing_product:
            raise SkuAlreadyExistsError(product_data.sku)

        new_product = ProductEntity(**product_data.model_dump())

        return self.repository.create_product(new_product)

    def update_product(self, product_id: UUID, product_data: ProductUpdateDTO):
        product = self.repository.get_product_by_id(product_id)

        if not product:
            raise ProductNotFoundError(product_id)

        update_dict = product_data.model_dump(exclude_unset=True)

        for key, value in update_dict.items():
            setattr(product, key, value)

        return self.repository.update_product(product_id, product)

    def delete_product(self, product_id: UUID) -> None:
        product = self.repository.get_product_by_id(product_id)

        if not product:
            raise ProductNotFoundError(product_id)

        self.repository.delete_product(product_id)
