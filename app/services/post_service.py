from app.db.postgres import get_db
from app.repository.post_repo import PostRepository
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi_sqlalchemy import db

class PostService(object):
    PostRepo = PostRepository(Depends(get_db))

    @staticmethod
    def get_post(post_id: int):
        return PostRepository.get_post_by_id(post_id)