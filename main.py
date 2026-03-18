from fastapi import FastAPI
from src.auth.auth_controller import router as auth_controller
from src.users.users_controller import router as users_controller
from fastapi.middleware.cors import CORSMiddleware
from src.common.constants import CORS_WHITELIST

app = FastAPI()

app.include_router(auth_controller)
app.include_router(users_controller)

app.add_middleware(
    CORSMiddleware,
    allow_origins = CORS_WHITELIST,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)