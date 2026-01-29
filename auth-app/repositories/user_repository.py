from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import Optional
from ..models.user import User
from ..database import pwd_acts

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_user(self, email: str, password: str):
        stmt = (select(User)
                .where(and_(User.email == email,
                            pwd_acts
                            .verify_password(password, User.password)))
                )
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user
    
    async def create_user(self, initials: str, email: str, password: str) -> User:
        new_user = User(
            initials=initials,
            email=email,
            password=pwd_acts.get_password_hash(password)
        )
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user
    