from datetime import datetime

from sqlalchemy import DateTime, String, func

from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(2000))
    is_complete: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())