from fastapi import HTTPException, status

class UnauthorizedException(HTTPException):
  def __init__(self, message: str):

    super().__init__(
      status_code = status.HTTP_401_UNAUTHORIZED,
      detail = message
    )