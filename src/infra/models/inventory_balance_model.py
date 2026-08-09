from datetime import datetime

from sqlalchemy import CheckConstraint, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base
from .products_model import ProductsModel
from .stores_model import StoresModel


class InventoryBalanceModel(Base):
    __tablename__ = "inventory_balances"

    product_id: Mapped[UUID] = mapped_column(
        ForeignKey("products.id"), primary_key=True
    )
    store_id: Mapped[UUID] = mapped_column(ForeignKey("stores.id"), primary_key=True)
    available_quantity: Mapped[int] = mapped_column(default=0)
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP")
    )

    product: Mapped["ProductsModel"] = relationship()
    store: Mapped["StoresModel"] = relationship()

    __table_args__ = (
        CheckConstraint("available_quantity >= 0", name="quantity_not_negative"),
    )
