import flask_login
import secrets
from .settings import project
from registration_app.models import User
import os
from flask_mail import Mail

project.secret_key = secrets.token_hex(32)
login_manager = flask_login.LoginManager(app = project)

@login_manager.user_loader
def load_user(id):
    return User.query.get(ident= id)

mail = Mail(project)

project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 587
project.config['MAIL_USERNAME'] = os.getenv("EMAIL_USERNAME")
project.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASSWORD")

# ADMINS = ['your-email@example.com']

#toaddrs=project.config['ADMINS'], subject='Microblog Failure'

#msg = Message('test subject', sender=project.config['ADMINS'][0],
# recipients=['your-email@example.com']
#msg.body = 'text body'
#msg.html = '<h1>HTML body</h1>'
#mail.send(msg)