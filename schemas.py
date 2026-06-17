from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title:       str
    description: Optional[str] = None
    priority:    str = "medium"
    due_date:    Optional[datetime] = None
    assignee_id: Optional[int] = None

class TaskOut(BaseModel):
    id:       int
    title:    str
    status:   str
    priority: str
    due_date: Optional[datetime] = None

    class Config:
        from_attributes = True