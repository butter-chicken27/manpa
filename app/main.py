from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse # todo: remove if not needed
from typing import List, Dict
from fastapi.staticfiles import StaticFiles
from database import Database
from orm.user import User

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
@app.post("/messages/{msg_name}/")
def add_msg(msg_name: str) -> Dict:
    with db.getSession() as session:
        try:
            details = {"first_name": msg_name, "last_name": "test", "email": "vik@g.com", "role": "client"}
            user = User(**details)
            session.add(user)
            session.commit()
            session.refresh(user)
            return {"message": {"first_name": user.first_name, "last_name": user.last_name}}
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=str(e))

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