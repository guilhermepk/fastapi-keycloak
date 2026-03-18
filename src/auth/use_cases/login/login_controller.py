from fastapi import APIRouter
from common.constants import KEYCLOAK_AUTH_URL, KEYCLOAK_CLIENT_ID, LOGIN_CALLBACK_REDIRECT_URI
from urllib.parse import urlencode
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get('/auth/login')
def login():
  params = {
    "scope": "openid profile",
    "client_id": KEYCLOAK_CLIENT_ID,
    "response_type": "code",
    "redirect_uri": LOGIN_CALLBACK_REDIRECT_URI,
    "prompt": "login"
  }

  target_url = f"{KEYCLOAK_AUTH_URL}?{urlencode(params)}"

  return RedirectResponse(url=target_url)