import json
from app.db.postgres import get_db
from app.db.redis import get_redis
from app.repository.post_repo import PostRepository
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi_sqlalchemy import db


class PostService(object):
    def __init__(self, db_session: Session = Depends(get_db)):
        self.post_repo = PostRepository(db_session)
        self.redis_client = get_redis()

    def get_post(self, post_id: int):
        res = self.redis_client.get_json(post_id)
        if res:
            return res

        post = self.post_repo.get_post_by_id(post_id)
    
        self.redis_client.set_with_ttl(post_id, post.__to_json_byte__(), 5)
        return post
    
    def create_post(self, post):
        return self.post_repo.create_post(post)