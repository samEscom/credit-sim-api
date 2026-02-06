from sqlalchemy import create_engine
from app.config.settings import DBSettings

settings = DBSettings()
engine = create_engine(settings.database_url)
