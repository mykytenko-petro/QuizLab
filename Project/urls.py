import home_app
import registration_app
import create_quiz_app

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

registration_app.registrationApp.add_url_rule(
    rule='/code_confirmation',
    view_func=registration_app.render_code_confirmation,
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
    rule= '/quiz/<id>',
    view_func= create_quiz_app.render_create_quiz,
    methods = ['GET', 'POST']
)

create_quiz_app.createQuizApp.add_url_rule(
    rule= '/question/<id>',
    view_func= create_quiz_app.render_create_quiz,
    methods = ['GET', 'POST']
)