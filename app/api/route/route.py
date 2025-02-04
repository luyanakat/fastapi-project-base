from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from app.db.postgres import get_db
from app.models.posts import Post
from app.services.post_service import PostService
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.posts import api_posts, api_test


router = APIRouter()

router.include_router(api_posts.post_router, prefix="/posts", tags=["posts"])
router.include_router(api_test.test_router, prefix="/test", tags=["test"])