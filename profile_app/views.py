import flask
import flask_session
import flask_login
def render_profile():
    
    username = flask_login.current_user
    return flask.render_template(template_name_or_list = "profile_app.html")