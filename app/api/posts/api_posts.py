from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.db.postgres import get_db
from app.models.posts import Post
from app.services.post_service import PostService


post_router = APIRouter()

def get_post_service(db: Session = Depends(get_db)) -> PostService:
    return PostService(db)

@post_router.get("/{post_id}", tags=["posts"])
def get_post(post_id: int, post_service: PostService = Depends(get_post_service)):
    return post_service.get_post(post_id)


@post_router.post("", tags=["posts"])
def create_post(request: dict, post_service: PostService = Depends(get_post_service)):
    return post_service.create_post(request)


@post_router.get("", tags=["posts"])
def get_posts(request: Request, post_service: PostService = Depends(get_post_service)):
    query_params = request.query_params
    return post_service.get_posts(query_params)