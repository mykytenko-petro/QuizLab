import os
import flask
import flask_mail
import flask_login
from .smtp_setup import mail

def toggle(name_of_bp):
    def inner(func):
        def wrapper(*agrs, **kwargs):
            if os.getenv(name_of_bp) == "TRUE":
                return func(*agrs, **kwargs)
            else:
                return flask.render_template("page_not_found.html")

        return wrapper

    return inner

def login_checker(func):
    def wrapper(*agrs, **kwargs):
        if flask_login.current_user.is_authenticated:
            return func(*agrs, **kwargs)
        else:
            return flask.redirect("/")
    
    return wrapper

def send_email(subject, recipients, html_body):
    msg = flask_mail.Message(
        subject= subject,
        recipients= recipients,
        html= html_body
    )

    mail.send(msg)