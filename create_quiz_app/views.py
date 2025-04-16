import flask

#Ця функція повертає файл create_quiz
def render_create_quiz():
    return flask.render_template("create_quiz.html")