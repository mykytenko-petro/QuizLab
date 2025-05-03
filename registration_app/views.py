import flask
import flask_login
import flask_session
from Project.settings import DATABASE
from .models import User
from Project.core import toggle

@toggle(name_of_bp="registrationApp")
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

            try:
                DATABASE.session.add(user)
                DATABASE.session.commit()

                message = 'Успішна реєстрація'
                
                return render_login()

            except Exception as error:
                return str(error)
        else:
            message = 'Паролі не співпадають'
        
    return flask.render_template(
        template_name_or_list= "registration.html",
        message= message
    )

@toggle(name_of_bp="loginApp")
def render_login():
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
        return flask.redirect('/')
    
def render_logout():
    flask.session.clear()
    return flask.redirect('/')