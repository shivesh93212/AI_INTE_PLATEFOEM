import os 
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME=os.getenv("APP_NAME")
    DEBUG: bool =os.getenv("DEBUG") =="True"

    DATABASE_URL: str = os.getenv("DATABASE_URL")

    CLERK_JWKS_URL:str = os.getenv("CLERK_JWKS_URL")

    CLOUDINARY_CLOUD_NAME: str = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY: str = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET: str = os.getenv("CLOUDINARY_API_SECRET")

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

settings=Settings()