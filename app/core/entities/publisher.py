from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.entities.base_entity import BaseEntity

class Publisher(BaseEntity):
    __tablename__ = "publishers"

    # Properties
    name = Column(String, nullable=False, index=True, default="")
    country = Column(String, nullable=False, default="")
    founded_year = Column(Integer, nullable=False)
    website = Column(String, nullable=False, default="")

    # Collection
    book_publishers = relationship("BookPublisher", back_populates="publisher")
