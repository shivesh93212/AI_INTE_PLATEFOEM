from fastapi import APIRouter , Depends,UploadFile,File,HTTPException
from app.services.cloudinary_service import upload_file
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.deps.auth import get_current_user


router=APIRouter()
@router.post("/resume")
def upload_resume(file:UploadFile=File(...),
                  current_user=Depends(get_current_user),
                  db:Session=Depends(get_db)):
    
    try:
        # upload file
        
        file_url=upload_file(file.file)

        # update user in db

        user=db.query(User).filter(User.clerk_id==current_user.clerk_id).first()

        if not user:
            raise HTTPException(status_code=404,detail="User not found")
        
        user.resume_url=file_url
        db.commit()

        return {
            "message":"Resume uploaded successfully",
            "resume_url":file_url
        }
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))


    