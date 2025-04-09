import flask

registrationApp = flask.Blueprint(
    name = "registration",
    import_name = "registration_app",
    template_folder = "templates",
    static_url_path = "/registration/static",
    static_folder = "static",
)