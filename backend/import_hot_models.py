"""Import hot search models from Excel into the database.

Reads 6月11热门型号.xlsx and creates Product records with is_hot=True.
Skips the 搜索次数(30日) and 搜索公司数(30日) columns.
"""
import asyncio
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).parent))

from app.database import async_session_factory, engine
from app.models.product import Product


EXCEL_PATH = Path(__file__).parent.parent / "6月11热门型号.xlsx"


async def import_hot_models():
    """Read Excel and insert hot models into the database."""
    wb = openpyxl.load_workbook(EXCEL_PATH)
    ws = wb["Sheet1"]

    rows = list(ws.iter_rows(min_row=2, values_only=True))  # skip header
    total = len(rows)
    print(f"Read {total} rows from Excel")

    async with async_session_factory() as session:
        # Check existing hot products count
        from sqlalchemy import select, func

        result = await session.execute(select(func.count(Product.id)).where(Product.is_hot == True))
        existing = result.scalar()
        if existing:
            print(f"Found {existing} existing hot products. Clearing them first...")
            await session.execute(
                Product.__table__.delete().where(Product.is_hot == True)
            )
            await session.commit()
            print("Cleared existing hot products.")

        # Build product list
        products = []
        skipped = 0
        for row in rows:
            rank, model, brand, package, *_ = row  # ignore search count columns
            if not model or not str(model).strip():
                skipped += 1
                continue

            products.append(
                Product(
                    name=str(model).strip(),
                    model=str(model).strip(),
                    brand=str(brand).strip() if brand else "",
                    pkg=str(package).strip() if package else "",
                    description=str(package).strip() if package else "",
                    is_hot=True,
                    price=0,
                    stock=0,
                )
            )

        # Insert in batches to keep memory manageable (50k+ rows)
        BATCH = 1000
        inserted = 0
        for i in range(0, len(products), BATCH):
            batch = products[i : i + BATCH]
            session.add_all(batch)
            await session.commit()
            inserted += len(batch)
            print(f"  Inserted {inserted}/{len(products)}...")

        print(f"\nDone! Inserted {inserted} hot models. Skipped {skipped} empty rows.")


if __name__ == "__main__":
    asyncio.run(import_hot_models())
