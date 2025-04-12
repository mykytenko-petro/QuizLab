import flask
import flask_login
from registration_app.models import User

def login(login):
    for user in User.query._filter_by_zero(login):
        if user.password == flask.request.form["password"]:
            flask_login.login_user(user)
            return flask.redirect("/")
