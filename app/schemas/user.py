from pydantic import BaseModel,EmailStr   
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    name:Optional[str] =None
    email:EmailStr


class UserCreate(BaseModel):
    clerk_id:str


class UserResponse(BaseModel):
    id:int
    clerk_id:str
    profile_image:Optional[str] =None
    resume_url:Optional[str] =None
    created_at:datetime
    

    class Config:
        from_attributes=True
