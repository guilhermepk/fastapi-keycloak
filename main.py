from fastapi import FastAPI
from src.auth.auth_controller import router as auth_controller
from src.users.users_controller import router as users_controller

app = FastAPI()

app.include_router(auth_controller)
app.include_router(users_controller)