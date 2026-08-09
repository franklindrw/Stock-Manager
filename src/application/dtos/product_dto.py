from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProductCreateDTO(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    sku: str = Field(..., min_length=3, max_length=50)


class ProductUpdateDTO(BaseModel):
    name: Optional[str] = Field(..., min_length=3, max_length=100)
    is_active: Optional[bool] = None


class ProductResponseDTO(BaseModel):
    id: UUID
    name: str
    sku: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
