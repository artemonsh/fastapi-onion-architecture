from schemas.tasks import TaskSchemaAdd, TaskSchemaEdit
from utils.unitofwork import IUnitOfWork


class TasksService:
    async def add_task(self, uow: IUnitOfWork, task: TaskSchemaAdd):
        async with uow:
            tasks_dict = task.model_dump()
            task_id = await uow.tasks.add_one(tasks_dict)
            return task_id

    async def get_tasks(self, uow: IUnitOfWork):
        async with uow:
            tasks = await uow.tasks.find_all()
            return tasks

    async def get_tasks_history(self, uow: IUnitOfWork):
        async with uow:
            task_history = await uow.task_history.find_all()
            return task_history

    async def edit_task(self, uow: IUnitOfWork, task_id: int, task: TaskSchemaEdit):
        async with uow:
            tasks_dict = task.model_dump()
            old_task = await uow.tasks.find_one(id=task_id)
            task_id = await uow.tasks.edit_one(tasks_dict, id=task_id)
            added_task_change = await uow.task_history.add_one(dict(
                task_id=task_id,
                previous_assignee_id=old_task.assignee_id,
                new_assignee_id=task.assignee_id,
            ))
            await uow.commit()
