import flask
import flask_login

def send_name():
    if flask.request.method == "POST":
        if flask_login.current_user.is_authenticated:
            return {"name": flask_login.current_user.login}
        else:
            return {"name": "guest"}