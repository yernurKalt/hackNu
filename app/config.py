from pydantic import BaseSettings

class Settings(BaseSettings):
    HIGGSFIELD_API_BASE: str = "https://api.higgsfield.ai"
    HIGGSFIELD_API_KEY: str = ""
    HIGGSFIELD_WEBHOOK_SECRET: str = 
    class Config:
        env_file = ".env"

settings = Settings()
