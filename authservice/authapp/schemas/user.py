from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    initials: str = Field(max_length=100)
    email: EmailStr = Field(max_length=100)
    password: str = Field(min_length=6, max_length=100)

class UserCreate(UserBase):
    code: int = Field(max_length=6)

class UserResponse(UserBase):
    id: int = Field(...,description="Unique user identifier")
    
    class Config:
        from_attributes = True