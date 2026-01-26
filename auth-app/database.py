from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from ..config import settings

async_engine = create_async_engine(
    url=settings.get_database_url
)

SessionLocal = async_sessionmaker(bind=async_engine, autoflush=False)

class Base(DeclarativeBase):
    pass

def init_db():
    Base.metadata.create_all(bind=async_engine)
    
async def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()