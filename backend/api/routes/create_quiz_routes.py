import flask

from quiz.core.create_quiz import (
    quiz_handle,
    question_handle,
    answer_handle
)

createQuizRouter = flask.Blueprint(
    name="createQuizRouter",
    import_name=__file__,
    url_prefix="/create_quiz"
)

createQuizRouter.add_url_rule(
    rule='/quiz',
    view_func=quiz_handle,
    methods=['POST']
)

createQuizRouter.add_url_rule(
    rule='/question',
    view_func=question_handle,
    methods=['POST']
)

createQuizRouter.add_url_rule(
    rule='/answer',
    view_func=answer_handle,
    methods=['POST']
)