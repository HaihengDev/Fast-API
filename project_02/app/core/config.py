from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  DB_HOST: str
  DB_PORT: int
  DB_USER: str
  DB_PASSWORD: str
  DB_NAME: str

  model_config = {
    "env_file": ".env"
  }

settings = Settings()