from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from settings import settings

engine = create_async_engine(settings.DATABASE_SQLITE_URL)
session = sessionmaker(
    bind=engine,
    future=True,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)

Base = declarative_base()
