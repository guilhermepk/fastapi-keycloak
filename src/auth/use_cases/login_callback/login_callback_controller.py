from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse
from src.keycloak.models.schemas.keycloak_tokens_schema import KeycloakTokensSchema
from src.common.constants import FRONTEND_URL, LOGIN_CALLBACK_ENDPOINT
from src.common.models.exceptions.unauthorized_exception import UnauthorizedException
from ..set_cookies.set_cookies_use_case import set_cookies_use_case
from src.keycloak.use_cases.exchange_keycloak_code_for_token.exchange_keycloak_code_for_token_use_case import exchange_keycloak_code_for_token

router = APIRouter()

@router.get(LOGIN_CALLBACK_ENDPOINT)
async def login_callback(
  code: str = Query(None),
  error: str = Query(None),
  error_description: str = Query(None),
  iss: str = Query(None),
):
  if not code:
    if error or error_description or iss:
      raise UnauthorizedException(f"Erro do Keycloak. error: {error} | error_description: {error_description} | iss: {iss}")

    raise UnauthorizedException("'code' ausente")

  tokens: KeycloakTokensSchema = await exchange_keycloak_code_for_token(code)

  response = RedirectResponse(
    url = FRONTEND_URL
  )

  return set_cookies_use_case(
    response = response,
    access_token = tokens.access_token,
    refresh_token = tokens.refresh_token,
    max_age = tokens.refresh_expires_in
  )