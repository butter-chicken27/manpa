from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse # todo: remove if not needed
from typing import List, Dict
from fastapi.staticfiles import StaticFiles
from database import Database
from orm.user import User
from models.user import UserBase, UserResponse

db = Database()
app = FastAPI()

app.mount("/app",StaticFiles(directory="static",html = True),name="static")

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello"}


# About page route
@app.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}


# Route to add a message
@app.post("/users", response_model=UserResponse)
def add_user(user_data: UserBase) -> UserResponse:
    with db.getSession() as session:
        try:
            return UserResponse.create(session, user_data)
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/users", response_model=List[UserResponse])
def get_users() -> List[UserResponse]:
    with db.getSession() as session:
        try:
            return UserResponse.getAllUsers(session)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))