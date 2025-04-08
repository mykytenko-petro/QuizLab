import flask

createQuizApp = flask.Blueprint(
    name = "create_quiz",
    import_name = "create_quiz_app",
    template_folder = "templates",
    static_url_path = "/create_quiz_static/",
    static_folder = "static"
)