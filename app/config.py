from pydantic import BaseSettings

class Settings(BaseSettings):
    # ... existing fields ...
    HIGGSFIELD_API_BASE: str = "https://api.higgsfield.ai"
    HIGGSFIELD_API_KEY: str = "b04d8d09-b12c-4ccd-ba9f-f18d9c5691e0"
    HIGGSFIELD_WEBHOOK_SECRET: str = ""  # optional: if you enable webhooks
    class Config:
        env_file = ".env"

settings = Settings()