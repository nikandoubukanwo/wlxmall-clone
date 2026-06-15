from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int
    name: str
    parent_id: Optional[int] = None

    model_config = {"from_attributes": True}


class ProductBase(BaseModel):
    name: str
    model: str
    brand: str
    price: float = 0
    stock: int = 0
    category: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    is_hot: bool = False


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


class ProductList(BaseModel):
    items: list[ProductResponse]
    total: int
    page: int = 1
    page_size: int = 20
