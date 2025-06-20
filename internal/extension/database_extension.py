
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings
from pkg.sqlalchemy import SQLAlchemy

async_engine=create_async_engine(settings.SQLALCHEMY_URL,**settings.SQLALCHEMY_ENGINE_OPTIONS)
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

db=SQLAlchemy(engine=async_engine,async_session_local=AsyncSessionLocal)