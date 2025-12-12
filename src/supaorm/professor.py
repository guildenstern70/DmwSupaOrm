"""
    DmwSupaOrm
    Demonstration of Supabase ORM for Python
    Professor Model

    @author: Alessio Saltarin

"""

from sqlalchemy import String
from supaorm.base import Entity
from sqlalchemy.orm import mapped_column


class Professor(Entity):
    __tablename__ = "professor"
    id = mapped_column(primary_key=True)
    first_name = mapped_column(String(80))
    last_name = mapped_column(String(80))
    email = mapped_column(String(120))
