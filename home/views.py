from Project.utils import page_config
from quiz.models import Quiz
import random

@page_config("home.html")
def render_home():
    return None

@page_config("dashboard.html")
def render_dashboard():
    quizes = Quiz.query.all()
    random_quizes = []
    for count in range(5):
        random_quizes.append(quizes[random.randint(0, len(quizes)-1)])
    if random_quizes:
        return {"quizes": random_quizes}
    else:
        return {"quizes": []}