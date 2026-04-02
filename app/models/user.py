from sqlalchemy import Column , String ,Integer,DateTime
from app.db.base import Base
from datetime import datetime

class User(Base):
    __tablename__="users"

    id=Column(Integer,index=True,primary_key=True)
    clerk_id=Column(String,nullable=False,unique=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
    profile_image=Column(String,nullable=True)
    resume_url=Column(String,nullable=True)
    created_at=Column(DateTime,default=datetime.utcnow)
    