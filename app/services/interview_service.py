from sqlalchemy.orm import Session
from app.models.interview import Interview


# create interview

def create_interview(db:Session,user_id:int,role:str,questions):
    interview=Interview(
        user_id=user_id,
        role=role,
        questions=questions,
        status="started"
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)


    return interview

# sumbit answer

def submit_answer(db:Session,interview_id:int,answer):
    interview = db.query(Interview).filter(Interview.id==interview_id).first()

    if not interview:
        return None
    
    interview.answers=answer
    interview.status="completed"

    db.commit()
    db.refresh(interview)

    
    return interview
