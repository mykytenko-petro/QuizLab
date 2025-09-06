import flask


playQuizApp = flask.Blueprint(
    name="playQuizApp",
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/playQuizApp/static",
)