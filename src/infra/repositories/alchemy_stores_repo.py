from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domains.entities.stores import StoreEntity
from src.domains.interfaces.stores import IStoresRepo
from src.infra.models import StoresModel


class AlchemyStoresRepo(IStoresRepo):
    def __init__(self, session: Session):
        self.session = session

    def get_stores(self) -> list[StoreEntity]:
        stores = self.session.execute(select(StoresModel)).scalars().all()
        return [self._to_entity(s) for s in stores]

    def get_store_by_id(self, store_id: UUID) -> StoreEntity:
        store = self.session.get(StoresModel, store_id)
        return self._to_entity(store) if store else None

    def create_store(self, store_data: StoreEntity) -> StoreEntity:
        store_model = StoresModel(
            name=store_data.name,
            is_active=store_data.is_active,
        )
        self.session.add(store_model)
        self.session.commit()
        self.session.refresh(store_model)
        return self._to_entity(store_model)

    def update_store(self, store_id: UUID, store_data: StoreEntity) -> StoreEntity:
        store_model = self.session.get(StoresModel, store_id)

        if not store_model:
            return None

        store_model.name = store_data.name
        store_model.is_active = store_data.is_active

        self.session.commit()
        self.session.refresh(store_model)
        return self._to_entity(store_model)

    def delete_store(self, store_id: UUID) -> None:
        store_model = self.session.get(StoresModel, store_id)

        if store_model:
            self.session.delete(store_model)
            self.session.commit()

    def _to_entity(self, store_model: StoresModel) -> StoreEntity:
        return StoreEntity(
            id=store_model.id,
            name=store_model.name,
            is_active=store_model.is_active,
            created_at=store_model.created_at,
            updated_at=store_model.updated_at,
        )
