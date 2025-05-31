from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from datetime import datetime, timezone
from uuid import uuid4
from ..models import Task, TaskCreate, TaskUpdate, User
from ..security import get_current_user
from ..storage import fake_tasks_db

router = APIRouter()

@router.post("/tasks", response_model=Task)
def create_task(task: TaskCreate, current_user: User = Depends(get_current_user)):
    task_id = str(uuid4())
    now = datetime.now(timezone.utc)
    new_task = Task(
        id=task_id,
        title=task.title,
        description=task.description,
        status=task.status or "todo",
        createdAt=now,
        updatedAt=now
    )
    fake_tasks_db.setdefault(current_user.username, {})
    fake_tasks_db[current_user.username][task_id] = new_task
    return new_task

@router.get("/tasks", response_model=List[Task])
def list_tasks(status: Optional[str] = None, current_user: User = Depends(get_current_user)):
    user_tasks = fake_tasks_db.get(current_user.username, {})
    tasks = list(user_tasks.values())
    if status:
        tasks = [t for t in tasks if t.status == status]
    return tasks

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str, current_user: User = Depends(get_current_user)):
    user_tasks = fake_tasks_db.get(current_user.username, {})
    task = user_tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task_update: TaskUpdate, current_user: User = Depends(get_current_user)):
    user_tasks = fake_tasks_db.get(current_user.username, {})
    task = user_tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    task.updatedAt = datetime.now(timezone.utc)
    user_tasks[task_id] = task
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: str, current_user: User = Depends(get_current_user)):
    user_tasks = fake_tasks_db.get(current_user.username, {})
    if task_id not in user_tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del user_tasks[task_id]
    return {"detail": "Task deleted"}