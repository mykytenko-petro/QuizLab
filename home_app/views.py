import flask


#Функція що відображає сторінку  home
async def render_home():
    return flask.render_template("home.html")