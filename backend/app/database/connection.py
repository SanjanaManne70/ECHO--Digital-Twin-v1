from sqlalchemy import create_engine

from app.core.config import settings

engine = create_engine(
    settings.sqlalchemy_database_url,
    echo=settings.debug,
    future=True,
)
