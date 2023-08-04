from fastapi import APIRouter

from api.dependencies import UOWDep
from schemas.tasks import TaskSchemaAdd, TaskSchemaEdit
from services.tasks import TasksService

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("")
async def add_task(
    task: TaskSchemaAdd,
    uow: UOWDep,
):
    task_id = await TasksService().add_task(uow, task)
    return {"task_id": task_id}


@router.patch("/{id}")
async def edit_task(
    id: int,
    task: TaskSchemaEdit,
    uow: UOWDep,
):
    task_id = await TasksService().edit_task(uow, id, task)
    return {"task_id": task_id}


@router.get("")
async def get_tasks(
    uow: UOWDep,
):
    tasks = await TasksService().get_tasks(uow)
    return tasks

@router.get("/history")
async def get_task_history(
    uow: UOWDep,
):
    tasks = await TasksService().get_tasks_history(uow)
    return tasks
