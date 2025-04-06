import flask

homeApp = flask.Blueprint(
    name = "home",
    import_name = "app",
    template_folder = "home_app/templates",
    static_url_path = "/home/",
    static_folder = "home_app/static",
)