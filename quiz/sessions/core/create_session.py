
from Project.db import DATABASE
from ..models import QuizSession


def create_quiz_session():
    quiz_session = QuizSession()

    DATABASE.session.add(quiz_session)
    DATABASE.session.commit()
    