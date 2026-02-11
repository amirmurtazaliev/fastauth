from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import Optional
from ..models.conf_code import ConfCode

class CodeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def get_code_by_email(self, email: str) -> Optional[int]:
        stmt = select(ConfCode).filter(ConfCode.user_email == email).order_by(ConfCode.created_at.desc()).limit(1)
        result = await self.session.execute(stmt)
        res = result.scalar_one_or_none()
        if res:
            return res.code

    async def create_code(self, email: str, code: int) -> ConfCode:
        new_code = ConfCode(
            user_email=email,
            code=code
        )
        self.session.add(new_code)
        await self.session.commit()
        await self.session.refresh(new_code)
        return new_code