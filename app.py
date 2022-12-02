# python3 -m uvicorn src.app:app --reload
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Dynasty as SchemaDynasty
from schema import Events as SchemaEvents

from schema import Dynasty
from schema import Events
from model import Dynasty as ModelDynasty, Events as ModelEvents
from typing import List
import os
from dotenv import load_dotenv

from starlette.middleware.cors import CORSMiddleware
import random

from sqlalchemy import func
from dotenv import load_dotenv

load_dotenv('.env')
app = FastAPI()

def _assert_dynasty_exists(dynasty: int):
    if dynasty is None:
        raise HTTPException(status_code=404, detail="Dynasty not found!")

#: Configure CORS
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URI'])

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.get('/dynasties/')
async def get_dynasties():
    dynasties = db.session.query(ModelDynasty).all()
    return dynasties

@app.get('/random/dynasty')
async def get_dynasties():
    random_dynasties_idx = random.randint(0, 8)
    dynasty = db.session.query(ModelDynasty).filter(ModelDynasty.id==random_dynasties_idx).one_or_none()
    return dynasty

@app.get('/events/')
async def get_events():
    events = db.session.query(ModelEvents).all()
    return events

@app.get('/events/{dynasty}')
async def get_dynasties(dynasty: str):
    dynasty = dynasty.lower()
    dynasty_id = db.session.query(ModelDynasty.id).filter(func.lower(ModelDynasty.name).like("%" + dynasty + "%")).one_or_none()
    _assert_dynasty_exists(dynasty_id)   
    dynasty_id = dynasty_id.id
    results = db.session.query(ModelEvents).filter(ModelEvents.dynasty_id == dynasty_id).all()
    return results

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
