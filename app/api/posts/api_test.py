from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from app.models.posts import Posts

router = APIRouter()

# test api
@router.get("", tags=["test"])
async def test():
    row = db.session.query(Posts).first()
    return row