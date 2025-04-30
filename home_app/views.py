import flask
import flask_login

#Функція що відображає сторінку  home
def render_home():
    

    return flask.render_template(
        template_name_or_list= "home.html"
    )