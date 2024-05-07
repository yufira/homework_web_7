from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(150), nullable=False)


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(100), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    student_name = Column(String(150), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))
    group = relationship('Group', backref='students')


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(300), nullable=False)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship('Teacher', backref='subjects')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_received = Column('date_received', Date, nullable=True)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    subject_id = Column('subject_id', ForeignKey('subjects.id', ondelete='CASCADE'))
    student = relationship('Student', backref='grades')
    subject = relationship('Subject', backref='grades')