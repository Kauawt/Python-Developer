from pydantic import BaseModel
from datetime import UTC, datetime


class PostIn(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False
