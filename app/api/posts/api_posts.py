from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.postgres import get_db
from app.models.posts import Post
from app.services.post_service import PostService


post_router = APIRouter()

def get_post_service(db: Session = Depends(get_db)) -> PostService:
    return PostService(db)

@post_router.get("/{post_id}", tags=["posts"])
def get_post(post_id: int, post_service: PostService = Depends(get_post_service)):
    post = post_service.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@post_router.post("", tags=["posts"])
def create_post(request: dict, post_service: PostService = Depends(get_post_service)):
    title = request.get("title")
    content = request.get("content")

    row=Post(title=title, content=content,)
    res = post_service.create_post(row)
    return res