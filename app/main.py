from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse # todo: remove if not needed
from typing import List, Dict
from fastapi.staticfiles import StaticFiles
from database import Database
from orm.user import User
from models.user import UserBase, UserResponse

from db import User, create_db_and_tables
from schemas import UserCreate, UserRead, UserUpdate
from users import (
    SECRET,
    auth_backend,
    current_active_user,
    fastapi_users,
    google_oauth_client,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
    yield

db = Database()
app = FastAPI(lifespan=lifespan)

app.mount("/",StaticFiles(directory="static",html = True),name="static")

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