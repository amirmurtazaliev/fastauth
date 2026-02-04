import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import settings

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from passlib.context import CryptContext

async_engine = create_async_engine(
    url=settings.get_database_url,
    echo=True
)

SessionLocal = async_sessionmaker(bind=async_engine, autoflush=False)

class Base(DeclarativeBase):
    pass

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
async def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Password:
    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

pwd_acts = Password()
if __name__ == "__main__":
    asyncio.run(init_db())
