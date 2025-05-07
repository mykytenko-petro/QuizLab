import home_app
import registration_app
import api

home_app.homeApp.add_url_rule(
    rule='/',
    view_func=home_app.render_home,
    methods = ['GET']
)

registration_app.registrationApp.add_url_rule(
    rule='/registration',
    view_func=registration_app.render_registration,
    methods=['GET', 'POST']
)

registration_app.loginApp.add_url_rule(
    rule = '/login',
    view_func = registration_app.render_login,
    methods = ['GET','POST']
)

registration_app.loginApp.add_url_rule(
    rule= '/logout',
    view_func= registration_app.render_logout,
    methods = ['GET']
)

api.apiApp.add_url_rule(
    rule= '/get_name',
    view_func= api.send_name,
    methods = ['POST']
)