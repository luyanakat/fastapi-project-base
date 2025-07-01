from fastapi import APIRouter
from app.api.categories import api_categories
from app.api.posts import api_posts, api_test


router = APIRouter()

router.include_router(api_categories.category_router, prefix="/category", tags=["category"])
router.include_router(api_posts.post_router, prefix="/posts", tags=["posts"])
router.include_router(api_test.test_router, prefix="/test", tags=["test"])