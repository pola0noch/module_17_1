from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean, Float
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates="user")
    is_active = Column(Boolean, default=True)

