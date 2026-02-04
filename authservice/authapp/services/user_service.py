from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.user_repository import UserRepository
from ..schemas.user import UserCreate, UserResponse

class UserService:
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)
        
    async def get_user(self, user_data: UserCreate) -> UserResponse:
        user = await self.repository.get_user(user_data)
        return UserResponse.model_validate(user)
    
    async def create_user(self, initials, email, password) -> UserResponse:
        user = await self.repository.create_user(initials, email, password)
        return user