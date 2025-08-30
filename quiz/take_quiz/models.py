from sqlalchemy import (
    Column,
    Integer,
    Table,
    ForeignKey
)
from sqlalchemy.orm import relationship

from Project.db import DATABASE
from Project.types import BaseModel


quiz_session_user_assosiation = Table(
    "quiz_session_user_assosiation",
    DATABASE.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('quiz_session_id', Integer, ForeignKey('quiz_session.id'), primary_key=True)
)

class QuizSession(BaseModel):
    __tablename__ = "quiz_session"

    id = Column(Integer, primary_key=True)

    quiz_id = Column(Integer, nullable=False)