from sqlalchemy import Column, DateTime, Integer, String, Text, func
from app.database import Base


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(300), nullable=False)
    content = Column(Text, nullable=True)
    summary = Column(String(500), nullable=True)
    category = Column(String(50), nullable=False, comment="品牌资讯/行业资讯/产品资讯")
    image = Column(String(500), nullable=True)
    view_count = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())
