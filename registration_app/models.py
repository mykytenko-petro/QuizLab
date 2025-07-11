import flask_login
from Project.db import BaseModel, DATABASE as DB

class User(BaseModel, flask_login.UserMixin):
    __tablename__ = "user"

    id = DB.Column(DB.Integer, primary_key = True)

    login = DB.Column(DB.String(50), nullable = False)
    email = DB.Column(DB.String(50), nullable = False)
    password = DB.Column(DB.String(35), nullable = False)
    is_admin = DB.Column(DB.Boolean, default = False, nullable = False)

    quizzes = DB.relationship('Quiz', backref= 'user', cascade= 'all, delete-orphan')