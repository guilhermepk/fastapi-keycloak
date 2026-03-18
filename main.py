from fastapi import FastAPI
from src.auth.auth_controller import router as auth_controller

app = FastAPI()

app.include_router(auth_controller)