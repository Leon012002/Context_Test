from fastapi import FastAPI
from routes import tasks, users

app = FastAPI(title="TaskFlow API")
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(users.router, prefix="/users", tags=["users"])