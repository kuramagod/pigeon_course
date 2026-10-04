from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Tasks
from app.schemes import TaskCreate, TaskUpdate


def get_tasks(session: Session, is_complete: bool | None = None) -> list[Tasks]:
    smtp = select(Tasks)

    if not is_complete is None:
        smtp = smtp.where(Tasks.is_complete == is_complete)
    
    return session.execute(smtp).scalars().all()


def get_task(session: Session, task_id: int) -> Tasks | None:
    return session.get(Tasks, task_id)


def create_task(session: Session, task_data: TaskCreate) -> Tasks:
    task = Tasks(
        title=task_data.title, 
        description=task_data.description
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def update_task(session: Session, task_id: int, task_data: TaskUpdate) -> Tasks | None:
    task = session.get(Tasks, task_id)
    if task is None:
        return None
    
    task.title = task_data.title
    task.description = task_data.description
    task.is_complete = task_data.is_complete
    
    session.commit()
    session.refresh(task)
    
    return task


def update_compelete_task(session: Session, task_id: int) -> Tasks | None:
    task = session.get(Tasks, task_id)
    if task is None:
        return None
    
    if task.is_complete:
        task.is_complete = False
    else:
        task.is_complete = True
    
    session.commit()
    session.refresh(task)
    
    return task


def delete_task(session: Session, task_id: int) -> bool:
    task = session.get(Tasks, task_id)
    if task is None:
        return False
    
    session.delete(task)
    session.commit()
    
    return True