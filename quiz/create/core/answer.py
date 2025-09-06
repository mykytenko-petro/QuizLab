import json
import os

import flask

from Project.db import DATABASE
from Project.utils import get_media_path
from ..models import Question, Answer


def create_answer(params):
    question = Question.query.filter_by(id=params.get("question_id", type=int)).first()
    answer = Answer()
            
    answer.description = ""
    answer.image = ""

    question.answers.append(answer)
    DATABASE.session.add(question)
    DATABASE.session.commit()

    return { "id": answer.id }

def read_answer(answer : Answer):
    return answer.to_dict()

def update_answer(answer : Answer, json_data, file_data):
    answer.description = json_data["description"]

    image = file_data.get('image')
    if image:
        image.save(dst=os.path.join(get_media_path(), "images", image.filename))
        answer.image = image.filename
            
    answer.is_right = json_data["is_right"]

    DATABASE.session.add(answer)
    DATABASE.session.commit()

    return answer.to_dict()

def delete_answer(answer : Answer):
    DATABASE.session.delete(answer)
    DATABASE.session.commit()
    return {}

def answer_handle():
    params = flask.request.args
    json_data = json.loads(flask.request.form["data"])
    file_data = flask.request.files

    if "id" in params:
        answer: Answer = Answer.query.filter_by(id=params.get("id", type=int)).first()

    match params["goal"]: 
        case "create": 
            return create_answer(params=params)
        
        case "read":
            return read_answer(answer=answer)
            
        case "update":
            return update_answer(answer=answer, json_data=json_data, file_data=file_data)
        
        case "delete": 
            return delete_answer(answer=answer)