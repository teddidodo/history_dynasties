from fastapi import FastAPI
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from model import Dynasty, Event
from schema import DynastySchema, EventSchema
from session import create_get_session
from starlette.middleware.cors import CORSMiddleware
import random
from sqlalchemy import func

app = FastAPI()

def _assert_dynasty_exists(dynasty: int):
    if dynasty is None:
        raise HTTPException(status_code=404, detail="Dynasty not found!")

#: Configure CORS
origins = [
    "http://localhost:8080",
    "https://htvisual-teddidodo.vercel.app"
]

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Server is up and running!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/dynasties/', status_code=200)
async def get_dynasties(db: Session = Depends(create_get_session)):
    dynasties = db.query(Dynasty).all()
    return dynasties

@app.get('/random/dynasty', status_code=200)
async def get_dynasties(db: Session = Depends(create_get_session)):
    random_dynasties_idx = random.randint(0, 8)
    dynasty = db.query(Dynasty).filter(Dynasty.id==random_dynasties_idx).one_or_none()
    return dynasty

@app.get('/dynasties/{dynasty}', status_code=200)
async def get_dynasty(dynasty: str, db: Session = Depends(create_get_session)):
    dynasty = dynasty.lower()
    dynasty = db.query(Dynasty).filter(func.lower(Dynasty.name).like("%" + dynasty + "%")).one_or_none()
    _assert_dynasty_exists(dynasty)
    return dynasty


@app.get('/events/{dynasty}', status_code=200)
async def get_dynasties(dynasty: str, db: Session = Depends(create_get_session)):
    dynasty = dynasty.lower()
    dynasty_id = db.query(Dynasty.id).filter(func.lower(Dynasty.name).like("%" + dynasty + "%")).one_or_none()
    _assert_dynasty_exists(dynasty_id)   
    dynasty_id = dynasty_id.id
    events = db.query(Event).filter(Event.dynasty_id == dynasty_id).all()
    # Split the timeline into the period
    period_dict = {}
    for event in events:
        if event.period in period_dict:
            period_dict[event.period].append(event)
        else:
            period_dict[event.period] = []
            period_dict[event.period].append(event)
    return period_dict

@app.get("/events", status_code=200)
async def get_events(db: Session = Depends(create_get_session)):
   events = db.query(Event).all()
   return events
