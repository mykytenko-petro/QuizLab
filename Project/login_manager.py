import flask_login

from registration_app.models import User
from .settings import project

login_manager = flask_login.LoginManager(app = project)

@login_manager.user_loader
def load_user(id):
    return User.query.get(ident= id)