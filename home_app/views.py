import flask
from Project.utils import toggle

@toggle(name_of_bp="homeApp")
def render_home():
    return flask.render_template(
        template_name_or_list= "home.html"
    )