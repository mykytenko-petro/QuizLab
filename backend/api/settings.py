import flask

from .routes import (
    createQuizRouter
)

apiApp = flask.Blueprint(
    name="apiApp",
    import_name="api",
    url_prefix="/api"
)

apiApp.register_blueprint(createQuizRouter)