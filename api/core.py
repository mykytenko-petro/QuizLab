import flask
from Project.utils import toggle, login_required
from create_quiz_app.core import handle_quiz_data

@toggle(name_of_bp= "apiApp")
@login_required
def create_quiz_api():
    if flask.request.method == "POST":
        return handle_quiz_data()