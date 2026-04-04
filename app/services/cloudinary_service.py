import cloudinary 
import cloudinary.uploader
from app.core.config import settings

# configure Cloudinary

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET
)

# upload file function 

def upload_file(file):
    try:
        if not file.name.endswith((".pdf",".doc",".docx")):
            raise Exception("Invalid file type. Only PDF and Word documents are allowed.")
        
        
        result=cloudinary.uploader.upload(
            file,
            resource_type="auto",
            folder="resumes"
            )

        return result.get("secure_url")
    except Exception as e:
        raise Exception(f"Cloudinary upload failed:{str(e)}")
    
