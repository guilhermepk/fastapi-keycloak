from src.common.constants import KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET, KEYCLOAK_ISSUER, LOGIN_CALLBACK_REDIRECT_URI
import requests
from src.keycloak.models.schemas.keycloak_tokens_schema import KeycloakTokensSchema

KEYCLOAK_TOKEN_URL: str = f"{KEYCLOAK_ISSUER}/protocol/openid-connect/token"

async def exchange_keycloak_code_for_token(
  keycloak_code: str
) -> KeycloakTokensSchema :
  payload = {
    'grant_type': 'authorization_code',
    'code': keycloak_code,
    'client_id': KEYCLOAK_CLIENT_ID,
    'client_secret': KEYCLOAK_CLIENT_SECRET,
    'redirect_uri': LOGIN_CALLBACK_REDIRECT_URI
  }

  response = requests.post(KEYCLOAK_TOKEN_URL, data=payload)
  data = response.json()
  return data