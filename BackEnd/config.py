from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_ENV: str = "dev"
    DATABASE_URL: str
    REDIS_URL: str

    HIGGSFIELD_BASE: str
    HIGGSFIELD_API_KEY: str
    HIGGSFIELD_SECRET: str

    S3_ENDPOINT: str
    S3_BUCKET: str
    S3_REGION: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
