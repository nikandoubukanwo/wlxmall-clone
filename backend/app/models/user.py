from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(200), nullable=False)
    email = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    company = Column(String(200), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
