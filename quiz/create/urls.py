import flask

from .settings import createQuizApp
from .views import (
    render_create_quiz,
    render_create_question
)
from .core import (
    answer_handle,
    question_handle,
    quiz_handle
)


# views
createQuizApp.add_url_rule(
    rule='/edit/<id>',
    view_func=render_create_quiz,
    methods=['GET', 'POST']
)

createQuizApp.add_url_rule(
    rule='/question/<id>',
    view_func=render_create_question,
    methods=['GET', 'POST']
)

# api
API = flask.Blueprint(
    name="createQuizAPI",
    import_name=__file__,
    url_prefix="/api"
)

API.add_url_rule(
    rule='/quiz',
    view_func=quiz_handle,
    methods=['POST']
)

API.add_url_rule(
    rule='/question',
    view_func=question_handle,
    methods=['POST']
)

API.add_url_rule(
    rule='/answer',
    view_func=answer_handle,
    methods=['POST']
)

createQuizApp.register_blueprint(API)