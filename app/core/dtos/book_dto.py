from pydantic import BaseModel, Field, condecimal
from typing import List, Optional
from .author_dto import AuthorDTO
from .book_publisher_dto import BookPublisherDTO
from ..enums import Genre

class BookDTO(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., max_length=200)
    publication_year: int
    isbn: str = Field(..., max_length=13)
    pages: int
    genre: Genre
    price: condecimal(gt=0)
    author_id: int
    author: Optional[AuthorDTO] = None
    book_publishers: List[BookPublisherDTO] = Field(default_factory=list)
