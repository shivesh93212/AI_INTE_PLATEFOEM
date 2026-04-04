from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

app=FastAPI()

from app.models import user
from app.routes import upload,user

app.include_router(user.router,prefix="/user",tags=["User"])
app.include_router(upload.router,prefix="/upload",tags=["Upload"])


Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message":"Welcome to FastAPI with SQLAlchemy!"}

