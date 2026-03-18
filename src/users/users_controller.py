from fastapi import APIRouter
from .use_cases.get_info.get_info_controller import router as get_info_controller

router = APIRouter()

router.include_router(get_info_controller)