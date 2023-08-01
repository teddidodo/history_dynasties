from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Text
from database import Base
from sqlalchemy.orm import relationship

class Dynasty(Base):
    __tablename__ = "dynasty"
    id  = Column(Integer(), primary_key=True)
    name = Column(Text())
    house = Column(Text())
    start_year = Column(Text())
    end_year = Column(Text())
    current_country = Column(Text())

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer(), primary_key=True)
    year = Column(Text())
    description = Column(Text())
    period = Column(Text())
    dynasty_id = Column(Integer(), ForeignKey('dynasty.id'))
    dynasty = relationship('Dynasty')