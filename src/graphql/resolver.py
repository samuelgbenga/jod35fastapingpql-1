from fastapi import Depends
from strawberry import ID, Info

from src.db.main import get_session
from . import schemas
from typing import List
from src.models import book
from sqlmodel.ext.asyncio.session import AsyncSession
from src.service.book_service import BookService


book_service = BookService()

class QueryResolver:
    @staticmethod
    async def get_books():
        async with get_session() as session:  # Use `async with` directly
            allbooks = await book_service.get_all_books(session)

            return [
                schemas.BookSchemagql(
                    uid=book.uid,
                    title=book.title,
                    author=book.author,
                    publisher=book.publisher,
                    published_date=book.published_date,
                    page_count=book.page_count,
                    language=book.language,
                    created_at=book.created_at,
                    updated_at=book.updated_at
                )
                for book in allbooks
            ]

       
        

    @staticmethod
    def get_book():
       newBook: schemas.Testing = schemas.Testing(samuel="samuel")
       return newBook


class MutationResolver:
    @staticmethod
    def add_book():
        pass

    @staticmethod
    def update_book() :
        pass

    @staticmethod
    def delete_book():
        pass
        
