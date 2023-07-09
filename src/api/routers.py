from api.tasks import router as router_tasks
from api.users import router as router_users

all_routers = [
    router_tasks,
    router_users,
]
