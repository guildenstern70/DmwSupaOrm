"""
    DmwSupaOrm
    Demonstration of Supabase ORM for Python
    Professor Model

    @author: Alessio Saltarin

"""

from sqlalchemy import String
from .entity import Entity
from sqlalchemy.orm import mapped_column, Mapped


class Professor(Entity):
    __tablename__ = "professor"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(80))
    last_name: Mapped[str] = mapped_column(String(80))
    email: Mapped[str] = mapped_column(String(120))
