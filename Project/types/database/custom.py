from sqlalchemy.orm import DeclarativeMeta

from ...db import DATABASE


Base: DeclarativeMeta = DATABASE.Model

class BaseModel(Base):
    r"""
        custom model with useful methods
    """

    __abstract__ = True
    
    def to_dict(self) -> dict:
        r"""
            returns model representation as a dict
            (relationships are not supported)
        """

        model_dict = {}

        for column in self.__table__.columns:
            model_dict.update({column.name: getattr(self, column.name)})

        return model_dict