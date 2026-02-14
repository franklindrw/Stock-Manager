from sqlalchemy import ForeignKey, Index, CheckConstraint, text, String
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class ProductsModel(Base):
    __tablename__ = "products"
    
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("uuidv7()"))
    sku: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP"), nullable=False)
    
class StoresModel(Base):
    __tablename__ = "stores"
    
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("uuidv7()"))
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP"), nullable=False)
    
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
    
class InventoryBalanceModel(Base):
    __tablename__ = "inventory_balances"
    
    product_id: Mapped[UUID] = mapped_column(ForeignKey("products.id"), primary_key=True)
    store_id: Mapped[UUID] = mapped_column(ForeignKey("stores.id"), primary_key=True)
    available_quantity: Mapped[int] = mapped_column(default=0)
    updated_at: Mapped[datetime] = mapped_column(
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=text("CURRENT_TIMESTAMP")
    )
    
    product: Mapped["ProductsModel"] = relationship()
    store: Mapped["StoresModel"] = relationship()
    
    __table_args__ = (
        CheckConstraint("available_quantity >= 0", name="quantity_not_negative"),
    )
