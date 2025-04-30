import flask
from Project.settings import DATABASE
from .models import User
import flask_login
import flask_session

def render_registration():
    message = ''
    if flask.request.method == 'POST':
        password = flask.request.form["password"]
        confirm_password = flask.request.form["password_confirm"]

        # is_email_found = 

        # list_users = User.query.all()
        # for user in list_users:
        #     if user.email == flask.request.form["email"]:
                


        if password == confirm_password:
            user = User(
                login = flask.request.form['name'], 
                password = password, 
                email = flask.request.form["email"], 
                is_admin = False
            )
            message = 'Успішна реєстрація'
        else:
            message = 'Паролі не співпадають'
            try:
                DATABASE.session.add(user)
                DATABASE.session.commit()
                
            except Exception as error:
                return str(error)
        
    return flask.render_template(
        template_name_or_list= "registration.html",
        message= message
    )

def render_login():
    if flask.request.method == "POST":
        username_form = flask.request.form["login"]
        password_form = flask.request.form["password"]
        list_users = User.query.all()

        for user in list_users:
            if user.login == username_form and user.password == password_form:
                flask_login.login_user(user)
    if not flask_login.current_user.is_authenticated:
        return flask.render_template(template_name_or_list = "login.html")
    else:
        return flask.redirect('/')
    

def render_logout():
    DATABASE.session.close()
    return flask.redirect('/')