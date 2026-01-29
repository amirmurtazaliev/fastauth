from pydantic import BaseModel, Field, EmailStr

class EmailVerifyBase(BaseModel):
    email: str = Field(max_length=100)
    
class SendConfCode(EmailVerifyBase):
    pass

class EmailVerifyResponse(EmailVerifyBase):
    pass

    class Config:
        from_attributes = True