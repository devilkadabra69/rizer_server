from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from typing import AsyncGenerator

_engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@localhost:5432/rizer",
    echo=True
)

_session_locale = async_sessionmaker(
    bind=_engine,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_db() ->AsyncGenerator[AsyncSession]:
    async with _session_locale() as session:
        yield session

