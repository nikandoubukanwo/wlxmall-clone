from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func
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
        .order_by(Product.id.asc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    result = await db.execute(stmt)
    items = result.scalars().all()

    total = await db.scalar(select(func.count(Product.id))) or 0

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
    pkg: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Product)
    if keyword:
        stmt = stmt.where(
            Product.name.ilike(f"%{keyword}%")
            | Product.model.ilike(f"%{keyword}%")
            | Product.brand.ilike(f"%{keyword}%")
            | Product.description.ilike(f"%{keyword}%")
        )
    if brand:
        stmt = stmt.where(Product.brand.ilike(f"%{brand}%"))
    if pkg:
        stmt = stmt.where(Product.pkg.ilike(f"%{pkg}%"))

    stmt = stmt.order_by(Product.id.asc())
    # Build count query from the same filters
    count_stmt = select(func.count(Product.id))
    if keyword:
        count_stmt = count_stmt.where(
            Product.name.ilike(f"%{keyword}%")
            | Product.model.ilike(f"%{keyword}%")
            | Product.brand.ilike(f"%{keyword}%")
            | Product.description.ilike(f"%{keyword}%")
        )
    if brand:
        count_stmt = count_stmt.where(Product.brand.ilike(f"%{brand}%"))
    if pkg:
        count_stmt = count_stmt.where(Product.pkg.ilike(f"%{pkg}%"))

    result = await db.execute(stmt.offset((page - 1) * page_size).limit(page_size))
    items = result.scalars().all()

    total = await db.scalar(count_stmt) or 0

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
