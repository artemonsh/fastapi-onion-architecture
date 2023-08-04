from abc import ABC, abstractmethod
from typing import Type
from db.db import async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.task_history import TaskHistoryRepository

from repositories.tasks import TasksRepository
from repositories.users import UsersRepository


class IUnitOfWork(ABC):
    tasks: Type[TasksRepository]
    task_history: Type[TaskHistoryRepository]
    users: Type[UsersRepository]

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork(IUnitOfWork):

    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session: AsyncSession = self.session_factory()
        
        self.tasks = TasksRepository(self.session)
        self.users = UsersRepository(self.session)
        self.task_history = TaskHistoryRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
