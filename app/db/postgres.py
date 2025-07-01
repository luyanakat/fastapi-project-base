from app.core.config import build_db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(build_db_url(), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()