
from datetime import datetime
from typing import Optional
import uuid
from fastapi.responses import JSONResponse
from pydantic import Field
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
class Usergql:
    uid: uuid.UUID
    username: str
    first_name: str
    last_name: str
    middle_name: str 
    is_verified: bool 
    email: str
    password_hash: str
    created_at: datetime

@strawberry.type
class LoginResponsegql:
    message: str
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    email: Optional[str] = None
    uid: Optional[str] = None
    


@strawberry.input
class NewUsergql:
    username: str
    first_name: str
    last_name: str
    middle_name: str 
    email: str
    password: str

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

@strawberry.input
class UserLoginModelgql:
    email: str = Field(max_length=40)
    password: str  = Field(min_length=6)


