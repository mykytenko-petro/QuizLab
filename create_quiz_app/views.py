import flask
from Project.utils import toggle, login_required, page_config
from .core import AssembleQuiz

@toggle(name_of_bp= "createQuizApp")
@login_required
@page_config(template_name= "create_quiz.html")
def render_create_quiz():
    AssembleQuiz.handle_data(data= {"goal": "create", "quiz": {}})

@toggle(name_of_bp= "createQuizApp")
@login_required
def create_quiz_api():
    return AssembleQuiz.handle_data(flask.request.json)