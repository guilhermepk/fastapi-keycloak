from typing import Literal
from fastapi import Response
from src.common.constants import PRODUCTION

def set_cookies_use_case(
  response: Response,
  access_token: str,
  refresh_token: str,
  max_age: int
):
  secure: bool = PRODUCTION
  same_site: Literal['strict', 'lax'] = 'strict' if PRODUCTION else 'lax'

  response.set_cookie(
      key = 'ACCESS_TOKEN',
      value = access_token,
      httponly = True,
      secure = secure,
      samesite = same_site,
      max_age = max_age
  )

  response.set_cookie(
      key = 'REFRESH_TOKEN',
      value = refresh_token,
      httponly = True,
      secure = secure,
      samesite = same_site,
      max_age = max_age
  )

  return response