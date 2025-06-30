import sqlalchemy as sa
from enum import Enum
from src.db import metadata


class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


transactions = sa.Table(
    "transactions",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("account_id", sa.Integer, sa.ForeignKey("accounts.id"), nullable=False),
    sa.Column(
        "type", sa.Enum(TransactionType, name="transaction_types"), nullable=False
    ),
    sa.Column("amount", sa.Numeric(10, 2), nullable=False),
    sa.Column("timestamp", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)
