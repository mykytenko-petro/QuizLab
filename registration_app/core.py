import flask
import flask_login

def login():
    for user in User.query.filter_by(login = flask.request.form["name"]):
        if user.password == flask.request.form["password"]:
            flask_login.login_user(user)
            print("sucsessfully login user:", flask.request.form["name"])
            return flask.redirect("/")
        else:
            print("failed to login")
            return flask.redirect("/login")
