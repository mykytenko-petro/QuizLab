import flask

def render_create_quiz():
    return flask.render_template(template_name_or_list= "create_quiz.html")