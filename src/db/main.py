from contextlib import asynccontextmanager
from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from src.config.loadenv import Config
from sqlmodel import SQLModel
from src.models.book import Book
from src.auth.models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator


engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True
)

async def initdb():
    """create a our db model in the postgress db"""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]: # type: ignore
    """Dependency to provide the session object"""
    async_session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False # type: ignore
    ) # type: ignore
    async with async_session() as session: # type: ignore
        yield session # type: ignore
