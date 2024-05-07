from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade
from random import randint, sample


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


fake = Faker()

num_students = randint(30, 50)
num_groups = 3
num_subjects = randint(5, 8)
num_teachers = randint(3, 5)
max_grades_per_student = 20

groups = [Group(group_name=f"Group {i+1}") for i in range(num_groups)]
session.add_all(groups)
session.commit()

teachers = [Teacher(teacher_name=fake.name()) for _ in range(num_teachers)]
session.add_all(teachers)
session.commit()

subjects = []
for _ in range(num_subjects):
    teacher = sample(teachers, 1)[0]
    subject = Subject(subject_name=fake.catch_phrase(), teacher=teacher)
    subjects.append(subject)
session.add_all(subjects)
session.commit()

students = []
for _ in range(num_students):
    student_name = fake.name()
    group = sample(groups, 1)[0]
    student = Student(student_name=student_name, group=group)
    students.append(student)
session.add_all(students)
session.commit()

for student in students:
    for subject in subjects:
        num_grades = randint(1, max_grades_per_student)
        for _ in range(num_grades):
            grade = randint(1, 10)
            date_received = fake.date_between(start_date='-1y', end_date='today')
            session.add(Grade(student=student, subject=subject, grade=grade, date_received=date_received))
session.commit()
