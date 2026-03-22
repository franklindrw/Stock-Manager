from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class StoreCreateDTO(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    is_active: bool = True


class StoreUpdateDTO(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3, max_length=100)
    is_active: Optional[bool] = None


class StoreResponseDTO(BaseModel):
    id: UUID
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
