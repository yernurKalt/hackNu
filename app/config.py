from pydantic import BaseSettings

class Settings(BaseSettings):
    HIGGSFIELD_API_BASE: str = "https://api.higgsfield.ai"
    HIGGSFIELD_API_KEY: str = "b04d8d09-b12c-4ccd-ba9f-f18d9c5691e0"
    HIGGSFIELD_WEBHOOK_SECRET: str = "73ae245d0dc69d143d9e0385b4c8c2ccbbed7867e2f0832a26abd302d71bcf0f"
    class Config:
        env_file = ".env"

settings = Settings()
