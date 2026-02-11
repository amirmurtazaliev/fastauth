from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_session
from ..schemas.user import UserBase, UserCreate
from ..repositories import *
from ..auth import security, auth_config

user_router = APIRouter(
    prefix="/api/user",
    tags=["user"]
)

@user_router.post("/login")
async def login_user(user_data: UserBase, response: Response, db: AsyncSession = Depends(get_session)):
    user_service = UserRepository(db)
    user = user_service.get_user(user_data.email, user_data.password)
    if user:
        token = security.create_access_token(uid=str(user))
        response.set_cookie(auth_config.JWT_ACCESS_COOKIE_NAME, token)
        return user
    
@user_router.post("/register")
async def register_user(user: UserCreate, response: Response, db: AsyncSession = Depends(get_session)):
    code_service = CodeRepository(db)
    user_service = UserRepository(db)
    code = await code_service.get_code_by_email(user.email)
    if code == user.code:
        new_user = await user_service.create_user(user.initials, user.email, user.password)
        token = security.create_access_token(uid=str(new_user.id))
        response.set_cookie(auth_config.JWT_ACCESS_COOKIE_NAME, token)
        return new_user.id