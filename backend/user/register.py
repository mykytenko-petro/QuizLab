from typing import Annotated

from fastapi import Form, Depends
from pydantic import BaseModel
from sqlalchemy import select

from Project.database import ASYNC_SESSION_MAKER
from .manager import UserManager, get_user_manager
from .models import User
from .schemas import UserCreate


class RegisterPayload(BaseModel):
    username : str
    email : str
    password : str
    password_confirm : str

async def register(
        form : Annotated[RegisterPayload, Form()],
        user_manager : UserManager = Depends(get_user_manager)
    ):
    async with ASYNC_SESSION_MAKER() as session:
        result = await session.execute(select(User).where(User.email == form.email)) # type: ignore

        if result.scalar_one_or_none():
            return {"error": "user is already exist"}

    if form.password == form.password_confirm:
        user_data = UserCreate(
            username=form.username,
            email=form.email,
            password=form.password
        )

        user: User = await user_manager.create(user_data)
        return {"message": "succsesfully created user:"}
    else:
        return {"error": "passwords don't match"}