from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductList, ProductResponse

router = APIRouter(prefix="/api/brands", tags=["brands"])


# Predefined brand list
BRANDS = [
    {"name": "TI", "full_name": "Texas Instruments"},
    {"name": "ADI", "full_name": "Analog Devices"},
    {"name": "ST", "full_name": "STMicroelectronics"},
    {"name": "NXP", "full_name": "NXP Semiconductors"},
    {"name": "ON", "full_name": "ON Semiconductor"},
    {"name": "Microchip", "full_name": "Microchip Technology"},
    {"name": "Infineon", "full_name": "Infineon Technologies"},
    {"name": "Renesas", "full_name": "Renesas Electronics"},
    {"name": "Samsung", "full_name": "Samsung Electro-Mechanics"},
    {"name": "Murata", "full_name": "Murata Manufacturing"},
    {"name": "Yageo", "full_name": "Yageo Corporation"},
    {"name": "TE", "full_name": "TE Connectivity"},
]


@router.get("")
async def get_brands():
    return BRANDS


@router.get("/{brand_name}/products", response_model=ProductList)
async def get_brand_products(
    brand_name: str,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    stmt = (
        select(Product)
        .where(Product.brand.ilike(f"%{brand_name}%"))
        .order_by(Product.created_at.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    result = await db.execute(stmt)
    items = result.scalars().all()

    count_stmt = select(Product).where(Product.brand.ilike(f"%{brand_name}%"))
    count_result = await db.execute(count_stmt)
    total = len(count_result.scalars().all())

    return ProductList(
        items=[ProductResponse.model_validate(p) for p in items],
        total=total,
        page=page,
        page_size=page_size,
    )
