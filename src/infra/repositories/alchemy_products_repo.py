from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domains.entities.products import ProductEntity
from src.domains.interfaces.products import IProductsRepo
from src.infra.models import ProductsModel


class AlchemyProductsRepo(IProductsRepo):
    def __init__(self, session: Session):
        self.session = session

    def get_all_products(self) -> list[ProductEntity]:
        products = self.session.execute(select(ProductsModel)).scalars().all()
        return [self._to_entity(p) for p in products]

    def get_product_by_id(self, product_id: UUID) -> ProductEntity:
        product = self.session.get(ProductsModel, product_id)
        return self._to_entity(product) if product else None

    def create_product(self, product_entity: ProductEntity) -> ProductEntity:
        product_model = ProductsModel(
            sku=product_entity.sku,
            name=product_entity.name,
            is_active=product_entity.is_active,
        )
        self.session.add(product_model)
        self.session.commit()
        self.session.refresh(product_model)
        return self._to_entity(product_model)

    def update_product(
        self, product_id: UUID, product_entity: ProductEntity
    ) -> Optional[ProductEntity]:
        product_model = self.session.get(ProductsModel, product_id)

        if not product_model:
            return None

        product_model.sku = product_entity.sku
        product_model.name = product_entity.name
        product_model.is_active = product_entity.is_active

        self.session.commit()
        self.session.refresh(product_model)
        return self._to_entity(product_model)

    def delete_product(self, product_id: UUID) -> None:
        product_model = self.session.get(ProductsModel, product_id)

        if product_model:
            self.session.delete(product_model)
            self.session.commit()

    @staticmethod
    def _to_entity(model: ProductsModel) -> ProductEntity:
        """Converte ProductsModel para ProductEntity"""
        return ProductEntity(
            id=model.id,
            sku=model.sku,
            name=model.name,
            is_active=model.is_active,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
