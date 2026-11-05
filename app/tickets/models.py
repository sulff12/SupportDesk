from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(5000))
    status: Mapped[str ] = mapped_column(
        String(20),
        default="open",
        nullable=False,
    )