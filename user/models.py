import flask_login
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)
from sqlalchemy.orm import relationship

from Project.types import BaseModel


class User(BaseModel, flask_login.UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    login = Column(String(50))
    email = Column(String(50))
    password = Column(String(35))
    is_admin = Column(Boolean, default=False)

    quizzes = relationship(
        argument='Quiz',
        backref='user',
        cascade='all, delete-orphan'
    )

    user_answers = relationship(
        argument='UserAnswers',
        backref='user'
    )