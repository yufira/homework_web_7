from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

print("Selection 1:")
print(select_1(session))

print("Selection 2:")
print(select_2(session, "Virtual didactic matrix"))

print("Selection 3:")
print(select_3(session, "Secured systemic instruction set"))

print("Selection 4:")
print(select_4(session))

print("Selection 5:")
print(select_5(session, "Scott Murray"))

print("Selection 6:")
print(select_6(session, "Group 1"))

print("Selection 7:")
print(select_7(session, "Group 1", "Enterprise-wide clear-thinking ability"))

print("Selection 8:")
print(select_8(session, "Scott Murray"))

print("Selection 9:")
print(select_9(session, "Courtney Sheppard"))

print("Selection 10:")
print(select_10(session, "Traci Floyd", "Kathleen Adams"))