import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.email_verify import emailver_router
from .routes.user import user_router
from .config import settings
from .models import *
from .database import init_db
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
app.include_router(emailver_router)

@app.get('/')
def root():
    return {
        "message": "Welcome to fastapi notification service!",
        "docs": "/docs"}
    
@app.post("/initdb")
async def initdb():
    return await init_db()

    
