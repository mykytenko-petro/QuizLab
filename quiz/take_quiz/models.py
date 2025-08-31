from sqlalchemy import (
    Column,
    Integer,
    Table,
    ForeignKey
)
from sqlalchemy.orm import relationship

from Project.db import DATABASE
from Project.types import BaseModel
