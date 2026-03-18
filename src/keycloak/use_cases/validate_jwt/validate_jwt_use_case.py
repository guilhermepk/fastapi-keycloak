from jose import jwt, JWTError, ExpiredSignatureError
from src.keycloak.use_cases.get_jwks.get_jwks_use_case import get_jwks_use_case
from src.common.constants import KEYCLOAK_CLIENT_ID, KEYCLOAK_ISSUER
from src.common.models.exceptions.unauthorized_exception import UnauthorizedException
from src.keycloak.models.schemas.keycloak_tokens_schema import KeycloakTokensSchema

def validate_jwt_use_case(
  token: str,
) -> KeycloakTokensSchema:
  jwks = get_jwks_use_case()

  try:
    payload: KeycloakTokensSchema = jwt.decode(
      token = token,
      key = jwks,
      algorithms = ["RS256"],
      audience = KEYCLOAK_CLIENT_ID,
      issuer = KEYCLOAK_ISSUER
    )

    return payload
  except ExpiredSignatureError as error:
      raise UnauthorizedException(f"Token expirado: {str(error)}")
  
  except JWTError as error:
      raise UnauthorizedException(f"Token inválido: {str(error)}")
  except Exception as error:
    print('Erro ao validar token JWT', str(error))