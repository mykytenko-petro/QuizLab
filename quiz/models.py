from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)
from sqlalchemy.orm import relationship

from Project.types import BaseModel


class Quiz(BaseModel):
    __tablename__ = "quiz"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    name = Column(String(50), nullable=True)
    description = Column(String(256), nullable=True)
    image = Column(String(256), nullable=True)

    questions = relationship('Question', backref='quiz', cascade='all, delete-orphan')

class Question(BaseModel):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quiz.id'), nullable=False)

    description = Column(String(256), nullable=True)
    image = Column(String(256), nullable=True)
    
    answers = relationship('Answer', backref='question', cascade='all, delete-orphan')

class Answer(BaseModel):
    __tablename__ = "answer"

    id = Column(Integer, primary_key = True)
    question_id = Column(Integer, ForeignKey('question.id'), nullable=False)

    description = Column(String(256), nullable=True)
    image = Column(String(256), nullable=True)
    is_right = Column(Boolean, default=False, nullable=True)