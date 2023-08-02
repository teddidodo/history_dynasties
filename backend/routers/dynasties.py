from fastapi import APIRouter

router = APIRouter()

@router.get("/dynasties/")
def read_dynasties():
    return ["Hi", "How are you!"]

# @app.get('/dynasties/', status_code=200)
# async def get_dynasties(db: Session = Depends(create_get_session)):
#     dynasties = db.query(Dynasty).all()
#     return dynasties


# @app.get('/random/dynasty', status_code=200)
# async def get_dynasties(db: Session = Depends(create_get_session)):
#     random_dynasties_idx = random.randint(0, 8)
#     dynasty = db.query(Dynasty).filter(Dynasty.id==random_dynasties_idx).one_or_none()
#     return dynasty

# @app.get('/dynasties/{dynasty}', status_code=200)
# async def get_dynasty(dynasty: str, db: Session = Depends(create_get_session)):
#     dynasty = dynasty.lower()
#     dynasty = db.query(Dynasty).filter(func.lower(Dynasty.name).like("%" + dynasty + "%")).one_or_none()
#     _assert_dynasty_exists(dynasty)
#     return dynasty
