from fastapi import Request, Response
from src.keycloak.use_cases.logout.keycloak_logout_use_case import keycloak_logout_use_case

def logout_use_case(
  request: Request,
  response: Response
) -> None:
  refresh_token: str = request.cookies.get('REFRESH_TOKEN', '')

  if refresh_token:
    keycloak_logout_use_case(refresh_token=refresh_token)

  response.delete_cookie('ACCESS_TOKEN')
  response.delete_cookie('REFRESH_TOKEN')