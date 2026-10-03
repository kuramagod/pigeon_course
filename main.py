from datetime import datetime

from fastapi import FastAPI, HTTPException, Response
from schemes import TaskRequest, TaskResponse

app = FastAPI()


TASKS = [
    TaskResponse(id=1, title="Тестовая задача", description="Описание задачи", is_complete=False, created_at=datetime.now()),
    TaskResponse(id=2, title="Тестовая задача 2", description="Описание задачи 2", is_complete=True, created_at=datetime.now())
]


@app.get("/tasks")
def get_tasks(is_complete: bool | None = None):
    tasks = TASKS
    
    if not is_complete is None:
        tasks = [x for x in tasks if x.is_complete == is_complete]
        
    return tasks


@app.get("/tasks/{id}", response_model=TaskResponse)
def get_tasks(id: int):
    tasks = TASKS
    
    for task in tasks:
        if task.id == id:
            return task

    raise HTTPException(status_code=404, detail=f"ID {id} not found")


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskRequest):
    task = TaskResponse(**task.model_dump(), id=len(TASKS) + 1, created_at=datetime.now())
    TASKS.append(task)
    return task


@app.put("/tasks/{id}", response_model=TaskResponse)
def update_tasks(id: int, task: TaskRequest):
    for index, existing_task in enumerate(TASKS):
        if existing_task.id == id:
            updated_task = existing_task.model_copy(update=task.model_dump())
            TASKS[index] = updated_task
            return updated_task
    
    raise HTTPException(status_code=404, detail=f"ID {id} not found")


@app.delete("/tasks/{id}")
def delete_task(id: int):
    for index, task in enumerate(TASKS):
        if task.id == id:
            del TASKS[index]
            return Response(status_code=204)

    raise HTTPException(status_code=404, detail=f"ID {id} not found")
