from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# simple in-memory store
_tasks = []
_next_id = 1

@router.post("/", response_model=Task)
async def create_task(task: Task):
    global _next_id
    task.id = _next_id
    _next_id += 1
    _tasks.append(task)
    return task

@router.get("/", response_model=List[Task])
async def list_tasks():
    return _tasks

@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int):
    for t in _tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Not found")

@router.delete("/{task_id}")
async def delete_task(task_id: int):
    global _tasks
    for t in _tasks:
        if t.id == task_id:
            _tasks = [x for x in _tasks if x.id != task_id]
            return {"message": "deleted"}
    raise HTTPException(status_code=404, detail="Not found")
