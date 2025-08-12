import os

import sqlalchemy

from .types import BaseModel
from user import User

DATABASE = sqlalchemy.create_engine(os.environ["DB_URL"])

BaseModel.metadata.create_all(DATABASE)