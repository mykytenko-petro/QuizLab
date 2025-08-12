import os

import uvicorn

from .root import project


uvicorn_server = uvicorn.Server(
    config=uvicorn.Config(
        app=project,
        host="0.0.0.0" if os.environ["IS_PRODACTION"] == "TRUE" else "127.0.0.1",
        port=int(os.environ["PORT"])
    )
)