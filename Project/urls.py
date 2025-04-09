import home_app
import create_quiz_app
import registration_app
import login_app
from .settings import project

project.add_url_rule(
    rule = '/',
    view_func = home_app.render_home
)
project.add_url_rule(
    rule = '/create_quiz',
    view_func = create_quiz_app.render_create_quiz
)
project.add_url_rule(
    rule = '/registration',
    view_func = registration_app.render_registration,
    methods = ['GET','POST']
)
project.add_url_rule(
    rule = '/login',
    view_func = login_app.render_login,
    methods = ['GET','POST']
)