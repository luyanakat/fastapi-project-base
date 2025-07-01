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

    def get_posts(self, page: int, limit: int, title: str = None, category_id: int = None):
        query = self.session.query(Post)
        
        if title:
            query = query.filter(Post.title.ilike(f"%{title}%"))
        
        if category_id:
            query = query.filter(Post.category_id == category_id)

        query = query.order_by(Post.updated_at.desc())
        offset = (page - 1) * limit
        return query.offset(offset).limit(limit).all()
    
    
    def get_posts_count(self, title: str = None, category_id: int = None):
        query = self.session.query(Post)
        
        if title:
            query = query.filter(Post.title.ilike(f"%{title}%"))
        
        if category_id:
            query = query.filter(Post.category_id == category_id)

        return query.count()