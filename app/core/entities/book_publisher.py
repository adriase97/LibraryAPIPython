from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.infrastructure.persistence import Base

class BookPublisher(Base):
    __tablename__ = "book_publishers"

    # Foreign Keys
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    publisher_id = Column(Integer, ForeignKey("publishers.id"), primary_key=True)

    # Additional properties
    published_date = Column(Date, nullable=False)

    # Navigation
    book = relationship("Book", back_populates="book_publishers")
    publisher = relationship("Publisher", back_populates="book_publishers")
