from .settings import apiApp
from .core import (
    create_quiz_api
)

apiApp.add_url_rule(
    rule= '/create_quiz_api',
    view_func= create_quiz_api,
    methods = ['POST']
)