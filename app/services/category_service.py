from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.db.postgres import get_db
from app.models.categories import Category
from app.repository.category_repo import CategoryRepository


class CategoryService(object):
    def __init__(self, db_session: Session):
        self.category_repo = CategoryRepository(db_session)
        
    
    def get_category(self, category_id: int):
        return self.category_repo.get_category_by_id(category_id)
    
    
    def create_category(self, request: dict):
        name = request.get("name")
        description = request.get("description")

        if not name:
            raise HTTPException(status_code=400, detail="Name is required")

        row = Category(name=name, description=description)
        return self.category_repo.create_category(row)