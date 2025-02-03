from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session

from app.models.posts import Posts


class PostRepository:
    def __init__(self, session: Session):
        self.session = session

    
    def get_post_by_id(self, post_id: int):
        return self.session.query(Posts).filter(Posts.id == post_id).first()
    


