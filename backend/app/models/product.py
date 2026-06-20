from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text, Boolean, func
from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    model = Column(String(200), index=True, nullable=False)
    brand = Column(String(100), index=True, nullable=False)
    pkg = Column(String(200), nullable=True, index=True)
    price = Column(Float, default=0)
    stock = Column(Integer, default=0)
    category = Column(String(100), nullable=True)
    image = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    is_hot = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
