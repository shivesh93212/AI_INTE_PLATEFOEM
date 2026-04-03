from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from app.core.security import verify_token 

security=HTTPBearer()

async def get_current_user(credentials:HTTPAuthorizationCredentials=Depends(security)):

    token = credentials.credentials

    try:
        payload=await verify_token(token)
        clerk_id=payload.get("sub")
        if not clerk_id:
            raise HTTPException(401, detail="Invalid token")
        return {
            "clerk_id": clerk_id,
            "email": payload.get("email"),
        }
    except Exception:
        raise HTTPException(401, detail="token verification failed")