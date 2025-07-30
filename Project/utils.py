import os
import functools
from typing import Callable

import flask
import flask_login


def toggle(name_of_feature : str):
    def inner(func : Callable):
        @functools.wraps(func)
        def wrapper(*agrs, **kwargs):
            if not os.getenv(name_of_feature) or os.getenv(name_of_feature) == "TRUE":
                return func(*agrs, **kwargs)
            else:
                return flask.render_template("page_not_found.html")

        return wrapper

    return inner

def login_required(func : Callable):
    @functools.wraps(func)
    def wrapper(*agrs, **kwargs):
        if flask_login.current_user.is_authenticated:
            return func(*agrs, **kwargs)
        else:
            return flask.redirect("/")
    
    return wrapper

def admin_required(func : Callable):
    @functools.wraps(func)
    def wrapper(*agrs, **kwargs):
        if flask_login.current_user.is_authenticated and flask_login.current_user.is_admin:
            return func(*agrs, **kwargs)
        else:
            return flask.redirect("/")
    
    return wrapper

def page_config(template_name : str):
    def inner(func : Callable):
        @functools.wraps(func)
        def wrapper(*agrs, **kwargs):
            user = flask_login.current_user if flask_login.current_user.is_authenticated else None

            context: dict = func(*agrs, **kwargs) or {}

            if "redirect" in context:
                return flask.redirect(context["redirect"])

            if "alternative_template" in context:
                render_template_name = context["alternative_template"]
            else:
                render_template_name = template_name

            rendered_template = flask.render_template(
                template_name_or_list=render_template_name,
                user=user,
                **context
            )
            
            response = flask.make_response(rendered_template)

            if "cookies" in context:
                for key, value in context["cookies"].values():
                    response.set_cookie(key, value)

            return response
        
        return wrapper
    
    return inner

def get_media_path() -> str:
    path = os.path.abspath(os.path.join(__file__, "..", "media"))
    return path