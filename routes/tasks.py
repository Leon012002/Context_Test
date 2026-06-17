from fastapi import APIRouter
from schemas import TaskCreate, TaskOut
from typing import List

router = APIRouter()

@router.get("/")
def get_tasks():
    # TODO: DB-Abfrage über repos/
    return []

@router.post("/")
def create_task(task: TaskCreate):
    return {"message": "created", "task": task}

@router.patch("/{task_id}/status")
def update_status(task_id: int, status: str):
    return {"task_id": task_id, "status": status}