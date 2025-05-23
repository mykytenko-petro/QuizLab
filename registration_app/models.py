from Project.db import BaseModel, DATABASE as DB
from flask_login import UserMixin

class User(BaseModel, UserMixin):
    id = DB.Column(DB.Integer, primary_key = True)

    login = DB.Column(DB.String(50), nullable = False)
    email = DB.Column(DB.String(50), nullable = False)
    password = DB.Column(DB.String(35), nullable = False)
    is_admin = DB.Column(DB.Boolean, default = False, nullable = False)

    quizzes = DB.relationship('Quiz', backref= 'user', cascade= 'all, delete-orphan')