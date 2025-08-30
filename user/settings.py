import flask


userApp = flask.Blueprint(
    name="userApp",
    import_name="user",
    template_folder="templates",
    static_folder="static",
    static_url_path="/userApp/static",
)