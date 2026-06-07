from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from typing import AsyncGenerator
from app.core.config import get_settings,Settings

_engine = create_async_engine(
    url=get_settings().construct_db_url,
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

