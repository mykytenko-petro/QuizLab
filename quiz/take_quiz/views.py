from Project.utils import page_config
from ..create_quiz.models import Quiz
from user.models import User


@page_config("start_quiz.html")
def render_start_quiz(id):
    quiz = Quiz.query.filter_by(id=id).first()
    creator_name = User.query.filter_by(id=quiz.owner_id).first()

    return {"quiz": quiz, "creator_name": creator_name.login}

@page_config("take_quiz.html")
def render_take_quiz(id):
    return None