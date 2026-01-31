from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..config import settings
from .routes.user import user_router

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    docs_url="/api/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credential=True
)

app.include_router(user_router)