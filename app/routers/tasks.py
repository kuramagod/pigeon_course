from fastapi import APIRouter, HTTPException, Response
from app.database import SessionDep
from app.schemes import TaskCreate, TaskUpdate, TaskResponse, TaskListResponse
from app.repository.tasks import get_tasks, get_task, create_task, update_task, delete_task, update_compelete_task


router = APIRouter(tags=["tasks"])


@router.get("/tasks", response_model=TaskListResponse)
def tasks(session: SessionDep, is_complete: bool | None = None):
    tasks = get_tasks(session, is_complete)
    return TaskListResponse(tasks=tasks)


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def task(session: SessionDep, task_id: int):
    task = get_task(session, task_id)
    if task:
        return task
    
    raise HTTPException(status_code=404, detail=f"ID {task_id} not found")


@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create(session: SessionDep, task_data: TaskCreate):
    return create_task(session, task_data)


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update(session: SessionDep, task_id: int, task_data: TaskUpdate):
    updated_task = update_task(session, task_id, task_data)

    if updated_task:
        return updated_task
    
    raise HTTPException(status_code=404, detail=f"ID {task_id} not found")


@router.patch("/tasks/{task_id}/complete", response_model=TaskResponse)
def update_complete(session: SessionDep, task_id: int):
    updated_complete = update_compelete_task(session, task_id)

    if updated_complete:
        return updated_complete
    
    raise HTTPException(status_code=404, detail=f"ID {task_id} not found")


@router.delete("/tasks/{task_id}")
def delete(session: SessionDep, task_id: int):
    if delete_task(session, task_id):
        return Response(status_code=204)

    raise HTTPException(status_code=404, detail=f"ID {task_id} not found")
