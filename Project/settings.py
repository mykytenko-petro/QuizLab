import flask
import home_app

project = flask.Flask(
    import_name = "Project",
    static_url_path = "/static/",
    static_folder = "static",
    template_folder = "templates"
)

project.register_blueprint(blueprint = home_app.homeApp)