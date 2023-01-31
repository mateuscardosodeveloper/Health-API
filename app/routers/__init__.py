from fastapi import APIRouter

from routers import financial, user
from settings import settings

api = APIRouter()


api.include_router(router=user.router, prefix=settings.API_PREFIX, tags=["User"])
api.include_router(
    router=financial.router, prefix=settings.API_PREFIX, tags=["Financial"]
)
