import flask

from .create_quiz import createQuizApp


quizApp = flask.Blueprint(
    name="quizApp",
    import_name="quiz",
    url_prefix="/quiz"
)

quizApp.register_blueprint(createQuizApp)