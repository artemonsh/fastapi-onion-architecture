from models.tasks import TaskHistory
from utils.repository import SQLAlchemyRepository


class TaskHistoryRepository(SQLAlchemyRepository):
    model = TaskHistory
