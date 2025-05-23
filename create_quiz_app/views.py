import flask
from Project.utils import toggle, login_checker
from .core import AssembleQuiz

@toggle(name_of_bp= "createQuizApp")
@login_checker
def render_create_quiz():
    return flask.render_template(template_name_or_list= "create_quiz.html")

@toggle(name_of_bp= "createQuizApp")
@login_checker
def create_quiz():
    return AssembleQuiz.handle_data(flask.request.json)