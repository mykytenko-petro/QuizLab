import flask
import flask_login
from Project.utils import toggle, login_checker
from Project.db import DATABASE
from .models import Quiz, Question, Answer

def assemble_quiz(data : dict) -> Quiz:
    quiz = Quiz(
        name= data["name"],
        description= data["description"],
    )

    for question_data in data["questions"]:
        question = Question(
            description= question_data["description"],
            path_to_image= question_data["path_to_image"],
        )

        for answer_data in question_data["answers"]:
            answer = Answer(
                description= answer_data["description"],
                path_to_image= answer_data["path_to_image"],
                is_right= answer_data["is_right"]
            )

            question.answers.append(answer)

        quiz.questions.append(question)

    return quiz

@toggle(name_of_bp= "createQuizApp")
@login_checker
def render_create_quiz():
    if flask.request.method == "POST":
        quiz_data = flask.request.json["quiz_data"]
        
        flask_login.current_user.quizzes.append(assemble_quiz(quiz_data))
        DATABASE.session.commit()

    return flask.render_template(template_name_or_list= "create_quiz.html")