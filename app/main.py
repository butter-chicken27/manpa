from fastapi import FastAPI, HTTPException
from typing import List, Dict
from models import MsgPayload
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from database import Database2
import pyodbc


db = Database2()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    db.connect()
    yield
    # Shutdown
    db.disconnect()

app = FastAPI(lifespan=lifespan)

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
    try:
        with db.get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO Users (FirstName, LastName) VALUES (?, ?)", 
                msg_name, 'test'
            )
            msg_id = cursor.fetchone()[0]
            return {
                "message": {
                    "first_name": msg_name,
                    "last_name": "test"
                }
            }
    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/messages")
def message_items() -> Dict[str, List[Dict[str, str]]]:
    try:
        with db.get_cursor() as cursor:
            cursor.execute("SELECT * FROM Users")
            rows = cursor.fetchall()
            messages = [
                {
                    "first_name": row.FirstName,
                    "last_name": row.LastName
                } for row in rows
            ]
            return {"messages": messages}
    except pyodbc.Error as e:
        raise HTTPException(status_code=500, detail=str(e))