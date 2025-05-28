import flask_mail
import os
from .settings import project

project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 587
project.config['MAIL_USERNAME'] = os.getenv("EMAIL_USERNAME")
project.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASSWORD")
project.config['MAIL_DEFAULT_SENDER'] = os.getenv("EMAIL_USERNAME")
project.config['MAIL_USE_SSL'] = False
project.config['MAIL_USE_TLS'] = True

mail = flask_mail.Mail(app = project)