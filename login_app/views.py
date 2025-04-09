import flask
import flask_login
from registration_app.models import User

#Створення функції render_authorization
def render_login():
    if flask.request.method == "POST":
        for user in User.query._filter_by_zero(login = flask.request.form["login"]):# filter user by id
            if user.password == flask.request.form["password"]: # check user password
                flask_login.login_user(user) # True/False by login
                return flask.redirect("/")
    
    return flask.render_template("login.html")