from typing import Any

import flask
import flask_login

from Project.utils import page_config
from Project.db import DATABASE
from user.views.login import ImmutableMultiDict
from ..models import User


@page_config(template_name="email_confirmation.html")
def render_email_confirmation() -> dict[str, str] | dict[str, Any | str] | None:
    if flask.request.method == 'POST':
        form: ImmutableMultiDict[str, str] = flask.request.form
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
                DATABASE.session.add(instance=user)
                DATABASE.session.commit()
                
                flask_login.login_user(user=user)
                
                return {"redirect": "/"}
            except Exception as error:
                print(error)
        else:
            message = "неправильний код"

        return {"message": message}