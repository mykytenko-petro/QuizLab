import flask_login
import secrets
from .settings import project
from registration_app.models import User
import os

project.secret_key = secrets.token_hex(32)
login_manager = flask_login.LoginManager(app = project)

@login_manager.user_loader
def load_user(id):
    return User.query.get(ident= id)
