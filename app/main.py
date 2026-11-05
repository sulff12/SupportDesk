from fastapi import FastAPI
from app.tickets.router import router
from app.database import Base, engine
from app.tickets.models import Ticket


app = FastAPI()
app.include_router(router)  

@app.get("/")
def root():
    return {"message": "SupportDesk is work"}