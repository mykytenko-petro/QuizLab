import flask

from .settings import takeQuizApp
from .views import (
    render_quiz
)


# views
takeQuizApp.add_url_rule(
    rule="/view/<id>",
    view_func=render_quiz,
)

# api
API = flask.Blueprint(
    name="takeQuizAPI",
    import_name=__file__,
    url_prefix="/api"
)


takeQuizApp.register_blueprint(blueprint=API)
