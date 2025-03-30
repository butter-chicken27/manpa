from pydantic import BaseModel, EmailStr
from datetime import datetime
from sqlalchemy.orm import Session
from orm.user import User
from typing import Literal

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    role: str

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
    
    @classmethod
    def create(cls, db: Session, user_data: "UserBase") -> "UserResponse":
        new_user = User(**user_data.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return cls.from_orm(new_user)

    @classmethod
    def getAllUsers(cls, db: Session) -> list["UserResponse"]:
        users = db.query(User).all()
        return [cls.from_orm(user) for user in users]