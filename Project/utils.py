import os
import flask
import flask_mail
import flask_login
import functools
from .smtp_setup import mail

def toggle(name_of_bp):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*agrs, **kwargs):
            if not os.getenv(name_of_bp) or os.getenv(name_of_bp) == "TRUE":
                return func(*agrs, **kwargs)
            else:
                return flask.render_template("page_not_found.html")

        return wrapper

    return inner

def login_required(func):
    @functools.wraps(func)
    def wrapper(*agrs, **kwargs):
        if flask_login.current_user.is_authenticated:
            return func(*agrs, **kwargs)
        else:
            return flask.redirect("/")
    
    return wrapper

def admin_required(func):
    @functools.wraps(func)
    def wrapper(*agrs, **kwargs):
        if flask_login.current_user.is_authenticated and flask_login.current_user.is_admin:
            return func(*agrs, **kwargs)
        else:
            return flask.redirect("/")
    
    return wrapper

def page_config(template_name : str):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*agrs, **kwargs):
            user = flask_login.current_user if flask_login.current_user.is_authenticated else None

            context = func(*agrs, **kwargs)
            print("context:", context)

            if context is None:
                return flask.render_template(
                    template_name_or_list= template_name,
                    user= user
                )

            if "alternative_template" in context:
                return flask.render_template(
                    template_name_or_list= context["alternative_template"],
                    username= user,
                    **context
                )
            
            elif "redirect" in context:
                return flask.redirect(context["redirect"])
            
            else:
                return flask.render_template(
                    template_name_or_list= template_name,
                    user= user,
                    **context
                )
        
        return wrapper
    
    return inner

def send_email(subject : str, recipients : list, *agrs, **kwargs):
    msg = flask_mail.Message(
        subject= subject,
        recipients= recipients,
        *agrs,
        **kwargs
    )

    mail.send(msg)