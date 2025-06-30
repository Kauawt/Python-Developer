from fastapi import APIRouter, HTTPException, status

from src.schemas.auth import LoginIn
from src.schemas.user import UserCreate, UserOut
from src.security import sign_jwt, verify_password
from src.services.user import UserService

router = APIRouter(prefix="/auth")

user_service = UserService()


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate):
    user = await user_service.get_by_username(user_data.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with that username already exists",
        )
    return await user_service.create_user(user_data)


@router.post("/login")
async def login(data: LoginIn):
    user = await user_service.get_by_username(data.username)
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return sign_jwt(user_id=user.id)
