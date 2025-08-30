import json
import os

import flask

from Project.db import DATABASE
from Project.utils import get_media_path
from ...models import Quiz, Question

def create_question(params):
    quiz = Quiz.query.filter_by(id=params.get("quiz_id", type=int)).first()
    question = Question()

    question.description = ""
    question.image = ""

    quiz.questions.append(question)
    DATABASE.session.add(quiz)
    DATABASE.session.commit()

    return { "id": question.id }

def update_question(question : Question, json_data, file_data):
    question.description = json_data["description"]
    image = file_data.get('image')
    
    if image:
        image.save(dst=os.path.join(get_media_path(), "images", image.filename))
        question.image = image.filename

    DATABASE.session.add(question)
    DATABASE.session.commit()

    return question.to_dict()

def delete_question(question : Question):
    DATABASE.session.delete(question)
    DATABASE.session.commit()

    return {}

def read_question(question : Question):
    data_dict = {}     
    data_dict["question"] = question.to_dict()
    data_dict["answers"] = []

    for answer in question.answers:
        data_dict["answers"].append(answer.to_dict())

    return data_dict



def question_handle():
    params = flask.request.args
    json_data = json.loads(flask.request.form["data"])
    file_data = flask.request.files

    if "id" in params:
        question: Question = Question.query.filter_by(id=params.get("id", type=int)).first()

    match params["goal"]: 
        case "create":
            return create_question(params=params)
        
        case "read":
            return read_question(question=question)
            
        case "update":
            return update_question(question=question, json_data=json_data, file_data=file_data)
        
        case "delete": 
            return delete_question(question=question)