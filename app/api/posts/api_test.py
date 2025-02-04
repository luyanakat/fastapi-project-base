from fastapi import APIRouter, Depends
from fastapi import Depends

test_router = APIRouter()

@test_router.get("", tags=["test"])
def test():
    return {"data": "OK!"}