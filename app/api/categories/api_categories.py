from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.categories import Category
from app.services.category_service import CategoryService
from app.db.postgres import get_db


category_router = APIRouter()

def get_category_service(db: Session = Depends(get_db)):
    return CategoryService(db)


@category_router.get("/{category_id}", tags=["categories"])
def get_category(category_id: int, category_service: CategoryService = Depends(get_category_service)):
    category = category_service.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@category_router.post("", tags=["categories"])
def create_category(request: dict, category_service: CategoryService = Depends(get_category_service)):
    return category_service.create_category(request)