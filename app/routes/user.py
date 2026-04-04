from fastapi import APIRouter,Depends
from app.services.user_service import get_or_create_user
from app.schemas.user import UserResponse
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.deps.auth import get_current_user


router=APIRouter()

@router.get("/me",response_model=UserResponse)

def get_me(current_user=Depends(get_current_user),db:Session=Depends(get_db)):

    user=get_or_create_user(db=db,clerk_id=current_user.clerk_id,email=current_user.email,name=None)

    return user

