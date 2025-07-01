from sqlalchemy import Column, ForeignKey, String, Boolean, DateTime, Integer
from app.models.base import BareBaseModel

class Post(BareBaseModel):
    __tablename__ = 'posts'

    title = Column(String(255),index=True, nullable=False)
    content = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
