from sqlalchemy import create_engine, Column, Integer, String, BigInteger, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
engine = create_engine("mysql://usuario:senha@host/banco", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

# define model
class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

class User(Base):
    __tablename__ = 'usuario'
    ID_USER = Column(Integer, primary_key=True)
    MAT_USER = Column(Integer)
    NM_USER = Column(String(50))
    PASS_USER = Column(String)
    SN_ATIVO =  Column(Boolean)
    DT_CREATE = Column(DateTime)
    DT_UPDATE = Column(DateTime)


# crate table
# Base.metadata.create_all(engine)

# insert student
# student1 = Student(name="Wanderson", age = 31, grade = "Fifth")
# student2 = Student(name="Adolfo", age = 31, grade = "Fifth")
# student3 = Student(name="Diego", age = 31, grade = "Fifth")
# for one data
# session.add(student1)
# for multiple data
# session.add_all([student2, student3])
# session.commit()

# get datas (select)
# get all data
# students = session.query(Student)
# for student in students:
#     print(student.name, student.age, student.grade)
# get data in order
# students = session.query(Student).order_by(Student.name)
# for student in students:
#     print(student.name)
# get data by filtering
# student = session.query(Student).filter(Student.name=="Wanderson").first()
# print(student.name, student.age)
# count the number of results
# students_count = session.query(Student).count()
# print(students_count)

users = session.query(User)
for user in users:
    print(user.NM_USER)