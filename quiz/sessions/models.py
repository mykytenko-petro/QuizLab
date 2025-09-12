from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from Project.types import BaseModel


class UserAnswers(BaseModel):
    __tablename__ = "user_answers"

    id = Column(
        Integer,
        primary_key=True
    )
    owner_id = Column(
        Integer,
        ForeignKey('user.id', name="fk_user_answers_owner_id")
    )
    quiz_session_id = Column(
        Integer,
        ForeignKey('quiz_session.id', name="fk_user_answers_quiz_session_id")
    )

    answers = relationship(
        argument='Answer',
        backref='user_answers',
        cascade='all, delete-orphan'
    )
    
class QuizSession(BaseModel):
    __tablename__ = "quiz_session"

    id = Column(
        Integer,
        primary_key=True
    )
    quiz_id = Column(Integer)

    is_group = Column(
        Boolean,
        default=False
    )

    user_answers = relationship(
        argument='UserAnswers',
        backref='quiz_session',
        cascade='all, delete-orphan'
    )