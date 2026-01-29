from pydantic import BaseModel, Field, EmailStr

class ConfCodeBase(BaseModel):
    email: str = Field(max_length=100)
    
class ConfCodeCreate(ConfCodeBase):
    code: int

class ConfCodeResponse(ConfCodeBase):
    pass

    class Config:
        from_attributes = True