from .settings import userApp
from .views import (
    render_registration,
    render_email_confirmation,
    render_login,
    logout,
    render_profile,
)


userApp.add_url_rule(
    rule='/registration',
    view_func=render_registration,
    methods=['GET', 'POST']
)

userApp.add_url_rule(
    rule='/email_confirmation',
    view_func=render_email_confirmation,
    methods=['GET', 'POST']
)

userApp.add_url_rule(
    rule='/login',
    view_func=render_login,
    methods=['GET','POST']
)

userApp.add_url_rule(
    rule='/logout',
    view_func=logout,
    methods=['GET']
)

userApp.add_url_rule(
    rule="/profile/<id>",
    view_func=render_profile,
    methods=['GET'] 
)