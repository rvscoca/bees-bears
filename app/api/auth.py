from fastapi import APIRouter, Form

from app.schemas.auth import Token, UserCreate, UserRead
from app.services.auth import AuthService

router = APIRouter(tags=["auth"], prefix="/auth")


@router.post("/register", response_model=UserRead, summary="Register a new user")
def register(payload: UserCreate):
    service = AuthService()
    user = service.register_user(payload)
    return user


@router.post("/login", response_model=Token, summary="Login and obtain an access token")
def login(username: str = Form(...), password: str = Form(...)):
    service = AuthService()
    token = service.login_user(username, password)
    return {"access_token": token, "token_type": "bearer"}
