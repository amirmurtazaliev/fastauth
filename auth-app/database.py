from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from passlib.context import CryptContext
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
    yield session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Password:
    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

pwd_acts = Password()
