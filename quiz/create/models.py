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
    owner_id = Column(
        Integer,
        ForeignKey('user.id', name='fk_quiz_owner_id')
    )

    name = Column(String(50))
    description = Column(String(256))
    image = Column(String(256))

    questions = relationship(
        argument='Question',
        backref='quiz',
        cascade='all, delete-orphan'
    )

class Question(BaseModel):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    quiz_id = Column(
        Integer,
        ForeignKey('quiz.id', name='fk_question_owner_id')
    )

    description = Column(String(256))
    image = Column(String(256))
    
    answers = relationship(
        'Answer',
        backref='question',
        cascade='all, delete-orphan'
    )

class Answer(BaseModel):
    __tablename__ = "answer"

    id = Column(Integer, primary_key = True)
    question_id = Column(
        Integer,
        ForeignKey('question.id', name='fk_answer_owner_id'),
        nullable=True
    )
    user_answers_id = Column(
        Integer,
        ForeignKey('user_answers.id', name='fk_user_answers_owner_id'),
        nullable=True
    )

    description = Column(String(256))
    image = Column(String(256))
    is_right = Column(Boolean, default=False)

    is_chosen = Column(Boolean, default=False)