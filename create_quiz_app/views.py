from Project.utils import toggle, login_required, page_config

@toggle(name_of_bp= "createQuizApp")
@login_required
@page_config(template_name= "create_quiz.html")
def render_create_quiz(id):
    return None

@toggle(name_of_bp= "createQuizApp")
@login_required
@page_config(template_name= "create_question.html")
def render_create_question(id):
    return None