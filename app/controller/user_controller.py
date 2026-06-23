from fastapi import APIRouter
from fastapi import Depends
from typing import List

from sqlalchemy.orm import Session

from app.dao.db_session import get_db
from app.schemas.user_create import UserCreate
from app.schemas.user_response import UserResponse
from app.service.user_service import UserService


router=APIRouter()

user_service = UserService()

@router.post("/users")
def create_user(
    user_request:UserCreate,
    db:Session= Depends(get_db)
):
    return user_service.create_user(
        db,
        user_request=user_request
    )

@router.get("/get_all_users",response_model=List[UserResponse])
def get_all_users(
    db:Session=Depends(get_db)
):
    return user_service.get_all_users(
        db
    )



