from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=2000)


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    is_complete: bool


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str
    is_complete: bool
    created_at: datetime


class TaskListResponse(BaseModel):
    tasks: list[TaskResponse]