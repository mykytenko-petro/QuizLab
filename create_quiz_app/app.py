import flask

createQuizApp = flask.Blueprint(
    name = "create_quiz",
    import_name ="create_quiz_app",
    static_url_path = "/create_quiz/static",
    static_folder = "static",
    template_folder = "templates"
)