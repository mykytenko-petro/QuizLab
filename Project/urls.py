import home_app
import registration_app
import create_quiz_app
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
    view_func= registration_app.logout,
    methods = ['GET']
)

create_quiz_app.createQuizApp.add_url_rule(
    rule= '/create_quiz',
    view_func= create_quiz_app.render_create_quiz,
    methods = ['GET', 'POST']
)

create_quiz_app.createQuizApp.add_url_rule(
    rule= '/create_quiz_api',
    view_func= create_quiz_app.create_quiz_api,
    methods = ['POST']
)

api.apiApp.add_url_rule(
    rule= '/get_name',
    view_func= api.send_name,
    methods = ['POST']
)