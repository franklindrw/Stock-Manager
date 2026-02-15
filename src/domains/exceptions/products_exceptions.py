from uuid import UUID


class DomainError(Exception):
    pass


class ProductNotFoundError(DomainError):
    def __init__(self, product_id: UUID):
        self.message = f"Product with id {product_id} not found"
        super().__init__(self.message)


class SkuAlreadyExistsError(DomainError):
    def __init__(self, sku: str):
        self.message = f"Product with SKU {sku} already exists"
        super().__init__(self.message)
