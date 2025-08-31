import flask_login
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)
from sqlalchemy.orm import relationship

from Project.types import BaseModel
# from quiz.take_quiz.models import quiz_session_user_assosiation


class User(BaseModel, flask_login.UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    login = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(35), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    quizzes = relationship('Quiz', backref='user', cascade='all, delete-orphan')
    passed_quizzes = Column(Integer, nullable=True, default=0)

    # quiz_sessions = relationship("QuizSession", secondary=quiz_session_user_assosiation, backref="users", lazy=True)