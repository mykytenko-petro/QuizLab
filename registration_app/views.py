import flask
from Project.settings import DATABASE
from .models import User

def render_registration():
    if flask.request.method == 'POST':
        if flask.request.form["password"] == flask.request.form["password_confirm"]:
            user = User(
                login = flask.request.form['name'], 
                password = flask.request.form["password"], 
                email = flask.request.form["email"], 
                is_admin = False
            )
        
            try:
                DATABASE.session.add(user)
                DATABASE.session.commit()
                return flask.redirect("/registration2")
                
            except Exception as error:
                return str(error)
        
    return flask.render_template(template_name_or_list= "registration.html")