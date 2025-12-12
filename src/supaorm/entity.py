"""
    DmwSupaOrm
    Demonstration of Supabase ORM for Python
    Base Entity Class

    @author: Alessio Saltarin

"""
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Table, Column, Integer, ForeignKey


class Entity(DeclarativeBase):
    pass

# Association table for Student <-> Course many-to-many
student_course = Table(
    "student_course",
    Entity.metadata,
    Column("student_id", Integer, ForeignKey("student.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("course.id"), primary_key=True),
)
