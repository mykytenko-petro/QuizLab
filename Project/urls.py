import home_app
import create_quiz_app

home_app.homeApp.add_url_rule(rule = '/', view_func = home_app.render_home)
create_quiz_app.createQuizApp.add_url_rule(rule = '/create_quiz', view_func = create_quiz_app.render_create_quiz)