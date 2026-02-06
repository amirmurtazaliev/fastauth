import random
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.code_repository import CodeRepository
from ..schemas.email_verify import ConfCodeBase
from ..http_client import NotifyHTTPClient
from ..database import get_session
from ..config import settings

http_client = NotifyHTTPClient("http://127.0.0.1:8000/api/")

emailver_router = APIRouter(
    prefix="/api/emailver",
    tags=["verifyemail"]
)

@emailver_router.post("/verify_email")
async def check_email(data: ConfCodeBase, db: AsyncSession = Depends(get_session)):
    code = random.randint(1000, 9999)
    service = CodeRepository(db)
    await service.create_code(data.email, code)
    send_data = {
        "sender_name": settings.app_name,
        "recipient_email": data.email,
        "message": f"code: {code}"
    }
    res = await http_client.send_post_request("sendmsg", send_data)
    return res
    