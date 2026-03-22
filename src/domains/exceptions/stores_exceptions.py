from uuid import UUID

from .products_exceptions import DomainError


class StoreNotFoundError(DomainError):
    def __init__(self, store_id: UUID):
        self.message = f"Store with id {store_id} not found"
        super().__init__(self.message)


class StoreNameAlreadyExistsError(DomainError):
    def __init__(self, name: str):
        self.message = f"Store with name {name} already exists"
        super().__init__(self.message)
