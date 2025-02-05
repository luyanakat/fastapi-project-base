from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session

from app.models.posts import Post


class PostRepository:
    def __init__(self, session: Session):
        self.session = session

    
    def get_post_by_id(self, post_id: int):
        return self.session.query(Post).filter(Post.id == post_id).first()
    
    def create_post(self, post):
        self.session.add(post)
        self.session.commit()
        return post
