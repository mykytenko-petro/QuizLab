import flask
import flask_login
import secrets
from Project.db import DATABASE
from Project.core import toggle
from .models import User

user_session = []

def user_seek(incoming_user_session):
    for session in user_session:
        # print(
        #     "server_side:\n", session["user_session"],
        #     "client side:\n", incoming_user_session
        # )
        if session["user_session"] == incoming_user_session:
            return session
    else:
        return None

@toggle(name_of_bp="registrationApp")
def render_registration():
    message = ''
    
    if flask.request.method == 'POST':
        form = flask.request.form
        
        session = user_seek(form["user_session"])
        if not session:
            list_users = User.query.all()
            for user in list_users:
                if user.email == form["email"]:
                    message = "Така почта вже існує"

            if message == "":
                if form["password"] == form["password_confirm"]:
                    confirmation_code = secrets.token_hex(6)
                    print(confirmation_code)
                    user_session.append(
                        {
                            "login": form['login'],
                            "password": form["password"],
                            "email": form["email"],
                            "user_session": form["user_session"],
                            "confirmation_code": confirmation_code
                        }
                    )
                    return flask.render_template(
                        template_name_or_list= "email_confirmation.html",
                        message= message
                    )
                
                else:
                    message = 'Паролі не співпадають'
        else:
            if form["confirmation_code"] == session["confirmation_code"]:
                user = User(
                    login = session['login'], 
                    password = session["password"],
                    email = session["email"],
                    is_admin = False
                )
                try:
                    DATABASE.session.add(user)
                    DATABASE.session.commit()
                    
                    return render_login(incoming_user= user)
                except Exception as error:
                    print(error)
            else:
                message = "неправильний код"

            return flask.render_template(
                template_name_or_list= "email_confirmation.html",
                message= message
            )
            
    flask.session["user_session"] = secrets.token_hex(32)
    return flask.render_template(
        template_name_or_list= "registration.html",
        message= message
    )

@toggle(name_of_bp="loginApp")
def render_login(incoming_user: User | None = None):
    if flask.request.method == "POST":
        form = flask.request.form

        list_users = User.query.all()
        if incoming_user:
            flask_login.login_user(incoming_user)
            flask.session["username"] = flask_login.current_user.login
        else:
            for user in list_users:
                if user.email == form["email"] and user.password == form["password"]:
                    flask_login.login_user(user)
                    flask.session["username"] = flask_login.current_user.login
    
    if not flask_login.current_user.is_authenticated:
        return flask.render_template(template_name_or_list = "login.html")
    else:
        return flask.redirect('/')
    
def render_logout():
    flask.session.clear()
    return flask.redirect('/')