import flask
import flask_login
from werkzeug import Response
from werkzeug.datastructures.structures import ImmutableMultiDict

from Project.utils import page_config
from ..models import User


@page_config(template_name="login.html")
def render_login() -> dict[str, str] | None:
    if flask.request.method == "POST":
        form: ImmutableMultiDict[str, str] = flask.request.form
        
        users_list: list[User] = User.query.all()
        for user in users_list:
            if user.email == form["email"] and user.password == form["password"]:
                flask_login.login_user(user)
                return {"redirect": "/"}
        else:
            if not User.query.filter_by(email=form["email"]).first():
                message = 'такої пошти не існує'
            else:
                message = 'неправильний код'
    
        return {"message": message}

def logout() -> Response:
    flask.session.clear()
    return flask.redirect(location='/')