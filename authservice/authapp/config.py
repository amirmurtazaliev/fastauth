from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #App
    app_name: str = "FastAuth"
    debug: bool = True
    cors_origins: list = ["*"]
    
    # Database
    db_host: str = Field(env="DB_HOST")
    db_port: int = Field(env="DB_PORT")
    db_name: str = Field(env="DB_NAME")
    db_user: str = Field(env="DB_USER")
    db_password: str = Field(env="DB_PASS")
    
    # JWT
    jwt_secret_key: str = Field(env="JWT_SECRET_KEY")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
    
    @property
    def get_database_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()