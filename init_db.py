import asyncio

from tortoise import Tortoise


async def init():
    await Tortoise.init(
        db_url="postgres://localhost:5432/tortoise",
        modules={"models": ["myapp.models"]},
    )
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
