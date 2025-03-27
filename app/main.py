import uvicorn
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from models import MsgPayload
from fastapi.responses import JSONResponse # todo: remove if not needed
from typing import List, Dict
from fastapi.staticfiles import StaticFiles
from database import Database
from orm.user import DBUser

from db import User, create_db_and_tables
from schemas import UserCreate, UserRead, UserUpdate
from users import (
    SECRET,
    auth_backend,
    current_active_user,
    fastapi_users,
    google_oauth_client,
)

import os
from dotenv import load_dotenv

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
    yield

db = Database()
app = FastAPI(lifespan=lifespan)
messages_list: dict[int, MsgPayload] = {}

app.mount("/app",StaticFiles(directory="static",html = True),name="static")
app.mount("/redirect",StaticFiles(directory="static",html = True),name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
app.include_router(
    fastapi_users.get_oauth_router(google_oauth_client, auth_backend, SECRET, "https://www.manpa.co.in/redirect", associate_by_email=True, is_verified_by_default=True),
    prefix="/auth/google",
    tags=["auth"],
)

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello"}


# About page route
@app.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}


# Route to add a message
@app.post("/messages/{msg_name}/")
def add_msg(msg_name: str) -> Dict:
    session = db.getSession()
    try:
        details = {"firstName": msg_name, "lastName": "test"}
        user = DBUser(**details)
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"message": {"first_name": user.firstName, "last_name": user.lastName}}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()

@app.get("/messages")
def message_items() -> Dict[str, List[Dict[str, str]]]:
    try:
        with db.getSession() as session:
            users = session.query(DBUser).all()
            messages = [
                {
                    "first_name": user.firstName,
                    "last_name": user.lastName
                } for user in users
            ]
            return {"messages": messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
