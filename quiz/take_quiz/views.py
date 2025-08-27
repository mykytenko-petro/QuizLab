from Project.utils import page_config
from ..models import Quiz
from user.models import User


@page_config("quiz.html")
def render_quiz(id):
    quiz = Quiz.query.filter_by(id=id).first()
    creator_name = User.query.filter_by(id=quiz.owner_id).first()
    return {"quiz": quiz, "creator_name": creator_name.login}

