from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str
    description: str
    database_url: str
    secret: str
    first_superuser_email: EmailStr
    first_superuser_password: str

    class Config:
        env_file = '.env'


settings = Settings()
