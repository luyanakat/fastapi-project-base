from app.db.postgres import get_db
from app.repository.post_repo import PostRepository
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi_sqlalchemy import db

class PostService(object):
    def __init__(self, db: Session = Depends(get_db)):
        self.post_repo = PostRepository(db)

    def get_post(self, post_id: int):
        return self.post_repo.get_post_by_id(post_id)
    
    def create_post(self, post):
        return self.post_repo.create_post(post)