import flask


mediaManagerApp = flask.Blueprint(
    name="media",
    import_name="Project",
    static_folder="media",
    static_url_path="/media"
)