import flask


#Функція що повертає сторінку  home
def render_home():
    return flask.render_template("home.html")