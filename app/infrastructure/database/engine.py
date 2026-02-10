from sqlalchemy import create_engine
from app.config.settings import DBSettings

_engine = None


def get_engine():
    global _engine
    if _engine is None:
        settings = DBSettings()
        _engine = create_engine(settings.database_url, pool_pre_ping=True)
    return _engine
