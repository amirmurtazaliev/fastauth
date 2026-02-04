import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.user import user_router
from .database import init_db
from .config import settings
from .models import *

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    docs_url="/api/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True
)

app.include_router(user_router)

@app.get('/')
def root():
    return {
        "message": "Welcome to fastapi notification service!",
        "docs": "/docs"}

    
