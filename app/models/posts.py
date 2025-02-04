import json
from sqlalchemy import func
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from app.models.base import BareBaseModel

class Post(BareBaseModel):
    __tablename__ = 'posts'

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category_id = Column(Integer, nullable=False)


    def __to_json_bytes__(self):
        return json.dumps(self.__to_dict__()).encode('utf-8')