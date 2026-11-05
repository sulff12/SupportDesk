from fastapi import APIRouter
from .schemas import TicketCreate

router = APIRouter(prefix="/tickets" , tags=["Tickets"])

@router.post("/")
def add_tickets(ticket: TicketCreate):
    return ticket


@router.get("/")
def ticketget():
    pass