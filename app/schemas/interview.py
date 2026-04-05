from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime

class Question(BaseModel):
    questions:str

class InterviewCreate(BaseModel):
    role:str
    questions:List[Question]

class AnswerInput(BaseModel):
    answers:List[str]


class InterviewResponse(BaseModel):
    id:int
    role:str
    questions:List[Question]
    answers:Optional[List[str]]
    status:str
    created_at:datetime

    class config:
        from_attributes=True





