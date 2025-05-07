import flask
from Project.core import toggle

@toggle(name_of_bp="apiApp")
def render_home():
    return flask.render_template(
        template_name_or_list= "home.html"
    )