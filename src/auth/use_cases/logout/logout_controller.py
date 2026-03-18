from fastapi import APIRouter, Depends, Request, Response
from src.auth.guards.user_guard import user_guard
from .logout_use_case import logout_use_case

router = APIRouter()

@router.get('/auth/logout', dependencies=[Depends(user_guard)])
def logout(
  request: Request,
  response: Response
):
  logout_use_case(
    request = request,
    response = response
  )

  return { 'message': 'Sessão encerrada' }