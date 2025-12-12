from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from supaorm.entity import Entity
from supaorm.professor import Professor
from supaorm.course import Course
from supaorm.student import Student

print('Starting M2M test')
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Entity.metadata.create_all(engine)
print('Tables created')

session = Session()
prof = Professor(first_name='John', last_name='Doe', email='john@example.com')
session.add(prof)
session.commit()
print('Professor id:', prof.id)

course = Course(name='Test Course', professor_id=prof.id)
session.add(course)
session.commit()
print('Course id:', course.id)

student = Student(first_name='Alice', last_name='Smith', courses=[course])
session.add(student)
session.commit()
print('Student id:', student.id)

s = session.query(Student).filter_by(id=student.id).one()
print('Student courses:', [(c.id, c.name) for c in s.courses])

c = session.query(Course).filter_by(id=course.id).one()
print('Course students:', [(st.id, st.first_name) for st in c.students])
print('M2M test completed successfully')

