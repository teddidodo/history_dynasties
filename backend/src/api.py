from fastapi import FastAPI
from .dynasties import router as DynastyRouter
from .events import router as EventRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {
        "message": "Welcome to my notes application, use the /docs route to proceed"
    }

app.include_router(DynastyRouter, prefix="/dynasties")
app.include_router(EventRouter, prefix="/events")