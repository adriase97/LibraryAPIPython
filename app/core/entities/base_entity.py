from sqlalchemy import Column, Integer
from app.infrastructure.persistence import Base

class BaseEntity(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
