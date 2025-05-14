import flask_login
# import flask_email
import os
import secrets
from .settings import project
from registration_app.models import User

project.secret_key = secrets.token_hex(32)
login_manager = flask_login.LoginManager(app = project)

@login_manager.user_loader
def load_user(id):
    return User.query.get(ident= id)

project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 587
project.config['MAIL_USERNAME'] = os.getenv("EMAIL_USERNAME")
project.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASSWORD")
project.config['MAIL_DEFAULT_SENDER'] = os.getenv("EMAIL_USERNAME")
project.config['MAIL_USE_SSL'] = False
project.config['MAIL_USE_TLS'] = True

# mail = flask_email.Mail(app = project)