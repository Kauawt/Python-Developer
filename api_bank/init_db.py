import asyncio
from src.db import create_db_and_tables, engine, database


async def main():
    create_db_and_tables()
    await database.connect()
    await database.disconnect()
    print("Banco de dados inicializado com sucesso!")


if __name__ == "__main__":
    asyncio.run(main())
