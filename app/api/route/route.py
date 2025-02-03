from fastapi import APIRouter

from app.api.posts import api_posts, api_test


router = APIRouter()

router.include_router(api_posts.router, prefix="/posts", tags=["posts"])
router.include_router(api_test.router, prefix="/test", tags=["test"])