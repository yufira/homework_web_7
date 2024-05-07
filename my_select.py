from sqlalchemy import func, desc, select
from models import Student, Grade, Subject, Teacher, Group


def select_1(session):
    return session.query(Student.student_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()


def select_2(session, subject_name):
    subquery = session.query(
        Student.id,
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ).join(Grade).join(Subject)\
    .filter(Subject.subject_name == subject_name)\
    .group_by(Student.id)\
    .subquery()

    query_result = session.query(
        Student.student_name,
        subquery.c.average_grade,
        Subject.subject_name
    ).join(subquery, Student.id == subquery.c.id)\
    .join(Grade).join(Subject)\
    .order_by(subquery.c.average_grade.desc())\
    .first()

    return query_result


def select_3(session, subject_name):
    subject_id_subquery = session.query(Subject.id).filter(Subject.subject_name == subject_name).scalar_subquery()

    query = session.query(
        Group.group_name,
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ).select_from(Group).join(Student).join(Grade).filter(Grade.subject_id == subject_id_subquery).group_by(Group.group_name).all()

    return query

def select_4(session):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).scalar()


def select_5(session, teacher_name):
    return session.query(Subject.subject_name).join(Teacher).filter(Teacher.teacher_name == teacher_name).all()


def select_6(session, group_name):
    return session.query(Student.student_name).join(Group).filter(Group.group_name == group_name).all()


def select_7(session, group_name, subject_name):
    return session.query(Student.student_name, Grade.grade).join(Group).join(Grade).join(Subject)\
        .filter(Group.group_name == group_name, Subject.subject_name == subject_name).all()


def select_8(session, teacher_name):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Subject).join(Teacher).filter(Teacher.teacher_name == teacher_name).scalar()


def select_9(session, student_name):
    return session.query(Subject.subject_name).join(Grade).join(Student)\
        .filter(Student.student_name == student_name).distinct().all()


def select_10(session, student_name, teacher_name):
    return session.query(Subject.subject_name).join(Teacher).join(Grade).join(Student)\
        .filter(Student.student_name == student_name, Teacher.teacher_name == teacher_name).distinct().all()
