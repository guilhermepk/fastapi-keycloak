from src.common.constants import KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET, KEYCLOAK_ISSUER
import requests

def keycloak_logout_use_case(
  refresh_token: str
) -> None:
  payload = {
    'client_id': KEYCLOAK_CLIENT_ID,
    'client_secret': KEYCLOAK_CLIENT_SECRET,
    'refresh_token': refresh_token
  }

  url: str = f"{KEYCLOAK_ISSUER}/protocol/openid-connect/logout"

  requests.post(url, payload)