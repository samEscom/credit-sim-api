from sqlalchemy.orm import sessionmaker, Session
from app.infrastructure.database.engine import get_engine


_session = None


def get_session():
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=get_engine(),
        )
    return _SessionLocal


def get_db() -> Session:
    db = get_session()()
    try:
        yield db
    finally:
        db.close()
