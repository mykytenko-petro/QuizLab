import flask

registrationApp = flask.Blueprint(
    name="registration",
    import_name="user",
    template_folder="templates",
    static_folder="static",
    static_url_path="/registration/static",
)

loginApp = flask.Blueprint(
    name='login',
    import_name='user',
    template_folder='templates',
    static_folder='static',
    static_url_path='/login/static'
)