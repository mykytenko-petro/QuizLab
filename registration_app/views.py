import flask
import flask_login
from Project.db import DATABASE
#from Project.core import toggle
from .models import User
#registration_app.views import send_email

from flask_mail import Message
#from app import mail




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
                    
                    
                    def index():
                        msg = Message(
                            subject="Hello",
                            sender="italymay20@gmai.com",
                            recipients=["timagreen2010@gmail.com"],
                        )
                    index()
                    
                    #def send_email(subject, sender, recipients, text_body, html_body):
                    #        mail = ("123123")
                    #        msg = Message(subject, sender=sender, recipients=recipients)
                    #        msg.body = text_body
                    #        msg.html = html_body
                    #        mail.send(msg)
                    #send_email(
                    #    subject="s", 
                    #    sender="italymay20@gmail.com", 
                    #    recipients=["timagreen2010@gmail.com"],
                    #    text_body= flask.render_template('email/reset_password.txt', user=user, token=token),
                    #    html_body= flask.render_template('email/reset_password.html', user=user, token=token)) 
                    #
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

