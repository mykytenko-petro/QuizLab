import secrets

import flask

from Project.utils import page_config
from Project.smtp_setup import send_email
from ..models import User


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
                        template_name_or_list="email_confirmation_mail.html",
                        confirmation_code=confirmation_code
                    )
                )

                return {"redirect": "/email_confirmation"}
            
            return {"message": message}