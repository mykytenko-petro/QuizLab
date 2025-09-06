import json
import os

import flask
import flask_login

from Project.db import DATABASE
from Project.utils import get_media_path
from ..models import Quiz


def create_quiz():
    quiz = Quiz()

    quiz.name = "Untiled"
    quiz.description = ""
    quiz.image = "default.png"

    flask_login.current_user.quizzes.append(quiz)
    DATABASE.session.commit()

    return { "id": quiz.id }

def read_quiz(quiz : Quiz):
    data_dict = {}

    data_dict["quiz"] = quiz.to_dict()
    data_dict["questions"] = []

    for question in quiz.questions:
        data_dict["questions"].append(question.to_dict())

    return data_dict

def update_quiz(quiz : Quiz, json_data, file_data):
    quiz.name = json_data["name"]
    quiz.description = json_data["description"]

    image = file_data.get('image')
    if image:
        image.save(dst=os.path.join(get_media_path(), "images", image.filename))
        quiz.image = image.filename

    DATABASE.session.add(quiz)
    DATABASE.session.commit()

    return quiz.to_dict()

def delete_quiz(quiz : Quiz):
    DATABASE.session.delete(quiz)
    DATABASE.session.commit()

    return {}
    
def quiz_handle():
    params = flask.request.args
    json_data = json.loads(flask.request.form.get("data") or r"{}") 
    file_data = flask.request.files

    if "id" in params:
        quiz: Quiz = Quiz.query.filter_by(id=params.get("id", type=int)).first()

    match params["goal"]: 
        case "create":
            return create_quiz()
        
        case "read":
            return read_quiz(quiz=quiz)
            
        case "update":
            return update_quiz(quiz=quiz, json_data=json_data, file_data=file_data)
        
        case "delete": 
            return delete_quiz(quiz=quiz)