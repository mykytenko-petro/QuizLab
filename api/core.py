import flask
from Project.utils import toggle, login_required
from create_quiz_app.core import AssembleQuiz

@toggle(name_of_bp= "apiApp")
@login_required
def create_quiz_api():
    if flask.request.method == "POST":
        return AssembleQuiz.handle_data(flask.request.json)

    return AssembleQuiz.handle_data(data= {"goal": "create", "quiz": {}})