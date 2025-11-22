from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from config import settings


database_url: str = settings.database_dsn
"""URL базы данных"""
engine = create_async_engine(url=database_url, echo="debug", pool_pre_ping=True)
"""Асинхронный движок SQLAlchemy"""
# Фабрика асинхронных сессий
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Асинхронный генератор сессий для FastAPI через Depends.

    Yields:
        AsyncSession: Асинхронная сессия SQLAlchemy.
    """
    async with async_session_maker() as session:
        yield session
