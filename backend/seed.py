"""Seed the database with sample data for development."""
import asyncio
import sys
from pathlib import Path

# Ensure the app module is importable
sys.path.insert(0, str(Path(__file__).parent))

from app.database import Base, async_session_factory, engine
from app.models.product import Category, Product
from app.models.news import News
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session_factory() as session:
        # Check if data already exists
        from sqlalchemy import select
        result = await session.execute(select(Product).limit(1))
        if result.scalar_one_or_none():
            print("Data already seeded, skipping.")
            return

        # Categories
        categories = [
            Category(name="微控制器"),
            Category(name="存储器"),
            Category(name="电源管理"),
            Category(name="数据转换"),
            Category(name="传感器"),
            Category(name="光电器件"),
            Category(name="二极管"),
            Category(name="晶体管"),
            Category(name="电阻"),
            Category(name="电容"),
            Category(name="连接器"),
            Category(name="模块"),
        ]
        session.add_all(categories)

        # Hot Products - FUJI IGBT modules (matching real data)
        products = [
            Product(name="IGBT管/模块", model="FGW75XS120C", brand="FUJI(富士电机)", price=16.905, stock=7200, category="IGBT管/模块", is_hot=True),
            Product(name="IGBT管/模块", model="FGW50XS65C", brand="FUJI(富士电机)", price=8.1995, stock=12000, category="IGBT管/模块", is_hot=True),
            Product(name="IGBT管/模块", model="FGW75XS65D", brand="FUJI(富士电机)", price=13.8345, stock=1200, category="IGBT管/模块", is_hot=True),
            Product(name="IGBT管/模块", model="FGW75XS65C", brand="FUJI(富士电机)", price=10.603, stock=4800, category="IGBT管/模块", is_hot=True),
            Product(name="IGBT管/模块", model="FGW40XS120C", brand="FUJI(富士电机)", price=10.1545, stock=2400, category="IGBT管/模块", is_hot=True),
            Product(name="IGBT管/模块", model="FGW40N120HD", brand="FUJI(富士电机)", price=19.09, stock=4800, category="IGBT管/模块", is_hot=True),
            Product(name="IGBT管/模块", model="FGZ75XS120C", brand="FUJI(富士电机)", price=27.485, stock=200, category="IGBT管/模块", is_hot=True),
            Product(name="IGBT管/模块", model="2MBI600VN-120-50", brand="FUJI(富士电机)", price=603.75, stock=78, category="IGBT管/模块", is_hot=True),
            Product(name="IGBT管/模块", model="FGW40N120WD", brand="FUJI(富士电机)", price=14.03, stock=4800, category="IGBT管/模块", is_hot=True),
            Product(name="场效应管(MOSFET)", model="FMW60N027S2FDHF", brand="FUJI(富士电机)", price=34.7645, stock=1800, category="场效应管(MOSFET)", is_hot=True),
            # More products from other brands
            Product(name="MCU", model="STM32F103C8T6", brand="ST(意法半导体)", price=12.50, stock=5000, category="微控制器", is_hot=True),
            Product(name="MCU", model="STM32F407VGT6", brand="ST(意法半导体)", price=45.00, stock=2000, category="微控制器", is_hot=True),
            Product(name="运算放大器", model="LM358DR", brand="TI(德州仪器)", price=0.85, stock=50000, category="放大器", is_hot=True),
            Product(name="电压基准", model="TL431AIDBZR", brand="TI(德州仪器)", price=0.65, stock=80000, category="电源管理", is_hot=True),
            Product(name="MLCC电容", model="CL10A106KP8NNNC", brand="三星(Samsung)", price=0.12, stock=200000, category="电容", is_hot=True),
            Product(name="电阻", model="RC0603FR-0710KL", brand="国巨(Yageo)", price=0.01, stock=1000000, category="电阻", is_hot=True),
        ]
        session.add_all(products)

        # News articles
        news_items = [
            News(title="一文读懂亚德诺半导体（ADI）公司、核心产品、运用领域",
                 summary="亚德诺半导体是全球领先的高性能模拟、混合信号和数字信号处理集成电路设计、制造和营销厂商。",
                 category="品牌资讯",
                 content="亚德诺半导体（ADI）是全球领先的高性能模拟技术公司...",
                 view_count=3521),
            News(title="一文读懂什么是光模块、内部结构、所用器件、用途？",
                 summary="光模块是光纤通信系统中的核心器件，完成光电转换功能。",
                 category="行业资讯",
                 content="光模块，全称光收发一体模块，是光纤通信系统中的核心器件...",
                 view_count=5632),
            News(title="MDD辰达半导体推出低内阻、高开关频率MOS管",
                 summary="MDD辰达半导体推出新型MOS管产品，适用于车载电源系统。",
                 category="品牌资讯",
                 content="MDD辰达半导体最新推出低内阻、高开关频率MOS管系列...",
                 view_count=243),
            News(title="国产FPGA公司、核心产品、应用介绍",
                 summary="详细介绍国产FPGA主要厂商及其产品线。",
                 category="行业资讯",
                 content="随着国产替代进程加速，国产FPGA厂商正在快速发展...",
                 view_count=4499),
            News(title="芯伯乐高效3A降压方案：XBL2596 PCB设计指南",
                 summary="XBL2596降压转换器的PCB设计要点和应用指南。",
                 category="产品资讯",
                 content="XBL2596是一款高效3A降压转换器...",
                 view_count=179),
            News(title="Infineon英飞凌 IMW65R010M2H 产品介绍",
                 summary="英飞凌CoolSiC™ MOSFET IMW65R010M2H产品特性与应用。",
                 category="产品资讯",
                 content="IMW65R010M2H是英飞凌推出的CoolSiC™ MOSFET...",
                 view_count=377),
            News(title="一文读懂DRAM工作原理、分类、主要厂商",
                 summary="全面介绍DRAM存储器的工作原理、分类及主要厂商。",
                 category="行业资讯",
                 content="DRAM（动态随机存取存储器）是计算机系统中最重要的存储器之一...",
                 view_count=1990),
            News(title="万联芯城2026年劳动节放假通知",
                 summary="万联芯城2026年劳动节放假安排通知。",
                 category="公司动态",
                 content="尊敬的客户：根据国家法定节假日规定...",
                 view_count=102),
        ]
        session.add_all(news_items)

        # Demo user
        demo_user = User(
            username="demo",
            password=pwd_context.hash("demo123"),
            email="demo@wlxmall.com",
            phone="4000-306-326",
            company="万联芯城",
        )
        session.add(demo_user)

        await session.commit()
        print(f"Seeded: {len(categories)} categories, {len(products)} products, {len(news_items)} news, 1 user")
        print("Demo account: username=demo, password=demo123")


if __name__ == "__main__":
    asyncio.run(seed())
