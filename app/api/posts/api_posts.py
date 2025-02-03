from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()

# test api
# @router.get("/test", tags=["test"])
# async def test():
#     return {"message": "Hello, FastAPI!"}