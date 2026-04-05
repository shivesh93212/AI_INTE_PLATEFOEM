from fastapi import APIRouter , Depends
from app.deps.auth import get_current_user
from app.services.ai_service import generate_questions
import json

router=APIRouter()


@router.get("/questions")

async def get_questions(role:str,current_user=Depends(get_current_user)):
    try:
        raw_output=await generate_questions(role=role)

        questions = json.loads(raw_output)

        return {
            "role":role,
            "questions":questions
        }

    except Exception as e:
        raise Exception(f"status_code=500 detail=str(e)")