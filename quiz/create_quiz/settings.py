from os.path import abspath, join, dirname

import flask


createQuizApp = flask.Blueprint(
    name="createQuizApp",
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/createQuizApp/static"
)

print(createQuizApp.import_name)