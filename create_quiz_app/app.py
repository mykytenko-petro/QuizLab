import flask

createQuizApp = flask.Blueprint(
    name = "createQuiz",
    import_name = "create_quiz_app",
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "/create_quiz/static",
)