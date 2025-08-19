import os
import asyncio
from collections.abc import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)


class Base(DeclarativeBase): pass

ENGINE = create_async_engine(os.environ["DB_URL"], echo=True)
ASYNC_SESSION_MAKER = async_sessionmaker(ENGINE, expire_on_commit=False)

async def create_db_and_tables():
    async with ENGINE.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
asyncio.run(create_db_and_tables())

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with ASYNC_SESSION_MAKER() as session:
        yield session