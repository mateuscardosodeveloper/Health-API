from fastapi import APIRouter

from settings import settings
from routers import financial
from routers import user


api = APIRouter()


api.include_router(router=user.router, prefix=settings.API_PREFIX, tags=['User'])
api.include_router(router=financial.router, prefix=settings.API_PREFIX, tags=['Financial'])
