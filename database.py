from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


_engine = create_async_engine("sqlite+aiosqlite://./db.sqlite", echo=True)

async_session = async_sessionmaker(_engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass
