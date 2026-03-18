from fastapi import Request, Response
from src.keycloak.use_cases.validate_jwt.validate_jwt_use_case import validate_jwt_use_case
from src.common.models.exceptions.unauthorized_exception import UnauthorizedException
from src.keycloak.use_cases.refresh_session.refresh_session_use_case import refresh_session_use_case
from src.keycloak.models.schemas.keycloak_tokens_schema import KeycloakTokensSchema
from src.auth.use_cases.set_cookies.set_cookies_use_case import set_cookies_use_case

def user_guard(
  request: Request,
  response: Response
) -> bool:
  access_token = request.cookies.get('ACCESS_TOKEN')

  if not access_token:
    raise UnauthorizedException("Token não informado")
  else:
    try:
      validate_jwt_use_case(access_token)
    except UnauthorizedException as error:
      refresh_token = request.cookies.get('REFRESH_TOKEN')

      if not refresh_token:
        raise error

      refresh_data: KeycloakTokensSchema = refresh_session_use_case(refresh_token)

      set_cookies_use_case(
        response = response,
        access_token = refresh_data.access_token,
        refresh_token = refresh_data.refresh_token,
        max_age = refresh_data.refresh_expires_in
      )
  
  return True