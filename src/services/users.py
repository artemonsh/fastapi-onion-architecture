from schemas.users import UserSchemaAdd
from utils.unitofwork import IUnitOfWork


class UsersService:
    async def add_user(self, uow: IUnitOfWork, user: UserSchemaAdd):
        async with uow:
            user_dict = user.model_dump()
            user_id = await uow.users.add_one(user_dict)
            return user_id

    async def get_users(self, uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users
