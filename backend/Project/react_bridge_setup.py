import os

import fastapi.staticfiles as staticfiles
import fastapi.responses as responses

from .root import project


INDEX_TEMPLATE_PATH = os.path.abspath(os.path.join("..", "frontend", "dist", "index.html"))
ASSETS_PATH = os.path.abspath(os.path.join("..", "frontend", "dist", "assets"))

project.mount(
    path='/assets',
    app=staticfiles.StaticFiles(directory=ASSETS_PATH)
)

async def react_page_serve(path : str):
    print(INDEX_TEMPLATE_PATH)
    return responses.FileResponse(INDEX_TEMPLATE_PATH)