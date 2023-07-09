from schemas.users import UserSchemaAdd
from utils.repository import AbstractRepository


class UsersService:
    def __init__(self, users_repo: AbstractRepository):
        self.users_repo: AbstractRepository = users_repo()

    async def add_user(self, user: UserSchemaAdd):
        user_dict = user.model_dump()
        user_id = await self.users_repo.add_one(user_dict)
        return user_id

    async def get_users(self):
        users = await self.users_repo.find_all()
        return users
