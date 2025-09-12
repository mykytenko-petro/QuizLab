import flask

from Project.db import DATABASE
from ..models import QuizSession


def create_quiz_session():
    params = flask.request.args

    quiz_session = QuizSession(
        quiz_id=params.get("quiz_id", type=int)
    )

    DATABASE.session.add(quiz_session)
    DATABASE.session.commit()

    return {"session_id": quiz_session.id}