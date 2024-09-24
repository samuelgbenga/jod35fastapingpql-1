
from datetime import datetime
from typing import Optional
import uuid
import strawberry


@strawberry.type
class BookSchemagql:
    uid:uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language:str
    created_at: datetime
    updated_at:datetime

@strawberry.type
class GeneralResponse:
    message:str


@strawberry.input
class PaginationInput:
	offset: int
	limit: int

@strawberry.input
class UpdateBookSchema:
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[str] = None
    page_count: Optional[int] = None
    language:Optional[str] = None

@strawberry.input
class BookUpdateSchemagql:
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None

@strawberry.type
class DeleteBookResponse:
    success: bool
    message: str
