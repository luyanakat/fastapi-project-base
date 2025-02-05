from sqlalchemy import Column, String, Boolean, DateTime, Integer
from app.models.base import BareBaseModel

class Category(BareBaseModel):
    __tablename__ = 'categories'

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
