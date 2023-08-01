from pydantic import BaseModel
from typing import Optional

class DynastySchema(BaseModel):
    name: str
    house: str
    start_year: str
    end_year: str
    current_country: str

class EventSchema(BaseModel):
    year: str
    description: str
    period: str
    dynasty_id:  int