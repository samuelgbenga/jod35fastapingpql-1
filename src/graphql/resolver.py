from fastapi import Depends
from strawberry import ID, Info

from src.db.main import get_session
from src.schemas.book_schema import BookSchema
from . import schemas
from typing import List
from src.models import book
from sqlmodel.ext.asyncio.session import AsyncSession
from src.service.book_service import BookService
from strawberry.exceptions import StrawberryException
from src.utils import schema_converter
from src.auth.service import UserService


book_service = BookService()

auth_service = UserService()


class QueryResolver:
    @staticmethod
    async def get_books():
        async with get_session() as session:  # Use `async with` directly
            allbooks = await book_service.get_all_books(session)
            return [
                schema_converter.to_BookSchemagql(book)
                for book in allbooks
            ]

    @staticmethod
    async def get_all_users():
        async with get_session() as session:  # Use `async with` directly
            allusers = await auth_service.get_all_users(session)
            return [
                schema_converter.to_Usergql(user)
                for user in allusers
            ]
        

    @staticmethod
    async def get_book(book_uid: str):
        async with get_session() as session:  # Use `async with` directly
            book = await book_service.get_book(book_uid, session)
            if book:
                return schema_converter.to_BookSchemagql(book)
            

class MutationResolver:
    @staticmethod
    async def add_book(new_book: schemas.UpdateBookSchema):
        book_for_service = schema_converter.to_BookSchema(new_book)
        async with get_session() as session:  # Use `async with` directly
            book = await book_service.create_book(book_for_service, session)
            if book:
                return schema_converter.to_BookSchemagql(book)  

    @staticmethod
    async def add_user(new_user: schemas.NewUsergql):
        user_for_service = schema_converter.to_UserSchema(new_user)
        async with get_session() as session:  # Use `async with` directly
            email = user_for_service.email
            isExist = await auth_service.user_exists(email, session)
            if isExist:
                return None
            else:
                user = await auth_service.create_user(user_for_service, session)
                if user:
                    return schema_converter.to_Usergql(user)              
    

    @staticmethod
    async def login_user(login_info: schemas.UserLoginModelgql):
        user_info_for_service = schema_converter.to_loginInfo(login_info)
        async with get_session() as session:  # Use `async with` directly
            login_resp = await auth_service.login_user(user_info_for_service, session)
            gqlResponse = schema_converter.to_loginResponsegql(login_resp)
            return gqlResponse

    @staticmethod
    async def update_book(book_uid: str, to_update:schemas.BookUpdateSchemagql ) :
       book_for_service = schema_converter.to_UpdateSchema(to_update)
       
       async with get_session() as session:  # Use `async with` directly
            book = await book_service.update_book(book_uid ,book_for_service, session)
            if book:
                return schema_converter.to_BookSchemagql(book)


    @staticmethod
    async def delete_book(book_uid: str)-> schemas.DeleteBookResponse:
        async with get_session() as session:  # Use `async with` directly
            book = await book_service.delete_book(book_uid, session)
            if book is None:
                return schemas.DeleteBookResponse(
                    success=False,
                    message=f"Book with uid {book_uid} not found or deletion failed."
                ) 
            else:
                return schemas.DeleteBookResponse(
                    success= True,
                    message = f"Book with uid {book_uid} has been deleted."
                )
        
