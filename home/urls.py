from .app import homeApp
from .views import index, render_dashboard, render_quiz_search

homeApp.add_url_rule(
    rule="/",
    view_func=index,
)

homeApp.add_url_rule(
    rule='/dashboard',
    view_func= render_dashboard,
    methods=['GET', 'POST']
)

homeApp.add_url_rule(
    rule='/search_result',
    view_func= render_quiz_search,
    methods=['GET']
)
