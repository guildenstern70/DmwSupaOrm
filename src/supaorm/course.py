"""
    DmwSupaOrm
    Demonstration of Supabase ORM for Python
    Course Model

    @author: Alessio Saltarin

"""

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from base import Entity

class Course(Entity):
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    professor_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    def __repr__(self) -> str:
        return f"Course(id={self.id!r}, name={self.name!r}, professor_id={self.professor_id!r})"
