import fastapi

from .register import register


user_router = fastapi.APIRouter(prefix="/user")

user_router.add_api_route(
    path="/register",
    endpoint=register,
    methods=["POST"]
)