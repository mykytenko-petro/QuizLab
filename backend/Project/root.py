import os

import fastapi


project = fastapi.FastAPI()

SECRET = os.environ["SECRET"]