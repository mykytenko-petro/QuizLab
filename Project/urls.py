import home_app
from .settings import project

# home_app.homeApp.add_url_rule(rule = '/', view_func = home_app.render_home)
project.add_url_rule(rule = '/', view_func = home_app.render_home)