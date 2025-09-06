from Project.utils import login_required, page_config


@login_required
@page_config("create_quiz.html")
def render_create_quiz(id):
    return None

@login_required
@page_config("create_question.html")
def render_create_question(id):
    return None