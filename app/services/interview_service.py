import json
from sqlalchemy.orm import Session
from app.models.interview import Interview
from app.services.ai_service import evaluate_answer

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


# submit ans and evaluate

async def submit_and_evaluate(db,interview,answer):
    interview.answers=answer
    interview.status="completed"

    # evaluate answer using ai service
    raw_feedback = await evaluate_answer(interview.questions, answers)

    feedback = json.loads(raw_feedback)

    # Store feedback
    interview.score = feedback.get("score")
    interview.feedback = feedback

    db.commit()
    db.refresh(interview)

    return interview