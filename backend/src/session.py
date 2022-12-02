from .model import Dynasty
from .database import SessionLocal, engine

Dynasty.metadata.create_all(bind=engine)
def create_get_session():
   try:
       db = SessionLocal()
       yield db
   finally:
       db.close()