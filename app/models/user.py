from pymysql.constants.FLAG import AUTO_INCREMENT
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'user'
    Id = Column(AUTO_INCREMENT, primary_key=True)
    FName = Column(String)
    LName = Column(String)
    Email = Column(String)
    Password = Column(String)
