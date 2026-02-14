from sqlalchemy import ForeignKey, Index, text, String
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base
from .products_model import ProductsModel
from .stores_model import StoresModel

class InventoryMovementModel(Base):
    __tablename__ = "inventory_movements"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("uuidv7()"))
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"))
    store_id: Mapped[UUID] = mapped_column(ForeignKey("stores.id"))
    quantity: Mapped[int] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"), nullable=False)

    product: Mapped["ProductsModel"] = relationship()
    store: Mapped["StoresModel"] = relationship()

    __table_args__ = (
        Index("idx_movements_query", "product_id", "store_id", "created_at"),
    )
