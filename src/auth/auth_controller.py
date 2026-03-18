from fastapi import APIRouter
from src.auth.use_cases.login.login_controller import router as login_controller

router = APIRouter()

router.include_router(login_controller)