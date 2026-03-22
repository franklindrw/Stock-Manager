from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class StoreEntity:
    name: str
    id: UUID | None = None
    is_active: bool = True
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __post_init__(self):
        if self.name:
            self.name = self.name.strip().capitalize()

        if not self.name or len(self.name) < 3:
            raise ValueError("Name is required and must be at least 3 characters long")

        if len(self.name) > 100:
            raise ValueError("Name must be less than 100 characters")
