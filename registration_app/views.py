import flask
from Project.settings import DATABASE
from registration_app.core import login
from .models import User

async def render_registration():
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
                login()
                
            except Exception as error:
                return str(error)
        
    return flask.render_template("registration.html")

async def render_login():
    if flask.request.method == "POST":
        login()
    
    return flask.render_template("login.html")

