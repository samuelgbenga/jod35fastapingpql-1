
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
class Testing:
    samuel:str


@strawberry.input
class PaginationInput:
	offset: int
	limit: int

@strawberry.input
class UpdateBookSchema:
    content: Optional[str] = None
    is_done: Optional[bool] = None
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[str] = None
    page_count: Optional[int] = None
    language:Optional[str] = None
	