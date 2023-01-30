from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import api
from settings import settings, pyproject


app = FastAPI(
    title=pyproject.PROJECT_NAME,
    description=pyproject.PROJECT_DESCRIPTION,
    version=pyproject.PROJECT_VERSION,
    debug=settings.DEBUG,
    docs_url=f'{settings.API_PREFIX}/docs',
    redoc_url=f'{settings.API_PREFIX}/redoc',
    openapi_url=f'{settings.API_PREFIX}/openapi.json',
    root_path=None
)


app.add_middleware(
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    middleware_class=CORSMiddleware,
)


app.include_router(api, prefix='/api')
