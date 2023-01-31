from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from settings import settings


engine = create_async_engine(settings.DATABASE_SQLITE_URL)
session = sessionmaker(
    bind=engine,
    future=True,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False
)

Base = declarative_base()
