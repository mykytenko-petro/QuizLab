import flask
import flask_login

def login():
    # Delay import until function call to avoid circular imports
    from registration_app.models import User
    
    for user in User.query.filter_by(login=flask.request.form["name"]):
        if user.password == flask.request.form["password"]:
            flask_login.login_user(user)
            return flask.redirect("/")
