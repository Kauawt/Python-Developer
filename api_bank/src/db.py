import databases
import sqlalchemy as sa
from src.config import settings
from src.db_base import metadata
from src.models import user, account, transaction

database = databases.Database(settings.database_url)

if settings.environment == "production":
    engine = sa.create_engine(settings.database_url)
else:
    engine = sa.create_engine(
        settings.database_url, connect_args={"check_same_thread": False}
    )


def create_db_and_tables():
    metadata.create_all(engine)
