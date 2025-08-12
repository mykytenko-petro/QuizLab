import os

import fastapi.staticfiles as staticfiles

from .root import project


MEDIA_PATH = os.path.abspath(os.path.join(__file__, '..', 'media'))

project.mount(
    path='/media',
    app=staticfiles.StaticFiles(directory=MEDIA_PATH)
)

