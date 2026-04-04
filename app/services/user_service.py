from sqlalchemy.orm import Session
from app.models.user import User


# grt user by clerk_id

def get_user_by_clerk_id(db:Session,clerk_id:str):
    return db.query(User).filter(User.clerk_id==clerk_id).first()


# create user

def create_user(db:Session,clerk_id:str,email:str,name:str=None):

    new_user=User(
        clerk_id=clerk_id,
        email=email,
        name=name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# main logic to create or get user

def get_or_create_user(db:Session,clerk_id:str,email:str,name:str=None):

    user=db.query(User).filter(User.clerk_id==clerk_id).first()

    if user:
        return user
    
    return create_user(db,clerk_id,email,name)