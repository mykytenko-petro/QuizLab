import flask_login
from Project.core import toggle

@toggle(name_of_bp="apiApp")
def send_name():
    if flask_login.current_user.is_authenticated:
        return {"name": flask_login.current_user.login}
    else:
        return {"name": "guest"}