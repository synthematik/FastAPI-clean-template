
from fastapi import APIRouter, Depends, Response

from app.exception import *
from app.users.auth import authenticate, create_access_token, get_password_hash
from app.users.dependencies import get_current_user
from app.users.models import User
from app.users.schemas import SUserAuth
from app.users.service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/register/")
async def register_user(user_data: SUserAuth):
    existing_user = await UserService.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException()
    hashed_password = get_password_hash(user_data.password)
    await UserService.add_data(email=user_data.email, password=hashed_password)


@router.post("/login/")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate(email=user_data.email, password=user_data.password)
    if not user:
        raise UserIncorrectPasswordException()
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
    return {"message": "logged out"}


@router.get("/me/")
async def read_me(current_user: User = Depends(get_current_user)):
    return current_user
