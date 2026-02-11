from authx import AuthX, AuthXConfig
from .config import settings

auth_config = AuthXConfig()
auth_config.JWT_SECRET_KEY = settings.jwt_secret_key
auth_config.JWT_ACCESS_COOKIE_NAME = settings.jwt_access_cookie_name
auth_config.JWT_TOKEN_LOCATION = settings.jwt_token_location

security = AuthX(config=auth_config)
