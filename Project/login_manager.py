import flask_login
from .settings import project
from .loadenv import SECRET_KEY
from registration_app.models import User

project.secret_key = SECRET_KEY
login_maneger = flask_login.LoginManager(app = project)

@login_maneger.user_loader
def load_user(id):
    return User.query.get(id)
