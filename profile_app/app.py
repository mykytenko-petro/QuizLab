import flask

profile_app = flask.Blueprint(

    name = "profile_app",
    import_name = "profile_app",
    static_url_path = "/profile_app/static/",
    static_folder = "static",
    template_folder = "templates"
)