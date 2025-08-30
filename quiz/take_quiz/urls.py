import flask

from .settings import takeQuizApp
from .views import (
    render_start_quiz,
    render_take_quiz
)



# views
takeQuizApp.add_url_rule(
    rule="/view/<id>",
    view_func=render_start_quiz
)

takeQuizApp.add_url_rule(
    rule="/play/<id>",
    view_func=render_take_quiz,
    methods = ["GET", "POST"]
)

# api
API = flask.Blueprint(
    name="takeQuizAPI",
    import_name=__file__,
    url_prefix="/api/take"
)

API.add_url_rule(
    rule="/get_quiz_data",
    view_func=render_take_quiz,
    methods = ["GET", "POST"]
)

takeQuizApp.register_blueprint(blueprint=API)