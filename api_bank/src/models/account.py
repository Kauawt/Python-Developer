import sqlalchemy as sa

from src.db import metadata
from src.models.user import users

accounts = sa.Table(
    "accounts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column(
        "user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True
    ),
    sa.Column("balance", sa.Numeric(10, 2), nullable=False, default=0),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)
