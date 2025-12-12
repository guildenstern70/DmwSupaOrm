"""
    DmwSupaOrm
    Demonstration of Supabase ORM for Python
    Student Model

    @author: Alessio Saltarin

"""

from typing import List
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .entity import Entity
from .entity import student_course


class Student(Entity):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(80))
    last_name: Mapped[str] = mapped_column(String(80))
    # Student <-> Course Many-to-Many relationship
    courses: Mapped[List["Course"]] = relationship(
        "Course",
        secondary=student_course,
        back_populates="students",
        cascade="all, delete",
    )
