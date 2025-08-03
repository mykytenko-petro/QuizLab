import home
import user
import quiz


home.homeApp.add_url_rule(
    rule='/',
    view_func=home.render_home,
    methods = ['GET']
)

user.registrationApp.add_url_rule(
    rule='/registration',
    view_func=user.render_registration,
    methods=['GET', 'POST']
)

user.registrationApp.add_url_rule(
    rule='/code_confirmation',
    view_func=user.render_code_confirmation,
    methods=['GET', 'POST']
)

user.loginApp.add_url_rule(
    rule = '/login',
    view_func = user.render_login,
    methods = ['GET','POST']
)

user.loginApp.add_url_rule(
    rule= '/logout',
    view_func= user.logout,
    methods = ['GET']
)

quiz.createQuizApp.add_url_rule(
    rule= '/quiz/<id>',
    view_func= quiz.render_create_quiz,
    methods = ['GET', 'POST']
)

quiz.createQuizApp.add_url_rule(
    rule= '/question/<id>',
    view_func= quiz.render_create_question,
    methods = ['GET', 'POST']
)