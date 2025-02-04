import json
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime

@as_declarative()
class BaseModel:
    __abstract__ = True
    __name__: str

    def __to_dict__(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __to_json_byte__(self):
        return json.dumps(self.__to_dict__(), default=str).encode('utf-8')

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class BareBaseModel(BaseModel):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)