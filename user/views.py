import secrets

import flask
import flask_login

from Project.db import DATABASE
from Project.utils import page_config
from Project.smtp_setup import send_email
from .models import User


@page_config("registration.html")
def render_registration():
    if flask.request.method == 'POST':
        form = flask.request.form
        
        if form['login']:
            if User.query.filter_by(email=form["email"]).first():
                message = "Така почта вже існує"

            elif not form["password"] == form["password_confirm"]:
                message = 'Паролі не співпадають'       
                
            else:
                confirmation_code = secrets.token_hex(6)

                flask.session["registration_input_data"] = {
                    "login": form['login'],
                    "password": form["password"],
                    "email": form["email"],
                    "confirmation_code": confirmation_code
                }

                send_email(
                    subject='Confirmation code',
                    recipients=[form['email']],
                    html=flask.render_template(
                        template_name_or_list="email_confirmation_in_mail.html",
                        confirmation_code=confirmation_code
                    )
                )

                return {"redirect": "/code_confirmation"}
            
            return {"message": message}


@page_config("email_confirmation.html")
def render_code_confirmation():
    if flask.request.method == 'POST':
        form = flask.request.form
        session_data = flask.session["registration_input_data"]
                
        if form["confirmation_code"] == session_data["confirmation_code"]:
            user = User(
                login=session_data['login'], 
                password=session_data["password"],
                email=session_data["email"],
                is_admin=False
            )
            flask.session.pop("registration_input_data")

            try:
                DATABASE.session.add(user)
                DATABASE.session.commit()
                
                flask_login.login_user(user)
                
                return {"redirect": "/"}
            except Exception as error:
                print(error)
        else:
            message = "неправильний код"

        return {"message": message}


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