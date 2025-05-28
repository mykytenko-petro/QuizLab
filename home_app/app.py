import flask

homeApp = flask.Blueprint(
    name = "home",
    import_name = "home_app",
    template_folder = "templates",
    static_url_path = "/home_app/static",
    static_folder = "static",
)