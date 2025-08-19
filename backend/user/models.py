from typing import List

from sqlalchemy import String
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from Project.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    '''
    SQLAlchemyBaseUserTableUUID already provides:
        id: UUID
        email: str
        hashed_password: str
        is_active: bool
        is_superuser: bool
        is_verified: bool
    '''

    username: Mapped[str] = mapped_column(String(35), nullable=False)

    # quizzes: Mapped[List["Quiz"]] = relationship(
    #     back_populates="user", cascade="all, delete-orphan"
    # )