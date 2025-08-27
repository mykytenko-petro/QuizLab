import flask

from .create_quiz import createQuizApp
from .take_quiz import takeQuizApp


quizApp = flask.Blueprint(
    name="quizApp",
    import_name="quiz",
    url_prefix="/quiz"
)

quizApp.register_blueprint(blueprint=createQuizApp)
quizApp.register_blueprint(blueprint=takeQuizApp)