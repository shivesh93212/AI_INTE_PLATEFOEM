from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from app.core.security import verify_token 
from app.services.user_service import get_or_create_user
from app.db.session import get_db
from sqlalchemy.orm import Session

security=HTTPBearer()

async def get_current_user(credentials:HTTPAuthorizationCredentials=Depends(security),db:Session=Depends(get_db)):

    token = credentials.credentials

    try:
        payload=await verify_token(token)
        clerk_id=payload.get("sub")
        email=payload.get("email")
        if not clerk_id:
            raise HTTPException(401, detail="Invalid token")
        
        user=get_or_create_user(db,clerk_id,email)
        return user
    except Exception:
        raise HTTPException(401, detail="token verification failed")