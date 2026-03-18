import requests
from src.common.constants import KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET, KEYCLOAK_ISSUER
from src.keycloak.models.schemas.keycloak_tokens_schema import KeycloakTokensSchema

KEYCLOAK_TOKEN_URL: str = f"{KEYCLOAK_ISSUER}/protocol/openid-connect/token"

def refresh_session_use_case(
  refresh_token: str
) -> KeycloakTokensSchema:
  payload = {
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token,
    'client_id': KEYCLOAK_CLIENT_ID,
    'client_secret': KEYCLOAK_CLIENT_SECRET
  }

  response: KeycloakTokensSchema = requests.post(KEYCLOAK_TOKEN_URL, payload).json()

  return response