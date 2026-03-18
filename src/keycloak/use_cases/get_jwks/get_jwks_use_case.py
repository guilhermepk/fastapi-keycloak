from functools import lru_cache
import requests

from src.common.constants import KEYCLOAK_ISSUER

JWKS_URL: str = f"{KEYCLOAK_ISSUER}/protocol/openid-connect/certs"

@lru_cache()
def get_jwks_use_case():
  try:
    jwks = requests.get(JWKS_URL).json()
    return jwks
  except Exception as error:
    print('Erro ao buscar JWKS', str(error))