import flask
import flask_login

from Project.utils import page_config
from ..models import User


@page_config(template_name="login.html")
def render_login():
    if flask.request.method == "POST":
        form = flask.request.form
        
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

def logout():
    flask.session.clear()
    return flask.redirect('/')