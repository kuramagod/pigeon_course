from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase


database_url = "sqlite:///tasks.db"

engine = create_engine(database_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)

def get_session():
    with SessionLocal() as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


class Base(DeclarativeBase):
    pass