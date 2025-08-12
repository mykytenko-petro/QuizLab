import os
import functools
from typing import Callable

from .root import project


# def toggle(name_of_feature : str):
#     def inner(func : Callable):
#         @functools.wraps(func)
#         def wrapper(*agrs, **kwargs):
#             if not os.getenv(name_of_feature) or os.getenv(name_of_feature) == "TRUE":
#                 return func(*agrs, **kwargs)
#             else:
#                 return flask.render_template("page_not_found.html")

#         return wrapper

#     return inner

# def login_required(func : Callable):
#     @functools.wraps(func)
#     def wrapper(*agrs, **kwargs):
#         if flask_login.current_user.is_authenticated:
#             return func(*agrs, **kwargs)
#         else:
#             return flask.redirect("/")
    
#     return wrapper

# def admin_required(func : Callable):
#     @functools.wraps(func)
#     def wrapper(*agrs, **kwargs):
#         if flask_login.current_user.is_authenticated and flask_login.current_user.is_admin:
#             return func(*agrs, **kwargs)
#         else:
#             return flask.redirect("/")
    
#     return wrapper

# def react_page_serve(func : Callable):
#     @functools.wraps(func)
#     def wrapper(*agrs, **kwargs):
#         func(*agrs, **kwargs)

#         return flask.send_from_directory(
#             directory=project.template_folder,
#             path="index.html"
#         )
    
#     return wrapper

# def react_html_inject(template_name : str):
#     def inner(func : Callable[..., dict]):
#         @functools.wraps(func)
#         def wrapper(*agrs, **kwargs):
#             params = flask.request.args

#             if params.get("render") == "true":

#                 user = flask_login.current_user if flask_login.current_user.is_authenticated else None

#                 context: dict = func(*agrs, **kwargs) or {}

#                 if "redirect" in context:
#                     return {"redirect": context["redirect"]}

#                 if "alternative_template" in context:
#                     render_template_name = context["alternative_template"]
#                 else:
#                     render_template_name = template_name

#                 rendered_template = flask.render_template(
#                     template_name_or_list=render_template_name,
#                     user=user,
#                     **context
#                 )

#                 return rendered_template
#             else:
#                 return flask.make_response('', 204)
        
#         return wrapper
    
#     return inner

def get_media_path() -> str:
    path = os.path.abspath(os.path.join(__file__, "..", "media"))
    return path