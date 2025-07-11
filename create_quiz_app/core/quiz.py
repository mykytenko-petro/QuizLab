import json
import os

import flask
import flask_login

from Project.db import DATABASE
from Project.utils import get_media_path
from ..models import Quiz


def quiz_handle():
    params = flask.request.args
    json_data = json.loads(flask.request.form["data"])
    file_data = flask.request.files

    if "id" in params:
        quiz: Quiz = Quiz.query.filter_by(id=params.get("id", type=int)).first()

    match params["goal"]: 
        case "create":
            quiz = Quiz()

            quiz.name = "your quiz"
            quiz.description = ""
            quiz.image = "default.png"

            flask_login.current_user.quizzes.append(quiz)
            DATABASE.session.commit()

            return { "id": quiz.id }
        
        case "read":
            data_dict = {}

            data_dict["quiz"] = quiz.to_dict()
            data_dict["questions"] = []

            for question in quiz.questions:
                data_dict["questions"].append(question.to_dict())

            return data_dict
            
        case "update":
            quiz.name = json_data["name"]
            quiz.description = json_data["description"]

            image = file_data.get('image')
            if image:
                image.save(dst=os.path.join(get_media_path(), "images", image.filename))
                quiz.image = image.filename

            DATABASE.session.add(quiz)
            DATABASE.session.commit()

            return quiz.to_dict()
        
        case "delete": 
            DATABASE.session.delete(quiz)
            DATABASE.session.commit()

            return {}