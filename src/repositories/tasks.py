from models.tasks import Tasks
from utils.repository import SQLAlchemyRepository


class TasksRepository(SQLAlchemyRepository):
    model = Tasks
