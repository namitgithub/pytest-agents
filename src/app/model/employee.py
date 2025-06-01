from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Employee(Base):    
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}', salary={self.salary})>"
    def __str__(self):
        return f"Employee ID: {self.id}, Name: {self.name}, Salary: {self.salary}"