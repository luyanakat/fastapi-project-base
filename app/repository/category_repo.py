from app.models.categories import Category
from sqlalchemy.orm import Session


class CategoryRepository:
    def __init__(self, session: Session):
        self.session = session
        
    
    def get_category_by_id(self, category_id: int):
        return self.session.query(Category).filter(Category.id == category_id).first()
    
    
    def create_category(self, category):
        self.session.add(category)
        self.session.commit()
        return category