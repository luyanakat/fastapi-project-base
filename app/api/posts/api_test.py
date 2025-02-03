from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from app.models.posts import Posts
from app.services.post_service import PostService

router = APIRouter()

# test api
@router.get("", tags=["test"])
async def test():
    row = PostService.get_post(1)
    return {"message": "Hello, FastAPI!", "row": row}