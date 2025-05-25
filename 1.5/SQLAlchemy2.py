from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Базовий клас для моделей
Base = declarative_base()

# Створення підключення до бази даних SQLite
engine = create_engine("sqlite:///students.db")
Session = sessionmaker(bind=engine)
session = Session()

# Оголошення моделі студента
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)  # Первинний ключ
    name = Column(String)  # Ім'я студента
    age = Column(Integer)  # Вік студента

# Створення таблиці в базі даних
Base.metadata.create_all(engine)

# Додавання нового студента
new_student = Student(name="Dmytro", age=46)
session.add(new_student)
session.commit()
print("Студент доданий")

# Отримання всіх записів з таблиці
students = session.query(Student).all()
print("Список студентів:")
for student in students:
    print(f"ID: {student.id}, Ім'я: {student.name}, Вік: {student.age}")