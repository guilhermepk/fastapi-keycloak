from os import getenv
from dotenv import load_dotenv

load_dotenv()

KEYCLOAK_URL: str = getenv('KEYCLOAK_URL', '')
KEYCLOAK_REALM: str = getenv('KEYCLOAK_REALM', '')
KEYCLOAK_CLIENT_ID: str = getenv('KEYCLOAK_CLIENT_ID', '')
KEYCLOAK_CLIENT_SECRET: str = getenv('KEYCLOAK_CLIENT_SECRET', '')

KEYCLOAK_AUTH_URL: str = f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/auth"
KEYCLOAK_ISSUER: str = f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}"

API_URL: str = getenv('API_URL', '')

LOGIN_CALLBACK_ENDPOINT: str = "/auth/successful-login-callback"
LOGIN_CALLBACK_REDIRECT_URI: str = f"{API_URL}{LOGIN_CALLBACK_ENDPOINT}"

FRONTEND_URL: str = getenv('FRONTEND_URL', '')

PRODUCTION: bool = getenv('PRODUCTION') == 'True'

CORS_WHITELIST: list[str] = getenv('CORS_WHITELIST', '').split(', ')