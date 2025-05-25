from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///students.db")
Session = sessionmaker(bind=engine)
session = Session()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

new_student = Student(name="Олександр", age=21)
session.add(new_student)
session.commit()
print("Студент доданий")
