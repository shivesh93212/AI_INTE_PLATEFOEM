from sqlalchemy import Column , String , Integer , ForeignKey, DateTime , JSON
from datetime import datetime
from app.db.base import Base



class Interview(Base):
    __tablename__="interviews"

    id=Column(Integer,primary_key=True,indes=True)

    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)

    role=Column(String,nullable=False)

    questions=Column(JSON,nullable=False)

    answers=Column(JSON,nullable=True)

    status=Column(String,default="started")

    created_at=Column(DateTime,default=datetime.utcnow())