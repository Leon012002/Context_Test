from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id    = Column(Integer, primary_key=True)
    name  = Column(String(100))
    email = Column(String(200), unique=True)
    team  = Column(String(50))              # z.B. "dev", "design", "pm"
    tasks = relationship("Task", back_populates="assignee")

class Task(Base):
    __tablename__ = "tasks"
    id          = Column(Integer, primary_key=True)
    title       = Column(String(200))
    description = Column(String(1000))
    status      = Column(String(20), default="open")    # open|in_progress|done|blocked
    priority    = Column(String(10), default="medium")  # low|medium|high|critical
    due_date    = Column(DateTime)
    created_at  = Column(DateTime, default=datetime.utcnow)
    assignee_id = Column(Integer, ForeignKey("users.id"))
    assignee    = relationship("User", back_populates="tasks")