from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class ProductEntity:
    sku: str
    name: str
    id: UUID | None = None
    description: Optional[str] = None
    is_active: bool = True
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __post_init__(self):
        if not self.sku or len(self.sku) < 3:
            raise ValueError("SKU is required and must be at least 3 characters long")

        if len(self.sku) > 50:
            raise ValueError("SKU must be less than 50 characters")

        if self.name:
            self.name = self.name.strip().capitalize()

        if not self.name or len(self.name) < 3:
            raise ValueError("Name is required and must be at least 3 characters long")

        if len(self.name) > 100:
            raise ValueError("Name must be less than 100 characters")
