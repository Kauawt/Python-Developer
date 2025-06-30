import sqlalchemy as sa
from src.db import metadata

users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("username", sa.String(255), nullable=False, unique=True),
    sa.Column("hashed_password", sa.String(255), nullable=False),
    sa.Column(
        "created_dt", sa.TIMESTAMP(timezone=True), default=sa.func.now(), nullable=False
    ),
)
