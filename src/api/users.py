from fastapi import APIRouter

from api.dependencies import UOWDep
from schemas.users import UserSchemaAdd
from services.users import UsersService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user(
    user: UserSchemaAdd,
    uow: UOWDep,
):
    user_id = await UsersService().add_user(uow, user)
    return {"user_id": user_id}


@router.get("")
async def get_users(
    uow: UOWDep,
):
    users = await UsersService().get_users(uow)
    return users
