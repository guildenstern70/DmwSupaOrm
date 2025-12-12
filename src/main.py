"""
    DmwSupaOrm
    Demonstration of Supabase ORM for Python

    @author: Alessio Saltarin

"""
import os

import sqlalchemy
from sqlalchemy.pool import NullPool
from sqlalchemy import text
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from supaorm.entity import Entity

from supaorm.course import Course
from supaorm.professor import Professor
from supaorm.student import Student

# Load secrets from .env file
load_dotenv()
DB_URL = os.getenv('DB_URL')

def create_database_entities(sql_engine):
    print("-- Creating database entities...")
    # Create all tables (including association table student_course)
    Entity.metadata.create_all(sql_engine)
    print("-- Done.")

def delete_database_entities(sql_engine):
    print("-- Deleting database entities...")
    # Drop all tables (including association table student_course)
    Entity.metadata.drop_all(sql_engine)
    print("-- Done.")

def popultate_entities(sql_engine):
    print("-- Populating entities...")
    # Use an ORM Session for object persistence (Connection has no add_all)
    with Session(sql_engine) as session:
        with session.begin():
            # Add sample professors
            prof1 = Professor(first_name="John", last_name="Doe", email="johndoe@gmail.com")
            prof2 = Professor(first_name="Jane", last_name="Smith", email="janes@outlook.com")
            prof3 = Professor(first_name="Alice", last_name="Johnson", email="alice.johnson@uni.edu")
            prof4 = Professor(first_name="Robert", last_name="Brown", email="robert.brown@college.edu")
            prof5 = Professor(first_name="Maria", last_name="Garcia", email="m.garcia@institution.org")
            session.add_all([prof1, prof2, prof3, prof4, prof5])
            session.flush()  # Ensure IDs are generated
            # Add sample courses
            course1 = Course(name="Introduction to Programming", professor_id=prof1.id)
            course2 = Course(name="Data Structures", professor_id=prof2.id)
            course3 = Course(name="Database Systems", professor_id=prof3.id)
            course4 = Course(name="Operating Systems", professor_id=prof4.id)
            course5 = Course(name="Computer Networks", professor_id=prof5.id)
            session.add_all([course1, course2, course3, course4, course5])
            session.flush()
            # Add sample students
            student1_courses = [course1, course2]
            student2_courses = [course2, course3, course4]
            student3_courses = [course3, course4]
            student4_courses = [course4, course5]
            student5_courses = [course1, course5]
            student1 = Student(first_name="Emily", last_name="Davis", courses=student1_courses)
            student2 = Student(first_name="Michael", last_name="Wilson", courses=student2_courses)
            student3 = Student(first_name="Sarah", last_name="Miller", courses=student3_courses)
            student4 = Student(first_name="David", last_name="Taylor", courses=student4_courses)
            student5 = Student(first_name="Laura", last_name="Anderson", courses=student5_courses)
            session.add_all([student1, student2, student3, student4, student5])
    print("-- Done.")

if __name__ == '__main__':
    print("DmwSupaOrm v.0.0.1")
    version = sqlalchemy.__version__
    print("-- SQLAlchemy version:", version)

    engine = sqlalchemy.create_engine(DB_URL, client_encoding='utf8', poolclass=NullPool)
    print("-- Connecting to database...")
    with engine.connect() as conn:
        result = conn.execute(text("select * from student"))  # execute a simple query
        students = result.all()
    print("-- Connection closed.")

    if len(students) > 0:
        print(f"-- Database already populated with {len(students)} students.")
    else:
        delete_database_entities(engine)
        create_database_entities(engine)
        print("-- Database is empty. Populating...")
        popultate_entities(engine)
        print("-- All done.")



