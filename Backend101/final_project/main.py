from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Task(BaseModel):
    id: int
    description: str 
    completed: bool = False

tasks = [] 

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks/")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task added successfully", "task": task}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return {"message": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] == updated_task
            return {"message": "Task updated successfully", "task": updated_task}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            return {"message": "Task deleted successfully"}
        raise HTTPException(status_code=404, detail="Task not found")


