import typing
import fastapi
import flask_login
from .settings import app

@app.post('/get_name')
def send_name():
    is_authenticated = flask_login.current_user.is_authenticated

    if is_authenticated:
        return {"name": flask_login.current_user.login}
    else:
        return {"name": ""}