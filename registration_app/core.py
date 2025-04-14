import flask
import flask_login
from registration_app.models import User
from Project.settings import DATABASE

def login(): 
    for user in User.query.filter_by(login = flask.request.form["name"]):
        if user.password == flask.request.form["password"]:
            flask_login.login_user(user)
            return flask.redirect("/")