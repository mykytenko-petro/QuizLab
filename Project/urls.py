from .settings import project

# Import apps inside this file to avoid circular imports
import home_app
import registration_app

project.add_url_rule(
    rule='/',
    view_func=home_app.render_home
)
project.add_url_rule(
    rule='/registration',
    view_func=registration_app.render_registration,
    methods=['GET', 'POST']
)
project.add_url_rule(
    rule = '/login',
    view_func = registration_app.render_login,
    methods = ['GET','POST']
)
