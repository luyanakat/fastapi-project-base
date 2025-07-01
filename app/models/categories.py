from sqlalchemy import Column, String, Boolean, DateTime, Integer
from app.models.base import BareBaseModel

class Category(BareBaseModel):
    __tablename__ = 'categories'

    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False)
