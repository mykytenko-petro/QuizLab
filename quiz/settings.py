import flask

from .create import createQuizApp
from .play import playQuizApp
from .sessions import sessionQuizApp


quizApp = flask.Blueprint(
    name="quizApp",
    import_name="quiz",
    url_prefix="/quiz"
)

quizApp.register_blueprint(blueprint=createQuizApp)
quizApp.register_blueprint(blueprint=playQuizApp)
quizApp.register_blueprint(blueprint=sessionQuizApp)