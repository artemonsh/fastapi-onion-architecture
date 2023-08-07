from schemas.tasks import TaskHistorySchemaAdd, TaskSchemaAdd, TaskSchemaEdit
from utils.repository import AbstractRepository
from utils.unitofwork import IUnitOfWork


class TasksService:
    async def add_task(self, uow: IUnitOfWork, task: TaskSchemaAdd):
        tasks_dict = task.model_dump()
        async with uow:
            task_id = await uow.tasks.add_one(tasks_dict)
            await uow.commit()
            return task_id

    async def get_tasks(self, uow: IUnitOfWork):
        async with uow:
            tasks = await uow.tasks.find_all()
            return tasks

    async def edit_task(self, uow: IUnitOfWork, task_id: int, task: TaskSchemaEdit):
        tasks_dict = task.model_dump()
        async with uow:
            await uow.tasks.edit_one(task_id, tasks_dict)

            curr_task = await uow.tasks.find_one(id=task_id)
            task_history_log = TaskHistorySchemaAdd(
                task_id=task_id,
                previous_assignee_id=curr_task.assignee_id,
                new_assignee_id=task.assignee_id
            )
            task_history_log = task_history_log.model_dump()
            await uow.task_history.add_one(task_history_log)
            await uow.commit()

    async def get_task_history(self, uow: IUnitOfWork):
        async with uow:
            history = await uow.task_history.find_all()
            return history