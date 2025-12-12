"""
    DmwSupaOrm
    Demonstration of Supabase ORM for Python
    Student Model

    @author: Alessio Saltarin

"""

from typing import List
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from supaorm.base import Entity
from supaorm.course import Course


class Student(Entity):
    __tablename__ = "student"
    id = mapped_column(primary_key=True)
    first_name = mapped_column(String(80))
    last_name = mapped_column(String(80))
    # Student <-> Course Many-to-Many relationship would be defined here
    courses: Mapped[List["Course"]] = relationship(
        back_populates = "student", cascade = "all, delete-orphan")

