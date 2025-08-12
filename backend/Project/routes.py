import fastapi

from .root import project


router = fastapi.APIRouter()

from .react_bridge_setup import react_page_serve
router.add_api_route(
    path="/{path:path}",
    endpoint=react_page_serve
)

project.include_router(router)