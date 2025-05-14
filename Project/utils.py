import os
import flask
import flask_mail
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

def send_email(subject, recipients, html_body):
    msg = flask_mail.Message(
        subject= subject,
        recipients= recipients,
        html= html_body
    )

    mail.send(msg)