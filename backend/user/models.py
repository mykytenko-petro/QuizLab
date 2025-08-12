from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)
from sqlalchemy.orm import relationship

from Project.types import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    login = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(35), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)

    quizzes = relationship('Quiz', backref='user', cascade='all, delete-orphan')