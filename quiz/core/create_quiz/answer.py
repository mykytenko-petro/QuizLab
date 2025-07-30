import json
import os

import flask

from Project.db import DATABASE
from Project.utils import get_media_path
from ...models import Question, Answer


def answer_handle():
    params = flask.request.args
    json_data = json.loads(flask.request.form["data"])
    file_data = flask.request.files

    if "id" in params:
        answer: Answer = Answer.query.filter_by(id=params.get("id", type=int)).first()

    match params["goal"]: 
        case "create": 
            question = Question.query.filter_by(id=params.get("question_id", type=int)).first()
            answer = Answer()
            
            answer.description = ""
            answer.image = ""

            question.answers.append(answer)
            DATABASE.session.add(question)
            DATABASE.session.commit()

            return { "id": answer.id }
        
        case "read":
            return answer.to_dict()
            
        case "update":
            answer.description = json_data["description"]

            image = file_data.get('image')
            if image:
                image.save(dst=os.path.join(get_media_path(), "images", image.filename))
                answer.image = image.filename
            
            answer.is_right = json_data["is_right"]

            DATABASE.session.add(answer)
            DATABASE.session.commit()

            return answer.to_dict()
        
        case "delete": 
            DATABASE.session.delete(answer)
            DATABASE.session.commit()

            return {}