from fastapi import APIRouter
from backend.api.v1.endpoints import health
from backend.api.v1.endpoints import login

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["Healthcheck"])
api_router.include_router(login.router, prefix="/login", tags=["Login"])
