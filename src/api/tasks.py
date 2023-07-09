from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import tasks_service
from schemas.tasks import TaskSchemaAdd
from services.tasks import TasksService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("")
async def add_task(
    task: TaskSchemaAdd,
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
):
    task_id = await tasks_service.add_task(task)
    return {"task_id": task_id}


@router.get("")
async def get_tasks(
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
):
    tasks = await tasks_service.get_tasks()
    return tasks
