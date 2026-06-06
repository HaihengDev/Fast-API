from app.core.config import settings

DATABASE_URL = (
  f"mysql+aiomysql://"
  f"{settings.DB_USER}:"
  f"{settings.DB_PASSWORD}@"
  f"{settings.DB_HOST}:"
  f"{settings.DB_PORT}/"
  f"{settings.DB_NAME}"
)