from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_session
from ..schemas.user import UserBase, UserCreate
from ..repositories import *

user_router = APIRouter(
    prefix="/api/user",
    tags=["user"]
)

@user_router.post("/login")
async def login_user(user: UserBase, db: AsyncSession = Depends(get_session)):
    ...
    
@user_router.post("/register")
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_session)):
    code_service = CodeRepository(db)
    code = await code_service.get_code_by_email(user.email)
    print(code)
    user_service = UserRepository(db)
    return await user_service.create_user(user.initials, user.email, user.password)