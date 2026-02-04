from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.code_repository import CodeRepository
from ..schemas.email_verify import ConfCodeCreate, ConfCodeResponse

class CodeService:
    def __init__(self, session: AsyncSession):
        self.repository = CodeRepository(session)
        
    async def get_code(self, data: ConfCodeCreate):
        code = await self.repository.get_code_by_email(data)
        return ConfCodeResponse.model_validate(code)
    
    async def create_code(self, data: ConfCodeCreate):
        code = await self.repository.create_code(data)
        return ConfCodeResponse.model_validate(code)