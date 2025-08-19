import fastapi

from user.routes import user_router
from .root import project
from .react_bridge_setup import react_page_serve


router = fastapi.APIRouter()

router.include_router(user_router)


router.add_api_route(
    path="/{path:path}",
    endpoint=react_page_serve
)


project.include_router(router)