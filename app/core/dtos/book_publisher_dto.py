from pydantic import BaseModel
from datetime import date
from typing import Optional
from .book_dto import BookDTO
from .publisher_dto import PublisherDTO

class BookPublisherDTO(BaseModel):
    book_id: int
    publisher_id: int
    published_date: date
    book: Optional[BookDTO] = None
    publisher: Optional[PublisherDTO] = None
