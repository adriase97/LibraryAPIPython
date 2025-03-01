from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.entities.base_entity import BaseEntity
from app.core.enums import genre

class Book(BaseEntity):
    __tablename__ = "books"

    # Properties
    title = Column(String, nullable=False, index=True, default="")
    publication_year = Column(Integer, nullable=False)
    isbn = Column(String, nullable=False, unique=True, default="")
    pages = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

    # Navigation
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", back_populates="books")

    # Collection
    book_publishers = relationship("BookPublisher", back_populates="book")
