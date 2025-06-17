import flask
import flask_login
import json
from flask import Flask, render_template, request
from os.path import abspath, join
from Project.db import DATABASE
from .models import Quiz, Question, Answer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def my_form():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('.html', name=name)
    return render_template('.html')

def handle_quiz_data(data : dict | None = None):
    if not data:
        print(flask.request.form)
        json_data = json.loads(flask.request.form["data"])
        file_data = flask.request.files

    else:
        json_data = data

    if "quiz" in json_data:
        if "id" in json_data["quiz"]:
            quiz: Quiz = Quiz.query.filter_by(id= json_data["quiz"]["id"]).first()

            if json_data["goal"] == "edit":
                quiz.name = json_data["quiz"]["name"]
                quiz.description = json_data["quiz"]["description"]

                image = file_data.get('image')
                if image:
                    image.save(dst= abspath(join(__file__, "..", "..", "Project", "static", "media", "images", f"{image.filename}")))
                    quiz.image = image.filename

                DATABASE.session.add(quiz)
                DATABASE.session.commit()

            elif "delete" in json_data["quiz"]:
                DATABASE.session.delete(quiz)
                DATABASE.session.commit()

                return {}
                
            return quiz.to_dict()

        else:
            quiz = Quiz()

            quiz.name = "your quiz"
            quiz.description = ""
            quiz.image = "default.png"

            flask_login.current_user.quizzes.append(quiz)
            DATABASE.session.commit()

            return flask.redirect(f"/quiz/{quiz.id}")
        
    elif "question" in json_data:
        ...
    elif "answer" in json_data:
        ...

# def handle_data(data):
#     print(data)

#     if "quiz" in data:
#         return create_quiz(data)

#     elif "question" in data:
#         return create_question(data)

#     elif "question" in data:
#         return create_answer(data)

# def create_quiz(data):
#     if "id" in data["quiz"]:
#         quiz: Quiz = Quiz.query.filter_by(id= json_data["quiz"]["id"]).first()
    
#     match data["goal"]:
#         case "create":
#             quiz = Quiz()

#             quiz.name = "your quiz"
#             quiz.description = ""
#             quiz.path_to_image = "default.png"

#             flask_login.current_user.quizzes.append(quiz)
#             DATABASE.session.commit()

#             return flask.redirect(f"/quiz/{quiz.id}")

#         case "edit":

#             quiz.name = json_data["quiz"]["name"]
#             quiz.description = json_data["quiz"]["description"]

#             image = data.files['image']
#             image.save(dst= abspath(join(__file__, "..", "static", "media", "images", f"{image.filename}")))
#             quiz.image = image.filename

#             DATABASE.session.add(quiz)
#             DATABASE.session.commit()

#         case "delete":
#             DATABASE.session.delete(quiz)
#             DATABASE.session.commit()

#             return {}
        
#         case "get":
#             ...

#     return quiz.to_dict()

# def create_question(data):
#     match data["goal"]:
#         case "create":
#             quiz = Quiz.query.filter_by(id= data["question"]["quiz_id"]).first()
#             question = Question()

#             quiz.questions.append(question)

#             DATABASE.session.add(quiz)
#             DATABASE.session.commit()

#         case "edit":
#             question: Question = Question.query.filter_by(id= data["question"]["id"]).first()

#             question.description = data["question"]["description"]
#             question.path_to_image = data["question"]["path_to_image"]

#             DATABASE.session.add(question)
#             DATABASE.session.commit()

#         case "delete":
#             question: Question = Question.query.filter_by(id= data["question"]["id"]).first()

#             DATABASE.session.delete(question)
#             DATABASE.session.commit()

#     return question.to_dict()

# def create_answer(data):
#     match data["goal"]:
#         case "create":
#             question = Question.query.filter_by(id= data["answer"]["question_id"]).first()
#             answer = Answer()

#             question.answers.append(answer)

#             DATABASE.session.add(question)
#             DATABASE.session.commit()

#         case "edit":
#             answer: Answer = Answer.query.filter_by(id= data["answer"]["id"]).first()

#             answer.description = data["description"]
#             answer.path_to_image = data["path_to_image"]

#             DATABASE.session.add(question)
#             DATABASE.session.commit()

#         case "delete":
#             answer: Answer = Answer.query.filter_by(id= data["answer"]["id"]).first()

#             DATABASE.session.delete(answer)
#             DATABASE.session.commit()

#             return {}

#     return answer.to_dict()