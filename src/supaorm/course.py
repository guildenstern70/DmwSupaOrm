"""
    DmwSupaOrm
    Demonstration of Supabase ORM for Python
    Course Model

    @author: Alessio Saltarin

"""

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .entity import Entity
from .entity import student_course
from .student import Student

class Course(Entity):
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    professor_id: Mapped[int] = mapped_column(ForeignKey("professor.id"))
    # Many-to-Many: students <-> courses
    students: Mapped[list["Student"]] = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses",
        cascade="all, delete",
    )

    def __repr__(self) -> str:
        return f"Course(id={self.id!r}, name={self.name!r}, professor_id={self.professor_id!r})"
