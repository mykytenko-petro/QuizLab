from .app import homeApp
from .views import render_home

homeApp.add_url_rule(
    rule="/",
    view_func=render_home,
)

homeApp.add_url_rule(
    rule='/dashboard',
    view_func= render_home,
    methods=['GET', 'POST']
)
