from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional
from .book_dto import BookDTO

class AuthorDTO(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., max_length=100)
    nationality: str = Field(..., max_length=50)
    birth_date: date
    biography: str = Field(..., max_length=1000)
    books: List[BookDTO] = Field(default_factory=list)
