from typing import Annotated

from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine


class Recipe(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    count_viewing: int = Field(default=0)
    cooking_time: int
    ingredients: str
    description: str


sqlite_file_name = "example.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
