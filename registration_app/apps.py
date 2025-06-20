import flask

registrationApp = flask.Blueprint(
    name = "registration",
    import_name = "registration_app",
    template_folder = "templates",
    static_url_path = "/registration/static",
    static_folder = "static",
)

loginApp = flask.Blueprint(
    name = 'login',
    import_name = 'registration_app',
    template_folder = 'templates',
    static_folder = 'static',
    static_url_path = '/login/static'
)