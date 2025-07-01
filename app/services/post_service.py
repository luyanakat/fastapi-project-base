from http.client import HTTPException
import json
from app.db.postgres import get_db
from app.db.redis import get_redis
from app.models.posts import Post
from app.repository.post_repo import PostRepository
from sqlalchemy.orm import Session
from app.helpers.log import logger
import logging


class PostService(object):
    def __init__(self, db_session: Session):
        self.post_repo = PostRepository(db_session)
        self.redis_client = get_redis()

    def get_post(self, post_id: int):
        res = self.redis_client.get_json(post_id)
        if res:
            return res

        post = self.post_repo.get_post_by_id(post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
    
        self.redis_client.set_with_ttl(post_id, post.__to_json_byte__(), 5)
        return post
    
    def create_post(self, request: dict):
        title = request.get("title")
        content = request.get("content")
        category_id = request.get("category_id")
        if not category_id:
            raise ValueError("Category ID is required")
        
        if not title:
            raise ValueError("Title is required")
        if not content:
            raise ValueError("Content is required")
        
        post = Post(title=title, content=content, category_id=category_id)
        return self.post_repo.create_post(post)
    
    
    def get_posts(self, request):
        page = int(request.get("page", 1))
        limit = int(request.get("limit", 10))
        title = request.get("title")
        category_id = request.get("category_id")
        
        key_ = f"posts:{page}:{limit}:{title}:{category_id}"
        cached_posts = self.redis_client.get_json(key_)
        if cached_posts:
            logger.info(f"Cache hit for key: {key_}")
            return cached_posts
        
        if not isinstance(page, int) or not isinstance(limit, int):
            raise ValueError("Page and limit must be integers")
        if page < 1 or limit < 1:
            logger.error("Page and limit must be greater than 0")
            return []
        posts = self.post_repo.get_posts(page, limit, title, category_id)
        if not posts:
            raise HTTPException(status_code=404, detail="No posts found")
        
        posts = [post.__to_dict__() for post in posts]
        self.redis_client.set_with_ttl(key_, json.dumps(posts).encode('utf-8'), 20)
        return posts