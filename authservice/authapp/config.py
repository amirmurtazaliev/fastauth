from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #App
    app_name: str = "FastAuth"
    debug: bool = True
    cors_origins: list = ["*"]
    
    # Database
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_pass: str
    
    # JWT
    jwt_secret_key: str
    jwt_access_cookie_name: str
    jwt_token_location: list
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
    
    @property
    def get_database_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()