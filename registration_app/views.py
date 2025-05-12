import flask
import flask_login
from Project.db import DATABASE
from Project.core import toggle
from .models import User
from .core import send_email

async def render_registration():
    if flask.request.method == 'POST':
        password = flask.request.form["password"]
        confirm_password = flask.request.form["password_confirm"]

        list_users = User.query.all()
        for user in list_users:
            if user.email == flask.request.form["email"]:
                message = "Така почта вже існує"

        if message == "":   
            if password == confirm_password:
                user = User(
                    login = flask.request.form['login'], 
                    password = password, 
                    email = flask.request.form["email"], 
                    is_admin = False
                )
        
                try:
                    # send_email(
                    #     subject = "First try",                      
                    #     recipients = flask.request.form["email"],
                    #     text_body = "2232"

                    # )
                    DATABASE.session.add(user)
                    DATABASE.session.commit()

                    message = 'Успішна реєстрація'
                    
                    return render_login()

                except Exception as error:
                    return str(error)
            else:
                message = 'Паролі не співпадають'
        
    return flask.render_template("registration.html")

async def render_login():
    if flask.request.method == "POST":
        email_form = flask.request.form["email"]
        password_form = flask.request.form["password"]

        list_users = User.query.all()
        for user in list_users:
            if user.email == email_form and user.password == password_form:
                flask_login.login_user(user)
    
    if not flask_login.current_user.is_authenticated:

        return flask.render_template(template_name_or_list = "login.html")
    else:
        # flask.logging.render_user()
        return flask.redirect('/')
    
def render_logout():
    flask.session.clear()
    return flask.redirect('/')

