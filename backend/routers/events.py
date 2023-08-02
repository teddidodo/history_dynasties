from fastapi import APIRouter

router = APIRouter()

@router.get("/events/dynasty_id")
def read_dynasty_events():
    return []

# @app.get('/events/{dynasty}', status_code=200)
# async def get_dynasties(dynasty: str, db: Session = Depends(create_get_session)):
#     dynasty = dynasty.lower()
#     dynasty_id = db.query(Dynasty.id).filter(func.lower(Dynasty.name).like("%" + dynasty + "%")).one_or_none()
#     _assert_dynasty_exists(dynasty_id)   
#     dynasty_id = dynasty_id.id
#     events = db.query(Event).filter(Event.dynasty_id == dynasty_id).all()
#     # Split the timeline into the period
#     period_dict = {}
#     for event in events:
#         if event.period in period_dict:
#             period_dict[event.period].append(event)
#         else:
#             period_dict[event.period] = []
#             period_dict[event.period].append(event)
#     return period_dict
