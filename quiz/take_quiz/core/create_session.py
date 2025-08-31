import json

import flask

from Project.db import DATABASE
from user.models import User
# from ..models import QuizSession


# def create_quiz_session():
#     json_data = json.loads(flask.request.form["data"])

#     quiz_session = QuizSession()
#     quiz_session.quiz_id = json_data["quiz_id"]

#     users: list[User] = User.query.filter(User.id.in_(json_data["id_list"]))

#     for user in users:
#         user.quiz_sessions.append(quiz_session)
#         DATABASE.session.add(user)

#     DATABASE.session.add(quiz_session)
#     DATABASE.session.commit()

#     return {"quiz_session_id": quiz_session.id}