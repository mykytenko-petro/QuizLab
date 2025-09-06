import random

from werkzeug import Response

from Project.utils import page_config
from quiz.create.models import Quiz
from flask import redirect, request


def index() -> Response:
    return redirect(location='/dashboard')


@page_config(template_name="dashboard.html")
def render_dashboard():
    quizzes = Quiz.query.all()
    num_to_select = 5

    num_to_select = min(len(quizzes), num_to_select)

    random_quizes = random.sample(quizzes, k=num_to_select)

    return {"quizzes": random_quizes}


@page_config(template_name="search.html")
def render_quiz_search():
    search = request.args.get("search", "").strip()
    results = []

    if search:
        results = Quiz.query.filter(Quiz.name.ilike(f"%{search}%")).all()
    
    return {"results": results, "search": search}