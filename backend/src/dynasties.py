from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from .model import Dynasty
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .schema import Dynasty 

from .session import create_get_session
router = APIRouter()

@router.get("/", status_code=200)
async def read_tasks(db: Session = Depends(create_get_session)):
   tasks = db.query(Dynasty).all()
   return tasks

# @router.get("/{id}")
# async def get_note(id: str) -> dict:
#     if int(id) > len(notes):
#         return {
#             "error": "Invalid note ID"
#         }

#     for note in notes.keys():
#         if note == id:
#             return {
#                 "data": notes[note]
#             }

#     return {
#         "Error": "Invalid ID"
#     }


