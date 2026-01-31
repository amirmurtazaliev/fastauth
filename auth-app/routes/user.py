from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_session
from ..schemas.user import UserBase, UserCreate
from ..services.user_service import UserService

router = APIRouter(
    prefix="/api/user",
    tags=["user"]
)

@router.post("/login")
async def login_user(user: UserBase, db: AsyncSession = Depends(get_session)):
    ...
    
@router.post("/register")
async def register_user(user: UserBase, db: AsyncSession = Depends(get_session)):
    service = UserService(db)
    return service.create_user(user)