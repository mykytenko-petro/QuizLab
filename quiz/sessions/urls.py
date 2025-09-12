import flask

from .settings import sessionQuizApp
from .core import (
    create_quiz_session
)


API = flask.Blueprint(
    name="sessionQuizAPI",
    import_name=__file__,
    url_prefix="/api"
)

API.add_url_rule(
    rule="/create_single_play_session",
    view_func=create_quiz_session,
    methods=["GET"]
)


sessionQuizApp.register_blueprint(API)