from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    coins = Column(Integer, default=50)
    is_premium = Column(Boolean, default=False)
    premium_until = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)