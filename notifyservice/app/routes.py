from fastapi import APIRouter
from .notifserver import send_message
from .schemas import MessageData

router = APIRouter(
    prefix="/api",
    tags=["notif-service"]
)

@router.post("/sendmsg")
def send_msg(message_data: MessageData):
    is_sended = send_message(
        message_data.sender_name,
        message_data.recipiemt_email,
        message_data.message
        )
    if is_sended[0]:
        return {"msg": "message sended"}
    return {"msg": "message not sended", "error": is_sended[1]}