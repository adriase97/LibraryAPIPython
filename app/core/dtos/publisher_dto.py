from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional
from .book_publisher_dto import BookPublisherDTO

class PublisherDTO(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., max_length=150, description="Name of the publisher")
    country: str = Field(..., max_length=100, description="Country of the publisher")
    founded_year: int = Field(..., description="Year of foundation")
    website: HttpUrl = Field(..., description="Publisher's website")
    book_publishers: List[BookPublisherDTO] = Field(default_factory=list, description="Relationship with published books")
