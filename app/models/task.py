from sqlalchemy import Column, Integer, String, Boolean ,ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    due_date = Column(String)
    completed = Column(Boolean)
