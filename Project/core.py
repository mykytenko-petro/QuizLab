import os
import flask

def toggle(name_of_bp):
    def inner(func):
        def wrapper():
            if os.getenv(name_of_bp) == "TRUE":
                return func()
            else:
                return flask.render_template("page_not_found.html")

        return wrapper
    
    return inner