import flask

homeApp = flask.Blueprint(
    name="home",
    import_name="home",
    template_folder="templates",
    static_folder="static",
    static_url_path="/home_app/static",
)

dashboardApp = flask.Blueprint(
    name="dashboard",
    import_name="home",
    template_folder="templates",
    static_folder="static",
    static_url_path="/home_app/static",
)