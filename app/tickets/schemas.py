from pydantic import BaseModel, Field


class TicketCreate(BaseModel):
    title: str = Field(min_length = 1 , max_length = 200)
    description: str = Field(min_length = 1, max_length = 5000)


class TicketRead(BaseModel):
    id: str
    title: str
    description: str
    status: str 
    