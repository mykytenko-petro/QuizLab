import flask

loginApp = flask.Blueprint(
    name = "login",
    import_name = "login_app",
    template_folder = "login_page/templates",
    static_url_path = "/login/",
    static_folder = "login_page/static",
)