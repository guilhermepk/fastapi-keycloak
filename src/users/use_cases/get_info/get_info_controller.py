from fastapi import APIRouter, Depends
from src.auth.guards.user_guard import user_guard

router = APIRouter()

@router.get('/users/me', dependencies=[Depends(user_guard)])
async def get_info():
    return 'usuario'