from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.product import Category, Product
from app.schemas.product import CategorySchema, ProductList, ProductResponse

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/hot", response_model=ProductList)
async def get_hot_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    stmt = (
        select(Product)
        .where(Product.is_hot == True)
        .order_by(Product.created_at.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    result = await db.execute(stmt)
    items = result.scalars().all()

    count_stmt = select(Product).where(Product.is_hot == True)
    count_result = await db.execute(count_stmt)
    total = len(count_result.scalars().all())

    return ProductList(
        items=[ProductResponse.model_validate(p) for p in items],
        total=total,
        page=page,
        page_size=page_size,
    )


@router.get("/search", response_model=ProductList)
async def search_products(
    keyword: Optional[str] = Query(None),
    brand: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Product)
    if keyword:
        stmt = stmt.where(
            Product.name.ilike(f"%{keyword}%")
            | Product.model.ilike(f"%{keyword}%")
        )
    if brand:
        stmt = stmt.where(Product.brand.ilike(f"%{brand}%"))
    if category:
        stmt = stmt.where(Product.category == category)

    stmt = stmt.order_by(Product.created_at.desc())
    count_stmt = stmt
    result = await db.execute(stmt.offset((page - 1) * page_size).limit(page_size))
    items = result.scalars().all()

    count_result = await db.execute(count_stmt)
    total = len(count_result.scalars().all())

    return ProductList(
        items=[ProductResponse.model_validate(p) for p in items],
        total=total,
        page=page,
        page_size=page_size,
    )


@router.get("/categories", response_model=list[CategorySchema])
async def get_categories(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Category))
    categories = result.scalars().all()
    return [CategorySchema.model_validate(c) for c in categories]


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductResponse.model_validate(product)
