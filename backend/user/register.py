from typing import Annotated

from fastapi import Form
from pydantic import BaseModel

from .models import User


class RegisterPayload(BaseModel):
    username : str
    email : str
    password : str
    password_confirm : str

async def register(form : Annotated[Annotated, Form()]):
    statement = User