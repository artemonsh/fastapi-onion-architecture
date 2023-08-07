from typing import Optional

from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: int
    title: str
    author_id: int
    assignee_id: int

    class Config:
        from_attributes = True


class TaskSchemaAdd(BaseModel):
    title: str
    author_id: int
    assignee_id: int


class TaskSchemaEdit(BaseModel):
    author_id: int
    assignee_id: int


class TaskHistorySchema(BaseModel):
    id: int
    task_id: int
    previous_assignee_id: int
    new_assignee_id: int


class TaskHistorySchemaAdd(BaseModel):
    task_id: int
    previous_assignee_id: int
    new_assignee_id: int
