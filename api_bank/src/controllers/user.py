from fastapi import APIRouter, Depends
from typing import List
from src.schemas.user import UserOut
from src.services.user import UserService
from src.security import login_required

router = APIRouter(prefix="/users")

user_service = UserService()


@router.get("/", response_model=List[UserOut], dependencies=[Depends(login_required)])
async def get_users(skip: int = 0, limit: int = 100):
    return await user_service.read_all(skip=skip, limit=limit)
