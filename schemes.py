from pydantic import BaseModel
from datetime import datetime


class TaskRequest(BaseModel):
    title: str
    description: str
    is_complete: bool = False


class TaskResponse(TaskRequest):
    id: int
    created_at: datetime
