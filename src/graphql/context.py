# src/graphql/context.py
from multiprocessing.context import BaseContext
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Depends
import strawberry
import strawberry.types
from src.db.main import get_session


class Context(BaseContext): 
    def __init__(self, session: AsyncSession):
        self.session = session

async def get_context(session: AsyncSession = Depends(get_session)) -> Context:
    return Context(session=session)
