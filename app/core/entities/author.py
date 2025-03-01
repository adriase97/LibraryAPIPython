from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.core.entities.base_entity import BaseEntity

class Author(BaseEntity):
    __tablename__ = "authors"

    # Properties
    name = Column(String, nullable=False, index=True, default="")
    nationality = Column(String, nullable=False, default="")
    birth_date = Column(Date, nullable=False)
    biography = Column(String, nullable=False, default="")

    # Collection
    books = relationship("Book", back_populates="author")
