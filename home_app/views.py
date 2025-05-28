import flask


#Функція що відображає сторінку  home
def render_home():
    return flask.render_template("home.html")