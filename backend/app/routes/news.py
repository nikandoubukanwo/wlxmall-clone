from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.news import News
from app.schemas.product import ProductList, ProductResponse

router = APIRouter(prefix="/api/news", tags=["news"])


class NewsResponse(ProductResponse):
    pass


@router.get("")
async def get_news(
    category: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(News).order_by(News.created_at.desc())
    if category:
        stmt = stmt.where(News.category == category)

    result = await db.execute(stmt.offset((page - 1) * page_size).limit(page_size))
    items = result.scalars().all()

    count_result = await db.execute(stmt)
    total = len(count_result.scalars().all())

    return {
        "items": [
            {
                "id": n.id,
                "title": n.title,
                "summary": n.summary,
                "category": n.category,
                "image": n.image,
                "view_count": n.view_count,
                "created_at": n.created_at.isoformat() if n.created_at else None,
            }
            for n in items
        ],
        "total": total,
        "page": page,
        "page_size": page_size,
    }


@router.get("/{news_id}")
async def get_news_detail(news_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(News).where(News.id == news_id))
    news = result.scalar_one_or_none()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")

    # Increment view count
    news.view_count = (news.view_count or 0) + 1
    await db.flush()

    return {
        "id": news.id,
        "title": news.title,
        "content": news.content,
        "summary": news.summary,
        "category": news.category,
        "image": news.image,
        "view_count": news.view_count,
        "created_at": news.created_at.isoformat() if news.created_at else None,
    }
