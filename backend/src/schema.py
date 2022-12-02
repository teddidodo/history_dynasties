# build a schema using pydantic
from pydantic import BaseModel

class Dynasty(BaseModel):
    name: str
    house: str
    start_year: str
    end_year: str
    current_country: str

class Events(BaseModel):
    year: str
    description: str
    period: str
    dynasty_id:  int