import uuid

from pydantic import BaseModel
from fastapi_users import schemas


class UserAbstract(BaseModel):
    username: str

class UserRead(schemas.BaseUser[uuid.UUID], UserAbstract): pass

class UserCreate(schemas.BaseUserCreate, UserAbstract): pass

class UserUpdate(schemas.BaseUserUpdate, UserAbstract):
    username: str | None = None