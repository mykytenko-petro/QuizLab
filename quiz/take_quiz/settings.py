import flask


takeQuizApp = flask.Blueprint(
    name="takeQuizApp",
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/takeQuizApp/static",
)