import flask

profileApp = flask.Blueprint(
    name = "profile",
    import_name = "profile_app",
    static_url_path = "/profile_app/static/",
    static_folder = "static",
    template_folder = "templates"
)