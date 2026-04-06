from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps.auth import get_current_user
from app.db.session import get_db
from app.services.interview_service import create_interview,submit_answer
from app.services.user_service import get_or_create_user
from app.schemas.interview import InterviewCreate,AnswerInput,InterviewResponse
from backend.app.models.interview import Interview
from app.services.interview_service import submit_and_evaluate

router=APIRouter()

@router.post("/start",response_model=InterviewResponse)
async def start_interview(
    data:InterviewCreate,
    current_user=Depends(get_current_user),
    db:Session=Depends(get_db)
):
    user=get_or_create_user(
        db,
        clerk_id=current_user["clerk_id"],
        email=current_user["email"],
    )

    interview=create_interview(
        db,
        user_id=user.id,
        role=data.role,
        questions=[q.dict() for q in data.questions]

    )
    return interview



@router.post("/{interview_id}/submit", response_model=InterviewResponse)
async def submit_interview(
    interview_id: int,
    data: AnswerInput,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    interview = db.query(Interview).filter(Interview.id == interview_id).first()

    if not interview:
        raise HTTPException(status_code=404, detail="Interview not found")

    interview = await submit_and_evaluate(
        db,
        interview,
        data.answers
    )

    return interview
