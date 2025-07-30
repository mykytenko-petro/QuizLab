import flask

createQuizApp = flask.Blueprint(
    name="createQuiz",
    import_name="quiz",
    template_folder="templates/create_quiz",
    static_folder="static/create_quiz",
    static_url_path="/create_quiz/static",
)