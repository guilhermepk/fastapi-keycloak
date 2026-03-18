from fastapi import APIRouter
from src.auth.use_cases.login.login_controller import router as login_controller
from .use_cases.login_callback.login_callback_controller import router as login_callback_controller
from .use_cases.logout.logout_controller import router as logout_controller

router = APIRouter()

router.include_router(login_controller)
router.include_router(login_callback_controller)
router.include_router(logout_controller)