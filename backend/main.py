from fastapi import FastAPI, Depends, HTTPException, APIRouter
# from sqlalchemy.orm import SessionS
from typing import List
# from model import Dynasty, Event
# from schema import DynastySchema, EventSchema
# from session import create_get_session
from starlette.middleware.cors import CORSMiddleware
# import random
# from sqlalchemy import func

from routers import dynasties, events

app = FastAPI()
router = APIRouter()

def _assert_dynasty_exists(dynasty: int):
    if dynasty is None:
        raise HTTPException(status_code=404, detail="Dynasty not found!")

#: Configure CORS
origins = [
    "http://localhost:8080",
    "https://htvisual-teddidodo.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Server is up and running!"}

app.include_router(
    dynasties.router,
    tags=[
        "dynasties"
    ],
)

app.include_router(
    events.router,
    tags=[
        "events"
    ],
)
