from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from .database import Base

class Person(Base):
    __tablename__ = "people"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, nullable=False)

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})" 