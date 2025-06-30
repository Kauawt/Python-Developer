from databases.interfaces import Record

from src.db import database
from src.models.account import accounts
from src.models.user import users
from src.schemas.user import UserCreate
from src.security import get_password_hash
from typing import List


class UserService:
    async def create_user(self, user: UserCreate) -> Record:
        hashed_password = get_password_hash(user.password)
        user_command = users.insert().values(
            username=user.username, hashed_password=hashed_password
        )
        user_id = await database.execute(user_command)

        account_command = accounts.insert().values(user_id=user_id, balance=0)
        await database.execute(account_command)

        query = users.select().where(users.c.id == user_id)
        return await database.fetch_one(query)

    async def get_by_username(self, username: str) -> Record | None:
        query = users.select().where(users.c.username == username)
        return await database.fetch_one(query)

    async def get_by_id(self, user_id: int) -> Record | None:
        query = users.select().where(users.c.id == user_id)
        return await database.fetch_one(query)

    async def read_all(self, skip: int = 0, limit: int = 100) -> List[Record]:
        query = users.select().offset(skip).limit(limit)
        return await database.fetch_all(query)
